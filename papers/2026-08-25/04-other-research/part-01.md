# 📦 其他研究 | 2026年08月25日

> 本类共 **158** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-158](./part-04.md)

---

### 1. [Bankruptcy Prediction via Hybrid Resampling and Stacking Ensemble Techniques with Explainable Artificial Intelligence (XAI)-Driven Analysis](https://arxiv.org/abs/2608.20343)

**<font color=#1a73e8>作者：</font>** Obu-Amoah Ampomah, Edmund Fosu Agyemang, Kofi Acheampong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study develops and evaluates a bankruptcy prediction framework that integrates consensus-based feature selection, hybrid resampling, stacking ensembles, and explainable artificial intelligence to improve minority-class detection in severely imbalanced financial data. Using the Taiwanese Bankruptcy Prediction dataset from the UCI Machine Learning Repository, five feature-selection algorithms were first applied, and a consensus retention rule reduced the input space to 23 robust variables. The balanced training data were then generated using SVM-SMOTE, SMOTE-Tomek, and SMOTE-ENN. Five ensemble machine learning classifiers, namely gradient boosting, extreme gradient boosting, histogram-based gradient boosting, LightGBM, and AdaBoost, were compared with five deep learning models, including RNN, LSTM, GRU, DNN, and MLP. In addition, hybrid stacking ensembles combined the five machine learning classifiers as base learners with each deep learning model as a meta-learner. Model performance was assessed using accuracy, recall, specificity, G-mean, and ROC-AUC, while SHAP was used to explain feature contributions. The results show that resampling strategy materially shaped model behavior. SVM-SMOTE and SMOTE-Tomek favored accuracy and specificity, whereas SMOTE-ENN delivered stronger minority-class detection. Among standalone models, the GRU with SMOTE-ENN achieved the best overall predictive balance, with recall of 0.8627, G-mean of 0.8517, and ROC-AUC of 0.9431. Among stacking ensembles, SMOTE-ENN with (GB+XGB+HGB+LGBM+AB)+LSTM provided the strongest compromise between sensitivity and specificity. SHAP analysis identified leverage, profitability, solvency, and operational efficiency indicators as the most influential predictors of bankruptcy risk. These findings support more reliable and interpretable early warning systems for financially distressed firms.

---


### 2. [Building and Evaluating a Synthetic Bengali Speech Resource for Telecom Customer Care](https://arxiv.org/abs/2608.20346)

**<font color=#1a73e8>作者：</font>** Kawshik Kumar Paul, Md. Nafiul Alam Fuji  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech systems used in customer-facing applications often require domain-specific language coverage. We present a synthetic Bengali speech dataset for telecom customer-care scenarios. The dataset contains 10,000 audio-text pairs, approximately 26.82 hours of 24 kHz speech, and predefined train, validation, and test splits of 9,000, 500, and 500 examples. It is publicly released on Hugging Face under the CC-BY-4.0 license. The speech was generated with OmniVoice in voice-cloning mode using a real female reference recording and transcript, with bfloat16 precision, 16 diffusion sampling steps, and a speaking-rate control value of 1.0. Along with the original Bengali text, the dataset provides a normalized transcript field designed for ASR/STT training and evaluation. We report an automatic intelligibility check over all 10,000 samples using a domain-adapted Whisper ASR model fine-tuned from bengaliAI/tugstugi_bengaliai-regional-asr_whisper-medium, along with a manual listening check on selected samples. The evaluation gives an average WER of 2.54%, an average CER of 0.59%, and median WER and CER values of 0.00%. These results suggest strong text-audio consistency under the selected automatic evaluation pipeline, while the paper also discusses the limitations of synthetic speech and STT-based evaluation.

---


### 3. [How to Train a Real-World Silicon Concierge? Internalizing Complex Business Workflow to Only OneModel](https://arxiv.org/abs/2608.20350)

**<font color=#1a73e8>作者：</font>** Chang Liu, Chaoyang Ning, Dayi Jiang 等 35 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Traditional industrial agents rely on modular pipelines, including Router, Retriever, Planner, Executor, Responder, Reviewer, and other components. These systems often fracture into a labyrinth of ad-hoc patches, leading to cascading errors and high latency. We propose OneModel, an applicable paradigm shift from external workflows to internalized knowledge representation. Unlike modular systems that slice fluid user intents into static steps, OneModel consolidates complex business logic and SOPs directly into the model parameters. Through Continual Pre-training (CPT) and logic-compilation SFT, we transform fragmented business rules into intuitive model reasoning within a unified attention space. Deployed in our global financial service system, OneModel effectively breaks the trade-off between latency, accuracy, and complexity. Online A/B testing demonstrates an end-to-end latency reduction of more than 50 percent, from 18.7 seconds to 8.0 seconds, while the Intelligent Resolution Rate (IRR) increases from 64.3 percent to 83.3 percent. The results show that OneModel can replace brittle engineering logic with internalized cognitive intuition, offering a scalable blueprint for transitioning industrial agents from complex, error-prone workflows to unified model architectures.

---


### 4. [The Divergence Hypothesis: Unmasking Lexical Interference and Label Bias in Mental Health NLP](https://arxiv.org/abs/2608.20353)

**<font color=#1a73e8>作者：</font>** Moustafa Yehia Hassan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Computational mental health (CMH) classifiers often degrade under distribution shift because human annotators and distant-supervision pipelines reward different linguistic signals. We introduce TSS (Triple-Stream Stress probe), a multi-channel diagnostic framework that decomposes text into (A) lexical character n-grams, (B) a small, mostly content-free morpho-syntactic channel, and (C) a 154-feature psycholinguistic style channel. Across four English datasets (N=12,906), TSS reveals a lexical interference effect: adding lexical features to the style channel reduces Macro-F1 on human-labeled data (mean drop 0.072, p<10^-4) but not on auto-labeled data. We propose Degree of Divergence (DoD), a difference-in-differences statistic adapted from econometrics for label-source auditing, with instance-level bootstrap inference; the headline estimate is DoD(BC-A) = 0.0374, 95% CI [0.0097, 0.0651], p=0.0032. A platform-stratified Twitter-only DoD (which removes the Reddit vs. Twitter contrast) reproduces the pattern with bootstrap inference: DoD-Tw(BC-A) = +0.096 (p<0.001) and DoD-Tw(AC-A) = -0.089 (p<0.001). Interventional masking (pos_only) retains ~95-99% of Channel C's performance after destroying content words on human datasets, indicating that the style channel does not rely primarily on lexical surface form. TSS is positioned as a diagnostic audit framework, not a clinical screening tool: it flags label-source-specific shortcut learning before generalization claims are made.

---


### 5. [Research Paper Quality Recognition Through Textual Feature Analysis](https://arxiv.org/abs/2608.20368)

**<font color=#1a73e8>作者：</font>** Saikiran Korla, Sadwik Gummadavelli, Trung-Nghia Le 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge and innovations are shaped by using the quality and credibility of the scientific research. Yet, distinguishing between impactful, high-quality work and flawed studies remains a challenge. This paper introduces a benchmark for classifying research papers into two categories: good (highly cited) and non-good (retracted), using only textual features from titles and abstracts. We evaluate multiple embedding techniques, including SBERT, Word2Vec, FastText, USE, and TF-IDF, combined with classifiers such as Support Vector Machines (SVM), Random Forests, and Neural Networks. Our contributions include: (1) hyperparameter transparency, (2) feature space visualizations using t-SNE, (3) model interpretability analysis with SHAP, and (4) detailed examination of error cases. Experimental results show that a neural network with SBERT embeddings achieves 87.22\% accuracy, while FastText combined with SVM reaches 91.12\%. These findings highlight the value of textual information in assessing research quality, with ethical considerations for deployment. This work contributes toward the development of academic integrity tools that promote trustworthy scholarship.

---


### 6. [Interpretable Multimodal Classification with Linear Discriminant Tree Ensembles](https://arxiv.org/abs/2608.20384)

