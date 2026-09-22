# 📦 其他研究 | 2026年09月23日

> 本类共 **463** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-463](./part-10.md)

---

### 1. [Memory That Looks Forward: A Zero-Inference Prospective Term for Personal Memory Retrieval](https://arxiv.org/abs/2609.22091)

**<font color=#1a73e8>作者：</font>** Jonathan Groff  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval over a personal memory store is retrospective: it surfaces what resembles the query, and it is blind to what the user has committed to do. We describe a prospective term for memory retrieval that costs no inference at query time. Commitments are held in an explicit ledger as dated or trigger-conditioned entries; memory items linked to a firing entry receive a salience boost, blended multiplicatively into embedding-based retrieval so that relevance remains sovereign. On a synthetic prospective-memory task set modeled on TriggerBench's published structure (48 blind-authored dialogues, 175 tasks), the term raised recall@5 on the hard stratum from 0.000 to 0.955 at the default blend weight and to 1.000 under a floor variant, with zero false boosts across 53 resolved-commitment tasks. Blind authorship also produced a scope finding: only 17-29% of naturally phrased commitment-trigger pairs defeat embedding similarity, so the term matters on a real minority of cases and must do no harm on the rest, which it does not. We position precomputed commitment linkage as the always-on floor of a layered design whose expansion layer is query-time prospection. Results are preliminary: the evaluation set is author-constructed, and evaluation on TriggerBench proper is committed follow-up work once its data is released.

---


### 2. [AI-inferred expressed well-being and collective-action discourse in climate-change campaigns on X](https://arxiv.org/abs/2609.22096)

**<font color=#1a73e8>作者：</font>** Wentao Xu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Climate campaigns are often evaluated through attention and mobilization, but less is known about the well-being language that accompanies them. Whether campaign periods alter positive affect and hope, and whether happiness aligns with action language, remains unresolved. We analysed 364,118 public Twitter/X posts from Earth Day, Earth Hour, Global Climate Action Day and World Environment Day in 19 occurrence-years, using 30-day pre-event, event and post-event windows. A versioned weighted lexical model estimated happiness, future-oriented hope, collective capability, distress and action language. Event-period happiness prevalence was 9.02 percentage points higher than the pre-event baseline , whereas paired occurrence contrasts showed a 10.75-point decline in action language, indicating a happiness--action divergence. The happiness estimate remained positive across composition and text-deduplication checks, but was less precise under a 19-cluster wild bootstrap. Happier source posts had lower odds of an observed matched retweet cascade.

---


### 3. [A framework for recipe data structure with applications for culinary and nutritional insights](https://arxiv.org/abs/2609.22099)

**<font color=#1a73e8>作者：</font>** Mansi Goel, Sumit Bhagat, Saloni Srivastava 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cooking is a complex process that transforms raw ingredients into delicious and nutritious dishes, yet the recipes that encode this process remain largely free text; readable by people but not directly computable. Existing recipe collections capture fragments of this information, but no shared representation links a recipe's structured ingredient composition, its geo-cultural provenance, and its nutritional profile within a single queryable schema. We address this representation gap by formalizing a framework for recipe data structure that decomposes each recipe into typed ingredient entities, grounds those entities in a reference nutritional database, and annotates them with geo-cultural and dietary context. We present RecipeDB2, a structured compilation of 128,942 recipes with 35,474 ingredients from 32 regions and 99 countries. Ingredient phrases are parsed into seven culinary attributes using a transformer-based named-entity model; ingredients are linked to the USDA reference tables through a BERT embedding strategy (F1 = 87.90 on a manually adjudicated set of the 200 most frequent ingredients), yielding 148 nutritional parameters per mapped ingredient; a Random Forest classifier propagates 34 ingredient categories across the full vocabulary; and a deterministic, conservative rule set assigns each recipe a dietary style. Through RecipeDB2 (this https URL), we demonstrate a scalable framework for making recipes computable, turning culinary heritage (long treated as an artistic rather than a quantitative object) into a data-driven analysis.

---


### 4. [Correcting Learning-based Perception for Safety](https://arxiv.org/abs/2609.22108)

**<font color=#1a73e8>作者：</font>** Yan Miao, Hussein Darir, Sayan Mitra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning-enabled perception is important in many autonomous systems. Unlike traditional sensors, the boundary where ML perception does or does not work is poorly characterized. Incorrect perception can lead to unsafe or overtly conservative downstream control actions. In this paper, we propose a two-step strategy for correcting ML-based state estimation. First, an offline computation is used to characterize the uncertainties resulting from the ML module's state estimation, using preimages of perception contracts. Second, at runtime, a risk heuristic is used to choose particular states from the uncertain estimates to drive the control decisions. We perform extensive simulation-based evaluation of this runtime perception correction strategy on different vision-based adaptive cruise controllers (ACC modules), in different weather conditions, and road scenarios. Out of 45 ACC scenarios where the original perception-based control system using Yolo and LaneNet led to safety violations, in 73% of the scenarios, our runtime perception correction preserved safety; our method wouldn't be able to recover 27% of the scenarios where the construction of the preimages of perception contracts is not fully conformant. Further, our runtime perception correction strategy is not overly conservative---on the average only a 2.8% increase in completion time is experienced in the corrected scenarios, with mild interventions.

---


### 5. [Toward Fairness in Machine Learning Models for Predicting Treatment Retention and Premature Discontinuation in Medication for Opioid Use Disorder](https://arxiv.org/abs/2609.22113)

**<font color=#1a73e8>作者：</font>** Tongnian Wang, Carolina Vivas-Valencia, Cici Bauer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Persistent low retention and completion rates in medications for opioid use disorder (MOUD) have driven the use of machine learning (ML) models to predict retention and identify patients at risk of premature discontinuation. However, the fairness of these models across patient populations remains largely unexplored, raising concerns about their application in treatment decision support. This study systematically assesses algorithmic fairness in ML models for predicting MOUD retention and premature discontinuation and investigates the effectiveness of bias mitigation techniques. Using the cross-sectional Treatment Episode Data Set-Discharges (TEDS-D), which includes treatment episodes for individuals in the U.S. discharged between 2015 and 2019, we trained four ML models to predict premature treatment discontinuation and retention beyond 180 days among individuals receiving outpatient MOUD. We evaluated overall performance and subgroup-level error rates across patient subgroups defined by race, ethnicity, age, and sex, complemented by model explanation analyses. We further assessed bias mitigation techniques and their effects on both fairness and predictive performance. Our findings demonstrate that ML models for MOUD outcome prediction can exhibit subgroup-level performance gaps even when overall predictive performance appears acceptable and that bias mitigation can reduce, but not fully eliminate, these gaps without trade-offs. By demonstrating the importance of fairness-aware evaluation and transparent reporting of subgroup performance, this study provides practical insights for the responsible and context-sensitive use of ML models for risk stratification and care prioritization in MOUD treatment settings.

---


### 6. [ZoAQ: Adaptive Zeroth-Order Querying via Query-Reuse Coupling](https://arxiv.org/abs/2609.22115)

**<font color=#1a73e8>作者：</font>** Yangyang Feng, Yao Shu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zeroth-order optimization (ZOO) estimates updates from function evaluations, making perturbation queries a primary cost. Fixed budgets spend the same number of queries at every step, while adaptive controllers may offset their savings by using additional oracle calls to test estimator reliability. We introduce ZoAQ, an adaptive ZOO method built around query reuse. Rather than discarding past evaluations after each step, ZoAQ makes them useful for both the next update and the decision to query further. This enables adaptive query allocation without extra validation queries. Our analysis characterizes when this agreement identifies an update that supports descent and guides the controller to a sufficient query budget. On synthetic objectives, ZoAQ reduces queries by 43-48% relative to fixed baselines using 1.2M queries. In black-box attacks, it reaches 100% success with 320 and 625 average queries on MNIST and CIFAR-10, respectively. Across four OPT fine-tuning settings, ZoAQ saves 43-46% forward evaluations relative to fixed K=4, with accuracy changes within tasks ranging from -0.018 to +0.010.

---


### 7. [LE4Mob: Towards Inductive, Distance-Aware and General-Purpose Location Embedding for Human Mobility Modelling](https://arxiv.org/abs/2609.22117)

**<font color=#1a73e8>作者：</font>** Xinglei Wang, Stephen Law, Zichao Zeng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Location representations provide mobility models with fundamental information about the spatial position, functional characteristics, and relationships of places. However, existing embeddings are often dependent on mobility observations, unable to represent unseen locations, and weakly constrained to retain geographic distance. This limits their reuse across datasets and mobility tasks. To address these limitations, we propose LE4Mob, an inductive, distance-aware, and geography-derived location embedding framework for mobility modelling. LE4Mob extends contrastive language-location pre-training while introducing a distance-aware regularisation objective that encourages the embedding space to preserve spatial relationships. Pre-trained from geographic context, LE4Mob can encode rich spatial-semantic information and generate embeddings for unseen locations inductively. Its independence from downstream mobility task supervision also makes it transferable across different mobility tasks. We evaluate LE4Mob on individual-level next location prediction and population-level commuter flow generation. Experiments across multiple datasets and study areas show that LE4Mob outperforms strong baselines, with particular advantages in inductive settings and when downstream models rely directly on interactions between location embeddings. These findings demonstrate the potential of distance-aware, geography-derived location representations as reusable foundations for human mobility modelling.

