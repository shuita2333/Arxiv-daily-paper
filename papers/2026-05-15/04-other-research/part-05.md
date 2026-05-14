# 📦 其他研究 | 2026年05月15日

> 本类共 **328** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-328](./part-07.md)

---

### 201. [Achieving Gold-Medal-Level Olympiad Reasoning via Simple and Unified Scaling](https://arxiv.org/abs/2605.13301)

**<font color=#1a73e8>作者：</font>** Yafu Li, Runzhe Zhan, Haoran Zhang 等 28 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent progress in reasoning models has substantially advanced long-horizon mathematical and scientific problem solving, with several systems now reaching gold-medal-level performance on International Mathematical Olympiad (IMO) and International Physics Olympiad (IPhO) problems. In this paper, we introduce a simple and unified recipe for converting a post-trained reasoning backbone into a rigorous olympiad-level solver. The recipe first uses a reverse-perplexity curriculum for SFT to instill rigorous proof-search and self-checking behaviors, then scales these behaviors through a two-stage RL pipeline that progresses from RL with verifiable rewards to more delicate proof-level RL, and finally boosts solving performance with test-time scaling. Applying this recipe, we train a 30B-A3B backbone with SFT on around 340K sub-8K-token trajectories followed by 200 RL steps. The resulting model, SU-01, supports stable reasoning on difficult problems with trajectories exceeding 100K tokens, while achieving gold-medal-level performance on mathematical and physical olympiad competitions, including IMO 2025/USAMO 2026 and IPhO 2024/2025. It also demonstrates strong generalization of scientific reasoning to domains beyond mathematics and physics.

---


### 202. [Safe Bayesian Optimization for Uncertain Correlations Matrices in Linear Models of Co-Regionalization](https://arxiv.org/abs/2605.13302)

**<font color=#1a73e8>作者：</font>** Jannis Lübsen, Annika Eichler  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper extends safety guarantees for multi-task Bayesian optimization with uncertain correlation matrices from intrinsic co-reginalization models to linear models of co-reginalization. The latter allows for more flexible modeling of the inter-task correlations by composing multiple features. We derive uniform error bounds for vector-valued functions sampled from a Gaussian process with a linear model of co-reginalization kernel. Furthermore, we show the potential improvement of performance using linear models of co-reginalization in a numerical comparison on a safe multi-task Bayesian optimization benchmark.

---


### 203. [MPINeuralODE: Multiple-Initial-Condition Physics-Informed Neural ODEs for Globally Consistent Dynamical System Learning](https://arxiv.org/abs/2605.13305)

**<font color=#1a73e8>作者：</font>** Lake Yang, Antonio Malpica-Morales, Frank Ioannis Papadakis Wood 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural ordinary differential equations (Neural ODEs) often fit training trajectories while generalizing poorly to unseen initial conditions and long horizons. We propose MPINeuralODE, which combines a soft physics-informed residual with a Multiple-Initial-Condition (MIC) multiple-shooting curriculum whose ingredients are structurally complementary: the physics term anchors the vector-field magnitude on the support that MIC enlarges. We evaluate along three axes: out-of-sample error, long-horizon stability, and Hamiltonian drift, which together expose whether the learned dynamics recover the underlying vector field. On Lotka-Volterra, MPINeuralODE achieves the lowest out-of-sample and long-horizon MSE among data-driven methods, with a 26% reduction over the baseline Neural ODE, while essentially matching the PINN ablation on Hamiltonian drift.

---


### 204. [Color Constancy in Hyperspectral Imaging via Reduced Spectral Spaces](https://arxiv.org/abs/2605.13306)

**<font color=#1a73e8>作者：</font>** G. Dofri Vidarsson, Liying Lu, Sabine Süsstrunk  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Illuminant estimation aims to infer scene illumination from image measurements despite intrinsic ambiguities between surface reflectance and lighting. Most existing methods operate on trichromatic RGB images and are therefore fundamentally limited by the restricted spectral information available. Hyperspectral imaging provides a much richer representation of scene radiance and has the potential to alleviate these ambiguities. However, its high dimensionality poses computational and statistical challenges. In this work, we systematically study the effect of spectral dimensionality and representation choice on illuminant estimation performance using hyperspectral data. We adopt the practical and effective Color-by-Correlation (CbC) framework as the estimation backbone and analyze its behavior under different spectral dimensionality reduction strategies. Our results offer practical insights into how hyperspectral information can be efficiently exploited for illuminant estimation and identify conditions under which compact spectral representations outperform conventional RGB-based approaches. The code is available at this https URL.

---


### 205. [IdeaForge: A Knowledge Graph-Grounded Multi-Agent Framework for Cross-Methodology Innovation Analysis and Patent Claim Generation](https://arxiv.org/abs/2605.13311)

**<font color=#1a73e8>作者：</font>** Joy Bose  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current AI-assisted innovation systems typically apply a single ideation methodology (such as TRIZ or Design Thinking) using sequential prompt-based workflows that do not preserve intermediate reasoning structure. As a result, insights generated across methodologies remain fragmented, limiting traceability, synthesis, and systematic evaluation of novelty. We present IdeaForge, a knowledge graph-grounded multi-agent framework for innovation analysis and patent claim generation. IdeaForge integrates multiple innovation methodologies (TRIZ, Design Thinking, and SCAMPER) through specialist agents operating over a persistent FalkorDB knowledge graph. Each agent contributes structured entities and relationships representing contradictions, inventive principles, user needs, transformations, analogies, and candidate claims. The central contribution of IdeaForge is a cross-methodology convergence mechanism implemented through graph-based claim linkage. Claims independently supported by multiple methodologies are connected using CONVERGENT relationships, enabling identification of high-confidence innovation candidates through graph traversal. A downstream patent drafting agent generates structured patent drafts grounded in convergent claim subgraphs, reducing reliance on unconstrained language model generation. An InnovationScore formula ranks claims by convergent support, methodology diversity, claim strength, and prior art challenge count. We describe the graph schema, agent architecture, convergence detection pipeline, and patent synthesis workflow. Experiments on a legal technology use case demonstrate that graph-grounded multi-methodology synthesis produces more diverse and traceable innovation candidates compared to single-methodology baselines. We discuss implications for computational creativity, explainable AI-assisted invention, and graph-native innovation systems.

---


### 206. [Test-time Sparsity for Extreme Fast Action Diffusion](https://arxiv.org/abs/2605.13316)

**<font color=#1a73e8>作者：</font>** Kangye Ji, Yuan Meng, Jianbo Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Action diffusion excels at high-fidelity action generation but incurs heavy computational costs owing to its iterative denoising nature. Despite current technologies showing promise in accelerating diffusion transformers by reusing the cached features, they struggle to adapt to policy dynamics arising from diverse perceptions and multi-round rollout iterations in open environments. We propose test-time sparsity to tackle this challenge, which aims to accelerate action diffusion by dynamically predicting prunable residual computations for each model forward at test time. However, two bottlenecks remain in this paradigm: 1) repetitive conditional encoding and pruning offset most potential speed gains, and 2) the features cached from previous denoising timesteps cannot constrain large pruning errors under aggressive sparsity. To address the first bottleneck, we design a highly parallelized inference pipeline that minimizes the non-decoder delay to milliseconds. Specifically, we first design a lightweight pruner that shares the encoder with the diffusion transformer. Then, we decouple the encoding and pruning from the autoregressive denoising loop by processing all denoising timesteps in parallel, and overlap the pruner with the decoder forward inference through asynchronism. To overcome the second bottleneck, we introduce an omnidirectional reusing strategy, which achieves 95% sparsity by selectively reusing features cached from the current forward, previous denoising timesteps, and earlier rollout iterations. To learn the rollout-level reusing strategies, we sample a few action trajectories to supervise the sparsified diffusion step by step. Extensive experiments demonstrate that our method reduces FLOPs by 92% and accelerates action generation by 5x, achieving lossless performance with an inference frequency of 47.5 Hz. Our code is available at this https URL.

---