**<font color=#1a73e8>作者：</font>** Mojtaba Moattari  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal affect and behaviour classifiers that fuse heterogeneous text, audio, and visual streams must simultaneously achieve competitive accuracy and produce human-understandable explanations of the cues driving their decisions -- a dual objective that current high-capacity models, notably Transformers, only partially address. While Transformers attain strong predictive performance, their distributed representations and deep nonlinearity make it difficult to assign meaningful importance weights to individual multimodal features, limiting their use in trust-sensitive applications such as clinical affect monitoring and educational assessment. We address this gap by developing a framework based on tree-based ensembles that balances accuracy and interpretability. The framework encodes each modality into tokens, extracts and clusters concepts to reduce dimensionality, routes the fused modalities through tree-based ensemble classifiers, and interprets trends using a novel modified feature importance metric. The modified importance reduces the influence of the negative class in binary classification tasks, thereby improving indicator or marker detection. The proposed tree-based ensembles -- Linear Discriminant Tree (LDT), Linear Discriminant Forest (LDF), and Linear Discriminant AdaBoost (LDAB) -- achieve F1-mod gains of 4.3\% over the Multimodal Transformer and accuracy gains of 3.0\% over the primary interpretable multimodal baseline, Interpretable Multimodal Routing (IMR). The proposed multimodal feature importance extracts salient inter-modal concepts with substantially higher human-annotator agreement scores than default feature importance (62.2\% vs.\ 43.2\% on IEMOCAP; 46.7\% vs.\ 32.1\% on CMU-MOSI).

---


### 7. [Representation Affects Retrieval: A Case Study of Skill Discovery and Routing in a Multimodal Agent Harness](https://arxiv.org/abs/2608.20389)

**<font color=#1a73e8>作者：</font>** Kevin Dela Rosa  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A production agent harness must discover and rank, from a growing library of skills, the one most appropriate for a user's task. At small scale this selection happens in context: the LLM planner chooses among skill representations exposed in its system prompt, without an explicit embedding-based retrieval step. We treat this in-context selection as the small-N counterpart to embedding-based skill retrieval at scale, and present a case study of how Tinycloud, a production multimodal video agent harness, represents its skills for the planner. The harness ships skills under two recurring representations: tool-skills that wrap a single external API or system tool and serve as primitive vocabulary, and workflow-skills that orchestrate tool-skill calls plus a template render to produce one named deliverable. The harness exposes them via two surfaces in the system prompt: an inlined-body surface (full instructions, scripts, templates) for autoloaded skills, and a one-line listing for on-demand skills. A six-task selection ablation across three exposure regimes (all-on, default, all-off) shows that full autoload selects the gold skill on every task; all-off slows execution and produces hard discovery failures; and the production default misroutes one task because its lexical signal collides with an autoloaded tool-skill that pulls planner attention away from a listed workflow-skill. The headline finding is that in-prompt exposure of skills is not monotonically helpful: partial exposure can create lexical competition that suppresses correct selection. We connect this small-N observation to recent retrieval-based skill-routing work at large scale, and frame this contribution as a case study rather than a benchmark.

---


### 8. [Self-Supervised Speech Representations Track Spoken Language Convergence to Adult Models in Infants and Children Who Are Deaf/Hard-of-Hearing](https://arxiv.org/abs/2608.20396)

**<font color=#1a73e8>作者：</font>** L. Choy, A. S. Khan, S. Patrizi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language development is characterized by a gradual convergence of children's speech toward adult patterns. Measuring this process has traditionally required detailed transcription and language-specific expertise, limiting scalability across languages and populations. Here, we use speech embeddings to capture this convergence directly from the acoustic signal in longform, child-centered recordings, taken as children go about their daily lives. Using HuBERT-BASE, we extracted embeddings from speech vocalizations of children who are deaf/hard-of-hearing and their female adult caregivers ($>$925 hrs. observation). Embedding distance between children and caregivers decreased with hearing age, controlling for pitch and vocalization length, indicating, as expected, that children's speech patterns converge to caregivers over development. This single distance metric likewise related to multiple standardized measures of speech and language from infancy through preschoolhood. These results suggest a path toward scalable, language-neutral assessment of spoken language development from children's everyday lives.

---


### 9. [When Retrieval Fails Before It Begins: Structurally Indirect Prerequisite Eviction as a Retention Failure in Agentic Memory](https://arxiv.org/abs/2608.20400)

**<font color=#1a73e8>作者：</font>** Minkyu Song  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic memory under a fixed budget involves two stages: retention and retrieval. Existing retrieval-centered paradigms implicitly assume necessary evidence survives eviction, but we challenge this by isolating a pre-retrieval failure mode: structurally indirect prerequisite eviction, in which upstream blocks weakly aligned with the query are discarded under budget pressure. We provide an operational definition of this failure, a reproducible deterministic benchmark, and per-seed trace diagnostics. Finally, we evaluate Dependency-aware Semantic Garbage Collection (DSGC), a one-hop graph-aware rule. In our main suite, DSGC improves full-chain retention from 0.03 to 0.90 under a lexical encoder and from 0.23 to 1.00 under a sentence encoder. Robustness checks then identify the budget and scaling regimes where the one-hop rule holds or degrades. Our released pipeline and failure postmortem support mechanistic analysis of retention before retrieval as a distinct failure boundary.

---


### 10. [World models of environment, agent and joint agent-environment systems](https://arxiv.org/abs/2608.20401)

**<font color=#1a73e8>作者：</font>** Manuel Baltieri, Filippo Torresan, Yivan Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models are a central component of model-based reinforcement learning. They are usually discussed in terms of what variables they predict, such as observations, rewards, states, latent or information states. We argue that there is a prior distinction: which channel they model. We consider three cases: the environment channel $O_{:} \mid A_{:}$, the agent channel $A_{:} \mid O_{:}$, and the realised joint process $(A, O)_{:}$, equivalently viewed as a channel with no inputs. Using computational mechanics, we define canonical predictive models for these three cases as $\epsilon$-transducers or $\epsilon$-machines. Canonical environment models recover standard predictive state representations, while the other two give analogous notions of canonical models for the agent and the joint system. We then build canonical support-restricted environment and agent models induced by closed-loop coupling, whose predictive equivalences range over continuations supported by the realised interaction. The key structural result is that canonical support-restricted environment states factor through the canonical joint causal states, and their transition structure is induced directly from the joint model; the agent-side construction is dual. Finally, we give a POMDP/controller example in which the unrestricted environment model has infinitely many states while the canonical support-restricted model induced by the coupling is finite. The framework clarifies what different world models are models of, and how coupling and support restriction can change their canonical predictive structure and complexity.

---


### 11. [LingShu: A Large-Scale Symptom-Centric Contextualized Knowledge Graph Bridging Traditional Chinese Medicine and Modern Biomedicine](https://arxiv.org/abs/2608.20402)

**<font color=#1a73e8>作者：</font>** Rui Hua, Zixin Shu, Kai Chang 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Biomedical knowledge graphs (KGs) are pivotal for knowledge organization, yet traditional binary relations often struggle to represent the conditional nature of biomedical knowledge. Symptoms provide a shared phenotypic layer for linking Traditional Chinese Medicine (TCM), which relies on symptom patterns for syndrome differentiation and treatment selection, with modern biomedicine, which connects clinical manifestations to diseases and molecular mechanisms. We present LingShu, a large-scale symptom-centric contextualized knowledge graph designed to bridge TCM and modern biomedicine. The exported version of LingShu analyzed in this study comprises 17.33 million atom-level entity records and 39.47 million relation records, including 17.19 million semantic triples and 22.29 million contextualized quadruples. LingShu integrates multi-source data, including clinical electronic medical records, authoritative TCM texts, biomedical ontologies, and curated knowledge bases, through a pipeline combining natural language processing, terminology normalization, and human-in-the-loop verification. A key innovation of LingShu is its hybrid data model: it maintains 64 typed triple relation patterns to ensure broad connectivity, while incorporating 35 contextual quadruple relation patterns to capture conditional medical associations. This dual-structure approach explicitly encodes conditional knowledge, providing a granular representation of the contexts associated with medical relations. These contextualized relations cover syndrome-dependent herb efficacy, disease-contextualized drug effects, population-specific clinical associations, and mechanism-related therapeutic responses. Furthermore, we developed a web platform (this http URL) that integrates graph visualization, graph-based reasoning, and an evidence-grounded knowledge question-answering agent.

---


### 12. [Machine Learning and ARIMA Model Averaging for Adaptive Public Health Forecasting: Comparative Evaluation and an Ontario COVID-19 Case Study](https://arxiv.org/abs/2608.20406)

