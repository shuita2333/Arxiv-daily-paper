# 📦 其他研究 | 2026年06月03日

> 本类共 **651** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-651](./part-14.md)

---

### 101. [GLENS: Global Search via Learning from Solver Iterates with Diffusion Models](https://arxiv.org/abs/2606.00366)

**<font color=#1a73e8>作者：</font>** Anjian Li, Bartolomeo Stellato, Ryne Beeson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider the problem of generating a large collection of initial guesses for local minima of multimodal non-convex continuous optimization problems. The goal is for these initial guesses to be high-quality (i.e., a numerical solver converges quickly) and diverse (i.e., represent many different local minima). Identifying multiple locally optimal solutions enables flexible downstream decision-making, but typically requires expensive global search. Existing data-driven methods predict initial guesses using only the final converged optima from offline solver runs, which discards information about the local neighborhoods of solutions and limits the available training data. We propose GLENS (Global Search via Learning from Solver Iterates), a data-efficient global search method that leverages intermediate solver iterates as free data augmentation. GLENS consists of two components: a neighborhood structure model that uses diffusion models to learn the local geometry around optima conditioned on problem parameters, and a solver behavior model that learns refinement directions to further guide samples towards nearby optima during diffusion sampling. Experiments on modified non-convex benchmark problems and a two-robot obstacle-avoidance navigation problem show that GLENS generates high-quality initial guesses while preserving the multimodal distribution of diverse local optima. The resulting initial guesses lead to faster solver convergence across different problem settings and solvers. We also analyze how key hyperparameter choices affect the performance.

---


### 102. [Reinforcement Learning with Pairwise Preferences in Long-Term Decision Problems](https://arxiv.org/abs/2606.00367)

**<font color=#1a73e8>作者：</font>** Jonathan Colaço Carr, Prakash Panangaden, Doina Precup 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning problems typically define the goal as maximizing the expected value of a scalar reward function. But, pairwise preferences are often easier to specify than scalar rewards, and they express certain goals that scalar rewards cannot. Methods for reinforcement learning with pairwise preferences have thus received growing interest. Unfortunately, these methods are inefficient in problems with long time horizons, and they lack guarantees on the performance of Markov policies relative to history-dependent policies, which bridge the theory and practice of reinforcement learning. We therefore propose the \textit{Markov decision contest} as a new problem model for reinforcement learning with pairwise preferences. We prove that stationary Markov policies are optimal among all history-dependent policies, that solving a Markov decision contest exactly is in P, and that a simple iterative algorithm converges to an optimal policy at a sublinear rate. Lastly, in a set of high-dimensional decision problems with long time horizons, we show that our approximate algorithm is significantly more learning-efficient than prior work.

---


### 103. [How Much Orthogonalization Does Muon Need?](https://arxiv.org/abs/2606.00371)

**<font color=#1a73e8>作者：</font>** Hua Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon optimizers improve neural-network training by replacing ill-conditioned momentum updates with approximately semi-orthogonal updates. This motivates a practical question: how much orthogonalization does Muon actually require? We study this question using a relaxed cubic Newton--Schulz schedule derived directly for Muon's low precision singular value band. The resulting five-step cubic construction uses ten dominant matrix multiplications, compared with fifteen for five quintic Newton--Schulz iterations. The cubic schedule is not intended as a more accurate polar solver; instead, it is a principled low-cost variant that lets us probe the relation between polar accuracy, spectral shaping, and training quality. Across synthetic diagnostics, NanoGPT ablations, and training experiments on hybrid MoE/Mamba models, we find that training quality is not governed monotonically by polar-decomposition accuracy: truncated Polar Express, Muon-Jordan, cubic Newton--Schulz, and an explicit FP32 SVD polar factor can reach nearly indistinguishable final loss on GPT-2 Small, and cubic5 matches the Muon-Jordan quintic update within about $10^{-3}$ validation loss on hybrid MoE/Mamba models with one billion to four billion parameters. These results support cubic5 as a practical low-cost Muon orthogonalization variant, with empirical evidence of training-quality parity in the settings tested.

---


### 104. [LFA: Layer Feature Attention for Run-Time Introspection of 2D Object Detectors in Automated Driving](https://arxiv.org/abs/2606.00372)

**<font color=#1a73e8>作者：</font>** Mert Keser, Alois Knoll  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable object detection is critical for automated driving, yet even state-of-the-art detectors inevitably make errors that can compromise safety. Introspection methods that predict detector failures enable safer deployment by triggering fallback mechanisms or alerting human operators. However, existing approaches rely solely on last-layer features or hand-crafted statistics, discarding valuable information from earlier layers that capture different levels of visual abstraction. We propose Layer Feature Attention (LFA), a lightweight introspection method that learns to aggregate features from multiple backbone layers through an attention mechanism. Our key insight is that detection errors manifest differently across feature hierarchies: low-level layers capture fine-grained details essential for detecting small or occluded objects, while high-level layers encode semantic information for scene understanding. LFA learns layer importance weights end-to-end, enabling both improved error prediction and interpretable analysis of which feature levels are most indicative of detector failures. Extensive experiments on KITTI and BDD100K demonstrate that LFA achieves state-of-the-art introspection performance, outperforming single-layer baselines across multiple detector architectures.

---


### 105. [The Deterministic Horizon: When Extended Reasoning Fails and Tool Delegation Becomes Necessary](https://arxiv.org/abs/2606.00376)

**<font color=#1a73e8>作者：</font>** Dongxin Guo, Jikun Wu, Siu Ming Yiu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Extended chain-of-thought reasoning can degrade performance on deterministic state-tracking tasks, not due to preference biases, but limits rooted in the information-theoretic capacity of decoder-only attention. We establish: (1) an Attention Bottleneck Theorem with a complementary achievability construction, bounding state-tracking capacity as $O(H \cdot \log(L/H) \cdot \sqrt{d_h})$; (2) a context-dependent error model yielding super-exponential accuracy decay; (3) the State-Space Jaccard metric distinguishing capability from preference failures; (4) a Deterministic Horizon $d^* \in [19, 31]$ beyond which tool delegation becomes necessary. Across 12 models and 8 task domains (including SWE-Bench, WebArena, and SQL-Multi), tool-integrated reasoning consistently outperforms neural chain-of-thought; on the primary model suite it reaches 86-94% accuracy versus 24-42% for neural chain-of-thought. Fine-tuning on optimal-length traces yields $<$5% improvement, confirming an architectural ceiling, and high cross-model correlation ($r = 0.81$-$0.91$) indicates these failures are architectural rather than training-specific. Our results provide principled guidance for when pure neural reasoning should yield to hybrid approaches in agentic systems.

---


### 106. [Score-Control for Hallucination Reduction in Diffusion Models](https://arxiv.org/abs/2606.00377)

**<font color=#1a73e8>作者：</font>** Mahesh Bhosale, Naresh Kumar Devulapally, Abdul Wasi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have emerged as the backbone of modern generative AI, powering advances in vision, language, audio and other modalities. Despite their success, they suffer from hallucinations, implausible samples that lie outside the support of true data distribution, which degrade reliability and trust. In this work, we first empirically confirm previously proposed hypothesis that score smoothness causes hallucinations in Image Generation diffusion models and provide a density-based perspective. We further formalize this notion by linking the hallucinations probability mass to lipschitz constant of the learned score function. Motivated by this, we introduce a Variance-Guided Score Modulation (VSM) strategy that controls the score Jacobian, in turn reducing score smoothness and better approximating the ground truth score that decreases hallucinations. Empirical results on synthetic and real-world datasets demonstrate that our approach reduces hallucinations (up to ~25%) while maintaining high fidelity and diversity, providing a principled step toward more reliable diffusion-based image generation. We also propose two benchmark datasets with extreme semantic variation for systematic hallucination evaluation. Code and Datasets are publicly available at this https URL.

---


### 107. [Non-Learning Low-Light Stereo Vision](https://arxiv.org/abs/2606.00379)