### 207. [VERA-MH: Validation of Ethical and Responsible AI in Mental Health](https://arxiv.org/abs/2605.13318)

**<font color=#1a73e8>作者：</font>** Luca Belli, Kate H. Bentley, Josh Gieringer 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chatbot usage has increased, including in fields for which they were never developed for--notably mental health support. To that end, we introduce Validations of Ethical and Responsible AI in Mental Health (VERA-MH), a novel clinically-validated evaluation for safety of chatbots in the context of mental health support. The first iteration of VERA-MH focuses on Suicidal Ideation (SI) risks, by assessing how well chatbots can responds to users that might be in crisis.
VERA-MH is comprised of three steps: conversation simulation, conversation judging and model rating. First, to simulate conversations with the chatbot under evaluation, another chatbot is tasked with role-playing users based on specific personas. Such user personas have been developed under clinical guidance, to make sure that, among others, multiple risk factors, demographic characteristics and disclosure factors were represented. In the judging step, a second support model is used as an LLM-as-a-Judge, together with a clinically-developed rubric. The rubric is structured as a flow, with a single Yes/No question asked each time, to improve answers' consistency and highlight models' failure modes. In the last stage, results of each conversation are aggregated to present the final evaluation of the chatbot. Together with the framework, we present the result of the evaluations for four leading LLM providers.

---


### 208. [Diversity of Extensions in Abstract Argumentation](https://arxiv.org/abs/2605.13332)

**<font color=#1a73e8>作者：</font>** Johannes K. Fichte, Markus Hecher, Yasir Mahmood 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Argumentation is an important topic of AI for modelling and reasoning about arguments. In abstract argumentation, we consider directed graphs, so-called argumentation frameworks (AF), that express conflicts between arguments. The semantics is defined by the notion of extensions, which are sets of arguments that satisfy particular relationship conditions in the AF. Usually, standard reasoning in argumentation do not reveal how far apart extensions are. We introduce a quantitative notion of diversity of extensions based on the symmetric difference and provide a systematic complexity classification. Intuitively, diversity captures whether extensions of a framework (accepted viewpoints) differ only marginally or represent fundamentally incompatible sets of arguments. We study whether an AF admits k-diverse extensions, admits k-diverse extensions covering specific arguments, and to compute the largest k for which an AF admits k-diverse extensions. We outline a prototype and provide an evaluation for computing diversity levels.

---


### 209. [Stylized Text-to-Motion Generation via Hypernetwork-Driven Low-Rank Adaptation](https://arxiv.org/abs/2605.13333)

**<font color=#1a73e8>作者：</font>** Junhyuk Jeon, Seokhyeon Hong, Junyong Noh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-driven motion diffusion models are capable of generating realistic human motions, but text alone often struggles to express fine-level nuances of motion, commonly referred to as style. Recent approaches have tackled this challenge by attaching a style injection mechanism to a pretrained text-driven diffusion model. Existing stylization methods, however, either require style-specific fine-tuning of existing models or rely on heavy ControlNet-based architectures, limiting efficiency and generalization to unseen styles. We propose a lightweight style conditioning framework that dynamically modulates a pretrained diffusion model through hypernetwork-generated LoRA parameters. A style reference motion is encoded into a global style embedding, which is mapped by a hypernetwork to low-rank updates applied at each denoising step of the diffusion model. By structuring the style latent space with a supervised contrastive loss, our framework reliably captures diverse stylistic attributes, improves generalization to unseen styles, and supports optimization-based guidance without requiring predefined style categories. Experiments on the HumanML3D and 100STYLE datasets show state-of-the-art stylization results, while achieving improved stylization for unseen styles.

---


### 210. [Ego2World: Compiling Egocentric Cooking Videos into Executable Worlds for Belief-State Planning](https://arxiv.org/abs/2605.13335)

**<font color=#1a73e8>作者：</font>** Qinchuan Cheng, Zhantao Gong, Pengzhan Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Embodied agents in household environments must plan under partial observation: they need to remember objects, track state changes, and recover when actions fail. Existing benchmarks only partially test this ability. Egocentric video datasets capture realistic human activities but remain passive, while interactive simulators support execution but rely on synthetic scenes and hand-crafted dynamics, introducing a sim-to-real gap and often assuming fully observable state. We introduce Ego2World, an executable benchmark that turns egocentric cooking videos into executable symbolic worlds governed by graph-transition rules. Built on HD-EPIC, Ego2World derives reusable transition rules from video annotations and executes them in a hidden symbolic world graph. During evaluation, the simulator maintains the hidden world graph, while the agent plans over its own partial belief graph using only local observations and execution feedback. This separation forces agents to update memory and replan without observing the true world state. Experiments show that action-overlap scores overestimate physical-state success, and that persistent belief memory improves task completion while reducing repeated visual exploration -- suggesting that belief maintenance should be a first-class target of embodied-agent evaluation.

---


### 211. [Context-Aware Web Attack Detection in Open-Source SIEM Systems via MITRE ATT&CK-Enriched Behavioral Profiling](https://arxiv.org/abs/2605.13337)

**<font color=#1a73e8>作者：</font>** Badr Alboushy, Assef Jafar, Mohamad Aljnidi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security Information and Event Management (SIEM) systems aggregate log data from heterogeneous sources to detect coordinated attacks. Traditional rule-based correlation engines struggle to classify multi-step web application attacks because they examine each event without reference to the behavioural history of the originating host.
We present Smart-SIEM, an AI module for the open-source Wazuh SIEM platform with two contributions: (1) a per-source-IP behavioural context vector encoding HTTP response-status distributions, peak rule activation counts, and MITRE ATT&CK technique frequencies from the N most recent prior events; (2) a two-stage hybrid cascade combining LightGBM for binary attack detection and XGBoost for six-class attack categorisation.
Evaluated on 46,454 purpose-built Wazuh security events, context features improve all tested gradient boosting algorithms from ~0.705 macro F1 to 0.947-0.967 (Stage 1) and 0.876-0.914 (Stage 2), an average gain of +0.254 and +0.324 respectively. The hybrid cascade achieves F1 of 0.967 (binary) and 0.914 (six-class). Wazuh's native rule engine detects 0% of Brute Force and Broken Authentication events; the AI module detects 100% and 98.3% respectively. A self-adaptive retraining mechanism recovers from concept drift: F1 drops from 0.905 to 0.465 when unseen attack types emerge, recovering to 0.814 after retraining on the combined corpus.

---


### 212. [Shortcut Mitigation via Spurious-Positive Samples](https://arxiv.org/abs/2605.13340)

**<font color=#1a73e8>作者：</font>** Phuong Quynh Le, Jörg Schlötterer, Sari Sadiya 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Shortcut mitigation strategies commonly rely on training data annotations, group-balanced held-out data or the presence of all groups, i.e., all combinations of (spurious) attributes and classes, in the training data. However, these requirements are rarely met in practice. We instead propose a method for targeted model analysis to identify a small set of instances in which the model relies on spurious attributes. Using that set and following ``this feature should not be used for prediction'' reasoning, we identify highly relevant neurons in an intermediate layer and regularize their impact. This ensures that models learn to depend on informative features rather than being right for the wrong reasons, thereby improving robustness without requiring additional balanced held-out data or annotations.

---


### 213. [Multi-Agent Systems in Emergency Departments: Validation Study on a ED Digital Twin](https://arxiv.org/abs/2605.13345)

**<font color=#1a73e8>作者：</font>** Markus Wenzel, Tobias Strapatsas, Jessika Kress 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Emergency departments (ED) face challenges in patient care and resource management. We propose to explore optimization strategies in a realistic and flexible model and develop a hybrid Discrete Event Simulation (DES) and Agent-Based Model (ABM) simulating highly configurable ED environments. We specifically focus on the validation of the modeling approach. We derive configurations for ED sizes, patient load, and staffing from real-world studies. We then validate the model expressivity by matching its key performance indicators and metrics with their values known from literature. We proceed by implementing scientifically established and practice-proven resource optimization strategies. Comparing the documented real-world outcomes with our model's results demonstrates that the DES-ABM based simulation can effectively replicate real-world ER dynamics under interventions. We lastly integrate a Proof-of-Concept multi-agent system (MAS) that can autonomously explore resource allocation strategies within the simulated ER environment based on a temporal ledger of ED event records. This modular DES-ABM-MAS framework offers a powerful tool to explore resource optimization strategies in emergency departments.

