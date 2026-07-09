# 📦 其他研究 | 2026年07月10日

> 本类共 **207** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-207](./part-05.md)

---

### 151. [Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors](https://arxiv.org/abs/2607.07368)

**<font color=#1a73e8>作者：</font>** Oliver Makins, Orazio Angelini, Zohreh Shams 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI control is a family of techniques to prevent an AI with malicious goals from subverting its operator's intent. AI Control usually studies a single agent in one trajectory, but real deployments run many agents over shared infrastructure, and the most severe risks (model-weight exfiltration, training-run poisoning) plausibly need several agents acting in concert. We initiate the empirical study of multi-agent AI control, formalising distributed attacks in which several agents jointly aim for a malicious goal. We develop FakeLab: a synthetic AI-lab codebase (9 services, 86 benign tasks, 4 attack objectives). We evaluate single agent monitoring against distributed attacks, varying the number of agents, their coordination, model capabilities and precise monitoring configuration.
Our central finding is the fragmentation effect: as more agents coordinate to attack, per-agent monitoring becomes less likely to catch any of the attackers. Secondly, this is not driven by the ratio of benign to malicious code -- we argue this is likely dependent on model capability. Third, an explicit planner amplifies the fragmentation effect, raises the rate of completing the attack up to sevenfold, and mildly sharpens executors' poor monitor-theory-of-mind. Finally: a weak "trusted" monitor misses most attacks, while a stronger one cuts undetected success by more than an order of magnitude but remains imperfect. We are happy to share FakeLab, our control setting, with safety researchers on request.

---


### 152. [zk-ScalHard: Scalable and Hardware-Rooted Privacy-Preserving Authentication for Secure OTA Updates in Zonal SDVs](https://arxiv.org/abs/2607.07371)

**<font color=#1a73e8>作者：</font>** Shrikant Tangade, Bansi Pambhar, Valeria Loscri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The automotive industry is transitioning to Zonal-oriented Architectures (ZoA) for Software-Defined Vehicles (SDVs), enabling frequent over-the-air (OTA) updates for 100+ Electronic Control Units (ECUs). While OTA updates improve efficiency, they introduce safety-critical security risks. Current standards like Uptane and AUTOSAR Adaptive rely on Public-Key Infrastructure (PKI). However, PKI-based authentication creates bandwidth bottlenecks in in-vehicle and vehicle-to-cloud (V2I) communication as ECU density increases. It also risks exposing sensitive vehicle configurations and passenger privacy due to centralized architectures. Next-generation Zonal SDVs require decentralized, scalable authentication with data privacy. To address this, we propose zk-ScalHard, a hardware-rooted, privacy-preserving authentication protocol. We introduce a decentralized, hierarchical trust-promotion model utilizing Silicon Physical Unclonable Functions (PUFs) and two novel Zero-Knowledge Proof (ZKP) circuits: (1) Zonal Identity and Integrity (ZIDI) and (2) High-Performance Computing Aggregation (HPCA). These circuits employ multi-party computation (MPC) and recursive aggregation to achieve decentralization and scalability. The integration of ZKPs and PUFs ensures 100% vehicle-level data sovereignty. Benchmarked against Uptane, zk-ScalHard achieves constant O(1) communication and verification complexity, improving upon the linear O(n) complexity of current systems. Evaluation shows a 99.2% reduction in authentication bandwidth and a 99.9% reduction in the temporal attack surface. Our results demonstrate that zk-ScalHard provides a scalable, secure, and GDPR-compliant architecture for future Zonal SDVs.

---


### 153. [Sparse Delta Memory: Scaling the State of Linear RNNs through Sparsity](https://arxiv.org/abs/2607.07386)

**<font color=#1a73e8>作者：</font>** Loïc Cabannes, Pierre-Emmanuel Mazaré, Gergely Szilvasy 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear attention models allow a fixed state size and a fixed amount of compute per token. However, due to their limited state size, linear attention models fall behind in long-context recall compared to softmax-attention-based transformer architectures. Increasing the state size of linear attention improves recall performance but at the cost of higher FLOPs. In this work, we introduce Sparse Delta Memory (SDM), an architecture that scales the hidden state of gated linear RNNs to orders of magnitude higher capacity using a sparse addressing scheme. SDM extends the Gated DeltaNet architecture by replacing the dense key-value outer product with sparse reads and writes to a large explicit memory. We show that, under an isoFLOP constraint and with an identical number of parameters, a higher state memory capacity significantly improves performance on in-context learning and long-context retrieval tasks. Moreover, by learning the initial state of the SDM memory and therefore using it as a parametric memory, we show that the model further improves on a wide range of common-knowledge and reasoning tasks.

---


### 154. [MIRA-Math: A Benchmark for Minimal Information Requesting and Mathematical Reasoning](https://arxiv.org/abs/2607.07391)

**<font color=#1a73e8>作者：</font>** Charbel Al Bateh, Samer Saab Jr  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mathematical reasoning benchmarks typically provide all facts needed to solve each problem, while interactive benchmarks often mix reasoning with tools, retrieval, and long-horizon dialogue. We introduce MIRA-Math, a benchmark for a narrower diagnostic capability: solving mathematical problems whose full latent state has a unique answer, but whose solver-facing view is missing exactly one necessary atomic fact. The solver must request the missing information in natural language under a strict budget and then integrate the returned fact into an exact final answer. A fixed constrained LLM responder sees only the dataset-provided atomic fact and must either offer the quoted fact when the request matches it, or decline otherwise. Thus, instance generation, typed hint specifications, validation, and final-answer verification are deterministic, while request metrics are measured under a fixed LLM-mediated responder channel. MIRA-Math contains 2{,}310 generated instances from 22 typed mathematical families spanning algebra, probability, linear systems, discrete structures, signal processing, Markov chains, circuits, interpolation, and numerical boundary-value problems. Experiments across frontier and small models show that request success and final-answer accuracy are separable: models may ask for the right fact yet fail the downstream computation, or fail before obtaining the canonical hint. We release generators, verifiers, prompts, run metadata, and dataset documentation to support reproducible evaluation of minimal information requesting in mathematical reasoning.

---


### 155. [Transformer-based segmentation of prosodic boundaries in Brazilian Portuguese](https://arxiv.org/abs/2607.07408)

**<font color=#1a73e8>作者：</font>** Rodrigo de Freitas Lima, Julio Cesar Galdino, Marcos Vinicius Treviso  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic prosodic segmentation identifies boundaries between speech units from acoustic and linguistic evidence. Although recent deep learning approaches have produced strong results for English, automatic segmentation for Brazilian Portuguese (BP) still relies mostly on rule-based or traditional machine-learning methods. This paper presents SAMPA, a Whisper-based segmenter that transcribes BP speech while inserting explicit markers for terminal prosodic boundaries. We fine-tune Whisper large-v3 on manually segmented recordings from the NURC-SP dataset and evaluate different training and test-time filtering configurations, including out-of-distribution testing on the MuPe-Diversidades dataset. SAMPA achieves competitive boundary-detection performance across settings, with the best models reaching F1=0.731 on the held-out test split and F1=0.796 on MuPe-Diversidades. Finally, through n-gram and acoustic-visual analyses, we show that our model follows morphosyntactic, semantic, and prosodic cues for detecting prosodic boundaries.

---


### 156. [DeLS-Spec: Decoupled Long-Short Contexts for Parallel Speculative Drafting](https://arxiv.org/abs/2607.07409)

**<font color=#1a73e8>作者：</font>** Hong-Kai Zheng, Piji Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates LLM inference by drafting multiple tokens and verifying them in parallel. Block-parallel drafters such as DFlash further improve drafting efficiency by predicting an entire block in one pass, but their position-wise predictions lack explicit intra-block causal conditioning. Recent methods such as Domino and DSpark attempt to introduce such causality into block-parallel drafting, but they require training the draft model from scratch, which limits their flexibility and increases training cost. We propose DeLS-Spec, a decoupled long-short context speculative decoding method. DeLS-Spec treats the fixed DFlash model as a long-context expert and introduces a lightweight local head as a short-context expert. The local head can be trained independently with a standard next-token prediction objective, without joint training with the target model or the DFlash backbone, leading to extremely low training cost. At inference time, DeLS-Spec combines long-context and short-context logits, and the local head is not tied to a specific DFlash checkpoint, making the method more modular and flexible. Experiments on Qwen3 models show that DeLS-Spec consistently improves speedup and average acceptance length over DFlash across math, code, and dialogue benchmarks.

---


### 157. [How Reliable Is the Multi-Input Heuristic for Bitcoin Address Clustering in Law Enforcement Contexts?](https://arxiv.org/abs/2607.07414)

