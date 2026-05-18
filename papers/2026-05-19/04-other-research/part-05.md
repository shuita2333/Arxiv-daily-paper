# 📦 其他研究 | 2026年05月19日

> 本类共 **234** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-234**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-234**

---

### 201. [MIND: Decoupling Model-Induced Label Noise via Latent Manifold Disentanglement](https://arxiv.org/abs/2605.16081)

**<font color=#1a73e8>作者：</font>** Dayong Ren  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The paradigm of learning from automatic annotations driven by pre-trained experts and Foundation Models dominates data-hungry applications. However, it introduces a critical challenge: model-induced label noise. Unlike stochastic noise in classical robust learning, this noise stems from annotator inductive biases, manifesting as systematic errors tightly coupled with local feature manifolds. Existing methods relying on global transition matrices underfit these structural patterns, while learning instance-specific matrices remains mathematically intractable. We propose Model-Induced Noise Decoupling (MIND), a theoretically grounded framework addressing this dilemma. We demonstrate that the high-dimensional noise manifold can be decoupled into tractable, subspace-dependent components via Latent Manifold Disentanglement. Specifically, our Latent Decoupling Estimator (LDE) dynamically projects samples into latent structural clusters with consistent error modes, facilitating noise identifiability without ground-truth anchor points. To rigorously evaluate robustness, we adopt a hierarchical protocol: moving from controlled noise on CIFAR-100 to a structural stress test on large-scale real-world 3D datasets (S3DIS, ScanNet), where error patterns explicitly couple with geometric manifolds. Empirically, MIND significantly outperforms state-of-the-art methods on these complex benchmarks and effectively corrects zero-shot hallucinations from Vision-Language Models (e.g., OpenSeg), highlighting its potential as a robust distillation framework for Foundation Models.

---


### 202. [Multi-level Self-supervised Pretraining on Compositional Hierarchical Graph for Molecular Property Prediction](https://arxiv.org/abs/2605.16088)

**<font color=#1a73e8>作者：</font>** Xiayu Liu, Zhengyi Lu, Hou-biao Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-supervised pretraining on molecular graphs has emerged as a promising approach for molecular property prediction, yet most existing methods operate at a single structural granularity and treat bond information as auxiliary edge attributes rather than as an independent semantic layer. In this work, we propose MolCHG, a multi-level self-supervised pretraining framework built upon a novel Compositional Hierarchical Graph that organizes molecular structure into four types of nodes across three semantic levels. By introducing a bond graph that operates in parallel with the atom graph, our architecture elevates bond-level information to independently evolving node representations, enabling fragment nodes to aggregate atom-level and bond-level semantics on an equal footing. We design three level-specific pretraining objectives: an atom-bond cross-view contrastive task that aligns the atom-view and bond-view representations within each fragment, a fragment-level functional group prediction task to inject domain-relevant chemical knowledge, and graph-level structure prediction tasks to encode global molecular topology. Experiments on nine MoleculeNet benchmarks demonstrate that MolCHG achieves the best performance on seven datasets across both classification and regression tasks, remaining competitive with the strongest baselines on the rest. Ablation studies further confirm that the multi-level supervision signals are complementary and that each component contributes to the overall performance.

---


### 203. [Centralized vs Decentralized Federated Learning: A trade-off performance analysis](https://arxiv.org/abs/2605.16089)

**<font color=#1a73e8>作者：</font>** Chaimaa Medjadji, Guilain Leduc, Sylvain Kubler 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) has emerged as a promising paradigm for collaborative model training across distributed edge devices while preserving data privacy especially with the huge increase amount of data due to the adoption of technologies which contributes to the growing number of IoT devices. Storing this amount of data centrally is challenging due to issues like limited communication, privacy, and regulations. FL can be Centralized (CFL), Decentralized (DFL), and Semi-decentralized (SDFL). Choosing the right FL architecture depends on the application's needs. However, very few research studies have experimentally compared these three types of architectures to not only understand the respective strengths and limitations, but also trade-offs between different performance indicators. This paper overcome this lack of analysis, conducting experimental analyses using the Fedstellar simulator, MNIST dataset, and MLP classifier.

---


### 204. [Multi-Agent Cooperative Transportation: Optimal and Efficient Task Allocation and Path Finding](https://arxiv.org/abs/2605.16097)

**<font color=#1a73e8>作者：</font>** Ning Zhou, Nikolai W.F. Bode, Edmund R. Hunt  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-robot systems are integral to modern logistics, but their capabilities are often limited to tasks executable by individual agents. This paper addresses a critical gap in existing frameworks like Multi-Agent Path Finding (MAPF) and Task Allocation and Path Finding (TAPF), which lack true cooperation for transporting large items that require multiple agents. To this end, we formalise the Cooperative Transportation Task Allocation and Path Finding (CT-TAPF) problem, which integrates team formation, task assignment, and collision-free pathfinding. We present an optimal solver, Cooperative Transportation Task Conflict-Based Search (CT-TCBS), which features a novel Incremental Expansion strategy to tackle the combinatorial explosion inherent in team formation. Recognising the computational cost of optimality, we also develop a family of sub-optimal solvers that employ a global, task-centric perspective, selecting the next task to assign based on a global difficulty metric (Best Task or Worst Task). Our comprehensive empirical evaluation demonstrates three key findings: (1) the incremental expansion strategy significantly outperforms the naive combinatorial approach by successfully pruning the dominant task-allocation search space; (2) we identify a task-conflict expansion dilemma, where sophisticated conflict resolvers effective for large-agent pathfinding subproblems can be detrimental in the integrated CT-TAPF setting; and (3) our proposed sub-optimal solvers establish a new, more efficient frontier on the solution quality-runtime spectrum compared to "nn-" agent-centric baselines. This work provides a foundational framework and a set of effective algorithms for a new, practical class of cooperative multi-agent problems.

