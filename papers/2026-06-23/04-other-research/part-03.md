# 📦 其他研究 | 2026年06月23日

> 本类共 **654** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-654](./part-14.md)

---

### 101. [Power Systems Agent Benchmark: Executable Evaluation of AI Agents in Electric Power Engineering](https://arxiv.org/abs/2606.20950)

**<font color=#1a73e8>作者：</font>** Sergei Trashchenkov  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Executable evaluation -- checking the consequences of an agent's actions with a program rather than grading its prose -- has become a prominent way to assess tool-using AI agents in software settings. Electric power engineering has not yet had an analogous benchmark: language-model use is still dominated by retrieval and text question answering, while agents acting on power-system artifacts remain mostly academic prototypes. We introduce the Power Systems Agent Benchmark, an executable benchmark for power-engineering agents. An agent receives a structured task and returns a structured solution; a deterministic evaluator recomputes the engineering quantities, checks operational constraints, and returns a feasibility flag, a normalized score, and explicit violations.
The benchmark contains 41 task families across eight areas of power engineering, from power flow and protection to stability, microgrids, reliability, power quality, and forecasting. Each task is grounded in a citable source, standard, or documented engineering formulation. To resist contamination, held-out cases are synthesized on demand by per-family generators from private seeds: the construction is inspectable, but the instances remain private. In a reference evaluation with three command-line agents, the strongest score near the compact tier's ceiling, a smaller open model trails, and public and held-out performance are broadly consistent; a separate public-split grid with OpenCode and Aider probes harness effects. The reference evaluation doubles as quality control: unanimous failures flag candidate task or evaluator defects, and it exposed a latent evaluator bug missed by self-consistency checks. The evaluators are compact deterministic surrogates, but the task contract allows their internals to be upgraded to simulator-backed checks without changing how tasks are posed or solved.

---


### 102. [Learning What Not to Forget: Long-Horizon Agent Memory from a Few Kilobytes of Learning](https://arxiv.org/abs/2606.20954)

**<font color=#1a73e8>作者：</font>** Nusrat Jahan Lia, Aritra Mazumder  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-running language-model systems accumulate interaction history that outgrows the context window, so they must continually evict. When an eviction policy drops a load-bearing detail, for example an access token issued at login or a path the next call needs, the action fails. We present LRE (Learned Relevance Eviction), a few kilobytes, CPU-only, language-model-free scorer that learns which units of history are load-bearing and keeps them by verbatim extraction. Under a matched-budget comparison, in our experiment, no baseline dominates LRE on the accuracy-cost plane. On agents, LRE matches the accuracy of keeping the entire history overall. On the simplest tasks, it exceeds that no-eviction baseline by 27%, while requiring zero compressor calls and reducing peak context size by up to 52%. A controlled study trace shows LRE completes tasks where the others loop, finishing one such task in 37% fewer calls than keeping everything and solving 14 tasks where no other run policy does. On conversational memory, LRE outranks dense and token-pruning encoders at zero neural cost. In downstream evaluation, LRE gives the best budgeted answer quality on LoCoMo reading 68% fewer tokens. Its supervision can also be annotation-free: training only on the system's own behavior recovers 95% of the supervised scorer's effectiveness. We argue that, because memory eviction in LLM agents is a fidelity problem, it requires a deployable proactive policy where the future query is unavailable and exact state is decisive, and that cheap learned relevance can be sufficient.

---


### 103. [Generative Responsible AI Data Evaluation Schema (GRAIDES) for AI Assurance in Local Government](https://arxiv.org/abs/2606.20963)

**<font color=#1a73e8>作者：</font>** Ethan Knights, Christopher Conlan, Temilorun Gbolahan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Trust in the application of generative Artificial Intelligence (AI) relies on well-governed measurable evidence of performance and safety. In practice, however, evaluation data is often fragmented across systems, inconsistently structured and difficult to compare. We introduce the Generative Responsible AI Data Evaluation Schema (GRAIDES) as a lightweight open-source data model for centralising AI observability across popular vendors. Practical blueprints for code, architecture and statistical evaluation are shared as guidance about how to approach generative system assurance at the organisational level. Illustrative case study results are reported from Westminster City Council's AI catalogue with a focus on measuring human-model alignment including detecting systematic disagreement between evaluators. By framing evaluations as a data modelling problem, GRAIDES provides a practical pathway toward more consistent and reproducible benchmarking, tuning and assurance activities for generative AI systems.

---


### 104. [Formalizing Task-Space Complexity for Zero-Shot Generalization](https://arxiv.org/abs/2606.20967)

**<font color=#1a73e8>作者：</font>** Jung-Hoon Cho, Heling Zhang, Siqi Du 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Policies must operate across diverse conditions, yet a single policy is often conservative while fully adaptive schemes can be complex. We study zero-shot generalization in contextual dynamical systems and introduce a performance-centric, directional task dissimilarity--the signed divergence--that upper bounds the generalization gap from a source context to a target context. The signed divergence induces $\varepsilon$-tolerance sets that certify when a source policy class generalizes, and it yields a concrete notion of task-space complexity: the minimum number of source contexts needed so that every target context incurs at most $\varepsilon$ generalization gap. Under a mild local smoothness assumption on performance, the induced tolerance sets admit certified inner/outer balls and instance-dependent volume bounds on task-space complexity. In the finite-oracle setting, source selection reduces to set cover; a greedy strategy inherits the standard $H(n)$ approximation guarantee. Using a Mass-Spring-Damper system with linear-quadratic regulator (LQR) controllers and a nonlinear CartPole system with deep reinforcement learning controllers, we show that greedy selection achieves the same $\varepsilon$-coverage with fewer policies than uniform or random baselines. Our approach delivers a performance-based task similarity measure and practical certificates for building generalizable control with simple policies.

---


### 105. [CogniRoute: Learning to Route Social Evidence in Omni-Modal Models](https://arxiv.org/abs/2606.20970)

**<font color=#1a73e8>作者：</font>** Yifan Shen, Pei Tian, Xinzhuo Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Omni-modal models can ingest video, audio, and text, but unified access to multiple modalities does not guarantee that a model uses the right evidence. This gap is especially pronounced in social video question answering, where the answer may hinge on a gesture, vocal tone, temporal cue, or mismatch between what is said and what is visually expressed. We introduce CogniRoute, a schema-guided Mixture-of-Experts framework for social omni reasoning. CogniRoute uses a training-only cognitive schema that factorizes each example by cross-modal relation, reasoning demand, and temporal scope, and aligns global routing signatures with this structure during supervised fine-tuning. We further introduce route-aware reinforcement learning, which jointly optimizes token generation and expert allocation using rewards for answer correctness, modality-consistent reasoning, and cognitive temporal grounding. To support training and evaluation, we construct OmniSocialBench, a diagnostic social video QA resource with 118K structured training examples, grounded reasoning traces, schema labels, temporal evidence spans, and a manually verified evaluation split. CogniRoute achieves 59.38\% average accuracy on OmniSocialBench, improving over the strongest proprietary baseline by 15.33 percentage points and the strongest open-source omni baseline by 26.77 points, with the largest gains on questions requiring audio-visual coordination, conflict resolution, and temporally grounded social inference.

---


### 106. [UNITY: Attention Flow Networks for Adaptive Conditioning in Diffusion](https://arxiv.org/abs/2606.20971)

**<font color=#1a73e8>作者：</font>** Aryan Das, Koushik Biswas, Moloud Abdar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce UNITY, a Universal-to-Specialized adapter for efficient and scalable composite conditioning in diffusion based image generation. Unlike prior methods that train separate adapters for each conditioning modality, UNITY jointly learns shared semantics across multiple conditioning types and subsequently specializes without modifying the underlying architecture. The proposed two stage training paradigm consists of a Universal Stage that captures cross modal representations across all conditioning modalities using half of the total training steps, followed by a Specialization Stage that refines modality specific features using the remaining training budget. At the core of UNITY are the Morphable Attention Flow (MAF) Network and Morph Wrapper modules, which enable channel aware and spatially adaptive feature alignment through learnable flow fields and attention based fusion. This constant complexity formulation supports flexible operation under both single and composite conditioning settings while significantly reducing inference latency and memory consumption. Extensive experiments across multiple datasets demonstrate that UNITY achieves state of the art image fidelity while maintaining superior memory efficiency. Code: this https URL

---