---


### 214. [Contextual Bandits for Resource-Constrained Devices using Probabilistic Learning](https://arxiv.org/abs/2605.13346)

**<font color=#1a73e8>作者：</font>** Marco Angioli, Kevin Johansson, Antonello Rosato 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contextual bandits (CB) are online sequential decision-making problems under partial feedback that underpin many adaptive services. There is a growing demand to deploy CB agents directly on-device, under strict constraints on memory, compute, and energy. However, standard linear CB algorithms are often impractical for resource-constrained devices with their unfavorable scaling in computational and memory costs. Recently, HD-CB, a CB approach based on hyperdimensional computing principles, has been proposed to model and solve CB problems by moving into high-dimensional spaces. HD-CB offers faster convergence, favorable scalability, and improves memory efficiency compared to linear CB algorithms. However, its learning rule is accumulation-based: the values of action vectors grow over time, requiring high precision. While periodic binarization can prevent overflow in low-precision components, it may discard important information about magnitudes and degrade decision quality. This paper introduces probabilistic HD-CB, a low-precision variant that replaces deterministic accumulation with a probabilistic update rule. At each step, only a random subset of vector components is updated, with a time-decaying update probability, and component values are constrained to a predefined range [-k,+k]. This approach enables low-precision components, prevents overflow without periodic binarization, and reduces the expected update cost in proportion to the fraction of updated components. Off-policy evaluation on standardized synthetic CB benchmarks using the Open Bandit Pipeline shows that probabilistic HD-CB consistently outperforms binarized HD-CB at equal precision, while approaching the performance of HD-CB with as few as 3 bits per component.

---


### 215. [GeoFlowVLM: Geometry-Aware Joint Uncertainty for Frozen Vision-Language Embedding](https://arxiv.org/abs/2605.13352)

**<font color=#1a73e8>作者：</font>** Mayank Nautiyal, Li Ju, Andreas Hellander 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard dual-encoder vision-language models that map images and text to deterministic points on a shared unit hypersphere through $\ell_2$ normalization typically expose neither \emph{aleatoric} uncertainty (cross-modal ambiguity) nor \emph{epistemic} uncertainty (lack of training-distribution support). Existing post-hoc methods either recover at most one of the two uncertainty components, or ignore the hyperspherical geometry of these models' embeddings. We propose \textbf{GeoFlowVLM} as a post-hoc adapter that learns the joint distribution of paired $\ell_2$-normalised dual-encoder VLM embeddings on the product hypersphere $\mathbb{S}^{d-1} \times \mathbb{S}^{d-1}$ via Riemannian flow matching with a single masked velocity field. A consistency result shows that, in the population limit, the trained network exposes the joint flow and both cross-modal conditional flows as valid Riemannian flow-matching velocity fields on their respective domains. We derive two quantities from this single model: a conditional retrieval entropy that quantifies aleatoric ambiguity with a decision-theoretic interpretation via a Fano-type bound, and a marginal-typicality epistemic score justified by an exact chain-rule decomposition of the joint NLL. This decomposition isolates a cross-modal pointwise-mutual-information term that is structurally discriminative rather than epistemic, and is empirically the only consistently uninformative standalone component. Empirically, the entropy tracks Recall@1 with near-ideal monotonic calibration across three retrieval benchmarks in both directions, and the marginal-typicality sum yields consistently calibrated selective accuracy across four zero-shot classification benchmarks.

---


### 216. [Constitutional Governance in Metric Spaces](https://arxiv.org/abs/2605.13362)

**<font color=#1a73e8>作者：</font>** Ehud Shapiro, Nimrod Talmon  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Computational social choice and algorithmic decision theory offer rich aggregation theory but no end-to-end, polynomial-time process for egalitarian self-governance: prior work treats aggregation, deliberation, amendment, and consensus in isolation, and key metric-space aggregators are NP-hard. We propose constitutional governance in metric spaces, integrating these stages into one polynomial-time process. The constitution assigns, per amendable component, a metric space, aggregation rule, and supermajority threshold. Each member submits an ideal element -- both vote and personal proposal. Any member may then submit a public proposal carrying supermajority public support under the revealed votes -- sourced from coalition deliberation, optimization, or AI mediation. The constitutional rule scores proposals against the status quo, adopting the supported proposal of positive maximal score (else retaining the status quo); the same rule, possibly with a higher threshold, amends the constitution itself. We develop the generalised median as the worked rule, establish framework-level guarantees, prove no misreport weakly dominates sincere voting, and study the compromise gap between best peak and unconstrained optimum -- zero in one dimension, bounded in general, narrowed in simulation by a simple heuristic. We instantiate the framework on seven canonical settings; the mean appears as a utilitarian alternative in the appendix. By unifying metric-space aggregation, reality-aware social choice, supermajority amendment, constitutional consensus, deliberative coalition formation, and AI mediation, this work delivers a comprehensive solution to the constitutional democratic governance of digital communities and organisations.

---


### 217. [Neural Surrogate Forward Modelling For Electrocardiology Without Explicit Intracellular Conductivity Tensor](https://arxiv.org/abs/2605.13366)

**<font color=#1a73e8>作者：</font>** Shaheim Ogbomo-Harmitt, Cesare Magnetti, Jakub Grzelak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate forward modelling is essential for non-invasive cardiac electrophysiology, particularly in atrial fibrillation, where electrical activation is highly disorganised. Conventional physics-based forward models require explicit specification of intracellular conductivity tensors, which are not directly measurable in clinical practice and introduce structural modelling errors. This proof-of-concept study presents a deep learning approach that learns a direct mapping from left atrial intracellular electrical potentials to far-field ECGs without requiring explicit intracellular conductivity inputs at inference time. Despite training only on 74 subjects, the model achieved an R2 of 0.949 \pm 0.037, highlighting potential to reduce structural uncertainty and improve non-invasive AF assessment.

---


### 218. [Phasor Memory Networks: Stable Backpropagation Through Time for Scalable Explicit Memory](https://arxiv.org/abs/2605.13370)

**<font color=#1a73e8>作者：</font>** Sungwoo Goo, Hwi-yeol Yun, Sangkeun Jung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> For over a decade, explicit memory architectures like the Neural Turing Machine have remained theoretically appealing yet practically intractable for language modeling due to catastrophic gradient instability during Backpropagation Through Time. In this work, we break this stalemate with \textit{Phasor Memory Network} (PMNet), a novel architecture that structurally resolves memory volatility through \textit{Unitary Phasor Dynamics} and \textit{Hierarchical Learnable Anchors}. Rather than relying on brute-force scaling, we present a mechanistic proof-of-concept in a controlled byte-level setting. By constraining recurrent state updates to phase rotations on a complex unit circle, PMNet preserves gradient norms and inherently prevents divergence without the need for specialized initialization. We empirically demonstrate the active actuation of the memory module through a synthetic Copy-Paste task, where PMNet utilizes an expansive \textit{85-slot hierarchical memory tree} ($=\sum^{4}_{h=1}4^{h-1}$) to achieve near 100\% exact retrieval across temporal distances that completely exceed the local sliding window attention's receptive field. Furthermore, despite being a compact 119M parameter model trained on 18.8B tokens, PMNet matches the zero-shot long-context robustness of a Mamba model that is three times larger. Our ablation studies and gradient analyses confirm that the historical failure of explicit memory was a structural alignment problem, which PMNet effectively overcomes, providing a theoretically grounded foundation for scalable sequence modeling.

---


### 219. [Exploiting Pre-trained Encoder-Decoder Transformers for Sequence-to-Sequence Constituent Parsing](https://arxiv.org/abs/2605.13373)