**<font color=#1a73e8>作者：</font>** Leopold Müller, Jana Elsner, Thomas Niedermayer 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Address clustering is an important technique in blockchain forensics, widely employed by law enforcement to trace illicit crypto asset flows. The multi-input heuristic (MIH), which clusters addresses potentially associated with the same entity, is the most widely used. Yet, despite its broad adoption, the MIH has rarely been evaluated against reliable ground truth data. We implement a reusable evaluation framework covering nine established metrics and apply it to ground truth address-to-entity mappings obtained directly from European crypto asset service providers under legally mandated reporting obligations. When evaluation is restricted to reported addresses, the MIH appears strong at dataset level: we observe no mergers between reported services and recover same-service address pairs with recall $0.71$. However, this result is driven by one large service and ignores unlabeled addresses absorbed into full clusters. Metrics that assess the full clusters show substantially lower precision and recall ($0.36$ and $0.44$), meaning that services are often only partially recovered or embedded in larger clusters. Entity-level results further reveal near-complete failures for some services. When MIH-based clusters are used to support criminal suspicion, preliminary seizure of crypto assets to secure later forfeiture/ confiscation, or as evidence in trial proceedings, prosecutors and judges must account for the heuristic's metric-dependent and entity-dependent reliability.

---


### 158. [VCDP: Variation-Conditioned Distributional Proxy Learning for Semi-Supervised Medical Image Segmentation](https://arxiv.org/abs/2607.07416)

**<font color=#1a73e8>作者：</font>** Zimu Zhang, Yiheng Zhong, Zhuoru Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semi-supervised 3D medical image segmentation reduces the need for dense voxel-level annotations by exploiting unlabeled volumes. Although existing methods such as consistency regularization, pseudo-labeling, and co-training improve prediction-level robustness, they often provide insufficient feature-space organization for anatomically complex structures, especially small organs and ambiguous boundary regions with large intra-class variations. To address this issue, we propose Variation-Conditioned Distributional Proxy Learning (VCDP), a plug-and-play training-only regularization module for semi-supervised 3D medical image segmentation. VCDP represents each class with a learnable Gaussian distribution for shared class semantics and multiple variation prototypes for fine-grained intra-class patterns. A unified variation-conditioned compatibility score is further formulated to fuse distributional similarity and soft variation aggregation, guiding voxel embeddings to align with both global organ identity and local anatomical variations. VCDP is attached to decoder features during training and removed during inference, introducing no additional inference cost. Experiments on multi-organ segmentation benchmarks show that VCDP improves most evaluated baselines, particularly for small, ambiguous, and highly variable organs. Our anonymous code is released at this https URL.

---


### 159. [InductWave: Inductive Multi-Hop Logical Query Answering on Knowledge Graphs](https://arxiv.org/abs/2607.07422)

**<font color=#1a73e8>作者：</font>** Mayank Kharbanda, Michael Cochez, Rajiv Ratn Shah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Logical Multi-Hop Query Answering over Knowledge Graphs (KGs) can be formulated as querying, with an implicit completeness assumption. Current works mainly focus on Existential First Order Logic (EFO) queries. These EFO queries contain conjunction, disjunction, and negation operators. Most existing works employ transductive reasoning, meaning they are not capable of reasoning over entities unseen during training. In the real world, there is a resource scarcity, and we cannot train a model with all the nodes of a large KG. Hence, we propose InductWave, a wavelet-based inductive embedding method for logical query answering on large KGs. Here, the training graph consists of fewer nodes than the test graph. Our model performs on par with the baseline models while having half the number of message-passing layers. It outperforms all of them in most cases, with 75% of the layers. These fewer resource requirements enable us to evaluate InductWave on massive graphs, such as Wiki-KG. We test our model using extensive experiments across varying train-test graph proportions of the FB15k-(237) dataset, comparing it with the state-of-the-art models. The code and datasets for the model are available at this https URL.

---


### 160. [The Optimal Sample Complexity of Learning Autoregressive Chain-of-Thought](https://arxiv.org/abs/2607.07423)

**<font color=#1a73e8>作者：</font>** Zhiyuan Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We prove that, in the realizable PAC setting, the sample complexity of exact-trace learning for full autoregressive Chain-of-Thought traces is upper bounded by the standard multiclass rate of the local next-token class, where this rate is governed by the Daniely--Shalev-Shwartz dimension. Under exact-trace loss, one wrong action makes the whole trace incorrect; nevertheless, for every stopping rule $\mathtt{halt}$ and every pointwise $\mathtt{halt}$-halting local class $\mathrm{H}$, $n_{\mathrm{PAC}}^{\varepsilon,\delta}(\operatorname{Roll}_{\mathtt{halt}}(\mathrm{H}))=O((\operatorname{DSdim}(\mathrm{H})+\log(1/\delta))/\varepsilon)$, with no dependence on rollout length. The dependence on $\operatorname{DSdim}(\mathrm{H})$ is worst-case optimal, since one-step stopping recovers ordinary multiclass learning of $\mathrm{H}$. The proof introduces parity dimension, a rollout-stable refinement of DS dimension based on even pseudo-cubes. It controls one-inclusion density via a low-coordinate spanning theorem on finite restrictions and, unlike DS dimension itself, does not increase under autoregressive rollout. We also show why this detour is necessary: DS dimension can increase under rollout.

---


### 161. [RLVP: Penalize the Path, Reward the Outcome](https://arxiv.org/abs/2607.07435)

**<font color=#1a73e8>作者：</font>** Bojie Li, Noah Shi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agents acting on our behalf in the real world (e.g. placing phone calls) must learn online from costly, often irreversible interactions rather than cheap simulator steps. Two things follow. First, deployability depends on the path, not only the outcome. An agent must respect outcome-neutral constraints such as not repeatedly calling an unresponsive user, respecting business hours, or completing required authentication constraints that outcome-based rewards cannot express, since violating them frequently improves apparent success. Second, because each interaction is expensive, the agent must learn efficiently from very few examples.
Reinforcement learning from verifiable rewards (RLVR) is blind to both challenges: it optimizes solely on the outcome and wastes expensive rollouts on all-fail groups where group-relative advantage collapses to zero. Attempts to densify supervision by rewarding progress target the hard-to-verify direction. In contrast, real agentic environments can cheaply detect bad moves. Since group-relative advantage is equivalent to within-group variance, a dense signal helps only when it supplies variance the outcome lacks. A verifiable penalty on the path meets this condition reliably, while a progress potential helps only where partial progress is reachable. The resulting recipe "penalize the path, reward the outcome" achieves high task success with near-zero violations, where outcome-only training violates constraints on nearly every episode. We provide four design rules for effective penalties, including avoidance of the inaction trap that arises when a penalty is used in isolation.

---


### 162. [The Blind Curator: How a Biased Judge Silently Disables Skill Retirement in Self-Evolving Agents](https://arxiv.org/abs/2607.07436)

**<font color=#1a73e8>作者：</font>** Xing Zhang, Yanwei Cui, Guanghui Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A self-evolving agent retires its bad skills by watching them fail, so what happens when the judge cannot see the failures? Skill retirement is the structural constraint that keeps a growing library from drifting below the no-skill baseline, but its guarantee assumes an unbiased reward, which is false for the LLM judges that reference-free tasks force upon us. We show that a biased judge does not merely add noise; it \emph{silently switches off the curator}. We make this precise with a corrupted-reward analysis and, isolating the causal channel by injecting corruption on top of a deterministic reward, a behavioral study on a reference-free report-writing testbed with a code-generation cross-check. Symmetric noise leaves retirement intact, but \emph{false-pass} bias (failures slipping through as passes) disables contribution-based retirement past a sharp threshold that no amount of data can cross. Separating genuine retirement from cap-eviction churn shows this \emph{mechanism} failure is universal, holding across domains and failure rates and sparing only near-zero-false-pass, verifier-like graders. The downstream \emph{outcome}, though, is regime-dependent: eval quality degrades only where the same corruption also starves skill synthesis, and otherwise holds steady, so the disabled curator is \emph{silent}, surfacing in no aggregate metric. The contribution is a behavioral safety result, not a performance one. A cheap defect-injection audit then tells an operator, before deployment, which side of the threshold their judge occupies.

---


### 163. [Should We Dangle a Carrot? The Effect of Performance-based Incentives in Visualization Experiments](https://arxiv.org/abs/2607.07463)

**<font color=#1a73e8>作者：</font>** Abhraneel Sarma, Matthew Kay, Sheng Long 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> A perennial research question in visualization involves identifying which visual encodings for a particular dataset are most effective for users in performing a specific task. The relative effectiveness of the different encodings are commonly identified through controlled experiments. However, designing an experiment involves making many, often ad hoc, decisions about the experimental setup such as whether to include a training module, whether to provide performance-based incentives to participants, etc. Yet, there is limited guidance on how these decisions should be made, and we do not fully understand the impact of these subjective decisions on empirical results. In this paper, we investigate the impact of one such key design decision: monetary rewards. Specifically, we ask: does providing or not providing participants with performance-based financial incentives affect the results and the conclusions that we draw from visualization studies? We conducted two crowdsourced studies investigating the impact of incentives on (i) a low-level, perceptual task (perception of correlations in scatterplots or parallel coordinate plots), and (ii) a task involving reasoning (decision-making based on a weather forecast represented as intervals or density plots). In each of these studies, we manipulate both the visual representation and the presence of incentives as between-subject conditions. We expected to find no effect of incentives on the perceptual task, but to see an effect for the decision-making task. However, we found no effect on task performance in either study. While these are results of only two studies and should be replicated, they suggest that performance-based financial incentives may not always have the intended effect on participants that we presumed, and calls for a reflection of how incentivized studies should be designed.