**<font color=#1a73e8>作者：</font>** Yushu Zou, Ye Li, Johra Moosa 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Public health forecasts must respond to abrupt changes in surveillance data without over-extrapolating noise, reporting artifacts, or temporary trends. We evaluated autoregressive integrated moving average (ARIMA), random forest, and extreme gradient boosting (XGBoost) models using 190 weekly observations of publicly available Ontario COVID-19 case counts from January 2020 to October 2023. Rolling-origin time-series cross-validation preserved temporal order during model tuning and evaluation. Performance was assessed across three operating dimensions: responsiveness following selected turning points, forecast horizons of one to six weeks, and the amount of historical training data. We also developed Machine Learning and ARIMA Model Averaging (MLAMA), a non-negative performance-weighted ensemble with weights that vary by forecast horizon and responsiveness setting. Retrospective comparisons showed that ARIMA adapted rapidly after turning points but its normalized error increased at longer horizons. Random forest and XGBoost were less responsive initially but maintained more stable normalized error over longer horizons. For two-week forecasts at the end of the study period, training on the most recent data outperformed using longer historical periods, particularly for XGBoost. MLAMA achieved the lowest normalized mean absolute percentage error across most forecast horizons and ranked among the best-performing methods across responsiveness settings. These findings support selecting forecasting models according to operating conditions rather than relying on a single universally preferred approach. MLAMA provides a practical framework for combining complementary statistical and machine-learning forecasts. The accompanying Python package is currently maintained in a private repository while software validation and reproducibility testing are completed.

---


### 13. [Categorical AI phenomenology: A first-person approach](https://arxiv.org/abs/2608.20420)

**<font color=#1a73e8>作者：</font>** Robert Prentner  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper develops a phenomenology-first approach to artificial consciousness by reframing consciousness as the subjective experience enacted through an agent's interface with the world. We shift the methodological focus to first-person structures, modeled mathematically by categories derived from Q-networks to capture actions and phenomenological invariants. In this framework, Q-networks are conceptualized as relational interfaces encoding agent-world interaction, analogous to how the dynamical states of a computer depend on its sensory inputs, previous states, and actions. Our work provides a rigorous framework for interface consciousness to describe computational systems that embed information-processing into phenomenological structure. The approach aligns with 4E approaches to cognition by emphasizing enactive, embedded, and extended dimensions of experience. The paper thus offers a principled, relational, and phenomenological account of artificial phenomenology grounded in categorical mathematics.

---


### 14. [From Thermal Preference Prediction to Adaptive Thermal Intervention: A Reinforcement Learning Approach Using Physiological and Environmental Sensing](https://arxiv.org/abs/2608.20423)

**<font color=#1a73e8>作者：</font>** Isibor Kennedy Ihianle, Emmanuel Manu, Ehsan Asnaashari 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Personalised thermal comfort is essential for occupant wellbeing and for the development of more responsive building-control strategies, yet conventional Heating, Ventilation, and Air Conditioning (HVAC) systems rely on static setpoints and population-level comfort models that fail to capture individual physiological variability. This paper presents a two-stage personalised thermal comfort approach integrating multimodal physiological and environmental sensing with reinforcement learning-based decision-making.

---


### 15. [Approximate Homomorphisms and Convergent Representations in Transducers](https://arxiv.org/abs/2608.20428)

**<font color=#1a73e8>作者：</font>** Santiago Cifuentes  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the stability of minimal representations of controlled stochastic processes (in particular, transducers) under perturbations. This question is motivated by recent experiments finding predictive-state structure in the latent representations of neural networks. We consider standard, linear and predictive transducers. We introduce notions of approximate homomorphism capturing local structural similarity between them, together with metrics comparing their induced dynamics (which we refer to as interfaces), and prove properties such as composability of the approximate homomorphisms. For standard transducers, we show that there exist simple interfaces for which there is no approximate homomorphism between the different implementations of the dynamics. In contrast, for every finite-rank interface $\mathcal I$, we prove that all minimal linear transducers implementing interfaces sufficiently close to $\mathcal I$ have an approximate homomorphism to the minimal implementation of $\mathcal I$, with error linear in the perturbation size. We prove an analogous stability result for predictive transducers under a residual metric using some mild hypothesis regarding the indistinguishability of the belief states. These results identify conditions under which canonical transducer representations are robust to perturbations, while showing that such convergence fails without additional structural restrictions. Under the assumption that these type of abstractions are embedded into the hidden layers of modern AI models, this gives some theoretical support to the hypothesis that their latent representations exhibit structural convergence.

---


### 16. [RISE: Adaptive Imagination for World Action Models](https://arxiv.org/abs/2608.20430)

**<font color=#1a73e8>作者：</font>** Hongbo Lu, Liang Yao, Chenghao He 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World Action Models (WAMs) improve planning by incorporating future world evolution into action generation, yet existing methods allocate a fixed imagination budget to every scene. We propose RISE (\textbf{R}efining \textbf{I}magination through \textbf{SE}lective Rollout), a system-level adaptive imagination framework that makes sequential \textsc{Roll}/\textsc{Stop} decisions according to the expected planning benefit of continued rollout. At each step, a Latent Evaluator estimates the risk revealed by the current prefix and how much planning could improve if imagination continues, while a Rollout Gate weighs this expected benefit against additional computation cost. Since factual driving logs expose only one realized future, we further construct \textbf{CounterDrive}, a counterfactual dataset with diverse outcomes and risk levels, to enrich future dynamics and provide localized risk supervision. Each retained sample undergoes expert verification and annotation of trajectory validity, incident onset, and causal category, providing a reusable resource for safety-critical world-modeling research. Experiments on NAVSIM and nuScenes show that RISE achieves the best overall planning performance while reducing unnecessary rollout, with additional transfer results supporting its plug-in generality across WAM architectures.

---


### 17. [Wrong-Physics Backdoors in Neural PDE Operators](https://arxiv.org/abs/2608.20439)

**<font color=#1a73e8>作者：</font>** Hanbing Liang, Fujun Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural PDE operators are increasingly trained on reusable solver archives, yet validation often relies on clean prediction error and parameter-agnostic plausibility checks. We introduce cross-parameter relinking, a data-poisoning primitive that makes a triggered input select a valid solution from the same PDE family under an incorrect physical parameter. We term this a wrong-physics backdoor: the output remains physically plausible but is wrong for the intended parameter. The attack exploits tensor-to-parameter provenance failures in multi-parameter archives by stamping the surrogate input and relinking its supervision to a cached alternate-parameter solution for the same latent sample. Across 476 attack campaigns, we evaluate Burgers, advection-diffusion, two-dimensional Navier-Stokes, and an elliptic Poisson case. Fourier Neural Operators and DeepONet provide the primary evidence, with Transformer, GRU, and LSTM models as support. FNO reaches a backdoor success rate of 1.0000 on both advection-diffusion and two-dimensional Navier-Stokes while retaining low clean relative L2 error. Clean-label, label-only, and shuffled controls show that high attack success alone is insufficient: successful attacks must move predictions toward the intended alternate-physics target while preserving bounded clean error. These results expose a structural validation gap: smoothness or generic solver-like behavior is insufficient unless the provenance of the intended physical parameter is also verified.

---


### 18. [Decision Tree and K-Means Analysis of Raman Spectra for Edible Oils: A Physics-Informed AI Approach](https://arxiv.org/abs/2608.20440)

**<font color=#1a73e8>作者：</font>** Amrita Shaw, Chandrasekar S. N., Sai Muthukumar V. 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Authentication of edible oils in processed foods is important for food quality, fraud prevention, and regulatory compliance. This study establishes an integrated Raman spectroscopy and machine-learning framework that links intrinsic spectral organization, interpretable classification, and Physics-Informed Artificial Intelligence (PI-AI). Five edible oils were investigated in pure form and within a fried-potato-chip matrix using t-SNE, K-means clustering, Decision Trees, and Non-Negative Least Squares (NNLS)-based spectral decomposition. Unsupervised analyses revealed substantially stronger class organization and separability in pure oils, whereas food-matrix effects introduced pronounced spectral overlap. Decision Trees achieved 100% classification accuracy for pure oils using only four Raman variables from the original 1866-feature spectral space. These four variables, consistently identified by both pre-pruned and post-pruned models, represented only approximately 0.21% of the available spectral information while retaining perfect test-set performance. For matrix-containing samples, NNLS-based PI-AI spectral decomposition substantially improved classification by separating oil-related signatures from paper and potato contributions. Optimized post-pruned models achieved accuracies of 86.4% and 85.4% for paper-subtracted and paper-plus-potato-subtracted datasets, respectively, while reducing the number of important Raman variables to only five and four. The compact four-feature representation further reduced the data footprint by 99.44% without loss of classification accuracy. Collectively, these findings demonstrate that accurate Raman-based oil identification can be achieved through physically meaningful, highly compact, and interpretable spectral representations, providing a promising foundation for Frugal AI, Edge AI, portable sensing, and embedded food-quality monitoring.

---


### 19. [Shared Physics Responses Recover Hidden Rankings in Neural Operator Libraries](https://arxiv.org/abs/2608.20441)