### 107. [Detecting Satellites in Radio-Frequency Data via Semi-Supervised Learning](https://arxiv.org/abs/2606.20976)

**<font color=#1a73e8>作者：</font>** Cade W. Trotter, Maksim E. Eren, Justin C. Holmes 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Radio-frequency (RF) monitoring is essential for space domain awareness, but it often generates large, variable, and sparsely populated datasets with few labels. These observations can capture satellites, space debris, and the ionospheric background, yet interpreting them typically requires specialized subject-matter expertise. Supervised deep learning methods can perform well on labeled RF data, but they require many annotated examples and may need careful retraining as RF conditions change. Semi-supervised approaches offer a practical alternative for limited-data settings by using unlabeled observations to reveal latent patterns that experts can interpret. In this paper, we present a semi-supervised RF detection and classification workflow for satellite monitoring that combines Non-negative Matrix Factorization with automatic model determination (NMFk), expert-guided cluster interpretation, and classifier-based prediction. We first represent RF observations as a non-negative feature matrix and apply NMFk to estimate the number of clusters that best captures patterns in the unlabeled data. Subject-matter experts then assign physical meaning to the resulting clusters, including satellite detections, ionospheric environmental conditions, and other RF event categories. Finally, we train a classifier on these interpreted clusters to evaluate performance on a test set and categorize future observations. This pipeline reduces reliance on large pre-labeled datasets by pairing unsupervised factorization with expert interpretation, enabling an interpretable and transferable methodology for detecting, observing, and classifying behavior in RF data.

---


### 108. [How Should Agents Read Demonstrations? Hierarchical Structure Beats Flat Action Logs](https://arxiv.org/abs/2606.20978)

**<font color=#1a73e8>作者：</font>** Honjar Xing, Jefferson Lin, Henry Lieberman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Programming by Demonstration (PbD) offers a human-centered way to author procedural knowledge for LLM agents: users communicate what they want by showing rather than by writing prompts or code, making agent authoring accessible to non-programmers. The natural output of a PbD recording is a flat action log, but how this log is organized before being passed to the agent is an open design question with significant consequences for plan quality. We propose grouping recorded actions into labeled, hierarchical subgoals and evaluate the effect of this organizational structure in a controlled experiment. Across 85 web automation tasks, we compare a zero-shot baseline against four demonstration formats that share identical action sequences but differ in structure. On 43 natural-language tasks with vague descriptions, hierarchically grouped demonstrations improve pass rates from 76.7\% to 90.7\% (paired permutation test $p{=}0.034$; win-loss 6:0), while flat demonstrations show a smaller, non-significant improvement. On 42 tasks with precise descriptions, no format provides any benefit, confirming that the hierarchical advantage arises specifically when descriptions leave procedural details ambiguous. Ablation shows that subgoal grouping alone drives the effect: preconditions, postconditions, and parameter annotations add no measurable benefit. These results offer a concrete design recommendation for PbD pipelines and, more broadly, for any system that feeds procedural context to an LLM agent: segment action sequences into named subgoal groups rather than presenting flat step lists.

---


### 109. [Robusto-2: Benchmarking Humans & VLMs for Autonomous Driving in Lima & New York City](https://arxiv.org/abs/2606.20980)

**<font color=#1a73e8>作者：</font>** Adrian Cespedes, Marcelo Chincha, Dunant Cusipuma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As Self-Driving Cars continue to expand internationally and use multi-modal systems such as VLMs as a cognitive backbone for their Action models; how well will these systems generalize in new settings, in particular out-of-distribution (OOD) edge-case scenarios in new geographies? In this paper, we study this open question by providing a full factorial analysis with human drivers of Lima, human drivers from New York City, and VLMs and showing them dashcam footage collected from Lima and New York City -- prompting them with a variety of questions under a Visual Question Answering (VQA) paradigm. In particular, we pick these two cities as they are highly challenging driving locations where no Self-Driving Car company currently operates in, and ask questions that span 4 categories: Factual, Ratings, Counterfactual and Reasoning. We find that Humans and VLMs diverge in their responses -- though this is modulated by the type of questions asked, and that Humans answer similarly independent of where they are from (Lima/NYC). To our surprise, we did not find a strong difference in terms of answers (Humans or VLMs) that was modulated by geography, likely due to their high out-of-distribution nature. Our dataset is available at: this https URL

---


### 110. [Physics-Guided Fully Convolutional Spatiotemporal Learning Toward Digital-Twin-Enabled Microstructure Evolution Prediction](https://arxiv.org/abs/2606.20983)

**<font color=#1a73e8>作者：</font>** Michael Trimboli, Wenxi Liu, Xianqi Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding and predicting microstructure evolution is central to materials design, yet purely data-driven spatiotemporal learning models often suffer from limited physical consistency and degraded long-term prediction accuracy. In this work, we introduce a physics-guided fully convolutional spatiotemporal learning framework for microstructure evolution prediction. Unlike prior self-supervised approaches, the proposed method explicitly incorporates governing physical equations into the training objective, thereby encouraging the learned dynamics to remain consistent with known thermodynamic and kinetic laws. This physics-guided formulation improves predictive accuracy, long-horizon stability, and robustness across spatial resolutions and temporal prediction settings. Extensive experiments for spinodal decomposition demonstrate that incorporating physics-guided residual regularization leads to more faithful reproduction of microstructural morphology, statistics, and evolution trends compared with purely data-driven baselines. The proposed framework preserves the scalability and computational efficiency of fully convolutional architectures while bridging the gap between high-fidelity physics-based simulations and data-driven surrogate modeling, offering a reliable and efficient surrogate-modeling step toward digital-twin-enabled microstructure evolution prediction.

---


### 111. [Phonemes to the Rescue: Multilingual Tokenization Based on International Phonetic Alphabet](https://arxiv.org/abs/2606.20993)

**<font color=#1a73e8>作者：</font>** Milan Miletić, Julie Kallini, Ekaterina Shutova  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual language models often exhibit performance disparities across languages that can arise as early as the tokenization stage. Widely-used subword tokenization approaches favor high-resource languages, and tokenizer-free methods still yield longer sequences for scripts with a higher bytes-per-character ratio. To address these shortcomings, we propose to use the International Phonetic Alphabet (IPA) as a language-agnostic input representation for multilingual tokenizers. IPA provides a compact symbol inventory, greater cross-lingual character overlap, and a more balanced byte-per-character distribution across languages. We train matched pairs of text vs. IPA subword tokenizers across 24 languages and 14 scripts and demonstrate that IPA tokenizers consistently improve tokenization quality, especially for non-Latin scripts, and generalize more effectively to unseen languages and scripts.

---


### 112. [BioInsight: Multi-Agent Orchestration for Interactive Biomedical Knowledge Discovery](https://arxiv.org/abs/2606.20997)

**<font color=#1a73e8>作者：</font>** Jieyi Wang, Bingxuan Li, Nanyi Jiang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Biomedical researchers increasingly use AI-generated analyses and reports to interpret protein-level signals, but static outputs are often insufficient for research decision-making, where users need to inspect evidence, assess uncertainty, compare mechanisms, and refine hypotheses. We present \textsc{BioInsight}, a multi-agent system that moves from static biomedical report generation to interactive evidence-centered interactive interface generation. Given a disease name, a protein association table, and optional cohort metadata, BioInsight organizes disease-specific evidence through typed intermediate artifacts, including ranked pathways, literature evidence packets, protein-level reasoning notes, citation-grounded reports, dashboard schemas, and rendered interactive interfaces. The system decomposes evidence retrieval from mechanistic reasoning, normalizes citations through deterministic components, and converts the same structured evidence used in the report into an interactive interface. We evaluate BioInsight on standardized biomedical QA, challenging protein-function reasoning, and end-to-end biomedical evidence synthesis. Results show that BioInsight achieves best, and suggest that biomedical AI systems should move beyond text-only and static reports toward provenance-preserving, interactive evidence artifacts.

---


### 113. [Closure of Self-Determining System Based on Causal and Constitutive Relations](https://arxiv.org/abs/2606.21010)