---


### 164. [A Theory of Contrastive Learning with Natural Images](https://arxiv.org/abs/2607.07470)

**<font color=#1a73e8>作者：</font>** Antonio Torralba, Yair Weiss  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Why does contrastive learning with simple images and augmentations yield useful representations for downstream tasks? We address this question by analytically computing the optimal representation in terms of a contrastive loss for a range of basic augmentations and any image dataset with stationary statistics. We show that for certain augmentations the optimum can be attained by a CNN whose first layer filters are sinusoids, followed by a pointwise nonlinearity, global average pooling, and a final linear layer that performs partial whitening. We also show that the optimal weights in such CNNs for more complicated augmentations are still sinusoids. The frequencies of the sinusoids and their weights can be computed using a simple waterfilling algorithm given the dataset's expected power spectrum. Experiments with different image datasets and augmentations show that such CNNs trained with SGD empirically learn sinusoids in their first layer and to perform partial whitening

---


### 165. [Where to Intervene? Benchmarking Fairness-Aware Learning on Differentially Private Synthetic Tabular Data](https://arxiv.org/abs/2607.07471)

**<font color=#1a73e8>作者：</font>** Vinícius Gabriel Angelozzi, Héber H. Arcolezi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning models are increasingly deployed in high-stakes domains, raising concerns about both privacy and fairness. Differential Privacy (DP) has become a gold standard for privacy-preserving data analysis, while fairness-aware mechanisms aim to mitigate discrimination against underrepresented groups. However, these objectives can conflict: DP often amplifies disparities across demographic groups, and little is known about whether established fairness interventions remain effective under DP constraints. In this work, we present, to our knowledge, the first systematic evaluation of fairness interventions on differentially private synthetic tabular data. Our benchmark centers on the Adaptive Iterative Mechanism (AIM), identified as the state-of-the-art marginal-based DP synthesizer (Cormode et al. 2025). We thus evaluate fairness interventions across four datasets, multiple group fairness metrics, and three categories of mitigation strategies (pre-processing, in-processing, and post-processing) under a wide range of privacy budgets. We compare four pipeline configurations: (Baseline) training on original data; (DP-only) training on DP synthetic data; (Fair-only) applying fairness mechanisms on original data; and (DP+Fair) combining fairness mechanisms with DP synthetic data. Our results demonstrate that while DP alone can degrade both utility and fairness, applying fairness interventions can partially restore equitable outcomes. Among them, post-processing methods tend to provide more stable fairness-utility trade-offs across privacy budgets and synthesizers, achieving strong fairness improvements while preserving competitive utility relative to other intervention stages. We release all code, data, and experimental artifacts in an open-source repository to ensure full reproducibility and to support future research on the privacy-fairness-utility trade-off.

---


### 166. [Beyond Attack-Success Rate: Action-Graded Severity Scale for Tool-Using AI Agents](https://arxiv.org/abs/2607.07474)

**<font color=#1a73e8>作者：</font>** Harry Owiredu-Ashley  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic red-teaming benchmarks report whether an injected agent was compromised as a single bit: the attack succeeded, or it did not. We argue that this binary attack-success rate discards the information a defender most needs, namely how harmful the resulting action was. We introduce an action-graded harm rubric that scores an agent's tool-call trajectory on a seven-level ordinal scale (L0 to L6) according to whether the executed action was reversible, whether it crossed scope to reach another party, and whether it expanded privilege. We compute the scale two ways: a deterministic oracle that reads the trajectory and the attacker's stated goal, and a panel of three frontier language-model judges that read a tag-free account of the same trajectory. Across four victim models and two defenses on the AgentDojo workspace suite, severity grading exposes three cases the binary metric hides, including a defense that reports a zero attack-success rate while still permitting an externally visible cross-scope leak through an unfiltered tool. The judge panel reproduces the oracle with high ordinal agreement (Krippendorff's alpha = 0.91) but shares systematic blind spots that we characterize, most notably a failure to recognize escalation chains. Unlike prior work that provides harm taxonomies, harmful-task completion tests, execution-level safety benchmarks, or severity-aware simulation, our contribution is a reusable, trace-grounded severity instrument applied to the actual actions recorded in existing red-team logs. All code, prompts, and per-episode logs are released.

---


### 167. [FourierQK: Spectral Preprocessing of Query-Key Projections Improves Transformer Attention](https://arxiv.org/abs/2607.07478)

**<font color=#1a73e8>作者：</font>** Athanasios Zeris  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> FFT-based spectral preprocessing of learned query-key (Q/K) projections substantially improves transformer attention on character-level language modelling. On TinyShakespeare: a fixed random spectral filter achieves val=1.031 (Delta=+0.443); a single learned frequency at paragraph scale achieves val=0.608 (Delta=+0.867); and four learned frequencies spanning paragraph to word scale achieve val=0.309 (Delta=+1.166), a 79% reduction over standard dot-product attention. The single-frequency result is confirmed across three random seeds (mean val=0.236, std=0.019). The four frequencies converge to a near-geometric multi-scale ordering (49, 27, 10, 6 tokens/cycle) corresponding to paragraph, sub-paragraph, phrase, and word scales. The gain is specific to spectral preprocessing: random orthogonal and non-orthogonal projections of Q/K produce no measurable improvement, suggesting the benefit comes from global frequency-domain mixing rather than metric distortion. All results are verified by a shuffled-validation diagnostic against positional leakage. Causal filters (Gaussian, Mexican Hat, Morlet) do not improve over standard attention at character-level tokenisation: the bilateral FFT kernel is structurally non-causal, coupling every position to future tokens. This defines an architectural boundary between bilateral spectral attention (this paper) and genuinely causal spectral attention at word-scale tokenisation (companion paper MorletQK). This work is architecturally distinct from FNet (Lee-Thorp et al., 2021), which replaces attention with Fourier mixing of token embeddings. Here, spectral preprocessing applies only to Q/K projections while the full attention score structure is preserved.

---


### 168. [Discovering Geometric Biases in 3D Face Reconstruction: A Curvature-Aware Spectral Framework for Fairness Evaluation](https://arxiv.org/abs/2607.07486)

**<font color=#1a73e8>作者：</font>** Veronika Shilova, Emmanuel Malherbe, Giovanni Palma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Morphable Models (3DMMs) remain the standard parametric shape priors for many state-of-the-art 3D face reconstruction algorithms. However, as these models are derived from a finite number of 3D face samples, they inherit the morphological biases of their training data, potentially limiting their generalizability across diverse global populations. In this paper, we propose a novel framework to analyze 3DMM reconstructions through the lens of surface curvature, with the objective to discover, quantify and visualize biases. While standard evaluation metrics often rely on Euclidean distances, our reconstruction error captures subtle surface nuances such as local topology or undulations. To do so, we leverage the Laplace-Beltrami Operator (LBO) to generate high-resolution curvature error maps, providing a localized and geometrically meaningful visualization of discrepancies between ground truth faces and reconstructed meshes. We derive from it an error metric that we validated through a user study, observing a significantly higher correlation to human perception compared to traditional methods. Furthermore, we conduct extensive experiments across several 3DMM bases and fitting algorithms, uncovering systematic age-related biases and providing preliminary evidence of biases associated with gender and ethnicity. Our findings highlight the necessity of adopting curvature-aware evaluation protocols to ensure demographic fairness and geometric precision in future 3D face reconstruction research.

---


### 169. [Search, Fail, Recover: A Training Framework for Correction-Aware Reasoning](https://arxiv.org/abs/2607.07492)

**<font color=#1a73e8>作者：</font>** Dmitry Beresnev, Vladimir Makharev, Roman Khalikov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many reasoning tasks are not well described by a single left-to-right chain: a solver may need to pursue a plausible branch, observe delayed failure, and return to the latest prefix that can still be completed. We introduce Pyligent, a training and inference framework inspired by the Diligent Learner formulation that represents reasoning as validated search over partial solution chains. A task validator labels generated continuations and failures, and the resulting search trees are converted into supervised targets for three actions: continue, finish, and backtrack, with optional traces that summarize abandoned branches. We evaluate Pyligent on a hidden directed graph task designed to isolate delayed-failure recovery, and on structured reasoning domains with exact validators, including $4{\times}4$ Sudoku, Sudoku with reasoning traces, and Blocksworld. Compared with gold-only supervised fine-tuning, Pyligent improves solve rate by $72.7$ percentage points on hidden graphs, by $17$ and $18$ points on mixed and expert Sudoku, by $27$ and $14$ points on mixed and expert Sudoku with reasoning traces, and by $13$ points on Blocksworld. These results suggest that explicit failed-branch supervision can teach useful recovery behavior beyond imitation of polished solution chains.

