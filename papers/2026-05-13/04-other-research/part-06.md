# 📦 其他研究 | 2026年05月13日

> 本类共 **396** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-396](./part-08.md)

---

### 251. [YFPO: A Preliminary Study of Yoked Feature Preference Optimization with Neuron-Guided Rewards for Mathematical Reasoning](https://arxiv.org/abs/2605.11906)

**<font color=#1a73e8>作者：</font>** Yifan Le  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Preference optimization has become an important post-training paradigm for improving the reasoning abilities of large language models. Existing methods typically rely on externally constructed preference data, using preferred and dispreferred responses as sample-level supervision. However, such external signals rarely make explicit use of capability-related information contained in the model's internal representations. For mathematical reasoning, certain neuron groups may exhibit activation patterns associated with mathematical knowledge, symbolic manipulation, or logical reasoning. Similar to reflexive behavioral signals, these internal activations may provide a coarse indication of whether the model is engaging math-related this http URL introduce YFPO, short for Yoked Feature Preference Optimization, a preliminary neuron-guided preference optimization framework for mathematical reasoning. YFPO first uses AttnLRP to identify math-related neurons, and then constructs an auxiliary reward from their activation margin between preferred and dispreferred responses. This design augments external preference learning with internal neuron-level signals. We conduct preliminary experiments on a small-scale language model using GSM8K as the main benchmark. Results suggest that neuron-level signals can interact with preference optimization and occasionally improve reasoning performance, offering a promising direction for more fine-grained and interpretable reasoning-oriented post-training.

---


### 252. [Delightful Gradients Accelerate Corner Escape](https://arxiv.org/abs/2605.11908)

**<font color=#1a73e8>作者：</font>** Jincheng Mei, Ian Osband  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Softmax policy gradient converges at $O(1/t)$, but its transient behavior near sub-optimal corners of the simplex can be exponentially slow. The bottleneck is self-trapping: negative-advantage actions reinforce the corner policy and can initially push the optimal action backward. We study \emph{Delightful Policy Gradient} (DG), which gates each policy-gradient term by the product of advantage and action surprisal. For $K$-armed bandits, we prove that the zero-temperature limit of DG removes this corner-trapping mechanism on a quantitative sector near any sub-optimal corner, yielding a first-exit escape bound logarithmic in the initial probability ratio. At every fixed temperature, the same local mechanism persists because harmful actions are polynomially suppressed as they become rare. A key structural insight is that every action better than the corner action is an \emph{ally}: its contribution to escape is non-negative. Combining corner instability with a monotonic value improvement identity, we prove that DG converges globally to the optimal policy in both bandits and tabular MDPs at an asymptotic $O(1/t)$ rate. We also show, via an exact counterexample, that this tabular mechanism can fail under shared function approximation. In MNIST contextual bandits with a shared-parameter neural network, DG nevertheless recovers from bad initializations faster than standard policy gradient, suggesting that the counterexample marks a boundary of the theory rather than a practical prohibition.

---


### 253. [Rethinking Positional Encoding for Neural Vehicle Routing](https://arxiv.org/abs/2605.11910)

**<font color=#1a73e8>作者：</font>** Chuanbo Hua, Federico Berto, Andre Hottung 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Transformer-based models have become the dominant paradigm for neural combinatorial optimization (NCO) of vehicle routing problems (VRPs), yet the role of positional encoding (PE) in these architectures remains largely unexplored. Unlike natural language, where tokens are uniformly spaced on a line, routing solutions exhibit several properties that render standard NLP positional encodings inadequate. In this work, we formalize three such structural properties that a routing-aware PE should respect, namely anisometric node distances, cyclic and direction-aware topology, and hierarchical depot-anchored global multi-route structure, combining them with a unifying design principle of geometric grounding. Guided by these criteria, we analyze and compare PE methods spanning NLP, graph-transformer, and routing-specific families, and propose a hierarchical anisometric PE that combines a distance-indexed, circularly consistent in-route encoding with a depot-anchored angular cross-route encoding. Extensive experiments across diverse VRP variants demonstrate that geometry-grounded PE consistently outperforms index-based alternatives, with gains that transfer across problem variants, model architectures, and distribution shifts.

---


### 254. [Understanding Sample Efficiency in Predictive Coding](https://arxiv.org/abs/2605.11911)

**<font color=#1a73e8>作者：</font>** Gaspard Oliviers, Elene Lominadze, Rafal Bogacz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive Coding (PC) is an influential account of cortical learning. Much of recent work has focused on comparing PC to Backpropagation (BP) to find whether PC offers any advantages. Small scale experiments show that PC enables learning that is more sample efficient and effective in many contexts, though a thorough theoretical understanding of the phenomena remains elusive. To address this, we quantify the efficiency of learning in BP and PC through a metric called ``target alignment'', which measures how closely the change in the output of the network is aligned to the output prediction error. We then derive and empirically validate analytical expressions for target alignment in Deep Linear Networks. We show that learning in PC is more efficient than BP, which is especially pronounced in deep, narrow and pre-trained networks. We also derive exact conditions for guaranteed optimal target alignment in PC and validate our findings through experiments. We study full training trajectories of linear and non-linear models, and find the predicted benefits of PC persist in practice even when some assumptions are violated. Overall, this work provides a mechanistic understanding of the higher learning efficiency observed for PC over BP in previous works, and can guide how PC should be parametrised to learn most effectively.

---


### 255. [Vector Scaffolding: Inter-Scale Orchestration for Differentiable Image Vectorization](https://arxiv.org/abs/2605.11913)

**<font color=#1a73e8>作者：</font>** Jaerin Lee, Kanggeon Lee, Kyoung Mu Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Differentiable vector graphics have enabled powerful gradient-based optimization of vector primitives directly from raster images. However, existing frameworks formulate this as a flat optimization problem, forcing hundreds to thousands of randomly initialized curves to blindly compete for pixel-level error reduction. This disordered optimization leads to topology collapse, where macroscopic structures are distorted by internal high-frequency noise, resulting in a redundant and uneditable "polygon soup" that limits practical editability. To address this limitation, we propose Vector Scaffolding, a novel hierarchical optimization framework that shifts from flat pixel-matching to structured topological construction tailored for vector graphics. By identifying a key cause of topology collapse as the mathematical imbalance between area and boundary gradients, we introduce Interior Gradient Aggregation to stabilize the learning dynamics of multi-scale curve mixtures. Upon this stabilized landscape, we employ Progressive Stratification and Rapid Inflation Scheduling to progressively densify vector primitives with extremely high learning rates ($\times 50$). Experiments demonstrate that our approach accelerates optimization by $2.5\times$ while simultaneously improving PSNR by up to 1.4 dB over the previous state of the art.

---


### 256. [Domain Restriction via Multi SAE Layer Transitions](https://arxiv.org/abs/2605.11920)

**<font color=#1a73e8>作者：</font>** Elias Shaheen, Avi Mendelson  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The general-purpose nature of Large Language Models (LLMs) presents a significant challenge for domain-specific applications, often leading to out-of-domain (OOD) interactions that undermine the provider's intent. Existing methods for detecting such scenarios treat the LLM as an uninterpretable black box and overlook the internal processing of inputs. In this work we show that layer transitions provide a promising avenue for extracting domain-specific signature. Specifically, we present several lightweight ways of learning on internal dynamics encoded using a sparse autoencoder (SAE) that exhibit great capability in distinguishing OOD texts. Building on top of SAEs representation transitions enables us to better interpret the LLM internal evolution of input processing and shed light on its decisions. We provide a comprehensive analysis of the method and benchmark it with the gemma-2 2B and 9B models. Our results emphasize the efficacy of the internal process in capturing fine-grained input-related details.

---


### 257. [RealDiffusion: Physics-informed Attention for Multi-character Storybook Generation](https://arxiv.org/abs/2605.11927)