**<font color=#1a73e8>作者：</font>** Yoshiyuki Ohmura, Earnest Kota Carr, Yasuo Kuniyoshi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A self-determining system is defined as one in which causes originating within the system influence the system itself. This definition raises the question of how to specify system boundaries. Although the concept of "closure" is commonly used for this purpose, defining boundaries solely in terms of causal relations introduce challenges, such as how to handle external causes and circular causality. To address this issue, we introduce two types of asymmetric relations: causal and constitutive. We propose that system boundaries can be defined as closures of loops formed by these relations, referred to as causal-constitutive loops. By constraining constitutive relations, the resulting system necessarily includes internal causes and thereby satisfies self-determination. Furthermore, to prevent reduction to supervenience, constitutive relations must involve at least two independent variables. This minimal requirement leads to two interdependent loops, which implies a dual-process organization.

---


### 114. [The AI Evaluability Gap: The Missing Layer for Managing Risk and Sustaining Value](https://arxiv.org/abs/2606.21015)

**<font color=#1a73e8>作者：</font>** Vishal Srivastava, Tanmay Sah  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Organizations deploying AI face two fundamental governance challenges: managing AI risk and sustaining AI value. Both depend on evidence whose sufficiency cannot be taken for granted. We call the shared underlying challenge the AI Evaluability Gap: the condition in which organizations lack sufficient evidence to support high-confidence governance decisions regarding either risk or value.
We argue that this gap reflects a category error in current practice. Existing governance approaches focus primarily on properties of systems, such as safety, fairness, reliability, compliance, and value, while paying comparatively little attention to the evidentiary foundations required to justify decisions about those properties. We further argue that AI governance encompasses both operational decisions regarding whether a system may operate and investment decisions regarding whether it merits continued organizational resources.
To address this problem, we introduce Evaluability, defined as the capability of a system to generate, maintain, and renew evidence sufficient to support high-confidence governance decisions over time. We formalize governance decisions as functions of calibrated confidence Conf(D|E) and identify six properties of evaluable evidence: observability, attributability, intervenability, verifiability, calibration, and temporal validity.
The framework distinguishes Operational Certification, which relies primarily on structural evidence to justify deployment decisions, from Investment Certification, which relies primarily on causal evidence to justify continued resource allocation. We argue that evidence sufficiency is a missing layer of AI governance and that closing the AI Evaluability Gap is a prerequisite for both managing risk and sustaining value in AI-enabled organizations.

---


### 115. [Quantifying the Impact of Stealthy BLE Spam & Flooding Attacks on IoT Environments](https://arxiv.org/abs/2606.21016)

**<font color=#1a73e8>作者：</font>** Usman Rauf, Adalynn Martinez, Fadi Mohsen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The energy-efficient design of the BLE protocol, emphasis on rapid, and userfriendly discovery, making it an ideal choice for IoMTs, specifically, military field medical systems, and battlefield wearable sensors. Especially in active conflict zones, when static medical facilities are vulnerable and often targeted, limiting their viability for sustained care delivery. This rapid deployment, and ease of management comes at the cost of expanded attack surface, i.e., BLE flooding attacks. During such attacks, adversaries flood advertisement channels with unauthorized connection or advertising requests to exhaust nearby device resources and disrupt legitimate communication, sometimes culminating in denial-of-service conditions. A first public proof-of-concept of such attacks, using a Raspberry Pi has since been adapted to commodity platforms (e.g., Flipper Zero, HackRF, Android), lowering the barrier to attack. In contested environments, such platforms are directly relevant to adversarial RF jamming and spoofing operations, where low-cost, portable devices can induce disproportionate disruption in dense wireless ecosystems. In this work, we develop a quantitative foundation for understanding the impact of such attacks and propose a practical deterrence strategy based on agility to raise the cost of such attacks.

---


### 116. [CheXpercept: A Benchmark for Evaluating Expert-Level Lesion Perception in Chest X-rays](https://arxiv.org/abs/2606.21020)

**<font color=#1a73e8>作者：</font>** Geon Choi, Hangyul Yoon, Nalee Kim 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The evaluation of vision-language models (VLMs) for chest X-ray (CXR) analysis has largely been limited to disease-presence classification without visual grounding. Such evaluations fail to verify the expert-level lesion perception necessary to ensure the clinical reliability of VLMs. To address these limitations, we introduce CheXpercept, a sequential, multi-level perception benchmark that mirrors a radiologist's cognitive workflow across coarse-level detection, fine-level contour evaluation and revision, and semantic-level attribute extraction. To ensure high clinical fidelity at scale, we construct the dataset using a semi-automated generation pipeline paired with a review by six medical experts. CheXpercept contains 10,400 QA items derived from 2,100 CXRs, covering seven clinically critical pulmonary and cardiac lesions. To demonstrate the current landscape of VLM perception, we benchmark 14 general and medical VLMs on CheXpercept. The models achieve adequate performance only at the coarse level, with accuracy degrading precipitously on deeper visual tasks. Notably, medical VLMs show almost no perceptual advantage over their general-domain counterparts, highlighting a systemic flaw in current domain adaptation. The code and dataset will be publicly available.

---


### 117. [Continuous-Time Probabilistic Correctors for Uncertainty-Aware Physics-Based Spacecraft Trajectory Forecasting](https://arxiv.org/abs/2606.21021)

**<font color=#1a73e8>作者：</font>** Muhammad Bilal Shahid, Zhanhong Jiang, Soumik Sarkar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon spacecraft trajectory forecasting suffers from error accumulation due to the absence of corrective observations in the forecast regime, making reliable uncertainty estimation crucial for safety-critical decision-making such as space domain awareness and conjunction assessment. While high-fidelity physics-based orbit propagators provide accurate deterministic forecasts, they typically lack calibrated uncertainty estimates over long horizons. We introduce a Predictor--Corrector framework in which a physics-based continuous-time $\textit{deterministic}$ forecaster is augmented with a learned continuous-time $\textit{probabilistic}$ Corrector that models forecast errors. The proposed Corrector can be wrapped around an existing deterministic propagator to improve forecast accuracy while producing sharp and calibrated full-covariance uncertainty estimates. The Corrector is based on Latent Neural Controlled Differential Equations (Latent NCDEs) and models the probabilistic temporal evolution of forecast errors in continuous time, naturally supporting irregular sampling and missing features. We further introduce a loss function that promotes calibration and sharpness in long-horizon uncertainty propagation. We evaluate the proposed framework on long-horizon spacecraft trajectory forecasting using real-world data from NASA's Crustal Dynamics Data Information System (CDDIS), wrapping the Corrector around NASA's General Mission Analysis Tool (GMAT). Across forecast horizons of 2--4 days without observations and six rolling test windows, the proposed approach consistently improves accuracy and uncertainty calibration compared to deterministic baselines and Latent ODE-based correctors, demonstrating the effectiveness of the continuous-time probabilistic Corrector for trajectory forecasting.

---


### 118. [Structure-Aware Graph Multi-Task Learning for Dynamic Sparse OD Demand Prediction](https://arxiv.org/abs/2606.21022)

**<font color=#1a73e8>作者：</font>** Ming Xu, Jiawei Cao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Origin-Destination (OD) demand prediction is fundamental to intelligent transportation systems, yet real-world OD flows are often dynamically sparse, long-tailed, and characterized by heterogeneous zero-flow patterns. These properties make it difficult to distinguish whether an OD connection is active from how much demand it generates once activated. Many existing methods primarily treat OD prediction as a single flow regression task, which limits their ability to model low-frequency, intermittent, and long-tailed OD interactions. To address these challenges, we propose SAGMTL, a Structure-Aware Graph Multi-Task Learning framework for dynamic sparse OD demand prediction. SAGMTL decomposes OD prediction into structural state modeling and flow intensity estimation, jointly learning regional activity states, OD connection activity, and edge-level flow intensity within a unified framework. Specifically, a node-edge collaborative representation module captures regional semantics, temporal dynamics, and spatial priors through interactive node-edge updates, producing structure-aware representations for dynamic OD interactions. Based on these representations, SAGMTL estimates OD flows by jointly modeling stable demand patterns and short-term fluctuations. A multi-constraint objective further improves sparsity awareness and structural consistency. Experiments on three real-world urban mobility datasets from Beijing, Chengdu, and Nanjing show that SAGMTL achieves superior overall performance compared with state-of-the-art baselines. Further analysis demonstrates that explicitly modeling regional activity, connection states, and flow intensity improves the robustness of dynamic sparse OD demand prediction.

---


### 119. [Negative Knowledge as Failure-aware Shared Memory for AutoResearch](https://arxiv.org/abs/2606.21024)