---


### 205. [PCDM: A Diffusion-Based Data Poisoning Attack Against Federated Learning Systems](https://arxiv.org/abs/2605.16098)

**<font color=#1a73e8>作者：</font>** Wei Sun, Yijun Chen, Bo Gao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) is vulnerable to data poisoning attacks due to its distributed nature. Although recent GAN-based data poisoning methods have indicated the potential of using generative AI to generate seemingly legitimate poisoned data, the inherent consistency of GAN outputs can still reveal a sign of data poisoning. In this paper, we propose a diffusion-based data poisoning framework against FL systems, which leverages a Poisoning-Oriented Conditional Diffusion Model (PCDM) to enable fine-grained control over the local generation of poisoned data while ensuring both attack effectiveness and stealthiness. Our PCDM incorporates an adjustable poisoning vector within the global context to precisely control the generation of poisoned data, with theoretical guarantees on attack performance. Furthermore, it employs a novel jumping diffusion strategy for lightweight and efficient poisoned data generation. We conduct the most systematic and broad experimental evaluation for FL poisoning attacks against various defenses, including advanced Byzantine robust aggregation mechanisms, on four open datasets: MNIST, Fashion-MNIST, CIFAR-10, CIFAR-100, and a real-world wireless-specific dataset VRAI. Our results demonstrate that PCDM is less likely to exhibit statistical anomalies compared with the state-of-the-art methods while more effectively degrading global FL performance, which poses a significant risk to data security in FL.

---


### 206. [Federated Imputation under Heterogeneous Feature Spaces](https://arxiv.org/abs/2605.16099)

**<font color=#1a73e8>作者：</font>** Imane Hocine, Chaimaa Medjadji, Sylvain Kubler 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) enables collaborative training across decentralized clients, but most methods assume aligned feature schemas, an assumption that rarely holds in tabular settings where clients observe only partially overlapping feature subsets. In these heterogeneous feature spaces, parameter-averaging methods (e.g., FedAvg) transfer little information across weakly overlapping or disjoint feature groups, limiting their effectiveness for federated imputation. To overcome this, we propose \textbf{FedHF-Impute}, a federated imputation framework that separates structural feature unavailability from conventional missingness and uses a shared global feature graph to propagate information across statistically related features through message passing. This enables indirect cross-client knowledge transfer, even when features are never jointly observed locally, while preserving standard federated communication. Under simulated partial schema overlap on the SECOM and AirQuality datasets, FedHF-Impute improves imputation accuracy (RMSE) over FL baselines by 26.9\%, and 8.4\% respectively, while achieving comparable performance on PhysioNET, with only a 0.3\% difference relative to the best baseline.

---


### 207. [Sign-Separated Finite-Time Error Analysis of Q-Learning](https://arxiv.org/abs/2605.16103)

**<font color=#1a73e8>作者：</font>** Donghwan Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper develops a sign-separated finite-time error analysis for constant step-size Q-learning. Starting from the switching-system representation, the error is decomposed into its componentwise negative and positive parts. The negative part is dominated by a lower comparison linear time-invariant (LTI) system associated with a fixed optimal policy, whereas the positive part is controlled by a linear switching system. The resulting bounds show that the negative-side LTI certificate is no slower than the positive-side switching certificate and may produce a faster exponential envelope. The analysis identifies a max-induced asymmetry in Q-learning error dynamics. This asymmetry is connected to overestimation: positive action-wise errors can be selected and propagated by the Bellman maximum, whereas negative errors admit an optimal-policy lower comparison. Finite-time bounds are provided for both deterministic and stochastic constant-step-size recursions.

---


### 208. [Multi-Level Contextual Token Relation Modeling for Machine-Generated Text Detection](https://arxiv.org/abs/2605.16107)

**<font color=#1a73e8>作者：</font>** Chenwang Wu, Yiuming Cheung, Bo Han 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Machine-generated texts (MGTs) pose risks such as disinformation and phishing, underscoring the need for reliable detection. Metric-based methods, which extract statistically distinguishable features of MGTs, are often more practical than complex model-based methods that are prone to overfitting. Given their diverse designs, we first place representative metric-based methods within a unified framework, enabling a clear assessment of their advantages and limitations. Our analysis identifies a core challenge across these methods: the token-level detection score is easily biased by the inherent randomness of the MGTs generation process. Then, we theoretically derive the multi-hop transitions of the token-level detection score and explore their local and global relations. Based on these findings, we propose a multi-level contextual token relation modeling framework for MGT detection. Specifically, for local relations, we model them through a lightweight Markov-informed calibration module that refines token-level evidence before aggregation. For global relations, we introduce a rule-support reasoning module that uses explicit logical rules derived from contextual score statistics. Finally, we combine the local calibrated score and the global rule-support reasoning signal in a joint multi-level inference framework. Extensive experiments show broad and substantial improvements across various real-world scenarios, including cross-LLM and cross-domain settings, with low computational overhead.

---


### 209. [Attention Dispersion in Dynamic Graph Transformers: Diagnosis and a Transferable Fix](https://arxiv.org/abs/2605.16112)