**<font color=#1a73e8>作者：</font>** Qi Zhao, Jun Chen, Ivor Tsang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While modern diffusion models excel at generating diverse single images, extending this to sequential generation reveals a fundamental challenge: balancing narrative dynamism with multi-character coherence. Existing methods often falter at this trade-off, leading to artifacts where characters lose their identity or the story stagnates. To resolve this critical tension, we introduce RealDiffusion, a unified framework designed to reconcile robust coherence with narrative dynamism. Heat diffusion serves as a dissipative prior that averages neighboring features along the sequence and removes high-frequency noise within the subject region. This suppresses attribute drift and stabilizes identity across frames. A region-aware stochastic process then introduces small perturbations that explore nearby modes and prevent collapse so the story maintains pose change and scene evolution. We thus introduce a lightweight, training-free Physics-informed Attention mechanism that injects controllable physical priors into the self-attention layers during inference. By modeling feature evolution as a configurable physical system, our method regularizes spatio-temporal relationships without suppressing intentional, prompt-driven changes. Extensive experiments demonstrate that RealDiffusion achieves substantial gains in character coherence while preserving narrative dynamism, outperforming state-of-the-art approaches. Code is available at this https URL.

---


### 258. [When Simulation Lies: A Sim-to-Real Benchmark and Domain-Randomized RL Recipe for Tool-Use Agents](https://arxiv.org/abs/2605.11928)

**<font color=#1a73e8>作者：</font>** Xiaolin Zhou, Aojie Yuan, Zheng Luo 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-use language agents are evaluated on benchmarks that assume clean inputs, unambiguous tool registries, and reliable APIs. Real deployments violate all these assumptions: user typos propagate into hallucinated tool names, a misconfigured request timeout can stall an agent indefinitely, and duplicate tool names across servers can freeze an SDK. We study these failures as a sim-to-real gap in the tool-use partially observable Markov decision process (POMDP), where deployment noise enters through the observation, action space, reward-relevant metadata, or transition dynamics. We introduce RobustBench-TC, a benchmark with 22 perturbation types organized by these four POMDP components, each grounded in a verified GitHub issue or documented tool-calling failure. Across 21 models from 1.5B to 32B parameters (including the closed-source o4-mini), the robustness profile is sharply uneven: observation perturbations reduce accuracy by less than 5%, while reward-relevant and transition perturbations reduce accuracy by roughly 40% and 30%, respectively; scale alone does not close these gaps. We then propose ToolRL-DR, a domain-randomization reinforcement learning (RL) recipe that trains a tool-use agent on perturbation-augmented trajectories spanning the three statically encodable POMDP components. On a 3B backbone, ToolRL-DR-Full retains roughly three-quarters of clean accuracy and reaches an aggregate perturbed accuracy comparable to open-source 14B function-calling baselines while substantially narrowing the gap to o4-mini. It closes approximately 27% of the Transition gap despite never seeing transition perturbations in training, suggesting that RL on adversarial static tool-use inputs induces a more persistent retry policy that transfers to unseen runtime failures. The dataset, code and benchmark leaderboard are publicly available.

---


### 259. [Interactive State Space Model with Cross-Modal Local Scanning for Depth Super-Resolution](https://arxiv.org/abs/2605.11934)

**<font color=#1a73e8>作者：</font>** Chen Wu, Ling Wang, Zhuoran Zheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Guided depth super-resolution (GDSR) reconstructs HR depth maps from LR inputs with HR RGB guidance. Existing methods either model each modality independently or rely on computationally expensive attention mechanisms with quadratic complexity, hindering the establishment of efficient and semantically interactive joint representations. In this paper, we observe that feature maps from different modalities exhibit semantic-level correlations during feature extraction. This motivates us to develop a more flexible approach enabling dense, semantically-aware deep interactions between modalities. To this end, we propose a novel GDSR framework centered around the Interactive State Space Model. Specifically, we design a cross-modal local scanning mechanism that enables fine-grained semantic interactions between RGB and depth features. Leveraging the Mamba architecture, our framework achieves global modeling with linear complexity. Furthermore, a cross-modal matching transform module is introduced to enhance interactive modeling quality by utilizing representative features from both modalities. Extensive experiments demonstrate competitive performance against state-of-the-art methods.

---


### 260. [Chronicles-OCR: A Cross-Temporal Perception Benchmark for the Evolutionary Trajectory of Chinese Characters](https://arxiv.org/abs/2605.11960)

**<font color=#1a73e8>作者：</font>** Gengluo Li, Shangpin Peng, Xingyu Wan 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Large Language Models (VLLMs) have achieved remarkable success in modern text-rich visual understanding. However, their perceptual robustness in the face of the continuous morphological evolution of historical writing systems remains largely unexplored. Existing ancient text datasets typically focus on isolated historical periods, failing to capture the systematic visual distribution shifts spanning thousands of years. To bridge this gap and empower Digital Humanities, we introduce Chronicles-OCR, the first comprehensive benchmark specifically designed to evaluate the cross-temporal visual perception capabilities of VLLMs across the complete evolutionary trajectory of Chinese characters, known as the Seven Chinese Scripts. Curated in collaboration with top-tier institutional domain experts, the dataset comprises 2,800 strictly balanced images encompassing highly diverse physical media, ranging from tortoise shells to paper-based calligraphy. To accommodate the drastic morphological and topological variations across different historical stages, we propose a novel Stage-Adaptive Annotation Paradigm. Based on this, Chronicles-OCR formulates four rigorous quantitative tasks: cross-period character spotting, fine-grained archaic character recognition via visual referring, ancient text parsing, and script classification. By isolating visual perception from semantic reasoning, Chronicles-OCR provides an authoritative platform to expose the limitations of current VLLMs, paving the way for robust, evolution-aware historical text perception. Chronicles-OCR is publicly available at this https URL.

---


### 261. [What Does It Mean for a Medical AI System to Be Right?](https://arxiv.org/abs/2605.11963)

**<font color=#1a73e8>作者：</font>** Antony Gitau  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper examines what it means for a medical AI system to be right by grounding the question in a specific clinical context: the automatic classification of plasma cells in digitized bone marrow smears for the diagnosis of multiple myeloma. Drawing on philosophy of science and research ethics, the paper argues that correctness in medical AI is not a singular property reducible to benchmark performance, but a multi-dimensional concept involving the availability of expertly labeled medical datasets, the explainability and interpretability of model outputs, the clinical meaningfulness of evaluation metrics, and the distribution of accountability in human-AI workflows. As such, the paper develops this argument through four interrelated themes: the instability of ground truth labels, the opacity of overconfident AI, the inadequacy of standard clinical metrics, and the risk of automation bias in time-pressured clinical settings.

---


### 262. [Enhancing Target-Guided Proactive Dialogue Systems via Conversational Scenario Modeling and Intent-Keyword Bridging](https://arxiv.org/abs/2605.11964)

**<font color=#1a73e8>作者：</font>** Maodong Li, Yancui Li, Fang Kong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A target-guided proactive dialogue system aims to steer conversations proactively toward pre-defined targets, such as designated keywords or specific topics. During guided conversations, dynamically modeling conversational scenarios and intent keywords to guide system utterance generation is beneficial; however, existing work largely overlooks this aspect, resulting in a mismatch with the dynamics of real-world conversations. In this paper, we jointly model user profiles and domain knowledge as conversational scenarios to introduce a scenario bias that dynamically influences system utterances, and employ intent-keyword bridging to predict intent keywords for upcoming dialogue turns, providing higher level and more flexible guidance. Extensive automatic and human evaluations demonstrate the effectiveness of conversational scenario modeling and intent keyword bridging, yielding substantial improvements in proactivity, fluency, and informativeness for target-guided proactive dialogue systems, thereby narrowing the gap with real world interactions.

---


### 263. [H2G: Hierarchy-Aware Hyperbolic Grouping for 3D Scenes](https://arxiv.org/abs/2605.11967)

