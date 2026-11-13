---
title: "ECON 463: Regional Economics"
layout: page
permalink: /syllabus/
format:
  pdf:
    pdf-engine: xelatex
    fontsize: 10pt
    geometry: margin=0.85in
---


## Course Information

| Item              | Details                                                                  |
| ----------------- | ------------------------------------------------------------------------ |
| Course            | ECON 463: Regional Economics                                             |
| Term and location | November 23-December 18, 2026; Foreign Trade University, Hanoi, Vietnam. |
| Instructor        | Jude Bayham                                                              |
| Email             | [jbayham@colostate.edu](mailto:jbayham@colostate.edu)                    |
| Exams             | Friday, December 4, and Friday, December 18                              |

### Sections and Meeting Times

| Section | Class code             | Time            |
| ------- | ---------------------- | --------------- |
| 1 - K63 | ECON463(2627-HK1)GD2.1 | 9:20-11:30 a.m. |
| 2 - K63 | ECON463(2627-HK1)GD2.2 | 12:30-2:40 p.m. |

### Meeting Rooms

| Day       | Section 1 | Section 2 |
| --------- | --------- | --------- |
| Monday    | A705      | H202      |
| Tuesday   | A705      | H302      |
| Wednesday | A703      | H206      |
| Thursday  | A1203     | H206      |
| Friday    | H302      | A703      |

**Meeting rooms may change.** Check course announcements for room updates. There is no class on November 24.

## Course Description

Why do cities exist, why do firms cluster, and why do some regions grow while others decline? This course uses economic theory, regional data, and quantitative models to investigate these questions. Topics include location, agglomeration, regional growth, trade and migration, land use, spatial equilibrium, and the valuation of amenities through housing markets. Students will use R to describe regional economies, estimate hedonic relationships, and conduct input-output and computable general equilibrium (CGE) calculations with supplied data and model structures. Applications emphasize how assumptions shape estimated impacts and how those impacts relate to welfare, environmental externalities, and distribution.

## Learning Outcomes

By the end of the course, students will be able to:

1. **LO1.** Explain how transportation costs, scale economies, and natural advantages shape the location of economic activity and the formation of cities.

2. **LO2.** Analyze how shared suppliers, labor markets, and knowledge spillovers encourage firms to cluster, and how congestion and other costs limit concentration.

3. **LO3.** Compare explanations for regional growth and decline, and explain how industrial specialization, productivity, market access, trade, and migration transmit economic changes across regions.

4. **LO4.** Explain how household and firm location choices jointly determine wages, rents, and population across places; estimate hedonic models in R to examine how amenities and other location characteristics are reflected in property values, and assess how sorting and omitted variables limit interpretation.

5. **LO5.** Define an appropriate regional unit and use data with comparable geographic boundaries, years, and sector definitions in R to measure industrial structure, specialization, and economic change.

6. **LO6.** Use supplied data and model structures to conduct input-output and computable general equilibrium (CGE) calculations in R and estimate regional economic impacts; compare how trade leakages, resource constraints, price adjustment, and factor mobility shape the models' results.

7. **LO7.** Apply regional theory and models to a real-world problem using an explicit baseline and counterfactual.

## Preparation and Course Tools

The course is designed for undergraduate students with intermediate microeconomic preparation. Basic statistics, regression interpretation, and familiarity with R will support the applied work.

We will use R for data analysis, estimation, and model calculations. Data, model structures, and starter code will be supplied; students are responsible for understanding the calculations and interpreting results. Guided work will occur in class. Computer access arrangements are to be confirmed before the first data exercise.

## Materials and Reading

I will share course materials via a Github website: <https://jbayham.github.io/econ-463/>. The material will be organized into modules containing slides, student readers, prepared datasets, and model handouts to support the class.

The main reference texts are:

