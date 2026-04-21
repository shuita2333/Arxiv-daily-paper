# 📦 其他研究 | 2026年04月22日

> 本类共 **535** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-535](./part-11.md)

---

### 101. [How to Approximate Inference with Subtractive Mixture Models](https://arxiv.org/abs/2604.16714)

**<font color=#1a73e8>作者：</font>** Lena Zellinger, Nicola Branchini, Lennert De Smet 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classical mixture models (MMs) are widely used tractable proposals for approximate inference settings such as variational inference (VI) and importance sampling (IS). Recently, mixture models with negative coefficients, called subtractive mixture models (SMMs), have been proposed as a potentially more expressive alternative. However, how to effectively use SMMs for VI and IS is still an open question as they do not provide latent variable semantics and therefore cannot use sampling schemes for classical MMs. In this work, we study how to circumvent this issue by designing several expectation estimators for IS and learning schemes for VI with SMMs, and we empirically evaluate them for distribution approximation. Finally, we discuss the additional challenges in estimation stability and learning efficiency that they carry and propose ways to overcome them. Code is available at: this https URL.

---


### 102. [Detecting Alarming Student Verbal Responses using Text and Audio Classifier](https://arxiv.org/abs/2604.16717)

**<font color=#1a73e8>作者：</font>** Christopher Ormerod, Gitit Kehat  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper addresses a critical safety gap in the use Automated Verbal Response Scoring (AVRS). We present a novel hybrid framework for troubled student detection that combines a text classifier, trained to detect responses based on their content, and an audio classifier, trained to detect responses using prosodic markers. This approach overcomes key limitations of traditional AVRS systems by considering both content and prosody of responses, achieving enhanced performance in identifying potentially concerning responses. This system can expedite the review process by humans, which can be life-saving particularly when timely intervention may be crucial.

---


### 103. [Chronax: A Jax Library for Univariate Statistical Forecasting and Conformal Inference](https://arxiv.org/abs/2604.16719)

**<font color=#1a73e8>作者：</font>** Xan Carey, Yash Deshmukh, Aileen Huang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series forecasting is central to many scientific and industrial domains, such as energy systems, climate modeling, finance, and retail. While forecasting methods have evolved from classical statistical models to automated, and neural approaches, the surrounding software ecosystem remains anchored to the traditional Python numerical stack. Existing libraries rely on interpreter-driven execution and object-oriented abstractions, limiting composability, large-scale parallelism, and integration with modern differentiable and accelerator-oriented workflows. Meanwhile, today's forecasting increasingly involves large collections of heterogeneous time series data, irregular covariates, and frequent retraining, placing new demands on scalability and execution efficiency. JAX offers an alternative paradigm to traditional stateful numerical computation frameworks based on pure functions and program transformations such as just-in-time compilation and automatic vectorization, enabling end-to-end optimization across CPUs, GPUs, and TPUs. However, this modern paradigm has not yet been fully incorporated into the design of forecasting systems. We introduce Chronax, a JAX-native time-series forecasting library that rethinks forecasting abstractions around functional purity, composable transformations, and accelerator-ready execution. By representing preprocessing, modeling, and multi-horizon prediction as pure JAX functions, Chronax enables scalable multi-series forecasting, model-agnostic conformal uncertainty quantification, and seamless integration with modern machine learning and scientific computing pipelines.

---


### 104. [Late Fusion Neural Operators for Extrapolation Across Parameter Space in Partial Differential Equations](https://arxiv.org/abs/2604.16721)

**<font color=#1a73e8>作者：</font>** Eva van Tegelen, Taniya Kapoor, George A.K. van Voorn 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Developing neural operators that accurately predict the behavior of systems governed by partial differential equations (PDEs) across unseen parameter regimes is crucial for robust generalization in scientific and engineering applications. In practical applications, variations in physical parameters induce distribution shifts between training and prediction regimes, making extrapolation a central challenge. As a result, the way parameters are incorporated into neural operator models plays a key role in their ability to generalize, particularly when state and parameter representations are entangled. In this work, we introduce the Late Fusion Neural Operator, an architecture that disentangles learning state dynamics from parameter effects, improving predictive performance both within and beyond the training distribution. Our approach combines neural operators for learning latent state representations with sparse regression to incorporate parameter information in a structured manner. Across four benchmark PDEs including advection, Burgers, and both 1D and 2D reaction-diffusion equations, the proposed method consistently outperforms Fourier Neural Operator and CAPE-FNO. Late Fusion Neural Operators achieve consistently the best performance in all experiments, with an average RMSE reduction of 72.9% in-domain and 71.8% out-domain compared to the second-best method. These results demonstrate strong generalization across both in-domain and out-domain parameter regimes.

---


### 105. [Neuroscience Inspired Graph Operators Towards Edge-Deployable Virtual Sensing for Irregular Geometries](https://arxiv.org/abs/2604.16722)

**<font color=#1a73e8>作者：</font>** William Howes, Farid Ahmed, Kazuma Kobayashi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting full-field physics through the real-time virtual sensing of engineering systems can enhance limited physical sensors but often requires sparse-to-dense reconstruction, complex multiphysics, and highly irregular geometries as well as strict latency and energy constraints for edge-deployability. Neural operators have been presented as a potential candidate for such applications but few architectures exist that explicitly address power consumption. Spiking neuron integration can provide a potential solution when integrated on neuromorphic hardware but the current existing neuron models result in severe performance degradation towards regression-based virtual sensing. To address the performance concerns and edge-constraints, we present the Variable Spiking Graph Neural Operator (VS-GNO) which integrates a sophisticated spectral-spatial convolutional analysis and a previously developed Variable Spiking Neuron (VSN) and energy-error balance loss function. With a non-spiking $L_2$ error baseline of $0.4\%$, VS-GNO can provide a reconstruction error of $0.71\%$ with $15\%$ average spiking in its spectral-only form and $1.04\%$ with $24.5\%$ spiking in its entire form. These results position VS-GNO as a promising step towards energy-efficient, edge-deployable neural operators for real-time sparse-to-dense virtual sensing in complex, highly irregular engineering environments.

---


### 106. [Active World-Model with 4D-informed Retrieval for Exploration and Awareness](https://arxiv.org/abs/2604.16733)

**<font color=#1a73e8>作者：</font>** Elaheh Vaezpour, Amirhosein Javadi, Tara Javidi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physical awareness, especially in a large and dynamic environment, is shaped by sensing decisions that determine observability across space, time, and scale, while observations impact the quality of sensing decisions. This loopy information structure makes physical awareness a fundamentally challenging decision problem with partial observations. While in the past decade we have witnessed the unprecedented success of reinforcement learning (RL) in problems with full observability, decision problems with partial observation, such as POMDPs, remain largely open: real-world explorations are excessively costly, while sim-to-real pipeline suffer from unobserved viewpoints. We introduce AW4RE (Active World-model with 4D-informed Retrieval for Exploration), an awareness-centric generative world model that provides a sensor-native surrogate environment for exploring sensing queries. Conditioned on a queried sensing action, AW4RE estimates the action-conditioned observation process. This is done by combining 4D-informed evidence retrieval, action-conditioned geometric support with temporal coherence, and conditional generative completion. Experiments demonstrate that AW4RE produces more grounded and consistent predictions than geometry-aware generative baselines under extreme viewpoint shifts, temporal gaps, and sparse geometric support.

---


### 107. [Teacher-Authored Prompts for Configuring Student-AI Dialogue: K-12 Classroom Implementation](https://arxiv.org/abs/2604.16738)

**<font color=#1a73e8>作者：</font>** Alex Liu, Min Sun, Lief Esbenshade 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> GenAI has rapidly entered instructional and learning settings as a teaching assistant or AI tutor. However, less is known about how pedagogical intent connects to the learning generated within these systems, especially when student-facing AI dialogues are fine-tuned through teacher orchestration in live classrooms. This study examines a classroom deployment of a "Classroom Teaching Aide" (TASD) system, which enables teachers to author both a teacher-to-AI setup prompt (instructional scaffold) and a student-facing conversation starter to launch AI-mediated classroom discussions. We analyze a multi-subject pilot conducted in Spring 2025, involving 20 participating teachers (16 of whom implemented the system), across 39 classrooms and 77 TASD settings, yielding 1,479 student-AI conversations with 878 unique students. Using platform logs, LLM coding with human validation, and post-study teacher interviews (N=10), we characterize teacher authoring choices and link them to enacted student-AI interaction outcomes. In deployment, student-AI conversations were largely aligned with instructional intent: 71% were fully on-track, and fewer than 1% were substantially off-track. However, a persistent design-enactment gap emerged for cognitive demand: 38% of conversations under-reached the teacher-targeted DOK level, approaching 50% when targeting DOK 3. The study also shows that explicit finish lines in the prompt reduced the DOK gap by 0.22 levels (p < .001), and "no direct answers" guardrails reduced AI final-answer rates by 8.5 percentage points. These findings position teacher-authored prompt layers as critical orchestration levers that translate pedagogical intent into structured student-AI dialogue, underscoring both their promise for scalable classroom integration and the need for additional supports to reliably sustain higher-order reasoning during enactment.