---


### 8. [Modelling daily activity patterns from mobile phone location data via deep representation learning](https://arxiv.org/abs/2609.22121)

**<font color=#1a73e8>作者：</font>** Xinglei Wang, Junyuan Liu, Guangsheng Dong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Passively collected mobile phone location data provide large-scale, longitudinal observations of human mobility but do not directly reveal activity purposes. The functional characteristics of visited locations offer useful contextual information, yet their relationship with activity purpose remains uncertain, particularly in mixed-use urban environments. We conceptualise activity pattern mining as an integrated process of representation, clustering, and interpretation, and propose the Activity Chain Encoder (ACE) for the representation stage. ACE is a self-supervised model that combines pre-trained urban embeddings with visit timing and duration and uses a Transformer to model the sequential organisation of stays. It is trained using masked activity modelling and identity-guided contrastive learning without requiring deterministic activity purpose labels. Learned daily representations are aggregated into user-level profiles, clustered, and interpreted through temporal-functional patterns and Census-derived demographic context. Applied to mobile phone app location data from London and compared with three representative methods, ACE supports the identification of six differentiated weekday activity-pattern groups characterised by distinct daily rhythms, urban functional contexts, and demographic associations. These complementary forms of evidence further support the development of empirically grounded activity-pattern personas, establishing a holistic route for deriving behaviourally meaningful population patterns from unlabelled mobile phone location data. The source code for the entire analytical pipeline developed in this study is publicly available at this https URL.

---


### 9. [StationPDE: Station-Oriented Surface PDE Learning for Multi-Station Multivariate Weather Forecasting](https://arxiv.org/abs/2609.22123)

**<font color=#1a73e8>作者：</font>** Xiao Wang, Changjian Chen, Rongwen Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-station multivariate weather forecasting aims to forecast future weather variables at multiple weather stations from historical surface observations. Existing station forecasting models learn statistical dependencies among discrete stations, but lack explicit physical evolution. Meanwhile, PDE-based weather models provide interpretable physical dynamics, yet require continuous fields and upper-air variables unavailable in surface station data. To bridge this gap, we propose StationPDE, a station-oriented surface PDE learning model. StationPDE constructs a terrain-aware continuous surface field from discrete station observations and decomposes its physical evolution into surface wind transport and upper-air inference. Surface wind transport explicitly evolves observable weather variables, while upper-air inference uses learnable horizontal diffusion to approximate the missing influence of unavailable upper-air variables. A parallel data-driven diffusion branch captures complementary motion patterns, and an adaptive router integrates the two forecasts for station-level multivariate forecasting. Experiments on Weather2K and MeteoNet show that StationPDE consistently outperforms state-of-the-art baselines, reducing MSE by about $9.6\%$ on average compared with the strongest baseline. Code and implementation details are available at this https URL.

---


### 10. [SolarFlowRefiner: Refinement-Aware Flow Matching for Surface Solar Radiation Downscaling](https://arxiv.org/abs/2609.22126)

**<font color=#1a73e8>作者：</font>** Udbhav Srivastava, Antonita Racheal, Yiheng Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-resolution surface solar radiation (SSR) is important for solar forecasting and grid operation. However, physically consistent reanalysis products are too coarse to resolve localized cloud-driven variability. In this paper, we study a multisource downscaling task that reconstructs high-resolution SolarCube SSR fields from coarse ERA5 radiative variables and co-registered satellite channels. The task is challenging because a single ERA5 grid cell may contain both sunlit and cloud-shadowed regions. As a result, the missing high-resolution correction can be spatially sharp and inherently ambiguous. One-stage predictors often oversmooth these structures. Post-hoc refinement also introduces a stage-wise mismatch: the generator is optimized independently, even though its output determines the refiner's initial state. We introduce SolarFlowRefiner, a refinement-aware flow-matching framework for SSR downscaling. A conditional FlowMatch generator first predicts a normalized correction to an upsampled ERA5 baseline. The refiner is then trained on prediction-conditioned states between the current FlowMatch output and the target residual. This exposes the refiner to the structured errors produced by the generator. The refinement objective is also backpropagated through the FlowMatch sampler, allowing generation and correction to be jointly optimized for the final reconstruction. Experiments on a day-blocked ERA5--SolarCube benchmark show consistent improvements over standalone generation and post-hoc refinement. More broadly, SolarFlowRefiner provides a general strategy for coupling generative predictors with iterative correctors.

---


### 11. [Helix-FNO: Spectral-Domain Operator Learning Coupled with a High-Fidelity Mechanistic Model for Fast Surrogate Simulation](https://arxiv.org/abs/2609.22129)

**<font color=#1a73e8>作者：</font>** Jiabao Zhao, Chuwei Wang, Jinxi Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mechanistic simulation models of full-scale treatment processes remain the only trustworthy, extrapolative description of the underlying physico-chemical dynamics, yet their runtime is far too slow to support the thousands of forward evaluations that a modern decision engine requires at a 5-minute decision cadence. The standard remedy-surrogate modelling-often produces a network that learns a single solution for a single configuration, so it generalises poorly to new influent profiles, control settings or plant layouts. This paper presents Helix-FNO, a teacher-student architecture that couples a thirty-two-state mechanistic teacher with a Fourier neural operator (FNO) student. The teacher supplies a high-fidelity dataset of input-field-to-solution pairs, curated by Latin-hypercube and uncertainty-based active learning to cover the boundary and overload regimes that matter in practice; the student learns, in the spectral domain, the solution operator itself rather than any single solution, thereby moving from learning one instance to learning an entire family of equations. We give the operator formulation, the spectral convolution definition, the weighted distillation loss and the active-learning criterion, and we analyse the approximation error of a truncated Fourier expansion with respect to the smoothness of the parametric solution manifold. An illustrative study compares Helix-FNO against a physics-informed network and a data-driven recurrent surrogate on accuracy, dataset efficiency and inference latency, and places the methods on a speed-accuracy Pareto front. The resulting operator is three orders of magnitude faster than the mechanistic teacher at millisecond inference, which is precisely the capability required for massive candidate screening and online decision support.

---


### 12. [Hierarchical Bayesian optimization of an aircraft-based multi-agent system-of-systems](https://arxiv.org/abs/2609.22130)

**<font color=#1a73e8>作者：</font>** Paul Saves, Thierry Lefebvre, Nathalie Bartoli 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Developing innovative system architectures increasingly relies on advanced modeling and optimization techniques to frame the architecting process and define the corresponding computational problems. For complex System-of-Systems (SoS), high-fidelity multiphysics and multidisciplinary simulations are essential for capturing detailed behaviors. However, their computational expense and the risk of evaluation failures make direct optimization challenging. To overcome these limitations, surrogate-based approaches, like Bayesian optimization, have emerged as effective tools for managing expensive, black-box simulation tasks. This work introduces a hierarchical Bayesian optimization framework that leverages Gaussian process meta-modeling to handle discrete architectural choices, conditional dependencies, and heterogeneous design variables inherent to SoS problems. Results show that the hierarchical formulation improves search efficiency and robustness compared to conventional surrogate-based methods, enabling the exploration of large and structurally diverse design spaces with limited simulation budgets.
We apply the approach to an aircraft-based multi-agent system for wildfire suppression, a use case developed within the EU-funded COLOSSUS project that illustrates how SoS principles can coordinate heterogeneous aerial platforms with complementary roles, supporting both sustainable mobility and emergency response missions. Our framework provides a scalable methodology for SoS architecting and model exploration, offering transferable insights for applications in aviation, sustainable mobility, and resilience-oriented system design. By combining hierarchical representations with surrogate-based optimization, this work is among the first practical demonstrations of hierarchical Bayesian optimization applied to real-world SoS problems, advancing both methodology and practice.

---


### 13. [DiFA: Dual Evidence Fusion and Aggregation for Token-Level Text Anomaly Detection](https://arxiv.org/abs/2609.22136)

**<font color=#1a73e8>作者：</font>** Yanyu Qian, Pengcheng Weng, Yue Tan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text anomaly detection, the task of identifying text instances that deviate from normal language patterns, is crucial for language-driven applications. However, most existing methods can only perform document-level anomaly detection, making it hard to locate harmful phrases or support targeted prevention. Recently, there has been an emerging trend toward token-level text anomaly detection, which aims to address the above limitation by identifying anomalous words or fragments within a document. Nevertheless, one representative method mainly relies on representation-space distance measurement, neglecting the complementary roles of different anomaly cues in capturing diverse abnormal patterns. To bridge the gaps, we propose a Dual-evidence framework with adaptive Fusion and Aggregation (DiFA) for token-level anomaly detection. DiFA derives anomaly scores from form-structural and semantic views to capture visible structural abnormality and contextual inconsistency, respectively, thereby providing complementary evidence for identifying diverse anomalies. To combine these two scores with varying numerical scales, DiFA incorporates a calibration and fusion mechanism to adaptively balance the two views. Moreover, to obtain a discriminative document-level score, a multivariate aggregation method is designed to summarize token-level anomaly scores from multiple perspectives, preventing rare anomalous tokens from being diluted. Extensive experiments across various text anomaly detection benchmarks demonstrate that DiFA consistently achieves top performance while maintaining strong efficiency, robustness, and interpretability. The code and scripts are available at: this https URL.