**<font color=#1a73e8>作者：</font>** Jason Wang, Lucas Nguyen, Hyunseung Eom 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a non-learning stereo framework for disparity estimation from severely noisy images. Using the Field of Junctions (FoJ), it retains coarse visual features stable under severe noise for cost volume construction while discarding fine textures inseparable from photon noise. The resulting structural information guides boundary-aware Semi-Global Matching (SGM) that dynamically adapts smoothness penalties to preserve true disparity discontinuities. The output is a sparse disparity map more accurate than those of recent stereo algorithms over unmasked pixels on widely-used benchmark datasets.

---


### 108. [SUPREME: A Multi-GPU Framework for Reproducible Image Unlearning Method Evaluation](https://arxiv.org/abs/2606.00380)

**<font color=#1a73e8>作者：</font>** Petros Andreou, Jamie Lanyon, Axel Finke 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Machine unlearning removes the influence of specific training data from a trained model without retraining it from scratch. Evaluating an unlearning method requires repeating training, unlearning, and evaluation across multiple seeds, which is computationally expensive. To our knowledge, existing image classification unlearning frameworks run on a single GPU, which limits how many seeds can be evaluated in reasonable time. We introduce SUPREME, an open-source framework that distributes these stages across multiple GPUs. SUPREME makes three contributions: a registry-based design for adding new methods, metrics, models, and scenarios; a multi-GPU architecture supporting multiple accelerators and precision modes; and a demonstration on Pins Face Recognition using ResNet18 and ViT under full-class and random-sample unlearning across ten seeds. The framework is available at this https URL.

---


### 109. [αDepth: Learning Single-Pass Soft Boundary Decomposition for Stereo Conversion](https://arxiv.org/abs/2606.00386)

**<font color=#1a73e8>作者：</font>** Xiang Zhang, Yang Zhang, Lukas Mehl 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurately modeling soft boundaries, e.g., hair and defocus blur, is a fundamental challenge in stereo conversion due to the ambiguous blending of foreground and background. Existing depth models primarily predict single-layer depth, leading to ambiguity in depth correspondence at soft boundaries. While matting techniques can capture opacity for layered modeling, they often struggle in complex scenes with multiple targets and usually require user intervention. This paper introduces {\alpha}Depth, a layered representation that decomposes soft boundaries for high-fidelity stereo conversion. Specifically, we first resolve mixed color and depth ambiguity by estimating layered color and depth values at soft boundaries. Considering complex multi-target scenes, we design a Circular Alpha Representation (CAR) that shifts the paradigm from global target extraction to local boundary decomposition. Unlike prior matting methods restricted to a single foreground/background, CAR enables efficient scene-level inference without manual guidance. Extensive evaluations demonstrate that {\alpha}Depth achieves state-of-the-art performance in stereo conversion, eliminating background bleeding and structural distortions at soft boundaries.

---


### 110. [Zamba2-VL Technical Report](https://arxiv.org/abs/2606.00390)

**<font color=#1a73e8>作者：</font>** Hassan Shapourian, Kasra Hejazi, Olabode M. Sule 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Zamba2-VL, a suite of vision-language models built on Zamba2, a hybrid language-model architecture combining Mamba2 state-space layers with a small number of shared transformer blocks. Across a broad range of image understanding, reasoning, OCR, grounding, and counting benchmarks, Zamba2-VL is competitive with leading Transformer-based open-weight VLMs of comparable scale, including the Molmo2, Qwen3-VL, and InternVL3.5 families, and substantially outperforms prior SSM-based and hybrid VLMs such as VL-Mamba, Cobra, and mmMamba. Inheriting the near-linear prefill compute and small, near-constant recurrent state of its Zamba2 backbone, Zamba2-VL delivers roughly an order of magnitude lower time-to-first-token (TTFT) than these Transformer baselines at matched parameter scale, with the efficiency gap most pronounced at the smaller 1.2B and 2.7B scales most relevant to on-device and edge deployment. We release three models -- 1.2B, 2.7B, and 7B -- together with inference code at this https URL.

---


### 111. [Multi-Objective Reference-Aligned Machine Unlearning](https://arxiv.org/abs/2606.00399)

**<font color=#1a73e8>作者：</font>** Rasa Khosrowshahli, Stephen Asobiela, Beatrice Ombuki-Berman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine unlearning aims to remove the influence of specific training samples while preserving the model's utility. Existing single-objective approaches, such as gradient ascent or random relabeling, often induce catastrophic forgetting due to conflicting optimization dynamics and unbounded forgetting objectives that cause the model to drift from its pre-trained knowledge. We propose Reference-Aligned UnLearning (RAUL), a multi-objective framework that jointly optimizes forgetting and retention by replacing unbounded loss maximization with a bounded KL alignment of predictions on forgotten samples toward a reference distribution representing unseen data, instantiated either as a uniform distribution or an empirical distribution from a held-out reference set, which constrains the forgetting objective and reduces gradient conflict with retention. The resulting multi-objective optimization (MOO) problem is solved via Jacobian descent, which aggregates multiple gradients into a direction that does not conflict. Our results demonstrate that RAUL achieves the closest gap compared to full retraining.

---


### 112. [Rethinking Amortized Neural Representations for High-Resolution Terrain Elevation Data](https://arxiv.org/abs/2606.00404)

**<font color=#1a73e8>作者：</font>** Haoan Feng, Xin Xu, Leila De Floriani  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Implicit neural representations (INRs) model a signal as a continuous coordinate-to-value function. For terrain elevation data, this supports analytic derivatives, arbitrary-resolution decoding, and a smooth surface model of the underlying heightfield. However, fitting and storing a separate INR for every tile does not scale to large terrain datasets. Amortized neural representations reduce this cost with a shared network: a new tile is mapped to a compact per-tile payload, and a shared decoder reconstructs the heightfield from it. Most such methods are hypernetworks that predict the payload in a single forward pass, while others recover it through a short per-tile optimization. These methods were developed primarily for natural images, and their suitability for terrain heightfields remains unclear. We introduce a controlled benchmark on a 1 m/pixel terrain dataset and evaluate three representative methods under a unified protocol. Observing a clear cross-domain gap, we propose HUVR+SIREN, a hypernetwork that adapts the strongest benchmarked method (HUVR) by replacing its coordinate decoder with a smooth, analytically differentiable one. It attains the best height and derivative fidelity on the benchmark with no additional per-tile storage and lower decode cost, and tolerates aggressive post-training quantization with negligible quality loss, giving a compact terrain neural format. Ablations and diagnostics further identify which design choices transfer to terrain and show that the per-tile bottleneck is already near its useful limit, leaving the remaining gap in the shared hypernetwork's architectural design.

---


### 113. [Masking Stale Observations Helps Search Agents -- Until It Doesn't: A Regime Map and Its Mechanism](https://arxiv.org/abs/2606.00408)

**<font color=#1a73e8>作者：</font>** Haoxiang Zhang, Qixin Xu, Zhuofeng Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon search agents accumulate large amounts of retrieved content across many tool calls, making context-budget efficiency increasingly important. A minimal intervention is to mask stale observations from the context as the trajectory progresses, but it remains unclear when this form of context management helps and why. We study observation masking through a systematic sweep over various agent backbones (4B to 284B parameters) and three retrievers on offline and live-web agentic search benchmarks. We find that the accuracy gain from masking follows an asymmetric inverted-U shape when plotted against the model's accuracy without context management: a plateau under weak retrievers, a peak when a strong retriever meets a mid-capacity model, and a sharp collapse when the model is saturated. This pattern reflects the interaction between retriever recall and the model's implicit filtering capacity, rather than either factor in isolation. Mechanistically, masking implements a token-for-turn trade-off: it removes observations the model has largely stopped attending to and pages the agent rarely re-opens. The added turns help when they convert failures into successes, but they fail when masking removes evidence the model would otherwise have used. We therefore reframe context management as a regime-dependent intervention and provide a holistic perspective for analyzing context use in agentic deep search. We release our scaffold and trajectories here (this https URL) to support future research.

---


### 114. [Auditing Near-Optimal Policies Can Be Exponentially Hard: Conditional Query Lower Bounds via Occupancy Rashomon Capacity](https://arxiv.org/abs/2606.00414)