**<font color=#1a73e8>作者：</font>** ByungHa Ko, Youngmin Lee, Dong Hwan Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hierarchical 3D grouping aims to recover scene groups across multiple granularities, from fine object parts to complete objects, without relying on semantic labels or a fixed vocabulary. The main challenge is to transform 2D foundation-model cues into coherent hierarchy supervision and embed that hierarchy in a 3D representation. We propose H2G, a hyperbolic affinity field for hierarchical 3D grouping. Our method derives semantically organized tree supervision by interpreting foundation-model affinities through Dasgupta's objective for similarity-based hierarchical clustering. This supervision is distilled into a single Lorentz hyperbolic feature field, whose geometry is well suited for tree-like branching structures. A hierarchy-aware objective aligns the field with fine-level assignments, coarse object structure, compact feature clusters, and LCA (Lowest Common Ancestor) ordering. This formulation represents multiple grouping levels in one feature space, enabling semantic hierarchical grouping grounded in 2D foundation-model knowledge.

---


### 264. [NOFE -- Neural Operator Function Embedding](https://arxiv.org/abs/2605.11970)

**<font color=#1a73e8>作者：</font>** Lars Uebbing, Harald L. Joakimsen, Siyan Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most dimensionality reduction methods treat data as discrete point clouds, ignoring the continuous domain structure inherent to many real-world processes. To bridge this gap, we introduce Neural Operator Function Embedding (NOFE), a domain-aware framework for continuous dimensionality reduction. NOFE learns function-to-function mappings via a Graph Kernel Operator, enabling mesh-free evaluation at arbitrary query locations independent of input discretization. We establish NOFE as approximation of sheaf-to-sheaf mappings, generalizing Sheaf Neural Networks to continuous domains. We evaluate NOFE across different datasets, comparing it against PCA, t-SNE, and UMAP. Our results demonstrate that NOFE significantly outperforms baselines in local structure preservation, achieving a local Stress of 0.111 compared to 0.398 for PCA, 0.773 for t-SNE, and 0.791 for UMAP for the ERA5 climate reanalysis dataset. NOFE also exhibits robust sampling independence, reducing the Patch Stitching Error by up to $20.0\times$ relative to UMAP (59.0 vs. 267.6 under regional normalization) and ensuring consistency across disjoint domain patches. While maintaining competitive global structure preservation (Stress-1: 0.379 vs. PCA's 0.268), NOFE resolves fine-grained structures and produces smooth, consistent embeddings that generalize across varying sample densities, addressing key limitations of discrete reduction methods.

---


### 265. [Stochastic Minimum-Cost Reach-Avoid Reinforcement Learning](https://arxiv.org/abs/2605.11975)

**<font color=#1a73e8>作者：</font>** Jingduo Pan, Taoran Wu, Yiling Xue 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study stochastic minimum-cost reach-avoid reinforcement learning, where an agent must satisfy a reach-avoid specification with probability at least $p$ while minimizing expected cumulative costs in stochastic environments. Existing safe and constrained reinforcement learning methods typically fail to jointly enforce probabilistic reach-avoid constraints and optimize cost in the learning setting in stochastic environments. To address this challenge, we introduce reach-avoid probability certificates (RAPCs), which identify states from which stochastic reach-avoid constraints are satisfiable. Building on RAPCs, we develop a contraction-based Bellman formulation that serves as a principled surrogate for integrating reach-avoid considerations into reinforcement learning, enabling cost optimization under probabilistic constraints. We establish almost sure convergence of the proposed algorithms to locally optimal policies with respect to the resulting objective. Experiments in the MuJoCo simulator demonstrate improved cost performance and consistently higher reach-avoid satisfaction rates.

---


### 266. [Optimizing 4D Wires for Sparse 3D Abstraction](https://arxiv.org/abs/2605.11977)

**<font color=#1a73e8>作者：</font>** Dong-Yi Wu, Tong-Yee Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a unified framework for 3D geometric abstraction using a single continuous 4D wire, parameterized as a B-spline with spatial coordinates and variable width $(x,y,z,w)$. Existing approaches typically represent shapes as collections of many independent curve segments, which often leads to fragmented structures and limited physical realizability. In contrast, we show that a single continuous spline is sufficiently expressive to capture complex volumetric forms while enforcing global topological coherence. By imposing continuity, our method transforms 3D sketching from a local density-accumulation process into a global routing problem, providing a strong inductive bias toward cleaner aesthetics and improved structural coherence. To enable gradient-based optimization, we introduce a differentiable rendering pipeline that efficiently rasterizes variable-width curves with bounded projection error. This formulation supports robust optimization using modern guidance signals such as Score Distillation Sampling (SDS) or CLIP. We demonstrate applications including image-to-3D abstraction, multi-view wire art generation, and differentiable stylized surface filling. Experiments show that our unified representation produces structures with higher semantic fidelity and improved structural coherence compared to approaches based on collections of discrete curves.

---


### 267. [QDSB: Quantized Diffusion Schrödinger Bridges](https://arxiv.org/abs/2605.11983)

**<font color=#1a73e8>作者：</font>** Tobias Fuchs, Florian Kalinke, Nadja Klein  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning generative models in settings where the source and target distributions are only specified through unpaired samples is gaining in importance. Here, one frequently-used model are Schrödinger bridges (SB), which represent the most likely evolution between both endpoint distributions. To accelerate training, simulation-free SBs avoid the path simulation of the original SB models. However, learning simulation-free SBs requires paired data; a coupling of the source and target samples is obtained as the solution of the entropic optimal transport (OT) problem. As obtaining the optimal global coupling is infeasible in many practical cases, the entropic OT problem is iteratively solved on minibatches instead. Still, the repeated cost remains substantial and the locality can distort the global transport geometry. We propose quantized diffusion Schrödinger bridges (QDSB), which compute the endpoint coupling on anchor-quantized endpoint distributions and lift the resulting plan back to original data points through cell-wise sampling. We show that the regularized optimal coupling is stable w.r.t. anchor quantization, with an error controlled by the quality of the anchor approximation. In real-world experiments, QDSB matches the sample quality of existing baselines, requiring substantially less time. Code and data are available at this http URL.

---


### 268. [Random-Set Graph Neural Networks](https://arxiv.org/abs/2605.11987)

**<font color=#1a73e8>作者：</font>** Tommy Woodley, Shireen Kudukkil Manchingal, Matteo Tolloso 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Uncertainty quantification has become an important factor in understanding the data representations produced by Graph Neural Networks (GNNs). Despite their predictive capabilities being ever useful across industrial workspaces, the inherent uncertainty induced by the nature of the data is a huge mitigating factor to GNN performance. While aleatoric uncertainty is the result of noisy and incomplete stochastic data such as missing edges or over-smoothing, epistemic uncertainty arises from lack of knowledge about a system or model (e.g., a graph's topology or node feature representation), which can be reduced by gathering more data and information. In this paper, we propose an original new framework in which node-level epistemic uncertainty is modelled in a belief function (finite random set) formalism. The resulting Random-Set Graph Neural Networks have a belief-function head predicting a random set over the list of classes, from which both a precise probability prediction and a measure of epistemic uncertainty can be obtained. Extensive experiments on 9 different graph learning datasets, including real-world autonomous driving benchmarks as such Nuscene and ROAD, demonstrate RS-GNN's superior uncertainty quantification capabilities

---


### 269. [A Transfer Learning Evaluation of Deep Neural Networks for Image Classification](https://arxiv.org/abs/2605.11989)

**<font color=#1a73e8>作者：</font>** Nermeen Abou Baker, Nico Zengeler, Uwe Handmann  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transfer learning is a machine learning technique that uses previously acquired knowledge from a source domain to enhance learning in a target domain by reusing learned weights. This technique is ubiquitous because of its great advantages in achieving high performance while saving training time, memory, and effort in network design. In this paper, we investigate how to select the best pre-trained model that meets the target domain requirements for image classification tasks. In our study, we refined the output layers and general network parameters to apply the knowledge of eleven image processing models, pre-trained on ImageNet, to five different target domain datasets. We measured the accuracy, accuracy density, training time, and model size to evaluate the pre-trained models both in training sessions in one episode and with ten episodes.