---


### 108. [CT Open: An Open-Access, Uncontaminated, Live Platform for the Open Challenge of Clinical Trial Outcome Prediction](https://arxiv.org/abs/2604.16742)

**<font color=#1a73e8>作者：</font>** Jianyou Wang, Youze Zheng, Longtian Bao 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientists have long sought to accurately predict outcomes of real-world events before they happen. Can AI systems do so more reliably? We study this question through clinical trial outcome prediction, a high-stakes open challenge even for domain experts. We introduce CT Open, an open-access, live platform that will run four challenge every year. Anyone can submit predictions for each challenge. CT Open evaluates those submissions on trials whose outcomes were not yet public at the time of submission but were made public afterwards. Determining if a trial's outcome is public on the internet before a certain date is surprisingly difficult. Outcomes posted on official registries may lag behind by years, while the first mention may appear in obscure articles. To address this, we propose a novel, fully automated decontamination pipeline that uses iterative LLM-powered web search to identify the earliest mention of trial outcomes. We validate the pipeline's quality and accuracy by human expert's annotations. Since CT Open's pipeline ensures that every evaluated trial had no publicly reported outcome when the prediction was made, it allows participants to use any methodology and any data source. In this paper, we release a training set and two time-stamped test benchmarks, Winter 2025 and Summer 2025. We believe CT Open can serve as a central hub for advancing AI research on forecasting real-world outcomes before they occur, while also informing biomedical research and improving clinical trial design. CT Open Platform is hosted at $\href{this https URL}{this https URL}$

---


### 109. [Automated Palynological Analysis System: Integrating Deep Metric Learning and $U^{2}$-Net Detection in $H\infty$ bright field microscopy](https://arxiv.org/abs/2604.16743)

**<font color=#1a73e8>作者：</font>** J. Staforelli-Vivanco, R. Jofré, B. Muñoz 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traditional melissopalynology is a time-consuming and subjective process, often taking 4-6 hours per sample. We present an automated, high-throughput microscopy system that integrates $H\infty$ robust mechanical control with advanced deep learning pipelines for the precise counting, classification, and morphological analysis of pollen grains from Bio Bio region in south central territory in Chile. Our system employs $U^{2}$-Net for salient object detection and a DINOv2 Vision Transformer backbone trained via Deep Metric Learning for classification. By integrating Gradient-Weighted Attention, the model provides human-interpretable texture and diagnostic feature annotations. The system achieves a 95.8$\%$ classification recall and a 6x processing speedup compared to manual expert analysis.

---


### 110. [Evaluating Adaptive Personalization of Educational Readings with Simulated Learners](https://arxiv.org/abs/2604.16744)

**<font color=#1a73e8>作者：</font>** Ryan T. Woo, Anmol Rao, Aryan Keluskar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a framework for evaluating adaptive personalization of educational reading materials with theory-grounded simulated learners. The system builds a learning-objective and knowledge-component ontology from open textbooks, curates it in a browser-based Ontology Atlas, labels textbook chunks with ontology entities, and generates aligned reading-assessment pairs. Simulated readers learn from passages through a Construction-Integration-inspired memory model with DIME-style reader factors, KREC-style misconception revision, and an open New Dale-Chall readability signal. Answers are produced by score-based option selection over the learner's explicit memory state, while BKT drives adaptation. Across three sampled subject ontologies and matched cohorts of 50 simulated learners per condition, adaptive reading significantly improved outcomes in computer science, yielded smaller positive but inconclusive gains in inorganic chemistry, and was neutral to slightly negative in general biology.

---


### 111. [Why Training-Free Token Reduction Collapses: The Inherent Instability of Pairwise Scoring Signals](https://arxiv.org/abs/2604.16745)

**<font color=#1a73e8>作者：</font>** Yang Shanglin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training-free token reduction methods for Vision Transformers (ToMe, ToFu, PiToMe, and MCTF) employ different scoring mechanisms, yet they share a closely matched cliff-like collapse at high compression. This paper explains \emph{why}. We develop a diagnostic framework with two tools, ranking consistency $\rho_s$ and off-diagonal correlation $\rho_\text{off}$, that decomposes the collapse into (1)a signal-agnostic error amplifier inherent to layer-wise reduction, predicting convex Pareto curves and $r_{\text{crit}} \propto 1/L$; and (2)shared reliance on \emph{pairwise} similarity signals whose ranking consistency degrades from $\rho_s{=}0.88$ to $0.27$ in deep layers. Pairwise rankings are inherently unstable ($O(N_p^2)$ joint perturbations) while unary signals enjoy greater stability ($O(N_p)$ perturbations, CLT). From three design principles derived from this diagnosis, we construct CATIS as a constructive validation: unary signals raise the trigger threshold, triage suppresses the gain. On ViT-Large at 63% FLOPs reduction, CATIS retains 96.9% of vanilla accuracy (81.0%) on ImageNet-1K where all baselines collapse to 43--65%.

---


### 112. [Incoherent Deformation, Not Capacity: Diagnosing and Mitigating Overfitting in Dynamic Gaussian Splatting](https://arxiv.org/abs/2604.16747)

**<font color=#1a73e8>作者：</font>** Ahmad Droby  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic 3D Gaussian Splatting methods achieve strong training-view PSNR on monocular video but generalize poorly: on the D-NeRF benchmark we measure an average train-test PSNR gap of 6.18 dB, rising to 11 dB on individual scenes. We report two findings that together account for most of that gap.
Finding 1 (the role of splitting). A systematic ablation of the Adaptive Density Control pipeline (split, clone, prune, frequency, threshold, schedule) shows that splitting is responsible for over 80% of the gap: disabling split collapses the cloud from 44K to 3K Gaussians and the gap from 6.18 dB to 1.15 dB. Across all threshold-varying ablations, gap is log-linear in count (r = 0.995, bootstrap 95% CI [0.99, 1.00]), which suggests a capacity-based explanation.
Finding 2 (the role of deformation coherence). We show that the capacity explanation is incomplete. A local-smoothness penalty on the per-Gaussian deformation field -- Elastic Energy Regularization (EER) -- reduces the gap by 40.8% while growing the cloud by 85%. Measuring per-Gaussian strain directly on trained checkpoints, EER reduces mean strain by 99.72% (median 99.80%) across all 8 scenes; on 8/8 scenes the median Gaussian under EER is less strained than the 1st-percentile (best-behaved) Gaussian under baseline. Alongside EER, we evaluate two further regularizers: GAD, a loss-rate-aware densification threshold, and PTDrop, a jitter-weighted Gaussian dropout. GAD+EER reduces the gap by 48%; adding PTDrop and a soft growth cap reaches 57%. We confirm that coherence generalizes to (a) a different deformation architecture (Deformable-3DGS, +40.6% gap reduction at re-tuned lambda), and (b) real monocular video (4 HyperNeRF scenes, reducing the mean PSNR gap by 14.9% at the same lambda as D-NeRF, with near-zero quality cost). The overfitting in dynamic 3DGS is driven by incoherent deformation, not parameter count.

---


### 113. [Frozen Vision Transformers for Dense Prediction on Small Datasets: A Case Study in Arrow Localization](https://arxiv.org/abs/2604.16758)

**<font color=#1a73e8>作者：</font>** Maxwell Shepherd  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a system for automated detection, localization, and scoring of arrow punctures on 40\,cm indoor archery target faces, trained on only 48 annotated photographs (5{,}084 punctures). Our pipeline combines three components: a color-based canonical rectification stage that maps perspective-distorted photographs into a standardized coordinate system where pixel distances correspond to known physical measurements; a frozen self-supervised vision transformer (DINOv3 ViT-L/16) paired with AnyUp guided feature upsampling to recover sub-millimeter spatial precision from $32 \times 32$ patch tokens; and lightweight CenterNet-style detection heads for arrow-center heatmap prediction. Only 3.8\,M of 308\,M total parameters are trainable. Across three cross-validation folds, we achieve a mean F1 score of $0.893 \pm 0.011$ and a mean localization error of $1.41 \pm 0.06$\,mm, comparable to or better than prior fully-supervised approaches that require substantially more training data. An ablation study shows that the CenterNet offset regression head, typically essential for sub-pixel refinement, provides negligible detection improvement while degrading localization in our setting. This suggests that guided feature upsampling already resolves the spatial precision lost through patch tokenization. On downstream archery metrics, the system recovers per-image average arrow scores with a median error of 1.8\% and group centroid positions to within a median of 4.00\,mm. These results demonstrate that frozen foundation models with minimal task-specific adaptation offer a practical paradigm for dense prediction in small-data regimes.