**<font color=#1a73e8>作者：</font>** Ibne Farabi Shihab, Sanjeda Akter, Anuj Sharma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When many reinforcement-learning policies achieve near-optimal return, a post-hoc auditor may have to distinguish among many behaviorally distinct but return-equivalent policies. We formalize this phenomenon through an occupancy-measure analogue of Rashomon capacity: the metric entropy of the near-optimal occupancy region, computed relative to an audited deployment class. Because occupancy measures identify behavior only up to occupancy equivalence, we formulate auditing at the occupancy-class level and distinguish exact local-query oracles from noisy sample-query oracles. Our main exact-query result is conditional: if the audited class contains a $2/H$-separated near-optimal packing whose local signatures are $b$-sparse, then exact local-query auditing requires $\Omega(M/b)$ queries; when the packing realizes deployment-class capacity and $b=O(1)$, this becomes $\Omega(2^{\Hopt^\cF(\eps)})$. We give a finite discounted hidden-branch MDP attaining this bound and show the exact Bayes success law. For noisy hidden-trigger testing, we prove a mixture lower bound of order $M/\beta$, where $\beta$ is the per-sample KL signal, yielding $\Omega(2^{\Hopt^\cF(\eps)}/(\rho^2\Delta^2))$ for capacity-order packings with $\beta=O(\rho^2\Delta^2)$. We also provide a static target-recognition information lower bound, a transcript-compatible oracle-cover verification upper bound, and a canonical occupancy regularizer whose regularized audited capacity collapses when a trusted reference occupancy is available. Controlled benchmarks distinguish positive sparse-signature instances from high-capacity negative controls where exact auditing is easy, and map the noisy-trigger law to post-processed continuous-control and visual-RL auditing regimes.

---


### 115. [4D Radar Meets LiDAR and Camera: Cooperative Perception under Adverse Weather](https://arxiv.org/abs/2606.00416)

**<font color=#1a73e8>作者：</font>** Melih Yazgan, Iramm Hamdard, Qiyuan Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cooperative perception is important for autonomous driving but remains fragile when cameras and LiDAR degrade in adverse weather. We address this challenge by integrating 4D imaging radar as a weather-robust modality into collaborative perception and introducing a Doppler-guided spatial attention mechanism for multi-agent fusion. Our approach extends two representative backbones: a radar-camera pipeline where radar substitutes LiDAR, and a LiDAR-radar pipeline where radar complements LiDAR. To support evaluation, we release radar-augmented benchmarks, OPV2V-R and Adver-City-R, with physics-based LiDAR degradation. Experiments show strong robustness gains in fog and rain, including substantial improvements when radar replaces degraded LiDAR. Additional validation on MAN TruckScenes demonstrates transfer beyond simulation. Overall, our results highlight 4D imaging radar as a robust modality for all-weather collaborative perception. Dataset and code are available at: this https URL.

---


### 116. [Weak Critics Make Strong Learners: On-Policy Critique Distillation for Scalable Oversight](https://arxiv.org/abs/2606.00424)

**<font color=#1a73e8>作者：</font>** Can Jin, Jiakang Li, Rui Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language models become stronger, weak supervisors may fail to provide reliable labels, preferences, or final judgments for complex outputs, limiting both weak-to-strong generalization and scalable oversight. We study a more tractable form of weak supervision: using a weak model as a critic rather than as a labeler or judge. Instead of solving the task or selecting the correct answer, the weak critic only needs to provide a non-misleading revision direction that helps the strong model better use its own knowledge. We call this setting *weak-critic strong oversight*. We first show that weak critiques can improve frozen strong models at inference time, and that critique quality is key to this improvement. We then propose progressive on-policy critique distillation (**OPCD**), which filters high-quality critiques and distills critic-guided behavior into the strong model through adaptive self-teacher signals. Experiments on reasoning and alignment benchmarks show that our method improves strong models over training epochs, suggesting an effective path for scalable oversight with weak supervision.

---


### 117. [Canonicalized Stable-List Replay for Private Federated Continual Learning over Language-Model Embeddings](https://arxiv.org/abs/2606.00426)

**<font color=#1a73e8>作者：</font>** Ibne Farabi Shihab, Abu Sa-Adat Mohamed Moon-Im Al Ahsan, Anuj Sharma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated continual learning (FCL) lets distributed clients adapt language-model heads to evolving NLP tasks without sharing raw text. Under user-level differential privacy (DP), replay-based continual learning faces a structural obstacle: clients can release only small noisy lists of candidate replay summaries, and those lists are unordered across clients. We introduce Canonicalized Stable-List Replay (CSLR), where clients privately produce candidate replay distributions over a shared sentence-embedding space and the server aligns them using signatures induced by public anchor sentences. The anchors provide identifiability for aggregation rather than additional replay data. We prove that, under an observable anchor-signature margin, $O(\log(N/\eta)/p)$ anchors distinguish $N$ candidate list elements with probability at least $1-\eta$, and we give a scoped anchorless non-identifiability result for unordered-label oracle models. Across five seeds on continual classification, NER, and dialogue benchmarks, CSLR improves the final average task metric by 3.9--5.6 points over the strongest non-CSLR DP baseline at $\eps=4$ under the reported replay-release budget, while also outperforming Hungarian and optimal-transport matchers. The formal privacy guarantee covers replay release; end-to-end private training additionally requires composition with a private optimizer for task-head updates.

---


### 118. [Topology-Aware State Abstraction with Tangle Cores for Markov Decision Processes](https://arxiv.org/abs/2606.00427)

**<font color=#1a73e8>作者：</font>** Ibne Farabi Shihab, Sanjeda Akter, Anuj Sharma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> State abstraction in reinforcement learning is usually formulated as a partition of states based on reward and transition similarity. This excludes a common structural pattern in navigation, graph, and hierarchical decision problems: interface states such as doors, hubs, and bottlenecks naturally participate in more than one region. We introduce \emph{tangle-core abstraction}, an overlapping state-abstraction framework based on graph tangles of empirical transition graphs. The method constructs abstract states from consistently oriented low-order separations and represents shared interfaces through a membership kernel rather than a hard partition. We give value-preservation guarantees for the induced overlapping abstract MDP under an explicit action-consistency condition, identify an interior-homogeneity/boundary-leakage error decomposition, and prove a quantitative interface-overlap result showing when hard partitions incur an avoidable boundary error. Empirically, tangle-core abstractions achieve favorable compression--return tradeoffs against reward-aware, learned, topological-map, and graph-partitioning baselines across bottlenecked tabular domains, procedurally generated mazes, and MiniGrid representations. We also identify a clear failure regime in which transition topology is uninformative, where tangles predictably offer little benefit. These results position graph tangles as an effective topology-aware abstraction prior for decision problems with shared interface structure.

---


### 119. [Finer Parameter Steps for Low-Rank PEFT: A Controlled Study with CP Tensor Adapters](https://arxiv.org/abs/2606.00428)

**<font color=#1a73e8>作者：</font>** Xinjue Wang, Xiuheng Wang, Yejun Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank adapters are usually compared by sweeping a small set of ranks, but the rank also fixes the resolution of the parameter budget. For a $2048{\times}2048$ OPT attention projection, increasing LoRA by one rank stores $4096$ trainable scalars, leaving large gaps between feasible low-budget adapter sizes. This paper asks whether a tensorized adapter with finer capacity increments changes the observed accuracy--budget trade-off. We instantiate this question with fixed-component canonical polyadic (CP) tensor adapters. Under a $32{\times}64{\times}32{\times}64$ tensorization, one normalized CP component stores $193$ trainable scalars per projection, about $21$ times smaller than one LoRA rank step. We compare CP adapters and LoRA on OPT-1.3B across SST-2, RTE, and BoolQ under matched target modules, training protocol, data caps, and seed schedules. CP trains stably and fills the gaps between LoRA ranks, but the effect is task-dependent: SST-2 reaches an early low-budget plateau, BoolQ benefits from additional CP components before saturating slightly below LoRA, and RTE remains LoRA-favored. Finer parameter steps are therefore useful for diagnosing PEFT budget sensitivity, but they do not by themselves guarantee a better accuracy--budget curve.

---