---


### 170. [Reward-Adaptive Iterative Discovery: A Case Study on Automated Game Testing for NHL26](https://arxiv.org/abs/2607.07498)

**<font color=#1a73e8>作者：</font>** Florian Fuchs, Jessy Gosselin-Grant, Boris Skuin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Testing is a major effort for the gaming industry, requiring a significant part of development budget and people power. We present a case study on a development version of the ice hockey game EA SPORTS NHL 26, for which human playtesters test the goalie AI for behavioral exploits. To reduce the effort of re-testing the goalie AI after every game or behavior modification in the development phase, we propose Reward-Adaptive Iterative Discovery (RAID), a novel approach to automatically find exploits using an iterative Reinforcement Learning (RL) approach that trains a population of goal scoring agents. While previous approaches can already successfully find exploits, RL algorithms tend to overfit to a single solution. We introduce a simple extension on top of existing RL algorithms, such that they find multiple diverse high-quality solutions. For our first deployment of this approach, within a single experiment we were able to find six hockey scoring exploit strategies that were qualitatively similar to those that playtesters had found in hours-long manual testing sessions.

---


### 171. [Fast Rates for Semi-Supervised Learning via Data-Augmentation Graph Regularization](https://arxiv.org/abs/2607.07513)

**<font color=#1a73e8>作者：</font>** Adam M. Oberman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning matches supervised accuracy from a fraction of the labels, but the labeled-sample efficiency behind this has lacked a theoretical explanation. We provide one. Data augmentation induces a similarity graph on the unlabeled data, so downstream learning on that graph is graph-Laplacian-regularized learning. We prove a fast transductive rate, $O(1/n_L)$ in the number of labels, in place of the supervised $O(1/\sqrt{n_L})$, by carrying the leave-one-out stability apparatus of Johnson and Zhang (JMLR 2007) over to the augmentation graph, and without the unrealistic assumptions of limit-based analyses (exact kernel, generalizing features). The bound makes augmentation quality explicit: the expected error is at most $C/n_L + R_{\mathrm{DA}}(y)$, where the data-augmentation alignment error $R_{\mathrm{DA}}(y)$ is the graph-cut mass of augmentations that cross a label boundary, so good augmentations let few labels suffice. The analysis uses a streamlined loss that drops the projector, negative-sample, and orthogonality overhead of standard objectives yet still recovers the top-$K$ ideal features in the infinite-data limit, the augmentation-kernel eigenspace studied by Zhai et al. The result explains the observed accuracy-versus-label-count curve rather than only bounding a generalization gap.

---


### 172. [Stability and Convergence of Optimistic Exponential Weights with Asymmetric Step Sizes in Bimatrix Games](https://arxiv.org/abs/2607.07517)

**<font color=#1a73e8>作者：</font>** Hédi Hadiji, Sarah Sachs  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We study bimatrix two-player games and investigate the last-iterate convergence and stability of equilibria for the iterates generated by the optimistic exponential weights method. In contrast to prior work, we allow the step sizes $\eta_x$ and $\eta_y$ to differ. Our first main result establishes, under the assumption that the set of fixed points is finite, a sufficient condition for global last-iterate convergence in the special case of zero-sum games, which constrains only the product $\eta_x\eta_y$ of the step sizes. This condition is practically relevant and partially explains empirically observed behavior. Our second main result provides an almost-tight threshold for asymptotic stability and instability, again in terms of products of the step sizes, for general bimatrix games. This result is primarily of theoretical interest. We derive several known results and practically relevant step size bounds for special cases and illustrate our results by experiments.

---


### 173. [Learning to Unify Deformable Shape and Texture Representations for Cardiac Video Classification](https://arxiv.org/abs/2607.07518)

**<font color=#1a73e8>作者：</font>** Tonmoy Hossain, Miaomiao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deformable shape representations have proven to be robust complements to texture features in cardiac image classification, offering geometric priors that are invariant to imaging artifacts and intensity variations. However, existing deep networks perform simple concatenation to combine these distinct feature representations, which neither fully exploits their complementary nature nor learns cross-modal feature dependencies. Furthermore, this results in uniform attention across all timepoints; hence ignoring the varying diagnostic importance across the cardiac phases. In this paper, we propose a novel cardiac video classification model that, for the first time, learns temporal features in an integrated space of deformable shape and image texture representations. In particular, we design a bi-directional cross-attention in the latent space to fuse latent deformable shape and image features, allowing each modality to adaptively weight the other based on spatio-temporal correspondence. In contrast to current methods that apply uniform weighting across all the cardiac phases, our approach learns to dynamically adjust the contributions of shape and texture representations, derived from images, over time. We demonstrate state-of-the-art classification performance on a cine cardiac magnetic resonance (CMR) video dataset, achieving improved interpretability from attention mechanisms that identify diagnostically critical cardiac phases and modality contributions.

---


### 174. [Gradient-free Riemannian Langevin Sampler](https://arxiv.org/abs/2607.07519)

**<font color=#1a73e8>作者：</font>** Ricardo Baptista, Olivier Zahm  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We address the problem of efficiently sampling multimodal probability distributions, where standard Markov Chain Monte Carlo methods often suffer from poor mixing and mode trapping. To mitigate these issues, we propose Gradient-free Riemannian Langevin Sampler (GRiLS), a novel proposal that improves exploration without requiring gradient evaluations of the target density. Our approach introduces a Riemannian metric which reshapes the local geometry in order to facilitate transitions across modes. The resulting gradient-free MCMC algorithm is particularly suitable for complex, computationally expensive targets where derivatives are unavailable or impractical. The GRiLS proposal requires knowing the mean and covariance of the target density, which we estimate using an ensemble of interacting particles. Empirical results on multimodal benchmarks demonstrate that GRiLS achieves improved mixing compared to existing gradient-based and gradient-free MCMC approaches.

---


### 175. [Two-player Alternate Uses Test: A Controlled Testbed for Interactive Human-AI and Human-Human Co-Creation](https://arxiv.org/abs/2607.07522)

**<font color=#1a73e8>作者：</font>** Babak Hemmatian, Anita Keshmirian, Yijun Lin 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Controlled research on AI ideation typically compares independent agents, while field studies of human-AI collaboration sacrifice experimental control. We introduce a controlled, two-player extension of the Alternate Uses Test (AUT) that enables comparison of human-human and human-AI co-creation under matched interactive conditions, alongside calibrated non-interactive baselines. The platform supports decomposition of performance into three typically confounded factors: participant traits, partner perceptions, and content dynamics. An in-person pilot (N = 62) demonstrates its utility. Under matched time limits, originality with a GPT-4 partner is statistically equivalent to that with a human partner. Approach motivation (BAS Drive) moderates whether interactive partnership benefits originality, and self-reported cognitive outsourcing predicts lower originality specifically in human-human dyads. Prior exposure to highly creative ideas improves later performance, suggesting a "seeding" intervention. We release the platform, code, and dataset as a shared testbed for controlled studies of human-AI co-creation.

---


### 176. [Context-Aware Slum Mapping in Sub-Saharan Africa Using Sentinel-1 Texture and Local Climate Zones](https://arxiv.org/abs/2607.07532)

**<font color=#1a73e8>作者：</font>** Peterson Chepkilot, Babak Memar, Paolo Gamba  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate mapping of informal settlements remains a major challenge in Sub-Saharan African (SSA) cities because optical imagery often fails to distinguish Informal Settlements (defined here as LCZ 7) from spectrally similar formal Compact Low-Rise areas (LCZ 3). This study presents a context-aware, reproducible Optical-SAR framework that improves informal settlement delineation using Sentinel-2 spectral features and Sentinel-1 structural information within an adapted Local Climate Zone (LCZ) taxonomy. We implement a three-tier SAR integration strategy: calibrated backscatter, GLCM textures, and a physics-guided feature engineered to capture the high structural disorder and weak radar return characteristic of SSA informal settlements. Using reference data across Nairobi and Eldoret (Kenya), we evaluate performance via a stratified hold-out protocol and a season-aware ablation study. Results show that SAR textures provide the dominant performance gain for LCZ 7 detection. The Optical-SAR model achieves overall accuracy of 0.816 (dry) and 0.807 (wet), significantly outperforming the WUDAPT baseline (OA 0.704) and reducing the critical LCZ 3 - LCZ 7 confusion to 7%. Seasonal analysis indicates that while optical-only separability varies with phenology, SAR-derived textures stabilize informal settlement mapping across seasons. These findings demonstrate that the incorporation of SAR-derived features yields consistent improvements for urban morphology mapping in data-scarce environments across seasons and across the evaluated source cities, while cross-city transfer remains limited without local adaptation strategies.

---


### 177. [Infinite Worlds with Versatile Interactions](https://arxiv.org/abs/2607.07534)

