# 📦 其他研究 | 2026年05月13日

> 本类共 **396** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-396](./part-08.md)

---

### 51. [Deep Learning for Protein Complex Prediction and Design](https://arxiv.org/abs/2605.11189)

**<font color=#1a73e8>作者：</font>** Ziwei Xie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurately modeling and designing protein complex structures is a central problem in computational structural biology, with broad implications for understanding cellular function and developing therapeutics. This thesis investigates two fundamental aspects of this problem using deep learning: domain-specific architectures that capture the hierarchical nature of protein structures, and search algorithms that efficiently navigate the vast sequence spaces of protein complexes to identify interacting homologs for improving complex structure prediction and to design protein sequences.

---


### 52. [Variational Linear Attention: Stable Associative Memory for Long-Context Transformers](https://arxiv.org/abs/2605.11196)

**<font color=#1a73e8>作者：</font>** Vishal Pandey, Gopal Singh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear attention reduces the quadratic cost of softmax attention to $\mathcal{O}(T)$, but its memory state grows as $\mathcal{O}(T)$ in Frobenius norm, causing progressive interference between stored associations. We introduce \textbf{Variational Linear Attention} (VLA), which reframes the memory update as an online regularised least-squares problem with an adaptive penalty matrix maintained via the Sherman-Morrison rank-1 formula. We prove that normalising the write direction to unit length gives the recurrence Jacobian spectral norm exactly $1$ for all sequence lengths and head dimensions (Proposition 2), and that the state norm is self-limiting under bounded inputs (Proposition 1). Empirically, VLA reduces $\|S_t\|_F$ by $109\times$ relative to standard linear attention at $T{=}1{,}000$, achieves near-perfect exact-match accuracy on multi-query associative recall within the effective per-head memory regime ($n_\text{pairs} < d_h$), maintaining substantially higher retrieval performance than DeltaNet and standard linear attention under increasing memory load, and maintains 62\% accuracy at the per-head capacity boundary. A Triton-fused kernel achieves $14\times$ speedup over sequential Python and $\mathcal{O}(T)$ scaling, crossing below softmax attention latency at approximately 43\,000 tokens.

---


### 53. [FeatMap: Understanding image manipulation in the feature space and its implications for feature space geometry](https://arxiv.org/abs/2605.11203)

**<font color=#1a73e8>作者：</font>** Elias B. Krey, Nils Neukirch, Nils Strodthoff  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Intermediate feature representations represent the backbone for the expressivity and adaptability of deep neural networks. However, their geometric structure remains poorly understood. In this submission, we provide indirect insights into this matter by applying a broad selection of manipulations in input space, ranging from geometric and photometric transformations to local masking and semantic manipulations using generative image editing models, and assess the feasibility of learning a mapping in the feature space, mapping from the original to the manipulated feature map. To this end, we devise different types of mappings, from linear to non-linear and local to global mappings and assess both the reconstruction quality of the mapping as well as the semantic content of the mapped representations. We demonstrate the feasibility of learning such mappings for all considered transformations. While global (transformer) models that operate on the full feature map often achieve best results, we show that the same can be achieved with a shared linear model operating on a single feature vector typically with very little degradation in reconstruction quality, even for highly non-trivial semantic manipulations. We analyze the corresponding mappings across different feature layers and characterize them according to dominance of weight vs. bias and the effective rank of the linear transformations. These results provide hints for the hypothesis that the feature space is to a first degree of approximation organized in linear structures. From a broader perspective, the study demonstrates that generative image editing models might open the door to a deeper understanding of the feature space through input manipulation.

---


### 54. [Instructions shape Production of Language, not Processing](https://arxiv.org/abs/2605.11206)

**<font color=#1a73e8>作者：</font>** Andreas Waldis, Leshem Choshen, Yufang Hou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Instructions trigger a production-centered mechanism in language models. Through a cognitively inspired lens that separates language processing and production, we reveal this mechanism as an asymmetry between the two stages by probing task-specific information layer-wise across five binary judgment tasks. Specifically, we measure how instruction tokens shape information both when sample tokens, the input under evaluation, are processed and when output tokens are produced. Across prompting variations, task-specific information in sample tokens remains largely stable and correlates only weakly with behavior, whereas the same information in output tokens varies substantially and correlates strongly with behavior. Attention-based interventions confirm this pattern causally: blocking instruction flow to all subsequent tokens reduces both behavior and information in output tokens, whereas blocking it only to sample tokens has minimal effect on either. The asymmetry generalizes across model families and tasks, and becomes sharper with model scale and instruction-tuning, both of which disproportionately affect the production stage. Our findings suggest that understanding model capabilities requires jointly assessing internals and behavior, while decomposing the internal perspective by token position to distinguish the processing of input tokens from the production of output tokens.

---


### 55. [Enforcing Constraints in Generative Sampling via Adaptive Correction Scheduling](https://arxiv.org/abs/2605.11214)

**<font color=#1a73e8>作者：</font>** Noah Trupin, Yexiang Xue  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hard constraints in generative sampling are typically enforced by projection, applied either once at the end of sampling or after every update. This binary framing overlooks a fundamental issue: projection changes the distribution of states which future updates depend on. As a result, delayed projection can produce samples that are feasible but inconsistent with the intended sampling dynamics, even after final projection. We formalize constraint enforcement as a correction scheduling problem over the generative rollout. Using one-step constraint defect as a local signal of geometric mismatch, we introduce adaptive correction scheduling, a state-dependent policy that allocates projection budget to the steps that most strongly perturb the trajectory. Terminal and stepwise projection arise as limiting cases of this family. Across controlled manifold rollouts and a learned projected diffusion sampler, adaptive scheduling improves the cost-accuracy frontier at matched projection budgets, recovering 71.2% of full stepwise benefit with 75% fewer corrections. These results show that constraint timing is a first-class design variable in generative sampling, and that enforcing feasibility alone is insufficient to preserve the intended constrained sampling dynamics.

---


### 56. [Don't Look at the Numbers: Visual Anchoring Bias and Layer-wise Representation in VLMs](https://arxiv.org/abs/2605.11218)

**<font color=#1a73e8>作者：</font>** M. Shalankin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Embedded numeric anchors on images systematically bias Vision-Language Model quality judgments across six VLMs from five architectural families (ANOVA eta^2 = 0.18-0.77, all p < 0.001). Anchor effects are 2.5x larger than severe image quality degradation, confirming bias is not reducible to visual changes. Layer-wise probing reveals consistent dissociation: layers where anchor classification saturates (L12-L34) are suboptimal for quality prediction, with optimal layers deeper (R^2 = 0.69-0.91). Fusion analysis identifies architecture-dependent integration -- instant fusion at L1-L2 in two models versus partial or no fusion in three others. These results establish a causal account of visual anchoring bias, linking behavioral susceptibility to representation dynamics.

---


### 57. [Do Vision-Language-Models show human-like logical problem-solving capability in point and click puzzle games?](https://arxiv.org/abs/2605.11223)

**<font color=#1a73e8>作者：</font>** Dominik Helfenstein, Marco Menner, Maximilian Triebel  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language(-Action) Models (VLMs) are increasingly applied to interactive environments, yet existing benchmarks often overlook the complex physical reasoning required for point-and-click puzzle games. This paper introduces Vision-Language Against The Incredible Machine (VLATIM), a benchmark designed to evaluate human-like logical problem-solving capabilities within the classic physics puzzle game The Incredible Machine 2 (TIM). Unlike existing benchmarks, VLATIM specifically targets the critical gap between high-level logical reasoning and continuous action spaces requiring precise mouse interactions. This benchmark is structured into five progressive parts, assessing capabilities that range from basic visual grounding and domain understanding to multi-step manipulation and full puzzle solving. Our results reveal a significant disparity between reasoning and execution. While large proprietary models demonstrate superior planning abilities, they struggle with precise visual grounding. Consequently, they do not yet show human-like problem-solving capabilities.

---


### 58. [ABRA: Agent Benchmark for Radiology Applications](https://arxiv.org/abs/2605.11224)