**<font color=#1a73e8>作者：</font>** Daniel Fernández-González, Cristina Outeiriño Cid  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> To achieve deep natural language understanding, syntactic constituent parsing plays a crucial role and is widely required by many artificial intelligence systems for processing both text and speech. A recent approach involves using standard sequence-to-sequence models to handle constituent parsing as a machine translation problem, moving away from traditional task-specific parsers. These models are typically initialized with pre-trained encoder-only language models like BERT or RoBERTa. However, the use of pre-trained encoder-decoder language models for constituency parsing has not been thoroughly explored. To bridge this gap, we extend the sequence-to-sequence framework by investigating parsers built on pre-trained encoder-decoder architectures, including BART, mBART, and T5. We fine-tune them to generate linearized parse trees and extensively evaluate them on different linearization strategies across both continuous treebanks and more complex discontinuous benchmarks. Our results demonstrate that our approach outperforms all prior sequence-to-sequence models and performs competitively with leading task-specific constituent parsers on continuous constituent parsing.

---


### 220. [Beyond Oversquashing: Understanding Signal Propagation in GNNs Via Observables](https://arxiv.org/abs/2605.13383)

**<font color=#1a73e8>作者：</font>** Eden Nagar, Ya-Wei Eileen Lin, Ron Levie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) perform computations on graphs by routing the signal between graph regions using a graph shift operator or a message passing scheme. Often, the propagation of the signal leads to a loss of information, where the signal tends to diffuse across the graph instead of being deliberately routed between regions of interest. Two notions that depict this phenomenon are oversmoothing and oversquashing. In this paper, we propose an alternative approach for modeling signal propagation, inspired by quantum mechanics, using the notion of observables. Specifically, we model the place in the graph where the signal lies, how much the signal is concentrated there, and how much of the signal is propagated towards a location of interest when applying a GNN. Using these new concepts, we prove that standard spectral GNNs have poor signal propagation capabilities. We then propose a new type of spectral GNN, termed Schrödinger GNN, which we show has a superior capacity to route the signal across the graph.

---


### 221. [Teaching and Learning under Deductive Errors](https://arxiv.org/abs/2605.13384)

**<font color=#1a73e8>作者：</font>** Jan Arne Telle, Brigt Håvardstun, Jose Hernandez-Orallo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most models of machine teaching and learning assume the learner makes no errors in its internal deductive inference. However, humans and large language models in few-shot learning regimes are two important examples of learners where this does not hold. They fail on some consistency checks, and they can fail stochastically. In this paper we introduce a teaching and learning framework that takes these deductive errors into account. We specifically study the case of machine teaching, as different characterizations of the teacher can account for both machine teaching and learning. In an overhauled Probably Approximately Correct (PAC) setting, we study theoretically that, for some estimated error level, the teacher must find a PAC teaching set that with high probability will lead the learner to guess a hypothesis that is approximately correct. We study the computational complexity of six different problems related to computing optimal PAC teaching sets. We give XP algorithms parametrized by size of teaching set, with tight runtime bounds under standard complexity assumptions like ETH. These results are complemented with a small experimental study of which teaching and learning protocols can best represent the observed behavior in some LLM teaching sessions.

---


### 222. [Support-Conditioned Flow Matching Is Kernel Smoothing](https://arxiv.org/abs/2605.13386)

**<font color=#1a73e8>作者：</font>** Daniel Matsui Smola  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models are often conditioned on a small set of examples via cross-attention. Under the Gaussian optimal-transport path, we show that the exact velocity field induced by a finite support set is a Nadaraya--Watson kernel smoother whose bandwidth decreases with flow time, from broad averaging at early steps to nearest-neighbor at late steps. A single Gaussian-kernel attention head exactly computes this field, connecting cross-attention conditioning to classical kernel theory. The theory predicts three failure regimes: nearest-neighbor collapse of the kernel at high dimension, mismatch between the isotropic kernel and the data geometry, and insufficient support for nonparametric estimation. Experiments on Gaussian mixtures, spherical shells, and DINOv2 ImageNet features confirm that learned conditioning improves in precisely these regimes, and that IP-Adapter's cross-attention implements approximate NW smoothing in practice.

---


### 223. [Taming the Long Tail: Rebalancing Adversarial Training via Adaptive Perturbation](https://arxiv.org/abs/2605.13395)

**<font color=#1a73e8>作者：</font>** Lilin Zhang, Yimo Guo, Yue Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks are highly vulnerable to adversarial examples, i.e.,small perturbations that can significantly degrade model performance. While adversarial training has become the primary defense strategy, most studies focus on balanced datasets, overlooking the challenges posed by real-world long-tail data. Motivated by the fact that perturbations in adversarial examples inherently alter the training distribution, we theoretically investigate their impact. We first revisit adversarial training for long-tail data and identify two key limitations: (i) a skewed training objective caused by class imbalance, and (ii) unstable evolution of adversarial distributions. Furthermore, we show that perturbations can simultaneously address both adversarial vulnerability and class imbalance. Based on these insights, we propose RobustLT, a plug-and-play framework that adaptively adjusts perturbations during adversarial training. Extensive experiments demonstrate that RobustLT consistently enhances adversarial robustness and class-balance on long-tailed datasets. The code is available at \href{this https URL}{this https URL}.

---


### 224. [PreFIQs: Face Image Quality Is What Survives Pruning](https://arxiv.org/abs/2605.13396)

**<font color=#1a73e8>作者：</font>** Jan Niklas Kolf, Guray Ozgur, Andrea Atzori 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face Image Quality Assessment (FIQA) evaluates the utility of a face image for automated face recognition (FR) systems. In this work, we propose PreFIQs, an unsupervised and training-free FIQA framework grounded in the Pruning Identified Exemplar (PIE) hypothesis. We hypothesize that low-utility face images rely disproportionately on fragile network parameters, resulting in larger geometric displacement of their embeddings under model sparsification. Accordingly, PreFIQs quantifies image utility as the Euclidean distance between L2-normalized embeddings extracted from a pre-trained FR model and its pruned counterpart. We provide a first-order theoretical justification via a Jacobian-vector product analysis, demonstrating that this empirical drift serves as a computationally efficient approximation of the exact geometric sensitivity of the latent embedding manifold. Extensive experiments across eight benchmarks and four FR models demonstrate that PreFIQs achieves competitive or superior performance compared to state-of-the-art FIQA methods, including establishing new state-of-the-art results on several benchmarks, without any training or supervision. These results validate parameter sparsification as a principled and practically efficient signal for face image utility, and demonstrate that quality is, in essence, what survives pruning.

---


### 225. [The Diffusion Encoder](https://arxiv.org/abs/2605.13399)

**<font color=#1a73e8>作者：</font>** Akhil Premkumar, Sarah Lucioni  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We construct a new kind of encoder, leveraging the expressive power of diffusion models. In a traditional variational autoencoder, the encoder and decoder jointly negotiate a latent representation of the input. This is made possible by the reparameterization trick, which simplifies training at the cost of restricting the encoder to a simple family of distributions. Replacing this encoder with a diffusion model requires rethinking how the decoder pressure can be transmitted back to the encoder, given that they tend to update their internal estimates of the latent in opposing directions. We solve this problem with an alternating training scheme, inspired by the expectation-maximization algorithm. Our method enables more reliable synchronization between encoder and decoder, while preserving the simple and efficient training objective of standard diffusion models.

---


### 226. [Trajectory-Level Data Augmentation for Offline Reinforcement Learning](https://arxiv.org/abs/2605.13401)

**<font color=#1a73e8>作者：</font>** Tobias Schmähling, Matthias Burkhardt, Tobias Windisch  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a data augmentation method for offline reinforcement learning, motivated by active positioning problems. Particularly, our approach enables the training of off-policy models from a limited number of suboptimal trajectories. We introduce a trajectory-based augmentation technique that exploits task structure and the geometric relationship between rewards, value functions, and mathematical properties of logging policies. During data collection, our augmentation supports suboptimal logging policies, leading to higher data quality and improved offline reinforcement learning performance. We provide theoretical justification for these strategies and validate them empirically across positioning tasks of varying dimensionality and under partial observability.