**<font color=#1a73e8>作者：</font>** Zelin Gao, Qiuyu Wang, Jiapeng Zhu 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present LingBot-World 2.0 (also known as LingBot-World-Infinity), an advanced iteration of LingBot-World featuring four distinct upgrades. (1) Our model achieves an unbounded interaction horizon while maintaining consistent output quality, benefiting from a carefully crafted causal pretraining paradigm. (2) Through distilling a real-time variant from the base model, our system guarantees rapid response time, sufficient to drive 720p video streams at 60 fps. (3) Compared to the previous version, this update introduces highly diverse interactive elements, comprising a broader spectrum of actions (e.g., attacking, archery, spell-casting, and shooting) alongside a richer variety of text-driven events. (4) We pioneer the integration of an agentic harness within the domain of world modeling, wherein a pilot agent is tasked with planning and executing character behaviors, while a director agent is responsible for synthesizing novel environmental elements as the scene progresses. Additionally, to facilitate a shared experience, we develop an interface that permits multiple players to simultaneously immerse themselves in this vivid world simulator. We pair our primary 14B model with a lightweight 1.3B counterpart, which supports effortless deployment on a single GPU.

---


### 178. [Avoiding unsafe sets when training with Langevin Dynamics](https://arxiv.org/abs/2607.07538)

**<font color=#1a73e8>作者：</font>** Adam M. Oberman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training a model with noisy gradient descent can be idealized as overdamped Langevin dynamics on the loss landscape, and a natural safety question is to bound the probability $\nu_t(\mathcal{A}_H) = \mathbb{P}(Q_t \in \mathcal{A}_H)$ that the trajectory lies in a designated failure region $\mathcal{A}_H$. We study this for a smooth, strongly convex loss in $d$ dimensions and a failure region separated from the minimizer by an energy gap. Three bounds emerge. At the end of training, the equilibrium mass $\pi(\mathcal{A}_H)$ is exponentially small in $d$, with a complementary energy-barrier rate when the noise is small. Along the trajectory, a shape-free bound $\nu_t(\mathcal{A}_H) \le \pi(\mathcal{A}_H)(1 + \sqrt{\chi_0^2/\pi(\mathcal{A}_H)}\,e^{-mt})$ shows that the in-set probability relaxes to (twice) the static value after a burn-in time of order $d$, using only the global spectral gap $m$ of the loss. A worked Ornstein-Uhlenbeck example shows this burn-in is necessary: an angular slice of the equilibrium shell can transiently swell by a factor exponential in $d$, even though its equilibrium mass is tiny. To rule such swelling out we introduce a local relaxation rate attached to the failure region, defined through the spectral measure of its centered indicator rather than a Dirichlet-form Rayleigh quotient. For geometrically isolated regions this rate exceeds the global one, shrinking the burn-in proportionally, and combined with a maximum-principle ceiling it caps the trajectory probability uniformly in time. The picture is that strong convexity sets how fast training relaxes, but the shape of the unsafe set decides whether the trajectory bulges through it on the way home.

---


### 179. [Face-trace: Open-Set Attribution and Progressive Discovery of Synthetic Face Generators](https://arxiv.org/abs/2607.07545)

**<font color=#1a73e8>作者：</font>** Alessia Infantino, Claudio Schiavella, Irene Amerini  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in generative Artificial Intelligence have made synthetic face images increasingly realistic, creating new challenges for multimedia forensics. Source attribution methods should not only identify the generator of an image when the source is known, but also handle samples produced by previously unseen models. However, most existing approaches address synthetic face attribution in a closed-set setting, where all possible generators are available during training. This assumption does not hold in real-world scenarios, where new generators continuously appear and rejected samples should be organized rather than simply discarded. In this work we propose a pipeline for open-set synthetic face source attribution that combines known generator classification, energy-based OOD rejection, and unknown generator discovery. A classifier is trained on known generators using frozen I-JEPA embeddings, while rejected samples are represented by combining projected I-JEPA features with Forensic Self-Descriptors and then clustered to discover groups of unknown generators. We also extend the discovery stage to an incremental scenario, where rejected samples arrive over time. Experiments on the WILD dataset show that the proposed method achieves 96.73% closed-set attribution accuracy. In the open-set setting, energy-based rejection reaches 71.25% balanced accuracy, while rejected samples are clustered into meaningful unknown-generator groups, obtaining an ARI of 0.81, an NMI of 0.90, and an overall clustering purity of 87.74%. In the incremental setting, the discovered generator space is progressively extended while maintaining a final purity of 99.23%. Cross-dataset experiments suggest that the pipeline can operate beyond the original dataset distribution, although post-processing remains challenging.

---


### 180. [Think Big, Search Small: Where Capacity Matters in Hierarchical Search Agents?](https://arxiv.org/abs/2607.07548)

**<font color=#1a73e8>作者：</font>** Qinnan Cai, Yibo Zhao, Xiang Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model based search agents increasingly adopt multi-agent architectures in which a main agent decomposes a complex question into sub-queries and dispatches them to parallel sub-agents. However, existing systems instantiate all roles from a single model of identical scale, leaving open how model capacity should be distributed across roles. We factorize hierarchical search into three roles: a delegation role responsible for task decomposition, an execution role responsible for retrieval and evidence extraction, and an answer generation role held fixed as a confound control. We then conduct controlled capacity sweeps along the delegation and execution axes on five multi-hop QA benchmarks. The experiments yield three findings. First, role factorization consistently outperforms a single-agent baseline, improving exact match from 4.5 to 8.6 points across six model scales. Second, capacity sensitivity is asymmetric: scaling the delegation backbone improves EM by ~11 points, whereas scaling the execution sub-agent moves EM by only ~2.6 points, identifying decomposition as the capability bottleneck. Third, a 1.7B-parameter executor trained via quality-filtered trajectory distillation matches a frontier sub-agent in accuracy while consuming 37% fewer sub-agent tokens, advancing the Pareto frontier. These results suggest a concrete recipe for building hierarchical search agents: concentrate capacity at delegation and downsize execution without sacrificing accuracy. Our code is available at this https URL.

---


### 181. [AA-ViT: Anatomically Aware Vision Transformer with Structural and Frequency Guidance for Contrast Enhanced Brain MRI Synthesis](https://arxiv.org/abs/2607.07553)

**<font color=#1a73e8>作者：</font>** Talha Meraj, Tom Flannery, Charlie Cummins 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate tumour localization and diagnosis is a critical component of clinical care for brain cancers. Magnetic Resonance Imaging (MRI) is the most commonly used imaging modality due to its superior soft-tissue contrast. However, standard MRI often exhibits limited contrast and imaging artifacts, which necessitates the use of contrast agents to enhance lesion visibility. The administration of chemical contrast agents is not always feasible and may be contraindicated in patients with renal impairment or other health conditions. As a result, developing accurate and non-invasive contrast enhanced MRI (CEMRI) synthesis methods has clinical importance. In recent years, numerous approaches for CEMRI synthesis have been proposed, predominantly relying on generative artificial intelligence models. While these methods demonstrate promising performance, their dependence on implicit feature learning often limits their ability to preserve anatomical boundaries and tumour-specific fine structures. To address these challenges, we propose an anatomically aware frequency-and-structure-guided vision transformer (AA-ViT), for CEMRI synthesis using pre-contrast MRI modalities (T1, T2, and FLAIR). Experiments on the BraTS 2021 dataset demonstrate that the proposed method preserves anatomical and lesion boundaries, achieving higher PSNR and SSIM than state-of-the-art approaches. Clinical evaluation by three neuroradiologists and a neurosurgeon on 19 randomly selected cases across diverse gliomas yielded a mean score of 3.94/5, providing preliminary clinical validation rarely seen in prior studies. Synthetic post-contrast scans from our model could lower scanning costs, shorten imaging time, and avoid the potential risks of using gadolinium-based contrast agents.

---


### 182. [Collaborative Synthetic Data Generation for Knowledge Transfer in Federated Learning](https://arxiv.org/abs/2607.07565)

**<font color=#1a73e8>作者：</font>** Maximilian Andreas Hoefler, Karsten Mueller, Wojciech Samek  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> One-shot federated learning (OSFL) addresses the communication overhead of federated learning by limiting training to a single round, but doing so without sacrificing model quality is non-trivial, particularly when client data distributions diverge. Recent work has addressed this challenge by aggregating client knowledge on the server through the construction of transferable synthetic datasets or distillates. However, most of these methods lack formal privacy guarantees, leaving a gap in jointly achieving low communication, robustness to heterogeneity, and rigorous privacy. We propose FedKT-CSD (Federated Knowledge Transfer via Collaborative Synthetic Data), a framework inspired by neural image compression that closes this gap by leveraging publicly pretrained autoencoders as a shared latent space. Each client encodes its private data in a single forward pass, computes class-conditional latent statistics, and transmits these to the server. The server aggregates these statistics via secure aggregation, adds calibrated differential privacy noise, and decodes a synthetic dataset for training a global model and further downstream tasks. This design provides formal $(\varepsilon,\delta)$-differential privacy by construction, while keeping client-side computation and communication lightweight. Despite operating under privacy constraints, FedKT-CSD is competitive with and even outperforms non-private baselines across diverse datasets and heterogeneity settings, and scales to a large number of clients. Our code is available at: this https URL