**<font color=#1a73e8>作者：</font>** Bulat Maksudov, Vladislav Kurenkov, Kathleen M. Curran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing medical-agent benchmarks deliver imaging as pre-selected samples, never as an environment the agent must navigate. We introduce ABRA, a radiology-agent benchmark in which the agent operates an OHIF viewer and an Orthanc DICOM server through twenty-one function-calling tools that span slice navigation, windowing, series selection, pixel-coordinate annotation, and structured reporting. ABRA contains 655 programmatically generated tasks across three difficulty tiers and eight types (viewer control, metadata QA, vision probe, annotation, longitudinal comparison, BI-RADS reporting, and oracle variants of annotation and BI-RADS reporting), drawn from LIDC-IDRI, Duke Breast Cancer MRI, and NLST New-Lesion LongCT. Each episode is scored along Planning, Execution, and Outcome (Bluethgen et al., 2025) by task-type-specific automatic scorers. Ten current models, five closed-weight and five open-weight, reach at least 89% Execution on real annotation but only 0-25% Outcome; on the paired oracle variant where a simulated detector supplies the finding, Outcome on the same task reaches 69-100% across the models evaluated, localising the bottleneck to perception rather than tool orchestration. Code, task generators, and scorers are released at this https URL

---


### 59. [LiBaGS: Lightweight Boundary Gap Synthesis for Targeted Synthetic Data Selection](https://arxiv.org/abs/2605.11231)

**<font color=#1a73e8>作者：</font>** Abhishek Moturu, Anna Goldenberg, Babak Taati  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synthetic data is useful only when the added samples fill missing parts of the training distribution that matter for the downstream task. We introduce LiBaGS, a lightweight, generator-agnostic method for targeted synthetic training data selection. LiBaGS scores candidate synthetic samples by combining decision-boundary proximity, predictive uncertainty, real-data density, and support validity, so that selected samples are both informative and likely to remain on the real data manifold. We then use a boundary-gap allocation rule that targets sparse but realistic decision-boundary neighborhoods, rather than simply adding more data or selecting only the most uncertain candidates. LiBaGS also learns when enough synthetic samples have been added through a marginal-value stopping rule, assigns softer labels near ambiguous boundaries, and uses a diversity objective to avoid redundant near-duplicate selections. Experiments show that LiBaGS improves accuracy over classical oversampling, hard augmentation, uncertainty and density ablations, and targeted-generation selection criteria.

---


### 60. [A Comparative Study of Model Selection Criteria for Symbolic Regression](https://arxiv.org/abs/2605.11233)

**<font color=#1a73e8>作者：</font>** Ali Soltani, Gabriel Kronberger, Fabricio Olivetti de Franca 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Effective model selection is critical in symbolic regression (SR) to identify mathematical expressions that balance accuracy and complexity, and have low expected error on unseen data. Many modern implementations of genetic programming (GP) for SR generate a set of Pareto optimal candidate solutions, but reliable automatic selection of solutions that generalize well remains an open issue. Current literature offers various information-theoretic and Bayesian approaches, yet comprehensive comparisons of their performance across different data regimes are limited. This study presents a systematic empirical comparison of widely used selection criteria: the Akaike information criterion (AIC), the corrected AIC (AICc), the Bayesian information criterion (BIC), minimum description length (MDL), as well as Efron's bootstrap estimate for the in-sample prediction error on seven synthetic datasets with Gaussian noise. We rank candidate expressions generated by perturbing ground-truth functions to assess generalization error and selection probability of the ground-truth expression. Our findings reveal that MDL consistently identifies models with the lowest test error and the shortest length across most datasets. While no single criterion dominates all results, MDL and BIC produced the highest probability of selecting the ground-truth expressions.

---


### 61. [DeconDTN-Toolkit: A Library for Evaluation and Enhancement of Robustness to Provenance Shift](https://arxiv.org/abs/2605.11237)

**<font color=#1a73e8>作者：</font>** Yongsen Tan, Zhecheng Sheng, Xiruo Ding 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite the burgeoning body of work on distribution shifts, provenance shift-where the relationship between data source and label changes at deployment-remains poorly understood and under-addressed. In this paper, we establish a formal connection between provenance shift, counterfactual invariance, and invariant learning to derive a learning objective for robustness. We then introduce \textsc{DeconDTN-Toolkit}, a specialized evaluation and remediation suite designed to simulate provenance shifts of varying degrees while maintaining the training protocol and the infrastructure of existing benchmarks. We reveal the vulnerability of Empirical Risk Minimization under provenance shift, introduce a robust out-of-distribution performance indicator, and conduct a comprehensive evaluation on existing algorithms. Our work provides both the theoretical grounding and the practical tools necessary to characterize the problem of confounding by provenance, and implementations of methods to mitigate it.

---


### 62. [Extending Kernel Trick to Influence Functions](https://arxiv.org/abs/2605.11239)

**<font color=#1a73e8>作者：</font>** Zhenhuan Sun, Shahrokh Valaee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we present a dual representation of the influence functions, whose computational complexity scales with dataset size rather than model size. Both analytically and experimentally, we show that this representation can be an efficient alternative to the original influence functions for estimating changes in parameters, model outputs and loss due to data point removal, when model size is large relative to dataset size, or when evaluating the original influence functions in parameter space is infeasible. The dual representation, however, is limited to linearizable models, which are models whose behavior can be approximated by their linearizations throughout training, and requires materializing a matrix, whose size grows with the product of model output dimension and dataset size.

---


### 63. [RETUYT-INCO at BEA 2026 Shared Task 2: Meta-prompting in Rubric-based Scoring for German](https://arxiv.org/abs/2605.11242)

**<font color=#1a73e8>作者：</font>** Ignacio Sastre, Ignacio Remersaro, Facundo Díaz 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this paper, we present the RETUYT-INCO participation at the BEA 2026 shared task "Rubric-based Short Answer Scoring for German". Our team participated in track 1 (Unseen answers three-way), track 3 (Unseen answers two-way) and track 4 (Unseen questions two-way). Since these tracks required scoring short student answers using specific rubrics, we looked for ways to handle the changing nature of the task. We created a method called Meta-prompting. In this approach, an LLM creates a custom prompt based on examples from the Train set. This prompt is then used to grade new student answers. Along with this method, we also describe other approaches we used, such as classic machine learning, fine-tuning open-source LLMs, and different prompting techniques. According to the official results, our team placed 6th out of 8 participants in Track 1 with a QWK of 0.729. In Track 3, we secured 4th place out of 9 with a QWK of 0.674, and we also placed 4th out of 8 in Track 4 with a QWK of 0.49.

---


### 64. [Support-Proximity Augmented Diffusion Estimation for Offline Black-Box Optimization](https://arxiv.org/abs/2605.11246)

**<font color=#1a73e8>作者：</font>** Yonghan Yang, Ye Yuan, Zipeng Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline black-box optimization aims to discover novel designs with high property scores using only a static dataset, a task fundamentally challenged by the out-of-distribution (OOD) extrapolation problem. Existing approaches typically bifurcate into inverse methods, which struggle with the ill-posed nature of mapping scores to designs, and forward methods, which often lack the distributional expressivity to quantify uncertainty effectively. In this work, we propose SPADE (Support-Proximity Augmented Diffusion Estimation), a novel framework that reimagines forward surrogate modeling through the lens of conditional generative modeling. SPADE models the forward likelihood p(y|x) using a diffusion model, but with two critical enhancements to tailor it for optimization: (1) a Calibrated Diffusion Estimation module that enforces global consistency in statistical moments and pairwise rankings, and (2) a Support-Proximity Regularization mechanism that implicitly internalizes the data manifold constraint p(x) via kNN-based density estimation. Theoretically, we prove that our regularization is first-order equivalent to maximizing a Bayesian posterior with a valid design prior. Empirically, SPADE achieves state-of-the-art performance across Design-Bench tasks and an LLM data mixture optimization benchmark.

---


### 65. [A Proof-of-Concept Simulation-Driven Digital Twin Framework for Decision-Aware Diabetes Modeling](https://arxiv.org/abs/2605.11247)