---


### 114. [Privacy-Aware Machine Unlearning with SISA for Reinforcement Learning-Based Ransomware Detection](https://arxiv.org/abs/2604.16760)

**<font color=#1a73e8>作者：</font>** Jannatul Ferdous, Rafiqul Islam, Md Zahidul Islam  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Ransomware detection systems increasingly rely on behavior-based machine learning to address evolving attack strategies. However, emerging privacy compliance, data governance, and responsible AI deployment demand not only accurate detection but also the ability to efficiently remove the influence of specific training samples without retraining the models from scratch. In this study, we present a privacy-aware machine unlearning evaluation framework for reinforcement learning (RL)-based ransomware detection built on Sharded, Isolated, Sliced, and Aggregated (SISA) training. The framework enables efficient data deletion by retraining only the affected model shards rather than the entire detector, reducing the retraining cost while preserving detection performance. We conduct a controlled comparative study using value-based RL agents, including Deep Q-Network (DQN) and Double Deep Q-Network (DDQN), under identical experimental settings with a cost-sensitive reward design and 5-fold cross-validation on Windows 11 ransomware dataset. Detection confidence is evaluated using a continuous Q-score margin, enabling ROC-AUC analysis beyond binary predictions. For unlearning, the dataset is partitioned into five shards with majority-vote aggregation, and a fast-unlearning path is evaluated by deleting 5% of the samples from a single shard and retraining only that shard. Results show that SISA-based unlearning incurs negligible utility degradation (<= 0.05 percent F1 drop) while substantially reducing retraining time relative to full SISA retraining. DDQN exhibits slightly improved stability and lower utility loss than DQN, while both agents maintain near identical in-distribution performance after unlearning. These findings indicate that SISA provides an efficient unlearning mechanism for RL-based ransomware detection, supporting privacy-aware deployment without compromising security effectiveness.

---


### 115. [CapSeal: Capability-Sealed Secret Mediation for Secure Agent Execution](https://arxiv.org/abs/2604.16762)

**<font color=#1a73e8>作者：</font>** Shutong Jin, Ruiyi Guo, Ray C. C. Cheung  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern AI agents routinely depend on secrets such as API keys and SSH credentials, yet the dominant deployment model still exposes those secrets directly to the agent process through environment variables, local files, or forwarding sockets. This design fails against prompt injection, tool misuse, and model-controlled exfiltration because the agent can both use and reveal the same bearer credential. We present CapSeal, a capability-sealed secret mediation architecture that replaces direct secret access with constrained invocations through a local trusted broker. CapSeal combines capability issuance, schema-constrained HTTP execution, broker-executed SSH actions, anti-replay session binding, policy evaluation, and tamper-evident audit trails. We describe a Rust prototype integrated with an MCP-facing adapter, formulate conditional security goals for non-disclosure, constrained use, replay resistance, and auditability, and define an evaluation plan spanning prompt injection, tool misuse, and SSH abuse. The resulting system reframes secret handling for agentic systems from handing the model a key to granting the model a narrowly scoped, non-exportable action capability.

---


### 116. [When Misinformation Speaks and Converses: Rethinking Fact-Checking in Audio Platforms](https://arxiv.org/abs/2604.16767)

**<font color=#1a73e8>作者：</font>** Chaewan Chun, Delvin Ce Zhang, Dongwon Lee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Audio platforms have evolved beyond entertainment. They have become central to public discourse, from podcasts and radio to WhatsApp voice notes and live streams. With millions of shows and hundreds of millions of listeners, audio platforms are now a major channel for misinformation. Yet existing fact-checking pipelines are mostly designed for written claims, overlooking the unique properties of spoken media. We argue that audio misinformation is not merely textual content with transcripts: it is structurally different because it is both spoken - carrying persuasive force through prosody, pacing, and emotion - and conversational - unfolding across turns, speakers, and episodes. These dual properties introduce verification difficulties that traditional methods rarely face. This position paper synthesizes evidence across modalities and platforms, examines datasets and methods, and highlights why existing pipelines fail on audio. We argue that advancing fact-checking requires rethinking verification pipelines around the spoken and conversational realities of audio.

---


### 117. [Representation Before Training: A Fixed-Budget Benchmark for Generative Medical Event Models](https://arxiv.org/abs/2604.16775)

**<font color=#1a73e8>作者：</font>** Inhyeok Lee, Luke Solo, Michael C. Burkhart 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Every prediction from a generative medical event model is bounded by how clinical events are tokenized, yet input representation is rarely isolated from other system and architectural choices. We evaluate how representation decisions affect downstream prediction after a shared one-epoch pretraining budget. We train 28 matched transformers on MIMIC-IV and evaluate them on 30 clinical outcomes in three experiments: (1) quantization granularity, reference-range anchoring, and code-value fusion; (2) value encoding (hard bins, soft discretization, code-normalized xVal) crossed with temporal encoding (event order, time tokens, admission-relative RoPE); and (3) native MIMIC laboratory/vital codes versus the Common Longitudinal ICU Format (CLIF)-remapped laboratory/vital codes with compression-preserving perturbation arms. In Experiment 1, fused code-value tokenization improves mortality AUROC from 0.891 to 0.915 (BH-adjusted p < 0.001), hospital length-of-stay AUROC from 0.763 to 0.788 (BH-adjusted p < 0.001), and, for the decile fused-vs-unfused comparison, mean regression Spearman rho across the 13 regression outcomes from 0.414 to 0.494. Across the three temporal encodings, event order only and admission-relative RoPE match or exceed inserting time tokens on average while shortening sequences by 11%. CLIF remapping preserves downstream performance in our single-site setting while yielding a smaller, clinically interpretable token set compatible with multi-site use. Finer-than-decile quantization, reference-range anchoring, and soft discretization help in selective outcomes, while code-normalized xVal remains well below the discrete and soft families, consistent with near-median suppression that persists after the affine variant.

---


### 118. [SAVE: A Generalizable Framework for Multi-Condition Single-Cell Generation with Gene Block Attention](https://arxiv.org/abs/2604.16776)

**<font color=#1a73e8>作者：</font>** Jiahao Li, Jiayi Dong, Peng Ye 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modeling single-cell gene expression across diverse biological and technical conditions is crucial for characterizing cellular states and simulating unseen scenarios. Existing methods often treat genes as independent tokens, overlooking their high-level biological relationships and leading to poor performance. We introduce SAVE, a unified generative framework based on conditional Transformers for multi-condition single-cell modeling. SAVE leverages a coarse-grained representation by grouping semantically related genes into blocks, capturing higher-order dependencies among gene modules. A Flow Matching mechanism and condition-masking strategy further enhance flexible simulation and enable generalization to unseen condition combinations. We evaluate SAVE on a range of benchmarks, including conditional generation, batch effect correction, and perturbation prediction. SAVE consistently outperforms state-of-the-art methods in generation fidelity and extrapolative generalization, especially in low-resource or combinatorially held-out settings. Overall, SAVE offers a scalable and generalizable solution for modeling complex single-cell data, with broad utility in virtual cell synthesis and biological interpretation. Our code is publicly available at this https URL

---


### 119. [Federation over Text: Insight Sharing for Multi-Agent Reasoning](https://arxiv.org/abs/2604.16778)

**<font color=#1a73e8>作者：</font>** Dixi Yao, Tahseen Rabbani, Tian Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM-powered agents often reason from scratch when presented with a new problem instance and lack automatic mechanisms to transfer learned skills to other agents. We propose a federated learning-like framework, Federation over Text (FoT), that enables multiple agents solving different tasks to collectively generate a shared library of metacognitive insights by iteratively federating their local reasoning processes. Instead of federation over gradients (e.g., as in distributed training), FoT operates at the semantic level without any gradient optimization or supervision signal. Iteratively, each agent does local thinking and self-improvement on their specific tasks independently, and shares reasoning traces with a central server, which aggregates and distills them into a cross-task (and cross-domain) insight library that existing and future agents can leverage to improve performance on related tasks. Experiments show that FoT improves reasoning effectiveness and efficiency across a wide range of challenging applications, including mathematical problem solving, cross-domain collaboration, and machine learning research insight discovery. Specifically, it improves average accuracies of downstream tasks by 24% while reducing the reasoning tokens by 28% across the first two applications. In the research insight discovery application, FoT is able to generate insights that cover over 90% of the major contributions in the subsequent papers.