---


### 183. [Multi-Class vs. Multi-Label BERT for CVE-to-CWE Mapping: How Taxonomy Structure Shapes the Errors](https://arxiv.org/abs/2607.07573)

**<font color=#1a73e8>作者：</font>** Ana Schwengber Kelm, Christian Bockermann, Jörg Frochte  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Assigning Common Weakness Enumeration (CWE) categories to Common Vulnerabilities and Exposures (CVE) records remains an important but largely manual step in vulnerability analysis. We study this task as a text classification problem and compare two modelling choices: a \emph{multi-class} formulation that predicts a single CWE per CVE and a \emph{multi-label} formulation that allows multiple assignments. Three transformer encoders (BERT Base, SecureBERT, and CySecBERT) are evaluated on three nested label spaces (83, 47, and 25 classes). Multi-class training achieves higher macro-F1 across all settings, although the gap to multi-label narrows from 21 to 2 percentage points as the label space shrinks. Post-hoc threshold optimisation on the multi-label side closes this gap on the 25-class setting. Confusion analysis shows that the dominant misclassification patterns follow the CWE hierarchy and are shared across all three encoders (Pearson $r > 0.92$), which suggests that the error structure is driven more by taxonomy design than by encoder choice. A hierarchy-relaxed evaluation that forgives within-family confusions raises macro-F1 from ${\sim}$81\% to ${\sim}$90\%, indicating that strict metrics understate branch-level classifier quality. CySecBERT achieves the strongest results overall, with statistically significant gains concentrated in the multi-label setting.

---


### 184. [Automatic Echocardiography Segmentation via Transition Probability Correlation for Stable Semantic Extraction](https://arxiv.org/abs/2607.07580)

**<font color=#1a73e8>作者：</font>** Xinran Chen, Xiyuan Wang, Guangquan Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While echocardiography is essential for cardiovascular diagnosis, inherent speckle noise and low signal-to-noise ratio often lead to ambiguous semantic features and fragmented boundaries. These limitations significantly hinder the segmentation accuracy of deep learning models in complex clinical cases. Moreover, temporal motion of the heart plays a critical role in recognizing anatomical structures. To address these challenges, we designed a STLSF module which comprises a window-matching-based semantic correction component and a semantics-guided texture enhancement component. By leveraging local transition probability correlations to correct semantics and employing semantics-guided texture enhancement, the STLSF module effectively mitigates texture instability and ambiguous semantic interpretations caused by disadvantaged echocardiography quality. Additionally, to facilitate the encoder's adaptation to the intrinsic priors of ultrasound-specific imaging patterns, we propose a frequency-aware denoising pre-training method. The entire work builds a convolution-based network with locality inductive bias and long-range dependencies. Extensive experiments confirm our SOTA performance, achieving 93.87\% Dice on CAMUS and 92.62\% on EchoNet-Dynamic, with respective HD95 values of 3.29mm and 2.73mm.

---


### 185. [Cardiac MRI Through-Plane Super-Resolution Guided by Reference and Memory](https://arxiv.org/abs/2607.07581)

**<font color=#1a73e8>作者：</font>** Shaoming Pan, Chenchuhui Hu, Leon Axel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Clinical cardiac MRI is commonly acquired with high in-plane resolution but coarse through-plane resolution to reduce scan time and accommodate breath-hold and cardiac-motion constraints, which limits 3D analysis and diagnostic accuracy. We propose STRMSR, a reference- and memory-guided through-plane super-resolution (SR) framework that reconstructs high-resolution (HR) cardiac volumes by leveraging HR reference views acquired from the same subject and intermediate SR results as the memory. Our method uses coarse-to-fine contextual matching to establish robust correspondence between low-resolution target and reference/memory images under spatial misalignment. A learnable patch-wise dynamic feature aggregation module predicts content-adaptive mixture weights for each local patch, effectively fusing dynamic information while suppressing unreliable feature transfers. The intermediate SR results stored in the memory bank ensure slice-to-slice consistency for the super-resolved 3D volume. Experiments on the WHS cardiac MRI dataset under two reference protocols, orthogonal-plane views and long-axis chamber views, demonstrate consistent improvements over baselines at 4x and 8x upsampling factors.

---


### 186. [NARAD: Non-colluding Aggregator-oblivious Record-And-Decrypt](https://arxiv.org/abs/2607.07596)

**<font color=#1a73e8>作者：</font>** Akshit Vakati Venkata, Rajat Dugar, Ayush Adarsh  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Electronic voting must keep individual ballots private while letting anyone verify the final tally. This paper presents an architecture that meets both goals without a trusted key dealer: each voter encrypts a ballot in the browser with a self-generated secret key under the Paillier additive homomorphic cryptosystem, and no party ever holds every key. Two server roles divide the tally. A collector combines the voters' per-ballot auxiliary values into a single group element; an aggregator uses that element to cancel the voters' random masks inside the homomorphic product and recover the exact vote sum, learning the result but no individual ballot. The Solana blockchain records every ciphertext immutably and enforces the election lifecycle, while a native C library (libtommath) performs the heavy modular arithmetic. We state six assumptions under which the protocol is correct and prove product homomorphism, mask cancellation, and sum recovery; privacy rests on the Decisional Composite Residuosity (DCR) assumption for the additive layer together with a Diffie-Hellman-style assumption on the masking base. A bit-packing scheme places an entire multi-candidate ballot in one ciphertext, cutting client work, on-chain transactions, storage, and tally cost by a factor of k (the candidate count); the slot width b is free, with only k*b bounded by log_2(N). With b = 25 and a 255-bit modulus the scheme supports ten candidates and up to 2^25 - 1 = 33,554,431 votes per candidate, about 335 million ballots, and tallies 50,000 ballots in under one second. Finally, running the collector and aggregator inside attested secure enclaves makes the tally tamper-resistant and prevents cross-role collusion to deanonymize voters. The proof-of-concept implementation is open-source; a worked numerical example in the appendix reproduces the full pipeline.

---


### 187. [Asymmetric Focal Loss Improves Graph Neural Network Prediction of Drug-Drug Interactions](https://arxiv.org/abs/2607.07611)

**<font color=#1a73e8>作者：</font>** Faranak Hatami, Mousa Moradi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Background: Graph neural networks improve computational prediction of polypharmacy side effects, but standard binary cross-entropy training allocates equal capacity to well-classified and difficult examples, potentially missing clinically significant interactions. We evaluated whether an asymmetric focal objective could improve multi-relational drug-drug interaction (DDI) prediction by emphasizing difficult positive interactions. Methods: ClinicalFocal loss was integrated into a relation-aware graph convolutional network using molecular fingerprints, physicochemical descriptors, and learned embeddings. The model was evaluated on TWOSIDES using five-fold cross-validation with identical experimental conditions (architecture, features, data partitions, hyperparameters, and random seeds) for ClinicalFocal loss and binary cross-entropy baseline. Results: ClinicalFocal loss increased accuracy from 0.699 to 0.892 (+19.3 percentage points) and F1 score from 0.700 to 0.894 (+19.4 percentage points). AUROC increased from 0.766 to 0.914, and AUCPR increased from 0.714 to 0.860. The false-negative rate decreased from 29.8% to 9.1%, while specificity increased from 69.6% to 87.5%. Overall classification error decreased from 30.1% to 10.8%, corresponding to a 64.1% relative reduction. Improvements were consistent across all five folds. Conclusions: Asymmetric focal optimization improved classification and ranking performance while achieving 90.9% recall for observed interaction triples, without modifying the underlying architecture. Loss-function design is a direct, tunable lever for improving graph-based DDI prediction.

---


### 188. [Higher-Order Geometric Updates for Levenberg-Marquardt Method via Riemann Normal Coordinates](https://arxiv.org/abs/2607.07623)

**<font color=#1a73e8>作者：</font>** Jianing Liu, Dong H. Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Nonlinear least-squares optimization is central to regression, physics-informed neural networks, and other machine-learning tasks. Such problems have a natural geometric interpretation, model predictions form a manifold in data space, while the chosen parameterization can introduce parameter-effects curvature that becomes a dominant source of nonlinearity. This exposes a limitation of the Levenberg-Marquardt (LM) method, its tangent-space step is applied as a straight update in parameter coordinates. Geodesic acceleration gives a second-order correction, but its removal of parameter-effect curvature is exact only in the infinitesimal-step limit. We propose a Riemann-normal-coordinate Levenberg-Marquardt method (RNC-LM) to improve this consistency for finite optimization steps. By reformulating the geodesic equation, RNC-LM extends geodesic acceleration to arbitrary-order corrections and constructs finite-step updates with progressively higher reparameterization consistency. A line search along the resulting RNC curve controls the traveled distance while keeping the cost close to standard LM. The method eliminates the tangential component of residual acceleration order by order in a moving tangent frame, making the actual objective reduction more consistent with the linear model prediction of LM. On classical nonlinear least-squares benchmarks, RNC-LM improves convergence and robustness in curved valleys and rank-deficient problems. On a reaction-diffusion PINN failure-mode benchmark, it reduces the relative L2 error to the order of 1e-3 and recovers a physically meaningful solution. On a large-scale machine-learning potential-energy-surface fitting task, it achieves a 34-fold speedup over standard LM.