**<font color=#1a73e8>作者：</font>** Hanbing Liang, Fujun Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Selecting the optimal neural-operator prediction during deployment is challenging when high-fidelity reference solutions are unavailable. We demonstrate that under a squared Hilbert-space loss, ranking a finite model library depends strictly on the low-dimensional span of candidate differences, allowing us to score all models simultaneously using a single anchor-based linearized response of the governing equation. This shared physical diagnostic accurately recovered over 99.6\% of pairwise preferences and 99.0\% of optimal checkpoints across diverse Fourier and convolutional operator libraries for fluid, reaction-diffusion, and wave dynamics. Furthermore, the corrected physical proxy frequently outperformed the best individual candidates, and we establish computable sufficient conditions that rigorously certify exact decisions for strongly monotone discretizations. By exploiting the local dynamical response rather than raw defect magnitude, this framework enables the reliable and highly efficient deployment of scientific surrogates without requiring ground-truth data.

---


### 20. [Amortized Bandwidth Learning for Kernel Density Estimation under Logarithmic Score](https://arxiv.org/abs/2608.20445)

**<font color=#1a73e8>作者：</font>** Junyi Liang, Hailiang Du  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Kernel density estimation converts finite samples into probability densities, but its performance depends critically on bandwidth selection. Classical selectors prescribe the sample-to-bandwidth rule analytically or asymptotically, or solve a new optimization for each sample. An amortized framework is proposed that instead learns this mapping across a distribution of density-estimation tasks by optimizing the logarithmic score. A truncated-and-renormalized bounded-support formulation enables stable learning across heterogeneous tasks, while affine standardization allows a selector trained on a single reference interval to transfer across bounded intervals. Experiments under Gaussian sampling, a multi-family benchmark, and randomized Gaussian-mixture training show that the amortized selector consistently and substantially outperforms Silverman's rule, the Sheather--Jones selector, and least-squares cross-validation, with especially large gains in small and heterogeneous samples. Finite Gaussian mixtures provide a generic training mechanism supported by their $L^1$ approximation property. Selectors trained in this way generalize strongly across different density structures, allowing the same trained selector to be applied directly to finite samples from unknown densities without specifying or fitting a distributional family. This combination of broad applicability and strong empirical performance makes the framework attractive for a wide range of applications in which finite samples or ensembles must be converted into continuous probability densities.

---


### 21. [Mutual information and sensitivity analysis for feature selection in customer targeting: a comparative study](https://arxiv.org/abs/2608.20447)

**<font color=#1a73e8>作者：</font>** Nestor Barraza, Sergio Moro, Marcelo Ferreyra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Feature selection is a highly relevant task in a data-driven knowledge discovery project. Several techniques have been developed aiming at finding the features that influence most an outcome to predict, including mutual information and, in recent years, the data-based sensitivity analysis. The present research focus on analyzing the advantages and disadvantages of each of these two techniques, by applying both to a bank telemarketing case. Thereafter, a logistic regression model is built on the tuned set of features identified by each of the two techniques as the most influencing set of features on the success of a telemarketing contact, in a total of 13 features for mutual information and 9 features for the data-based sensitivity analysis. The latter performs better for lower values of false positives while the former is slightly better for a higher false positive ratio. Thus, mutual information becomes a better choice if bank managers intend to reduce slightly the cost of contacts without risking losing a high number of successes. Such results show that mutual information, although not recent, is still a valid method for feature selection. On the other side, the data-based sensitivity analysis selection achieved good prediction results with less features.

---


### 22. [STCO: Conditional Neural Operators for Time-Dependent PDEs](https://arxiv.org/abs/2608.20477)

**<font color=#1a73e8>作者：</font>** Xingxin Yang, Zhan Zhang, Juan Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neural operators have emerged as efficient surrogates for time-dependent physical systems governed by partial differential equations (PDEs), but their future-state predictions are often conditioned only on observed states and static problem descriptors. For control or optimization, however, body motion, inflow, or forcing are prescribed for the query without being determined solely by the observed state. We introduce the Spatiotemporal Conditional Operator (STCO) for prescribed-condition operator learning (PCOL), a common interface that supplies prescribed target-time condition fields to heterogeneous backbone architectures while retaining their architecture-specific core computation and context pathways. Its condition interface combines Flow-Aware Graph Leaf (FAGL) with Dual-Site Feature-wise Linear Modulation (DSFiLM). Non-learned FAGL uses vorticity from the final observed frame to construct a fixed-cardinality adaptive partition, then co-locates the observed history and target-time condition fields at its regional coordinates. DSFiLM injects separate motion, inflow, and force routes before and after operator computation through current-feature-driven slot- and channel-wise gates. We evaluate twelve matched backbone architectures with different existing physical and temporal inputs. The immersed-boundary computational fluid dynamics (CFD) benchmark spans prescribed motion, inflow disturbances, body-force actuation, and morphology. Across twelve matched backbones, three regimes, and two lead ranges, STCO yields mean paired reductions of 31.1% in relative-L2 field error and 24.7% in normalized pressure-derived load error. It also lowers longer-lead field error for 11 backbones, while interventions on individual condition groups produce measurable prediction changes for every group evaluated.

---


### 23. [When Clean Data Hurts: Learning with Monotone Corruptions Beyond Binary Classification](https://arxiv.org/abs/2608.20480)

**<font color=#1a73e8>作者：</font>** Julian Asilis, Shaddin Dughmi, Chirag Pabbaraju  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimal learners are tailored to exploit the i.i.d.\ data assumption underlying the classic PAC model. What if an i.i.d.\ training sample were corrupted with correctly labeled examples drawn from an otherwise unrelated, even adversarial source? This model of learning with monotone adversarial corruptions was recently introduced by Larsen et al. (2026), who demonstrated that all known optimal binary learners suffer increased error rates in this setting, from $O(d / n)$ in the PAC model to $\Omega (d \log(n / d) / n)$ under monotone corruption. Mehrotra (2026) proved this logarithmic factor to be necessary for binary classification, but left open the consequences of corruption for more general learning settings, such as multiclass classification and partial binary concept classes.
As our primary result, we demonstrate that monotone adversaries are frighteningly more powerful in each of these settings. We exhibit a learnable multiclass problem, of DS dimension only 2, that becomes altogether unlearnable under a monotone adversary, and show an analogous result for partial binary concept classes. These results are achieved by an adaptive adversary permitted to view the original i.i.d.\ training set $S$ and to insert $b < \infty$ corrupted datapoints into $S$. In the multiclass example, the adversary need only insert a linear number $b = |S| = n$ of datapoints.
We complement these impossibility results by proving that every class remains learnable when the number of adaptive additions is $o(n)$, which our previous multiclass lower bound proves to be tight. We further observe that the classic multiclass error rate of $O(d_{\mathrm{DS}} / n)$ remains achievable against adaptive adversaries restricted to a known constant budget $b = O(1)$, against semi-adaptive adversaries viewing only a $p$-fraction of $S$ for $p \in (0, 1)$, and against oblivious adversaries that cannot view $S$.

---


### 24. [Metag: A dataset to build agentic meta-reviewing capabilities](https://arxiv.org/abs/2608.20488)

**<font color=#1a73e8>作者：</font>** Anirudh Sundar, Min Chen, Divya Tadimeti 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI tools increasingly support tasks across the scientific research cycle, from experiment design and manuscript preparation to peer review. At the same time, the continuing growth in conference submissions has increased the burden on meta-reviewers, who must synthesize reviewer feedback, author rebuttals, and manuscript revisions. To address this concern, this paper introduces Metag, a dataset to accelerate the development of meta-reviewing agents, specifically to identify changes made to scientific articles during the review-rebuttal process. Each instance contains a reviewer concern, the author's proposed resolution, and the manuscript diffs implementing the stated change. Metag is collected by obtaining manuscript versions from before the review deadline and after acceptance, computing differences between the two documents, and asking human annotators to align these differences with action items from OpenReview discussions. The resulting dataset consists of 349 high-quality action items tied to paper differences and will enable building methods to empower meta reviewers to quickly identify whether authors have addressed reviewer statements and where in the paper those changes have been made, resulting in additional transparency and traceability throughout peer review. The dataset is publicly available at this https URL.

---


### 25. [Lost in Translation: How Universal Ethical Values Fail to Translate Across Global Contexts](https://arxiv.org/abs/2608.20490)