---


### 120. [FairNVT: Improving Fairness via Noise Injection in Vision Transformers](https://arxiv.org/abs/2604.16780)

**<font color=#1a73e8>作者：</font>** Qiaoyue Tang, Sepidehsadat Hosseini, Mengyao Zhai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents FairNVT, a lightweight debiasing framework for pretrained transformer-based encoders that improves both representation and prediction level fairness while preserving task accuracy. Unlike many existing debiasing approaches that address these notions separately, we argue they are inherently connected: suppressing sensitive information at the representation level can facilitate fairer predictions. Our approach learns task-relevant and sensitive embeddings via lightweight adapters, applies calibrated Gaussian noise to the sensitive embedding, and fuses it with the task representation. Together with orthogonality constraints and fairness regularization, these components jointly reduce sensitive-attribute leakage in the learned embeddings and encourage fairer downstream predictions. The framework is compatible with a wide range of pretrained transformer encoders. Across three datasets spanning vision and language, FairNVT reduces sensitive-attribute attacker accuracy, improves demographic-parity and equalized-odds metrics, and maintains high task performance.

---


### 121. [EdgeVTP: Exploration of Latency-efficient Trajectory Prediction for Edge-based Embedded Vision Applications](https://arxiv.org/abs/2604.16783)

**<font color=#1a73e8>作者：</font>** Seungjin Kim, Reza Jafarpourmarzouni, Christopher Neff 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vehicle trajectory prediction is central to highway perception, but deployment on roadside edge devices necessitates bounded, deterministic end-to-end latency. We present EdgeVTP, an embedded-first trajectory predictor that combines interaction-aware graph modeling with a lightweight transformer backbone and a one-shot curve decoder. By predicting future motion as compact curve parameters (anchored at the last observed position) rather than horizon-scaled autoregressive waypoints, EdgeVTP reduces decoding overhead while producing smooth trajectories. To keep runtime predictable in crowded scenes, we explicitly bound interaction complexity via a locality graph with a hard neighbor cap. Across three highway benchmarks and two Jetson-class platforms, EdgeVTP achieves the lowest measured end-to-end latency under a protocol that includes graph construction and post-processing, while attaining state-of-the-art (SotA) prediction accuracy on two of the three datasets and competitive error on other benchmarks. Our code is available at this https URL.

---


### 122. [When Informal Text Breaks NLI: Tokenization Failure, Distribution Shift, and Targeted Mitigations](https://arxiv.org/abs/2604.16787)

**<font color=#1a73e8>作者：</font>** Avinash Goutham Aluguvelly  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study how informal surface forms degrade NLI accuracy in ELECTRA-small (14M) and RoBERTa-large (355M) across four transforms applied to SNLI and MultiNLI: slang substitution, emoji replacement, Gen-Z filler tokens, and their combination. Slang substitution (replacing formal words with informal equivalents, e.g., "going to" -> "gonna", "friend" -> "homie") causes minimal degradation (at most 1.1pp): slang vocabulary falls largely within WordPiece coverage, so the tokenizer handles it without signal loss. Emoji replaces content words with Unicode characters that ELECTRA's WordPiece tokenizer maps to [UNK], destroying the input signal before any learned parameters see it (93.6% of emoji examples contain at least one [UNK], mean 2.91 per example). Noise tokens (no cap, deadass, tbh) are fully in-vocabulary but absent from NLI training data, consistent with the model assigning them inferential weight they do not carry. The two failure modes respond to different interventions: preprocessing recovers emoji accuracy by normalizing text before tokenization; augmentation handles noise by exposing the model to noise-bearing examples during training. A hybrid of both achieves 88.93% on the combined variant for ELECTRA on SNLI (up from 75.88%), with no statistically significant drop on clean text. Against GPT-4o-mini zero-shot, unmitigated ELECTRA is significantly worse on transformed variants (p < 0.0001); hybrid ELECTRA surpasses it across all SNLI variants and reaches statistical parity on MultiNLI.

---


### 123. [Improving Radio Interferometry Imaging by Explicitly Modeling Cross-Domain Consistency in Reconstruction](https://arxiv.org/abs/2604.16794)

**<font color=#1a73e8>作者：</font>** Kai Cheng, Ruoqi Wang, Qiong Luo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radio astronomy plays a crucial role in understanding the universe, particularly within the realm of non-thermal astrophysics. Images of celestial objects are derived from the signals (called visibility) measured by radio telescopes. Such imaging results, called dirty images, contain artifacts due to factors such as sparsity and therefore require reconstruction to improve imaging quality. Existing methods typically restrict reconstruction to a unimodal domain, either to the dirty image after imaging or to the sparse visibility prior to imaging. Focusing solely on each unimodal reconstruction results in the loss of complementary in-context information in either the visibility or image domain, leading to an incomplete modeling of mutual dependency and consistency. To address these challenges, we propose CDCRec, a multimodal radio interferometric data reconstruction method that explicitly models cross-domain consistency. We design a hierarchical multi-task and multi-stage framework to enhance the exploration of interplays between domains during reconstruction. Our experimental results demonstrate that CDCRec improves imaging performance through enhanced cross-domain correlation extraction. In particular, our self-supervised complementary modeling strategy is better than current methods at interferometric domain translations that rely heavily on recovering dense information from constrained source-domain data.

---


### 124. [Generative Semantic Communication via Alternating Dual-Domain Posterior Sampling](https://arxiv.org/abs/2604.16796)

**<font color=#1a73e8>作者：</font>** Shunpu Tang, Qianqian Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative semantic communication (SemCom) harnesses pretrained generative priors to improve the perceptual quality of wireless image transmission. Existing generative SemCom receivers, however, rely on maximum a posteriori (MAP) estimation, which fundamentally cannot preserve the data distribution and thus limits achievable perceptual quality. Moreover, current diffusion-based approaches using single-domain guidance face significant limitations: latent-domain guidance is sensitive to channel noise, while image-domain guidance inherits decoder bias. Simply combining both domains simultaneously yields an overconfident pseudo-posterior. In this paper, we formulate semantic decoding as a Bayesian inverse problem and prove that posterior sampling achieves optimal perceptual quality by preserving the data distribution. Building on this insight, we propose alternating dual-domain posterior sampling (ADDPS), a diffusion-based SemCom receiver that alternately enforces latent-domain and image-domain consistency during the sampling process. This alternating strategy decomposes joint posterior sampling into simpler subproblems, avoiding gradient conflicts while retaining the complementary strengths of both domains. Experiments on FFHQ demonstrate that the proposed ADDPS achieves superior perceptual quality compared with existing methods.

---


### 125. [Frequency-Decomposed INR for NIR-Assisted Low-Light RGB Image Denoising](https://arxiv.org/abs/2604.16800)

**<font color=#1a73e8>作者：</font>** Ligen Shi, Zengyu Pang, Chang Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Addressing the issues of severe noise and high frequency structural degradation in visible images under low-light conditions, this paper proposes a Near Infrared (NIR) aided low light image restoration method based on Frequency Decoupled Implicit Neural Representation (FDINR). Based on the statistical prior of RGB-NIR cross-modal frequency correlations, specifically that low-frequency RGB signals are more reliable, whereas high frequency NIR signals exhibit higher correlation, we explicitly decompose images into distinct frequency components via multi-scale wavelet transforms and construct a dual-branch implicit neural representation framework. Within this framework, we design a cross modal differentiated frequency supervision mechanism, leveraging low light RGB to guide the reconstruction of low frequency luminance and color, and utilizing high-SNR NIR signals to constrain the generation of high frequency texture details, thereby achieving complementary advantages in the frequency domain. Furthermore, an uncertainty-based adaptive weighting loss function is introduced to automatically balance the contributions of different frequency tasks, solving the problems of color distortion and artifacts caused by rigid fusion in the spatial domain common in traditional methods. Experimental results demonstrate that FD-INR not only effectively restores image luminance consistency and structural details but also, benefitting from its implicit continuous representation, outperforms existing methods in arbitrary-resolution reconstruction tasks, significantly enhancing the reliability of low light perception.

---


### 126. [Continuous Limits of Coupled Flows in Representation Learning](https://arxiv.org/abs/2604.16801)