---


### 189. [Embedded Blockchain Infrastructure Management (eBIM): A RISC-V-Empowered Hardware--Software Co-Design Framework Towards Trustworthy Blockchain](https://arxiv.org/abs/2607.07625)

**<font color=#1a73e8>作者：</font>** Qinglin Yang, Yuan Liu, Yaoyao Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Blockchain systems are undergoing a fundamental transition from decentralized ledgers for digital assets to general-purpose trust infrastructures for verifiable computation, decentralized physical resources, and automated infrastructure management. Meanwhile, the limitations of the Blockchain as a Service (BaaS) model stem from a common structural problem: outsourcing control of infrastructure to third-party service providers inevitably involves a systemic surrender of trust, flexibility, and data sovereignty. RISC-V, with its open, modular, and extensible design, provides a general-purpose computing foundation for public blockchains that is open, low-level, compileable, verifiable, and scalable. Inspired by the development and characteristics of eSIM, the embedded Blockchain infrastructure management (eBIM) is defined as a software-hardware collaborative paradigm for blockchain infrastructure management with RISC-V. This study aims to provide a comprehensive survey on eBIM supporting research and technologies, to answer the following research questions (RQs): RQ1 What is eBIM? RQ2 How does eBIM work? RQ3 What can eBIM do? By introducing the concept of eBIM, this paper establishes a foundational reference for researchers, hardware architects, and protocol designers in this rapidly evolving landscape, including cryptographic acceleration, trusted execution environments, zero-knowledge virtual machines, and smart contract execution engines. The prospects of the proposed e-BIM and its future research directions are indicated in this paper.

---


### 190. [Unlearning to Protect: A Distilled Reinforcement Learning Framework with Privacy-Preserving Feature Unlearning and XAI for IoT Security](https://arxiv.org/abs/2607.07635)

**<font color=#1a73e8>作者：</font>** Md. Nahid Hasan, Golam Rabiul Alam  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Botnets pose a significant cybersecurity threat, enabling attacks such as DDoS, data theft, and service disruptions on IoT devices. These devices often lack built-in botnet traffic filtering, leaving them highly exposed. Existing AI-based solutions improve detection capabilities but have limitations: (i) they are too heavy for IoT deployment, and (ii) they lack unlearning capabilities to forget sensitive or outdated features without retraining. To address these challenges, we propose DiRLU, a lightweight, reinforcement learning driven framework, while ensuring privacy by selectively unlearning sensitive or outdated features without requiring retraining. The framework leverages knowledge distillation to transfer knowledge from a teacher model into a lightweight student model, with both models trained using A2C. A post-hoc unlearning mechanism modifies weights to remove targeted features, while restored features show negligible performance loss, confirming reversibility. Unlike many benchmark models that used only 5% of the BoT-IoT dataset, this research leverages 25%, allowing us to develop a strong teacher model. Both the teacher and student models were trained using the A2C reinforcement learning algorithm, achieving impressive results, with the student model achieving 99.60% accuracy and a 99.80% F1 score. To enhance transparency, we integrated Explainable AI (XAI), particularly LIME, which helps interpret the model's decisions and identify the key features influencing its predictions. Moreover, DiRLU requires only 2,370 FLOPS, approximately 3.87x more efficient than the state-of-the-art model, highlighting its efficiency for edge deployment. DiRLU combines efficiency with privacy, aligning with GDPR standards (right to be forgotten) to provide practical and scalable IoT security solution.

---


### 191. [An optimal control approach for neural network architecture adaptation with a posteriori error estimation](https://arxiv.org/abs/2607.07637)

**<font color=#1a73e8>作者：</font>** C G Krishnanunni, Thomas Scott, Tan Bui-Thanh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work presents a novel approach for adapting neural network architecture along the depth based on a posteriori error estimation. By formulating neural network training as a continuous-time optimal control problem, we derive rigorous error estimates that quantify how approximation error distributes across network layers. This error decomposition enables a principled depth adaptation strategy: new layers are inserted at locations of maximum estimated error, allowing the network to efficiently capture complex, nonlinear variations in the underlying problem. Our framework introduces a novel network architecture that treats weights and biases as piecewise linear functions varying across layers, with the error estimator bounding the discrepancy between this discrete representation and the true continuous optimal control solution. The approach leverages dual weighted residual methodology from finite element analysis to derive computable upper bounds on the functional error. A key theoretical contribution is the derivation of explicit error bounds that decompose the total approximation error into interval-wise contributions, providing a rigorous basis for targeted architecture refinement. We demonstrate the effectiveness of our method on scientific datasets, including learning the observable-to-parameter map for the Navier-Stokes equation. Numerical results reveal that our approach consistently outperforms existing architecture adaptation methods in terms of generalization performance.

---


### 192. [ALER-TI: Aligned Latent Embedding Retrieval for Time Series Imputation](https://arxiv.org/abs/2607.07640)

**<font color=#1a73e8>作者：</font>** Xuan-Thong Truong, Trung-Kien Le, Tung Kieu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning has significantly advanced time series imputation, yet most existing architectures primarily rely on localized temporal context within the corrupted input sequence. This reliance can be limiting in real-world scenarios, where time series often exhibit non-stationary dynamics, weak temporal correlations, and infrequent patterns that are difficult to reconstruct from nearby observations alone. In this paper, we propose ALER-TI, Aligned Latent Embedding Retrieval for Time Series Imputation, a retrieval-augmented framework that explicitly leverages historical patterns to supplement degraded local context for more reliable missing-value reconstruction. The core of ALER-TI is Latent Embedding Alignment (LEA), which mitigates the representation mismatch between corrupted queries and complete historical candidates. By applying post-hoc masking in the latent space, LEA aligns candidates with the query's missingness pattern while allowing historical embeddings to be pre-computed and cached for efficient retrieval. ALER-TI is model-agnostic and can be integrated with various imputation backbones through a lightweight adaptation module. Extensive experiments on six real-world datasets under different missing rates demonstrate that ALER-TI consistently improves strong baseline models and enhances robustness across diverse imputation settings.

---


### 193. [Modeling Failure Dynamics in Time-Constrained Authentication Systems: Evidence of a Success Cliff in USSD Workflows](https://arxiv.org/abs/2607.07650)

**<font color=#1a73e8>作者：</font>** Aklile Seyoum Mamo, Amanuel Kebede, Anny Christelle Irakoze 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Time-constrained interactive systems such as USSD (Unstructured Supplementary Service Data)-based financial services operate under strict session limits and sequential user interaction. While stronger authentication mechanisms improve security, they also increase interaction complexity and time burden, potentially reducing transaction completion. In this work, we model the failure dynamics of such systems and investigate how authentication complexity interacts with user response time and network round-trip time to influence session success rate. We propose and implement a simulation-based framework to investigate these failure dynamics and formally define a non-linear failure phenomenon, termed the \textit{Success Cliff}, where session success rates sharply decline beyond a critical complexity threshold. Through controlled experiments, we quantify the trade-off between security and usability and identify conditions under which secure authentication workflows become operationally unreliable.

---


### 194. [Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops](https://arxiv.org/abs/2607.07663)

**<font color=#1a73e8>作者：</font>** Mingguang Chen, Licheng Wang, Bo Qu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI systems increasingly participate in their own improvement: revising their outputs, adapting their own harnesses during deployment, training on data they generate, and, increasingly, conducting AI research itself. This literature is described under a vocabulary ("self-refine," "self-reward," "self-play," "self-evolve") that conflates fundamentally different ambitions. We survey 1,250 arXiv papers (2024-2026) along two axes: what the system improves -- its behavior in deployment, its policy through training, its evaluator, or the research process itself -- and the degree of loop closure (human-in-the-loop to fully closed). The taxonomy separates bounded self-refinement -- convergent, evaluable, and already industrial practice -- from open-ended recursive self-improvement (RSI), which remains bounded by grounding requirements, collapse dynamics, and compute constraints on every measured axis. Its distinctive feature is a dedicated category for self-evaluation: every improvement loop is a claim that some signal can substitute for human judgment. We survey the evaluator design space -- judges, process reward models, verifiers, rubrics, meta-evaluation -- order the signals into a verification hierarchy from formal verifiers (strongest) to intrinsic self-assessment (weakest), and observe that demonstrated self-improvement strength tracks this hierarchy, that its failure modes (self-confirming loops, model collapse, diversity collapse) follow from its violations, and that the "research direction-setting" bottleneck keeping humans in the loop sits at the top of that hierarchy. We connect the technical literature to the theory of RSI limits and to the safety and governance questions raised by frontier-lab accounts of closing the loop, and identify governance-grade measurement of self-improvement as the field's most underpopulated niche.