---


### 14. [From Latent Biomarkers to Clinical Rules: Embedding-Guided Rule Mining and Attribution-Based Translation for Interpretable Tabular Learning](https://arxiv.org/abs/2609.22155)

**<font color=#1a73e8>作者：</font>** Majid Lotfian Delouee, Hamed Ayoobi, Sjors G. J. G. In 't Veld 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clinical decision support tools are most useful when accurate predictions are accompanied by understandable explanations. Rule-based models provide transparency, but rules derived directly from raw clinical measurements may miss patterns arising from interactions between multiple variables. We present a four-step pipeline that mines decision rules in the latent space of an FT-Transformer and translates them back into measurable clinical features. Embedding dimensions that consistently separate patient groups are treated as latent biomarkers, rules are mined using small decision trees, and selected rules are translated using gradient-input saliency and CLS attention attribution. We evaluate the framework on six public clinical and population health datasets at four embedding dimensions. Translated rules outperformed raw-feature rules in five of six datasets, with mean AUROC gains ranging from 0.04 to 0.23. On the heart disease dataset, embedding-space rules reached 0.98 AUROC, but translation reduced this to 0.72, showing that high-performing latent rules cannot always be represented by simple raw-feature conditions. These results show that latent-space rule discovery can uncover predictive patterns while translating them into clinically measurable features that can be evaluated by clinicians.

---


### 15. [Uncertainty and Business-Aware Remaining Useful Life Estimation for Semiconductor Manufacturing](https://arxiv.org/abs/2609.22160)

**<font color=#1a73e8>作者：</font>** Davide Frizzo, Francesco Borsatti, Gian Antonio Susto  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Semiconductor manufacturing relies on tightly interconnected components, so early identification of the assets most likely to fail is essential to prevent a single breakdown from disrupting the entire production pipeline. Maintenance planning must therefore balance unexpected failures against prematurely interrupted operating life. We present a Predictive Maintenance (PdM) framework combining Deep Learning (DL) sequence models and Simoultaneous Quantile Regression (SQR)
for uncertainty-aware Remaining Useful Life (RUL) estimation and risk-aware maintenance decisions. Several architectures are compared on ion-milling data from the 2018 PHM Data Challenge (PHM18), including architectures based on State Space Models (SSM), using prediction and business metrics: Unexpected Breaks (UB), Unexploited Lifetime (UL), and a cost-weighted objective. Diagonal State Spaces (S4D) delivers the best Remaining Useful Life (RUL) estimates across quantiles and, relative to Preventive Maintenance (PvM) baselines, substantially lowers business cost by avoiding systematically early interventions. The results support uncertainty-aware, cost-sensitive maintenance planning in semiconductor production.

---


### 16. [A Multi-Agent Pipeline for Source-Grounded Synthetic Note Generation from Longitudinal Structured EHR](https://arxiv.org/abs/2609.22164)

**<font color=#1a73e8>作者：</font>** Nina Fatehi, Reihaneh Hassanzadeh, Meysam Ghaffari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Structured EHR is abundant but sparse, coded, and difficult to use directly for note-centric clinical modeling. We present MedNotes, a multi-agent synthetic data generation pipeline that converts longitudinal structured EHR into source-grounded clinical note representations under explicit quality control. MedNotes treats structured-data-to-text synthesis as a closed-loop agentic process: a generator proposes a note, evaluator agents diagnose factual, coverage, structural, and hallucination-related failures, and a router accepts, revises, or rejects the draft. On 1,485 EHRSHOT encounters, MedNotes achieves a 91.4% pass rate, with mean factual accuracy of 0.980, completeness of 99.1%, structural fidelity of 0.761, and 0.028 critical hallucinations per encounter. Iterative refinement improves acceptance from 69.4% to 91.4%. The resulting synthetic corpus improves downstream CPT prediction and paragraph-level section prediction when combined with limited real data.

---


### 17. [TARGet: Topology-Aware Fusion-based Radio Frequency Circuit Functional Modeling using Graph Neural Networks](https://arxiv.org/abs/2609.22165)

**<font color=#1a73e8>作者：</font>** Soroosh Noorzad, Sebastian Bodero, Morteza Fayazi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automatic synthesis of analog and Radio Frequency (RF) circuits is an emerging area that requires an efficient circuit modeling method. In recent years, Machine Learning (ML) solutions have played a promising role in this regard. However, many existing ML approaches require separate training data for each circuit topology, even when a single circuit component is added or removed. In addition, they overlook circuit topology information, which limits their ability to capture complex component interactions. Furthermore, they rely on fully connected neural networks with flat feature representations, which require substantial amounts of training data. In this work, we propose an open-source topology-aware RF circuit modeling method, TARGet. Our model considers the circuit at two levels: sub-circuits and the overall circuit topology. At the sub-circuit level, TARGet leverages S-parameter representations to capture sub-circuit behavior rather than relying on individual circuit components, providing a reusable behavioral abstraction for RF building blocks. Moreover, TARGet explicitly incorporates circuit topology information into the model, enabling it to learn across multiple topologies. TARGet introduces a novel fusion-based architecture that integrates Graph Neural Networks (GNNs) and sub-circuit connectivity-aware neural networks to improve data efficiency. Experimental evaluation across multiple RF circuit topologies demonstrates that TARGet achieves sub-1% prediction error while reducing the required training data by up to 35.5x compared to state-of-the-art (SOTA) approaches. Furthermore, TARGet achieves 9.7x higher prediction accuracy under a strict 1% error threshold relative to SOTA models. A held-out matching-network evaluation further demonstrates zero-shot transfer to an unseen sub-circuit topology, where TARGet reduces NMAE by up to 45%.

---


### 18. [Clustering-Based Collective Anomaly Detection in IoT Systems: A Graph Neural Network Approach](https://arxiv.org/abs/2609.22166)

**<font color=#1a73e8>作者：</font>** Dalila Khettaf, Djamel Djenouri, Zeinab Rezaeifar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of Internet of Things (IoT) technology has led to the widespread deployment of smart, interconnected devices across a range of domains. However, this expansion has also resulted in a substantial increase in network traffic, creating more opportunities for malicious actors to launch cyberattacks and compromise sensitive information, thereby increasing the need for effective anomaly detection. The state-of-the-art in anomaly detection has predominantly focused on point anomalies. In contrast, the detection of collective anomalies remains relatively under-explored in the literature. In this paper, we introduce Unsupervised Graph Collective Anomaly Detection (UGCAD), a novel frame- work designed to identify collective anomalies in IoT network traffic. Unlike many existing methods, UGCAD operates on graph-structured data without any prior knowledge of group labels or membership. It leverages a variational graph autoencoder (VGAE) to learn the graph representation, which is subsequently used to enhance a clustering algorithm for effective grouping of nodes. To detect collective anomalies, clusters identified as normal are first aggregated and refined, after which anomaly scores are applied to detect collective anomalies. Extensive experiments conducted on the CICIoT2023 and ToN-IoT network datasets demonstrate the effectiveness of UGCAD in both clustering and collective anomaly detection (CAD). Furthermore, comparative evaluations against several traditional and state-of-the-art clustering-based CAD approaches confirm the superiority of UGCAD in accurately detecting collective anomalies.

---


### 19. [Role-Aware Morgan Fingerprints for Reaction Yield Prediction](https://arxiv.org/abs/2609.22167)

**<font color=#1a73e8>作者：</font>** Chinmay Mirji, Prashant Shekhar, Foram Madiyar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting reaction yield from molecular structure and reaction context can cut experimental trial-and-error and speed up condition screening in synthetic chemistry. Recent methods for this task use learned representations such as graph neural networks or Transformer encoders over reaction SMILES (Simplified Molecular Input Line Entry System), but these approaches carry heavy preprocessing overhead and can break when input formatting is inconsistent. We propose MFP, a reaction yield prediction method built on role-aware Morgan fingerprints where count-based circular fingerprints are computed for each reaction component, aggregated by chemical role (reactant, reagent, product), and combined with transformation-sensitive difference features into a fixed-length reaction descriptor fed to a feed-forward neural regressor. We test MFP against state of the art methods such as YieldBERT (with and without data augmentation) and GNAN (graph neural network) on the Suzuki-Miyaura and Buchwald-Hartwig benchmarks using a shared preprocessing and evaluation protocol. MFP reaches R2 = 0.878 on Suzuki-Miyaura and R2 = 0.969 on Buchwald-Hartwig while training an order of magnitude faster than graph- or Transformer-based alternatives. A formal complexity analysis confirms that MFP folds all representation cost into a one-time preprocessing step, removing the per-epoch message-passing overhead that graph methods carry. An ablation over fingerprint radius and folded vector length shows that radius-2 representations at nBits =2048 give the best balance of accuracy, speed, and cross-split stability on both datasets. These results establish MFP as an effective, reproducible, and efficient baseline for reaction yield prediction.