**<font color=#1a73e8>作者：</font>** Zilin Li, Weiwei Xu, Xuchun Tong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While modern representation learning relies heavily on global error signals, decentralized algorithms driven by local interactions offer a fundamental distributed alternative. However, the macroscopic convergence properties of these discrete dynamics on continuous data manifolds remain theoretically unresolved, notoriously suffering from parameter explosion. We bridge this gap by formalizing decentralized learning as a coupled slow-fast dynamical system on Riemannian manifolds. First, using measure-theoretic limits, we prove that the discrete spatial transitions converge uniformly to an overdamped Langevin stochastic differential equation. Second, via the Itô-Poisson resolvent and a stochastic extension of LaSalle's Invariance Principle, we establish that the representation weights unconditionally avoid divergence and align strictly with the principal eigenspace of the spatial measure. Finally, we construct a joint Lyapunov functional for the fully coupled spatial-parametric flow. This proves global dissipativity and demonstrates that orthogonally disentangled, linearly separable features emerge spontaneously at the stationary limit. Our framework bridges discrete algorithms with continuous stochastic analysis, providing a formal theoretical baseline for decentralized representation learning.

---


### 127. [Channel Attention-Guided Cross-Modal Knowledge Distillation for Referring Image Segmentation](https://arxiv.org/abs/2604.16806)

**<font color=#1a73e8>作者：</font>** Chen Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Referring image segmentation (RIS) requires accurate segmentation of target regions in images according to language descriptions, which is a cross-modal task integrating vision and language. Existing RIS methods typically employ large-scale vision and language encoding models to improve performance, but their enormous parameter size severely restricts deployment in scenarios with limited computing resources. To solve this problem, this paper proposes a channel attention-guided cross-modal knowledge distillation method, which transfers the high-order fine-grained correlations between vision and language learned by the teacher network, as well as the correlations between semantic components represented by each channel, to the student network. Compared with the traditional pixel-wise relational distillation, this method not only enables the student to learn the knowledge of the teacher, but also retains part of its independent learning ability, alleviating the transfer of learning bias. Experimental results on two public datasets show that the proposed distillation method does not introduce additional parameters during inference and can achieve significant performance improvement for the student model.

---


### 128. [Modeling Biomechanical Constraint Violations for Language-Agnostic Lip-Sync Deepfake Detection](https://arxiv.org/abs/2604.16808)

**<font color=#1a73e8>作者：</font>** Hao Chen, Junnan Xu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current lip-sync deepfake detectors rely on pixel-level artifacts or audio-visual correspondence, failing to generalize across languages because these cues encode data-dependent patterns rather than universal physical laws. We identify a more fundamental principle: generative models do not enforce the biomechanical constraints of authentic orofacial articulation, producing measurably elevated temporal lip variance -- a signal we term temporal lip jitter -- that is empirically consistent across the speaker's language, ethnicity, and recording conditions. We instantiate this principle through BioLip, a lightweight framework operating on 64 perioral landmark coordinates extracted by MediaPipe.

---


### 129. [PersonalHomeBench: Evaluating Agents in Personalized Smart Homes](https://arxiv.org/abs/2604.16813)

**<font color=#1a73e8>作者：</font>** Nikhil Verma, InJung Yang, Sungil Kim 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI systems are rapidly advancing toward real-world applications, yet their readiness in complex and personalized environments remains insufficiently characterized. To address this gap, we introduce PersonalHomeBench, a benchmark for evaluating foundation models as agentic assistants in personalized smart home environments. The benchmark is constructed through an iterative process that progressively builds rich household states, which are then used to generate personalized, context-dependent tasks. To support realistic agent-environment interaction, we provide PersonalHomeTools, a comprehensive toolbox enabling household information retrieval, appliance control, and situational understanding. PersonalHomeBench evaluates both reactive and proactive agentic abilities under unimodal and multimodal observations. Thorough experimentation reveals a systematic performance reduction as task complexity increases, with pronounced failures in counterfactual reasoning and under partial observability, where effective tool-based information gathering is required. These results position PersonalHomeBench as a rigorous evaluation platform for analyzing the robustness and limitations of personalized agentic reasoning and planning.

---


### 130. [Self-Reinforcing Controllable Synthesis of Rare Relational Data via Bayesian Calibration](https://arxiv.org/abs/2604.16817)

**<font color=#1a73e8>作者：</font>** Chongsheng Zhang, Hao Wang, Zelong Yu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Imbalanced data is commonly present in real-world applications. While data synthesis can effectively mitigate the data scarcity problem of rare-classes, and LLMs have revolutionized text generation, the application of LLMs to relational/structured tabular data synthesis remains underexplored. Moreover, existing approaches lack an effective feedback mechanism that can guide LLMs towards continuously optimizing the quality of the generated data throughout the synthesis process. In this work, we propose RDDG, Relational Data generator with Dynamic Guidance, which is a unified in-context learning framework that employs progressive chain-of-thought (CoT) steps to generate tabular data for enhancing downstream imbalanced classification performance. RDDG first uses core set selection to identify representative samples from the original data, then utilizes in-context learning to discover the inherent patterns and correlations among attributes within the core set, and subsequently generates tabular data while preserving the aforementioned constraints. More importantly, it incorporates a self-reinforcing feedback mechanism that provides automatic assessments on the quality of the generated data, enabling continuous quality optimization throughout the generation process. Experimental results on multiple real and synthetic datasets demonstrate that RDDG outperforms existing approaches in both data fidelity and downstream imbalanced classification performance. We make our code available at this https URL.

---


### 131. [Beyond Serendipity: From Exposing the Unknown to Fostering Engagement through Peer Recommendation](https://arxiv.org/abs/2604.16818)

**<font color=#1a73e8>作者：</font>** Sosui Moribe, Taketoshi Ushiama  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Serendipity-oriented recommender systems expose users to unfamiliar items to counter filter bubbles, yet mere exposure does not ensure that users will understand or appreciate the content they encounter. We propose Peer Recommendation, a framework in which a user and an AI agent (Peer) with distinct preferences collaboratively explore unfamiliar content. Unlike conventional conversational recommender systems where the user is a passive recipient, our framework positions the user as both a recommender and a recipient: the user and the Peer mutually recommend songs to each other through chat-based dialogue, collaboratively building a shared playlist. In an exploratory within-subjects experiment (N=14), we compared three conditions: (1) a Close Peer, (2) a Distant Peer, and (3) a baseline agent without an explicit preference profile. The Close Peer significantly increased users' interest expansion and perceived value of the activity compared to the baseline, with medium-to-large effect sizes. The Distant Peer showed no significant difference at the aggregate level; however, qualitative analysis revealed varied responses, with some participants strongly preferring the Distant Peer. These findings suggest that the "otherness" of a recommendation partner is essential for moving beyond mere exposure toward genuine engagement, and that the appropriate degree of preference distance may vary and need to be adapted to individual users.

---


### 132. [R&F-Inventory: A Large-Scale Dataset for Monotonic Inventory Estimation in Reach and Frequency Advertising](https://arxiv.org/abs/2604.16821)

**<font color=#1a73e8>作者：</font>** Yunshan Peng, Ji Wu, Wentao Bai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reach and Frequency (R&F) contract advertising is an important form of widely used brand advertising. Unlike performance advertising, R&F contracts emphasize controllable delivery of UV and PV under given targeting, scheduling, and frequency control constraints. In practical systems, advertisers typically need to view the UV, PV change curves at different budget levels in real time when creating an R&F contract. However, most existing publicly available advertising datasets are based on independent samples, lacking a characterization of the core structure of the "budget-performance curve" (including UV and PV) in R&F this http URL paper proposes and releases a large-scale R&F contract inventory estimation dataset. This dataset uses the R&F contract context consisting of "targeting-scheduling-frequency control" as the basic context, providing observations of UV and PV corresponding to multiple budget points within the same context, thus forming a complete budget-performance curve. The dataset explicitly includes a time-window-based frequency control mechanism (e.g.,"no more than 3 times within 5 days") and naturally satisfies the monotonicity and diminishing marginal returns characteristics in the budget and scheduling dimensions. We further derive the theoretical maximum exposure ceiling and use it as a consistency check to evaluate data quality and the feasibility of model predictions. Using this data set, this paper defines two standardized benchmark tasks: single-point performance prediction and reconstruction of budget-performance curves, and provides a set of reproducible baseline methods and evaluation protocols. This dataset can support systematic research on problems such as structural constraint learning, monotonic regression, curve consistency modeling, and R&F contract this http URL code for our experiments can be found at this https URL.

---