---


### 270. [Towards Visually-Guided Movie Subtitle Translation for Indic Languages](https://arxiv.org/abs/2605.11993)

**<font color=#1a73e8>作者：</font>** Tarun Chintada, Kshetrimayum Boynao Singh, Asif Ekbal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Movie subtitle translation is inherently multimodal, yet text-only systems often miss visual cues needed to convey emotion, action, and social nuance, especially for low-resource Indic languages (English to Hindi, Bengali, Telugu, Tamil and Kannada). We present a case study on five full-length films and compare two lightweight visual grounding strategies: structured attribute summaries from a 5-minute sliding window and free-text summaries of inter-subtitle visual gaps. Our analysis shows that temporal misalignment between subtitles and frames is a major obstacle in long-form video, often rendering indiscriminate visual grounding ineffective. However, oracle selective grounding, which replaces only the lowest-quality 20-30\% of baseline segments with visual-enhanced outputs, consistently improves COMET over the text-only baseline while requiring far less visual processing. Among the two approaches, coarse attribute-based visual context summarization is more robust, capturing scene-level emotion and contextual subtle cues that text alone often misses

---


### 271. [A microservices-based endpoint monitoring platform with predictive NLP models for real-time security and hate-speech risk alerting](https://arxiv.org/abs/2605.11997)

**<font color=#1a73e8>作者：</font>** Darlan Noetzold, Anubis Graciela De Moraes Rossetto, Juan Francisco De Paz Santana 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Organizations increasingly depend on endpoint devices and corporate communication channels, yet they still face critical risks such as sensitive data leakage, suspicious user behavior, and the circulation of hateful or harmful language in workplace contexts. Current solutions frequently address these issues in isolation (e.g., productivity tracking, data loss prevention, or hate-speech detection), limiting correlation across signals and delaying incident response. This work proposes a unified, microservices-based platform that collects endpoint telemetry and applies predictive natural language processing models to support real-time security and compliance alerting. The architecture is modular and scalable, relying on RabbitMQ for event ingestion and routing and Redis for low-latency data access and alert delivery. For text classification, transformer-based models such as BERT are evaluated for hate-speech risk detection, achieving an average accuracy of 87\%. Experimental results indicate that the proposed platform can promptly surface indicators of data exfiltration and policy violations while centralizing alert management, providing an integrated framework that combines monitoring, security analytics, and predictive capabilities.

---


### 272. [Split the Differences, Pool the Rest: Provably Efficient Multi-Objective Imitation](https://arxiv.org/abs/2605.12000)

**<font color=#1a73e8>作者：</font>** Ziyad Sheebaelhamd, Luca Viano, Volkan Cevher 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work investigates multi-objective imitation learning: the problem of recovering policies that lie on the Pareto front given demonstrations from multiple Pareto-optimal experts in a Multi-Objective Markov Decision Process (MOMDP). Standard imitation approaches are ill-equipped for this regime, as naively aggregating conflicting expert trajectories can result in dominated policies. To address this, we introduce Multi-Output Augmented Behavioral Cloning (MA-BC), an algorithm that systematically partitions divergent expert data while pooling state-action pairs where no behavior conflict is observed. Theoretically, we prove that MA-BC converges to Pareto-optimal policies at a faster statistical rate than any learner that considers each expert dataset independently. Furthermore, we establish a novel lower bound for multi-objective imitation learning, demonstrating that MA-BC is minimax optimal. Finally, we empirically validate our algorithm across diverse discrete environments and, guided by our theoretical insights, extend and evaluate MA-BC on a continuous Linear Quadratic Regulator (LQR) control task.

---


### 273. [EDGER: EDge-Guided with HEatmap Refinement for Generalizable Image Forgery Localization](https://arxiv.org/abs/2605.12002)

**<font color=#1a73e8>作者：</font>** Minh-Khoa Le-Phan, Minh-Hoang Le, Minh-Triet Tran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-guided inpainting has made image forgery increasingly realistic, challenging both SID and IFL. However, existing methods often struggle to point out suspicious signals across domains. To address this problem, we propose EDGER, a patch-based, dual-branch framework that localizes manipulated regions in arbitrary resolution images without sacrificing native resolution. The first branch, Edge-Guided Segmentation, introduces a Frequency-based Edge Detector to emphasize high-frequency inconsistencies at manipulation boundaries, and fine-tunes a SegFormer to fuse RGB and edge features for pixel-level masks. Since edge evidence is most informative only when patches contain both authentic and manipulated pixels, we complement Edge-Guided Segmentation with a Synthetic Heatmapping branch, a classification-based localizer that fine-tunes a CLIP-ViT image encoder with LoRA to flag fully synthetic patches. Together, Synthetic Heatmapping provides coarse, patch-level synthetic priors, while Edge-Guided Segmentation sharpens boundaries within partially manipulated patches, yielding comprehensive localization. Evaluated in the MediaEval 2025, SynthIM challenge, Manipulated Region Localization Task's setting, our approach scales to multi-megapixel imagery and exhibits strong cross-domain generalization. Extensive ablations highlight the complementary roles of frequency-based edge cues and patch-level synthetic priors in driving accurate, resolution-agnostic localization.

---


### 274. [Robust Promptable Video Object Segmentation](https://arxiv.org/abs/2605.12006)

**<font color=#1a73e8>作者：</font>** Sohyun Lee, Yeho Gwon, Lukas Hoyer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The performance of promptable video object segmentation (PVOS) models substantially degrades under input corruptions, which prevents PVOS deployment in safety-critical domains. This paper offers the first comprehensive study on robust PVOS (RobustPVOS). We first construct a new, comprehensive benchmark with two real-world evaluation datasets of 351 video clips and more than 2,500 object masks under real-world adverse conditions. At the same time, we generate synthetic training data by applying diverse and temporally varying corruptions to existing VOS datasets. Moreover, we present a new RobustPVOS method, dubbed Memory-object-conditioned Gated-rank Adaptation (MoGA). The key to successfully performing RobustPVOS is two-fold: effectively handling object-specific degradation and ensuring temporal consistency in predictions. MoGA leverages object-specific representations maintained in memory across frames to condition the robustification process, which allows the model to handle each tracked object differently in a temporally consistent way. Extensive experiments on our benchmark validate MoGA's efficacy, showing consistent and significant improvements across diverse corruption types on both synthetic and real-world datasets, establishing a strong baseline for future RobustPVOS research. Our benchmark is publicly available at this https URL.

---


### 275. [Estimating Subgraph Importance with Structural Prior Domain Knowledge](https://arxiv.org/abs/2605.12009)

**<font color=#1a73e8>作者：</font>** Changhyun Kim, Seunghwan An, Jong-June Jeon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a subgraph importance estimation method for pretrained Graph Neural Networks (GNNs) on graph-level tasks, formulated as a linear Group Lasso regression problem in the embedding space. Our method effectively leverages prior domain knowledge of graph substructures, while remaining independent of the specific form of the output layer or readout function used in the GNN architecture, and it does not require access to ground-truth target labels. Experiments on real-world graph datasets demonstrate that our method consistently outperforms existing baselines in subgraph importance estimation. Furthermore, we extend our method to identify important nodes within the graph.

---


### 276. [Limits of Learning Linear Dynamics from Experiments](https://arxiv.org/abs/2605.12010)

**<font color=#1a73e8>作者：</font>** Aybüke Ulusarslan, Niki Kilbertus, Nora Schneider  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning governing dynamics from data is a common goal across the sciences, yet it is only well-posed when the underlying mechanisms are identifiable. In practice, many data-driven methods implicitly assume identifiability; when this assumption fails, estimated models can yield spurious predictions and invalid mechanistic conclusions. Classical identifiability guarantees for controlled linear time-invariant (LTI) systems provide sufficient conditions -- controllability and persistent excitation -- but leave open whether identifiability holds when these conditions fail, and which parts of the system remain identifiable without full identifiability. We show that the experimental setup, i.e., the realized initial state and control input, dictates a fundamental limit on the information recoverable from the observed trajectory. We develop a geometric characterization of this limit and derive a closed-form description of all systems consistent with the experimental setup. Crucially, we prove that even when the full system is not identifiable, the restricted dynamics on the subspace reachable by the experiment remain uniquely determined.