---


### 20. [Industrial Kinematic Trajectory Model (IKTM): Coordinate-Free Autoregressive Generator](https://arxiv.org/abs/2609.22173)

**<font color=#1a73e8>作者：</font>** Max Amiri, David Eyers  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mobility simulation supports logistics, safety, and communications planning in industrial environments such as ports, mines, and airports. Existing trajectory models, however, rely on absolute coordinates, road-network tokens, or semantic zones: representations that are site-specific and not well suited to unstructured industrial terrain. We introduce the Industrial Kinematic Trajectory Model (IKTM), a coordinate-free trajectory generator that represents industrial vehicle motion through kinematic sequences (speed and heading change) with no absolute spatial reference. IKTM uses an autoregressive causal transformer with probabilistic mixture heads and extends our prior coordinate-free Markovian model with deep sequence modelling and an explicit duration-conditioning signal. Trained on one site and evaluated zero-shot on three unseen sites, it matches the small-turn shape of the empirical turn-rate distributions of held-out telematics; across all four sites, the per-site mean Jensen-Shannon divergence over 100 sampling seeds spans approximately 0.035-0.050 bits under an oracle-length duration-target protocol and approximately 0.032-0.042 bits under a fully zero-shot prior-length protocol, with similar ranges whether out-of-distribution (OOD) duration targets are drawn from each held-out site's empirical length distribution or from the Site A prior. Both protocols stay above the metric's sampling-noise floor (<=0.0049 bits). Paired by site, the oracle-length values are 5.3-6.0x lower than those of a re-implementation of our prior Markovian model under the same 1 Hz protocol. Termination is duration-conditioned rather than spatial: rollouts stop on 100% of trials with a length-tracking error of +0.0 +/- 0.0 s against the sampled target (100 of 100 exactly on target; N=100, T=0.2, untouched in-distribution test split).

---


### 21. [SCoR: A Hierarchical Framework for Forecasting Relations Between Scientific Concepts](https://arxiv.org/abs/2609.22174)

**<font color=#1a73e8>作者：</font>** Jingze Wang, Fred Sun, Shangqi Guo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Anticipating emerging research directions is a critical goal of AI-assisted science. Existing methods mainly predict which concepts will co-occur in future papers, but co-occurrence captures shared attention rather than the scientific meaning of a connection, such as whether one method uses, combines, replaces, or contradicts another. We formulate research-direction discovery as hierarchical scientific-relation forecasting over a shared candidate-pair space, comprising three temporally aligned tasks: first co-occurrence, first scientific-relation formation, and relation type at formation. We construct SCoR-Graph from 187,848 cs.CV papers published between 2017 and 2026, yielding 270,687 consolidated concepts, 7.45 million co-occurrence edges, and 615,036 typed, directed relation edges. From cutoff-specific graph snapshots, we derive SCoR-Bench, a leakage-audited benchmark for these three capabilities, with expert-verified gold labels for the entire relation-type test set. We further introduce HiSCoR, a task-adapted model family that models relation emergence as a temporally evolving, hierarchically constrained process by encoding pre-cutoff event histories and conditioning relation formation on future co-occurrence. On the held-out 2025-2026 window, HiSCoR achieves an AUROC of 0.9515, a 2.4% relative improvement over the strongest temporal-graph baseline, and improves population-AUPRC by 14.0%; its relation-type variant achieves a Macro-AUROC of 0.7795. Ablations show that semantic, co-occurrence, and typed-relation views provide complementary predictive evidence. SCoR advances research-direction forecasting from predicting which concepts will co-occur to anticipating whether and how evidence-backed scientific relations will emerge.

---


### 22. [Contrastive World Models](https://arxiv.org/abs/2609.22175)

**<font color=#1a73e8>作者：</font>** Bonnie Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models trained via pixel reconstruction can struggle in visually complex environments, where irrelevant information dominates the objective and distract the model from information relevant to planning and control. We present Contrastive World Models, an approach for learning latent dynamics models without pixel reconstruction. Building on Dreamer, we replace observation reconstruction in the standard world model objective with a Deep InfoMax-like lower bound that maximizes the mutual information between state-action sequences and local patch features of future observations, encouraging state representations to retain information that is predictive of the future without requiring the model to reconstruct visually irrelevant details. We evaluate our approach in small-scale experiments across three settings of increasing visual complexity. Our method matches Dreamer and a momentum prediction baseline in the default setting, and substantially outperforms both once distractors or natural video backgrounds are introduced, while also training more efficiently by removing the pixel decoder entirely. Our approach is general and makes minimal assumptions beyond access to state-action sequences and future observations. These results suggest that contrastive, infomax-based objectives are a principled and promising direction for building world models that are robust to visual nuisance factors, a property particularly relevant for transferring model-based RL agents to the real world.

---


### 23. [OpenBlock: Constructive and Verified Content Generation for Adaptive Tile-Matching Games](https://arxiv.org/abs/2609.22177)

**<font color=#1a73e8>作者：</font>** Jiang Jun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tile-matching puzzle games serve hundreds of millions of players, yet the content-generation algorithms that decide which pieces to present at each turn remain proprietary, and no open platform exists for studying adaptive difficulty in this genre. We present an adaptive tile-matching platform whose central algorithmic contribution is a dual-track content-generation architecture: a deterministic rule-based generator that is always available, and an optional learned generator, both subject to a common verification gate that establishes, by exhaustive sequential-placement search, that every delivered piece set is fully placeable so the learned track can never degrade the constructive-feasibility guarantee of the rule track. A self-play reinforcement-learning placement agent, supervised by auxiliary tasks that expose per-shape placeability to shared representations, is used to diagnose the game's dominant failure mode: at high board fill, long-bar pieces lose the majority of their legal placements. Across 234,000+ self-play episodes the agent reaches a 35.6\% win rate (median score 4,200), and controlled simulation shows that at board fill rates of 70--75\%, 33--56\% of long-bar pieces have no legal placement, while spawn difficulty distributions are statistically indistinguishable between won and lost games---evidence that board-state degeneration, not content difficulty, drives late-game failure. Head-to-head ablations show that per-shape placeability supervision---not aggregate difficulty features---drives the representation gain, and a 14-day online gray rollout (48,000 players; sample-ratio verified, CUPED-adjusted) lifts day-1 retention by 1.8 percentage points and session duration by 7\% over the rule track alone, quantifying the neural track's asymmetric upside in live play.

---


### 24. [Gaussian Process Decorrelation for Spatiotemporal Deep Learning-Based Snow Water Equivalent Prediction](https://arxiv.org/abs/2609.22182)

**<font color=#1a73e8>作者：</font>** Colin Fenster, Adrienne Marshall, Soutir Bandyopadhyay 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the Western United States, snowmelt is essential to the agricultural industry in addition to being a key source of municipal drinking water. Consequently, accurate snowpack forecasting is critical for water policy and management. Automated Snow Telemetry (SNOTEL) stations provide accurate daily measurements of snow water equivalent (SWE) that exhibit strong correlations in space and in time. We tackle the problem of predicting future SWE values across the SNOTEL network.
Specifically, we use a Gaussian Process-based linear transformation to remove spatial correlations before training a long short-term memory (LSTM) neural network on the decorrelated SWE data. This approach allows the LSTM to learn a clean temporal signal at each station. We show that this separation of spatial and temporal components yields better predictive success than multiple baseline models.
Furthermore, we incorporate conformal prediction to quantify uncertainty in the resulting SWE forecasts, providing a distribution-free approach to illustrate a potential framework for establishing predictive intervals for spatiotemporal data. Together, accurate point forecasts and distribution-free uncertainty quantification provide a framework for SWE accumulation forecasting on subseasonal scales or projecting SWE with future data while motivating and supporting future work in predicting a large-scale, spatiotemporally complete SWE map.

---


### 25. [CleanScore: Black-Box Benchmark Audits with Negative Controls and Sensitivity Bounds](https://arxiv.org/abs/2609.22183)

**<font color=#1a73e8>作者：</font>** Jeffery Opoku, David Banahene  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Public benchmark scores may reflect skill, prior exposure to the questions, or both, and for most models the training data are unknown. We present CleanScore, a black-box audit using scored outputs only. Each benchmark question becomes a parent item with one public form and two independently written fresh forms preserving its numbers, facts and answer. The audit reports an interval for the public-form advantage rather than a verdict, and a private negative-control bank with an explicit transport radius separates exposure from ordinary form mismatch. A registered controlled-exposure experiment detects planted exposure and stays quiet under fresh-form exposure. A registered audit of five open models on 200 GSM8K and 200 ARC-Challenge items finds no exposure-consistent advantage, bounding surface-form inflation below five points. Registered positive controls then bound what such a null can mean. Leaking an item raises accuracy on paraphrases the model never saw almost as much as on the leaked wording, leaving 52% to 110% of the effect invisible to a paraphrase audit. On ARC a planted 49-point advantage shows an observable gap of -0.020, and about 20 points survive rewriting stem and options, across four training seeds. A surface-form null bounds far less than the phrase contamination audit implies.