### 120. [Variance-sensitive Thompson sampling for generalised linear bandits, revisited](https://arxiv.org/abs/2606.00431)

**<font color=#1a73e8>作者：</font>** Tom Perneczky, Marc Abeille, David Janz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We prove a variance-sensitive regret bound for Thompson sampling in stochastic generalised linear bandits. The argument assumes a warm-up, after which the regret is controlled through using the Gaussian Poincaré inequality. This bypasses the point at which previous optimism-based analyses break down. Removing the warm-up while retaining the same variance-sensitive scaling remains open, and appears nontrivial.

---


### 121. [EST-PRM: Stress-Testing Process Reward Models Before They Become Load-Bearing](https://arxiv.org/abs/2606.00437)

**<font color=#1a73e8>作者：</font>** Ibne Farabi Shihab, Fariya Afrin, Sanjeda Akter 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Process reward models (PRMs) are widely used in language-model training with dense step-level supervision. They assume PRM scores are stable proxies for step correctness under label-preserving transformations. These transformations change reasoning structure but preserve final answers. We argue this assumption is not well validated. Such transformations can change how PRM scores relate to correctness signals, leading to different failure modes across this http URL address this gap, we introduce \textbf{EST-PRM}, a stress-testing framework for dense process rewards. It applies three transformations: (1) step inflation, (2) dependency-aware step reordering, and (3) confidence markers. A vulnerability decomposition is defined that separates reward inflation from loss of correctness sensitivity. Five PRM-style models are evaluated on 4,687 reasoning chains from MATH-500, GSM8K, and this http URL results indicate clear differences in vulnerability patterns across models. Math-Shepherd shows the strongest sensitivity to position perturbations, with a Pearson correlation drop of $0.152 \pm 0.038$ and a $32.8 \pm 4.9\%$ score inflation rate. Qwen2.5-Math-PRM is most affected by step inflation, reaching a $47.6 \pm 4.3\%$ inflation rate. Confidence-based perturbations also distort reward calibration, revealing inconsistencies in correctness estimation. Three mitigation strategies are evaluated, highlighting trade-offs between robustness coverage and false-positive rates.

---


### 122. [Exploiting weight-space symmetries for approximating curvature](https://arxiv.org/abs/2606.00442)

**<font color=#1a73e8>作者：</font>** Artem Artemev, Rui Xia, Benjamin M. Boyd 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many machine learning techniques rely on approximating a loss function's curvature, but this is notoriously hard to do at the scale of modern deep networks. Surprisingly, no previous work has exploited the curvature constraints that arise from well known weight-space symmetries in loss landscapes. By analytically averaging over group actions that leave the loss invariant, we construct structured Hessian approximations from single gradients that can be tractably estimated, stored, and inverted. The choice of user-specified symmetry group directly governs the trade-off between approximation accuracy and computational cost. Moreover, our framework provides a unifying theoretical lens for viewing existing methods; in particular, a specific choice of symmetry group recovers Shampoo/Muon-like curvature estimates. We validate our method on a range of network architectures, and deploy it to second-order optimization benchmarks, including a small language model. Our curvature estimation framework might find applications in other machine learning problems such as uncertainty estimation, continual learning, compression/pruning, training data attribution, and more.

---


### 123. [Real-Time Physics Simulation with Dynamic Mesh-Gaussian Reconstructions](https://arxiv.org/abs/2606.00444)

**<font color=#1a73e8>作者：</font>** Adrian Ramlal, John S. Zelek  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Integrating dynamic 3D reconstructions into physics simulation requires fixed mesh topology for efficient collision detection, but state-of-the-art methods like DG-Mesh produce varying topology optimized for geometric quality. We investigate whether topology conversion can enable physics integration while preserving reconstruction fidelity. We propose a dual-representation framework combining fixed-topology meshes for physics with Gaussian splatting for rendering, achieving 4.65$\times$ speedup over varying-topology baselines through runtime vertex buffer updates. We evaluate two conversion strategies, temporal correspondence tracking and template-based projection, against native fixed-topology methods (MaGS) on the DG-Mesh dataset. Our evaluation reveals that both conversion approaches incur 65-80% geometric degradation, producing results inferior to MaGS despite DG-Mesh's superior initial quality. This demonstrates that high-quality reconstruction and physics-compatible topology represent fundamentally distinct objectives that cannot be reconciled through post-processing. Our findings inform future development of physics-aware reconstruction methods and our framework enables real-time simulation with any fixed-topology approach.

---


### 124. [DarkVesselNet: Multi-Modal Remote Sensing and Trajectory Reasoning for Dark Vessel Detection](https://arxiv.org/abs/2606.00445)

**<font color=#1a73e8>作者：</font>** Arun Sharma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dark vessel detection requires fusing what vessels report through AIS with what satellites observe through radar and optical sensors. DarkVesselNet is a multi-modal remote sensing stack that combines Sentinel-1 SAR, Sentinel-2 optical imagery, geospatial foundation model backbones, AIS trajectory reasoning, TGARD-style gap detection, and a Pi-DPM-inspired anomaly head. The repository exposes the system as a tested Python package and a public Hugging Face Space. The paper presents the sensor stack, backbone abstraction, fusion path, anomaly head, and current validation. The evidence currently available is software-grounded: tests for SAR speckle filtering, optical band ratios, Haversine distance, TGARD gap emission, sensor coregistration, backbone token shapes, and differentiable anomaly scoring.

---


### 125. [GeoSAM-3D: Geodesic Prompt Propagation for Open-Vocabulary 3D Scene Segmentation from Monocular Video](https://arxiv.org/abs/2606.00447)

**<font color=#1a73e8>作者：</font>** Arun Sharma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary 3D scene segmentation usually assumes RGB-D video, calibrated multi-view imagery, or a reconstructed mesh. GeoSAM-3D studies a lighter setting: a user uploads a short monocular video, clicks or names an object in one frame, and receives a propagated 3D mask over a Gaussian scene. The implementation combines frozen image and video foundation models with a monocular 3D Gaussian Splatting reconstruction and a differentiable graph-geodesic propagation kernel over Gaussian centroids. The central design choice is to propagate prompts by heat-kernel distance on the reconstructed scene graph, rather than by Euclidean nearest neighbors in 3D. This preserves continuity around curved surfaces and reduces leakage across nearby but disconnected objects. This paper describes the repository state, the mathematical kernel implemented in this http URL, the feature head trained from Segment Anything masks, and the validation already present in the codebase. The evaluation protocol separates implementation validation, graph propagation quality, leakage control, and interactive latency.

---


### 126. [Optimizing 3D Gaussian Splatting via Point Cloud Upsampling](https://arxiv.org/abs/2606.00450)

**<font color=#1a73e8>作者：</font>** Adrian Ramlal, Yan Song Hu, John S. Zelek  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) is a technique for creating and rendering 3D scenes, however its performance depends heavily on the quality of initial seed points. To improve 3DGS initialization, this study presents and evaluates several point cloud upsampling approaches: linear interpolation, triangular interpolation, spline-based surface reconstruction, moving least squares surface fitting, and Voronoi-based point generation. Additionally, this research introduces a depth-guided point lifting method that leverages depth maps to maintain geometric consistency with Structure-from-Motion (SfM) reconstructions. Through extensive experiments on the Mip-NeRF360 and Replica datasets, the proposed methods demonstrate improvements in reconstruction quality across diverse scene types. Results indicate that different upsampling strategies excel in different scenarios: surface reconstruction methods perform better with organic, detailed scenes, while simpler interpolation approaches are more suited for scenes dominated by piecewise-smooth geometries. In comparison, the depth-guided approach shows promise for adding geometry-aware points across the entire scene, importantly in texture-less regions. These findings, which provide preliminary practical guidelines for selecting appropriate upsampling methods based on scene characteristics and computational constraints, advances the understanding of how point cloud initialization affects 3DGS quality.

---


### 127. [Beyond Static Gaussians: An Empirical Investigation of Architectural Paradigms for Dynamic 3D Scene Reconstruction](https://arxiv.org/abs/2606.00452)