**<font color=#1a73e8>作者：</font>** Zarrin Monirzadeh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper presents a proof-of-concept digital twin framework for simulation-driven diabetes modeling using benchmark clinical data, synthetic temporal augmentation, and illustrative continuous glucose monitoring (CGM) analysis. Unlike traditional predictive models, the framework focuses on generating interpretable simulated trajectories rather than clinically validated outcomes. Evaluation is conducted using a public dataset combined with controlled synthetic scenarios to illustrate temporal behavior and intervention effects. Results illustrate the feasibility of integrating prediction with counterfactual simulation for decision-aware analysis. This work does not claim clinical readiness but provides a foundation for future research on simulation-driven digital twin systems in healthcare.

---


### 66. [Latent Chain-of-Thought Improves Structured-Data Transformers](https://arxiv.org/abs/2605.11262)

**<font color=#1a73e8>作者：</font>** Carson Dudley, Samet Oymak  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought and more broadly test-time compute are known to augment the expressive capabilities of language models and have led to major innovations in reasoning. Motivated by this success, this paper explores latent chain-of-thought as well as the impact of depth and looping for time-series and tabular data. We propose a recurrent scheme in which a structured-data transformer, after an initial forward pass, compresses its query-position hidden states into feedback tokens that are appended to the input and processed again, allowing multiple rounds of latent computation before prediction. We compare CoT models against a same-depth no-CoT baseline, a deeper baseline matched to the CoT model in effective depth, and a looped transformer with weight-tied recurrence but no additional chain-of-thought tokens. Across 36 datasets in time-series forecasting and tabular prediction, latent chain-of-thought improves over the baseline on 8/9 time-series datasets (+10.99\% average gain) and 22/27 tabular datasets (+5.31\% average gain). Across both settings, the CoT models perform the best on average. These results demonstrate that chain-of-thought is a useful axis for scaling test-time compute for structured data.

---


### 67. [DenseTRF: Texture-Aware Unsupervised Representation Adaptation for Surgical Scene Dense Prediction](https://arxiv.org/abs/2605.11265)

**<font color=#1a73e8>作者：</font>** Guiqiu Liao, Matjaž Jogan, Daniel A. Hashimoto  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dense prediction tasks in surgical computer vision, such as segmentation and surgical zone prediction, can provide valuable guidance for laparoscopic and robotic surgery. However, these models often suffer from distribution shifts, as training datasets rarely cover the variability encountered during deployment, leading to poor generalization. We propose DenseTRF, a self-supervised representation adaptation framework based on texture-centric attention. Our method leverages slot attention to learn texture-aware representations that capture invariant visual structures. By adapting these representations to the target distribution without supervision, DenseTRF significantly improves robustness to domain shifts. The framework is implemented through conditioning dense prediction on slot attention and model merging strategies. Experiments across multiple surgical procedures demonstrate improved cross-distribution generalization in comparison to state-of-the-art segmentation models and test-distribution adaptation methods for dense prediction tasks.

---


### 68. [PG-3DGS: Optimizing 3D Gaussian Splatting to Satisfy Physics Objectives](https://arxiv.org/abs/2605.11266)

**<font color=#1a73e8>作者：</font>** Zachary Lee, Maxwell Jacobson, Yexiang Xue  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in Gaussian Splatting have enabled fast, high-fidelity 3D scene generation, yet these methods remain purely visual and lack an understanding of how shapes behave in the physical world. We introduce Physics-Guided 3D Gaussian Splatting (PG-3DGS), a framework that couples differentiable physics simulation with 3D Gaussian representations to generate 3D structures satisfying physics functionalities. By allowing physical objectives to guide the shape optimization process alongside visual losses, our approach produces geometries that are not only photometrically accurate but also physically functional. The model learns to adjust shapes so that the generated objects exhibit physically meaningful behaviors, for example, teapots that can pour and airplanes that can generate lift, without sacrificing visual quality. Experiments on pouring and aerodynamic lift tasks show that PG-3DGS improves physical functionality while preserving visual quality. In addition to simulation gains, bench-top physical lift tests with 3D-printed aircraft (Cessna, B-2 Spirit, and paper plane) under identical airflow conditions show higher scale-measured lift for PG-3DGS, generated structures than an appearance-matching baseline in all three cases. Our unified framework connects appearance-based reconstruction with physics-based reasoning, enabling end-to-end generation of 3D structures that both look realistic and function correctly.

---


### 69. [Real-Scale Island Area and Coastline Estimation using Only its Place Name or Coordinates](https://arxiv.org/abs/2605.11267)

**<font color=#1a73e8>作者：</font>** Quanyun Wu, Kyle Gao, Wentao Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate measurement of island area and coastline length is crucial for coastal zone monitoring and oceanographic analysis. However, traditional measurement and mapping methods usually rely heavily on orthophotos, expensive airborne depth sensors, or dense ground control points, which face serious limitations of high labor costs, time-consuming efforts, and low operational efficiency in vast and inaccessible open sea environments. To overcome these challenges and break away from the reliance on manual field exploration, this paper proposes a geometrically consistent, real-scale island measurement framework based on pure monocular vision. This project significantly reduces the mapping cost through a fully automated process and achieves high-efficiency measurement without prior GIS data. In our system pipeline, only the geographical coordinates or names of the target area need to be input to obtain a low-altitude surrounding image sequence. After obtaining the point clouds, a lightweight trajectory alignment algorithm (Umeyama) is used to restore the global physical scale, and the scaled model is orthorectified, enabling high-precision area and perimeter extraction directly on the 2D rasterized plane. We have fully verified this pipeline on four islands with different terrain features (covering natural landform islands and islands with complex artificial facilities). The experimental results show that the final measurement error of the system is stable at around 10\%, demonstrating excellent accuracy and robustness. Moreover, this framework has outstanding inference speed, requiring only 70 ms to process a single high-resolution image and generate point clouds, providing a highly practical new paradigm for large-scale marine and coastline

---


### 70. [Context-Aware Spear Phishing: Generative AI-Enabled Attacks Against Individuals via Public Social Media Data](https://arxiv.org/abs/2605.11268)

**<font color=#1a73e8>作者：</font>** Elham Pourabbas Vafa, Sayak Saha Roy, Shirin Nilizadeh  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We demonstrate how publicly available social-media data and generative AI (GenAI) can be misused to automate and scale highly personalized, context-aware spear-phishing campaigns. With minimal attacker effort, a small amount of public activity per target is sufficient for GenAI models to extract interests and contextual cues, producing persuasive messages that mirror a target's style while bypassing generic content-moderation safeguards. We introduce a modular framework that combines multimodal signal extraction, communication-style profiling, and attack-type instantiation across seven strategies (baiting, scareware, honey trap, tailgating, impersonation, quid pro quo, and personalized emotional exploitation). We conduct a large-scale, multi-model evaluation covering thousands of generated emails and eight security-relevant criteria, benchmarking against a corpus of real-world phishing messages. The GenAI-produced emails exhibit markedly higher personalization, contextual grounding, and persuasive leverage. Importantly, a complementary user study corroborates these results, revealing that LLM-generated attacks consistently outperform APWG eCrimeX emails across eight dimensions while eliciting lower suspicion among human recipients. Finally, we measure and analyze the behavior of existing proactive, prompt-level defense mechanisms, which incorporate adaptive mechanisms, as well as two complementary defense approaches-policy-augmented SOTA safeguard models and system-instruction chain-of-thought moderation. We document how these defenses respond to contextualized and adaptive attack prompts, underscoring the need for platform-level safeguards that explicitly account for contextualized abuse at scale.

---


### 71. [Localization Boosting for Growth Markets: Mitigating Cross-Locale Behavioral Bias in Learning-to-Rank](https://arxiv.org/abs/2605.11272)