**<font color=#1a73e8>作者：</font>** Ozioma C. Oguine, Munachimso B. Oguine, Cesar Cervera 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI ethics frameworks treat values such as fairness, transparency, and accountability as universal and uniformly operationalizable across contexts. We examined how 14 experts across 10 countries made sense of AI in practice, reinterpreted core values, and envisioned governance alternatives. We found that AI deployment is characterized by structurally unequal conditions, marked by infrastructural constraints, extractive practices, and a "mystification" of technology, which fundamentally shape perceptions of risks and opportunities. Our findings reveal that experts reinterpret values to fit local moral logics: privacy as collective and relational rather than individual; transparency as trust-building accountability rather than technical disclosure; and fairness as equity in access and representation rather than parity in outcomes. We identify these as translation gaps between encoded global frameworks and situated local practices. Finally, we propose pathways toward plural governance that redistributes epistemic authority and treats ethical negotiation as an ongoing, context-sensitive process rather than a settled technical standard.

---


### 26. [Bern2Edge: A Neurosymbolic Compiler for Edge Deployment via Bernstein Polynomial Networks](https://arxiv.org/abs/2608.20497)

**<font color=#1a73e8>作者：</font>** Malak Gamal El-Din, Yifan Zhang, Yasser Shoukry 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying high-accuracy neural networks on resource-constrained edge devices remains challenging, as existing approaches treat training, compression, and hardware synthesis as separate stages, leaving a gap between software-trained models and efficient end-to-end deployment with limited support for interpretability. We propose Bern2Edge, an end-to-end framework that uses knowledge distillation to convert a pretrained teacher feed-forward network into hardware-efficient representations via Bernstein polynomial activations. This representation enables two deployment paths: (i) a high-fidelity LUT-based realization that preserves model fidelity under compression, and (ii) a symbolic rule-based representation derived from Bernstein activation geometry, enabling interpretable inference with explicit input-space constraints. The resulting BNNs achieve up to 2.12 percentage-point (pp) accuracy improvement over ReLU under identical compression constraints. At the system level, Bern2Edge achieves up to 99.8% latency reduction and 95.2% BRAM reduction relative to a W8A8 quantized teacher on an AMD Xilinx KV260 FPGA, while maintaining accuracy within 0.5 pp, and further deploys on a low-power Spartan-7 XC7S15 FPGA. The rule-based path reduces DSP usage by up to 89.0% at a cost of 1.5 pp in total accuracy.

---


### 27. [A Temporal Planning Approach for Intelligent Flood Response](https://arxiv.org/abs/2608.20510)

**<font color=#1a73e8>作者：</font>** Fazlul Hasan Siddiqui, Md. Monjurul Islam, Sabah Binte Noor  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Effective response to multiple, simultaneously flooded areas requires coordinating appropriate actions in the correct temporal order, under severe resource constraints. Automated planning provides a foundation for addressing this challenge by generating time-aware schedules, given a formal description of available resources, constraints, and goals. This work presents an intelligent flood-response framework that exploits temporal planning and models the complete operational life cycle of flood response. The framework incorporates priority-driven triage, route accessibility and travel costs, resource allocation, and supply management, while also supporting mid-execution re-planning in response to unexpected environmental changes. The framework is formulated both in the Action Notation Modeling Language (ANML) and the Planning Domain Definition Language (PDDL) 2.1, facilitating compatibility with a wider range of temporal planners. Experimental results establish the feasibility and scalability of the proposed framework, showing that flood response scenarios can be effectively modeled and solved using temporal planning, while providing guidance on planner selection.

---


### 28. [DiffVC-ONE: Diffusion-based Generative Video Compression with One-Step Video Diffusion Transformer](https://arxiv.org/abs/2608.20515)

**<font color=#1a73e8>作者：</font>** Wenzhuo Ma, Zhenzhong Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative video compression can recover rich visual details at low bitrates, but simultaneously achieving high temporal consistency and low inference cost remains challenging. To address this issue, we propose DiffVC-ONE, a diffusion-based generative video compression framework built on a one-step Video Diffusion Transformer. First, we introduce a Unified Unidirectional Latent Compressor that uses a shared model to efficiently and uniformly compress compact latent slices. We then develop a Video DiT-based One-Step Diffusion Enhancer that uses the reconstructed latent slices as content anchors and performs single-step spatio-temporal perceptual enhancement over an entire group of pictures. Finally, a Hybrid Condition Generator extracts structural, strength, and semantic conditions from the reconstructed content and quantization information. These conditions preserve faithful regions, control the degree of generative enhancement, and supplement content-aware perceptual details during one-step diffusion enhancement. Extensive experiments on multiple standard benchmarks demonstrate that DiffVC-ONE achieves state-of-the-art perceptual quality and temporal consistency with low inference cost.

---


### 29. [When Graph-JEPA Learns the Wrong Thing: Diagnosing and Repairing Category-Conditional Collapse](https://arxiv.org/abs/2608.20516)

**<font color=#1a73e8>作者：</font>** Gollam Rabby, Sören Auer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Joint-embedding predictive architectures are selected almost universally by linear probing and effective rank. We report a case where both read healthily while the representation carries zero usable instance information. We repair it, and a second failure appears: the repaired metric saturates on a target carrying no structural information. Our corpus is a scientific-reasoning graph over 57,903 articles, each a subgraph. A Graph-JEPA predicts one masked aspect from a subgraph's remaining aspects, attaining linear-probe accuracy 0.871 and effective rank 18-47, yet retrieval recovers 0.00 of 14.4 bits (MRR 1.9e-4 vs chance 1.99e-4, p=0.98). Three upper bounds on the same pool and code recover nearly everything (+14.28, +14.34, +14.22 bits), ruling out corpus, masking, pool, and metric as causes. We trace this to variance allocation - frozen inputs place 86.05% of variance on subgraph identity and 0.40% on aspect identity, while trained latents place 0.39% and 99.61%. This is a property of the objective's optimum: the degenerate solution is a global minimum of the coupled predictor/EMA-target objective, present already at init. A repaired configuration reaches 14.377 of 14.379 bits, above the 13.865-bit oracle; reverting the loss to regression drops it to 0.307 bits, confirming it. Yet the repair licenses nothing about reasoning: the target is reducible, since intra-subgraph edges are a deterministic function of node census. The oracle reaches 96.4% of the ceiling, and our largest effect is the learning-rate schedule, not architecture. Bits and a reasoning probe show no relation across ten cells. A data-derived target fails a quality gate - 25.96% of nodes are duplicate placeholders, and the rest is more generic than supporting evidence. Rank, probes, and metrics can all saturate on an unsupportive evaluation. We release a harness with a reducibility audit and target gate.

---


### 30. [Me Among Us: Affective Framing in Data Donation](https://arxiv.org/abs/2608.20523)

**<font color=#1a73e8>作者：</font>** Zeya Chen, Zach Pino  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This study investigates how different framing approaches influence the affective aspects of data donation decision-making. Although framing effects are well studied in charitable giving, how affective framing shapes data donation, especially through data visualization, remains poorly understood. Using a theoretical framework based on the functions of affect in decision-making, we examine how three distinct framing approaches, an individual-donor lens (Group A), an individual-collective lens (Group B), and a collective-institutional lens (Group C), shape participants' affective experiences and subsequent donation decisions. Through a real-world data donation study (N=24), we found that framing designs substantially influenced donation outcomes, with the individual-collective lens generating the most favorable responses. Our analysis illustrates how affect can functions as information, motivation, and as a spotlight during the decision-making process, providing insights for designing more informed data donation interfaces and communications. This research contributes to understanding the complex interplay between framing designs, affective responses, and decision outcomes in data donation contexts.

---


### 31. [Learning Exact NVIDIA SASS Encoders with $\mathbb{F}_2$ Linear Algebra](https://arxiv.org/abs/2608.20532)

**<font color=#1a73e8>作者：</font>** Jiading Gai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> NVIDIA provides a SASS disassembler but no public SASS assembler for recent data-center GPUs, limiting controlled machine-code rewriting. We present F2Asm, which learns exact 128-bit SASS encoders from paired disassembly and original CUBIN instruction words. To our knowledge, F2Asm is the first system to learn SASS instruction encoders as vector-valued affine maps over F2 and the first open-source NVIDIA SASS assembler to support Rubin SM107. F2Asm uses Gaussian elimination over F2 to incrementally build a compact basis, detect inconsistencies, and reject inputs outside the learned span. F2Asm separates target-specific control bits, relocation rules, and CUBIN metadata from its learning algorithm. We train encoders for Hopper SM90/SM90a, Blackwell SM100, and Rubin SM107 using 3,225 CUBINs from pinned NVIDIA and third-party production libraries, CUDA 13.3 packages, and CUDA 13.4 Developer Preview archives. In round-trip tests, F2Asm reassembles the disassembled SASS for each CUBIN, and all compared executable text sections match the originals exactly.