### 133. [Hierarchical Vision Transformer Enhanced by Graph Convolutional Network for Image Classification](https://arxiv.org/abs/2604.16823)

**<font color=#1a73e8>作者：</font>** Haibin Jiao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformer (ViT) has brought new breakthroughs to the field of image classification by introducing the self-attention mechanism and Graph Convolutional Networks(GCN) have been proposed and successfully applied in data representation and analysis. However, there are key challenges which limit their further development: (1) The patch size selected by ViT is crucial for accurate predictions, which raises a natural question: How to select the size of patches properly or how to comprehensively combine small patches and larger patches; (2) While the spatial structure information is important in vision tasks, the 1D position embeddings fails to capture the spatial structure information of patches more accurately; (3) The GCN can capture the local connectivity relationships between image nodes, but it lacks the ability to capture global graph structural information. On the contrary, the self-attention mechanism of ViT can draw the global relation on image patches, but it is unable to model the local structure of image. To overcome such limitations, we propose the Hierarchical Vision Transformer Enhanced by Graph Convolutional Network (GCN-HViT) for image classification. Specifically, the Hierarchical ViT we designed can model patch-wise information interactions on a global scale within each level and model hierarchical relationships between small patches and large patches across multiple levels. In addition, the proposed GCN method functions as a local feature extractor to obtain the local representation of each image patch which serves as a 2D position embedding of each patch in the 2D space. Meanwhile, it models patch-wise information interactions on a local scale within each level. Extensive experiments on 3 real-world datasets demonstrate that GCN-HViT achieves state-of-the-art performance.

---


### 134. [Crowded in B-Space: Calibrating Shared Directions for LoRA Merging](https://arxiv.org/abs/2604.16826)

**<font color=#1a73e8>作者：</font>** Yixuan Tang, Yi Yang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Merging separately trained LoRA adapters is a practical alternative to joint multi-task training, but it often hurts performance. Existing methods usually treat the LoRA update $\Delta W = BA$ as a single object and do not distinguish the two LoRA matrices. We show that the main source of LoRA merge interference comes from the output-side matrix $B$. Across tasks, $B$ repeatedly uses a small set of shared directions, while $A$ remains much more task-specific. As a result, the merged adapter overemphasizes these shared directions, and task-specific information is lost. We propose Pico (Pre-merge interference calibration in output-space), a data-free method that calibrates $B$ before merge by downscaling over-shared directions and then rescaling the merged update. Pico plugs directly into existing merging methods such as Task Arithmetic, TIES, and TSV-M. Across eight different benchmarks from math, coding, finance, and medical domains, Pico improves average accuracy by 3.4-8.3 points over the corresponding base method and achieves the best overall average performance. Pico also enables merged adapters to outperform the LoRA trained with all task data. These results show that LoRA merging works better when the two LoRA matrices are treated separately.

---


### 135. [ParikkhaChain: Blockchain-Based Result Processing and Privacy-Preserving Academic Record Management for the Complete Examination Lifecycle](https://arxiv.org/abs/2604.16827)

**<font color=#1a73e8>作者：</font>** Rabib Jahin Ibn Momin, Ahmed Mahir Sultan Rumi, Rezwana Reaz  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Academic examination systems worldwide continue to rely on centralised, opaque record-keeping that is often vulnerable to credential forgery, result tampering, examiner bias, and the absence of transparent re-evaluation pathways. Existing blockchain-based approaches in education focus predominantly on post-hoc certificate storage or online-only examination portals, leaving the complete onsite examination lifecycle, from conducting exams through scrutiny, largely unaddressed. This paper proposes ParikkhaChain, a blockchain-based framework that covers the entire examination lifecycle of an onsite examination system with three distinguishing contributions: (i) anonymous script evaluation through cryptographic hashing of answer scripts before examiner access, thereby eliminating identity-based bias; (ii) a transparent evaluation and scrutiny workflow backed by an immutable on-chain audit trail that records every mark submission and grade revision; and (iii) inclusion of privacy-preserving verification using zero-knowledge proofs and off-chain storage mechanisms. The system is architected around four Solidity smart contracts deployed on the Ethereum blockchain. The proposed architecture is the first initiative to our knowledge to support physical examination process, anonymous marking, and re-evaluation transparency. We successfully simulate full exam cycles of an onsite exam to grade-sheet generation using a working prototype on a large scale of 100 courses and hundreds of teachers and students. The experimental results show that the system can manage online examinations of hundreds of courses, students and faculties efficiently with great throughput, low storage, and transaction cost. Our codebase is available in open source form at this https URL

---


### 136. [The Illusion of Certainty: Decoupling Capability and Calibration in On-Policy Distillation](https://arxiv.org/abs/2604.16830)

**<font color=#1a73e8>作者：</font>** Jiaxin Zhang, Xiangyu Peng, Qinglin Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) is an increasingly important paradigm for post-training language models. However, we identify a pervasive Scaling Law of Miscalibration: while OPD effectively improves task accuracy, it systematically traps models in severe overconfidence. We trace this failure to an information mismatch: teacher supervision is formed under privileged context available during training, whereas the deployed model must report confidence using only deployment-time information. We formalize this perspective theoretically, showing that teacher-conditioned success is generally not a valid target for deployment-time confidence and that helpful privileged context induces entropy collapse and a systematic optimism bias. To address this, we propose a calibration-aware OPD framework, CaOPD, that estimates empirical confidence from model rollouts, replaces self-reported confidence with this student-grounded target, and distills the revised response through the same self-distillation pipeline. Experiments across various models and domains show that CaOPD achieves Pareto-optimal calibration while maintaining competitive capability, generalizing robustly under out-of-distribution and continual learning. Our findings highlight that capability distillation does not imply calibrated confidence, and that confidence should be treated as an essential objective in post-training. Code: this https URL

---


### 137. [DALC-CT: Dynamic Analysis of Low-Level Code Traces for Constant-Time Verification](https://arxiv.org/abs/2604.16832)

**<font color=#1a73e8>作者：</font>** Nges Brian Njungle, Edwin P. Kayang, Mishel J. Paul 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Timing side-channel attacks exploit variations in program execution time to recover sensitive information. Cryptographic implementations are especially vulnerable to these attacks, since even small timing differences in operations such as modular exponentiation or key comparisons can be exploited to extract highly sensitive information, such as secret keys. To mitigate this threat, implementations of programs that handle sensitive information are often expected to adhere to constant-time principles, ensuring that execution behavior does not depend on secret inputs. However, validating the constant-time property of programs remains a major challenge in cryptography development. Formal method approaches to verify constant-time implementations rely on abstractions that often fail to capture real execution behavior, while timing-based measurement techniques are highly sensitive to noise from other programs and even hardware environments. In this work, we propose a novel approach for verifying constant-time programs based on dynamic analysis of low-level execution traces. Our method measures instruction sequences across multiple input values for any given binary and targeted function. Any variations in the instruction mix distribution for any given pair of traces indicate a deviation from the constant-time principle and behavior. We developed an open-source tool called DALC-CT, for the constant-time verification of programs using this approach. We evaluated it on a set of well-known constant-time and non-constant-time examples, achieving a perfect detection of issues. Our results demonstrate that analyzing the logical execution of programs via instruction trace comparisons provides a lightweight and reliable way to verify the constant-time property of programs.

---


### 138. [Towards Deep Encrypted Training: Low-Latency, Memory-Efficient, and High-Throughput Inference for Privacy-Preserving Neural Networks](https://arxiv.org/abs/2604.16834)

**<font color=#1a73e8>作者：</font>** Nges Brian Njungle, Eric Jahns, Michel A. Kinsy  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Privacy-preserving machine learning (PPML) has become increasingly important in applications where sensitive data must remain confidential. Homomorphic Encryption (HE) enables computation directly on encrypted data, allowing neural network inference without revealing raw inputs. While prior works have largely focused on inference over a single encrypted image, batch processing of encrypted inputs lags behind, despite being critical for high-throughput inference scenarios and training-oriented workloads.
In this work, we address this gap by developing optimized algorithms for batched HE-friendly neural networks. We also introduced a pipeline architecture designed to maximize resource efficiency for different batch size execution. We implemented these algorithms and evaluated our work using HE-friendly ResNet-20 and ResNet-34 models on encrypted CIFAR-10 and CIFAR-100 datasets, respectively.
For ResNet-20, our approach achieves an amortized inference time of 8.86 seconds per image when processing a batch of 512 encrypted images, with a peak memory usage of 98.96 GB. These results represent a 1.78x runtime improvement and a 3.74x reduction in memory usage compared to the state-of-the-art design. For the deeper ResNet-34 model, we achieve an amortized inference time of 28.14 on a batch of 256 encrypted images using 246.78GB of RAM