**<font color=#1a73e8>作者：</font>** Suryaa Veerabathiran Seran, Ashwin Naresh Kumar, Tracy Holloway King 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adobe Express is expanding internationally, but the US has a disproportionately large content supply and interaction volume. Learning-to-rank (LTR) models trained primarily on behavioral feedback inherit this imbalance: templates popular in US are over-served in non-US locales. This cross-locale exposure bias suppresses local content discoverability and degrades ranking quality in growth locales.
We show that click-only training suppresses semantically informative localization features. Adding vision-language model (VLM) graded relevance labels as auxiliary supervision alongside clicks improves semantic alignment but does not preserve local content visibility. We propose a multi-objective framework combining behavioral supervision, VLM-derived relevance signals, and locale-aware boosting. Across five locales, the resulting model improves relevance while restoring stable localization, demonstrating the importance of disentangling exposure from semantic supervision.

---


### 72. [Generative AI for Visualizing Highway Construction Hazards Through Synthetic Images and Temporal Sequences](https://arxiv.org/abs/2605.11276)

**<font color=#1a73e8>作者：</font>** Trevor Neece, Mason Smetana, Lev Khazanovich  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Highway construction workers face a high risk of serious injury or death. Image-based training materials depicting hazardous scenarios are essential for engaging safety instruction but remain scarce due to ethical and logistical barriers. This study develops and evaluates a generative AI methodology for producing synthetic visualizations of highway construction hazards from OSHA Severe Injury Report narratives. Two modes were developed: a single-pass approach yielding one image per incident, and a temporal approach producing a four-stage sequence. A sample of 75 incident records yielded 750 images, evaluated using CLIP-based semantic retrieval and expert assessment across dimensions such as educational utility, fidelity, and alignment. Single-pass images achieved 81.1% educational acceptability with fidelity and alignment scores of 4.14/5 and 4.07/5, respectively, while temporal sequences achieved 60.9% acceptability with comparable alignment (3.94/5) but lower fidelity (3.51/5). CLIP-based retrieval revealed that both modes produce images with statistically significant retrieval capabilities. This is among the first studies to leverage modern autoregressive image generation models for visualizing construction hazards from reported severe injuries and to generate temporally sequenced hazard imagery, and a new multi-dimensional evaluation framework was developed to support future research in this domain. The work enables safety trainers to pair narrative storytelling with visual learning material without photographing real-world hazards, and the framework could be applied to datasets across diverse domains, enabling synthetic image generation tailored to new application areas.

---


### 73. [Beyond Similarity: Temporal Operator Attention for Time Series Analysis](https://arxiv.org/abs/2605.11287)

**<font color=#1a73e8>作者：</font>** Jevon Twitty, Vinh Pham, Nitiwith Rotchanarak 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A persistent paradox in time-series forecasting is that structurally simple MLP and linear models often outperform high-capacity Transformers. We argue that this gap arises from a mismatch in the sequence-modeling primitive: while many time-series dynamics are governed by global temporal operators (e.g., filtering and harmonic structure), standard attention forms each output as a convex combination of inputs. This restricts its ability to represent signed and oscillatory transformations that are fundamental to temporal signal processing. We formalize this limitation as a simplex-constrained mixing bottleneck in softmax attention, which becomes especially restrictive for operator-driven time-series tasks. To address this, we propose $\textbf{Temporal Operator Attention (TOA)}$, a framework that augments attention with explicit, learnable sequence-space operators, enabling direct signed mixing across time while preserving input-dependent adaptivity. To make dense $N \times N$ operators practical, we introduce Stochastic Operator Regularization, a high-variance dropout mechanism that stabilizes training and prevents trivial memorization. Across forecasting, anomaly detection, and classification benchmarks, TOA consistently improves performance when integrated into standard backbones such as PatchTST and iTransformer, with particularly strong gains in reconstruction-heavy tasks. These results suggest that explicit operator learning is a key ingredient for effective time-series modeling.

---


### 74. [Optimal Representations for Generalized Contrastive Learning with Imbalanced Datasets](https://arxiv.org/abs/2605.11291)

**<font color=#1a73e8>作者：</font>** Thuan Nguyen, Shuchin Aeron, D. Richard Brown III 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we provide a computable characterization of the geometry of optimal representations in Contrastive Learning (CL) when the classes are imbalanced. When classes are balanced and the representation dimension is greater than the number of classes, it is well-known that the optimal representations exhibit Neural Collapse (NC), i.e., representations from the same class collapse to their class means and the class means form an Equiangular Tight Frame (ETF). For imbalanced classes and a large, generalized family of CL losses, we prove that the optimal representations of all samples from the same class collapse to their class means and their geometry exhibits an angular symmetry structure that is determined by the relative class proportions. In general, we show that the geometry can be determined by solving a convex optimization problem. Exploiting this symmetry structure, we analytically investigate a special case where class imbalance is extreme and prove that CL exhibits a phenomenon called Minority Collapse (MC) where all samples from the minority classes (classes with small probabilities) collapse into a single vector, whenever the class imbalance exceeds a threshold, which in turn depends on the regularity properties of the CL loss used and on the number of negative samples. Numerical results are provided to illustrate these phenomena and corroborate the theoretical results. We conclude by identifying a number of open problems.

---


### 75. [Information and Contract Design for Repeated Interactions between Agents with Misaligned Incentives](https://arxiv.org/abs/2605.11294)

**<font color=#1a73e8>作者：</font>** Nanda Kishore Sreenivas, Kate Larson  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We study the consequences of information asymmetries and misaligned incentives in settings with multiple independent agents. We model an interaction between a Sender, who holds vital private information but cannot act, and a Receiver, who must make decisions but is dependent on the Sender's information. We find that the Sender learns an optimal communication strategy that the Receiver reliably acts on. Importantly, this strategy is highly sensitive to the degree of conflict in the agents' rewards and the amount of environmental information the Receiver can already observe. We introduce a mechanism allowing the agents to form linear contracts, where a price is established for the information. We demonstrate that the Sender learns to use these payment structures to improve its rewards, though this comes at a cost of "fairness" between agents as the Sender is able to extract much of the Receiver's surplus. This raises questions about fairness, contract design, and learning in the context of multi-agent systems.

---


### 76. [Primal Generation, Dual Judgment: Self-Training from Test-Time Scaling](https://arxiv.org/abs/2605.11299)

**<font color=#1a73e8>作者：</font>** Yizhu Jiao, Ruixiang Zhang, Richard Bai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Code generation is typically trained in the primal space of programs: a model produces a candidate solution and receives sparse execution feedback, often a single pass/fail bit. Test-time scaling enriches the inference procedure by sampling multiple candidates and judging among them, but the comparative information this process reveals is discarded after inference. We argue that this information defines a dual judgment space that provides a far richer training signal: the model learns not from an isolated success or failure, but from the relative correctness structure across its own plausible attempts, identifying which succeed, which fail, and what distinguishes them. We introduce DuST (Dual Self-Training), a framework for self-training from the dual judgment space. DuST samples candidate programs from the model's own distribution, labels them through sandbox execution, retains groups containing both successes and failures, and trains the model to rank candidates by execution correctness using GRPO. The objective is purely discriminative: the model is never directly rewarded for generating correct programs. Dual self-training improves both judgment and generation. Across five models spanning two families and three scales (4B to 30B), DuST consistently improves Best-of-4 test-time scaling on LiveCodeBench. For Qwen3-30B-Thinking on LiveCodeBench v6, judgment quality improves by +6.2 NDCG, single-sample pass@1 improves by +3.1, and Best-of-4 accuracy improves by +4.1. The trained model's single rollout matches the base model's Best-of-4 performance. SFT on the same ranking data improves judgment without improving generation, confirming that on-policy RL is the mechanism that transfers dual-space learning back into primal generation.

---


### 77. [Can Graphs Help Vision SSMs See Better?](https://arxiv.org/abs/2605.11300)