---


### 277. [L2P: Unlocking Latent Potential for Pixel Generation](https://arxiv.org/abs/2605.12013)

**<font color=#1a73e8>作者：</font>** Zhennan Chen, Junwei Zhu, Xu Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pixel diffusion models have recently regained attention for visual generation. However, training advanced pixel-space models from scratch demands prohibitive computational and data resources. To address this, we propose the Latent-to-Pixel (L2P) transfer paradigm, an efficient framework that directly harnesses the rich knowledge of pre-trained LDMs to build powerful pixel-space models. Specifically, L2P discards the VAE in favor of large-patch tokenization and freezes the source LDM's intermediate layers, exclusively training shallow layers to learn the latent-to-pixel transformation. By utilizing LDM-generated synthetic images as the sole training corpus, L2P fits an already smooth data manifold, enabling rapid convergence with zero real-data collection. This strategy allows L2P to seamlessly migrate massive latent priors to the pixel space using only 8 GPUs. Furthermore, eliminating the VAE memory bottleneck unlocks native 4K ultra-high resolution generation. Extensive experiments across mainstream LDM architectures show that L2P incurs negligible training overhead, yet performs on par with the source LDM on DPG-Bench and reaches 93% performance on GenEval.

---


### 278. [SkillSafetyBench: Evaluating Agent Safety under Skill-Facing Attack Surfaces](https://arxiv.org/abs/2605.12015)

**<font color=#1a73e8>作者：</font>** Chang Jin, An Wang, Zeming Wei 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Reusable skills are becoming a common interface for extending large language model agents, packaging procedural guidance with access to files, tools, memory, and execution environments. However, this modularity introduces attack surfaces that are largely missed by existing safety evaluations: even when the user request is benign, task-relevant skill materials or local artifacts can steer an agent toward unsafe actions. We present SkillSafetyBench, a runnable benchmark for evaluating such skill-mediated safety failures. SkillSafetyBench includes 155 adversarial cases across 47 tasks, 6 risk domains, and 30 safety categories, each evaluated with a case-specific rule-based verifier. Experiments with multiple CLI agents and model backends show that localized non-user attacks can consistently induce unsafe behavior, with distinct failure patterns across domains, attack methods, and scaffold-model pairings. Our findings suggest that agent safety depends not only on model-level alignment, but also on how agents interpret skills, trust workflow context, and act through executable environments.

---


### 279. [FAME: Feature Activation Map Explanation on Image Classification and Face Recognition](https://arxiv.org/abs/2605.12017)

**<font color=#1a73e8>作者：</font>** Xinyi Zhang, Manuel Günther  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep Learning has revolutionized machine learning, reaching unprecedented levels of accuracy, but at the cost of reduced interpretability. Especially in image processing systems, deep networks transform local pixel information into more global concepts in a highly obscured manner. Explainable AI methods for image processing try to shed light on this issue by highlighting the regions of the image that are important for the prediction task. Among these, Class Activation Mapping (CAM) and its gradient-based variants compute attributions based on the feature map and upscale them to the image resolution, assuming that feature map locations are influenced only by underlying regions. Perturbation-based methods, such as CorrRISE, on the other hand, try to provide pixel-level attributions by perturbing the input with fixed patches and checking how the output of the network changes. In this work, we propose Feature Activation Map Explanation (FAME), which combines both worlds by using network gradients to compute changes to the input image, manipulating it in a gradient-driven way rather than using fixed patches. We apply this technique on two common tasks, image classification and face recognition, and show that CAM's above-mentioned assumption does not hold for deeper networks. We qualitatively and quantitively show that FAME produces attribution maps that are competitive state-of-the-art systems. Our code is available: {\footnotesize this https URL.}

---


### 280. [What-Where Transformer: A Slot-Centric Visual Backbone for Concurrent Representation and Localization](https://arxiv.org/abs/2605.12021)

**<font color=#1a73e8>作者：</font>** Ryota Yoshihashi, Masahiro Kada, Satoshi Ikehata 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many image understanding tasks involve identifying what is present and where it appears. However, tasks that address where, such as object discovery, detection, and segmentation, are often considerably more complex than image classification, which primarily focuses on what. One possible reason is that classification-oriented backbones tend to emphasize semantic information about what, while implicitly entangling or suppressing information about where. In this work, we focus on an inductive bias termed what-where separation, which encourages models to represent object appearance and spatial location in a decomposed manner. To incorporate this bias throughout an attentive backbone in the style of Vision Transformer (ViT), we propose the What-Where Transformer (WWT). Our method introduces two key novel designs: (1) it treats tokens as representations of what and attention maps as representations of where, and processes them in concurrent feed-forward modules via a multi-stream, slot-based architecture; (2) it reuses both the final-layer tokens and attention maps for downstream tasks, and directly exposes them to gradients derived from task losses, thereby facilitating more effective and explicit learning of localization. We demonstrate that even under standard single-label classification-based supervision on ImageNet, WWT exhibits emergent multiple object discovery directly from raw attention maps, rather than via additional postprocessing such as token clustering. Furthermore, WWT achieves superior performance compared to ViT-based methods on zero-shot object discovery and weakly supervised semantic segmentation, and it is transferable to various localization setups with minimal modifications. Code will be published after acceptance.

---


### 281. [Approximation Theory of Laplacian-Based Neural Operators for Reaction-Diffusion System](https://arxiv.org/abs/2605.12025)

**<font color=#1a73e8>作者：</font>** Takashi Furuya, Ryo Ozawa, Jenn-Nan Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators provide a framework for learning solution operators of partial differential equations (PDEs), enabling efficient surrogate modeling for complex systems. While universal approximation results are now well understood, approximation analysis specific to nonlinear reaction-diffusion systems remains limited. In this paper, we study neural operators applied to the solution mapping from initial conditions to time-dependent solutions of a generalized Gierer-Meinhardt reaction-diffusion system, a prototypical model of nonlinear pattern formation. Our main results establish explicit approximation error bounds in terms of network depth, width, and spectral rank by exploiting the Laplacian spectral representation of the Green's function underlying the PDE. We show that the required parameter complexity grows at most polynomially with respect to the target accuracy, demonstrating that Laplacian eigenfunction-based neural operator architectures alleviate the curse of parametric complexity encountered in generic operator learning. Numerical experiments on the Gierer-Meinhardt system support the theoretical findings.

---


### 282. [Spectral Vision Transformer for Efficient Tokenization with Limited Data](https://arxiv.org/abs/2605.12026)

**<font color=#1a73e8>作者：</font>** Alexandra G. Roberts, Maneesh John, Jinwei Zhang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a novel spectral vision transformer architecture for efficient tokenization in limited data, with an emphasis on medical imaging. We outline convenient theoretical properties arising from the choice of basis including spatial invariance and optimal signal-to-noise ratio. We show reduced complexity arising from the spectral projection compared to spatial vision transformers. We show equitable or superior performance with a reduced number of parameters as compared to a variety of models including compact and standard vision transformers, convolutional neural networks with attention, shifted window transformers, multi-layer perceptrons, and logistic regression. We include simulated, public, and clinical data in our analysis and release our code at: \verb+this http URL.

---


### 283. [4DVGGT-D: 4D Visual Geometry Transformer with Improved Dynamic Depth Estimation](https://arxiv.org/abs/2605.12027)