**<font color=#1a73e8>作者：</font>** Jinhao Zhang, Kangfei Zhao, Qiuhao Zeng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer-based architectures have become the dominant paradigm for Continuous-Time Dynamic Graph (CTDG) learning, yet their performance remains limited on temporally shifted datasets. In this work, we identify attention dispersion as a shared failure mode of dynamic graph Transformers under temporal distribution shift. Through controlled ablation contrasting structurally and temporally distinguished historical neighbors against random ones, we show that prediction depends on a class of critical nodes that carry consistently more predictive signal than arbitrary neighbors. However, existing Transformers fail to focus on these nodes even when they are present in the input, as temporal shift weakens attention contrast and produces overly dispersed attention distributions. This diagnosis suggests a simple and transferable fix: replace standard attention with differential attention, which suppresses common-mode attention and amplifies distinctive token-level signals. When added to three representative CTDG Transformer baselines, differential attention consistently improves performance, with gains concentrated on high-shift datasets. Attention-level measurements further confirm the mechanism, showing reduced attention entropy and increased attention mass on critical nodes. Building on these findings, we introduce DiffDyG, a reference implementation combining differential attention with standard input encodings. Across 9 benchmarks and three negative sampling protocols, DiffDyG achieves SOTA performance, with especially large gains on the most shifted datasets.

---


### 210. [ShopGym: An Integrated Framework for Realistic Simulation and Scalable Benchmarking of E-Commerce Web Agents](https://arxiv.org/abs/2605.16116)

**<font color=#1a73e8>作者：</font>** Chinmay Savadikar, Mingyu Zhao, Yuanzheng Zhu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Developing and evaluating e-commerce web agents requires environments that preserve meaningful task structure while enabling controllable, reproducible, and scalable scientific comparison. Existing methodologies force a tradeoff: live storefronts provide realism but are non-stationary, difficult to inspect, and irreproducible, while hand-built sandbox benchmarks provide control but cover only a narrow range of layouts, catalogs, policies, and interaction patterns. We argue that the core bottleneck is methodological: the field lacks a scalable way to construct evaluation settings that are simultaneously realistic, diverse, controllable, inspectable, and reproducible. We introduce ShopGym, an integrated framework for realistic simulation and scalable benchmarking of e-commerce web agents. ShopGym is a framework for constructing e-commerce simulation environments and grounded benchmark tasks. Its simulation layer, ShopArena, converts live seed storefronts into self-contained sandbox shops through anonymized shop specifications and a staged, validated generation process. On top of these simulated storefronts, ShopGuru synthesizes benchmark tasks across seven skill categories, grounding each task in the shop's catalog, navigation structure, policies, and interaction affordances. Together, ShopArena and ShopGuru produce self-contained, resettable, inspectable, and stable evaluation artifacts that preserve structural properties and agent-evaluation signals relevant to shopping tasks. We validate the framework through graph-based structural analysis and agent-based behavioral evaluation with 224 generated tasks across six sandbox shops: three constructed with synthetic data and three with real data. Our results show that the synthetic shops preserve key structural properties of live storefronts, with agent performance on synthetic shops positively correlated with performance on live storefronts.

---


### 211. [Multi-Fidelity Flow Matching: Cascaded Refinement of PDE Solutions](https://arxiv.org/abs/2605.16118)

**<font color=#1a73e8>作者：</font>** Sipeng Chen, Junliang Liu, Hewei Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The source distribution in conditional flow matching is a design parameter that can be calibrated to data, not a default isotropic prior. We exploit this in Multi-Fidelity Flow Matching (MFFM), a cascade refinement framework for parametric PDE solutions: the source is calibrated to the empirical low-to-high-fidelity residual scale with local Gaussian-blur correlation, and the velocity network is conditioned on the low-fidelity solution. Conditioning makes the residual refinement problem substantially easier than unconditional field generation, while residual-calibrated source noise improves the flow-matching training geometry. A multi-resolution cascade applies the same construction independently between adjacent fidelities. After level-wise flow-matching pretraining, we fine-tune the composed cascade end-to-end with a deterministic one-step rollout, which makes one velocity evaluation per cascade level the optimized operating point at inference. The result is a learned analog of multigrid refinement that reaches the finest grid in $L$ deterministic network evaluations per query. We validate MFFM on eight benchmarks: two super-resolution problems and six spatiotemporal forecasting tasks from PDEBench, The Well, and the FNO Navier--Stokes dataset.

---


### 212. [GenShield: Unified Detection and Artifact Correction for AI-Generated Images](https://arxiv.org/abs/2605.16122)

**<font color=#1a73e8>作者：</font>** Zhipei Xu, Xuanyu Zhang, Youmin Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based image synthesis has made AI-generated images (AIGI) increasingly photorealistic, raising urgent concerns about authenticity in applications such as misinformation detection, digital forensics, and content moderation. Despite the substantial advances in AIGI detection, how to correct detected AI-generated images with visible artifacts and restore realistic appearance remains largely underexplored. Moreover, few existing work has established the connection between AIGI detection and artifact correction. To fill this gap, we propose GenShield, a unified autoregressive framework that jointly performs explainable AIGI detection and controllable artifact correction in a closed loop from diagnosis to restoration, revealing a mutually reinforcing relationship between these two tasks. We further introduce a Visual Chain-of-Thought based curriculum learning strategy that enables self-explained, multi-step ``diagnose-then-repair'' correction with an explicit stopping criterion. A high-quality dataset with large-scale ``artifact-restored'' pairs is also constructed alongside a unified evaluation pipeline. Extensive experiments on our correction benchmark and mainstream AIGI detection benchmarks demonstrate state-of-the-art performance and strong generalization of our method. The code is available at this https URL.

---


### 213. [Entropy Across the Bridge: Conditional-Marginal Discretization for Flow and Schrödinger Samplers](https://arxiv.org/abs/2605.16126)