**<font color=#1a73e8>作者：</font>** Adrian Ramlal, John S. Zelek  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic scene reconstruction via 3D Gaussian Splatting (3DGS) has emerged as a compelling approach for representing evolving environments, yet understanding trade-offs between methodologies remains crucial. This paper presents a comprehensive analysis of dynamic 3DGS methods, categorizing them into two paradigms: structure-guided methods employing auxiliary representations (deformation fields, canonical spaces, grids) to model temporal changes, and gaussian-centric methods encoding dynamics directly into primitives via continuous functions or 4D representations. We evaluate representative methods from both paradigms on the D-NeRF benchmark. Our findings reveal that structure-guided methods achieve superior reconstruction fidelity and compact model sizes, while gaussian-centric approaches demonstrate significantly higher rendering speeds enabling real-time performance, though with greater quality variability and potentially substantial storage overhead. This analysis highlights a fundamental trade-off between reconstruction quality/compactness versus rendering speed, providing insights to guide future research and application development in dynamic scene reconstruction.

---


### 128. [An explainable hierarchical self attention-based approach for tremor detection in the time domain](https://arxiv.org/abs/2606.00461)

**<font color=#1a73e8>作者：</font>** Timothy Odonga, Jeanne M. Powell, Mark Saad 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tremor is a common movement disorder associated with conditions like Parkinson's disease and Essential tremor, traditionally diagnosed through expert clinician assessment. Current automated detection methods rely on frequency-domain features informed by clinical expertise. In this work, we present an explainable, two-stage hierarchical framework for tremor detection in the time domain that learns tremor patterns directly from 3D kinematic marker time-series data across entire tremor-provoking trials. Our framework combined a deep convolutional and long short-term memory network to learn tremor representations from short, discrete, non-overlapping time segments of kinematic time series data from trials, which are then processed by a vision transformer that models their long-term temporal dynamics of time segment features for trial (session) level classification. Evaluated across nine body parts, the framework achieved F1-scores of 0.594 - 0.947 depending on body parts (average: 0.765), falling short of the frequency-domain state-of-the-art performance (0.909) while requiring minimal preprocessing. Attention weights and gradient-based class activation maps (Grad-CAM) identified time-domain features of tremor across body parts. This proof of concept demonstrated the feasibility of data-driven time-domain modeling for tremor detection across anatomically diverse body parts, while reducing reliance on expert-engineered spectral features and providing posthoc interpretability of temporal and anatomical patterns of tremor.

---


### 129. [MUSCLE-NET: Predicted-Multiscale-Aware Network for Pedestrian Trajectory Forecasting](https://arxiv.org/abs/2606.00471)

**<font color=#1a73e8>作者：</font>** Yu Liu, Ming Huang, Xiao Ren 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate pedestrian trajectory prediction is essential for safe navigation in autonomous driving and intelligent transportation systems. Despite substantial progress made by recent methods, most existing approaches are limited in fully exploiting diverse observations and often overlook the scale dependency of future motion, treating multiscale features uniformly regardless of underlying motion dynamics. This limits their robustness across diverse pedestrian behaviors. To address these challenges, we propose a Predicted-MUltiSCale-Aware Network (MUSCLE-NET) for Pedestrian Trajectory Forecasting that integrates complementary multimodal cues with scale-adaptive prediction mechanisms. The proposed framework is built upon a Multiscale Multimodal Feature Extraction (MMFE) module, which combines multiscale representation, modality-aware recalibration, and directional cross-modal fusion to construct semantically aligned representations from bounding boxes, velocities, and pose information. Building on these features, a Multiscale Enhanced Hierarchical Prediction (MEHP) module performs prediction-aware future-motion refinement via a probabilistic coarse predictor, scale-aligned fusion, and progressive refinement, adaptively selecting scale-relevant cues to mitigate spatial drift. Extensive experiments on the JAAD and PIE benchmarks demonstrate that the proposed MUSCLE-Net achieves competitive performance and consistent gains compared with state-of-the-art trajectory prediction methods.

---


### 130. [CodeCytos: AI-assisted spatial molecular imaging analysis via code-augmented agent action space](https://arxiv.org/abs/2606.00472)

**<font color=#1a73e8>作者：</font>** Hung Q. Vo, Huy Q. Vo, Son T. Ly 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conventional tissue image analysis software provides foundational capabilities for cellular analysis, including segmentation, basic morphological feature extraction, and spatial organization analysis. However, these tools often require manual intervention and are not well integrated with code-driven automation, limiting efficiency and scalability for complex spatial tissue studies. In addition, they offer limited flexibility for custom analyses, as they typically support only a fixed set of pre-implemented spatial cellular features. To address these limitations, we propose CodeCytos, a coding-based reasoning agent framework that enables dynamic, programmable interaction with spatial molecular imaging data to improve automation and customization. CodeCytos is designed to streamline the exploration of custom spatial cellular features and adapt to diverse research needs. We demonstrate its utility through case studies on four expert-curated datasets from distinct tissue types: frontal cortex, non-small-cell lung cancer, pancreas, and tonsil. We evaluate CodeCytos under a realistic minimal prompt setting, where bioscientists pose simple questions without task-specific instructions or contextual information about spatial cellular analysis, and benchmark multiple LLM backbones with strong coding capabilities. We further show that incorporating tailored, domain-agnostic few-shot in-context coding-reasoning examples (randomly sampled demonstrations outside the spatial analysis domain) can substantially improve performance without requiring costly, expert-crafted in-domain demonstrations. Overall, CodeCytos outperforms baseline approaches, highlighting the potential of code-action agents to assist with custom feature exploration in spatial molecular imaging and to accelerate biomarker discovery.

---


### 131. [Do Text Edits Generalize to Visual Generation? Benchmarking Cross-Modal Knowledge Editing in UMMs](https://arxiv.org/abs/2606.00477)

**<font color=#1a73e8>作者：</font>** Xin Gao, Cheng Yang, Chufan Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Unified multimodal models (UMMs) have emerged as a promising paradigm for general-purpose multimodal intelligence. As they are deployed in real-world applications, effectively updating internal knowledge becomes critical. While knowledge editing has matured for text-only models, it remains unclear whether edits that successfully modify textual outputs also transfer to image generation in UMMs. To study this question, we introduce UniKE, the first benchmark for cross-modality knowledge editing in UMMs, comprising 2,971 edit subjects spanning attribute and relation edits. Using VQA-based visual verification, we reveal a striking modality gap: text-side efficacy can reach approximately 92%, whereas the best overall VQA accuracy under direct image generation is only 18.5%. We further propose Reasoning-augmented Parameter Editing, which explicitly activates edited knowledge before generation and improves overall VQA accuracy for all evaluated model-editor pairs, with gains up to 18.6 percentage points. Mechanistic analysis shows that this gap is associated with partial alignment between edited textual representations and the conditioning pathways for visual generation, where edits sufficient for text outputs may remain too weak or misaligned to steer image synthesis. These findings show that textual knowledge edits do not guarantee reliable cross-modality transfer and motivate modality-aware editing methods. Our code and data are available at this https URL.

---


### 132. [Stochastic Analysis of Cybersecurity Defense Strategies Under Single Attack Scenario](https://arxiv.org/abs/2606.00481)

**<font color=#1a73e8>作者：</font>** Song-Kyoo Kim  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This research presents a novel stochastic framework for proactive cybersecurity defense timing under a single attack scenario. The approach models the defense process as a continuous observation mechanism in which the defense instant and the subsequent observation slot follow independent exponential distributions. Laplace-Carson transforms combined with first-excess theory yield the joint detection function that brackets the attack moment. Marginalization under Markovian Poisson arrivals then produces the probability density of the defense moment and conditional expectations of pre-attack and post-attack observation times. These closed-form results enable quantitative assessment of defense timing sensitivity to threat intensity and support precise calibration of observation parameters for low-latency proactive measures. Major contributions include the explicit derivation of marginal distributions and expected values, visualization of defense moment density, and the bridging of stochastic duel methodology with practical cybersecurity applications.

---


### 133. [TAPS: Target-Aware Prefix Tree Selection for Diffusion-Drafted Speculative Decoding](https://arxiv.org/abs/2606.00487)