**<font color=#1a73e8>作者：</font>** Hanchun Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI-assisted research systems generate many failed attempts, but those failures rarely become a durable, shared knowledge asset. We propose a negative knowledge memory layer: a curator agent converts each failed attempt into a bounded, typed record in a shared bank, and a downstream research agent explicitly adopts or rejects those records before proposing its next experiment. We evaluate this layer in two settings: same-task retry on ScienceAgentBench and cross-task scientific research on two nonlinear math-physics PDE problems. The negative knowledge layer outperforms vanilla AutoResearch baselines while using fewer tokens; agents with the negative knowledge bank solve new tasks that all baselines fail to solve in PDE systems research. We also show that the previous negative knowledge bank can transfer and enhance AutoResearch on different PDE problems. These results suggest that structured negative knowledge is a knowledge asset that should be explicitly maintained in broader AI-engaged scientific research beyond a memory-compression or debugging aid, alongside positive findings, as a collective infrastructure for scientific memory. Code is available at this https URL.

---


### 120. [Sparse Point-Guided Fusion of Supervised and Self-Supervised Learning Model for Seaweed Segmentation](https://arxiv.org/abs/2606.21026)

**<font color=#1a73e8>作者：</font>** Tatsuya Suzuki, Kazuya Ijuin, Hideki Tomimori 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The ocean plays a critical role in sustainable development, particularly in climate change mitigation. Among marine ecosystems, blue carbon ecosystems are recognized as important natural carbon sinks. In this context, this paper addresses precise seaweed classification for blue carbon quantification in Ocean Digital Twin initiatives. Conventional methods, including supervised learning (limited by data scarcity and domain gaps) and self-supervised learning (unable to assign class labels), struggle with underwater complexities and diverse seaweed species. To overcome this, we propose a novel two-stage seaweed segmentation technique. This technique first utilizes Supervised and Self-supervised Learning Model Propagation (this http URL.), which leverages supervised learning for initial class information and approximate locations, guiding self-supervised learning for detailed, accurate segmentation. Subsequently, MaskFusion (MF) refines these results by merging instance-level masks for highly accurate segmentation. This integrated approach allows automatic class label assignment and mitigates domain gap effects. Specifically, instance segmentation estimates sparse point locations which then guide self-supervised learning for detailed region segmentation. Evaluated with underwater images from Yamaguchi Prefecture, our full proposed method (this http URL.+MF) achieved a 0.068 mIoU improvement over USIS-SAM, demonstrating significant accuracy gains, particularly for small seaweed. This approach demonstrates strong potential for improving blue carbon quantification and marine ecosystem monitoring.

---


### 121. [Self-Supervised Dual-Frequency Phase Decomposition for Single-Shot Composite Fringe Projection Profilometry](https://arxiv.org/abs/2606.21027)

**<font color=#1a73e8>作者：</font>** Jin-Hyuk Seok, Yatong An, Jae-Sang Hyun  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-shot fringe projection profilometry (FPP) has been actively studied for real-time measurement, dynamic object reconstruction, and motion-sensitive environments. Composite fringe patterns are advantageous in single-shot FPP because multiple frequency components can be encoded in a single pattern, enabling phase ambiguity resolution. Existing approaches mainly rely on Fourier transform-based methods or supervised deep learning methods. However, Fourier transform-based methods often suffer from limited accuracy and degraded performance in complex regions, while supervised methods require dense phase or depth labels, which are costly to obtain. In this work, we propose a self-supervised phase refinement framework for single-shot composite fringe patterns without requiring phase or depth labels. The proposed method exploits the scale and direction relationships between low- and high-frequency phase gradients, improving the reliability of phase separation. We also introduce a soft edge consistency loss to preserve object boundaries and fine geometric structures. Experimental results show that the proposed method achieves MAE_z and RMSE_z of 0.367 mm and 1.804 mm, respectively, outperforming the best-performing transform-based baseline, which obtains 0.402 mm and 2.785 mm. The proposed method also improves the valid-pixel ratio from 84.75 % to 95.07 %. These results demonstrate the effectiveness of self-supervised dual-frequency phase refinement for reliable single-shot 3D reconstruction without ground-truth label supervision.

---


### 122. [OVIG: Optimistic Verification of AI Training Integrity via Gradient Signals](https://arxiv.org/abs/2606.21045)

**<font color=#1a73e8>作者：</font>** Hongxu Su, Jianzhu Yao, Huan Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid growth of AI has increased the demand for domain-specific post-training, while the cost and specialization of accelerator infrastructure push many model owners to outsource this process. Outsourced training lowers operational barriers, but creates a training-integrity gap: the owner receives a checkpoint, logs, and aggregate metrics without direct evidence that the declared training trajectory was faithfully executed. An untrusted provider may have incentives to deviate from that trajectory, either to save computation or to introduce targeted security risks. Auditing such deviations is difficult because floating-point execution on heterogeneous accelerators introduces benign numerical drift, making it hard to distinguish honest replay differences from integrity violations. Existing verification methods either observe training at too coarse a granularity or impose costs and deployment constraints that are impractical at scale. We present OVIG, an optimistic verification framework that audits outsourced post-training using an empirical boundary on gradient differences calibrated from honest heterogeneous replays. OVIG checks opened intervals against this boundary and combines optimistic sampling with a stride parameter $s$, which partitions training into stride-aligned intervals and retains only interval-endpoint evidence. Across shortcut training attacks and targeted manipulation attacks, OVIG maintains $0\%$ ASR on language, vision, and diffusion workloads. On Qwen3, increasing the stride from $s=1$ to $s=2000$ reduces off-chain storage and evidence transmission by $1996\times$ while preserving $0\%$ ASR; at this setting, OVIG incurs only $1.143\times$ total system overhead relative to training without verification. These results show that OVIG provides a practical integrity layer for outsourced AI post-training under heterogeneous execution.

---


### 123. [A Blockchain Consensus Mechanism for Distributed Electricity Trading](https://arxiv.org/abs/2606.21060)

**<font color=#1a73e8>作者：</font>** Shanglin Yang, Guo Chen, Shiping Chen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Distributed power systems complement centralized grids by coordinating distributed energy resources (DERs) to achieve regional energy self-sufficiency. Scaling such systems raises four persistent challenges: decentralized coordination, fair economic settlement, trustworthy operation, and system optimization, all without a central authority. This paper proposes Proof of Energy (PoE), a blockchain consensus mechanism that addresses these challenges through cryptographically secured, contribution-proportional node selection. In PoE, block generation rights are tied directly to real-world energy contributions, enabling distributed consensus without centralized dispatch. An Energy Contribution Unit (ECU) model is introduced to map heterogeneous energy services onto a unified value metric via scarcity-weighted normalization. A Verifiable Random Function (VRF)-based proposal mechanism then ensures selection probability is strictly proportional to node contribution, preserving fairness and resisting manipulation. Case studies validate PoE across three dimensions: grid coordination, incentive fairness, and optimization efficiency. The result is a cryptographically secured, incentive-compatible framework for decentralized value distribution in energy systems.

---


### 124. [Neural Architecture Distributions: A New Paradigm for Stochastic Segmentation](https://arxiv.org/abs/2606.21061)

**<font color=#1a73e8>作者：</font>** Conghui Li, Junhao Huang, Chern Hong Lim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Stochastic segmentation seeks to represent multiple plausible masks for a single image, which is essential in safety- and quality-critical applications such as medical imaging or building defect inspection. Most existing methods introduce stochasticity by injecting continuous latent variables or by iterative denoising trajectories, whose stochastic sources are difficult to search or audit directly. We propose architecture distributions as a new stochastic source for segmentation: instead of sampling a latent variable or noise, we sample a discrete architecture from a learned distribution over operator choices at multiple searchable positions in a segmentation backbone. Each sampled architecture yields one mask through the selected active path, so inference depends on the executed subnet rather than the complete candidate bank. This approach also supports architectural provenance, since each output corresponds to a specific architecture configuration. To reduce collapse toward averaged masks, we train with set-level supervision by matching a set of architecture-sampled predictions to the annotation set using an IoU-based energy-distance surrogate. We further construct the candidate bank with evolutionary search, making the support of the stochastic source optimizable before distribution learning. The proposed method achieves state-of-the-art distribution matching and hypothesis coverage on LIDC-IDRI, and remains effective on two extension tasks. To the best of our knowledge, this is the first work to formulate stochastic segmentation as learning an architecture distribution and realizing output diversity through architecture sampling.