---


### 32. [Grounded-Exo2Ego: Structured Semantic Grounding for Robust Exocentric-to-Egocentric Video Generation](https://arxiv.org/abs/2608.20534)

**<font color=#1a73e8>作者：</font>** Shengze Wang, Michael Stengel, Tianye Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating egocentric video from a single exocentric video is an emerging and important topic for AR/VR and physical AI. Compared with conventional novel view synthesis, exo-to-ego generation is a significantly harder task because the standard geometric conditioning becomes highly unreliable under extreme view changes and large unobservable regions. We present Grounded-Exo2Ego, a principled framework that addresses these challenges at both the architectural and data levels. Architecturally, Grounded-Exo2Ego is a dual-branch video diffusion model that couples a geometric anchoring branch, which conditions the generation on the rendering of a 3D reconstruction, with a novel semantic grounding branch, which goes beyond the prevailing geometry-based approach and improves quality by synthesizing challenging regions based on object-level context. Additionally, we found that the overlooked issue of camera-reconstruction misalignment severely undermines exo-to-ego learning. We thus introduce a camera re-localization algorithm that resolves this issue and substantially improves quality across all metrics. We further develop a fully automated synthetic data engine that generates and renders rigged 3D characters in procedurally generated environments. Evaluation on the challenging EgoExo4D dataset shows that our method outperforms recent state-of-the-art approaches by large margins across all metrics. Detailed ablations validate improvements from each of our contributions at both the data and architectural level.

---


### 33. [Keep Your Friends Close, and the Right Neighbours Closer: Disaster-Conditioned Kernel-Regularized Graph Attention for Building Damage Classification](https://arxiv.org/abs/2608.20548)

**<font color=#1a73e8>作者：</font>** Fuad Hasan, Chul Min Yeum  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Disaster damage is spatial: buildings rarely fail in isolation. Yet using spatial context for damage classification remains surprisingly underexplored, and many pipelines still rely primarily on per-building appearance cues even when the dominant uncertainty is spatially structured. Complicating matters, the right neighbourhood is not the same across events. Floods, hurricanes, and wildfires can exhibit very different clustering behaviour, making spatial reasoning valuable but easy to misuse - naive context aggregation can improve visual coherence while oversmoothing boundaries or propagating structured errors. We study this tension on xBD (the dataset used in the xView2 challenge) in a controlled post-localization, classification-only setup: each building is represented by a pre/post combined (PPC) patch cropped from the provided polygons, and spatial context is modelled with GPS-derived building graphs. Our approach keeps local evidence "close" by preserving strong spatial relationships in disaster damage patterns, while bringing only the right neighbours "closer" through a disaster-type-conditioned graph model that injects a learnable multi-scale spatial kernel prior into attention, allowing the effective neighbourhood scale to adapt across disaster types rather than being learned as a single global smoothing rule. To discourage coherence-by-smoothing, we add a residual de-correlation loss that penalizes positive Moran's~I in prediction residuals. We evaluate the method under event and dataset shift with a leave-one-event-out (LOEO) protocol on xBD and cross-dataset transfer from xBD to Ida-BD. The model improves macro-F1 and substantially reduces residual spatial autocorrelation under zero-shot event shift, indicating better use of spatial context rather than naive smoothing and enabling more reliable transfer to unseen events within known disaster types.

---


### 34. [Learning Prostate Anatomy at Test Time for Cancer Detection in Micro-Ultrasound](https://arxiv.org/abs/2608.20557)

**<font color=#1a73e8>作者：</font>** Obed Korshie Dzikunu, Mohammad Mahdi Abootorabi, Mohamed Harmanani 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Domain shift across clinical centers using different imaging hardware or acquisition protocols remains a fundamental barrier to deploying deep learning models for prostate cancer (PCa) detection. Existing test-time adaptation (TTA) methods address distribution shift through entropy minimization or augmentation-based self-supervision, correcting for statistical differences in image appearance but ignoring the anatomical structure of the target domain. We propose ANT, a segmentation-guided TTA framework that adapts a pretrained cancer detection encoder to the target domain by solving an auxiliary prostate segmentation task at test time, supervised by pseudo-masks from a frozen pretrained segmentation network. By aligning encoder representations to prostate anatomy in the target domain, ANT corrects domain-specific feature drift while preserving cancer-discriminative structure. The model was trained on 693 patients imaged with an earlier-generation micro-ultrasound scanner in a multi-center clinical trial, and evaluated on 118 patients acquired with a newer-generation system across two centers in another clinical trial. Under a leave-one-center-out protocol with identical evaluation conditions across all methods, ANT improves mean AUC by 2.9% and 3.6% at the biopsy-core and patient levels, respectively, over no adaptation, outperforming TTA baselines. Code is available at: this https URL.

---


### 35. [Zero-Shot Color Image Manipulation Localization via Noise Residual Artifact Pattern Analysis](https://arxiv.org/abs/2608.20558)

**<font color=#1a73e8>作者：</font>** Edgar Gonzalez-Fernandez  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Digital cameras embed device-specific artifacts into every acquired image through demosaicing, in-camera post-processing, and lossy compression. These traces constitute a forensic signal that can be exploited to assess image authenticity. Existing passive methods rely predominantly on the green channel of the Bayer residual, discarding the correlated information available in the remaining color channels and typically requiring training data or device enrollment. This work proposes a zero-shot, training-free blind image manipulation localization pipeline that estimates a reference artifact pattern directly from the noise residual of a single suspect image, without assuming a fixed filter configuration, color layout, or block period. The pipeline incorporates a principled denoiser selection criterion based on the acquired-to-interpolated noise variance ratio, a block-level correlation analysis against the estimated reference pattern, and a two-component Gaussian Mixture Model scoring stage that produces a pixel-level tampering probability map. An ablation study evaluates the impact of denoiser choice and block size on localization accuracy, and comparisons against state-of-the-art passive methods demonstrate the competitiveness of the proposed zero-shot approach.

---


### 36. [Faults That Fortify: CNN Adversarial Robustness via GPU Undervolting](https://arxiv.org/abs/2608.20572)

**<font color=#1a73e8>作者：</font>** Behnam Omidi, Ahmad Tahmasivand, Husam Alsyouri 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Convolutional Neural Networks (CNNs) face a dual challenge: vulnerability to adversarial attacks and prohibitive training cost. Adversarial training is effective but expensive, a burden that grows as learning shifts to the energy-constrained edge. This paper addresses both through GPU undervolting during training. Reducing supply voltage introduces stochastic perturbations that act as implicit regularization, improving robustness while lowering power. We characterize undervolting-induced faults at the bit level, then train LeNet, VGG-6, and MobileNetV3 on MNIST and CIFAR-10 under two training regimes, standard and adversarial, each at nominal and undervolted voltage, and evaluate all models against adversarial attacks. In both regimes, the undervolted model consistently achieves higher adversarial accuracy than its nominal-voltage counterpart, showing that hardware-induced faults strengthen even adversarial training. Because dynamic power scales quadratically with supply voltage, these robustness gains arrive with substantial energy savings. GPU undervolting is therefore a readily deployable hardware-level defense requiring no algorithmic change, and opens a promising direction in which robustness and energy efficiency move together.

---


### 37. [Temporal Risk on Satellites](https://arxiv.org/abs/2608.20575)

**<font color=#1a73e8>作者：</font>** Shiqi Liu, Kun Sun  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Satellite vulnerabilities change over time as orbits shift, power margins tighten, and the space environment deteriorates. However, most cybersecurity risk frameworks still treat threats as static. In practice, the same exploit can be far more damaging during a critical maneuver than during routine operations. We propose a temporal risk assessment framework that makes time an explicit axis in satellite security analysis. It extends existing adversary behavior taxonomies with a five-dimensional temporal capability model and estimates exploitation difficulty across distinct temporal windows of a mission. Rather than producing a single risk score, the framework outputs a series of time-indexed likelihood-impact matrices. It discretizes missions into operationally meaningful time windows and environmental bands to show when systems are most exposed. This view helps operators avoid scheduling sensitive operations in high-risk periods and align defensive resources with a threat landscape that shifts over time.

---


### 38. [Keyed Provenance Watermarking with Complementary Lattice-Based Secure Aggregation for Federated Learning](https://arxiv.org/abs/2608.20580)