**<font color=#1a73e8>作者：</font>** Dhruv Parikh, Anvitha Ramachandran, Haoyang Fan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision state space models inherit the efficiency and long-range modeling ability of Mamba-style selective scans. However, their performance depends critically on the representation of two-dimensional visual features as one-dimensional token sequences. Existing scan operators range from predefined geometric traversals to dynamic coordinate-based samplers that reroute tokens through predicted offsets and interpolation. While effective, these mechanisms primarily adapt paths or sampling locations, rather than explicitly modeling which local patches should exchange information before global state-space mixing. This motivates a simple question: \emph{can graphs help vision state space models see better?} We introduce \textbf{GraphScan}, a graph-induced dynamic scanning operator for Vision SSMs. For each token, GraphScan constructs a spatially bounded local graph, learns feature-conditioned affinities with relative positional bias, and produces the output token by one-step message passing over its semantic neighborhood. The resulting tokens are locally grounded before being processed by the selective SSM for global aggregation. GraphScan preserves token count and linear scaling in image size, while replacing coordinate-conditioned interpolation with feature-conditioned semantic routing. Integrated into a hierarchical backbone, \textbf{GraphScan-Mamba} achieves state-of-the-art performance among Vision SSMs across image classification, object detection, instance segmentation, and semantic segmentation, with modest computational overhead. Our analysis further shows that GraphScan induces interpretable displacement fields over the token lattice, providing a semantic and spatially grounded view of dynamic scanning. These results suggest that future Vision SSMs should treat scanning not merely as geometric serialization, but as learned local semantic routing before global state-space modeling.

---


### 78. [A Theory of Time-Sensitive Language Generation: Sparse Hallucination Beats Mode Collapse](https://arxiv.org/abs/2605.11302)

**<font color=#1a73e8>作者：</font>** Atul Ganju, Travis McVoy, Shaddin Dughmi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study language generation in the limit under a global preference ordering on strings, as introduced by Kleinberg and Wei. As in [arXiv:2504.14370, arXiv:2511.05295], we aim for \emph{breadth}, but impose an additional requirement of timeliness: higher-ranked strings should be generated earlier. A string is then only credited if it is generated before a deadline, where its deadline is defined by a function that maps a string's rank in the target language to the time by which it must be produced. This is in keeping with a central consideration in machine learning, where inductive bias favors ``simpler'' or ``more plausible'' outputs, all else being equal. We show that timely generation is impossible in a strong sense for eventually consistent generators -- the protagonists of most prior related work. Under what is perhaps the mildest natural relaxation of consistency, a hallucination rate that vanishes over time, we show that we can circumvent our impossibility result. In particular, we can achieve optimal density with respect to any superlinear deadline function. We also show this is tight by ruling out timely generation with linear deadlines and vanishing hallucination rate.

---


### 79. [Vision2Code: A Multi-Domain Benchmark for Evaluating Image-to-Code Generation](https://arxiv.org/abs/2605.11307)

**<font color=#1a73e8>作者：</font>** Ajay Vikram Periasami, Junlin Wang, Bhuwan Dhingra  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image-to-code generation tests whether a vision-language model (VLM) can recover the structure of an image enough to express it as executable code. Existing benchmarks either focus on narrow visual domains, depend on paired executable reference code, or rely on generic rubrics that miss domain-specific reconstruction errors. We introduce Vision2Code, a reference-code-free benchmark and evaluation framework for multi-domain image-to-code generation. Vision2Code contains 2,169 test examples from 15 source datasets that span charts and plots, geometry, graphs, scientific imagery, documents, and 3D spatial scenes. Models generate executable programs, which we render and score against the source image using a VLM rater with dataset-specific rubrics and deterministic guardrails for severe semantic failures. We report render-success diagnostics that separate code execution failures from reconstruction quality. Human validation shows that this evaluation protocol aligns better with human judgments than either a generic visual rubric or embedding-similarity baselines. Across nine open-weight and proprietary models, we find that image-to-code performance is domain-dependent: leading models perform well on regular chart- and graph-like visuals but remain weak on spatial scenes, chemistry, documents, and circuit-style diagrams. Finally, we show that evaluator-filtered model outputs can serve as training data to improve image-to-code capability, with Qwen3.5-9B improving from 1.60 to 1.86 on the benchmark without paired source programs. Vision2Code provides a reproducible testbed for measuring, diagnosing, and improving image-to-code generation. Our code and data are publicly available at this https URL.

---


### 80. [Couple to Control: Joint Initial Noise Design in Diffusion Models](https://arxiv.org/abs/2605.11311)

**<font color=#1a73e8>作者：</font>** Jing Jia, Liyue Shen, Guanyang Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models typically generate image batches from independent Gaussian initial noises. We argue that this independence assumption is only one choice within a broader class of valid joint noise designs. Instead, one can specify a coupling of the initial noises: each noise remains marginally standard Gaussian, so the pretrained diffusion model receives the same single-sample input distribution, while the dependence across samples is chosen by design. This reframes initial-noise control from selecting or optimizing individual seeds to designing the dependence structure of a multi-sample gallery. This view gives a general framework for initial-noise design, covering several existing methods as special cases and leading naturally to new coupled-noise constructions. Coupled noise can improve generation on its own without adding sampling cost, and it is flexible enough to serve as a structured initialization for optimization-based pipelines when additional computation is available. Empirically, repulsive Gaussian coupling improves gallery diversity on SD1.5, SDXL, and SD3 while largely preserving prompt alignment and image quality. It matches or outperforms recent test-time noise-optimization baselines on several diversity metrics at the same sampling cost as independent generation. Subspace couplings also support fixed-object background generation, producing diverse, natural backgrounds compared with specialized inpainting baselines, with a tunable trade-off in foreground fidelity.

---


### 81. [Constraint-Data-Value-Maximization: Utilizing Data Attribution for Effective Data Pruning in Low-Data Environments](https://arxiv.org/abs/2605.11312)

**<font color=#1a73e8>作者：</font>** Danilo Brajovic, David A. Kreplin, Marco F. Huber  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Attributing model behavior to training data is an evolving research field. A common benchmark is data removal, which involves eliminating data instances with either low or high values, then assessing a model's performance trained on the modified dataset. Many existing studies leverage Shapley-based data values for this task. In this paper, we demonstrate that these data values are not optimally suited for pruning low-value data when only a limited amount of data remains. To address this limitation, we introduce the Constraint-Data-Value-Maximization (CDVM) approach, which effectively utilizes data attributions for pruning in low-data scenarios. By casting pruning as a constrained optimization that both maximizes total influence and penalizes excessive per-test contributions, CDVM delivers robust performance when only a small fraction of the data is retained. On the OpenDataVal benchmark, CDVM shows strong performance and competitive runtime.

---


### 82. [Quantifying Rodda and Graham Gait Classification from 3D Makerless Kinematics derived from a Single-view Video in a Heterogeneous Pediatric Clinical Cohort](https://arxiv.org/abs/2605.11314)

**<font color=#1a73e8>作者：</font>** Lauhitya Reddy, Seth Donahue, Jeremy Bauer 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cerebral Palsy (CP) is a neurological disorder of movement and the most common cause of lifelong physical disability in childhood. Approximately 75% of children with CP are ambulatory, and accurate gait assessment is central to preserving walking function, which deteriorates by mid-adulthood in a quarter to half of adults with CP. The Rodda and Graham classification system quantifies sagittal-plane gait deviations using ankle and knee z-scores derived from 3D Instrumented Gait Analysis (3D-IGA), but 3D-IGA is expensive and limited to specialized centers, while observational assessment shows only moderate inter-rater agreement. We developed a markerless gait analysis pipeline that quantifies Rodda and Graham knee and ankle z-scores directly from single-view clinical gait videos. Across 1,058 bilateral limb samples from 529 trials of 152 children (88 male, 63 female; age 12.1 $\pm$ 4.0 years; 60 distinct primary diagnoses, cerebral palsy the most common at $n=54$), the sagittal-view model achieved $R^2 = 0.80 \pm 0.02$ and CCC $= 0.89 \pm 0.02$ for knee z-scores and $R^2 = 0.57 \pm 0.02$ and CCC $= 0.72 \pm 0.02$ for ankle z-scores against 3D-IGA. Binary screening for excess knee flexion achieves AUROC $= 0.88$, correctly identifying 83% of affected children, and applying Rodda and Graham rules yields $43 \pm 1$% 7-class accuracy with macro-AUROC $= 0.78 \pm 0.01$, ankle prediction error remaining the primary bottleneck. Beyond cross-sectional screening, continuous z-scores support longitudinal trajectory tracking across visits, providing a quantitative substrate for monitoring disease progression and treatment response unavailable from observational scales. These results demonstrate the feasibility of video-based z-score estimation, excess-flexion screening, and longitudinal trajectory tracking as a path toward scalable, objective gait assessment in low-resource clinical settings.

