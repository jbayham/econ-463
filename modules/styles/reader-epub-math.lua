local dpi = 240
local pixels_per_em = 10 * dpi / 72.27

local function equation_key(math)
  return math.mathtype .. ":" .. math.text
end

local function render_equations(equations)
  local tex = assert(io.open("equations.tex", "w"))
  tex:write([[
\documentclass[10pt]{article}
\usepackage{amsmath,amssymb}
\usepackage[active,tightpage]{preview}
\setlength{\PreviewBorder}{0.4pt}
\begin{document}
]])
  for _, equation in ipairs(equations) do
    local math_style = equation.mathtype == "DisplayMath" and [[\displaystyle ]] or ""
    tex:write("\\begin{preview}\n\\(", math_style, equation.text, "\\)\n\\end{preview}\n")
  end
  tex:write("\\end{document}\n")
  tex:close()

  pandoc.pipe("latex", {"-no-shell-escape", "-halt-on-error", "-interaction=nonstopmode", "equations.tex"}, "")
  local output = pandoc.pipe("dvipng", {
    "-T", "tight", "-D", tostring(dpi), "-bg", "White", "--depth", "--width",
    "-o", "equation-%d.png", "equations.dvi"
  }, "")

  local images = {}
  for page, depth, width in output:gmatch("%[(%d+)[^%]]-depth=(%-?%d+) width=(%d+)%]") do
    local filename = "equation-" .. page .. ".png"
    local png = assert(io.open(filename, "rb"))
    pandoc.mediabag.insert(filename, "image/png", png:read("*a"))
    png:close()
    images[tonumber(page)] = {
      filename = filename,
      width = tonumber(width) / pixels_per_em,
      depth = tonumber(depth) / pixels_per_em
    }
  end
  return images
end

function Pandoc(doc)
  local equations, indices = {}, {}
  doc:walk({
    Math = function(math)
      local key = equation_key(math)
      if not indices[key] then
        equations[#equations + 1] = math
        indices[key] = #equations
      end
    end
  })
  if #equations == 0 then
    return doc
  end

  local images = pandoc.system.with_temporary_directory("reader-equations", function(path)
    return pandoc.system.with_working_directory(path, function()
      return render_equations(equations)
    end)
  end)

  return doc:walk({
    Math = function(math)
      local index = indices[equation_key(math)]
      local image = assert(images[index], "Missing rendered equation: " .. math.text)
      local classes = {}
      local style = ("width: %.3fem;"):format(image.width)
      if math.mathtype == "DisplayMath" then
        classes[1] = "equation-display"
      else
        style = style .. (" vertical-align: %.3fem;"):format(-image.depth)
      end
      local element = pandoc.Image({pandoc.Str(math.text)}, image.filename, "", pandoc.Attr("", classes, {style = style}))
      if math.mathtype == "DisplayMath" then
        -- Keep Quarto from treating a standalone equation as a captioned figure.
        return pandoc.Span({element})
      end
      return element
    end
  })
end