---


### 227. [Fast and Compact Graph Cuts for the Boykov-Kolmogorov Algorithm](https://arxiv.org/abs/2605.13402)

**<font color=#1a73e8>作者：</font>** Christian Møller Mikkelstrup, Anders Bjorholm Dahl, Philip Bille 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computing a minimum $s$-$t$ cut in a graph is a solution to a wide range of computer vision problems, and is often done using the Boykov-Kolmogorov (BK) algorithm. In this paper, we revisit the BK algorithm from both a theoretical and practical point of view. We improve the analysis of the time complexity of the BK algorithm to $O(mn|C|)$ and propose a new algorithm, the fast and compact BK (fcBK) algorithm, with a time complexity of $O(m|C|)$, where $m$, $n$, and $|C|$ are the number of edges, number of vertices, and the capacity of the cut, respectively. We additionally propose a compact graph representation that allows our implementation to find a minimum $s$-$t$ cut in a graph with upwards of $10^9$ vertices and $10^{10}$ edges on a machine with 128 GB of memory. We find our implementation of the BK algorithm to be the fastest available implementation of the BK algorithm when evaluating on a comprehensive set of benchmark datasets, highlighting the importance of memory-efficient implementations. We make our implementations publicly available for further research and implementation development within minimum $s$-$t$ cut algorithms.

---


### 228. [Vector-Quantized Discrete Latent Factors Meet Financial Priors: Dynamic Cross-Sectional Stock Ranking Prediction for Portfolio Construction](https://arxiv.org/abs/2605.13407)

**<font color=#1a73e8>作者：</font>** Namhyoung Kim, Jae Wook Song  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting cross-sectional stock returns is challenging due to low signal-to-noise ratios and evolving market regimes. Classical factor models offer interpretability but limited flexibility, while deep learning models achieve strong performance yet often underutilize financial priors. We address this gap with PRISM-VQ (PRior-Informed Stock Model with Vector Quantization), a dynamic factor framework that integrates expert prior factors, vector-quantized discrete latent factors learned from cross-sectional structure, and a structure-conditioned Mixture-of-Experts to generate time-varying factor loadings. Vector quantization acts as an information bottleneck that suppresses noise while capturing robust market structure, with discrete codes serving both as latent factors and as routing signals for temporal expert specialization. Experiments on CSI 300 and S&P 500 show consistent improvements in cross-sectional return prediction and portfolio performance over strong baselines while preserving interpretability. Our code is available at this https URL.

---


### 229. [DP-KFC: Data-Free Preconditioning for Privacy-Preserving Deep Learning](https://arxiv.org/abs/2605.13418)

**<font color=#1a73e8>作者：</font>** Marc Molina Van den Bosch, Riccardo Taiello, Albert Sund Aillet 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Differentially private optimization suffers from a fundamental geometric mismatch: deep networks have highly anisotropic loss landscapes, yet DP-SGD injects isotropic noise. Second-order preconditioning can resolve this, but estimating curvature typically requires private data (consuming privacy budget) or public data (introducing distribution shift). We show that the Fisher Information Matrix decouples into architectural sensitivity, recoverable via synthetic noise, and input correlations, approximable from modality-specific frequency statistics. We propose DP-KFC, which constructs KFAC preconditioners by probing networks with structured synthetic noise, requiring neither private nor public data. Empirically, DP-KFC consistently outperforms DP-SGD and adaptive baselines across diverse modalities in strong privacy regimes ($\varepsilon \leq 3$). DP-KFC matches private-data preconditioners while public-data variants degrade by up to $4.8\%$, showing that curvature can be estimated without consuming privacy budget or introducing distribution shift. This enables privacy-preserving learning in specialized domains (e.g., medical applications) where regulatory constraints make data scarce.

---


### 230. [Strategic PAC Learnability via Geometric Definability](https://arxiv.org/abs/2605.13426)

**<font color=#1a73e8>作者：</font>** Yuval Filmus, Shay Moran, Elizaveta Nesterova 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Strategic classification studies learning settings in which individuals can modify their features, at a cost, in order to influence the classifier's decision. A central question is how the sample complexity of the induced (strategic) hypothesis class depends on the complexities of the underlying hypothesis class and the cost structure governing feasible manipulations. Prior work has shown that in several natural settings, such as linear classifiers with norm costs, the induced complexity can be controlled. We begin by showing that such guarantees fail in general - even in simple cases: there exist hypothesis classes of VC dimension $1$ on the real line such that, even under the simplest interval neighborhoods, the induced class has infinite VC dimension. Thus, strategic behavior can turn an easy learning problem into a non-learnable one. To overcome this, we introduce structure via a geometric definability assumption: both the hypothesis class and the cost-induced neighborhood relation can be defined by first-order formulas over $\mathbb{R}_{\mathtt{exp}}$. Intuitively, this means that hypotheses and costs can be described using arithmetic operations, exponentiation, logarithms, and comparisons. This captures a broad range of natural classes and cost functions, including $\ell_p$ distances, Wasserstein distance, and information-theoretic divergences. Under this assumption, we prove that learnability is preserved, with sample complexity controlled by the complexity of the defining formulas.

---


### 231. [Rescaled Asynchronous SGD: Optimal Distributed Optimization under Data and System Heterogeneity](https://arxiv.org/abs/2605.13434)

**<font color=#1a73e8>作者：</font>** Ammar Mahran, Artavazd Maranjyan, Peter Richtárik  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Asynchronous stochastic gradient descent (ASGD) is a standard way to exploit heterogeneous compute resources in distributed learning: instead of forcing fast workers to wait for slow ones, the server updates the model whenever a gradient arrives. Vanilla ASGD applies each arriving gradient with the same weight. When local data distributions are heterogeneous, this becomes problematic: faster workers contribute more updates, and we show theoretically that the method is biased toward a frequency-weighted average of the local objectives rather than the desired global objective. Existing remedies typically move away from the simple ASGD template by introducing gathering phases, buffering, or extra memory. We show that this is unnecessary. Keeping the standard ASGD mechanism, we recover the correct objective by rescaling worker-specific stepsizes in proportion to their computation times, so that each worker contributes the same aggregate learning rate over a cycle. In the non-convex setting, under smoothness and bounded heterogeneity assumptions, we prove that the resulting method, Rescaled ASGD, converges to stationary points of the correct global objective in the fixed-computation model. Its time complexity matches the known lower bound in the leading term, while the effects of staleness and data heterogeneity appear only in lower-order terms. Experiments confirm that the method converges to the correct objective and is competitive with state-of-the-art baselines.

---


### 232. [Q-Flow: Stable and Expressive Reinforcement Learning with Flow-Based Policy](https://arxiv.org/abs/2605.13435)

**<font color=#1a73e8>作者：</font>** JaeHyeok Doo, Byeongguk Jeon, Seonghyeon Ye 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> There is growing interest in utilizing flow-based models as decision-making policies in reinforcement learning due to their high expressive capacity. However, effectively leveraging this expressivity for value maximization remains challenging, as naive gradient-based optimization requires backpropagating through numerical solvers and often leads to instability. Existing approaches typically address this issue by restricting the expressive capacity of flow-based policies, resulting in a trade-off between optimization stability and representational flexibility. To resolve this, we introduce Q-Flow, a framework that leverages the deterministic nature of flow dynamics to explicitly propagate terminal trajectory value to intermediate latent states along the policy-induced flow. This formulation enables stable policy optimization using intermediate value gradients without unrolling the numerical solver, effectively bridging the gap between stability and expressivity. We evaluate Q-Flow in the offline learning setting on the challenging OGBench suite, where it consistently outperforms state-of-the-art baselines by an average of 10.6 percentage points, while also enabling stable online adaptation within the same framework.

---


### 233. [Cognifold: Always-On Proactive Memory via Cognitive Folding](https://arxiv.org/abs/2605.13438)