---


### 125. [Demographic Metadata as Construct-Irrelevant Noise in DistilBERT-Based Automated Essay Scoring](https://arxiv.org/abs/2606.21066)

**<font color=#1a73e8>作者：</font>** Teik Peng Ch'ng, Hui Na Chua  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated Essay Scoring (AES) systems are increasingly used to support teachers in managing grading workloads and to provide a supplementary rater in large-scale assessments. While human grading is frequently influenced by students' demographic characteristics, the efficacy of different strategies for integrating demographic metadata with textual input used to train AES models remains underexplored. This study investigates the impact of a specific multimodal fusion strategy - naive metadata concatenation - on the predictive accuracy, training convergence, and score parity of a DistilBERT-based AES model. A comparative analysis was conducted using the ASAP 2.0 dataset to evaluate a baseline model against an experimental model trained with input that concatenates tokenised text and demographic metadata using a naive multimodal fusion strategy. Evaluated via 10-fold cross-validation, the findings reveal that the early fusion of demographic metadata and the input significantly degrades the model's overall predictive accuracy. The baseline model achieved a Quadratic Weighted Kappa (QWK) of 0.727, which dropped to 0.656 upon integrating metadata. Furthermore, the experimental model exhibited higher validation loss (1.29) compared to the baseline model (1.25). The experimental model also displayed exacerbated scoring bias, reducing score parity instances from 15 to 12 out of 19 tests.

---


### 126. [Snatcher: Apple Find My Network Exposes Your Lost Devices To Strangers](https://arxiv.org/abs/2606.21067)

**<font color=#1a73e8>作者：</font>** Zhenyu Ren, Yanbo Zhang, Boya Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Apple's Find My network connects nearly one billion devices to locate missing property via Bluetooth Low Energy (BLE). This paper reveals that insecure BLE advertisements and design tradeoffs allow unauthorized discovery and physical theft of lost Apple devices. We develop Snatcher, an attack and analysis framework implemented fully on Android smartphones without specialized hardware. Snatcher identifies vulnerabilities in unencrypted BLE advertisements, unauthenticated acoustic triggers, and slow MAC address randomization. Through three levels - sound-based direction finding, RSSI-IMU sensor-fusion navigation, and spatial-temporal clustering - our Android-based platform physically tracks and locates lost Apple accessories and devices in real-world tests. Our results highlight a crucial conflict between privacy protection, anti-stalking design, and physical security, urging Apple to strengthen Find My defenses.

---


### 127. [Quality and Agreement in Multilabel Emotion Annotation: A Case Study and Evaluation Framework](https://arxiv.org/abs/2606.21069)

**<font color=#1a73e8>作者：</font>** Emily Öhman, Anna Koufakou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Emotion annotation is inherently subjective, yet most NLP pipelines still assume "gold" labels, typically produced by majority voting, and treat annotator variation as noise. In this paper, we present a multilabel emotion annotation case study and use it to examine how annotator behavior and aggregation choices affect both agreement estimates and downstream emotion classifiers. Rather than collapsing disagreement into a single label, we represent targets as soft vote-share labels (including an intensity-weighted variant) and evaluate models using both thresholded metrics (macro-/micro-F1) and probabilistic alignment (Bernoulli cross-entropy SoftBCE), alongside data-derived disagreement diagnostics. Across annotation regimes, we show that disagreement is structured and leaves measurable traces in model behavior: hard labels may maximize F1 metrics, while soft supervision yields predictions that better reflect empirical annotator variance and uncertainty. Our results provide practical guidance for designing, aggregating, and evaluating multilabel emotion datasets when multiple interpretations are plausible.

---


### 128. [An Efficient and Effective Architecture for Large-Scale Traffic Prediction via Geometry-Adaptive Square Partitioning](https://arxiv.org/abs/2606.21072)

**<font color=#1a73e8>作者：</font>** Yongfeng Su, Hongwen Li, Zijian Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traffic prediction is a core task in intelligent transportation systems and urban-scale decision making. Despite the effectiveness of mainstream neural-network based methods, their deployment in real-world settings with thousands of traffic sensors is jeopardized severely by their poor computational scalability. To address this, the community has attempted to incorporate spatial database partitioning techniques (e.g., Grid, Quadtree, and K-D Tree) to improve model scalability. However, these approaches rely on handcrafted geometric heuristics and often produce irregular or imbalanced data partitions, leading to boundary fragmentation, excessive padding overheads, and degraded model accuracy. In this paper, we propose SqLinear, an efficient and effective architecture for large-scale traffic prediction. First, we design Square Partition, a geometry-adaptive algorithm that partitions massive traffic sensors into balanced, non-overlapping, and near-square spatial regions. Unlike existing heuristic-based designs, Square Partition is theoretically grounded and provides provable guarantees on aspect ratio, balance, and partition utilization, establishing a high-quality foundation for downstream spatiotemporal modeling. Next, we propose a Hierarchical Linear Interaction (HLI) module that abandons the costly attention mechanisms commonly used in Transformer-based spatio-temporal models. HLI efficiently captures both local intra-region dynamics and global inter-region dependencies through a lightweight linear interaction scheme, enabling effective spatiotemporal modeling with linear computational complexity. Extensive experiments on four large-scale traffic datasets and 10 baselines show that SqLinear reduces MAE by 2.30% on average under standard setting and by 5.81% under extreme scalability settings, while reducing training runtime by 13.27%--30.84% in spatial- and horizon-scaling scenarios.

---


### 129. [OTTER: A Red-Teaming System for Toxicity-Evading Jailbreak Prompt Optimization](https://arxiv.org/abs/2606.21077)

**<font color=#1a73e8>作者：</font>** Jerry Wang, Hsin-Ling Hsu, Yi-Cheng Lai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Production LLMs increasingly rely on toxicity-based moderation filters as a primary defense, assuming that harmful intent correlates with toxic surface wording. We show this assumption is fundamentally brittle: surface toxicity and adversarial intent can be decoupled by replacing as few as five tokens. We present OTTER (Obfuscated Toxicity-Evading Token Evolution for Rewriting), a black-box red-teaming framework requiring only standard API access, directly targeting the practical constraints of industry security audits. Evaluated on 457 AdvBench prompts across four GPT models, OTTER raises average ASR from 7.0% to 84.0%. We further provide the first quantitative analysis of the toxicity--bypass relationship and a per-category breakdown, translating our findings into actionable recommendations for classifier hardening in production deployments.

---


### 130. [Scalable Hierarchical Attention Transformers for Multi-Turn Jailbreak Detection in Long Conversations](https://arxiv.org/abs/2606.21082)

**<font color=#1a73e8>作者：</font>** Chenhui Hu, Muhammed Salih, Sudipto Guha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-turn jailbreaks can evade turn-level moderation by spreading unsafe intent across a dialogue through gradual escalation, reframing, and role manipulation. We address multi-turn jailbreak detection as a conversation-level classification problem and introduce an efficient hierarchical detector that avoids expensive long-context concatenation while retaining cross-turn reasoning. The model encodes individual turns to form compact turn representations and applies a lightweight conversation module that captures dialogue dynamics and selectively attends to fine-grained evidence when needed. On a challenging evaluation benchmark of 14,038 conversations, our approach achieves an F1 of 0.9394, outperforming Claude Opus 4.7, the strongest competing baseline, by 0.07 while halving its false-positive rate. Ablation studies confirm that each architectural component contributes meaningfully, with combining cross-attention and self-attention in the conversation module yielding a 2.26 percentage point reduction in false-positive rate over the self-attention-only variant.

---


### 131. [Sim2O: Efficient Offline-to-Online MARL via Joint Action Composition](https://arxiv.org/abs/2606.21085)

**<font color=#1a73e8>作者：</font>** Bingchang Song, Yiqin Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline-to-online adaptation serves as a pivotal paradigm for mitigating the prohibitive cost of online exploration by bootstrapping reinforcement learning from offline datasets. While this paradigm has been extensively studied in single-agent settings, its extension to Multi-Agent Reinforcement Learning (MARL) remains largely unexplored, despite its critical relevance to complex coordinated decision-making. To bridge this gap, we introduce Sim2O, an elegant and minimalist framework for offline-to-online MARL. Rather than treating adaptation as a monolithic joint decision, Sim2O conceptualizes it as a compositional process. Specifically, candidate joint actions are synthesized by dynamically blending offline and online action proposals across agents. By leveraging a centralized value function to evaluate these hybrid combinations, Sim2O identifies high-value coordination strategies without requiring auxiliary training objectives or structural overhead. Empirical evaluations across diverse benchmarks demonstrate that Sim2O significantly outperforms existing baselines, underscoring that a minimalist design is not only viable but highly effective for multi-agent offline-to-online adaptation.