**<font color=#1a73e8>作者：</font>** Bruno Trentini, Dejan Stancevic, Michael M. Bronstein 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> For a fixed flow-based generative model under a small inference budget, sample quality can depend strongly on where the sampler spends its few function evaluations. Flow matching and Schrödinger bridges define probability paths, yet their inference grids are usually heuristic or inherited from one-endpoint diffusion. We derive a conditional-marginal entropy-rate objective for bridge-aware discretization, separating endpoint-conditioned bridge geometry from marginal flow evolution, and use it to build a training-free entropic inference-time scheduler from first principles. For Gaussian Brownian bridges this rate is closed-form and U-shaped, motivating boundary-heavy nonuniform grids. On trained two-dimensional bridge/flow models, the estimated profile recovers the predicted shape and improves 10-step ODE-Heun MMD over linear by 18.1%, with a paired 22.7% SDE-Heun improvement in the same low-NFE sweep. On EDM/CIFAR-10, the entropic time-discretization gives the best tested five-step FID (186.3 \pm 4.0 versus 200.5 \pm 2.9 for linear and 238.0 \pm 5.3 for cosine). On AlphaFlow protein generation, entropic conditional-marginal (cond-marg) scheduling shows advantage in low-NFE regimes on both CAMEO22 and ATLAS benchmarks. These results support entropy-rate scheduling as a practical low-budget allocation signal for high-dimensional bridge and flow samplers.

---


### 214. [WeatherOcc3D: VLM-Assisted Adverse Weather Aware 3D Semantic Occupancy Prediction](https://arxiv.org/abs/2605.16127)

**<font color=#1a73e8>作者：</font>** A. Enes Doruk, Abdelaziz Hussein, Hasan F. Ates  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While multi-modal 3D semantic occupancy prediction typically enhances robustness by fusing camera and LiDAR inputs, its effectiveness is fundamentally constrained by environmental variability. Specifically, camera sensors suffer from severe low-light degradation, while LiDAR sensors encounter significant backscatter noise during heavy precipitation. These adverse conditions create a modality trust problem, as static fusion strategies fail to adaptively re-weight inputs when a specific sensor becomes unreliable. To address this, we propose a VLM-assisted framework leveraging the pre-trained CLIP latent space to guide multi-sensor integration via linguistic environmental cues. We utilize a parameter-efficient adapter to align weather-specific text embeddings with sensor features, coupled with a gating strategy that decomposes environmental uncertainty into two factors: visibility and illumination. This enables the model to dynamically modulate the fusion ratio - prioritizing semantic camera features in clear daylight and shifting to geometric LiDAR priors during rainy nights. Evaluations on the nuScenes dataset demonstrate the versatility of our approach, as implementing our proposed framework on the OccMamba and M-CONet architectures achieves mIoU scores of 26.3 and 21.1, respectively, significantly outperforming their traditional baselines.

---


### 215. [Navigating Potholes with Geometry-Aware Sharpness Minimization](https://arxiv.org/abs/2605.16134)

**<font color=#1a73e8>作者：</font>** Simon Dufort-Labbé, Mehrab Hamidi, Razvan Pascanu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sharpness-aware minimization (SAM) encourages flat minima by perturbing parameters along directions of high loss curvature, but treats all parameter directions uniformly, ignoring the underlying loss geometry. We introduce LLQR+SAM, which combines SAM with a learned preconditioner obtained from the recently proposed LLQR framework, a second-order method that recasts steepest descent as a layerwise linear-quadratic regulator problem. The preconditioner is updated sparsely and maintained as a slow exponential moving average, so it captures a smoothed, low-resolution picture of the loss landscape geometry. The SAM perturbation then operates on top of this learned geometry, probing curvature at a faster timescale. We show that this two-timescale structure is not merely a computational convenience: theoretically, the preconditioner amplifies the SAM escape signal in directions that are flat under the average geometry but locally sharp (potholes). Wide, flat basins, by contrast, remain stable. Empirically, LLQR+SAM gives consistent gains over both SAM and LLQR alone across standard vision and sequence modeling benchmarks, supporting the view that slow learned geometry and fast sharpness correction are genuinely complementary.

---


### 216. [Surrogate Neural Architecture Codesign Package (SNAC-Pack)](https://arxiv.org/abs/2605.16138)

**<font color=#1a73e8>作者：</font>** Jason Weitz, Dmitri Demler, Benjamin Hawks 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural architecture search (NAS) is a powerful approach for automating model design, but existing methods often optimize for accuracy alone or rely on proxy metrics such as bit operations (BOPs) that correlate poorly with hardware cost. This gap is particularly large for FPGA deployment, where cost is dominated by a multi-dimensional budget of lookup tables, DSPs, flip-flops, BRAM, and latency. We present the Surrogate Neural Architecture Codesign Package (SNAC-Pack), an open-source AutoML framework for hardware-aware neural architecture codesign and end-to-end FPGA deployment. SNAC-Pack runs a multi-objective global search with Optuna and NSGA-II, loading trials to a shared SQLite store that enables parallel workers across compute nodes. A hardware surrogate model outputs per-trial resource and latency estimates, avoiding the synthesis cost that would otherwise dominate the search loop. A local search stage then applies quantization-aware training (QAT) together with iterative magnitude pruning in a combined compression loop, after which the final model is synthesized to FPGA firmware via the hls4ml Python library. A YAML configuration and an optional agentic frontend let users run the pipeline on new datasets without modifying the framework. We demonstrate SNAC-Pack on jet classification at the Large Hadron Collider and superconducting qubit readout, discovering compact architectures that match or exceed strong baselines on the task metric while reducing FPGA resource utilization and, in the qubit readout case, reducing the design space exploration process from months of manual fine-tuning to hours of automated search.