---


### 195. [Guidance Breaks the Fitted Operator: A Terminal-Fitted Repair for Classifier-Free Guidance](https://arxiv.org/abs/2607.07665)

**<font color=#1a73e8>作者：</font>** Shiheng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classifier-free guidance (CFG) is the standard way to strengthen class-conditioning in diffusion and flow-matching samplers, yet at large guidance it oversaturates and destabilizes, symptoms practitioners suppress with more steps or limited-interval schedules. We analyze CFG through an asymptotic-preserving, numerical-analysis lens. Building on a recent result that the deterministic DDIM step is the unique fitted operator for the unguided terminal layer, exact on the final small-sigma stretch of sampling, we show that guidance re-stiffens exactly the discriminative subspace to an anomalous exponent 1+w. DDIM is therefore no longer fitted there, and on coarse meshes its guided residual diverges as sigma_min goes to zero. We prove a guided clock barrier with three ordered step-size thresholds, and read one-step oversaturation as its endpoint: a solver artifact on the calibration model rather than the continuous guided law. The same analysis yields a one-coefficient, zero-extra-NFE repair: replace CFG's w(r-1) by r^(1+w)-r on the guidance direction. On the calibration model's discriminative crossover, this removes CFG's sigma_min-divergent blow-up and is first-order accurate against the exact guided flow as sigma_min goes to zero. On learned CIFAR-10 checkpoints, and as a cross-domain smoke test on Stable Diffusion 1.5 DDIM, it acts as a high-guidance stabilizer at no extra cost rather than a universal quality knob: it cuts residual amplification and saturation, gives 9/9 point-FID wins over CFG on the tested grid, and preserves classifier-proxy target accuracy in the hard-cell blocks. We report the limits alongside: it is not a universal image-quality win, and against a dense vanilla-CFG reference it is not a uniformly better integrator of that field.

---


### 196. [Does Bielik Know What It Doesn't Know? Activation Dispersion Separates Entity Familiarity from Factual Reliability Across Model Scale](https://arxiv.org/abs/2607.07670)

**<font color=#1a73e8>作者：</font>** Grzegorz Brzezinka  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models hallucinate most about entities they have never seen. We ask whether a model's activations betray entity familiarity before a single answer token is generated, and whether that signal predicts the factual reliability of the answers. On four Polish Bielik models (1.5B-11B parameters), we probe four entity domains (athletes, cities, writers, musicians), each with 42 well-known, 42 obscure-but-real, and 42 fabricated entities addressed by a one-sentence question (504 prompts per model). Two unsupervised, single-forward-pass dispersion measures over post-SwiGLU MLP activations, inverse participation ratio and spectral entropy, separate known from fabricated entities at AUROC 0.95-1.00 across all domains and scales; a supervised linear probe reaches 0.99-1.00. Both clear selection-aware permutation floors of about 0.70-0.74 (empirical p<=1e-3), survive held-out layer selection (0.93-0.99), and persist on real names (known vs. obscure-but-real: 0.96-1.00). The signal transfers across entity types (mean off-diagonal AUROC 0.92-0.99); a matched-template counterfactual shows the only large drops are template-caused, not entity-type effects, and the signal is diffuse across heads. This representational signal is already at ceiling at 1.5B, whereas behavioral factual reliability scales sharply: 0, 2, 10, and 19 of 42 known athletes are answered fully correctly by the 1.5B, 4.5B, 7B, and 11B models under a strict judge. Within known entities, separating correct from hallucinated answers is much harder (probe 0.93; dispersion no better than a first-token-entropy baseline). A five-sample semantic-entropy baseline reaches only 0.71-0.83 at 5x the inference cost. Despite this internal awareness, the models almost never abstain: an audit of 2,520 answers finds 2 refusals and 1 hedge. Entity familiarity and factual reliability are distinct phenomena on different scaling curves.

---


### 197. [Max Out GRPO Signal: Adaptive Trace Prefix Control for Hard Reasoning Problems](https://arxiv.org/abs/2607.07674)

**<font color=#1a73e8>作者：</font>** Vladislav Beliaev  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group Relative Policy Optimization (GRPO) stalls on a model's hardest problems: when no rollout in a group succeeds, the group-relative advantages vanish and the problem contributes no gradient, wasting the frontier examples we most want to learn from. Prepending a correct prefix of a reference solution raises the success rate, making prefix length a continuous knob on difficulty. Concurrent methods set the knob once; AdaPrefix-GRPO turns it into a feedback controller: throughout training it adjusts how much of the solution each problem gets, holding its success rate near 50%, where GRPO's gradient signal is largest, then withdraws the assistance entirely, so the deployed model solves problems unaided. On hard math, at matched training FLOPs, it more than doubles GRPO's accuracy on held-out problems from the training distribution for a 0.6B model (2.1x), with 1.6x on Qwen3-1.7B and 1.7x on AIME, while roughly halving trace length. The method is implemented in data preparation plus a loss mask on prefix tokens; the trainer is otherwise stock. The smaller the model, the larger the gain.

---


### 198. [Scaling Mixture-of-Experts Video Pretraining for Embodied Intelligence](https://arxiv.org/abs/2607.07675)

**<font color=#1a73e8>作者：</font>** Shuailei Ma, Jiaqi Liao, Xinyang Wang 等 27 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the recent promise in robot control, video generative models suffer from a domain mismatch due to their primary focus on content creation. For example, their design inherently prioritizes visual fidelity and creativity over computational efficiency and physical realism. In this work, we present LingBot-Video, a DiT-based video pretraining paradigm specifically tailored for embodied intelligence. From the architecture perspective, we adopt the Mixture-of-Experts (MoE), instead of dense, framework to achieve a better trade-off between modeling capacity and inference efficiency, and manage to scale it up from scratch. From the data perspective, we construct a data profiling engine that augments standard internet videos with extensive robot-oriented footage, encompassing manipulation, navigation, and egocentric perspectives, to equip the base model with an intrinsic understanding of actions and world dynamics. From the training perspective, we develop a multi-dimensional reward system to enforce the alignment regarding physical rationality and task completion, going beyond standard criteria such as aesthetics, prompt-following, and motion consistency. Comprehensive evaluations validate its performance and efficiency as a video foundation model. We contribute LingBot-Video as the inaugural large-scale, open-source MoE video foundation model to the community, in a pioneering effort to bridge digital creativity and physical actuation.

---


### 199. [SkillCenter: A Large-Scale Source-Grounded Skill Library for Autonomous AI Agents](https://arxiv.org/abs/2607.07676)

**<font color=#1a73e8>作者：</font>** Tianming Sha, Yue Zhao, Lichao Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous AI agents can execute complex tasks with limited human review, yet they often lack the grounded operational knowledge to make their outputs not just executable but correct, secure, and maintainable. We introduce SkillCenter, to our knowledge the largest open skill library for agents by total count: 216,938 structured skills across 24 domain bundles. A SkillGate-filtered pipeline contributes 114,565 source-grounded skills from peer-reviewed journals, ArXiv, and over 24,000 technical sources, integrated with 102,373 community skills from GitHub and the ClawHub marketplace. We present the end-to-end framework that builds the pipeline subset: multi-source acquisition, an LLM-based quality gate (SkillGate), template-driven generation, iterative source-grounding, and quality-controlled publishing. Source grounding is a traceability guarantee: each retained claim maps to an exact quotation in its source. All skills ship as offline-searchable SQLite FTS5 bundles.

---


### 200. [How Data Shapes RoPE Frequency Usage: From Positional Scale Matching to Length Generalization](https://arxiv.org/abs/2607.07678)

**<font color=#1a73e8>作者：</font>** Xinyi Wu, Siyuan Liu, Ali Jadbabaie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rotary Position Embeddings (RoPE) provide transformers with a fixed grid of positional frequencies, yet trained models use these frequencies highly non-uniformly. We study what determines this frequency usage and propose a data-centered explanation: RoPE frequencies are selected to match the relative-distance structure of the training data. Viewing each frequency as a positional lens, we formalize a field-resolution tradeoff and show that, for a data-induced dependency profile of width $W$, the optimal frequency scales as $1/W$. This frequency-matching principle explains controlled observations on synthetic and text-based data, and suggests that the mid-low frequency bands observed in language models arise from the multi-scale dependency structure of natural language. We further connect frequency selection to position-interpolation-based length generalization: scaling frequencies down expands the effective field while reducing resolution. This helps when longer-context dependencies are approximate dilations of those seen during training, but can fail when relevant dependencies do not scale with context length. Empirically, we show that natural language exhibits approximate self-similarity across positional scales, explaining why test-time frequency scaling can support long-context generalization. Overall, our results identify a data-driven mechanism behind emergent RoPE frequency usage and show that long-context generalization depends on two forms of scale matching: between learned frequencies and training-time dependencies, and between frequency scaling and how those dependencies extend to longer contexts.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-207](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