---


### 132. [BASIL: Bayesian Application for Scientific Iteration and Learning](https://arxiv.org/abs/2606.21092)

**<font color=#1a73e8>作者：</font>** Kelvin P. Idanwekhai, Valeriia Kaneva, Stefano Menegatti 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce BASIL, a user-friendly desktop application for process optimization. BASIL employs a Bayesian approach, incorporating special acquisition functions that can be used to solve both single and multi-objective optimization problems. It provides a graphical interface that enables users to input their experimental parameters, optimization objectives, and legacy data. This is then used to build surrogate models, which are coupled with acquisition functions to guide and optimize a process towards a desired objective. To facilitate model building, BASIL provides a variety of predefined surrogate model templates. BASIL can be used to optimize any arbitrary experiment or process with known, user-defined input variables, optimization objectives, and defined output.

---


### 133. [SLeDGe: Semi-Supervised Learning on Data Streams with Graph Structure Learning](https://arxiv.org/abs/2606.21096)

**<font color=#1a73e8>作者：</font>** Heechan Moon, Kijung Shin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Semi-supervised learning (SSL) on data streams is challenging due to the continuous evolution of high-volume data and the scarcity of labels. Existing methods are limited in leveraging the intrinsic relationships among samples because they typically rely on fixed similarity measures or static graph structures, which cannot capture how relationships evolve over time. We propose SLeDGe, an SSL method for data streams that jointly learns a predictive model and an adaptive graph structure under strict memory and label constraints. SLeDGe maintains compact labeled and unlabeled memories using distinct update strategies, balancing rapid adaptation to novel features with the retention of historical consistency. In addition, by encouraging sparsity in the relational graph, SLeDGe filters out spurious connections and enables effective propagation of label supervision. Across 12 datasets, SLeDGe outperforms state-of-the-art competitors, achieving average relative accuracy gains of 31.7% with 0.1% labels and 14.8% with 1% labels.

---


### 134. [ShuffleFlow: Scalable Posterior Inference for Bayesian Inverse Imaging](https://arxiv.org/abs/2606.21099)

**<font color=#1a73e8>作者：</font>** Tianao Li, Tjitske Starkenburg, Yu Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Variational inference (VI) is a powerful method for principled posterior inference for scientific inverse imaging. VI learns the posterior distribution, often with a flow-based network, which can cheaply generate posterior samples upon optimization, and can flexibly incorporate score-based or classic priors. However, its application to large-scale image reconstruction is severely hindered by the poor scalability of the flow-based networks. In this work, we introduce ShuffleFlow, a scalable VI framework to address this challenge. Our method breaks down the problem into three parts: a pixel-unshuffling-based image coordinate sampler, a neural field as feature encoder, and a conditional normalizing flow (CNF) as posterior estimator. Specifically, our framework partitions an image into a stack of sub-images with pixel-unshuffling and uses a shared CNF to model the joint distribution of the sub-image stack. We condition the CNF on the output of a neural field, which embeds feature vectors corresponding to pixel-unshuffling sample locations to capture spatial structures, and share the flow's latent variable across the channels to model their correlations. We demonstrate our method's effectiveness and efficiency on both linear and nonlinear imaging inverse problems, and show its ability to more rapidly generate a high-sample-count posterior than diffusion samplers.

---


### 135. [Enhancing Differentially Private Mechanisms via Empirical Bayes](https://arxiv.org/abs/2606.21107)

**<font color=#1a73e8>作者：</font>** Minwoo Kim, Junyong Park, Sungkyu Jung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Differential privacy (DP) has become the gold standard for ensuring the privacy protection of machine learning and statistical algorithms in recent decades. A plethora of algorithms and methods have been developed to enhance the utility of DP algorithms while maintaining the same level of DP. However, these are often overly complex or computationally ineffective. We propose a novel approach focusing on denoising the output of the simple additive Gaussian mechanism by adopting the idea of \textit{empirical Bayes estimation}. We highlight that the empirical Bayes approach can reduce the mean-squared error solely by taking the output of the Gaussian mechanism as input. Our numerical studies show that this simple yet powerful approach can be applied to improve upon various statistical problems, including histogram release, principal component analysis, and linear regression, often outperforming existing private algorithms.

---


### 136. [SARIF: Segment Anything for Robust Image Forensics](https://arxiv.org/abs/2606.21108)

**<font color=#1a73e8>作者：</font>** Dong-Hyun Moon, Ju-Hyeon Nam, Sang-Chul Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image forgery localization remains challenging due to diverse manipulation techniques and distribution shifts. Existing forgery localization models achieve high accuracy on benchmarks but often struggle with cross-domain generalization and robustness. In this paper, we propose SARIF (Segment Anything for Robust Image Forensics), a framework that leverages the Segment Anything Model (SAM), which has a promptable architecture and strong generalization ability. SARIF introduces a feedback-guided mask decoder and a dual-encoder design that extracts forgery-specific information to capture forensic traces while exploiting the SAM architecture. To localize manipulated regions, we design a block-wise prompting mechanism that derives forgery-specific cues from residual features between an adapted encoder and its frozen counterpart. These features are fused with the previous mask prompt to drive a feedback-based mask refinement process, enabling automatic forgery segmentation without manual input. Extensive experiments on standard forgery-localization benchmarks show that SARIF achieves strong average cross-dataset performance and robustness to common image corruptions.

---


### 137. [Chem2Gen-Bench: Benchmarking Chemical-to-Genetic Translation in Perturbation Response Space](https://arxiv.org/abs/2606.21109)

**<font color=#1a73e8>作者：</font>** Yuxiang Lin, Ying Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Virtual-cell and perturbation models are increasingly used to predict cellular responses for biomedical discovery, but chemical and genetic perturbations are not automatically interchangeable. Existing evaluations often study chemical response prediction or genetic perturbation prediction separately, leaving target-matched chemical-to-genetic translation under-tested. We introduce Chem2Gen-Bench, a benchmark comprising 260,084 chemical and 1,099,045 genetic perturbation profiles organized into cell-target contexts, and evaluate pairwise alignment, retrieval, protocol covariate associations, feature spaces, and foundation-model embeddings. Across matched contexts, translation fidelity is measurable but heterogeneous; background adjustment increases the association between pairwise similarity and retrieval success, while paired tests show lower mean retrieval success after adjustment under the evaluated settings. In a target-matched K562 audit, the evaluated foundation-model embeddings did not consistently improve over gene-delta baselines. Chem2Gen-Bench provides an auditable framework for testing when chemical and genetic perturbations align around shared targets and when representation gains are supported by matched perturbation evidence.

---


### 138. [Object-Centric Dataset Resources for Constrained-Data Image Generation and Augmentation](https://arxiv.org/abs/2606.21113)

**<font color=#1a73e8>作者：</font>** Vasile Marian, Yong-Bin Kang, Alexander Buddery  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object-centric image generation is important in settings with few labeled examples, including pedestrian analysis in smart-city scenes, traffic-sign inspection, and domain-specific object detection. Synthetic images are most useful for training and evaluation when datasets preserve object structure, bounding boxes, visual diversity, and realistic context. Existing image datasets usually target classification, detection, or scene understanding rather than controlled object-centric generation and augmentation with limited class-specific data. We present a shareable collection of three object-centric dataset resources: Cityscapes-Pedestrian, TrafficSigns, and COCO PottedPlant. The collection standardizes 256-by-256 object-centric crops and bounding-box annotations across three regimes: dense pedestrian scenes with privacy blur and occlusion, cleaner high-contrast traffic signs, and context-diverse potted-plant scenes. The release contains 3,009 TrafficSigns samples, 2,156 Cityscapes-Pedestrian manifest records, and 7,679 COCO PottedPlant manifest records. The larger COCO-derived manifest preserves contextual and multi-instance diversity, while equal-size subsets can be drawn with a fixed random seed for controlled comparisons. The release provides direct TrafficSigns data where redistribution is permitted, together with scripts, manifests, box-level annotation tables, checksums, and reconstruction documentation for the Cityscapes- and COCO-derived subsets. It is available through the Latzi/object-centric-low-data-datasets GitHub repository and Zenodo DOI https://doi.org/10.5281/zenodo.20573001. The collection supports label and split inspection, subset creation, reconstruction from upstream data, and evaluation of object-centric image generation or synthetic-data augmentation methods on shared records.