---


### 217. [Registers Matter for Pixel-Space Diffusion Transformers](https://arxiv.org/abs/2605.16147)

**<font color=#1a73e8>作者：</font>** Nikita Starodubcev, Ilia Sudakov, Ilya Drobyshevskiy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) are known to exhibit high-norm patch-token outliers that degrade feature map quality, a problem effectively mitigated by \textit{register tokens}. As diffusion models increasingly adopt transformer architectures and move toward pixel-space training, they become closer in form to ViTs, raising the question of whether register tokens are also useful for Diffusion Transformers (DiTs). In this work, we show that DiTs differ from ViTs in a key respect: they do not exhibit patch-token outliers. Interestingly, register tokens significantly improve convergence and generation quality of pixel-space DiTs. By analyzing intermediate representations, we find that register tokens produce cleaner feature maps at high noise levels, which may contribute to their effectiveness in pixel-space generation. We further observe that recent pixel-space DiT architectures implicitly incorporate register-like mechanisms, which may partially account for their strong empirical performance. Motivated by these insights, we investigate a parameter-efficient dual-stream architecture that specializes processing for register tokens and improves pixel-space generation quality with negligible runtime overhead.

---


### 218. [An Algebraic Exposition of the Theory of Dyadic Morality](https://arxiv.org/abs/2605.16153)

**<font color=#1a73e8>作者：</font>** Kush R. Varshney  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper provides an algebraic exposition of the theory of dyadic morality (TDM), a psychological model of moral judgment grounded in a simple two-node template: an intentional agent causing harm to a vulnerable patient. We formalize TDM using structural causal modeling (SCM) notation and identify three psychological operators (typecasting operator, completion operator, and valence-dependent inference mechanism) that extend standard SCM to capture how people compute moral judgments under constraints. We address scalability challenges arising from TDM's dyadic limitation, showing how moral cognition compresses multi-node scenarios through node collapse and sequential processing. Drawing on this algebraic framework, we demonstrate concrete applications to AI policy design: detecting conflicting obligations, structuring helpfulness policies to preserve user agency, and designing post-failure communication as causal interventions. Finally, we recommend scoped, contextual measurement of mind perception over universal averaging to operationalize the theory empirically. This algebraic formalization enables neurosymbolic AI systems to compute morality in a way that is both mathematically rigorous and faithful to human moral cognition.

---


### 219. [Entropic Auto-Encoding via Implicit Free-Energy Minimization](https://arxiv.org/abs/2605.16164)

**<font color=#1a73e8>作者：</font>** Hazhir Aliahmadi, Irina Babayan, Greg van Anders  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite their ubiquity, variational autoencoders (VAEs) inherently suffer from posterior collapse, a failure mode in which latent variables are effectively ignored. This failure arises because explicit prior imposition drives optimization toward loss landscape regions corresponding to uninformative latent representations. Here, we introduce Entropic Autoencoders (EAEs), a framework in which reconstruction loss is the only explicit objective, and entropy generates the latent variables' prior implicitly through a free energy-minimizing ensemble of encoders. This ensemble biases learning toward high-volume regions of near-optimal solutions, while decoder updates direct the search trajectories toward informative latent representations. We demonstrate that EAEs mitigate posterior collapse by learning non-Gaussian, multimodal latent distributions that yield diverse, data-consistent generations and preserve different forms of underlying structure in the data. As a proof-of-concept, we show that an EAE captures a superposition of the known low-dimensional dynamics of a reaction-diffusion process. Then, we show that an EAE identifies implicit categorical distinctions in MNIST latent representations, and displays a hierarchical understanding of facial structure on the CelebA dataset, from an "all-human" face to individual-dependent features.

---


### 220. [From Backup Restoration to Minimum Viable Factory Recovery: A Systematization of Ransomware Recovery in Manufacturing Systems](https://arxiv.org/abs/2605.16167)

**<font color=#1a73e8>作者：</font>** Chun Yin Chiu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Ransomware recovery in critical manufacturing infrastructure is not only a backup-restoration problem. Production capability depends on coupled information-technology, operational-technology, physical-process, quality, logistics, identity, and supplier systems. After ransomware, a plant may rebuild servers yet remain unable to schedule work, authenticate operators, trust engineering workstations, release product, reconnect OT assets, or coordinate suppliers. This paper reframes manufacturing ransomware recovery as a critical-infrastructure continuity and interdependency problem. We conduct a PRISMA-guided multivocal review of academic literature, standards and government guidance, threat frameworks, public incident material, and verified full-text/source-page evidence anchors. The review identifies nine evidence-backed recovery failure modes: dependency blindness, untrusted restore point and backup over-trust, identity trust collapse, lack of proof-of-recovery, unsafe OT reconnection, segmentation assumption failure, capability mismatch, unmanaged degraded operation, and supplier dependency failure. We then introduce Minimum Viable Factory Recovery (MVF Recovery): the smallest safe, trusted, and operationally meaningful production capability that can be resumed under current dependency, evidence, identity, data, network, OT, and supplier constraints. MVF Recovery is an analytical objective rather than a claim of full recovery, implementation, or safety certification. The paper derives a recovery lifecycle and benchmarking directions as secondary outputs. The contribution is an evidence-calibrated foundation for capability-centric ransomware recovery in critical manufacturing infrastructure.

---


### 221. [BAPR: Bayesian amnesic piecewise-robust reinforcement learning for non-stationary continuous control](https://arxiv.org/abs/2605.16170)