---


### 83. [Error whitening: Why Gauss-Newton outperforms Newton](https://arxiv.org/abs/2605.11316)

**<font color=#1a73e8>作者：</font>** Maricela Best McKay, Nathan P. Lawrence, Brian Wetton 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Gauss-Newton matrix is widely viewed as a positive semidefinite approximation of the Hessian, yet mounting empirical evidence shows that Gauss-Newton descent outperforms Newton's method. We adopt a function space perspective to analyze this phenomenon. We show that the generalized Gauss-Newton (GGN) matrix projects the Newton direction in function space onto the model's tangent space, while a Jacobian-only variant obtained by applying the least squares Gauss-Newton matrix to non-least squares losses projects the function space loss gradient onto this same tangent space. Both projections eliminate distortions from the model's parameterization. Specifically, the evolution of the prediction-target mismatch depends on the model's parameterization through the matrix $JJ^\top$ where $J$ is the Jacobian of the model with respect to its parameters. The projections effectively replace $JJ^\top$ with the identity. We call this effect error whitening. Once the parameterization is removed, the prediction-target mismatch evolves according to dynamics dictated by the structure of the loss and the projection produced by the optimizer. Error whitening is a special property of Gauss-Newton descent that rigorously distinguishes it from Newton's method. We empirically demonstrate that Gauss-Newton optimizers follow the theoretically predicted function space dynamics and outperforms Newton's method, Adam, and Muon across case studies spanning supervised learning, physics-informed deep learning, and approximate dynamic programming.

---


### 84. [$\varepsilon$-Good Action Identification in Fixed-Budget Monte Carlo Tree Search](https://arxiv.org/abs/2605.11324)

**<font color=#1a73e8>作者：</font>** Yinan Li, Tuan Nguyen, Kwang-Sung Jun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the fixed-budget max-min action identification problem in depth-2 max-min trees, an important special case of Monte Carlo Tree Search. A learner sequentially allocates $T$ samples to leaves and then recommends a subtree whose minimum leaf value is largest. Motivated by approximate planning, we focus on $\varepsilon$-good subtree identification, where any subtree whose min value is within $\varepsilon$ of the optimal maximin value is acceptable.
Our main contribution is an $\varepsilon$-agnostic algorithm: it does not require $\varepsilon$ as input, but achieves instance-dependent error bounds for every meaningful $\varepsilon$. We show that the misidentification probability decays as $\exp(-\widetilde{\Theta}(T/H_2(\varepsilon)))$, where $H_2(\varepsilon)$ captures both cross-subtree and within-subtree gaps. When each subtree has a single leaf, the problem reduces to standard fixed-budget best-arm identification, and our analysis recovers, up to accelerating factors, known $\varepsilon$-good guarantees for halving-style methods while giving a new $\varepsilon$-good guarantee for Successive Rejects.
On the lower-bound side, we provide complementary positive and negative results showing that max-min identification has a different hardness structure from standard $K$-armed bandits. To our knowledge, this is the first provable fixed-budget algorithmic guarantee for max-min action identification.

---


### 85. [Neural Statistical Functions](https://arxiv.org/abs/2605.11327)

**<font color=#1a73e8>作者：</font>** Daniel Xu, Yuxin Xie, Minghao Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classical deep learning typically operates on individual cases. Despite its success, real-world usage often requires repeated inference to estimate statistical quantities for complex decision-making tasks involving uncertainty or extreme-value analysis, resulting in substantial latency. We introduce neural statistical functions, a new family of models learned from pre-trained single-sample predictors and scattered data samples, which can directly infer statistics over continuous operating condition ranges without explicit sampling. By introducing the notion of prefix statistics, we transform and unify diverse statistical functions (e.g., integrals, quantiles, and maxima) into an interval-conditional framework, in which a principled identity between the prefix statistics and the individual-case regression serves as the learning objective. Neural statistical functions achieve strong performance in estimating essential statistics of complex physical processes, including accumulated energy in dynamical systems, quantiles of aerodynamic responses, and maximum stress in crash processes, while achieving up to a 100$\times$ reduction in model evaluations.

---


### 86. [Epistemic Uncertainty for Test-Time Discovery](https://arxiv.org/abs/2605.11328)

**<font color=#1a73e8>作者：</font>** Kainat Riaz, Muhammad Ahmed Mohsin, Ahsan Bilal 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated scientific discovery using large language models relies on identifying genuinely novel solutions. Standard reinforcement learning penalizes high-variance mutations, which leads the policy to prioritize familiar patterns. As a result, the maximum reward plateaus even as the average reward increases. Overcoming this limitation requires a signal that distinguishes unexplored regions from intrinsically difficult problems. This necessitates measuring disagreement across independently adapted weight hypotheses rather than relying on a single network's confidence. UG-TTT addresses this challenge by maintaining a small ensemble of low-rank adapters over a frozen base model. The per-token disagreement, quantified as the mutual information between ensemble predictions and weight hypotheses, isolates epistemic uncertainty and identifies positions where insufficient coverage leads to adapter divergence rather than intrinsic problem difficulty. This measure is incorporated as an exploration bonus into the policy gradient, directing the policy toward positions where persistent adapter disagreement signals low training coverage, the same frontier where genuine discovery is possible. A nuclear norm regularizer ensures the adapters remain distinct from one another, thereby preserving the exploration signal throughout training. Across four scientific discovery benchmarks, UG-TTT increases the maximum reward on three tasks, maintains substantially higher solution diversity, and an ablation study confirms that the regularizer is essential for sustaining this behavior.

---


### 87. [A Systematic Security Testing Approach for InterUSS-based environments](https://arxiv.org/abs/2605.11339)

**<font color=#1a73e8>作者：</font>** Henrique Curi de Miranda, Ágney Lopes Roth Ferraz, Wagner Comin Sonaglio 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Unmanned Traffic Management (UTM) federated ecosystems, such as InterUSS, enable secure coordination among UAS Service Suppliers (USSs). However, they bring up some security challenges at the infrastructure level that haven't been fully explored. This paper presents a security testing approach for InterUSS-based environments from the maintainer's perspective. By deploying and analyzing a working InterUSS infrastructure, we pinpoint key components and develop specific security tests aligned with established standards and protocols, such as mTLS and OAuth 2.0. We compiled these tests into a Testing Guide that aids both component validation and interaction analysis across InterUSS-based ecosystems, filling a gap in current research.

---


### 88. [Making Abstraction Concrete: A Design Space and Interaction Model of Abstraction in Interactive Systems](https://arxiv.org/abs/2605.11344)

**<font color=#1a73e8>作者：</font>** Bryan Min, Sangho Suh, Jim Hollan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The principle of abstraction guides the design of interactive systems, yet we lack a conceptual framework to understand how it shapes interaction design. Existing models, such as the gulfs of execution and evaluation, do not explicitly model abstractions in the system or in users' mental models, and therefore lack actionable guidance for designing abstractions. To investigate how abstractions are employed in interactive systems, we surveyed 457 papers and synthesized a design space of abstraction techniques along six dimensions. We use this design space to reframe the gulfs through a lens of abstraction, explicitly articulate the cognitive and design processes by which users and systems bridge and navigate the abstraction gap, and demonstrate how this model integrates existing perspectives and surfaces new opportunities for future systems.

---


### 89. [Physics-Informed Teacher-Student Ensemble Learning for Traffic State Estimation with a Varying Speed Limit Scenario](https://arxiv.org/abs/2605.11346)