---


### 139. [MS-rPPG: Multi-spectral State Space Model for Remote Photoplethysmography in Driver Monitoring Systems](https://arxiv.org/abs/2606.21115)

**<font color=#1a73e8>作者：</font>** Jiho Choi, Sang Jun Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote photoplethysmography (rPPG) is a camera-based technique for measuring physiological signals, particularly cardiac activity. From the remotely measured signals, heart rate can be estimated, which is crucial for health monitoring. In this study, we investigate a driver health monitoring system based on remote heart rate estimation. However, driving environments represent uncontrolled settings where videos are subject to varying illumination conditions and frequent head movements. We introduce MS-rPPG, a multi-spectral framework that combines RGB with near-infrared (NIR) face video to alleviate rPPG estimation under challenging driving conditions. To combine the complementary features from two spectral videos, we propose a cross-spectral linear modulation (CSLM) strategy based on frequency-domain analysis. Moreover, we introduce MS-Mamba, a novel state space model designed to effectively model long-range temporal dependencies while jointly capturing cross-channel interactions between multi-spectral features. We collected a real-world dataset called MS-Drive, which was recorded from 50 participants while driving the vehicle. The proposed method was evaluated on the MR-NIRP Car dataset and MS-Drive datasets. The experimental results indicate that MS-rPPG shows better robustness and heart rate estimation accuracy than previous methods, highlighting its promise for driver health monitoring. The codes are available at this http URL.

---


### 140. [ConnectomeBench2: A Unified Benchmark for Automated Connectomic Proofreading](https://arxiv.org/abs/2606.21116)

**<font color=#1a73e8>作者：</font>** Jeff Brown, Tim Farkas, Gleb Razgar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Proofreading--correcting segmentation errors in 3D brain reconstructions--is the rate-limiting step in synapse-resolution connectomics. We release ConnectomeBench2, a unified multi-species dataset of over 716,485 expert-labeled proofreading decisions with >4,500,000 associated images spanning four major open connectomes (mouse, human, zebrafish, fly), spanning both split and merge error correction. Trained on this dataset, a single Vision Transformer with shared encoders for mesh geometry and electron microscopy reaches human-level accuracy across species for split error correction and merge error identification, with performance scaling with data size and modality. Beyond accuracy, we show that the model is well-calibrated within distribution, that measures of distribution distance predict where calibration and accuracy will degrade on unseen data, and that connectomics-specific pretraining and active learning-based sample selection show potential to substantially reduce the labeling effort needed to extend to new species and brain regions. The benchmark provides the infrastructure to train and evaluate increasingly capable vision models for connectomic proofreading.
Data and code availability. The ConnectomeBench2 dataset is released on Hugging Face at this https URL. The accompanying codebase is available on GitHub at this https URL.

---


### 141. [PulseCX: Breaking the Closed-World Assumption in Real-Time CX](https://arxiv.org/abs/2606.21124)

**<font color=#1a73e8>作者：</font>** Rajat Agarwal, Suvidha Tripathi, Shubham Sharma  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conversational AI agents in Customer Experience (CX) typically suffer from a Closed-World Constraint, ignoring high-velocity external shifts like viral trends or outages. Ad-hoc web search attempts to bridge this gap but often introduce prohibitive latency and context poisoning. We introduce PulseCX, a framework that decouples knowledge acquisition from consumption. Adopting a structure-first paradigm, PulseCX employs an asynchronous agent to linearize signals into a Decay-Aware Temporal Knowledge Graph (DA-TKG) governed by reinforcement--decay dynamics to actively manage information lifecycles. By coupling this self-evolving memory with hierarchical intent gating, PulseCX removes synchronous search bottlenecks (<10ms overhead) and drives significant gains in Intent Resolution (IRR) and Customer Satisfaction (s-CSAT) in dynamic environments.

---


### 142. [Learning Burst-Aware Early Warning Models for Capacity Stress under AI Workload Surges in Hyperscale Data Centers](https://arxiv.org/abs/2606.21130)

**<font color=#1a73e8>作者：</font>** Zihan Yu, Xianling Zeng, Zhiming Xue 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid growth of large-scale AI workloads, particularly Large Language Model (LLM) training and inference, is fundamentally reshaping the operational dynamics of hyperscale data centers. Unlike traditional cloud workloads, AI-driven jobs exhibit bursty, high-intensity, and rapidly shifting resource demands, often leading to sudden capacity stress that cannot be effectively handled by reactive threshold-based mechanisms. In this paper, we propose a deployment-oriented, burst-aware early warning framework for proactive capacity stress prediction under AI workload surges. We formulate the problem as a high-recall forecasting task over multivariate telemetry windows, with the explicit goal of enabling operational intervention before system degradation occurs. The proposed framework integrates workload intensity, temporal variation, and system pressure signals, and employs a lightweight tree-based learning model to capture nonlinear interactions in highly imbalanced environments. To evaluate the system under realistic conditions, we introduce an AI workload surge injection methodology that simulates burst-driven demand patterns observed in large-scale AI systems. Our XGBoost-based model achieves an ROC AUC of 0.697 and an AP of 0.670, significantly outperforming baseline methods. Under deployment-oriented threshold selection, the framework achieves a Recall of 0.914, enabling the detection of the majority of stress-prone periods with acceptable false-alarm cost. Beyond predictive performance, we show how the proposed framework can be integrated into operational control loops to support proactive actions such as workload throttling and resource scaling. Our results highlight the practical value of high-recall, learning-based early warning systems in enabling resilient and adaptive data center operations in the era of AI-driven workloads.

---


### 143. [Horizon Adaptive Offline Policy Learning via Value Stitching](https://arxiv.org/abs/2606.21136)

**<font color=#1a73e8>作者：</font>** Kexin Zheng, Xianyuan Zhan, Xintao Yan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning accurate value functions plays a decisive role for reinforcement learning (RL) agents to solve long-horizon, complex tasks. Conventional temporal-difference (TD) learning objectives suffer from value-estimation bias that accumulates over the horizon, while extended-horizon modeling methods, such as n-step TD backups and Q-chunking, adopt a rigid, fixed-horizon value-modeling recipe that is often not flexible enough to capture complex value structures in long-horizon, multi-stage tasks. In this paper, we show that enabling value updates with dynamic horizon composition can yield a strong offline policy learning scheme. Our method, Horizon Adaptive Offline Policy Learning via VAlue STitching (VAST), replaces fixed-horizon backups with recursive, horizon-adaptive value composition. Its key ingredient is to couple value optimization with a future state- and horizon-length-conditioned auxiliary value function that is learned through direct data supervision, and a stitching policy that optimally selects the reward-maximizing horizon length and future sub-goal to achieve horizon-adaptive value stitching. This design enables direct estimation and compositional "stitching" of variable-length returns grounded in actionable sub-goal states, providing an accurate and greedily exploitable value-supervision signal for offline policy optimization. Across 50 tasks on OGBench, VAST outperforms fixed-step, extended-horizon methods, and generative-value offline RL baselines, achieving strong performance particularly in high-complexity, long-horizon decision-making tasks.

---


### 144. [SEED: Simple ViT and Evolving Harness for Explainable Text Forgery Detection](https://arxiv.org/abs/2606.21138)

**<font color=#1a73e8>作者：</font>** Kahim Wong, Kemou Li, Yiming Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-assisted image editing threatens trust in financial, legal, and identity records. The GenText-Forensics Challenge at ACM MM 2026 addresses this by requiring structured forensic reports, in which integrating detection, pixel-level localization, and natural language explanation for multilingual text-centric forgery images. We present SEED, a modular system with three components. First, a similarity-guided pipeline augments training with diverse synthetic forgeries. Second, a single ViT, built on DINOv3 with LoRA adaptation, jointly performs detection and pixel-level localization while preserving pre-trained priors with minimal trainable parameters. Third, an evolving harness takes the detector's predictions and generates a complete forensic report via an MLLM, iteratively improved through a proposer-evaluator loop optimizing report quality. SEED ranked 3rd in the GenText-Forensics Challenge. Code and data are available at this https URL.