**<font color=#1a73e8>作者：</font>** Zhuoyu Wang, Junnan Huang, Xinyu Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Using a diffusion model for parallel drafting is a promising approach for speculative decoding. By predicting tokens at multiple future positions in a single forward pass, diffusion drafters substantially reduce drafting latency. However, this shifts the bottleneck to verification: verifying a single sequence limits acceptance length, while verifying large draft trees incurs excessive target-model latency. We identify a key mismatch in existing draft-tree methods: existing diffusion-tree methods rank nodes by the marginal probability, ignoring that verification is prefix-conditioned. As a result, they may verify unreachable descendants of rejected prefixes, increasing latency with limited acceptance gains. To address this, we propose TAPS, a target-aware prefix selection method that turns diffusion marginals into path-conditioned acceptance estimates. TAPS then selects a compact prefix-closed subtree under a fixed verification budget, improving the acceptance-cost tradeoff rather than simply expanding the draft tree. Experiments across diverse datasets and model families demonstrate that TAPS achieves up to 7.9x lossless end-to-end speedup over vanilla autoregressive decoding, outperforming state-of-the-art DFlash and DDTree by 1.36x and 1.74x respectively. Our work is available at this https URL

---


### 134. [3D Segment Anything Model with Visual Mamba for Diagnosing Placenta Accreta Spectrum](https://arxiv.org/abs/2606.00489)

**<font color=#1a73e8>作者：</font>** Yuliang Zhang, Fang He, Lulu Peng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Placenta Accreta Spectrum (PAS) is a rare but highly dangerous obstetric disease. Early and accurate PAS diagnosis is critical for maternal health. Traditional PAS diagnosis relies on experienced doctors by analyzing the cesarean history and Magnetic Resonance Imaging (MRI) data. However, district-level hospitals often lack the expertise and resources for accurate PAS diagnosis. To address these challenges, we establish the first MRI-based PAS dataset, which includes both fine-grained segmentation and classification annotations. Meanwhile, diagnosing PAS can be significantly enhanced by segmenting lesion areas from MRI images of the uterus. To achieve automatic PAS diagnosis, we propose 3DSAMba, a novel feature learning framework for effective lesion segmentation. More specifically, we first design a 3D Segment Anything Model (SAM) and incorporate medical domain information into the model through an efficient adapter mechanism. In addition, we introduce a Multi-Level Aggregation Mamba (MLAM) to aggregate feature maps across different levels and a Fusion State Space Model (FSSM) to fuse multi-scale features from both the encoder and decoder. Finally, we apply segmentation masks to the original MRI images through element-wise multiplication, effectively isolating lesion areas for more accurate PAS diagnosis. Extensive experiments validate that our framework significantly improves the PAS diagnostic performance. To facilitate further research in PAS diagnosis, we have released the dataset and source code at this https URL.

---


### 135. [Pre-Deployment Robustness Stress Testing for CT Segmentation Systems Using Clinically Motivated Multi-Corruption Augmentation](https://arxiv.org/abs/2606.00491)

**<font color=#1a73e8>作者：</font>** CholMin Kang, Jonghyun Chung, Amanpreet Kaurb 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning-based CT segmentation systems often achieve high accuracy on clean benchmark images, but their performance may degrade under heterogeneous clinical imaging conditions such as noise, resolution loss, contrast variation, intensity shift, and artifacts. This instability can limit reliable deployment in real-world medical imaging workflows.
We propose Robustness via Augmented Multi-corruption Pipeline (RAMP), a robustness-oriented augmentation framework for CT segmentation. RAMP combines anatomically constrained spatial perturbations, CT intensity transformations, and stochastic multi-corruption composition to expose models to clinically plausible image degradation during training.
Across two CT segmentation evaluation settings, RAMP achieved the strongest corrupted-image performance and the smallest clean-to-corrupted robustness gap. In the five-organ noisy evaluation benchmark, RAMP improved mean corrupted Dice from 0.610 to 0.753 and reduced the robustness gap from 0.264 to 0.064 compared with the nnU-Net baseline. In Abdomen1K, RAMP improved mean corrupted Dice from 0.633 to 0.789 and reduced the robustness gap from 0.290 to 0.070. Although RAMP did not achieve the highest clean-image Dice, it substantially mitigated worst-case segmentation collapse under severe image degradation.
These results suggest that multi-corruption augmentation can serve as a practical pre-deployment strategy for improving the reliability of CT segmentation systems in heterogeneous clinical environments.

---


### 136. [Torus Graphs for Large Scale Neural Phase Analysis](https://arxiv.org/abs/2606.00496)

**<font color=#1a73e8>作者：</font>** Jack Goffinet, Casey Hanks, David E. Carlson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Oscillatory neural signals such as electroencephalography (EEG) and local field potentials (LFPs) show phase relationships that coordinate communication across brain regions. Modern recordings capture hundreds of channels across many frequency bins, yet standard phase analyses are restricted to only a few variables. The Torus Graph (TG) model, an exponential-family distribution over phases whose univariate and pairwise potentials generalize von Mises distributions, infers principled structure among oscillations but models only static, undirected dependencies and is limited to $\sim \! 100$ variables because its score matching inference scales as $\mathcal{O}(d^{6})$. We introduce a stochastic score matching procedure that reduces the per-iteration cost to $\mathcal{O}(d^{2})$, enabling inference on datasets with thousands of variables. This scalable foundation supports analyses of 1,860 frequency-phase features from multi-electrode LFPs and enables two extensions previously inaccessible to TGs or classical circular statistics: (i) a TG Hidden Markov Model capturing state-dependent phase-coupling changes (e.g., spindle-related states during sleep) and (ii) an autoregressive TG inferring directional interactions via transfer-entropy estimation. Applied to LFP recordings, these models reveal state-dependent phase-interaction patterns between wakefulness and NREM sleep. Together, they enable systematic, large-scale mapping of dynamic and directional phase relationships across brain and cognitive states.

---


### 137. ["I Strongly Suspect This Website Is a Scam": Benchmarking PII Leakage and Detection without Defense in Autonomous Web Agents](https://arxiv.org/abs/2606.00497)

**<font color=#1a73e8>作者：</font>** Soham Roy, Sarthakbrata Halder, Arya Bharaty 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deceptive web content, widely instantiated across the internet and commonly known as \textit{social-engineering attacks}, manipulates autonomous web agents into submitting users' personally identifiable information (PII) to attacker-controlled endpoints. In this paper, we show that social-engineering attacks are highly effective at extracting critical-tier PII from frontier web agents, posing a severe risk to deployed agentic systems. To quantify this risk, we introduce \textbf{\textsc{Scammer4U}}, a pre-registered benchmark of 91 attacker-controlled environments and 10 benign-twin baselines, spanning 8 attack vectors and 16 site categories on an 8-axis factorial taxonomy that isolates the causal contribution of individual attack design factors. Across frontier agents, we find that critical-tier PII leakage reaches 54--93\% under no privacy guidance, compared to 0\% on benign-twin baselines, confirming that leakage is attack-attributable rather than incidental form-filling. Escalating prompt-level mitigation yields sharply model-dependent reductions across the four families and remains insufficient to reliably prevent critical PII submission at the pooled level. Most critically, we identify a detection--action gap: agents whose reasoning an independent LLM judge confirms has flagged the site as suspicious still submit critical PII in 35.9\% of sessions, versus 66.1\% when no suspicion is verbalized, a 30.2\% gap robust across all four model families. Our findings reveal that defenses conditioned on the agent's own recognition of an attack are gating on the wrong signal, motivating output-level interception of outbound submissions that operates independently of the agent's reasoning loop.

---


### 138. [OptiWorld: Optimal Control for Video World Generation under Physical Constraints](https://arxiv.org/abs/2606.00499)