---


### 139. [The CTLNet for Shanghai Composite Index Prediction](https://arxiv.org/abs/2604.16835)

**<font color=#1a73e8>作者：</font>** Haibin Jiao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Shanghai Composite Index prediction has become a hot issue for many investors and academic researchers. Deep learning models are widely applied in multivariate time series forecasting, including recurrent neural networks (RNN), convolutional neural networks (CNN), and transformers. Specifically, the Transformer encoder, with its unique attention mechanism and parallel processing capabilities, has become an important tool in time series prediction, and has an advantage in dealing with long sequence dependencies and multivariate data correlations. Drawing on the strengths of various models, we propose the CNN-Transformer-LSTM Networks (CTLNet). This paper explores the application of CTLNet for Shanghai Composite Index prediction and the comparative experiments show that the proposed model outperforms state-of-the-art baselines.

---


### 140. [Lorentz Framework for Semantic Segmentation](https://arxiv.org/abs/2604.16836)

**<font color=#1a73e8>作者：</font>** Zahid Hasan, Masud Ahmed, Nirmalya Roy  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic segmentation in hyperbolic space enables compact modeling of hierarchical structure while providing inherent uncertainty quantification. Prior approaches predominantly rely on the Poincaré ball model, which suffers from numerical instability, optimization, and computational challenges. We propose a novel, tractable, architecture-agnostic semantic segmentation framework (pixel-wise and mask classification) in the hyperbolic Lorentz model. We employ text embeddings with semantic and visual cues to guide hierarchical pixel-level representations in Lorentz space. This enables stable and efficient optimization without requiring a Riemannian optimizer, and easily integrates with existing Euclidean architectures. Beyond segmentation, our approach yields free uncertainty estimation, confidence map, boundary delineation, hierarchical and text-based retrieval, and zero-shot performance, reaching generalized flatter minima. We introduce a novel uncertainty and confidence indicator in Lorentz cone embeddings. Further, we provide analytical and empirical insights into Lorentz optimization via gradient analysis. Extensive experiments on ADE20K, COCO-Stuff-164k, Pascal-VOC, and Cityscapes, utilizing state-of-the-art per-pixel classification models (DeepLabV3 and SegFormer) and mask classification models (mask2former and maskformer), validate the effectiveness and generality of our approach. Our results demonstrate the potential of hyperbolic Lorentz embeddings for robust and uncertainty-aware semantic segmentation. Code is available at this https URL.

---


### 141. [enclawed: A Configurable, Sector-Neutral Hardening Framework for Single-User AI Assistant Gateways](https://arxiv.org/abs/2604.16838)

**<font color=#1a73e8>作者：</font>** Alfredo Metere  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present enclawed, a hard-fork hardening framework built on top of the OpenClaw single-user personal artificial intelligence (AI) assistant gateway. enclawed targets deployments that need attestable peer trust, deny-by-default external connectivity, signed-module loading, and a tamper-evident audit trail typically regulated industries such as financial services, healthcare, defense contracting, regulated R&D, and government enclaves. The framework ships in two flavors: an open flavor that preserves OpenClaw compatibility while still emitting audit, classification, and data-loss-prevention (DLP) signals, and an enclaved flavor that activates strict allowlists, Federal Information Processing Standards (FIPS) cryptographic-module assertion, mandatory module-manifest signature verification, and high-assurance peer attestation for the Model Context Protocol (MCP). The classification ladder is fully data-driven: a deploying organization selects from five built-in presets (generic, US-government, healthcare, financial services, three-tier) or supplies its own JSON. We accompany the implementation with a security review, a 204-case test suite (146 unit tests, 58 adversarial pen-tests for tamper detection, signature forgery, egress bypass, trust-root mutation, DLP evasion, prompt injection, and code injection), real-time human-in-the-loop control (per-agent pause / resume / stop and approval queues), a memory-bounded secure transaction buffer with rollback (default cap 50% of system RAM, configurable), a strict-mode TypeScript typecheck of all 22 framework files, and a GitHub Actions workflow ready for continuous integration. enclawed is a hardening framework, not an accredited compliance certification. The deploying organization remains responsible for hardware, validated cryptographic modules, certified facilities, and assessor sign-off.

---


### 142. [TowerDataset: A Heterogeneous Benchmark for Transmission Corridor Segmentation with a Global-Local Fusion Framework](https://arxiv.org/abs/2604.16848)

**<font color=#1a73e8>作者：</font>** Xu Cui, Xinyan Liu, Chen Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained semantic segmentation of transmission-corridor point clouds is fundamental for intelligent power-line inspection. However, current progress is limited by realistic data scarcity and the difficulty of modeling global corridor structure and local geometric details in long, heterogeneous scenes. Existing public datasets usually provide only a few coarse categories or short cropped scenes which overlook long-range structural dependencies, severe long-tail distributions, and subtle distinctions among safety-critical components. As a result, current methods are difficult to evaluate under realistic inspection settings, and their ability to preserve and integrate complementary global and local cues remains unclear.
To address the above challenges, we introduce TowerDataset, a heterogeneous benchmark for transmission-corridor segmentation. TowerDataset contains 661 real-world scenes and about 2.466 billion points. It preserves long corridor extents, defines a fine-grained 22-class taxonomy, and provides standardized splits and evaluation protocols.
In addition, we present a global-local fusion framework which preserves and fuses whole-scene and local-detail information. A whole-scene branch with NoCrop training and prototypical contrastive learning captures long-range topology and contextual dependencies. A block-wise local branch retains fine geometric structures. Both predictions are then fused and refined by geometric validation. This design allows the model to exploit both global relationships and local shape details when recognizing rare and confusing components. Experiments on TowerDataset and two public benchmarks demonstrate the challenge of the proposed benchmark and the robustness of our framework in real, complex, and heterogeneous transmission-corridor scenes. The dataset will be released soon at this https URL.

---


### 143. [Applications of deep generative models to DNA reaction kinetics and to cryogenic electron microscopy](https://arxiv.org/abs/2604.16851)

**<font color=#1a73e8>作者：</font>** Chenwei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This dissertation explores how deep generative models can advance the analysis of challenging biological problems by integrating domain knowledge with deep learning. It focuses on two areas: DNA reaction kinetics and cryogenic electron microscopy (cryo-EM). In the first part, we present ViDa, a biophysics-informed framework leveraging variational autoencoders (VAEs) and geometric scattering transforms to generate biophysically-plausible embeddings of DNA reaction kinetics simulations. These embeddings are reduced to a two-dimensional space to visualize DNA hybridization and toehold-mediated strand displacement reactions. ViDa preserves structure and clusters trajectory ensembles into reaction pathways, making simulation results more interpretable and revealing new mechanistic insights. In the second part, we address key challenges in cryo-EM density map interpretation and protein structure modeling. We provide a comprehensive review and benchmarking of deep learning methods for atomic model building, with improved evaluation metrics and practical guidance. We then present Struc2mapGAN, a generative adversarial network that synthesizes high-fidelity experimental-like cryo-EM density maps from protein structures. Finally, we present CryoSAMU, a structure-aware multimodal U-Net that enhances intermediate-resolution cryo-EM maps by integrating density features with structural embeddings from protein language models via cross-attention. Overall, these contributions demonstrate the potential of deep generative models to interpret DNA reaction mechanisms and advance cryo-EM density map analysis and protein structure modeling.

---


### 144. [A Community-Based Approach for Stance Distribution and Argument Organization](https://arxiv.org/abs/2604.16852)

**<font color=#1a73e8>作者：</font>** Rudra Ranajee Saha, Laks V. S. Lakshmanan, Raymond T. Ng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The proliferation of online debate platforms and social media has led to an unprecedented volume of argumentative content on controversial topics from multiple perspectives. While this wealth of perspectives offers opportunities for developing critical thinking and breaking filter bubbles (Pariser 2011), the sheer volume and complexity of arguments make it challenging for readers to synthesize and comprehend diverse viewpoints effectively. We present an unsupervised graph-based approach for community-based argument organization that helps users navigate and understand complex argumentative landscapes. Our system analyzes collections of topic-focused articles and constructs a rich interaction graph by capturing multiple relationship types between arguments: topic similarity, semantic coherence, shared keywords, and common entities. We then employ community detection to identify argument communities that reveal homogeneous and heterogeneous viewpoint distributions. The detected communities are simplified through strategic graph operations to present users with digestible, yet comprehensive summaries of key argumentative patterns. Our approach requires no training data and can effectively process hundreds of articles while preserving nuanced relationships between arguments. Experimental results demonstrate our system's ability to identify meaningful argument communities and present them in an interpretable manner, facilitating users' understanding of complex socio-political debates.