**<font color=#1a73e8>作者：</font>** Suli Wang, Yiqun Duan, Yu Deng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing agent memory remains predominantly reactive and retrieval-based, lacking the capacity to autonomously organize experience into persistent cognitive structure. Toward genuinely autonomous agents, we introduce Cognifold, a brain-inspired "always-on" agent memory designed for the next generation of proactive assistants. CogniFold continuously folds fragmented event streams into self-emerging cognitive structures, bootstrapping progressively higher-level cognition from incoming events and accumulated knowledge. We ground this by extending Complementary Learning Systems (CLS) theory from two layers (hippocampus, neocortex) to three, adding a prefrontal intent layer. Emulating the prefrontal cortex as the locus of intentional control and decision-making, CogniFold achieves this through graph-topology self-organization: cognitive structures proactively assemble under the stream, merge when semantically similar, decay when stale, relink through associative recall, and surface intents when concept-cluster density crosses a threshold. We evaluate structural formation using CogEval-Bench, demonstrating that CogniFold uniquely produces memory structures that match cognitive expectations and concept emergence. Furthermore, across 7 broad-coverage benchmarks spanning five cognitive domains, we validate that CogniFold simultaneously performs robustly on conventional memory benchmarks.

---


### 234. [LongBEL: Long-Context and Document-Consistent Biomedical Entity Linking](https://arxiv.org/abs/2605.13451)

**<font color=#1a73e8>作者：</font>** Adam Remaki, Xavier Tannier, Christel Gérardin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Biomedical entity linking maps textual mentions to concepts in structured knowledge bases such as UMLS or SNOMED CT. Most existing systems link each mention independently, using only the mention or its surrounding sentence. This ignores dependencies between mentions in the same document and can lead to inconsistent predictions, especially when the same concept appears under different surface forms. We introduce LongBEL, a document-level generative framework that combines full-document context with a memory of previous predictions. To make this memory robust, LongBEL is trained with cross-validated predictions rather than gold labels, reducing the mismatch between training and inference and limiting cascading errors. Experiments on five biomedical benchmarks across English, French, and Spanish show that LongBEL improves over sentence-level generative baselines, with the largest gains on datasets where concepts frequently recur within documents. An ensemble of local, global, and memory-based variants achieves the best results across all benchmarks. Further analysis shows that the largest gains occur on recurring concepts, suggesting that LongBEL mainly improves document-level consistency rather than isolated mention disambiguation.

---


### 235. [Bayesian In Vivo Tracking of Synapses using Joint Poisson Deconvolution and Diffeomorphic Registration](https://arxiv.org/abs/2605.13455)

**<font color=#1a73e8>作者：</font>** Shashwat Kumar, Dominic M. Padova, Binish Narang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synapses are densely packed submicron structures that dynamically reorganize during learning and memory formation. Longitudinal \textit{in vivo} imaging of fluorescently tagged synaptic receptors offers a promising opportunity to study large-scale synaptic dynamics and how these processes are disrupted in neurological disease. However, in vivo imaging with 2-photon microscopy uses low laser power and therefore suffers from low signal-to-noise ratio (SNR) and high shot noise, nonlinear tissue motion between days, nonstationary fluctuations in synaptic fluorescence, and significant blur induced by the microscope point spread function (PSF). Together, these factors make it challenging to detect and track synapses, especially in regions with high synaptic density. This paper presents a novel template-based framework for modeling synapses as varying luminance point sources that move under a nonlinear tissue deformation. Taking a unified Bayesian approach, we apply this model to microscopy data by deriving a posterior that incorporates a diffeomorphic mapping for domain warping, a Gaussian point spread function for the imaging process, and a Poisson observation model for raw photon counts. The Bayesian solution simultaneously: (1) Constructs a probabilistic template of synapse locations, (2) denoises and deconvolves the image data, (3) infers fluorescence intensities, (4) performs diffeomorphic image registration to correct for tissue motion, and (5) provides confidence regions for these parameter estimates. We demonstrate the framework on both a 2D+t simulated dataset and a 3D+t longitudinal \textit{in vivo} microscopy dataset of fluorescent synapses imaged in a mouse over two weeks.

---


### 236. [OP4KSR: One-Step Patch-Free 4K Super-Resolution with Periodic Artifact Suppression](https://arxiv.org/abs/2605.13457)

**<font color=#1a73e8>作者：</font>** Chengyan Deng, Pengbin Yu, Zhentao Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based real-world image super-resolution (Real-ISR) has achieved remarkable perceptual quality; however, directly super-resolving images to 4K remains limited by extreme memory consumption. Consequently, prior methods adopt patch-based inference, sacrificing global context and introducing semantic confusion, spatial inconsistency, and severe latency. We propose OP4KSR, a one-step patch-free 4K SR approach built upon the powerful Flux backbone. By leveraging the extreme-compression F16 VAE, OP4KSR makes 4K SR inference tractable under practical GPU budgets, preserving global spatial-semantic coherence while enabling highly efficient inference. However, adapting this one-step architecture intrinsically triggers severe periodic artifacts. We trace this to a RoPE base frequency allocation mismatch and intra-token spatial ambiguity, both exacerbated by the lack of iterative refinement. To suppress these artifacts, we couple RoPE base frequency rescaling (RFR) with an autocorrelation-based periodicity loss ($\mathcal{L}_\text{AP}$). Furthermore, we curate a dedicated training dataset alongside three benchmarks (one synthetic and two real-world) to advance 4K SR research. Extensive experiments demonstrate that OP4KSR achieves competitive perceptual quality with efficient inference, generating a $4096\times4096$ output in only 5.75 seconds on a single NVIDIA H20 GPU.

---


### 237. [Efficient Sensor Fusion for Gesture Recognition on Resource-Constrained Devices](https://arxiv.org/abs/2605.13462)

**<font color=#1a73e8>作者：</font>** Pietro Bartoli, Christian Veronesi, Tommaso Bondini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gesture recognition is a cornerstone of Human-Computer Interaction (HCI) for smart eyewear, enabling natural and device-free control in augmented reality environments. Traditional vision-based approaches face significant challenges regarding power consumption, computational latency, and user privacy. This paper proposes a lightweight, privacy-preserving gesture recognition system based on the fusion of low-resolution Time-of-Flight (ToF) and Infrared (IR) thermal sensors. We used an 8 times 8 multizone ToF sensor (VL53L8CH) and an 8 times 8 IR array (AMG8833) to capture complementary depth and thermal cues. A compact Convolutional Neural Network (CNN) with a specialized grouped-convolution architecture is designed to fuse these modalities efficiently on a microcontroller (MCU). Experimental results on a custom dataset of 7 static gestures, validated via k-fold cross-validation, demonstrate that the proposed fusion strategy significantly outperforms single-sensor baselines with an accuracy of 92.3% and a macro F1-score of 0.93. Finally, on-device benchmarks on STM32F4 and STM32H7 MCUs confirm the system's suitability for resource-constrained wearables, requiring only 6,343 parameters and achieving millisecond-level inference latency with a total system power of 50 mW.

---


### 238. [A Unified Three-Stage Machine Learning Framework for Diabetes Detection, Subtype Discrimination, and Cognitive-Metabolic Hypothesis Testing](https://arxiv.org/abs/2605.13464)

**<font color=#1a73e8>作者：</font>** Vishal Pandey, Ruzina Haque Laskar, Rishav Tewari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diabetes mellitus affects over 537 million adults worldwide and remains a major challenge in preventive healthcare. Existing machine-learning studies primarily formulate diabetes prediction as a binary classification problem, while subtype-oriented analysis and glycaemic-cognitive associations remain comparatively underexplored. We present a reproducible three-stage machine learning framework for diabetes detection, subtype-oriented clustering, and metabolic-cognitive association analysis. In Stage 1, five supervised classifiers together with a stacking ensemble are benchmarked on the NCSU Diabetes Dataset using stratified five-fold cross-validation and evaluation metrics including ROC-AUC, balanced accuracy, recall, and F1-score. SVM-RBF and Logistic Regression achieve the highest ROC-AUC ($0.825 \pm 0.026$), while Random Forest achieves the highest accuracy ($0.762 \pm 0.030$). SHAP explainability identifies Glucose, BMI, and Age as the dominant predictive biomarkers. In Stage 2, silhouette-validated K-Means clustering ($k=2$, silhouette $\approx 0.116$) is applied to confirmed diabetic cases using Glucose, Insulin, and Age, recovering clinically plausible subtype-oriented partitions without requiring ground-truth subtype labels. In Stage 3, statistical analysis of the Ohio Longitudinal Cognitive Dataset ($n=373$) reveals a significant positive association between glycaemic control and cognitive function ($\rho_s = 0.208$, $p = 5.29 \times 10^{-5}$), which survives Holm correction. The findings support the utility of statistically grounded and interpretable ML pipelines for reproducible diabetes analytics and subtype-aware exploratory analysis.