**<font color=#1a73e8>作者：</font>** Archie J. Huang, Dongdong Wang, Shaurya Agarwal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed deep learning (PIDL) neural networks have shown their capability as a useful instrument for transportation practitioners in utilizing the underlying relationship between the state variables for traffic state estimation (TSE). Another efficient traffic management approach is implementing varying speed limits (VSLs) on transportation corridors to control traffic and mitigate congestion. However, the existing training architecture of PIDL in the literature cannot accommodate the changing traffic characteristics on a freeway with VSL. To tackle this challenge, we propose a novel framework integrating teacher-student ensemble training with PIDL neural networks for TSE under VSL scenarios. The physics of flow conservation law is encoded locally in the teacher models by PIDL, and the student model uses a multi-layer perceptron classifier (MLP) to identify traffic characteristics and selects the ensemble member of PIDL neural networks for TSE. This integrated framework provides a natural solution for capturing the heterogeneity of VSL and accurately addressing the TSE problem. The case study results validate the proposed ensemble approach, demonstrating its superior performance in TSE compared to other popular baseline methods, as indicated by relative L2 error.

---


### 90. [Lite3R: A Model-Agnostic Framework for Efficient Feed-Forward 3D Reconstruction](https://arxiv.org/abs/2605.11354)

**<font color=#1a73e8>作者：</font>** Haoyu Zhang, Zeyu Zhang, Zedong Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transformer-based 3D reconstruction has emerged as a powerful paradigm for recovering geometry and appearance from multi-view observations, offering strong performance across challenging visual conditions. As these models scale to larger backbones and higher-resolution inputs, improving their efficiency becomes increasingly important for practical deployment. However, modern 3D transformer pipelines face two coupled challenges: dense multi-view attention creates substantial token-mixing overhead, and low-precision execution can destabilize geometry-sensitive representations and degrade depth, pose, and 3D consistency. To address the first challenge, we propose Lite3R, a model-agnostic teacher-student framework that replaces dense attention with Sparse Linear Attention to preserve important geometric interactions while reducing attention cost. To address the second challenge, we introduce a parameter-efficient FP8-aware quantization-aware training (FP8-aware QAT) strategy with partial attention distillation, which freezes the vast majority of pretrained backbone parameters and trains only lightweight linear-branch projection layers, enabling stable low-precision deployment while retaining pretrained geometric priors. We further evaluate Lite3R on two representative backbones, VGGT and DA3-Large, over BlendedMVS and DTU64, showing that it substantially reduces latency (1.7-2.0x) and memory usage (1.9-2.4x) while preserving competitive reconstruction quality overall. These results demonstrate that Lite3R provides an effective algorithm-system co-design approach for practical transformer-based 3D reconstruction. Code: this https URL. Website: this https URL.

---


### 91. [gym-invmgmt: An Open Benchmarking Framework for Inventory Management Methods](https://arxiv.org/abs/2605.11355)

**<font color=#1a73e8>作者：</font>** Reza Barati, Qinmin Vivian Hu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inventory-policy comparisons are often difficult to interpret because performance depends on the evaluation contract as much as on the policy itself. Differences in topology, demand regime, information access, feasibility constraints, shortage treatment, and Key Performance Indicator (KPI) definitions can change method rankings. We present gym-invmgmt, a Gymnasium-compatible extension of the OR-Gym inventory-management lineage for auditable cross-paradigm evaluation. The benchmark evaluates optimization, heuristic, and learned controllers under a shared CoreEnv transition, reward, action-bound, and KPI contract, while varying stress conditions through a 22-scenario core grid plus four supplemental MARL-mode rows. Within these released scenarios, informed stochastic programming provides the strongest non-oracle reference, reflecting the value of scenario hedging under forecast access, but at substantially higher online computational cost. Among learned controllers, the Proximal Policy Optimization Transformer variant (PPO-Transformer) achieves the strongest learned-policy quality at fast inference, while Residual Reinforcement Learning (Residual RL) provides competitive hybrid performance. The graph neural network variant (PPO-GNN) is highly competitive on the default divergent topology but less robust on the serial topology. Imitation learning performs well in stationary regimes but degrades under demand shift, and the bounded Large Language Model (LLM) policy-parameter baseline is best interpreted as a diagnostic controller rather than an autonomous inventory optimizer. Overall, the benchmark identifies scenario-conditioned leaders while showing that performance depends jointly on information access, demand shift, topology, and policy representation.

---


### 92. [CVEvolve: Autonomous Algorithm Discovery for Unstructured Scientific Data Processing](https://arxiv.org/abs/2605.11359)

**<font color=#1a73e8>作者：</font>** Ming Du, Xiangyu Yin, Yanqi Luo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific data processing often requires task-specific algorithms or AI models, creating a barrier for domain scientists who need to analyze their data but may not have extensive computing or image-processing expertise. This barrier is especially pronounced when data are noisy, have a high dynamic range, are sparsely labeled, or are only loosely specified. We introduce CVEvolve, an autonomous agentic harness with a zero-code interface for scientific data-processing algorithm discovery. CVEvolve combines a multi-round search strategy with tools for code execution, evaluation implementation, history management, holdout testing, and optional inspection of scientific data and visual outputs. The search alternates between discovery and improvement actions, and uses lineage-aware stochastic candidate sampling to balance exploration and exploitation. We demonstrate CVEvolve on x-ray fluorescence microscopy image registration, Bragg peak detection, and high-energy diffraction microscopy image segmentation. Across these tasks, CVEvolve discovers algorithms that improve over baseline methods, while holdout test tracking helps identify candidates that generalize better than later over-optimized alternatives. These results show that zero-code, autonomous LLM-powered algorithm development can help domain scientists turn unstructured scientific image data into practical algorithms and downstream scientific discoveries.

---


### 93. [Options, Not Clicks: Lattice Refinement for Consent-Driven MCP Authorization](https://arxiv.org/abs/2605.11360)

**<font color=#1a73e8>作者：</font>** Ying Li, Yanju Chen, Peiran Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As Model Context Protocol adoption grows, securing tool invocations via meaningful user consent has become a critical challenge, as existing methods, broad always allow toggles or opaque LLM-based decisions, fail to account for dangerous call arguments and often lead to consent fatigue. In this work, we present Conleash, a client-side middleware that enforces boundary-scoped authorization by utilizing a risk lattice to auto-permit safe calls within known boundaries while escalating risks, a policy engine for user-defined invariants, and a refinement loop that converts user decisions into reusable rules. Evaluated on 984 real-world traces, Conleash achieved 98.2% accuracy, caught 99.4% of escalations, and added only 8.2 ms of overhead for policy verification; furthermore, in a user study where N=16, participants significantly preferred Conleash scoped permissions over traditional methods, citing higher trust and reduced prompting.

---


### 94. [Causal Fairness for Survival Analysis](https://arxiv.org/abs/2605.11362)

**<font color=#1a73e8>作者：</font>** Drago Plecko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the data-driven era, large-scale datasets are routinely collected and analyzed using machine learning (ML) and artificial intelligence (AI) to inform decisions in high-stakes domains such as healthcare, employment, and criminal justice, raising concerns about the fairness behavior of these systems. Existing works in fair ML cover tasks such as bias detection, fair prediction, and fair decision-making, but largely focus on static settings. At the same time, fairness in temporal contexts, particularly survival/time-to-event (TTE) analysis, remains relatively underexplored, with current approaches to fair survival analysis adopting statistical fairness definitions, which, even with unlimited data, cannot disentangle the causal mechanisms that generate disparities. To address this gap, we develop a causal framework for fairness in TTE analysis, enabling the decomposition of disparities in survival into contributions from direct, indirect, and spurious pathways. This provides a human-understandable explanation of why disparities arise and how they evolve over time. Our non-parametric approach proceeds in four steps: (1) formalizing the necessary assumptions about censoring and lack of confounding using a graphical model; (2) recovering the conditional survival function given covariates; (3) applying the Causal Reduction Theorem to reframe the problem in a form amenable to causal pathway decomposition; (4) estimating the effects efficiently. Finally, our approach is used to analyze the temporal evolution of racial disparities in outcome after admission to an intensive care unit (ICU).

---


### 95. [Causal Bias Detection in Generative Artifical Intelligence](https://arxiv.org/abs/2605.11365)