**<font color=#1a73e8>作者：</font>** Ying Zang, Xuanyi Liu, Yidong Han 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing dynamic 4D scenes from monocular videos is a fundamental yet challenging task. While recent 3D foundation models provide strong geometric priors, their performance significantly degrades in dynamic environments. This degradation stems from a fundamental tension: the inherent coupling of camera ego-motion and object motion within global attention mechanisms. In this paper, we propose a novel, training-free progressive decoupling framework that disentangles dynamics from statics in a principled, coarse-to-fine manner. Our core insight is to resolve the tension by first stabilizing the camera pose, followed by geometric refinement. Specifically, our approach consists of three synergistic components: (1) a Dynamic-Mask-Guided Pose Decoupling module that isolates pose estimation from dynamic interference, yielding a stable motion-free reference frame; (2) a Topological Subspace Surgery mechanism that orthogonally decomposes the depth manifold, safely preserving dynamic objects while injecting refined, mask-aware geometry into static regions; and (3) an Information-Theoretic Confidence-Aware Fusion strategy that formulates depth integration as a heteroscedastic Bayesian inference problem, adaptively blending multi-pass predictions via inverse-variance weighting. Extensive experiments on standard 4D reconstruction benchmarks demonstrate that our method achieves consistent and substantial improvements across principal point-cloud metrics. Notably, our approach shows competitive performance in robust 4D scene reconstruction without requiring fine-tuning, suggesting the potential of mathematically grounded dynamic-static disentanglement.

---


### 284. [Caraman at SemEval-2026 Task 8: Three-Stage Multi-Turn Retrieval with Query Rewriting, Hybrid Search, and Cross-Encoder Reranking](https://arxiv.org/abs/2605.12028)

**<font color=#1a73e8>作者：</font>** David-Maximilian Caraman, Gheorghe Cosmin Silaghi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We describe our system for SemEval-2026 Task 8 (MTRAGEval), participating in Task A (Retrieval) across four English-language domains. Our approach employs a three-stage pipeline: (1) query rewriting via a LoRA-fine-tuned Qwen 2.5 7B model that transforms context-dependent follow-up questions into standalone queries, (2) hybrid BM25 and dense retrieval combined through Reciprocal Rank Fusion, and (3) cross-encoder reranking with BGE-reranker-v2-m3. On the official test set, the system achieves nDCG@5 of 0.531, ranking 8th out of 38 participating systems and 10.7% above the organizer baseline. Development comparisons reveal that domain-specific temperature tuning for query generation, where technical domains benefit from deterministic decoding and general domains from controlled randomness, provides consistent gains, while more complex strategies such as domain-aware prompting and multi-query expansion degrade performance.

---


### 285. [OmniHumanoid: Streaming Cross-Embodiment Video Generation with Paired-Free Adaptation](https://arxiv.org/abs/2605.12038)

**<font color=#1a73e8>作者：</font>** Yiren Song, Xiyao Deng, Pei Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-embodiment video generation aims to transfer motions across different humanoid embodiments, such as human-to-robot and robot-to-robot, enabling scalable data generation for embodied intelligence. A major challenge in this setting is that motion dynamics are partly transferable across embodiments, whereas appearance and morphology remain embodiment-specific. Existing approaches often entangle these factors, and many require paired data for every target embodiment, which limits scalability to new robots. We present OmniHumanoid, a framework that factorizes transferable motion learning and embodiment-specific adaptation. Our method learns a shared motion transfer model from motion-aligned paired videos spanning multiple embodiments, while adapting to a new embodiment using only unpaired videos through lightweight embodiment-specific adapters. To reduce interference between motion transfer and embodiment adaptation, we further introduce a branch-isolated attention design that separates motion conditioning from embodiment-specific modulation. In addition, we construct a synthetic cross-embodiment dataset with motion-aligned paired videos rendered across diverse humanoid assets, scenes, and viewpoints. Experiments on both synthetic and real-world benchmarks show that OmniHumanoid achieves strong motion fidelity and embodiment consistency, while enabling scalable adaptation to unseen humanoid embodiments without retraining the shared motion model.

---


### 286. [SkillGraph: Skill-Augmented Reinforcement Learning for Agents via Evolving Skill Graphs](https://arxiv.org/abs/2605.12039)

**<font color=#1a73e8>作者：</font>** Xiaoyuan Li, Moxin Li, Keqin Bao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Skill libraries enable large language model agents to reuse experience from past interactions, but most existing libraries store skills as isolated entries and retrieve them only by semantic similarity. This leads to two key challenges for compositional tasks. Firstly, an agent must identify not only relevant skills but also how they depend on and build upon each other. Secondly, it also makes library maintenance difficult, since the system lacks structural cues for deciding when skills should be merged, split, or removed. We propose SKILLGRAPH, a framework that represents reusable skills as nodes in a directed graph, with typed edges encoding prerequisite, enhancement, and co-occurrence relations. Given a new task, SKILLGRAPH retrieves not just individual skills, but an ordered skill subgraph that can guide multi-step decision making. The graph is continuously updated from agent trajectories and reinforcement learning feedback, allowing both the skill library and the agent policy to improve together. Experiments on ALFWorld, WebShop, and seven search-augmented QA tasks show that SKILLGRAPH achieves state-of-the-art performance against memory-augmented RL methods, with especially large gains on complex tasks that require composing multiple skills.

---


### 287. [Is Child-Directed Language Optimized for Word Learning? A Computational Study of Verb Meaning Acquisition](https://arxiv.org/abs/2605.12047)

**<font color=#1a73e8>作者：</font>** Francesca Padovani, Jaap Jumelet, Yevgen Matusevych 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Is child-directed language (CDL) optimized to support language learning, and which aspects of linguistic development does it facilitate? We investigate this question using neural language models trained on CDL versus adult-directed language (ADL). We selectively remove syntactic or lexical co-occurrence information from the model training data, and evaluate the impact of these manipulations on verb meaning acquisition. While disrupting syntax impairs learning across all datasets, models trained on CDL and spoken ADL show significantly higher resilience than those trained on written input. Tracking semantic and syntactic performance over training, we observe a semantic-first trajectory, with verb meanings emerging prior to robust syntactic proficiency, an asynchrony most pronounced in the spoken domain, especially CDL. These results suggest that the advantage for verb learning previously attributed to CDL may instead reflect broader properties of the spoken register, rather than a uniquely CDL-specific optimization.

---


### 288. [Scaling Laws and Tradeoffs in Recurrent Networks of Expressive Neurons](https://arxiv.org/abs/2605.12049)

**<font color=#1a73e8>作者：</font>** Aaron Spieler, Georg Martius, Anna Levina  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cortical neurons are complex, multi-timescale processors wired into recurrent circuits, shaped by long evolutionary pressure under stringent biological constraints. Mainstream machine learning, by contrast, predominantly builds models from extremely simple units, a default inherited from early neural-network theory. We treat this as a normative architectural question. How should one split a fixed parameter budget $P$ between the number of units $N$, per-unit effective complexity $k_e$, and per-unit connectivity $k_c$? What controls the optimal allocation? This calls for a model in which per-unit complexity can be tuned independently of width and connectivity. Accordingly, we introduce the ELM Network, whose recurrent layer is built from Expressive Leaky Memory (ELM) neurons, chosen to mirror functional components of cortical neurons. The architecture allows for individually adjusting $N$, $k_e$, and $k_c$ and trains stably across orders of magnitude in scale. We evaluate the model on two qualitatively different sequence benchmarks: the neuromorphic SHD-Adding task and Enwik8 character-level language modeling. Performance improves monotonically along each of the three axes individually. Under a fixed budget, a clear non-trivial optimum emerges in their tradeoff, and larger budgets favor both more and more complex neurons. A closed-form information-theoretic model captures these tradeoffs and attributes the diminishing returns at two ends to: per-neuron signal-to-noise saturation and across-neuron redundancy. A hyperparameter sweep spanning three orders of magnitude in trainable parameters traces a near-Pareto-frontier scaling law consistent with the framework. This suggests that the simple-unit default in ML is not obviously optimal once this tradeoff surface is probed, and offers a normative lens on cortex's reliance on complex spatio-temporal integrators.

---


### 289. [Learning plug-in surrogate endpoints for randomized experiments](https://arxiv.org/abs/2605.12051)