- Brueckner, J. K. (2011). [*Lectures on urban economics*](https://mitpress.mit.edu/9780262300315/lectures-on-urban-economics/). MIT Press.
- Hoover, E. M., & Giarratani, F. (1999). [*An introduction to regional economics*](https://researchrepository.wvu.edu/rri-web-book/4/) (4th web ed., updated 2020; S. Loveridge & R. Jackson, Eds.). Regional Research Institute, West Virginia University.
- Schaffer, W. A. (1999). [*Regional impact models*](https://researchrepository.wvu.edu/rri-web-book/7/) (2nd ed., updated 2020; S. Loveridge & R. Jackson, Eds.). Regional Research Institute, West Virginia University.
- Hewings, G. J. D. (1985). [*Regional input-output analysis*](https://researchrepository.wvu.edu/rri-web-book/10/). SAGE Publications. (Web reprint edited by G. I. Thrall, Regional Research Institute, West Virginia University, 2020.)
- Hall, J., Lawson, K., & Shia, J. (Eds.). (2021). [*Measuring amenities and disamenities in the housing market: Applications of the hedonic method*](https://researchrepository.wvu.edu/rri-web-book/32/). Regional Research Institute, West Virginia University.

## Class Format and Expectations

Class meetings combine explanation, discussion, worked examples, and supported problem solving or data analysis. Students should participate in guided practice and bring questions about methods and assumptions. I’ll expect some work outside of class.


## Assessment and Grading

The course has four problem sets and two exams. Problem sets assess the ability to use tools and explain results. Exams assess economic reasoning, assumptions, and interpretation.

| Component                             | Focus                                                                                       | Points  |
| ------------------------------------- | ------------------------------------------------------------------------------------------- | ------: |
| PS 1: Location and regional structure   | Location calculations, agglomeration/growth reasoning, and a regional profile in R.         | 7.5     |
| PS 2: Spatial equilibrium and amenities | Spatial adjustment and hedonic estimation/interpretation in R.                              | 7.5     |
| PS 3: Input-output analysis             | Accounts, coefficients, model solution, a demand shock, and sensitivity.                    | 7.5     |
| PS 4: CGE and model comparison          | Baseline replication, one shock, one sensitivity comparison, and a bounded policy question. | 7.5     |
| Exam 1                                | Modules 1-5                                                                                 | 35      |
| Final exam                            | Modules 6-8                                                                                 | 35      |
| **Total**                             |                                                                                             | **100** |

### Exams

You will have the full class period for exams. Exam 1 is scheduled for **Friday, December 4** and covers regional foundations, measurement, spatial equilibrium, and hedonics. The **final is Friday, December 18**, emphasizing IO, CGE, and policy interpretation.

## Course Topics by Module

### Module 1: Location, Cities, and Agglomeration

- Natural advantages, transportation costs, scale economies, and city formation.
- Firm location, shared suppliers, labor pooling, knowledge spillovers, and the costs of concentration.

### Module 2: Regional Growth and Interregional Connections

- Regional growth and decline, productivity, specialization, structural change, and convergence.
- Market access, trade costs, migration, and the transmission of economic changes across regions.

### Module 3: Defining and Measuring a Regional Economy

- Administrative and functional regions; geographic, temporal, and sector comparability.
- Regional data analysis in R, location quotients, shift-share, and regional profiles.

### Module 4: Land Use and Spatial Equilibrium

- Bid rents, commuting, housing supply, and land-use constraints.
- Wages, rents, amenities, mobility, capitalization, and population adjustment across places.

### Module 5: Hedonics and Interpretation of Spatial Evidence

- Hedonic models of property values and amenities; estimation and interpretation in R.
- Sorting, omitted variables, specification comparisons, and limits to causal and welfare interpretation.

### Module 6: Input-Output Analysis and Regional Linkages

- Regional accounts, technical coefficients, the Leontief inverse, and demand shocks.
- Direct, indirect, and induced effects; imports and leakages; output, value added, income, and employment.
- Model assumptions, sensitivity, and interpretation of regional impacts.

### Module 7: Regional CGE Modeling and Model Comparison

- Social accounting, household and firm behavior, market clearing, and baseline replication.
- Closure, regional trade, factor mobility, substitution, prices, and resource constraints.
- Counterfactual calculations in R, sensitivity analysis, and comparison with input-output results.

### Module 8: Regional Application and Policy Evaluation

- Defining a baseline and counterfactual and selecting an appropriate regional model.
- Economic impacts, welfare, opportunity costs, externalities, distribution, and model limitations.
- Communicating findings and evaluating regional policy claims.

## Academic Work and Course Policies

Students are responsible for the accuracy of submitted calculations, code, claims, and interpretations. You may use AI tools to help with understanding course materials. I suggest you try to avoid using them on problem sets because it will undermine your ability to answer exam questions.