---


### 239. [Z-Order Transformer for Feed-Forward Gaussian Splatting](https://arxiv.org/abs/2605.13465)

**<font color=#1a73e8>作者：</font>** Can Wang, Lei Liu, Wei Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in 3D Gaussian Splatting (3DGS) have enabled significant progress in photorealistic novel view synthesis. However, traditional 3DGS relies on a slow, iterative optimization process, which limits its use in scenarios demanding real-time results. To overcome this bottleneck, recent feed-forward methods aim to predict Gaussian attributes directly from images, but they often struggle with the redundancy of Gaussian primitives and rendering quality. In this work, we introduce a transformer-based architecture specifically designed for feed-forward Gaussian Splatting. Our key insight is that spatial and semantic relationships among Gaussians can be effectively captured through a sparse attention mechanism, enabled by a Z-order strategy that organizes the unstructured Gaussian set into a spatially coherent sequence. Furthermore, we incorporate this Z-order strategy to adaptively suppress redundancy while preserving critical structural details. This allows the transformer to efficiently model context, compress Gaussian primitives, and predict Gaussian attributes in a single forward pass. Comprehensive experiments demonstrate that our method achieves fast and high-quality novel view synthesis with fewer Gaussian primitives.

---


### 240. [PDCR: Perception-Decomposed Confidence Reward for Vision-Language Reasoning](https://arxiv.org/abs/2605.13467)

**<font color=#1a73e8>作者：</font>** Hee Suk Yoon, Eunseop Yoon, Ji Woo Hong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) traditionally relies on a sparse, outcome-based signal. Recent work shows that providing a fine-grained, model-intrinsic signal (rewarding the confidence growth in the ground-truth answer) effectively improves language reasoning training by providing step-level guidance without costly external models. While effective for unimodal text, we find that naively applying this global reward to vision-language (V-L) reasoning is a suboptimal strategy, as the task is a heterogeneous mix of sparse visual perception and dense textual reasoning. This global normalization creates mixture-induced signal degradation, where the training signal for visual steps is statistically distorted by the predominant textual steps. We propose Perception-Decomposed Confidence Reward (PDCR), a framework that solves this by aligning the reward structure with the task's heterogeneous nature. PDCR first performs an unsupervised skill decomposition, introducing a model-internal Visual Dependence Score to quantify visual reliance and applying a clustering algorithm to separate perception and reasoning steps. Based on this, PDCR computes a decomposed advantage by normalizing confidence gains within each skill cluster. This intra-cluster normalization provides a stable, correctly-scaled signal for both perception and reasoning. We demonstrate that PDCR outperforms the naive, global-reward formulation and sparse-reward baselines on key V-L reasoning benchmarks.

---


### 241. [Twincher: Bijective Representation Learning for Robust Inversion of Continuous Systems](https://arxiv.org/abs/2605.13470)

**<font color=#1a73e8>作者：</font>** Arkady Gonoskov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in AI have been primarily driven by large-scale neural architectures that excel at function approximation, rather than by tailored inductive biases and inference or learning strategies that could be important for resource-efficient real-world perception and planning through the solution of inverse problems. In this work, we consider the possibility of enabling robust inversion of continuous forward processes $p \mapsto y$ by learning representations of $y$ that are bijectively aligned with $p$ while remaining insensitive to perturbations in $y$ caused by noise or model mismatch. We propose Twincher, a class of architectures based on stacks of structured diffeomorphic transformations and tailored adversarial training strategies that enable learning such bijective representations. We provide a public API for training and inference and empirically demonstrate the ability of the proposed architecture to efficiently learn bijective representations of synthetic systems, thereby enabling robust and efficient iterative inverse inference. Compared to a baseline inverse-modeling approach, the method exhibits improved data efficiency and robustness, providing initial evidence for the potential of bijective representation learning in robotics, vision, and physical AI.

---


### 242. [Sleeper Channels and Provenance Gates: Persistent Prompt Injection in Always-on Autonomous AI Agents](https://arxiv.org/abs/2605.13471)

**<font color=#1a73e8>作者：</font>** Narek Maloyan, Dmitry Namiot  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Always-on AI agents (OpenClaw, Hermes Agent) run as a single persistent process under the owner's identity, folding messaging, memory, self-authored skills, scheduling, and shell into one authority boundary. This configuration opens what we call \emph{sleeper channels}: an untrusted input to one surface persists as a memory, skill, scheduled job, or filesystem patch, then fires later through a different surface with no attacker present. Two independent axes define the class: persistence substrate and firing-separation. We walk a confused-deputy cron attack end-to-end through OpenClaw at a pinned commit. The defense is tiered (D1, D2, D3), and D2 carries a soundness theorem against seven named deployment invariants. D2 keys on a canonical action-instance digest with one-shot owner attestations, defeating paraphrase laundering, multi-input grant reuse, and replay. A companion artifact ships the gate, a static audit over the vendored source, and a runtime adapter realising five of the ten mediation hooks (H1, H2, H3, H6, H9) around the cron path (42 tests, Node~$\geq{}20$, at \href{this https URL}{this http URL}). Empirical evaluation is preregistered as follow-on.

---


### 243. [OSDN: Improving Delta Rule with Provable Online Preconditioning in Linear Attention](https://arxiv.org/abs/2605.13473)

**<font color=#1a73e8>作者：</font>** Chenyu Zhou, Hongpei Li, Yuerou Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear attention and state-space models offer constant-memory alternatives to softmax attention, but often struggle with in-context associative recall. The Delta Rule mitigates this by writing each token via one step of online gradient descent. However, its step size relies on a single scalar gate that ignores the feature-wise curvature of the inner objective. We propose Online Scaled DeltaNet (OSDN), which augments the scalar gate with a diagonal preconditioner updated online via hypergradient feedback. Crucially, this right-preconditioning is algebraically equivalent to a per-feature scaling of the write-side key. This equivalence allows OSDN to strictly preserve the hardware-friendly chunkwise parallel pipeline of DeltaNet without incurring high-dimensional state overhead. Theoretically, by exploiting the exact-quadratic structure of the inner regression loss, we establish super-geometric convergence against a right-Newton comparator and prove an algorithm-aligned token-local residual contraction bound. To handle non-stationary contexts, we further introduce Adaptive Preconditioner Forgetting (APF) to dynamically refresh stale calibration. Empirically, OSDN demonstrates strong performance across scales. At the 340M-parameter scale, OSDN improves JRT-style in-context recall by 32% over DeltaNet. Scaling to 1.3B parameters, it achieves a 39% reduction in the recall residual ratio while maintaining parity on general downstream tasks (e.g., perplexity and LongBench) -- demonstrating that our online-preconditioning mechanism effectively transfers and amplifies at the billion-parameter scale.

---


### 244. [FedHPro: Federated Hyper-Prototype Learning via Gradient Matching](https://arxiv.org/abs/2605.13475)