**<font color=#1a73e8>作者：</font>** Alessandro-Umberto Margueritte, Ahmet Zahid Balcıoğlu, Jesse Krijthe 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Surrogate endpoints are used in place of long-term outcomes in randomized experiments when observing the real outcome for a large enough cohort is prohibitively expensive or impractical. A short-term surrogate is good if the result of an experiment using the surrogate is predictive of the result of a hypothetical study using the real outcome. Much attention has been paid to formalizing this property in causal terms, but most criteria are unidentifiable and cannot be turned into practical algorithms for learning surrogate endpoints from data. To address this, we study plug-in composite surrogates, functions of post-treatment variables that may be substituted directly for the primary outcome in a randomized experiment. We propose two methods for learning plug-in surrogates that maximize effect predictiveness, and characterize the possibility of finding endpoints that yield unbiased effect estimates in representative scenarios. Finally, in both synthetic experiments with known effects and in data from a real-world experiment, we find that our method, based on directly modeling the surrogate effect, returns plug-in endpoints more predictive of the primary effect than established methods.

---


### 290. [Hölder Policy Optimisation](https://arxiv.org/abs/2605.12058)

**<font color=#1a73e8>作者：</font>** Yuxiang Chen, Dingli Liang, Yihang Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group Relative Policy Optimisation (GRPO) enhances large language models by estimating advantages across a group of sampled trajectories. However, mapping these trajectory-level advantages to policy updates requires aggregating token-level probabilities within each sequence. Relying on a fixed aggregation mechanism for this step fundamentally limits the algorithm's adaptability. Empirically, we observe a critical trade-off: certain fixed aggregations frequently suffer from training collapse, while others fail to yield satisfactory performance. To resolve this, we propose \textbf{HölderPO}, a generalised policy optimisation framework unifying token-level probability aggregation via the Hölder mean. By explicitly modulating the parameter $p$, our framework provides continuous control over the trade-off between gradient concentration and variance bounds. Theoretically, we prove that a larger $p$ concentrates the gradient to amplify sparse learning signals, whereas a smaller $p$ strictly bounds gradient variance. Because no static configuration can universally resolve this concentration-stability trade-off, we instantiate the framework with a dynamic annealing algorithm that progressively schedules $p$ across the training lifecycle. Extensive evaluations demonstrate superior stability and convergence over existing baselines. Specifically, our approach achieves a state-of-the-art average accuracy of $54.9\%$ across multiple mathematical benchmarks, yielding a substantial $7.2\%$ relative gain over standard GRPO and secures an exceptional $93.8\%$ success rate on ALFWorld.

---


### 291. [RoboBlockly Studio: Conversational Block Programming with Embodied Robot Feedback for Computational Thinking](https://arxiv.org/abs/2605.12059)

**<font color=#1a73e8>作者：</font>** Leyi Li, Chenyu Du, Jiafei Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Computational thinking (CT) is increasingly promoted as a core literacy, yet learners and teachers face challenges in connecting abstract program logic to meaningful outcomes. We design and evaluate RoboBlockly Studio, an integrated interactive system that combines block-based programming, a conversational AI teaching agent, and embodied robot execution. RoboBlockly Studio creates a tight iterative loop of authoring, running, observing, and revising. Informed by interviews with five programming teachers, the system was designed to support four goals: (1) preserving learner agency in computational thinking, (2) making program behavior transparent and interpretable, (3) grounding programming in embodied, classroom-aligned tasks, and (4) scaffolding reflection through pedagogically grounded AI dialogue. We deployed RoboBlockly Studio with 32 high school students, observing how robot and AI feedback influenced students' interactions with code, reflections on problem-solving strategies, and understanding of CT concepts. We discuss design insights and implications for creating interactive, embodied learning environments that integrate AI and robotics to support CT learning in computing education.

---


### 292. [TAR: Text Semantic Assisted Cross-modal Image Registration Framework for Optical and SAR Images](https://arxiv.org/abs/2605.12064)

**<font color=#1a73e8>作者：</font>** Zhuoyu Cai, Dou Quan, Ning Huyan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing deep learning-based methods can capture shared features from optical and synthetic aperture radar (SAR) images for spatial alignment. However, optical-SAR registration remains challenging under large geometric deformations, because the model needs to simultaneously handle cross-modal appearance discrepancies and complex spatial transformations. To address this issue, this paper proposes a text semantic-assisted cross-modal image registration framework, named TAR, for optical and SAR images. TAR exploits text semantic priors from remote sensing scenes and land-cover categories to alleviate the modality gap and enhance cross-modal feature learning. TAR consists of three components: a multi-scale visual feature learning (MSFL) module, a text-assisted feature enhancement (TAFE) module, and a coarse-to-fine dense matching (CFDM) module. MSFL extracts multi-scale visual features from optical and SAR images. TAFE constructs text descriptors related to remote sensing scenes and land-cover objects, and uses a frozen RemoteCLIP text encoder to extract text features. These text features are introduced through visual-text interaction to enhance high-level visual features for more reliable coarse matching. CFDM then establishes coarse correspondences based on the enhanced high-level features and refines the matched locations using low-level features. Experimental results on cross-modal remote sensing images demonstrate the effectiveness of TAR, which achieves stronger matching performance than several state-of-the-art methods and yields significant gains under large geometric deformations.

---


### 293. [Anomaly-Aware Vision-Language Adapters for Zero-Shot Anomaly Detection](https://arxiv.org/abs/2605.12069)

**<font color=#1a73e8>作者：</font>** Muhammad Aqeel, Maham Nazir, Uzair Khan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot anomaly detection aims to identify defects in unseen categories without target-specific training. Existing methods usually apply the same feature transformation to all samples, treating normal and anomalous data uniformly despite their fundamentally asymmetric distributions, compact normals versus diverse anomalies. We instead exploit this natural asymmetry by proposing AVA-DINO, an anomaly-aware vision-language adaptation framework with dual specialized branches for normal and anomalous patterns that adapt frozen DINOv3 visual features. During training on auxiliary data, the two branches are learned jointly with a text-guided routing mechanism and explicit routing regularization that encourages branch specialization. At test time, only the input image and fixed, predefined language descriptions are used to dynamically combine the two branches, enabling an asymmetric activation. This design prevents degenerate uniform routing and allows context-specific feature transformations. Experiments across nine industrial and medical benchmarks demonstrate state-of-the-art performance, achieving 93.5% image-AUROC on MVTec-AD and strong cross-domain generalization to medical imaging without domain-specific fine-tuning. this https URL

---


### 294. [PairDropGS: Paired Dropout-Induced Consistency Regularization for Sparse-View Gaussian Splatting](https://arxiv.org/abs/2605.12072)

**<font color=#1a73e8>作者：</font>** Hantang Li, Qiang Zhu, Xiandong Meng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dropout-based sparse-view 3D Gaussian Splatting (3DGS) methods alleviate overfitting by randomly suppressing Gaussian primitives during training. Existing methods mainly focus on designing increasingly sophisticated dropout strategies, while they overlook the resulting inconsistencies among different dropped Gaussian subsets. This oversight often leads to unstable reconstruction and suboptimal Gaussian representation this http URL this paper, we revisit dropout-based sparse-view 3DGS from a consistency regularization perspective and propose PairDropGS, a Paired Dropout-induced Consistency Regularization framework for sparse-view Gaussian splatting. Specifically, PairDropGS first constructs a pair of the dropped Gaussian subsets from a shared Gaussian field and designs a low-frequency consistency regularization to constrain their low-frequency rendered structures. This design encourages the shared Gaussian field to preserve stable scene layout and coarse geometry under different random dropouts, while avoiding excessive constraints on ambiguous high-frequency details. Moreover, we introduce a progressive consistency scheduling strategy to gradually strengthen the consistency regularization during training for stability and robustness of reconstruction. Extensive experiments on widely-used sparse-view benchmarks demonstrate that PairDropGS achieves superior training stability, significantly outperforms existing dropout-based 3DGS methods in reconstruction quality, while exhibiting the simplicity and plug-and-play nature for improving dropout-based optimization.