**<font color=#1a73e8>作者：</font>** Xinyun Liu, Zhi Lu, Yu Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) is vulnerable to multi-level attacks. However, existing methods address them separately, leaving FL exposed to data leakage, unauthorized reuse, and malicious gradient manipulation. In this work, we propose an FL framework that couples keyed context-provenance watermarking with verifiable lattice-based secure aggregation of Real-World Anchored Watermarking and Lattice-Based Zero-Knowledge Secure Aggregation. At the data layer, we propose a Kerckhoffs-compliant scheme that utilizes Physical Anchor Metadata (PAM) to ensure data provenance. PAM is defined as a context-provenance token derived from trusted infrastructure data (time, location, and server ID) and then subjected to a keyed HMAC-SHA-256 transformation to produce a watermark payload that cannot be generated without the client's secret key. We further design FMGAN, a GAN-based robust image watermarking framework that embeds this transformed payload using a feature fusion module and a Mamba-guided linear attention mechanism. At the computation layer, we adopt a lattice-based zero-knowledge secure aggregation (LZKSA) protocol that verifies key correctness, L2 norm bounds, and cosine similarity constraints over committed gradients without revealing private updates. The RLWE-based design guarantees post-quantum security. Extensive experiments validate the complementary protection of the two layers under composite attack scenarios. To our knowledge, no prior verification workflow has jointly evaluated both layers in a hybrid, end-to-end trustworthy FL framework.

---


### 39. [MATEE: Efficiently Bridging the Semantic Gap in TrustZone via Arm Pointer Authentication](https://arxiv.org/abs/2608.20583)

**<font color=#1a73e8>作者：</font>** Shiqi Liu, Xiang Li, Jie Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Trusted Execution Environments (TEEs) employ hardware-based isolation mechanisms to safeguard the confidentiality and integrity of sensitive code and data. One such prevalent implementation is Arm TrustZone, which partitions the system into the secure and normal (non-secure) worlds. However, this partitioning results in the secure world having very limited visibility into the operating information of the normal world, creating a semantic gap between these two worlds. Specifically, the secure world lacks an effective user identity authentication when receiving data requests from the normal world. Consequently, malicious Client Applications (CAs) in the normal world can deceive Trusted Applications (TAs) in the secure world by utilizing elaborate request parameters, compromising the sensitive data stored by other CAs. We systematically classify these Semantic Gap Vulnerabilities (SGVs) and propose a mate system for the TEE called MATEE to defend against SGVs. MATEE utilizes Arm Pointer Authentication (PA) to bind each request to the corresponding CA's identity and then verifies the identity when the CA accesses sensitive data, thereby preventing malicious request forgery. In particular, MATEE isolates sensitive data of different CAs without modifying existing CAs and TAs. Our evaluation demonstrates that MATEE successfully defends against SGVs with a minimal runtime overhead (2.19%).

---


### 40. [Aggregate, Don't Adapt: Subject-Level Posterior Aggregation and Transductive Calibration for Cross-Site Parkinsonian Gait Severity](https://arxiv.org/abs/2608.20587)

**<font color=#1a73e8>作者：</font>** Junlong Shen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We describe the winning entry to the MoCha 2026 Benchmark and Challenge on Parkinsonian Gait, which predicts MDS-UPDRS gait severity from canonicalized SMPL motion recorded at clinical sites unseen during training. The system reaches 0.6945 macro-F1 on the hidden test and ranked first of 58 entries, ahead of the runner-up at 0.5807 and the organizers' baseline at 0.4289, on a frozen public motion encoder with a single $4\times512$ linear layer. Nearly all of the margin comes from three stages usually treated as bookkeeping: reproducing the reference benchmark's exact head recipe, averaging per-walk posteriors within the subject grouping the organizers ship, and a label-free transductive calibration of the feature mean and the decision operating point. Fine-tuning the encoder lost in four distinct forms, and ten alternative encoders were worse. Every ablation number is a paid read on the hidden test, because our own leave-two-cohort-out cross-validation proved anti-correlated with the deciding score over eleven configurations. We give the negative record in full, and identify our largest gain, subject-level aggregation, as the binding ceiling on this benchmark.

---


### 41. [A Dataset-Centric Benchmark of Deep Learning Methods for Grape Leaf Disease Classification and Detection](https://arxiv.org/abs/2608.20608)

**<font color=#1a73e8>作者：</font>** Petar Canoski, Vlatko Spasev, Ivica Dimitrovski 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Grape leaf disease recognition is important for precision agriculture, enabling early diagnosis, timely intervention, and improved vineyard management. Although deep learning has achieved strong results, many studies rely on few datasets, often acquired under controlled conditions, and may not reflect real vineyard challenges such as complex backgrounds, variable illumination, occlusion, leaf pose, disease severity, and device differences. This paper presents a dataset-centric benchmark of deep learning methods for grape leaf disease classification and detection. We analyze publicly available datasets in terms of disease categories, annotation types, acquisition conditions, image characteristics, class distributions, provenance, and task suitability. Representative models are evaluated in three settings: image-level classification, region-level classification, and object detection. Classification is assessed using accuracy, while detection is evaluated using mAP@50 and mAP@50:95. Cross-dataset experiments further examine transfer between datasets with compatible disease categories but different visual and annotation characteristics. Results show near-saturated classification performance on several controlled or derivative datasets, greater difficulty on heterogeneous datasets, and substantial variation in detection performance across annotation settings. Cross-dataset performance drops sharply, especially for object detection, indicating that shared disease labels do not necessarily define equivalent recognition tasks. The benchmark emphasizes dataset provenance, realistic field evaluation, annotation compatibility, and external validation for reliable vineyard disease recognition.

---


### 42. [RECOUNT: Reference-guided Counting with Synthetic Visual Exemplars](https://arxiv.org/abs/2608.20621)

**<font color=#1a73e8>作者：</font>** Adriano D'Alessandro, Ali Mahdavi-Amiri, Ghassan Hamarneh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-guided zero-shot object counters excel at spatial localization but categorize poorly on novel or fine-grained classes: natural language is too coarse to fully specify visual identity, so they fail to separate visually similar distractors. Few-shot counters sidestep this with visual exemplars, but require manual annotations on every image. To resolve this dilemma, we introduce RECOUNT, a plug-and-play framework for image-guided zero-shot counting. Rather than specify a category with a text prompt, our key insight is to specify it visually, from a single off-scene reference image. However, we find that a lone reference image provides narrow coverage of a category's appearance and is unreliable across diverse scenes. We therefore repurpose a diffusion model as an automated contrastive data engine that expands the reference into a diverse exemplar gallery, supplying the discriminative detail that text cannot. RECOUNT preserves the class-agnostic proposals of any frozen counter and offloads categorization to a separate visual module (a frozen backbone with a lightweight head trained on this synthetic data) that matches each proposal against the target and distractor galleries. Applied to a frozen counter, RECOUNT attains the best zero-shot accuracy on both benchmarks, cutting counting error (MAE) by 55% on LookAlikes and 21% on PairTally relative to the strongest prior zero-shot counter.

---


### 43. [Pneumatic Units for Logic-based Sequential Excitation (PULSE) in Wearable Haptic Devices](https://arxiv.org/abs/2608.20626)

**<font color=#1a73e8>作者：</font>** Jessica Healey, Anoush Sepehri, Michael T. Tolley 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Soft, wearable robotic devices can deliver haptic feedback to support a wide range of tasks, such as extended reality, training various skills, and rehabilitation. Pneumatic actuation can deliver complex haptic feedback, is lightweight and compliant, and can be incorporated into textiles, making it promising for wearable applications. These soft pneumatic devices, however, typically require a valve and input for each pneumatic actuator, making it challenging to develop fully portable devices for at-home use. In this work we present a pneumatic unit for logic-based sequential excitation (PULSE). The PULSE is a flat, textile-based pneumatic actuator with embedded fluidic logic. By combining these actuators into a fluidic ring oscillator, we decreased the typical amount of required pneumatic inputs for a haptic forearm sleeve by 60%, with the ability to scale. We built the ring oscillator by optimizing design variables to reach desired periods of oscillation. We demonstrated a set of tactile stroking cues with periods ranging from 1.16 to 1.56 s and forces ranging from 1.07 to 2.04 N. We assessed the sleeve's ability to render differentiable, pleasant, and continuous haptic cues in a user study. The forearm sleeve containing PULSEs successfully delivered four directional cues and guided users to target wrist angles with fast reaction times, low overshoot amounts, and a 93.3% average accuracy of correct initial directions.

---


### 44. [SAGE: A Unified Algebra and Self-Adaptive Execution for AI Functions in SQL](https://arxiv.org/abs/2608.20630)