---


### 26. [Adaptive Physics-Informed Neural Networks for the Blasius Boundary-Layer Problem](https://arxiv.org/abs/2609.22185)

**<font color=#1a73e8>作者：</font>** Mehari Fentahun Endalew, Xiaoming John Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) provide a mesh-free approach
for solving differential equations, but their performance can depend
strongly on loss weighting, collocation placement, and optimization
strategy. This study develops an adaptive PINN framework for the Blasius
boundary-layer equation using gradient-norm-based adaptive loss
weighting, nonuniform and residual-based collocation, and sequential
Adam--L-BFGS optimization. In the representative run using the
architecture $[1,100,100,1]$, the model predicts
$f''(0)=0.3320762918$, compared with the high-accuracy benchmark
$0.332057336215$, giving an absolute error of
$1.896\times10^{-5}$. The final weighted loss is
$6.789\times10^{-8}$, and the predicted stream-function, velocity, and
shear profiles agree closely with an independent numerical
boundary-value solution. A separate full-training architecture study
shows that the two-hidden-layer model achieves the smallest wall-shear
error among the four tested architectures, $1.629\times10^{-6}$,
whereas the deepest network attains the smallest weighted objective
but a substantially larger wall-shear error. Compared with the
previously reported PINN value $f''(0)=0.33165$, the representative
run reduces the wall-shear error by approximately a factor of $21.5$.
The results show that the combined adaptive training framework can
achieve high accuracy for the Blasius problem and that weighted loss
alone is insufficient for identifying the most physically accurate
PINN. Because the adaptive components are applied jointly, their
individual contributions cannot be isolated from the present results
and would require a controlled ablation study for separate assessment.

---


### 27. [Correlation-Guided Flow Matching with Annealed Masking for Spatial Transcriptomics Generation](https://arxiv.org/abs/2609.22187)

**<font color=#1a73e8>作者：</font>** Yupei Zhang, Hao Chen, Li Pan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatial transcriptomics (ST) provides spatially resolved gene expression profiling but remains expensive, motivating the prediction of ST from histology images. Generative models have emerged as a mainstream paradigm for ST prediction due to their ability to model the conditional distribution of gene expression and capture its inherent stochasticity. However, these methods typically treat genes as independent prediction targets and overlook the intrinsic gene-gene interactions in biological systems, which limits their ability to preserve biologically meaningful co-expression patterns. We argue that gene-gene interactions, which reflect shared pathways and regulatory mechanisms, are essential for generating numerically accurate and biologically coherent ST profiles. In this paper, we propose CorrFlow, a correlation-guided flow matching framework for histology-to-ST prediction that explicitly models gene-gene dependencies through two complementary mechanisms. First, we introduce an annealed masked flow matching strategy, where subsets of genes are progressively masked following a timestep-dependent annealing schedule, encouraging the model to infer masked genes conditioned on the remaining genes and promoting joint conditional modeling beyond per-gene marginal estimation. Second, we devise a gene graph-regularized optimization scheme that integrates prior knowledge from the STRING database and data-driven co-expression estimated by WGCNA to construct a gene affinity graph, which enforces both local consistency and global smoothness in the predicted expression. Extensive experiments across 12 datasets show that CorrFlow achieves the best average PCC and HPCC among evaluated methods, leading to more biologically coherent ST predictions.

---


### 28. [WildfireSpreadBench: The Metric Decides the Model in Wildfire Spread Prediction](https://arxiv.org/abs/2609.22191)

**<font color=#1a73e8>作者：</font>** Arin Gopakumar, Marco Pannozzo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning is being increasingly used to predict where active wildfires will burn the following day, helping inform evacuation boundaries and containment lines. Most models are evaluated using Average Precision (AP), which summarizes performance across all decision thresholds, although acting on a forecast requires choosing one. We benchmarked five discriminative architectures and one generative model on WildfireSpreadTS using a shared evaluation pipeline and two input configurations. We found that model rankings varied depending on whether performance was measured by AP or by threshold-dependent metrics like F1 and IoU. The highest-AP model flagged 4 to 5 times the area that burned and ranked fifth of six on F1 and IoU, and the most recall-heavy model flagged 16 to 23 times. Models with more usable predictions had AP scores 24 to 37 lower. Across architectures, we identified three distinct prediction profiles: over-predicting, balanced, and under-predicting, which AP alone could not distinguish. Expanding the input from 7 to 23 channels changed AP by 0.03 on average, against a 0.21 to 0.24 spread across architectures. These results show AP alone can favor models whose predictions are poorly suited for operational wildfire forecasting.

---


### 29. [SegTSim: A Big Data Driven Segmented Temporal Simulation Framework for Heterogeneous Multivariate Systems](https://arxiv.org/abs/2609.22192)

**<font color=#1a73e8>作者：</font>** Xinhang Li, Chenxi Geng, Yujia Sun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Heterogeneous multivariate time-series systems exhibit segment-specific nonlinear dynamics that challenge monolithic forecasting architectures. We propose SegTSim, a big-data-driven segmented temporal simulation framework that integrates segment-specific elasticity modeling with adaptive min-gating, dynamic production relocation optimization, multi-factor data fusion with exchange-rate propagation, and a deep ensemble validation pipeline. The framework is validated on US--Japan automotive trade data from USITC repositories spanning 2015 to 2025, comprising approximately 13000 annual records. Under a 25% perturbation scenario, Japanese import volume declines by 20.4% to 0.93 billion USD, while all output variables maintain coefficients of variation below 3.5% across 1000 ensemble inference runs.

---


### 30. [Prediction of Nonlinear Oscillations in a Jumping Quarter-Car Model Using Reservoir Computing](https://arxiv.org/abs/2609.22205)

**<font color=#1a73e8>作者：</font>** Masahisa Watanabe, Shiva Dixit, Nirmal Punetha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable prediction of vehicle dynamics is essential for smart driving applications such as autonomous control and advanced driver-assistance systems. Off-road vehicles used in agricultural and construction settings are particularly prone to nonlinear behavior, including bifurcations and chaotic motion arising from intermittent loss of tire--road contact. Predicting such dynamics is challenging because it requires resolving both smooth nonlinearities and the discontinuous switching associated with contact loss. In this work, we investigate the feasibility of reservoir computing (RC) -- specifically an echo state network (ESN) -- for data-driven prediction of a jumping quarter-car model. The reservoir is trained on time-series data from a small number of points and evaluated on its ability to reconstruct bifurcation diagrams, phase-space attractors, and time trajectories across periodic and chaotic regimes. The trained reservoir qualitatively reproduces the period-doubling route to chaos, captures the geometric structure of periodic and chaotic attractors. These results demonstrate that reservoir computing is a feasible data-driven predictor of nonlinear dynamics in a practical, non-smooth vehicle system.

---


### 31. [Schematize: An Agentic System for Generating and Refining Information-Extraction Schemas for Legal Research](https://arxiv.org/abs/2609.22209)

**<font color=#1a73e8>作者：</font>** Albert Sawczyn, Jakub Binkowski, Kamil Tagowski 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Empirical legal research often relies on turning research questions into structured data extracted from large collections of rulings and judgments. Designing the extraction schema and then extracting the data remain a manual, expertise-heavy bottleneck. We present schematize, an open-source multi-agent system that interactively turns a researcher's problem statement into a validated extraction schema that can later be used for autonomous extraction. Schematize couples (i) a clarification dialogue that elicits implicit expert intent, (ii) iterative schema generation, (iii) data-grounded refinement that tests the schema against documents, and (iv) chat-based post-editing. We evaluated the system with human legal professional, introducing our novel methodology, and schematize achieves top performance in most of tested configurations. While the system is designed to be domain-agnostic and applicable to any document collection, we tailor and evaluate it on legal research problems. We release schematize as a pip-installable Python package with full documentation.

---


### 32. [A Channel-Boosted Multi-Agent System with Iterative Consultation for Document Sensitivity Classification](https://arxiv.org/abs/2609.22212)

**<font color=#1a73e8>作者：</font>** Aleesha Zainab, Asifullah Khan, Muhammad Ahmed Khalid 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Organizations in critical national infrastructure sectors must assess heterogeneous documents for sensitivity before routing or storage. Manual assessment is slow, inconsistent, and unscalable. Extending our prior leakage-controlled benchmark, BERT established the top single-encoder baseline (89.14% accuracy, 89.33% F1-score under 5-fold cross-validation on the Strategic 16K corpus). However, transformer baselines suffer from a structural limitation: fixed input length truncation discards evidence beyond the retained window-precisely where sensitive cables tend to be longest. We present Channel-Boosted MAS (CB-MAS) and instantiate it as IC-MAS (Iterative Consultation Multi-Agent System) to solve this without long-context computational costs. A Channel Critic Agent learns document-adaptive trust weights governing Gated Channel Boosting between two first-window encoders, while paired Consultation Agents iteratively exchange belief states to reconcile evidence from the beginning and end of long documents. IC-MAS holds computation constant regardless of document length by reconciling fixed windows in a compact representation space. Ablation studies show critic-controlled Channel Boosting provides the bulk of accuracy gains, while consultation recovers recall without precision collapse. Critic-Controlled Gated Channel Boosting with Max-Pool fusion and Blackboard Adaptive Consultation achieves 90.72% accuracy, 91.23% F1-score, 92.01% sensitive recall, and 90.46% sensitive precision, using about 54% less average computation than a fixed-round baseline. Gains over the single-encoder baseline are statistically significant (McNemar's test, p less than 0.000001; paired t-test). We include LIME/SHAP explainability, multi-agent evaluation, and an honest accounting of limitations.