**<font color=#1a73e8>作者：</font>** Yifan Zhang, Liang Zheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world control systems frequently operate under \emph{piecewise stationary} conditions, where dynamics remain stable for extended periods before undergoing abrupt regime changes. Standard robust RL methods face a fundamental dilemma: a globally conservative policy wastes performance during stable periods, while a locally adaptive policy risks catastrophic failure when the regime changes undetected.
We propose \textbf{BAPR} (Bayesian Amnesic Piecewise-Robust SAC), which unifies Bayesian Online Change Detection (BOCD) with robust ensemble RL. The BAPR operator -- a convex combination of mode-conditional Bellman operators weighted by a frozen belief distribution -- is a $\gamma$-contraction. A complementary counterexample, machine-verified in Lean~4, establishes a \emph{sharp boundary}: when beliefs depend on the Q-function, the contraction factor becomes $\gamma + \lambda\Delta$ (where $\Delta$ is the mode reward gap), and contraction fails exactly when $\gamma + \lambda\Delta \geq 1$. We derive a \emph{component-wise} formal error budget for the abstract operator -- every component machine-verified -- bounding post-switch recovery; the budget applies to the abstract mode-mixture operator and inherits to the implemented shared-critic algorithm only through the frozen-parameter design intuition. All results are formally verified with no \texttt{sorry} (1,145 lines across 3 Lean~4 files, 22 machine-verified theorems). BOCD drives an adaptive conservatism mechanism: the policy becomes maximally conservative after detected change-points and smoothly relaxes as confidence grows, with detection delay $O(\log(1/\delta))$. A context-conditioning module trained via RMDM loss provides mode-aware representations from simulator-provided mode IDs at training time and requires no mode labels at deployment.

---


### 222. [Imitation learning for clinical decision support in pediatric ECMO](https://arxiv.org/abs/2605.16175)

**<font color=#1a73e8>作者：</font>** Fateme Golivand, Michael Skinner, Saurabh Mathur 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pediatric critical care is a dynamic, high-stakes process involving constant monitoring and adjustments in life-saving treatments. Modeling these interventions is crucial for effective decision support. To address the challenges of high complexity and data scarcity in pediatric Extracorporeal Membrane Oxygenation (ECMO), we frame clinical decision-making as learning to act from trajectories, i.e., imitation learning that learns action models from observational data, with a key feature that actions are not directly observed. We consider TabPFN, a recent transformer-based approach for tabular data, and traditional baselines including XGBoost and Multi-Layer Perceptrons(MLPs) on real-world pediatric ECMO data to learn the action models. We find that the TabPFN-based approach consistently outperforms these classical baselines, supporting its use as a strong clinician-behavior baseline for pediatric ECMO decision support.

---


### 223. [Improving Cross-Cultural Survey Simulation with Calibrated Value Personas](https://arxiv.org/abs/2605.16193)

**<font color=#1a73e8>作者：</font>** Axel Abels, Elias Fernandez Domingos, Apurva Shah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to simulate human opinions and survey responses, but their ability to reproduce population responses across cultures remains limited. Existing persona-based prompting methods typically rely on sociodemographic or personality traits, which are only indirect proxies for the values that shape human responses. We propose a value-based persona construction method that derives textual descriptors from survey responses capturing core cultural dimensions. By sampling value profiles from target populations and aggregating LLM responses across personas, we obtain population-level predictions grounded in observed value distributions. We further introduce a calibration procedure that improves response diversity while preserving estimated opinions. We show that our approach reduces prediction error across countries, with the largest improvements observed in underrepresented populations. This substantially narrows the performance gap between countries aligned with dominant LLM priors and those that are less represented in training data, while also yielding response distributions that closely match human diversity.

---


### 224. [Position: AI as Part of Self -- Extending the Mind Requires Cognitive Co-Regulation](https://arxiv.org/abs/2605.16197)

**<font color=#1a73e8>作者：</font>** Alina Gutoreva, Fendi Tsim, Trisevgeni Papakonstantinou  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This position paper argues that safety and alignment cannot be achieved by constraining an external system: they must emerge from the co-regulatory design of the human--AI cognitive system as a whole ("AI as Part of Self"). Contemporary AI increasingly participates in attention allocation, reasoning, synthesis, and decision-making, shaping the very cognitive processes through which humans form beliefs, make decisions, and constitute their sense of self. Humans and AI occupy complementary epistemic roles under mutual constraint, forming a symbiotic cognitive unit whose co-regulation -- not the external control of either party alone -- is the proper locus of alignment. We identify the risks of unstructured delegation: deskilling, automation bias, transfer of epistemic authority, and oracle-style centralization of knowledge. Drawing on System~0 cognition theory, we further show that AI operates prior to conscious deliberation, shaping the pre-attentive infrastructures through which agency and trust are negotiated -- a level that conventional oversight cannot reach. We conclude with design principles for cognitive co-regulation addressed to ML engineers and governance bodies. The goal of this work is to guide human cognition toward resilience and epistemic agency at the foundation of human selfhood.

---


### 225. [Hypothesis-driven construction of mesoscopic dynamics](https://arxiv.org/abs/2605.16211)