**<font color=#1a73e8>作者：</font>** Drago Plecko  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated systems built on artificial intelligence (AI) are increasingly deployed across high-stakes domains, raising critical concerns about fairness and the perpetuation of demographic disparities that exist in the world. In this context, causal inference provides a principled framework for reasoning about fairness, as it links observed disparities to underlying mechanisms and aligns naturally with human intuition and legal notions of discrimination. Prior work on causal fairness primarily focuses on the standard machine learning setting, where a decision-maker constructs a single predictive mechanism $f_{\widehat Y}$ for an outcome variable $Y$, while inheriting the causal mechanisms of all other covariates from the real world. The generative AI setting, however, is markedly more complex: generative models can sample from arbitrary conditionals over any set of variables, implicitly constructing their own beliefs about all causal mechanisms rather than learning a single predictive function. This fundamental difference requires new developments in causal fairness methodology. We formalize the problem of causal fairness in generative AI and unify it with the standard ML setting under a common theoretical framework. We then derive new causal decomposition results that enable granular quantification of fairness impacts along both (a) different causal pathways and (b) the replacement of real-world mechanisms by the generative model's mechanisms. We establish identification conditions and introduce efficient estimators for causal quantities of interest, and demonstrate the value of our methodology by analyzing race and gender bias in large language models across different datasets.

---


### 96. [LPDP: Inference-Time Reward Control for Variable-Length DNA Generation with Edit Flows](https://arxiv.org/abs/2605.11368)

**<font color=#1a73e8>作者：</font>** Jeongchan Kim, Yunkyung Ko, Jong Chul Ye  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the application of recent Edit Flows for inference-time reward control for DNA sequence generation. Unlike most reward-guided DNA generation frameworks, which operate on fixed-length sequence spaces, Edit Flows have a potential to generate variable-length DNA through biologically plausible insertion, deletion, and substitution operations. In particular, we propose Local Perturbation Discrete Programming (LPDP), a training-free, intermediate-state and action-aware local re-solving operator for variable-length DNA edit-action generators at inference time. More specifically, at each guided rollout step, LPDP scores one-step root edits, retains a near-best root band, and re-ranks each retained root by solving a bounded local discrete program around its child sequence. This local program uses the typed geometry of edit actions to focus on coherent substitution, insertion, or deletion subgraphs, and aggregates local continuations with either a hard Max backup or a soft log-sum-exponential (LSE) backup. We instantiate LPDP in two regimes: front-loaded reward tilting for enhancer optimization, where early edits are critical for establishing global regulatory sequence structure, and back-loaded reward tilting for exon-intron-exon inpainting, where late edits fine-tune splice-boundary contexts.

---


### 97. [Dynamic Full-body Motion Agent with Object Interaction via Blending Pre-trained Modular Controllers](https://arxiv.org/abs/2605.11369)

**<font color=#1a73e8>作者：</font>** Sanghyeok Nam, Byoungjun Kim, Daehyung Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating physically plausible dynamic motions of human-object interaction (HOI) remains challenging, mainly due to existing HOI datasets limited to static interactions, and pretrained agents capable of either dynamic full-body motions without objects or static HOI motions. Recent works such as InsActor and CLoSD generate HOI motions in planning and execution stages, are yet limited to either static or short-term contacts e.g. striking. In this work, we propose a framework that fulfills dynamic and long-term interaction motions such as running while holding a table, by combining pretrained motion priors and imitation agents in planning and execution stages. In the planning stage, we augment HOI datasets with dynamic priors from a pretrained human motion diffusion model, followed by object trajectory generation. This plans dynamic HOI sequences. In the execution stage, a composer network blends actions of pretrained imitation agents specialized either for dynamic human motions or static HOI motions, enabling spatio-temporal composition of their complementary skills. Our method over relevant prior-arts consistently improves success rates while maintaining interaction for dynamic HOI tasks. Furthermore, blending pretrained experts with our composer achieves competitive performance in significantly reduced training time. Ablation studies validate the effectiveness of our augmentation and composer blending.

---


### 98. [Causal Algorithmic Recourse: Foundations and Methods](https://arxiv.org/abs/2605.11373)

**<font color=#1a73e8>作者：</font>** Drago Plecko, Collin Wang, Elias Bareinboim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The trustworthiness of AI decision-making systems is increasingly important. A key feature of such systems is the ability to provide recommendations for how an individual may reverse a negative decision, a problem known as algorithmic recourse. Existing approaches treat recourse outcomes as counterfactuals of a fixed unit, ignoring that real-world recourse involves repeated decisions on the same individual under possibly different latent conditions. We develop a causal framework that models recourse as a process over pre- and post-intervention outcomes, allowing for partial stability and resampling of latent variables. We introduce post-recourse stability conditions that enable reasoning about recourse from observational data alone, and develop a copula-based algorithm for inferring the effects of recourse under these conditions. For settings where paired observations of the same individual before and after intervention are available (called recourse data), we develop methods for inferring copula parameters and performing goodness-of-fit testing. When the copula model is rejected, we provide a distribution-free algorithm for learning recourse effects directly from recourse data. We demonstrate the value of the proposed methods on real and semi-synthetic datasets.

---


### 99. [An Empirical Study of Automating Agent Evaluation](https://arxiv.org/abs/2605.11378)

**<font color=#1a73e8>作者：</font>** Kang Zhou, Sangmin Woo, Haibo Ding 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agent evaluation requires assessing complex multi-step behaviors involving tool use and intermediate reasoning, making it costly and expertise-intensive. A natural question arises: can frontier coding assistants reliably automate this evaluation process? Our study shows that simply prompting coding assistants is insufficient for this task. Without domain-specific evaluation knowledge, frontier coding assistants achieve only a 30% execution success rate and produce over-engineered evaluations averaging 12+ metrics per agent, indicating that strong coding ability does not automatically translate to reliable agent evaluation. We introduce EvalAgent, an AI assistant that automates the end-to-end agent evaluation pipeline. EvalAgent encodes evaluation domain expertise as evaluation skills (procedural instructions, reusable code and templates, and dynamically retrieved API documentation) that compose into a trace-based pipeline producing complete evaluation artifacts including metrics, executable code, and reports. To systematically assess generated evaluations, we introduce a meta-evaluation framework alongside AgentEvalBench, a benchmark comprising 20 agents, each paired with evaluation requirements and test scenarios. We further propose the Eval@1 metric to measure whether generated evaluation code both executes and yields meaningful results on the first run. Our experiments show that EvalAgent produces focused evaluations, improving Eval@1 from 17.5% to 65%, and achieving 79.5% human expert preference over baseline approaches. Further ablation studies show that evaluation skills are critical for handling complex evaluation: removing them causes Eval@1 to drop significantly from 65% to 30%.

---


### 100. [TRACE: Temporal Routing with Autoregressive Cross-channel Experts for EEG Representation Learning](https://arxiv.org/abs/2605.11380)

**<font color=#1a73e8>作者：</font>** Fan Ma, Qier An, Peng Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning transferable representations for electroencephalography (EEG) remains challenging because EEG signals are inherently multi-channel and non-stationary. Channels observed at the same time provide coupled measurements of neural activity, while the relevant temporal dynamics vary across contexts. This structure is poorly matched by architectures that apply uniform computation across time or route each channel patch independently. To this end, we propose TRACE, an autoregressive EEG pre-training framework that predicts future EEG patches from causal context while performing temporally adaptive and cross-channel coherent computation. At each temporal step, TRACE derives an expert routing decision from the causal cross-channel history and applies it jointly to all channels at that step. This preserves instantaneous cross-channel coherence while allowing different temporal regimes to activate different computation. Since routing is defined over the available channel set and causal temporal context, TRACE is compatible with heterogeneous pre-training across corpora with different channel counts, montages, sequence lengths, and recording domains. Across eight downstream EEG benchmarks, TRACE is evaluated in both settings: when downstream domains are seen only as unlabeled pre-training data and when downstream datasets are completely unseen during pre-training. It obtains the best results on several benchmarks while remaining competitive on motor imagery and clinical event classification tasks, with ablations supporting the importance of cross-channel temporal routing.

---


> [!TIP]
> 当前位于：**51-100**（第 2/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-396](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