---


### 145. [CATP: Confidence-Aware Token Pruning for Camouflaged Object Detection](https://arxiv.org/abs/2604.16854)

**<font color=#1a73e8>作者：</font>** Yuhan Gao, Shuhao Kang, Xin He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camouflaged Object Detection (COD) aims to segment targets that share extreme textural and structural similarities with their complex environments. Leveraging their capacity for long-range dependency modeling, Transformer-based detectors have become the mainstream approach and achieve state-of-the-art (SoTA) accuracy, yet their substantial computational overhead severely limits practical deployment. To address this, we propose a hierarchical Confidence-Aware Token Pruning framework (CATP) tailored for COD. Our approach hierarchically identifies and discards easily distinguishable tokens from both background and object interiors, focusing computations on critical boundary tokens. To compensate for information loss from pruning, we introduce a dual-path feature compensation mechanism that aggregates contextual knowledge from pruned tokens into enriched features. Extensive experiments on multiple COD benchmarks demonstrate that our method significantly reduces computational complexity while maintaining high accuracy, offering a promising research direction for the efficient deployment of COD models in real-world scenarios. The code will be released.

---


### 146. [When W4A4 Breaks Camouflaged Object Detection: Token-Group Dual-Constraint Activation Quantization](https://arxiv.org/abs/2604.16855)

**<font color=#1a73e8>作者：</font>** Tianqi Li, Wenyu Fang, Xin He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camouflaged object detection (COD) segments objects that intentionally blend with the background, so predictions depend on subtle texture and boundary cues. COD is often needed under tight on-device memory and latency budgets, making low-bit inference highly desirable. However, COD is unusually hard to quantify aggressively. We study post-training W4A4 quantization of Transformer-based COD and find a task-specific cliff: heavy-tailed background tokens dominate a shared activation range, inflating the step size and pushing weak-but-structured boundary cues into the zero bin. This exposes a token-local bottleneck -- remove cross-token range domination and bound the zero-bin mass under 4-bit activations. To address this, we introduce COD-TDQ, a COD-aware Token-group Dual-constraint activation Quantization method. COD-TDQ addresses this token-local bottleneck with two coupled steps: Direct-Sum Token-Group (DSTG) assigns token-group scales to suppress cross-token range domination, and Dual-Constraint Range Projection (DCRP) projects each token-group clip range to keep the step-to-dispersion ratio and the zero-bin mass bounded. Across four COD benchmarks and two baseline models (CFRN and ESCNet), COD-TDQ consistently achieves an S{\alpha}score more than 0.12 higher than that of the state-of-the-art quantization method without retraining. The code will be released.

---


### 147. [Q-DeepSight: Incentivizing Thinking with Images for Image Quality Assessment and Refinement](https://arxiv.org/abs/2604.16858)

**<font color=#1a73e8>作者：</font>** Xudong Li, Jiaxi Tan, Ziyin Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image Quality Assessment (IQA) models are increasingly deployed as perceptual critics to guide generative models and image restoration. This role demands not only accurate scores but also actionable, localized feedback. However, current MLLM-based methods adopt a single-look, language-only paradigm, which departs from human evidence-seeking judgment and yields weakly grounded rationales, limiting their reliability for in-the-loop refinement. We propose Q-DeepSight, a think-with-image framework that emulates this human-like process. It performs interleaved Multimodal Chain-of-Thought (iMCoT) with tool-augmented evidence acquisition (e.g., crop-and-zoom) to explicitly determine where quality degrades and why. To train these long iMCoT trajectories via reinforcement learning, we introduce two techniques: Perceptual Curriculum Reward (PCR) to mitigate reward sparsity and Evidence Gradient Filtering (EGF) to improve credit assignment for visually-grounded reasoning. Q-DeepSight achieves state-of-the-art performance across diverse benchmarks, including natural, restored, and AI-generated content. Furthermore, we demonstrate its practical value with Perceptual-in-Generation (PiG), a training-free framework where Q-DeepSight's diagnoses guide iterative image enhancement, effectively closing the loop between assessment and refinement.

---


### 148. [GAMMA-Net: Adaptive Long-Horizon Traffic Spatio-Temporal Forecasting Model based on Interleaved Graph Attention and Multi-Axis Mamba](https://arxiv.org/abs/2604.16859)

**<font color=#1a73e8>作者：</font>** Dongyi He, Yuanquan Gao, Bin Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate traffic forecasting is crucial for intelligent transportation systems, supporting effective traffic management, congestion reduction, and informed urban planning. However, traditional models often fail to adequately capture the intricate spatio-temporal dependencies present in traffic data. To overcome these limitations, we introduce GAMMA-Net, a novel approach that integrates Graph Attention Networks (GAT) with multi-axis Selective State Space Models (Mamba). The GAT component uses a self-attention mechanism to dynamically adjust the influence of nodes within the traffic network, enabling adaptive spatial dependency modeling based on real-time conditions. Simultaneously, the Mamba module efficiently models long-term temporal and spatial dynamics without the heavy computational cost of conventional recurrent architectures. Extensive experiments on several benchmark traffic datasets, including METR-LA, PEMS-BAY, PEMS03, PEMS04, PEMS07, and PEMS08, show that GAMMA-Net consistently outperforms existing state-of-the-art models across different prediction horizons, achieving up to a 16.25% reduction in Mean Absolute Error (MAE) compared to baseline models. Ablation studies highlight the critical contributions of both the spatial and temporal components, emphasizing their complementary role in improving prediction accuracy. In conclusion, the GAMMA-Net model sets a new standard in traffic forecasting, offering a powerful tool for next-generation traffic management and urban planning. The code for this study is available at this https URL

---


### 149. [CCAR: Intrinsic Robustness as an Emergent Geometric Property](https://arxiv.org/abs/2604.16861)

**<font color=#1a73e8>作者：</font>** Akash Samanta, Manish Pratap Singh, Debasis Chaudhuri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard supervised learning optimizes for predictive accuracy but remains agnostic to the internal geometry of learned features, often yielding representations that are entangled and brittle. We propose Class-Conditional Activation Regularization (CCAR) to explicitly engineer the feature space, imposing a block-diagonal structure via a soft inductive bias. By shaping the latent representation to confine class energy to orthogonal subspaces, we create an intrinsic geometric scaffold that naturally filters noise and adversarial perturbations. We provide theoretical analysis linking this structural constraint to the maximization of the Fisher Discriminant Ratio, establishing a formal connection between geometric disentanglement and algorithmic stability. Empirically, this approach demonstrates that robustness is an emergent property of a well-engineered feature space, significantly outperforming baselines on label noise and input corruption benchmarks.

---


### 150. [Governed MCP: Kernel-Level Tool Governance for AI Agents via Logit-Based Safety Primitives](https://arxiv.org/abs/2604.16870)

**<font color=#1a73e8>作者：</font>** Daeyeon Son  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents increasingly call external tools (file system, network, APIs) through the Model Context Protocol (MCP). These tool calls are the agent's syscalls -- privileged operations with side effects on shared state -- yet today's safety enforcement lives entirely in userspace, where a 10-line script can bypass it. I propose Governed MCP, a kernel-resident tool governance gateway built on a logit-based safety primitive (ProbeLogits, companion paper: arXiv:2604.11943). The gateway interposes on every MCP tool call in a 6-layer pipeline: schema validation, trust tier check, rate limit, adversarial pre-filter, ProbeLogits gate (the load-bearing semantic check), and constitutional policy match, with a Blake3-hashed audit chain.
I implement Governed MCP in Anima OS, a bare-metal x86_64 OS in approximately 86,000 lines of Rust. The five non-inference layers add 65.3 microseconds of overhead per call; ProbeLogits adds 65 ms (per-token-class semantic decision) on 7B Q4_0. A 4-config ablation on a 101-prompt MCP-domain benchmark shows that removing the ProbeLogits layer collapses F1 from 0.773 to 0.327 (Delta F1 = -0.446) -- hand-rule firewalling alone is insufficient. All 15 WASM-to-system host functions in the runtime route through the gateway (complete mediation of the WASM ABI surface; the scope and caveats of this claim are stated in Section 4.6); a 10-LoC userspace bypass that defeats existing guardrail libraries is structurally impossible against the kernel-resident gate.

---


> [!TIP]
> 当前位于：**101-150**（第 3/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-535](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