---


### 33. [SCoP: Structured Constraint Parsing for Evidence-Space Control in Temporal Knowledge Graph Question Answering](https://arxiv.org/abs/2609.22213)

**<font color=#1a73e8>作者：</font>** Xiaokun Guo, Zhen Xu, Dongdong Huo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Temporal Knowledge Graph Question Answering (TKGQA) requires answer inference from evidence that is both structurally valid and temporally admissible. Existing methods often leave anchor-event binding, temporal admissibility, and ordinal selection implicit in model reasoning, task-specific training, or similarity-driven retrieval, allowing locally relevant but invalid facts to enter the answer context. We formulate complex TKGQA as evidence-space control and propose SCoP (Structured Constraint Parsing), a constraint-centric framework that externalizes temporal decisions before answer inference. Instead of treating retrieved facts as admissible evidence by default, SCoP separates answer-seeking event patterns from temporal anchor events, conservatively grounds them to canonical TKG entities and relations, and translates temporal intent into executable constraints with optional ranking requirements. These constraints operate over normalized point and interval ranges, enabling deterministic filtering of structurally compatible candidates and producing a compact evidence space for generation. Experiments on MultiTQ and TimelineCronQ-R assess SCoP across timestamped point-fact and interval-oriented settings with richer temporal relations and ordering dependencies. Without task-specific parameter updates, SCoP achieves 0.825 Hits@1 on MultiTQ and 0.761 Hits@1 on TimelineCronQ-R, with gains on constraint-intensive question types. These results support explicit evidence-space control over unconstrained retrieval or implicit temporal reasoning.

---


### 34. [UniGIO: Unified Generative Global In-situ Weather Modeling from Spatiotemporal Incomplete Observations](https://arxiv.org/abs/2609.22217)

**<font color=#1a73e8>作者：</font>** Songru Yang, Zili Liu, Tao Han 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Global In-situ Observation (GIO) provides fine-scale, direct records of the global weather system from sparse point stations, making it an indispensable source for capturing localized and transient dynamics beyond the reach of satellite gridded data, and playing a critical role in key fields such as numerical weather prediction, disaster prevention, and agriculture. However, GIO exhibits strong spatiotemporal incompleteness, severely impairing accurate and real-time in-situ weather modeling. Unlike existing methods waiting for completed AI-ready data with extra introduced errors, in this work, we explore UniGIO, a novel generative framework for directly modeling global in-situ weather dynamics from native incomplete GIO. By generating missing data from observed ones annotated by masks, it unifies the coexisting forecasting, imputation, and generation under arbitrary missing ratios. Between the missing and observed, UniGIO captures station and region level complementarity through the Observation Mixer and Event Aligner, which diffuse discrete observations into continuous spaces where weather processes naturally span multiple stations. We further establish temporal dependencies with pattern shifts using the Adaptive Temporal Mixer, and track extreme events in chaotic local weather systems through a Mixture-ofExperts structure. Steady and extreme events are adapted in decoder by a Local Refiner. Extensive experiments on the up-todate largest global station weather dataset Weather-5K validate its SOTA performance with 11%, 12%, and 5% advantages on accuracy, fidelity, and extreme event capture, delivering a novel holistic solution for weather modeling in GIO networks.

---


### 35. [A Synthetic Multivariate Refrigerator Time-Series Dataset for Predictive Maintenance](https://arxiv.org/abs/2609.22229)

**<font color=#1a73e8>作者：</font>** Islam Benamirouche, Feriel Fass, Djemel Ziou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We generated synthetic multivariate time series for 27 refrigerators with a simplified physicsinspired simulator at one-minute resolution. The simulator includes ambient-temperature variation, door use, thermostat and compressor operation, heat exchange, defrost, electrical consumption, and six progressive degradation types. Each refrigerator provides 15 to 20 sensor outputs according to its configuration. The dataset contains 7,066,161 rows in 27 time-series files and 27 failure logs. The release also includes the Python generator, refrigerator configurations, and documentation. The data can support failure prediction, degradation analysis, and learning across refrigerators with different sensor-output sets.

---


### 36. [CNA: An AI-Oriented Comprehensive Normalized Assessment for Healthy Status and Application to Optimize RRT Strategies by Reinforcement Learning](https://arxiv.org/abs/2609.22232)

**<font color=#1a73e8>作者：</font>** Jiang Liu, Chan Zhou, Yujie Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Millions worldwide require Renal Replacement Therapy (RRT) as a treatment essential for survival. However, optimizing RRT strategies via AI is challenging due to heterogeneous patient dynamics, missing data, and the absence of an AI-oriented health assessment criterion. We propose an AI-Oriented Comprehensive Normalized Assessment (CNA) for healthy status and apply it to optimize RRT strategies by using offline reinforcement learning (RL). The key idea of CNA is transforming vital-sign distributions into a standard normal space, enabling a unified, data-driven health-status score defined by deviations from referent intervals, which also provides an AI-oriented criterion to assess strategy quality and supports RL termination. We further design a structured 23-dimensional state representation that integrates 19 indicators with 4 RRT descriptors, and employ matrix decomposition to reconstruct missing vital signs, improving data completeness for learning. These components are incorporated into multiple offline RL algorithms and validated via systematic ablation studies on RRT feature subsets. Compared with physicians' observed treatments, the best learned strategy reduces mortality from 13.2% to 5.0% (reducing 62.24%) and shortens average in-hospital stay from 308.5 to 250.1 hours (reducing 18.93%), demonstrating both methodological innovation and the potential of CNA-guided RL to improve RRT outcomes in nephrology.

---


### 37. [SCALE: Simulation-Calibrated Amortized Learning for Energy Materials (A hybrid architecture connecting deterministic modeling, real-world data, and transformer-scale inference for accelerated energy-materials discovery)](https://arxiv.org/abs/2609.22233)

**<font color=#1a73e8>作者：</font>** Kuan Huang, Bo Bai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Energy systems face converging pressures for security, affordability, resilience, and sustainability, creating a need for faster discovery of deployable energy materials. Here we introduce SCALE (Simulation-Calibrated Amortized Learning for Energy Materials), a physics-grounded, real-world-data-calibrated learning architecture that connects deterministic scientific operators, experimental calibration, expanded calibrated label generation, and transformer-scale inference. SCALE converts selected high-cost mechanistic computation and measured evidence into reusable models for rapid screening, ranking, inverse design, and active learning. We formulate the framework, identify ten method-based application regimes, and demonstrate SCALE for solid-state metal-hydride hydrogen-storage capacity prediction. In this implementation, a hydride phase-equilibrium capacity operator is calibrated against 381 measured ML-HydPARK capacity anchors and used to generate 5,000 candidate-condition-prototype teacher labels. A crystallographically anchored periodic-graph representation preserves atomic sites, periodic neighbor relationships, and local metal environments absent from formula-only encodings. An edge-biased graph transformer with 2.90 million parameters reproduces calibrated teacher labels with five-fold surrogate fidelity of MAE 0.0582 wt% H2, RMSE 0.0833 wt% H2, R2 = 0.9927, and Pearson r = 0.9963. Post hoc attention analysis suggests that SCALE learns chemically organized element groupings and metal-metal relationships consistent with established hydride chemistry, without chemistry-group labels as supervision. Once trained, SCALE shifts million-candidate evaluation from repeated deterministic workflow execution to batched learned inference, reducing per-candidate screening cost by approximately 10^7-10^8 while retaining links to simulation and experimental evidence.

---


### 38. [Not All Ranks Are Equal: Budget-Aware LoRA Merging Across Tasks](https://arxiv.org/abs/2609.22237)

**<font color=#1a73e8>作者：</font>** Avinash Amballa, Yashas Malur Saidutta, Wenbo Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Merging low-rank adapters (LoRAs) promises to eliminate the overhead of swapping task-specific weights at inference time. However, existing merging methods assume every layer needs the same rank budget. Further, some methods assume that rank budget needs to be split equally among the tasks too. We show this uniform-budget assumption is a major source of the performance gap between merged and per-task LoRAs. However, rank selection is an NP hard problem. To this end, we introduce Net Utility, a data free metric that first decomposes every task LoRA by its Singular Value Decomposition (SVD) and scores each of those singular directions by its task utility and its interference with other tasks directions. Next, we globally pool these scores to select singular directions with the highest values with a constraint on the total number of directions selected. The proposed Net Utility metric is applied on top of five different merging methods across three different merging spaces. The merging is done over two sets of tasks, vision and language tasks. Net utility based rank allocation outperforms its counterparts without that allocation. On average, over vision tasks it achieves +2.1% improvement in performance, and +2.2% improvement over the language tasks.