---


### 295. [BARISTA: A Multi-Task Egocentric Benchmark for Compositional Visual Understanding](https://arxiv.org/abs/2605.12074)

**<font color=#1a73e8>作者：</font>** Patrick Knab, Orgest Xhelili, Inis Buzi 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scene understanding is central to general physical intelligence, and video is a primary modality for capturing both state and temporal dynamics of a scene. Yet understanding physical processes remains difficult, as models must combine object localization, hand-object interactions, relational parsing, temporal reasoning, and step-level procedural inference. Existing benchmarks usually evaluate these capabilities separately, limiting diagnosis of why models fail on procedural tasks. We introduce BARISTA, a densely annotated egocentric dataset and benchmark of 185 real-world coffee-preparation videos covering fully automatic, portafilter-based, and capsule-based workflows. BARISTA provides verified per-frame scene graphs linking persistent object identities to masks, tracks, boxes, attributes, typed relations, hand-object interactions, activities, and process steps. From these graphs, we derive zero-shot language-based tasks spanning phrase grounding, hand-object interaction recognition, referring, activity recognition, relation extraction, and temporal visual question answering. Experiments reveal strong variation across task families and no consistently dominant model family, positioning BARISTA as a challenging diagnostic benchmark for procedural video understanding. Code and dataset available at this https URL.

---


### 296. [The Deepfakes We Missed: We Built Detectors for a Threat That Didn't Arrive](https://arxiv.org/abs/2605.12075)

**<font color=#1a73e8>作者：</font>** Shaina Raza  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Nearly a decade of Machine Learning (ML) research on deepfake detection has been organized around a threat model inherited from 2017--2019, revolving around face-swap and talking-head manipulation of public figures, motivated by concerns about large-scale misinformation and video-evidence fraud. This position paper argues that the threat the field prepared for did not arrive, and the threats that did arrive are substantially different. An accounting of deepfake incidents in 2022--2026 shows that the dominant observed harms are peer-generated Non-Consensual Intimate Imagery (NCII), voice-clone scam calls targeting families and finance workers, and emotional-manipulation fraud. The predicted large-scale public-figure deepfake catastrophe did not materialize during the 2024 global information environment despite extensive preparation. Meanwhile, research effort, benchmarks, and detection methods remain concentrated on the inherited threat model. The central claim of this paper is that this misalignment is now the dominant bottleneck on real-world deepfake defense, not model capability. We argue the ML research community should substantially rebalance its research agenda toward the harm categories that are actually growing. We support this position with empirical accounting of research effort and harm distribution, identify the structural reasons the misalignment persists, and outline three concrete technical research agendas for the under-defended harm categories.

---


### 297. [Elicitation-Augmented Bayesian Optimization](https://arxiv.org/abs/2605.12079)

**<font color=#1a73e8>作者：</font>** Alvar Haltia, Ville Hyvönen, Samuel Kaski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Human-in-the-loop Bayesian optimization (HITL BO) methods utilize human expertise to improve the sample-efficiency of BO. Most HITL BO methods assume that a domain expert can quantify their knowledge, for instance by pinpointing query locations or specifying their prior beliefs about the location of the maximum as a probability distribution. However, since human expertise is often tacit and cannot be explicitly quantified, we consider a setting where domain knowledge of an expert is elicited via pairwise comparisons of designs. We interpret the expert's pairwise judgements as noisy evidence about the values of the observable objective function and develop a principled method for combining the information obtained via direct observations and pairwise queries. Specifically, we derive a cost-aware value-of-information acquisition function that balances direct observations against pairwise queries. The proposed method approaches the convex hull of the trajectories of the individual information sources: when pairwise queries are cheap it substantially improves sample-efficiency over observation-only BO, and when pairwise queries are costly or noisy, it recovers the performance of standard BO by relying on direct observations alone.

---


### 298. [UniCustom: Unified Visual Conditioning for Multi-Reference Image Generation](https://arxiv.org/abs/2605.12088)

**<font color=#1a73e8>作者：</font>** Yiyan Xu, Qiulin Wang, Wenjie Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-reference image generation aims to synthesize images from textual instructions while faithfully preserving subject identities from multiple reference images. Existing VLM-enhanced diffusion models commonly rely on decoupled visual conditioning: semantic ViT features are processed by the VLM for instruction understanding, whereas appearance-rich VAE features are injected later into the diffusion backbone. Despite its intuitive design, this separation makes it difficult for the model to associate each semantically grounded subject with visual details from the correct reference image. As a result, the model may recognize which subject is being referred to, but fail to preserve its identity and fine-grained appearance, leading to attribute leakage and cross-reference confusion in complex multi-reference settings. To address this issue, we propose UniCustom, a unified visual conditioning framework that fuses ViT and VAE features before VLM encoding. This early fusion exposes the VLM to both semantic cues and appearance-rich details, enabling its hidden states to jointly encode the referred subject and corresponding visual appearance with only a lightweight linear fusion layer. To learn such unified representations, we adopt a two-stage training strategy: reconstruction-oriented pretraining that preserves reference-specific appearance details in the fused hidden states, followed by supervised finetuning on single- and multi-reference generation tasks. We further introduce a slot-wise binding regularization that encourages each image slot to preserve low-level details of its corresponding reference, thereby reducing cross-reference entanglement. Experiments on two multi-reference generation benchmarks demonstrate that UniCustom consistently improves subject consistency, instruction following, and compositional fidelity over strong baselines.

---


### 299. [Sign Language Recognition and Translation for Low-Resource Languages: Challenges and Pathways Forward](https://arxiv.org/abs/2605.12096)

**<font color=#1a73e8>作者：</font>** Nigar Alishzade, Gulchin Abdullayeva  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sign languages are natural, visual-gestural languages used by Deaf communities worldwide. Over 300 distinct sign languages remain severely low-resource due to limited documentation, sparse datasets, and insufficient computational tools. This systematic review synthesizes literature on sign language recognition and translation for under-resourced languages, using Azerbaijan Sign Language (AzSL) as a case study. Analysis of global initiatives extracts eight actionable lessons, including community co-design, dialectal diversity capture, and privacy-preserving pose-based representations. Turkic sign languages (Kazakh, Turkish, Azerbaijani) receive special attention, as linguistic proximity enables effective transfer learning. We propose three paradigm shifts: from architecture-centric to data-centric AI, from signer-independent to signer-adaptive systems, and from reference-based to task-specific evaluation metrics. A technical roadmap for AzSL leverages lightweight MediaPipe-based architectures, community-validated annotations, and offline-first deployment. Progress requires sustained interdisciplinary collaboration centered on Deaf communities to ensure cultural authenticity, ethical governance, and practical communication benefit.

---


### 300. [Adaptive Multi-Round Allocation with Stochastic Arrivals](https://arxiv.org/abs/2605.12111)

**<font color=#1a73e8>作者：</font>** Yuqi Pan, Davin Choo, Haichuan Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study a sequential resource allocation problem motivated by adaptive network recruitment, in which a limited budget of identical resources must be allocated over multiple rounds to individuals with stochastic referral capacity. Successful referrals endogenously generate future decision opportunities while allocating additional resources to an individual exhibits diminishing returns. We first show that the single-round allocation problem admits an exact greedy solution based on marginal survival probabilities. In the multi-round setting, the resulting Bellman recursion is intractable due to the stochastic, high-dimensional evolution of the frontier. To address this, we introduce a population-level surrogate value function that depends only on the remaining budget and frontier size. This surrogate enables an exact dynamic program via truncated probability generating functions, yielding a planning algorithm with polynomial complexity in the total budget. We further analyze robustness under model misspecification, proving a multi-round error bound that decomposes into a tight single-round frontier error and a population-level transition error. Finally, we evaluate our method on real-world inspired recruitment scenarios.

---


> [!TIP]
> 当前位于：**251-300**（第 6/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-396](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