**<font color=#1a73e8>作者：</font>** Xiangqi Wang, Nhan H. Pham, Oktie Hassanzadeh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> SQL systems increasingly expose AI functions for tasks such as classification, extraction, filtering, ranking, retrieval, joining, and summarization. Despite their diverse APIs, these functions play only three relational roles: transforming individual rows, aggregating groups, or generating relationships between row pairs. We present SAGE (Self-Adaptive Generative Execution), a unified logical and physical framework that captures these roles with three typed primitives, AI_SCALAR, AI_AGG, and AI_JOIN, and composes them naturally with standard relational operators. All primitives share a confidence-gated execution interface while supporting physical strategies tailored to their relational shape. The main challenge is AI_JOIN, where SAGE analyzes the predicate, decomposes compound conditions when possible, and uses a recipe card together with a small label-free probe to select among complete execution strategies. Across a broad audit of public AI operators and evaluations spanning scalar, aggregate, and join workloads, this formulation covers common AI functionality while consistently improving execution quality and efficiency. SAGE achieves the strongest overall SemBench performance and, on a representative factorable join, reduces pairwise model calls by more than two orders of magnitude, yielding a 358-fold measured cost reduction.

---


### 45. [Sparse Token Routing in Efficient Transformers](https://arxiv.org/abs/2608.20632)

**<font color=#1a73e8>作者：</font>** Sai Krishna Arthanari, JaeHyeong Chang, Chengzhe Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Efficient-transformer research often motivates token pruning and adaptive computation with the claim that not all tokens require equal computational effort. We test this claim end to end using SEWN, a two-stream Transformer that routes tokens through either lightweight or full-capacity processing using a learned gate. Across our experiments, routing introduces negligible accuracy change relative to parameter-matched baselines, while the gate's token-importance signal depends critically on how it is learned. A static lexicon-seeded prior fails a counterfactual faithfulness test on BoolQ, whereas a fully contextual gate achieves highly significant separation ($p<10^{-10}$) on both evaluated tasks without changing task accuracy.

---


### 46. [MIL-BERT: Classification of Arbitrarily Large Text with Performance and Explanatory Guarantees](https://arxiv.org/abs/2608.20636)

**<font color=#1a73e8>作者：</font>** John Cadigan, Dayne Freitag, Eric Yeh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Many text classification decisions are viable based on constituent excerpts alone. Taking inspiration from the field of multiple instance learning, we present an algorithm for training a neural network to classify text by selecting such excerpts. We show that our approach is also scalable with demonstrated learning against samples with nearly 1M tokens. We evaluate our methods on 7 datasets with emphasis on long-textual collections that far exceed the encoding limit of our base model. We present state-of-the-art results with this algorithm on 3 datasets: identification of political bias in news outlets, trigger warnings in long stories, and demographic characteristics of authors in tweet collections. Furthermore, the model trained on weakly-labeled collections of text (bags) generalizes to accurately classify constituent, smaller instances. Besides a new state-of-the-art for these problems, this approach is one of the few neural methods to excel in these datasets.

---


### 47. [Provable Edge-of-Stability for Adam on a One-Dimensional Quadratic](https://arxiv.org/abs/2608.20638)

**<font color=#1a73e8>作者：</font>** Yiman Fong, Heng Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The edge-of-stability (EoS) phenomenon of Adam has been widely observed, while its underlying dynamical mechanism is not yet fully understood. We study uncorrected Adam on a one-dimensional quadratic, a clean setting where constant curvature isolates the optimizer-induced dynamics behind the EoS. We characterize the resulting dynamics across the parameter space. In broad regimes, we prove that Adam exhibits a restoring tendency toward its frozen stability threshold $2(1+\beta_1)/[\eta(1-\beta_1)]$. We also identify settings in which this edge-seeking mechanism breaks down, including strictly subcritical periodic orbits and specially tuned trajectories that converge to the optimum while remaining uniformly supercritical. These results give a concrete dynamical explanation for Adam's EoS in a setting free of evolving loss geometry, while also exposing its limitations.

---


### 48. [Directional Contextual Representations for Dependency Relations: Why Cross-Direction Pairing Fails](https://arxiv.org/abs/2608.20647)

**<font color=#1a73e8>作者：</font>** Sai Krishna Arthanari, JaeHyeong Chang, Chengzhe Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Splitting a bidirectional LSTM's contextual representation into a forward-only $F_i$ (strictly a function of tokens $1..i$) and a backward-only $B_i$ (strictly a function of tokens $i..n$) beats either alone and beats a fused self-attention representation for dependency relation-type classification. But a specific, natural extension of this idea -- pairing a token's forward state against a \emph{candidate}'s backward state (``cross-direction'' pairing, $F_i$ vs.\ $B_j$) -- consistently \emph{underperforms} same-direction pairing, and the penalty \emph{grows}, not shrinks, with token distance, both paired-bootstrap significant. We diagnose why using a frozen-trunk methodology: architectural information leakage between directions is impossible by construction (a single-layer BiLSTM, verified by code inspection); 93\% of the same-vs-cross gap survives freezing the trunk and training only fresh heads, ruling out training-co-adaptation as the primary cause; linear regression shows partial representational redundancy between $F_i$ and $B_i$ ($R^2{=}0.324$ vs.\ $0.028$ for a shuffled control) and a linear probe shows partial anticipatory encoding of upcoming tokens in $F_i$ (36.5\% vs.\ 17.2\% majority baseline) -- real effects, but neither alone, nor combined, cleanly explains the full gap. Extended frozen-trunk diagnostics (a positional probe and a distance-decay probe) show directional information is genuinely stored but not exactly positioned, and propagates only a few tokens before decaying to baseline -- consistent with, and mechanistically underneath, the distance-growth finding.

---


### 49. [Beyond Effectiveness: A Multi-Criteria Framework for Comparing Practical Socio-Technical Interventions](https://arxiv.org/abs/2608.20649)

**<font color=#1a73e8>作者：</font>** Catherine King, Lynnette Hui Xian Ng, Kathleen M. Carley  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Designers and policymakers in sociotechnical domains like content moderation, privacy interfaces, recommender systems and beyond, must choose among a growing menu of proposed interventions, but typically lack a principled basis for comparing them. Prior work tends to evaluate interventions individually and mostly along the effectiveness criteria, while implementation constraints such as cost, effort and feasibility are often considered separately. We present a multi-criteria framework for evaluating sociotechnical interventions. This framework is instantiated through the case of misinformation, a domain of intense focus for proposed countermeasures. We survey $N=39$ researchers on 40 operationalized interventions across five evaluative criteria: political feasibility, effectiveness, user acceptance, cost, and implementation effort. We find that the interventions that experts judge to be the most effective are not always the most acceptable to the public or the most feasible to implement. We also discuss how this tension has implications for the design of sociotechnical interventions beyond misinformation, and offer a decision framework for practitioners navigating the trade-offs of sociotechnical interventions.

---


### 50. [Meta-clustering of milk mid-infrared spectra identifies dairy cow groups associated with negative energy balance in early lactation](https://arxiv.org/abs/2608.20653)

**<font color=#1a73e8>作者：</font>** T. Touil, E. R. Paquet  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clustering methods have been used to identify distinct groups of milk samples, cows, or herds. Fourier-transform infrared (FTIR) spectroscopy, particularly mid-infrared (MIR) spectroscopy, has been applied to individual cow milk samples to predict various milk traits. Applying clustering directly to MIR spectral data may reveal latent groups of cows associated with milk traits or health disorders and can help prevent these conditions or monitor at-risk animals. This study aimed to identify groups of individual dairy cows in early lactation directly from milk MIR spectra and to analyze their associations with milk traits. Using a dataset of 407,632 individual milk MIR records from 3,408 commercial farms, we combined (i) spectral filtering that selects informative wavenumbers, (ii) two dimensionality-reduction methods: principal component analysis (PCA) and an autoencoder, and (iii) two clustering algorithms: k-means and spectral clustering to yield eight different clustering approaches. We regrouped the assigned clusters into meta-clusters that encompassed the most similar ones identified by the eight approaches. Our results revealed five distinct meta-clusters of early-lactation individual dairy cows significantly associated with milk traits. Despite substantial differences, the eight approaches converged on the same five meta-clusters, and the classic, computationally efficient PCA-based k-means approach using the full spectrum recaptured clusters identified by more sophisticated, computationally intensive approaches. The five meta-clusters were strongly associated with DIM and appeared to reflect a gradient of negative energy balance (NEB) severity: severe, moderate, and possibly mild, while the remaining two likely represented cows recovering from NEB, one with rapid restoration of energy balance and one in early recovery.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-158](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