---


### 145. [ChronoLock: Protecting Videos from Unauthorized Text-to-Video Personalization](https://arxiv.org/abs/2606.21146)

**<font color=#1a73e8>作者：</font>** Jiaming He, Jiashu Zhang, Guanyu Hou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-video (T2V) diffusion models have made it increasingly easy to synthesize realistic and temporally coherent videos, while recent personalization techniques allow such models to imitate a specific subject, style, or motion pattern from only a few reference clips. This capability creates a new data-misuse risk: videos shared online can be collected and used for unauthorized T2V fine-tuning. Existing protective perturbations are mainly designed for image recognition or text-to-image personalization, and therefore focus on corrupting static appearance cues rather than the temporal denoising dynamics that make video personalization possible. To address this gap, we introduce ChronoLock, the first proactive protection framework that makes released videos difficult to exploit for unauthorized T2V personalization. ChronoLock targets the motion-learning process directly by optimizing bounded perturbations over temporal denoising trajectories. It first disrupts intra-chunk temporal adaptation with a diffusion objective that combines fitting error, frame-relative denoising relations, and adjacent-frame variation, and then enlarges inter-chunk boundary mismatch to weaken long-range motion continuity. Transformation-sampled updates further improve robustness to common preprocessing this http URL on UCF Sports and HMDB51 with popular T2V backbones and personalization scheme show that ChronoLock effectively reduces motion imitation under automatic metrics and human evaluation.

---


### 146. [Who Checks the Citations? Benchmarking Legal Hallucination Detection](https://arxiv.org/abs/2606.21155)

**<font color=#1a73e8>作者：</font>** Patty Liu, Dominik Stammbach, Peter Henderson  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Attorneys, judges, and pro se filers increasingly use AI to draft legal documents, yet these tools frequently fabricate citations. Despite predictions that newer models would hallucinate less or that court sanctions would deter negligent filers, we found over 1,000 filings containing fabricated citations -- with this number growing year-over-year. This study evaluates whether AI-based systems can mitigate these errors by automatically detecting hallucinations. We propose a taxonomy of legal citation hallucinations grounded in actual court filings and introduce a dataset of 1,300 brief excerpts containing injected errors. Benchmarking five models in agentic and non-agentic settings reveals that while the latest iterations perform better -- GPT-5 achieves 82.8% recall and a 60.5% F1 score in an agentic framework -- all models struggle with subtle error categories. Agentic verification remains resource-intensive, with GPT-5 averaging 16.9 steps per excerpt. Furthermore, restricted information access limits the efficacy of even the best agents. This gap creates policy concerns, as it disadvantages both AI systems and litigants who lack subscriptions to commercial legal databases. Together, our dataset, tools, and policy recommendations provide a foundation for building and auditing reliable legal citation checking tools.

---


### 147. [Contrastive and Adaptive Multi-modal Masked Autoencoder for Spatial Transcriptomics](https://arxiv.org/abs/2606.21156)

**<font color=#1a73e8>作者：</font>** Joohyeok Kim, Taejin Jeong, Jinyeong Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The high cost of spatial transcriptomics (ST) has driven extensive studies into predicting gene expression directly from H&E histology images. However, this prediction task faces an inherent limitation, as tissue morphology alone provides insufficient information to fully resolve underlying gene expression. To address this limitation, a recent study leverages partial gene expression to guide the prediction process alongside histology images. Building on this paradigm, we approach the prediction task as a spatial imputation problem, employing a Masked Autoencoder (MAE) to utilize a small fraction of gene expression as genetic anchors for inferring whole-slide gene expression profiles. Specifically, we propose a bio-saliency score and a learning-to-rank strategy to adaptively identify the most informative spots within the tissue. Based on these identified spots, our framework selects contiguous regions as genetic anchors to ensure suitability for real-world ST profiling hardware. To effectively leverage these anchors, we design a cross-modal joint encoder that integrates visual and genetic modalities. By aligning the selected anchors with their corresponding visual features via contrastive learning, the encoder generates robust joint representations to accurately predict gene expression across the whole slide. Notably, our framework consistently surpasses existing methods in both histology-only prediction and spatial imputation, achieving superior accuracy even without genetic anchors and further excelling with as little as 10% transcriptomic coverage. Our code is available at this https URL.

---


### 148. [Dead-Direction Signatures: A Cheap Spectral Reading of Singular Complexity](https://arxiv.org/abs/2606.21158)

**<font color=#1a73e8>作者：</font>** Tejas Pradeep Shirodkar, P. J. Narayanan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Singular learning theory characterises the complexity of a deep network through the geometry of its loss singularities. The local learning coefficient (LLC), the standard estimator of Watanabe's real log canonical threshold (RLCT, $\lambda$), reads this geometry as an integrated Bayesian scalar through SGLD, which needs per-task calibration and $10^4$-$10^6$ forward-backward passes per checkpoint. We introduce Dead-Direction Signatures (DDS), a family of cheap closed-form spectral readings of singular structure: each reads a network's activation matrix or per-sample-gradient Fisher-Gram at a chosen layer, replacing the SGLD posterior chain with spectral linear algebra. The readings rest on a dead-direction framework that predicts a structural correlation between activation- and Fisher-side spectra at any singular minimum, and a rank-multiplicative volume identity that single-eigenvalue monitors cannot produce: the active-volume $\log\det^{+}(G)$ slope counts the dead directions, tracking the rank-deficit $r$ across $r \in \{1,2,3,4\}$ (slope ratios $2.0, 3.1, 4.0$ at $r{=}2,3,4$ against the predicted $2,3,4$), where the smallest eigenvalue is rank-blind. On reduced-rank regression with closed-form $\lambda$, calibrated LLC recovers $\lambda$ at $99\%$ mean and the DDS observables rank-track it at the framework-predicted sign; on a non-linear modular-addition transformer DDS separates $d_{\mathrm{model}}$ across eighteen orders of magnitude where calibrated LLC at the protocol budget is rank-flat. Complementary to LLC's integrated posterior reading, DDS gives a directional, layer-local handle on a network's dead directions, read in closed form from its activation and gradient spectra.

---


### 149. [Trip+: Benchmarking Agents in Personalized Interactive Travel Planning](https://arxiv.org/abs/2606.21169)

**<font color=#1a73e8>作者：</font>** Junle Chen, Wei Chen, Yehong Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interactive travel planning has become a popular use case for language models. Agents are deployed to manage evolving preferences and unexpected disruptions over multiple turns. Such settings require models to make complex, profile-conditioned planning decisions. However, existing benchmarks often evaluate feasibility, personalization, or interaction in relatively isolated settings. We therefore introduce Trip+ to measure the ability of agents to plan travel holistically. In Trip+, given traveler profiles and dynamic interactions, agents must generate and revise minute-level itineraries. End-to-end traveler experiences are evaluated via an LLM-based simulator, enabling the assessment of subjective metrics like fatigue. Our scenarios range from simple request resolutions to complex environment-driven replanning. We evaluate 18 LMs and find a consistent gap in experiential quality. Models favor technically feasible but exhausting itineraries that diverge sharply from profiled traveler preferences.

---


### 150. [HERO: Hypothesis-Driven Evidence Retrieval from Omics for Multi-Task Breast Cancer Analysis](https://arxiv.org/abs/2606.21174)

**<font color=#1a73e8>作者：</font>** Xiangyu Li, Ran Su  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Matched multi-omics can improve WSI-based biomarker and prognosis prediction, but most existing pipelines use omics as a paral lel feature stream or textual context rather than as an explicit retrieval constraint. HERO asks whether observed omics can be a testable mor phology hypothesis: a sparse pathway-to-morphology prior maps DNA methylation and miRNA into a K-dimensional intent vector m (K=16), TF-IDF retrieval over structured 10 captions selects endpoint-relevant regions, and a cosine gate c=cos(m,v) triggers deterministic deficit driven repair when c<{\tau}c. This closed-loop design bounds VLM calls, reduces reliance on embedding-based semantic matching, and makes every retrieval and verification step lexically auditable. On TCGA-BRCA (930WSIs, patient-level 5-fold CV), HERO sets new state-of-the-art across ER, PR, HER2, subtype, and risk prediction, outperforming both multimodal fusion and VLM-based baselines.

---


> [!TIP]
> 当前位于：**101-150**（第 3/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-654](./part-14.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