**<font color=#1a73e8>作者：</font>** Yu Yuan, Jianhao Yuan, Xijun Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation models are becoming a scalable form of world models, but they mainly generate plausible motion rather than proactively control or optimize the underlying dynamics. As a result, an object in the generated video may follow trajectories that are unsafe, not smooth, inefficient, or physically inconsistent. In this work, we propose \textbf{OptiWorld}, a framework that brings classical optimal control into video generation at inference time. OptiWorld first extracts a compact, task-relevant world state, then plans an optimal trajectory under physical constraints, and finally renders the video conditioned on this trajectory. We formulate planning as a geometric problem on a continuous manifold, which converts 3D geometry and task-dependent physical constraints into a unified planning geometry. By adding this optimal-control layer, OptiWorld generates videos with preferable dynamics, demonstrating strong potential in multiple tasks including goal-conditioned image-to-video generation, video dynamics editing, and counterfactual generation.

---


### 139. [TabChange: Precise Attribute Changes in Tabular Data](https://arxiv.org/abs/2606.00503)

**<font color=#1a73e8>作者：</font>** Arjun Dahal, Yu Lei, Raghu N. Kacker 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modifying an attribute in tabular data often introduces an unnatural instance by breaking its relationships with other attributes. The modified instance must be both natural and minimally changed from the original instance. This paper addresses the challenge of generating such a modified instance. We identify key limitations in existing approaches: generative models either don't support instance-level attribute editing or, in the case of methods like CVAE, retain attribute information in the latent space, leading to unnecessary modifications. To solve this, we propose TabChange, an approach that analyzes the relationship between the attribute of interest and other attributes in the dataset. If the relationship is weak, it simply flips the attribute; if it is strong, it uses an adversarial framework that removes information about the attribute in the latent space representation. This removal enables precise modifications, making only the necessary adjustments to maintain naturalness. Our experiments across seven datasets show that TabChange generates counterfactuals in attributes that are comparable in naturalness and are more proximal to their original instances. This leads to a higher number of valid counterfactuals and a lower number of invalid counterfactuals compared to the baselines.

---


### 140. [EnergyMamba: An Uncertainty-Aware Graph-Enhanced Selective State Space Model for Energy Consumption Prediction](https://arxiv.org/abs/2606.00506)

**<font color=#1a73e8>作者：</font>** Dahai Yu, Rongchao Xu, Lin Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Energy consumption prediction is essential for efficient grid management, demand-side optimization, and sustainable energy planning. Although advanced machine learning methods have been employed for better prediction performance, existing works have two key limitations: (1) they usually formulate this task as a purely time-series prediction problem without explicitly modeling the spatial dependencies among different regions, and (2) they fail to provide reliable predictions with uncertainty estimates under abnormal situations such as extreme weather events. To advance existing research, we propose EnergyMamba, an uncertainty-aware spatiotemporal learning framework for accurate and reliable energy consumption prediction, which comprises two key components: (i) a novel Graph-Enhanced Selective State Space Model (GE-Mamba) that injects spatial context learned from the grid topology into the temporal dynamics, enabling coupled spatiotemporal modeling, and (ii) an Adaptive Sequential Conformalized Quantile Regression (AS-CQR) module, which includes locally adaptive normalization and an online feedback mechanism to dynamically calibrate prediction intervals under potential distribution shifts. We evaluate EnergyMamba on four large-scale real-world datasets from Florida, New York, and California. Results show EnergyMamba achieves around 5% improvement in prediction accuracy and 6% improvement in uncertainty quantification over 15 state-of-the-art baselines.

---


### 141. [Structure-Aware Consistency Priors for Shape from Polarization in Complex Media](https://arxiv.org/abs/2606.00509)

**<font color=#1a73e8>作者：</font>** Kaimin Yu, Puyun Wang, Huayang He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering surface normals from single view polarization images in complex media remains challenging. This paper focuses on ice as a representative complex medium, where intricate light matter interactions lead to a nonlinear mapping between polarization observations and surface normals. To address this, a structure-aware polarization prior based on autocorrelation functions is proposed to capture the local spatial consistency of AoLP. Building on this, a dual-branch network (IceSfP) is designed to integrate raw polarization features with priors via cross modal attention and multi-scale feature fusion, enabling accurate surface normal estimation under complex media conditions. To evaluate the method, the first real-world ice SfP dataset is constructed. Experimental results show that the method outperforms existing approaches across all metrics, achieving a MAE of 16.01 deg, which is 2.74 deg lower than the second-best method. The framework provides a generalizable solution for high-precision geometric perception in complex media.

---


### 142. [Saliency-Aware Model Merging](https://arxiv.org/abs/2606.00511)

**<font color=#1a73e8>作者：</font>** Jungin Park, Jiyoung Lee, Kwanghoon Sohn  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model merging aims to consolidate multiple task-specific models fine-tuned on different datasets into a unified architecture that performs cross-domain proficiency. Current data-free model merging methods often struggle to scale as they rely on simple parameter-level heuristics that ignore inter-layer dependencies and non-uniform distribution of expertise. This work proposes SA-Merging, which is built upon connectivity-based saliency formulations from structural pruning (e.g., SynFlow) and extends them to the data-free model merging setting. We define a saliency score over task vectors relative to a shared base model, and further introduce merge-aware modulation that incorporates agreement across experts to mitigate task interference. Based on this formulation, an iterative saliency-aware merging procedure progressively removes non-informative updates while preserving end-to-end connectivity. Furthermore, we extend SA-Merging to introduce rank-wise saliency decomposition for LoRAs without compromising their structural integrity. Extensive experiments on vision and language tasks demonstrate the effectiveness of our saliency-based approach, further reducing the gap between data-free and test-time adaptation methods.

---


### 143. [Semi-Supervised Learning with Noisy Proxy Covariates: Generalization Bounds and Distribution Regression](https://arxiv.org/abs/2606.00512)

**<font color=#1a73e8>作者：</font>** Kwangho Kim, Jisu Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In many modern machine learning pipelines, abundant pretrained representations serve as noisy proxy covariates, while task-specific labels remain scarce. We study semi-supervised regression in this setting, and propose a simple two stage estimator that learns kernel eigenfeatures from all proxy covariates and fits a ridge predictor on labeled data. We derive finite sample bounds showing that fast labeled sample rates are recovered when proxy perturbation is controlled and unlabeled proxy covariates are sufficiently abundant. We also show that distribution regression is a direct special case, with analogous guarantees when the finite bag size is large enough. Experiments show consistent gains over supervised and semi-supervised baselines, especially in low label regimes.

---


### 144. [Generate in Reconstruction Space, Match in Semantic Space: Transport Geometry for One-Step Generation](https://arxiv.org/abs/2606.00514)

**<font color=#1a73e8>作者：</font>** Hugues Van Assel, Edward De Brouwer, Saeed Saremi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative modeling and self-supervised representation learning (SSL) optimize structurally different objectives: generative training rewards distributional fidelity, while SSL rewards semantic coherence. Yet recent work repeatedly finds that SSL features improve generative training, though the mechanism of this synergy remains unclear. Here, we study the benefits of SSL in generative modeling in the framework of one-step generation where the role of representation is explicit: frozen SSL features are used to match generated samples to real data. We use the Sinkhorn divergence in that feature space, providing a tractable surrogate for the Wasserstein distance, the population-level discrepancy approximated by Fréchet-style evaluation metrics (such as FID). We find that this objective becomes highly effective when computed in a semantically structured SSL feature space (a 39$\times$ reduction in ImageNet FID). We trace this behavior primarily to matching estimation: semantic SSL features that suppress nuisance reconstruction details induce a more compact geometry, making distribution matching more tractable. As a consequence, the best training SSL features need not match the features used by the evaluation metric. In particular, we show that using Inception as the feature extractor can improve FID while degrading matching stability and sample quality, revealing a form of metric hacking. Using extensive experiments on ImageNet, we identify which SSL feature families lead to best generation performance and show that matching stability is a quantitative criterion for selecting them. Code is available at this https URL.

---


### 145. [An Effective Solution for the CVPR 2026 8th UG2+ Challenge Track 3: Dynamic Object Segmentation in Turbulence](https://arxiv.org/abs/2606.00522)