**<font color=#1a73e8>作者：</font>** Zhuoyuan Li, Aiqing Zhu, Qianxiao Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traditional scientific modeling typically begins with fixed, instance-wise effective equations and then carries out equation-specific analysis and computation, a procedure that becomes exceptionally challenging in complex applications such as multiscale systems. We propose an alternative paradigm by learning mesoscopic dynamics within a mathematically constrained hypothesis class. Building upon a generalized Onsager principle, we introduce a unified framework encompassing both dissipative and conservative mesoscopic dynamics. We establish uniform and a priori theoretical guarantees, including global well-posedness, asymptotic stability, unique factorization identifiability, and discrete energy dissipation, applicable to all spatio-temporal evolution equations within this hypothesis class prior to all learning stages. Data from each problem instance is then used to guide the identification of members within our hypothesis class, giving rise to accurate, robust and interpretable dynamical models. We empirically validate this framework on both data from continuum PDE models as a check, and on data arising from microscopic chain models for which exact meso-scale models are unknown. The proposed approach not only acts as an effective dynamics learner, but also offers vital interpretable diagnostics of the underlying physics.

---


### 226. [Argus: Evidence Assembly for Scalable Deep Research Agents](https://arxiv.org/abs/2605.16217)

**<font color=#1a73e8>作者：</font>** Zhen Zhang, Liangcai Su, Zhuo Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deep research agents have achieved remarkable progress on complex information seeking tasks. Even long ReAct style rollouts explore only a single trajectory, while recent state of the art systems scale inference time compute via parallel search and aggregation. Yet deep research answers are composed of complementary pieces of evidence, which parallel rollouts often duplicate rather than complete, yielding diminishing returns while pushing the aggregation context toward the model's limit. We propose Argus, an agentic system in which a Searcher and a Navigator cooperate to treat deep research as assembling a jigsaw from complementary evidence pieces, rather than brute forcing the whole answer in parallel. The Searcher collects evidence traces for a given sub-query through ReAct-style interaction. The Navigator maintains a shared evidence graph, verifying which pieces are still missing, dispatching Searchers to gather them, and reasoning over the completed graph to produce a source-traced final answer. We train the Navigator with reinforcement learning to verify, dispatch, and synthesize, while independently training the Searcher to remain a standard ReAct agent. The resulting Navigator supports rollouts with a single Searcher or many in parallel without retraining. With both Searcher and Navigator built on a 35B-A3B MoE backbone, Argus gains 5.5 points with a single Searcher and 12.7 points with 8 parallel Searchers, averaged over eight benchmarks. With 64 Searchers it reaches 86.2 on BrowseComp, surpassing every proprietary agent we benchmark, while the Navigator's reasoning context stays under 21.5K tokens.

---


### 227. [The Privacy Price of Tail-Risk Learning: Effective Tail Sample Size in Differentially Private CVaR Optimization](https://arxiv.org/abs/2605.16219)

**<font color=#1a73e8>作者：</font>** El Mustapha Mansouri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Differential privacy changes the effective sample size governing CVaR learning. For tail mass $\tau$, the privacy-relevant sample size is not $n$, but $n\tau$; equivalently, the effective private tail sample size is $\epsilon n\tau$. Private CVaR excess risk decomposes into ordinary tail-risk statistical error and a privacy price. This decomposition is complete for scalar estimation and finite classes: scalar estimation has rate $\Theta(B \min\{1,(n\tau)^{-1/2}+(\epsilon n\tau)^{-1}\})$, and finite classes of size $M$ have rate $\Theta(B \min\{1,\sqrt{\log(2M)/(n\tau)}+\log(2M)/(\epsilon n\tau)\})$. These complete rates hold under pure DP, and their lower bounds extend to approximate DP in the stated small-$\delta$ regimes. For convex Lipschitz learning, modular upper and lower reductions show that the CVaR-specific privacy term necessarily scales as $1/(\epsilon n\tau)$, with dimension dependence inherited from private stochastic convex optimization. Together, these results identify ordinary private learning on $\Theta(n\tau)$ informative tail records as the canonical hard subproblem inside private CVaR learning.

---


### 228. [LymphNode: A Plug-and-Play Access Control Method for Deep Neural Networks](https://arxiv.org/abs/2605.16227)

**<font color=#1a73e8>作者：</font>** Hanyu Pei, Shang Liu, Zeyan Liu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deep Neural Networks (DNNs) are high-value intellectual property (IP), yet deploying them to edge environments exposes them to \textbf{unrestricted oracle access}, rendering them vulnerable to model extraction and inversion attacks. Existing defenses fail to address this practically: passive watermarking only offers post-hoc provenance, while active defenses impose prohibitive latency or require persistent access to sensitive training data. To bridge this gap, we propose \textit{LymphNode}, a novel post-hoc defense framework that acts as an intrinsic ``immune system" within the model. \textit{LymphNode} enforces a strict ``default-deny'' policy: it actively neutralizes model utility for unauthorized queries via \textbf{Generalized Sparse Universal Adversarial Perturbations (GSUAP)} injected into the feature space, effectively blocking gradient estimation and data inference. Utility is selectively restored only for authorized inputs carrying a stealthy feature-domain credential. Our framework is highly practical: it is \textbf{data-efficient}, establishing robust protection with fewer than 100 samples ($<1\%$ of training data), and \textbf{cross-dataset adaptable}, enabling protection using public surrogate datasets. \textit{LymphNode} thus provides a lightweight, immediately deployable defense for high-stakes scenarios where original training data is restricted or unavailable.

---


### 229. [A Unified Generative-AI Framework for Smart Energy Infrastructure: Intelligent Gas Distribution, Utility Billing, Carbon Analytics, and Quantum-Inspired Optimisation](https://arxiv.org/abs/2605.16232)

**<font color=#1a73e8>作者：</font>** Pavan Manjunath, Thomas pruefer  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The accelerating convergence of smart metering, generative artificial intelligence, and quantum-inspired combinatorial optimisation is reshaping how energy utilities manage physical infrastructure, customer engagement, and environmental accountability

---


### 230. [Layer Equivalence Is Not a Property of Layers Alone: How You Test Redundancy Changes What You Find](https://arxiv.org/abs/2605.16234)