---


### 39. [Task-Aware Hybrid QUBO Optimization for Structured Neural Network Pruning](https://arxiv.org/abs/2609.22238)

**<font color=#1a73e8>作者：</font>** Osama Orabi, Artur Zagitov, Hadi Salloum 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural network pruning can be formulated as a combinatorial optimization problem, yet many existing approaches rely on independent filter-importance scores or simplified objective functions. In this work, we propose a Hybrid Quadratic Unconstrained Binary Optimization (QUBO) framework for structured filter pruning that combines task-aware sensitivity information with interactions between candidate filters. The formulation incorporates first-order Taylor sensitivity and Weight-Fisher sensitivity into the linear component of the objective and can additionally incorporate activation similarity into the quadratic interactions. To control the target pruning cardinality without introducing an explicit quadratic cardinality penalty, we use a binary search over the capacity incentive to identify a coefficient that empirically yields the target pruning cardinality. We further investigate a two-stage QUBO--Tensor-Train refinement strategy in which the QUBO solution initializes gradient-free probabilistic black-box optimization to search for improved pruning masks using the downstream metric. Experiments on the SIDD image denoising task and a Half-UNet model show that the Hybrid QUBO achieves higher PSNR and SSIM than the evaluated Taylor and L1-based QUBO baselines at the studied pruning target. Multi-seed experiments under a fixed dataset protocol are used to assess robustness, while controlled sub-problem experiments demonstrate that Tensor-Train refinement becomes increasingly valuable as the combinatorial problem size grows. The results support Hybrid QUBO as a task-aware structured pruning framework for the evaluated setting, while also highlighting the computational and deployment limitations of mask-based pruning.

---


### 40. [Statistical Inference for Adversarial Training: Central Limit Theorems via Optimal Transport](https://arxiv.org/abs/2609.22240)

**<font color=#1a73e8>作者：</font>** Kim Jakwang, Kwon Dohyun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The purpose of this paper is to rigorously quantify the statistical and learning-theoretic properties of adversarial training models for classification. Equivalently, we establish the statistical properties of empirical optimal partial transport. Precisely, first we provide two types of central limit theorems (CLT): CLT centered at the expected empirical value, and CLT centered at the population one with smoothing. These results are based on the uniqueness of optimal potential for various equivalent optimal transport formulations, and the empirical process theory argument. For the binary setting, we indeed prove the uniqueness of optimal potential by leveraging the connection between optimal partial transport and the derived multi-marginal optimal transport formula. As byproducts, we also obtain the stability of a saddle point of the adversarial training model, and the sample complexity and concentration probability of the generalization error.

---


### 41. [Universal Observatory Graphs for Distributed Sky Coverage and Artificial Intelligence Based Interplanetary Routing](https://arxiv.org/abs/2609.22244)

**<font color=#1a73e8>作者：</font>** Mohammed Abdel Razek  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This research proposes the Universal Observatory Graph (UOG), an AI-driven framework for distributed astronomical observation across the Solar System. The proposed architecture models autonomous observatories located at the Sun planet L2 Lagrange points as nodes in a weighted graph, while communication links are represented as graph edges characterized by multi-objective physical and operational metrics, including interplanetary distance, communication latency, transmission power, and link reliability. The resulting graph provides a unified mathematical representation of a cooperative interplanetary observatory network. This proposal examines a six-observatory Solar System configuration comprising Earth, Mars, Jupiter, Saturn, Uranus and Neptune. Instantaneous sky coverage is evaluated independently using a 200,000 direction Fibonacci sphere, a 2,000,000 direction fixed seed Monte Carlo calculation and deterministic spherical integration. All three methods yield complete network union coverage, approximately 0.43% complete six observatory intersection and approximately 24.96% mean pairwise Jaccard similarity under the adopted pointing model. Communication routing is subsequently formulated as a finite horizon Markov decision process and solved using tabular Q-learning. The reward balances node participation and a distance dependent reliability proxy against distance, light time latency and a distance squared transmission power proxy. The learned Earth-Saturn-Uranus-Neptune route is also the highest discounted return route among all 41 feasible simple paths under the four hop constraint. The framework provides a reproducible baseline for sequential coverage assessment and multi objective routing; time dependent ephemerides, mission specific visibility, calibrated link budgets and scalable graph policies remain future work.

---


### 42. [A Tutorial on Prompt Engineering: From Messy Thoughts to AI Workflows](https://arxiv.org/abs/2609.22249)

**<font color=#1a73e8>作者：</font>** Erfan Loweimi, Hadi Daneshvar, Samira Loveymi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper treats prompt engineering as a discipline for turning informal human intent into structured AI work specifications. It develops the practice as a sequence of reusable design moves: define the work, construct only the context the answer depends on, choose a role, or a moderated panel of roles, as an attention lens, and state affirmative quality targets, reserving prohibitions for hard boundaries. To keep prompts lean, it adapts two classical principles, Occam's razor and Chekhov's gun, so that every instruction earns its place. For consequential tasks, it adds structured critique through steelmanning and premortems, followed by verification and, where tools or multi-step actions are involved, agentic operating loops with explicit boundaries and escalation. Aimed at a general readership, this tutorial is not a benchmarking study; it offers a practical, technically grounded path from casual prompting to disciplined AI workflow design, illustrated by a worked example that carries one task from a weak prompt to a strong specification. The framework is presented as principles and checklists that remain useful as models and tools change. The strongest prompt is rarely the longest prompt; it is the one that makes desired behaviour, required sources and checks, and success criteria unmistakable.

---


### 43. [Predictors and Orchestrators: Parsimonious Machine Learning within an Agentic AI Harness for Multi-Horizon Karst Aquifer Forecasting](https://arxiv.org/abs/2609.22251)

**<font color=#1a73e8>作者：</font>** Pramod Lekhak, Chetan Sharma, Hakan Başağaoğlu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Forecasting karst aquifer dynamics is difficult because recharge responses are nonlinear, event-driven, and governed by strongly heterogeneous flow paths. This study develops and evaluates a deployment-aware framework for 1-12-week-ahead prediction of spring discharge and groundwater level using approximately 79 years of hydroclimatic observations from the Edwards Aquifer, Texas. Five model families were compared under a common temporal evaluation design: extreme gradient boosting, extremely randomized trees, long short-term memory, convolutional neural networks, and Transformers. Predictions were evaluated using coefficient of determination, Kling-Gupta efficiency, root-mean-square error, and agreement with operational drought thresholds. Extreme gradient boosting was consistently most reliable, with R2 at least 0.97, 0.96, and 0.94 across 1-4-, 5-8-, and 9-12-week horizons, respectively, and greater than 90% critical-stage agreement at the first three drought stages across all horizons. Deep models were competitive at short horizons but degraded progressively and exhibited isolated failures at longer lead times. We attribute this contrast to an alignment between tree partitioning and low-dimensional, axis-aligned hydroclimatic predictors, together with the tendency of neural models to smooth irregular extremes. The validated models were embedded in a five-agent operational architecture that automates data acquisition, model assignment, deterministic prediction, threshold monitoring, prospective verification, literature retrieval, and reporting. The contribution is therefore a transferable framework joining parsimonious model selection, leakage-aware multi-horizon evaluation, decision-relevant threshold skill, and auditable agentic automation.

---


### 44. [DIPLOMAT: Dialogue-Span-Aware Direct Preference Optimization for Polite Persuasive Workplace Negotiation Dialogues](https://arxiv.org/abs/2609.22256)

**<font color=#1a73e8>作者：</font>** Bibhuti Jha, Rishikant Chigrupaatii, Priyanshu Priya 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Effective workplace negotiation requires balancing multiple objectives, including achieving task goals, preserving professional relationships, and resolving conflicts constructively. However, misunderstandings, misaligned preferences, and interpersonal friction often impede successful outcomes. Politeness mitigates these challenges by fostering trust, reducing tension, and preventing escalation, and persuasive communication helps overcome resistance, align preferences, and guide participants toward mutually beneficial agreements. Motivated by these insights, we present DIPLOMAT, a dialogue system for polite and persuasive workplace negotiation. To support its development, we introduce PROWESS, a dataset of multi-turn workplace negotiation dialogues generated via a multi-agent framework and enriched withnegotiation strategies, politeness levels, persuasive strategies. DIPLOMAT is trained using Dialogue-Span-Aware Direct Preference Optimization (DSA-DPO), a novel preference learning objective that identifies key dialogue spans for preference alignment. This enables DIPLOMAT to generate contextually coherent responses that employ intended negotiation strategies, maintain politeness, and incorporate effective persuasion strategies throughout interactions. Automatic and human evaluation on PROWESS confirm that DIPLOMAT consistently outperforms baselines in generating coherent, polite, and persuasive negotiation responses.

---