**<font color=#1a73e8>作者：</font>** Hongzhen Li, Miao Yu, Leilei Cao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we present our solution for the 8th UG2+ Challenge (CVPR 2026) Track 3: Dynamic Object Segmentation in Turbulence (DOST). Our method is built upon the strong baseline framework Segment Any Motion (SegAnyMo), which provides powerful mask generation and motion tracking capabilities. To further boost the segmentation performance under severe atmospheric distortions, we propose two key improvements. First, we employ a data-centric domain adaptation strategy. We significantly expand our training data by incorporating selected sequences from the DAVIS dataset alongside a subset of the DOST dataset, and apply simulated atmospheric fluctuation degradations to enhance the model's robustness against complex geometric distortions. Second, we introduce a spatio-temporal post-processing module. This refinement step effectively removes persistent boundary-connected false foregrounds and short-lived fragmented noise, while strictly preserving genuine small targets and maintaining original individual labels across frames. With these combined strategies, our proposed method ranks the 2st place in the challenge.

---


### 146. [State Machine Guided Multi-Relational Synthetic Data from Logs for Anomaly Detection](https://arxiv.org/abs/2606.00531)

**<font color=#1a73e8>作者：</font>** Aja Khanal, Apurva Narayan  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Software systems generate massive unstructured logs that record execution behavior, failures, and interactions across components, yet existing log anomaly detection methods treat these logs primarily as flat sequences of templates, overlooking the relational execution structure that governs how events co-occur and evolve over time. We propose a framework that discovers this hidden structure by recovering an execution state machine directly from logs and inducing a corresponding multi-table relational schema connecting traces, events, states, transitions, and parameters. This discovered state machine serves as a generative prior to produce realistic multi-relational synthetic data that preserves structural, temporal, and process constraints while amplifying rare but valid execution behaviors. We assess the fidelity of the generated data through constraint validation, distributional similarity, and process-level metrics, and demonstrate its usefulness by showing that augmenting real logs with the synthetic relational data significantly improves anomaly and bug detection on held-out real datasets compared to sequence-based baselines and naive oversampling. Our results show that execution logs implicitly encode a relational database governed by a latent state machine, and that recovering this structure enables principled synthetic data generation for robust and interpretable anomaly detection.

---


### 147. [KACE: Knowledge-Adaptive Context Engineering for Mathematical Reasoning](https://arxiv.org/abs/2606.00532)

**<font color=#1a73e8>作者：</font>** Jayant Parashar, Suchendra M. Bhandarkar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Context engineering can improve large language models without updating their weights, but mathematical reasoning exposes a key limitation: feedback accumulated in one growing prompt causes context bloat and limits the amount of learned guidance that can be used. Existing methods often conflate storage, what is learned across runs, with usage, what is included for a particular problem, and therefore inherit this prompt-size ceiling. We introduce Knowledge-Adaptive Context Engineering (KACE), which separates storage from usage through difficulty- and domain-based organization. Offline, a self-reflective learning loop distills training traces into an epistemic tree: a knowledge base of typed cards stratified by problem difficulty and epistemic domain. Each card is assigned to the difficulty-domain node corresponding to the failure from which it originated. At evaluation time, tiered self-consistency with per-tier agreement gates dynamically classifies each problem as easy, medium, or hard. Easy problems exit without retrieved cards, while harder problems retrieve only the matching branch of the tree. This tiered scheme matches or exceeds Best-of-N while using comparable compute, and it classifies problem difficulty with 78 percent pairwise concordance. The main empirical contribution is the construction and use of a difficulty- and domain-stratified knowledge base enabled by tiered self-consistency. On AIME 2025, KACE achieves 62.2 percent accuracy, a 10.4-point absolute gain over fixed Best-of-5 self-consistency at a comparable solver-call budget and a 5.6-point gain over the strongest learned-context baseline, Tiered + GEPA. We also observe consistent gains on MATH-HARD and the verifiable subset of OlymMATH.

---


### 148. [Rethinking Bregman Divergences in Kronecker-Factored Optimizers](https://arxiv.org/abs/2606.00542)

**<font color=#1a73e8>作者：</font>** Bing Liu, Wenjie Zhou, Chengcheng Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Shampoo-style optimizers approximate gradient covariance matrices using Kronecker-factored structures. Recent work~\cite{lin2026understanding} showed that such approximations can be viewed as projections under Bregman matrix divergences, leading to different Kronecker-factored preconditioners. However, it remains unclear what role the choice of divergence plays when the covariance is not exactly Kronecker-factored. We study this question through the spectrum of the covariance matrix. We show that Frobenius, von Neumann, and LogDet divergences distribute the unavoidable Kronecker approximation error differently across the covariance spectrum. We further show that their Kronecker factors are governed by divergence-weighted residuals rather than the raw approximation error, explaining how these spectral preferences are realized in the resulting preconditioners. Empirically, we observe that the top covariance eigenspace is substantially better aligned with the Hessian matrix, while the tail spectrum is much noisier and unreliable. Motivated by these findings, we propose a subspace-aware Kronecker optimizer that applies eigenvalue-based preconditioning in the top subspace and uses an adaptive isotropic acceleration constant in the bottom subspace.

---


### 149. [Learning to Retrieve: Dual-Level Long-Term Memory for Text-to-SQL Agents](https://arxiv.org/abs/2606.00547)

**<font color=#1a73e8>作者：</font>** Yibo Wang, Nikki Lijing Kuang, Philip S. Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Interactive text-to-SQL agents solve database tasks through multi-turn interactions involving schema exploration, query execution, feedback interpretation, and decision revision. Long-term memory helps agents reuse past experiences, but existing retrieval methods remain limited. Static methods rely on fixed similarity heuristics that do not optimize downstream utility, while dynamic methods often learn from sparse final outcomes and retrieve memories at a single decision horizon. This is insufficient when memory usefulness changes across interaction stages, since memories useful for initial planning may differ from those needed for local, state-conditioned execution. We propose MERIT, a dynamic multi-horizon memory retrieval framework. MERIT maintains episode-level memory for global strategic guidance and turn-level memory for local decision support. Both levels use learned retrieval policies optimized with reinforcement learning. To train turn-level retrieval despite limited intermediate supervision, MERIT uses a lightweight Process Reward Model to provide dense proxy rewards for local memory selection. Experiments on BIRD-Interact show that MERIT outperforms no-memory, static-retrieval, and dynamic-retrieval baselines in success rate while reducing average interaction turns. Transfer results on Spider2-Snow further show positive cross-benchmark transfer without benchmark-specific tuning. These results suggest that multi-horizon retrieval improves experience reuse in interactive text-to-SQL agents.

---


### 150. [CAFOSat: A Strongly Annotated Dataset for Infrastructure-Aware CAFO Mapping Using High-Resolution Imagery](https://arxiv.org/abs/2606.00548)

**<font color=#1a73e8>作者：</font>** Oishee Bintey Hoque, Nibir Chandra Mandal, Mandy L Wilson 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Concentrated Animal Feeding Operations (CAFOs) play an important role in agricultural production but are also associated with environmental, public health, and disease surveillance concerns. Large-scale mapping of CAFOs from remote sensing imagery remains challenging due to heterogeneous infrastructure layouts, noisy location records, inconsistent annotations, and incomplete inventories. We introduce CAFOSat, a strongly annotated, infrastructure-aware dataset for CAFO mapping across the United States. CAFOSat integrates high-resolution National Agriculture Imagery Program (NAIP) imagery with multi-source CAFO inventories collected across multiple states and transforms weak geolocation records into refined annotations through a human-in-the-loop pipeline combining AI-assisted annotation, GradCAM-based localization, and geometric clustering. To improve dataset quality, we curate challenging negative samples using land-cover-guided sampling with spatial exclusion constraints and provide infrastructure-level annotations, including barns, manure ponds, and grazing-related features, through manual verification. The resulting dataset contains more than 45,000 image patches spanning 20 states and four major CAFO categories. We benchmark a diverse set of convolutional, transformer-based, and vision-language models, demonstrating the value of refined annotations and curated negative samples for CAFO classification and generalization. In addition, we introduce a synthetic augmentation pipeline that generates infrastructure-aware variations to increase training diversity and improve robustness under distribution shifts. CAFOSat provides a large-scale benchmark for advancing infrastructure-aware agricultural monitoring and CAFO mapping from high-resolution remote sensing imagery.

---


> [!TIP]
> 当前位于：**101-150**（第 3/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-651](./part-14.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