**<font color=#1a73e8>作者：</font>** Gabriel Garcia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When researchers ask whether two transformer layers are "equivalent" for compression, they often conflate distinct tests. Replacement asks whether one layer's map can substitute for another's in place; interchange asks whether two layers approximately commute when their positions are swapped. Both are output-grounded swap-KL probes, but they need not agree: on pretrained transformers the protocol gap can change which layers look safe to prune by several-fold under the same evaluator, especially when replacement distances are high.
We measure both protocols across checkpoints and architectures. On a Pythia training trajectory (410M and 1.4B), the replacement-interchange gap grows from initialization to convergence. Under one matched WikiText-2 contract at 8B scale, Qwen3-8B enters a divergent regime: interchange-guided removal is several-fold safer than replacement-guided at the same layer budgets, while Llama-3.1-8B ties the two protocols for pruning cost even though interchange KL is lower, showing metric gaps need not map one-to-one to removal. Before layer removal or merging, score both swap-KLs on the target checkpoint; the diagnostic requires only unlabeled forward passes.

---


### 231. [Dynamics-Level Watermarking of Flow Matching Models with Random Codes](https://arxiv.org/abs/2605.16239)

**<font color=#1a73e8>作者：</font>** Shuchan Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce a dynamics-level approach to watermarking generative models. Rather than embedding signals into model weights or outputs, we embed the watermark directly into the learned continuous dynamics -- the velocity field of a flow matching model. We formulate this as random coding over a continuous channel: a key-dependent perturbation is added during training, and the message is recovered at detection time from black-box queries. The perturbation is designed to leave the generated distribution unchanged. Experiments on MNIST and CIFAR-10 across different architectures confirm reliable message recovery, preserved generation quality, and chance-level decoding accuracy without the secret key.

---


### 232. [Offline Semantic Guidance for Efficient Vision-Language-Action Policy Distillation](https://arxiv.org/abs/2605.16241)

**<font color=#1a73e8>作者：</font>** Jin Shi, Brady Zhang, Yishun Lu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Billion-parameter Vision-Language-Action (VLA) policies have recently shown impressive performance in robotic manipulation, yet their size and inference cost remain major obstacles for real-time closed-loop control. We introduce \textbf{VLA-AD}, a distillation framework that uses a Vision-Language Model as an offline semantic supervisor to transfer large VLA teachers into lightweight student policies. Instead of relying only on low-level action imitation, VLA-AD augments teacher-provided 7-DoF action targets with high-level semantic guidance, including task phase anchors and multi-frame operating-direction descriptions. These auxiliary signals are used only during training: at test time, the student policy runs independently, with neither the VLA teacher nor the VLM required. We evaluate VLA-AD on three LIBERO benchmark suites. Using OpenVLA-7B as the teacher, our method produces a 158M-parameter student, yielding a $44\times$ reduction in model size while matching the teacher with only a $0.27\%$ average relative gap. The resulting policy runs at 12.5 Hz on an RTX 4090, achieving a $3.28\times$ inference speedup over OpenVLA-7B. We further show that the same semantic distillation pipeline generalizes to a different $\pi_{0.5}$-4B teacher, where the student outperforms the teacher on two suites and remains within $0.53\%$ on \texttt{libero\_goal}. Additional analysis indicates that phase-level supervision and multi-frame directional cues make the student less sensitive to noisy teacher actions, such as erroneous high-frequency gripper changes. Overall, VLA-AD demonstrates that offline semantic guidance from VLMs can substantially improve the efficiency, robustness, and deployability of VLA policy distillation.

---


### 233. [A Generative AI Framework for Intelligent Utility Billing CO 2 Analytics and Sustainable Resource Optimisation](https://arxiv.org/abs/2605.16250)

**<font color=#1a73e8>作者：</font>** Pavan Manjunath, Thomas Pruefer  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Distribution utilities are now expected to deliver bills that customers can actually read attach a defensible carbon number to every kWh sold and schedule load against grid stress and emissions constraints We propose an end-to-end framework that unifies four production-grade capabilities under one architectural roof a generative-AI agent that drafts each customers natural-language billing statement from structured numeric inputs under a constrained decoding policy a transformer-based forecaster that supplies the day-ahead consumption estimate with calibrated quantile bands

---


### 234. [IVGT: Implicit Visual Geometry Transformer for Neural Scene Representation](https://arxiv.org/abs/2605.16258)

**<font color=#1a73e8>作者：</font>** Yuqi Wu, Tianyu Hu, Wenzhao Zheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing coherent 3D geometry and appearance from unposed multi-view images is a fundamental yet challenging problem in computer vision. Most existing visual geometry foundation models predict explicit geometry by regressing pixel-aligned pointmaps, often suffering from redundancy and limited geometric continuity. We propose IVGT, an Implicit Visual Geometry Transformer that implicitly models continuous and coherent geometry from pose-free multi-view images. This formulation learns a continuous neural scene representation in a canonical coordinate system and supports continuous spatial queries at any 3D positions, retrieving local features to predict signed distance (SDF) values and colors using lightweight decoders. It allows direct extraction of continuous and coherent surface geometry, enabling rendering of RGB images, depth maps, and surface normal maps from arbitrary viewpoints. We train IVGT via multi-dataset joint optimization with 2D supervision and 3D geometric regularization. IVGT demonstrates generalization across scenes and achieves strong performance on various tasks, including mesh and point cloud reconstruction, novel view synthesis, depth and surface normal estimation, and camera pose estimation.

---


> [!TIP]
> 当前位于：**201-234**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-234**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