### 45. [Which Part of the Context Layer Does the Work? Separating Semantic Content from Retrieval Scaffolding in Text-to-SQL Agents](https://arxiv.org/abs/2609.22259)

**<font color=#1a73e8>作者：</font>** Qing Ye  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Context layers, curated documentation that an analytics agent fetches at query time, produce large accuracy gains on text-to-SQL benchmarks. A with/without comparison cannot say which part of the layer does the work: the semantic content, the retrieval scaffolding that delivers it, or the pre-computed views that usually accompany it. We report a four-arm ablation on DABStep on four models that separates the three. The instrument is a data contract: a YAML artifact that carries a domain's semantics and the rules an agent's tools enforce. One arm empties every field of prose in the frozen contract while holding the tool surface, retrieval instruction, table allow-list and operation rules byte-for-byte fixed. Compiling the contract's own SQL expressions into views gives the ceiling a pre-computed layer would reach: gold on all 176 tasks it covers. Content dominates. It raises hard-task accuracy from 13.9% to 55.1%, 22.6% to 56.6%, 22.9% to 68.4% and 37.0% to 77.4%, beating the same knowledge pasted into the prompt on every model. Scaffolding without content is worth 0 to 5 points on two flash models and 14 to 15 on two frontier models. Against the compiled ceiling the contract arm's shortfall is a failure to derive, and it falls from 39 points to 5 with model capability. The contract beats the prompt because the rule it needs is one lookup away rather than buried in a long prompt: its SQL carries the fee semantics up to 98% of the time against the prompt arm's 4%, and at the lowest cost per correct answer on three of four models. For practitioners: semantics first, scaffolding second, pre-computed macros only where an agent demonstrably fails to derive. Ungoverned arms submitted 166 mutating statements; governed arms none. The gain is confined to the contract's domain. On one model the benchmark's own withheld golds grade the contract arm at 51.9% against 18.8% for the prompt baseline.

---


### 46. [Did You Steal My Shot? Pioneering Camera Motion Plagiarism Detection in Generative Videos](https://arxiv.org/abs/2609.22267)

**<font color=#1a73e8>作者：</font>** Chengguo Zhang, Ping Ping  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera motion often reflects directorial intent and requires professional equipment, making it a high value form of intellectual property. However, generative video models can imitate such high value camera motions with simple prompts, while existing similarity detection methods mainly operate on visual content and fail to capture deeper motion similarity. This is mainly because their training data entangles camera motion with visual content. Moreover, traditional optical flow is insufficient to represent complex camera motions. We therefore build the first benchmark for camera motion analysis, including a motion dataset with \textbf{11} motion styles and evaluation protocols. Furthermore, we propose a motion representation that augments optical flow with vorticity cues from fluid dynamics, thereby better capturing motions. Experiments show that our detector achieves a \textbf{3.02*} improvement in plagiarism detection over the strongest baseline and remains effective on generative videos. We believe our work extends copyright protection beyond static content to dynamic camera motion.

---


### 47. [Enabling Vision and Cross-Modal Learning for Multimodal Stroke Recurrence Prediction: An Interpretable Two-Step Framework](https://arxiv.org/abs/2609.22271)

**<font color=#1a73e8>作者：</font>** Christian Gapp, Elias Tappeiner, Martin Welk 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal stroke recurrence prediction requires effective integration of heterogeneous clinical and imaging data, yet modality imbalance often causes models to over-rely on dominant modalities and underutilize complementary information. While self-supervised pretraining and selective parameter freezing are commonly employed to improve representation learning and fine-tuning stability, their effect on modality contributions and cross-modal behavior in multimodal medical models remains largely unexplored. In this work, we investigate whether image pretraining on 3D CTA scans reduces modality imbalance and improves cross-modal integration for stroke recurrence prediction, a clinically critical task we recently addressed. To this end, two multimodal neural networks are pretrained in a self-supervised manner and subsequently fine-tuned using two distinct freezing strategies. Their performance and modality utilization are compared against both the baseline model from our previous work and models trained entirely from scratch in this study. Our results demonstrate that self-supervised pretraining enables more effective utilization of the multimodal image-tabular dataset, outperforming both the prior baseline and all non-pretrained models. Notably, the best-performing Vision Transformer based neural network successfully overcomes unimodal collapse. Synergy analysis reveals significant interactions between vision and both gender and CHD, suggesting clinically relevant patterns for stroke recurrence. Overall, our findings demonstrate that self-supervised pretraining and strategic fine-tuning support more balanced modality utilization and enable meaningful cross-modal interactions. Code is publicly available at this https URL.

---


### 48. [An Affordable AI-Integrated Smart Cane for Multimodal Mobility Assistance of Visually Impaired Users](https://arxiv.org/abs/2609.22277)

**<font color=#1a73e8>作者：</font>** Ali Akarma, Adeel Ahmad, Toqeer Ali Syed  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Visual impairment affects over 2.2 billion people worldwide, yet conventional white canes cannot detect elevated hazards or provide semantic environmental context. Existing AI-assisted navigation systems typically rely on expensive hardware or cloud connectivity, limiting accessibility in resource-constrained settings. This paper presents an affordable (\$88 USD), fully offline AI-integrated smart cane designed for multimodal mobility assistance on an ultra-low-power Raspberry Pi Zero 2W. The system fuses RGB vision sensing with Time-of-Flight (ToF) distance estimation, pairing an INT8-quantized SSD MobileNet V1 model with distance-aware vibrotactile feedback and real-time audio alerts. To ensure operational robustness on constrained hardware, a multiprocessing architecture isolates sensor acquisition, neural inference, and haptic feedback into independent processes with fail-safe sensing support. Experimental evaluation across indoor mobility scenarios demonstrates a macro-averaged F1-score of 0.82 (precision: 0.85, recall: 0.81), a mean end-to-end latency of 330\,ms, and a peak power draw of 2.8\,W. A preliminary usability study with 12 participants (SUS: 78.5, NASA-TLX) demonstrated positive user perception and enhanced obstacle awareness. The proposed prototype validates the feasibility of deploying privacy-preserving, edge-native assistive intelligence for cost-sensitive mobility assistance.

---


### 49. [Brain-to-Image Generation: Reconstructing Visual Stimuli from EEG using Generative Adversarial Networks](https://arxiv.org/abs/2609.22282)

**<font color=#1a73e8>作者：</font>** Harshit Goyal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing visual stimuli from electroencephalography (EEG) is difficult because scalp measurements have high temporal but limited spatial resolution, and paired EEG-image datasets remain small relative to modern generative-model training corpora. We present a reproducible single-subject baseline on THINGS-EEG2 that first tests the more defensible question of whether EEG can retrieve the viewed stimulus in a visual embedding space. A compact temporal-spatial convolutional encoder maps repetition-averaged EEG (63 by 250) to provided 512-dimensional ViT-B/32 image features. Model selection uses a concept-disjoint validation split, and final evaluation uses the official 200-image, 200-concept test gallery. Across three training seeds, the model obtains 12.83 +/- 0.58%, 39.17 +/- 1.76%, and 58.00 +/- 1.73% image recall at 1, 5, and 10 (mean +/- sample standard deviation), compared with analytical chance levels of 0.5%, 2.5%, and 5.0%. A session-balanced ablation shows that averaging more test repetitions generally improves ranking. Applying the Subject 01 model to the other nine subjects without adaptation causes a sharp performance drop, exposing subject specificity. We further report exploratory stress tests of direct conditional generators trained without external visual weights: single-subject and ten-subject variants produce noise-dominated outputs, with early validation improvements reversing after one to four epochs. Finally, we distinguish direct reconstruction from semantic rendering with a pretrained diffusion prior. The results support above-chance coarse semantic decoding under a closed-set, repetition-averaged protocol, but do not support faithful recovery of stimulus pixels.

---


### 50. [Rethinking Streaming Video Diffusion Model: Context, Execution, and Training](https://arxiv.org/abs/2609.22283)

**<font color=#1a73e8>作者：</font>** Hongchen Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding the design space of streaming video diffusion is essential to exploring its potential for generation quality and computational efficiency. We develop a unified analytical framework that relates model and sampler choices, historical conditioning, execution scheduling, and training strategies. The framework accommodates a broad family of causal context-selection policies and makes their computational dependencies and training-inference alignment explicit. Within this design space, we study three representative policies: clean, same-level, and progressive history. On the full VBench prompt set, same-level and progressive history achieve aggregate scores of 85.24 and 85.60, respectively, compared with 84.45 for the clean-history reference. Long-video comparisons further show improved subject consistency and more coherent motion with progressive history. By allowing multiple denoising nodes to be processed together, progressive-history pipelining achieves $1.57$-$2.83\times$ steady-state DiT speedups under our evaluated conditions. We additionally find that LoRA adaptation of the DMD fake-score network improves generation quality using only 2.15% as many trainable fake-score parameters as full-parameter adaptation. Together, these findings show that fully denoised history is not a prerequisite for high-quality streaming generation and motivate the joint design of historical conditioning, execution, and training.

---


> [!TIP]
> 当前位于：**1-50**（第 1/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-463](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