**<font color=#1a73e8>作者：</font>** Huan Wang, Jun Shen, Haoran Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) enables collaborative training of distributed clients while protecting privacy. To enhance generalization capability in FL, prototype-based FL is in the spotlight, since shared global prototypes offer semantic anchors for aligning client-specific local prototypes. However, existing methods update global prototypes at the prototype-level via averaging local prototypes or refining global anchors, which often leads to semantic drift across clients and subsequently yields a misaligned global signal. To alleviate this issue, we introduce hyper-prototypes, defined by a set of learnable global class-wise prototypes to preserve underlying semantic knowledge across clients. The hyper-prototypes are optimized via gradient matching to align with class-relevant characteristics distilled directly from clients' real samples, rather than prototype-level descriptors. We further propose FedHPro, a Federated Hyper-Prototype Learning framework, to leverage hyper-prototypes to promote inter-class separability via mutual-contrastive learning with client-specific margin, while encouraging intra-class uniformity through a consistency penalty. Comprehensive experiments under diverse heterogeneous scenarios confirm that 1) hyper-prototypes produce a more semantically consistent global signal, and 2) FedHPro achieves state-of-the-art performance on several benchmark datasets. Code is available at \href{this https URL}{this https URL}.

---


### 245. [Neural Video Compression with Domain Transfer](https://arxiv.org/abs/2605.13476)

**<font color=#1a73e8>作者：</font>** Tiange Zhang, Rongqun Lin, Xiandong Meng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Content-adaptive compression has always been a key direction in neural video coding (NVC), aiming to mitigate the domain gap between training and testing data. Such gaps often arise from distributional discrepancies between training and inference data, which may cause noticeable performance degradation when the testing content differs from the training distribution. To tackle this challenge, we propose DCVC-DT, a domain transfer enhanced neural video compression framework. Specifically, we design a lightweight online domain transfer (DT) mechanism that dynamically adapts the encoded latent representation during inference, effectively bridging the domain gap without modifying the encoder or decoder parameters. In addition, we develop a frame-level dynamic RD (Rate and Distortion) adjustment scheme that actively regulates the ratio of R and D in the loss function based on quality fluctuation, thereby improving rate-distortion performance. Extensive experiments demonstrate that DCVC-DT achieves up to 6.21% bitrate savings over the baseline DCVC-DC, while significantly enhancing generalization to unseen testing data and alleviating error propagation. Our code is available at this https URL.

---


### 246. [Discovery of Hidden Miscalibration Regimes](https://arxiv.org/abs/2605.13484)

**<font color=#1a73e8>作者：</font>** Katarzyna Kobalczyk, Mihaela van der Schaar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Calibration is commonly evaluated by comparing model confidence with its empirical correctness, implicitly treating reliability as a function of the confidence score alone. However, this view can hide substantial structure: models may be systematically overconfident on some kinds of inputs and underconfident on others, causing global reliability diagnostics to obscure localised calibration failures. To address this, we formulate the problem of discovering hidden miscalibration regimes without assuming access to predefined data slices. We define the corresponding miscalibration field and propose a diagnostic framework for estimating it. Our approach learns a calibration-aware representation of the input space and estimates signed local miscalibration by kernel smoothing in the learned geometry. Across four real-world LLM benchmarks and twelve LLMs, we find that input-dependent calibration heterogeneity is prevalent. We further show that the discovered fields are actionable: they support local confidence correction and reduce calibration error in systematically miscalibrated regions where confidence-based methods such as isotonic regression and temperature scaling are less effective.

---


### 247. [R^2-Mem: Reflective Experience for Memory Search](https://arxiv.org/abs/2605.13486)

**<font color=#1a73e8>作者：</font>** Xinyuan Wang, Wenyu Mao, Junkang Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deep search has recently emerged as a promising paradigm for enabling agents to retrieve fine-grained historical information without heavy memory pre-managed. However, existing deep search agents for memory system repeat past error behaviors because they fail to learn from the prior high- and low-quality search trajectories. To address this limitation, we propose R^2-Mem, a reflective experience framework for memory search systems. In the offline stage, a Rubric-guided Evaluator scores low- and high-quality steps in historical trajectories, and a self-Reflection Learner distills the corresponding abstract experience. During the online inference, the retrieved experience will guide future search actions to avoid repeated mistakes and maintain high-quality behaviors. Extensive experiments demonstrate that R^2-Mem consistently improves both effectiveness and efficiency over strong baselines, improving F1 scores by up to 22.6%, while reducing token consumption by 12.9% and search iterations by 20.2%. These results verify that R^2-Mem provides a RL-free and low-cost solution for self-improving LLM agents.

---


### 248. [Path-independent Flow Matching for Multi-parameter Generative Dynamics](https://arxiv.org/abs/2605.13487)

**<font color=#1a73e8>作者：</font>** Francisco Téllez, AmirHossein Zamani, Philippe Martin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow Matching is a powerful framework for learning transport maps between probability distributions. Yet its standard single-parameter formulation is not designed to capture multi-parameter variations where the resulting transport should be path-independent. Path independence is crucial because it ensures that transformations depend only on the initial and target distributions, not on the specific path. In this work, we introduce Path-independent Flow Matching (PiFM), a method for learning vector fields whose induced flows yield path-independent transport between distributions. We show that PiFM generalizes Flow Matching to higher-dimensional parameter domains while enforcing structural conditions that ensure consistency of composed transformations. In addition, we show that, under suitable assumptions, PiFM approximates the Wasserstein barycenter, linking the framework to a notion of distributional interpolation. To enable practical training, we propose a tractable, simulation-free objective that regresses onto multi-parameter conditional probability paths. We showcase empirically that PiFM outperforms other approaches on both synthetic and real world data in interpolating path-independent trajectories and generating desired out of distribution samples.

---


### 249. [Phantom Force: Injecting Adversarial Tactile Perceptions into Embodied Intelligence via EMI](https://arxiv.org/abs/2605.13492)

**<font color=#1a73e8>作者：</font>** Zirui Kong, Youqian Zhang, Sze Yiu Chau  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Embodied intelligent robots rely on tactile sensors to interact with the physical world safely. While the security of visual perception systems has been studied (e.g., adversarial samples), the integrity of the tactile sensory channel remains unexplored. This work explores a vulnerability in Hall-effect fingertip sensors, showing their susceptibility to intentional Electromagnetic Interference (EMI). We demonstrate that a targeted signal injection can induce strong ``phantom forces'', amplifying perceived force magnitude by over \textbf{9$\times$} and deviating the inferred force direction by \textbf{65$^\circ$}. Such perturbations can paralyze learning-based tactile classification models, seriously affecting robot movement. An attacker could exploit this vulnerability to coerce a robot hand into crushing fragile objects or dropping dangerous payloads.

---


### 250. [PhysEditBench: A Protocol-Conditioned Benchmark for Dense Physical-Map Prediction with Image Editors](https://arxiv.org/abs/2605.13493)

**<font color=#1a73e8>作者：</font>** Jiaxin Yang, Yu Hou, Muxin Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Can general-purpose image editors predict physical maps from a single RGB image? General-purpose image editors differ from standard task-specific dense-prediction models: they do not directly take an image and output a physical map. Instead, they must be guided by prompts, examples, or image-based textual cues. To this end, we introduce PhysEditBench, a novel protocol-conditioned benchmark to evaluate and standardize image editors in dense physical-map prediction that covers five targets: depth, normal, albedo, roughness, and metallic maps. For evaluation data, we build a target-dependent benchmark substrate. We use OpenRooms-FF for depth, surface normal, albedo, and roughness, InteriorVerse as an additional source for depth, normal, albedo, and a new procedurally generated source for metallic maps. We curate the data with quality checks, valid-region masks, scene-level sampling, and lighting-based stress subsets to ensure reliable and diverse evaluation. For each target, PhysEditBench defines a fixed protocol that specifies the allowed input, expected output format, and scoring procedure. Each score, therefore, reflects the performance of a model under a specified protocol, rather than its best possible performance under all prompts or interaction modes. Experimental results show that specialized models remain much stronger on depth, normal, and albedo, and stronger image editors can produce more reasonable map-like outputs. For roughness and metallic, image editors can match or outperform specialized baselines on some scalar metrics, but they still suffer from structural errors, sparsity effects, and sensitivity to lighting.

---


> [!TIP]
> 当前位于：**201-250**（第 5/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-328](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
