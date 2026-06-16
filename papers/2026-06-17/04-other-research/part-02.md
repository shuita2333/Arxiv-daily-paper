# 📦 其他研究 | 2026年06月17日

> 本类共 **509** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-509](./part-11.md)

---

### 51. [Trust Between AI Agents: Measuring Formation, Breakage, and Recovery, with Implications for Governing Multi-Agent Systems](https://arxiv.org/abs/2606.14923)

**<font color=#1a73e8>作者：</font>** Yujiao Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As language-model agents increasingly work in teams, each agent must decide how much to trust its teammates. Yet we lack a standard way to measure trust between AI agents. We propose a behavioral measure based on costly verification. In a cooperative survival game, checking a teammate's work consumes resources, while trusting a wrong answer can be fatal. Relative to a memoryless version of the same model, reduced verification provides an observable measure of trust. Using this framework, we study trust formation, breakage, and recovery across six frontier model snapshots. When paired with a consistently reliable teammate, four snapshots (Claude Opus 4.6, Claude Sonnet 4.6, GPT-5.1, and Gemini 3.1 Pro) reduce verification by roughly 60-85%, whereas two smaller snapshots show little or no such adjustment. Failures reverse this discount, but models differ in how they respond. Some concentrate renewed scrutiny on the culprit, while others become more cautious toward the entire team. Recovery is slower than formation, and clustered failures sustain suspicion far longer than the same number of failures spread apart. These differences have practical consequences. Models that form trust verify less, decide more quickly, and achieve higher payoffs in our environment. By contrast, persistent over-verification is associated with indecision rather than safety. Our results show that trust dispositions can be measured before deployment and suggest that calibration, rather than maximal suspicion, should be the central concern in the governance of multi-agent AI systems.

---


### 52. [FlexPooling with Simple Auxiliary Classifiers in Deep Networks](https://arxiv.org/abs/2606.14926)

**<font color=#1a73e8>作者：</font>** Muhammad Ali, Omar Alsuwaidi, Salman Khan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In computer vision, the basic pipeline of most convolutional neural networks consists of multiple feature extraction layers, where the input signal is downsampled to a lower resolution in each subsequent layer. This downsampling process is commonly referred to as pooling, which is an essential operation in CNNs. Pooling improves robustness against transformations, reduces the number of trainable parameters, increases the receptive field, and lowers computation time. Since pooling is a lossy process but remains important for extracting high-level information from low-level representations, it is important to preserve the most prominent information from previous activations to improve network discriminability. Standard pooling is usually performed using dense pooling methods, such as max pooling or average pooling, or through strided convolutional kernels. In this paper, we propose a simple yet effective adaptive pooling method, called FlexPooling, which generalizes average pooling by learning a weighted average over activations jointly with the rest of the network. We further show that attaching Simple Auxiliary Classifiers (SAC) to the CNN improves performance and demonstrates the effectiveness of the proposed method compared with standard pooling methods. Experiments on multiple popular image classification datasets show that FlexPooling consistently outperforms baseline networks, achieving approximately 1 to 3 percent improvement in accuracy.

---


### 53. [Policy Regret for Embedding Model Routing: Contextual Bandits with Low-Rank Experts](https://arxiv.org/abs/2606.14929)

**<font color=#1a73e8>作者：</font>** Yan Dai, Negin Golrezaei, Patrick Jaillet  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern recommendation systems increasingly rely on dynamically routing diverse queries to multiple embedding models. Despite its practical significance, this problem remains poorly understood under realistic conditions like adversarial queries, bandit feedback, and limited observability of models. We formalize embedding model routing as an adversarial contextual linear bandit with low-rank experts, where contexts are queries, actions are items, and experts are the embedding models working on low-rank latent representation spaces. We first establish that standard regret notions suffer from structural misspecification or statistical intractability, and we identify a log-quadratic policy class that is expressive enough to capture query-dependent model routing, yet structured enough to allow efficient online learning. Second, we propose a policy gradient algorithm called Hypentropy Policy Gradient (HPG). It provably adapts to the unknown low-rank structure under incomplete information and attains $\tilde{\mathcal O}(s\sqrt{M T})$ linearized policy regret -- where $s, M$, and $T$ are the intrinsic rank of the experts, the number of models, and the number of rounds -- thus avoiding a curse of dimensionality. Finally, we also provide an computationally efficient and parameter-free implementation of HPG.

---


### 54. [Censorship-Resistant Sealed-Bid Auctions on Blockchains](https://arxiv.org/abs/2606.14939)

**<font color=#1a73e8>作者：</font>** Orestis Alpos, Lioba Heimbach, Kartik Nayak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Auctions are now central to blockchain markets, settling NFT sales, token launches, DeFi liquidations, and arbitrage opportunities. Each on-chain bid is a public transaction whose inclusion is decided by a single consensus proposer per block. The proposer can observe pending bids, exclude competitors, and submit bids of their own, breaking the fairness guarantees of classical sealed-bid auctions.
To enable latency-sensitive sealed-bid auctions in blockchain settings, we formalize four properties -- each necessary to prevent a concrete attack -- and design a protocol achieving all four: hiding bid contents, existence, and bidder identity until reveal (Hiding); counting all timely honest bids and rejecting late adversarial bids (Simultaneous Release); preventing silent withdrawal of committed bids (No Free Bid Withdrawal); and charging on-chain fees only to winners (Auction Participation Efficiency).
Our protocol uses a timestamping oracle (instantiated with a committee of 2f_ts+1 timestampers) and a censorship-resistant inclusion predicate (instantiated using a FOCIL-based inclusion list), with only the winning bid settled on-chain. Our construction relies on two zero-knowledge proofs: an eligibility proof that anonymously proves deposit membership to the timestamping committee, and an auction proof that binds a bid to a specific auction for the inclusion list committee. We implement both using Groth16 over BN254 with Poseidon hashing in arkworks/Rust: the auction proof generates in 13 ms and verifies in under 1 ms; eligibility proofs for Merkle trees up to 2^32 bidders generate in 47-159 ms and verify in about 1 ms.
Together, this yields a sealed-bid auction primitive practical for high-value, time-sensitive blockchain settings.

---


### 55. [Semantics-Enhanced Retrieval-Augmented Time Series Forecasting](https://arxiv.org/abs/2606.14941)

**<font color=#1a73e8>作者：</font>** Shiqiao Zhou, Zipeng Wu, Holger Schöner 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Time series forecasting models often benefit from historical patterns. Inspired by Retrieval-Augmented Generation (RAG), recent research explored retrieving relevant historical time series segments to enhance forecasting. However, relying solely on time series similarity is often insufficient for retrieval under non-stationarity. To address this, we propose a multimodal approach: a \textbf{S}emantics-\textbf{E}nhanced \textbf{R}etrieval-\textbf{A}ugmented Time Series \textbf{F}orecasting framework, SERAF. Unlike mainstream approaches that depend only on time series similarity, SERAF conducts dual retrieval over the time series and their self-generated textual descriptions. It retrieves two complementary sets of historical patterns and corresponding futures, which are selectively and jointly used to guide future predictions. Experiments across seven real-world datasets demonstrate the effectiveness of SERAF in bridging numerical and semantic views of time series compared with state-of-the-art baselines.

---


### 56. [Simplifying the Modeling of Arbitrary Conditionals in Natural Language](https://arxiv.org/abs/2606.14943)

**<font color=#1a73e8>作者：</font>** Yinhan Lu, Eric Elmoznino, Léo Gagnon 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Causal Transformers model sequences through an autoregressive factorization of the joint distribution, which enables efficient left-to-right decoding and conditional likelihood computation. However, they cannot tractably sample from or evaluate arbitrary conditionals -- e.g., a block of text conditioned on past and future tokens. Recent work aims to solve this problem through novel architectures, but they often lead to sub-optimal modeling of such conditionals and degraded generations. We propose Arbitrary Conditionals GPT (AC-GPT) which introduces a simple modification to standard causal Transformers to enable evaluating and sampling from arbitrary conditionals -- including past, future, and mixed contexts -- within a single forward pass. Unlike prior approaches, our method preserves the standard left-to-right ordering and next-token prediction objective essential for both strong performance and efficient training on natural language. Crucially, this compatibility allows existing LLMs to be fine-tuned for arbitrary conditioning. Our empirical results indicate that our method outperforms baselines on modeling arbitrary conditionals, without degrading standard left-to-right performance.

---


### 57. [Remember, Don't Re-read: Stateful ReAct Agents for Token-Efficient Autonomous Experimentation](https://arxiv.org/abs/2606.14945)

**<font color=#1a73e8>作者：</font>** Faramarz Jabbarvaziri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The autoresearch pattern enables autonomous experimentation by having a large language model (LLM) iteratively modify code to optimize a target metric. Its stateless design, however, reconstructs experimental context from scratch at every iteration, incurring $O(n)$ token cost per iteration and $O(n^{2})$ total. This work reformulates the pattern as a stateful ReAct agent using LangGraph, where typed persistent state carries experimental history across iterations via a tool-calling interface. Two benchmarks are evaluated: hyperparameter tuning (15 iterations, small per-iteration observations) and code performance optimization (40 iterations, large per-iteration observations containing full source code and benchmark results). On hyperparameter tuning, the stateful agent consumes 90\% fewer tokens (2{,}492 vs.\ 24{,}465). On code optimization, the stateful agent consumes 52\% fewer tokens (627K vs.\ 1{,}275K) while achieving comparable optimization quality on both tasks. The token reduction is structural: the stateless agent re-reads the full history at $O(n)$ cost per iteration, while the stateful agent operates within a fixed-size conversation window at $O(1)$ cost. This paper describes the architecture in sufficient detail for practitioners to implement a stateful autoresearch agent for their own workflows.

---


### 58. [A Comparative Study of Graph Neural Network Layer Selection for Interaction Modelling in Driving Trajectory Prediction](https://arxiv.org/abs/2606.14956)

**<font color=#1a73e8>作者：</font>** George Daoud, Mohamed El-Darieby  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autonomous driving systems rely on precise trajectory prediction to plan safe and efficient movement. Graph Neural Networks (GNNs) have become a promising approach for modelling spatiotemporal interactions among road agents. However, designing GNN architectures for trajectory prediction remains non-standardized, with little guidance on which graph layers effectively capture spatial interactions and temporal dynamics. This paper offers a detailed comparative study of 19 graph layer types, focusing on their spatial and temporal processing capabilities to discover the most effective architectures for trajectory prediction. Within the explored hyperparameter setting, we highlight five standout layer combinations, with ARMA, Chebyshev, and topology-aware layers consistently performing better than others. Beyond performance metrics, our findings yield practical design principles: sum-based aggregation is more effective than mean-based methods, multi-head attention mechanisms enable richer interactions, and assigning different weights to different hop distances significantly improves prediction accuracy. These findings offer useful guidance for designing more interpretable and effective trajectory prediction models.

---


### 59. [MVEB: Massive Video Embedding Benchmark](https://arxiv.org/abs/2606.14958)

**<font color=#1a73e8>作者：</font>** Adnan El Assadi, Roman Solomatin, Isaac Chung 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce the Massive Video Embedding Benchmark (MVEB), a 23-task benchmark for video embeddings spanning classification, zero-shot classification, clustering, pair classification, retrieval, and video-centric question answering. We evaluate 33 models and find that no single model dominates: MLLM-based embeddings lead on classification, clustering, pair classification, and QA; multimodal binding leads on retrieval and zero-shot classification; generative MLLMs without contrastive adaptation collapse on cross-modal tasks. Paired video-only vs. audio+video evaluations show that audio's contribution depends on dataset annotation provenance: audio helps when labels were produced from both modalities and hurts when they were produced from visuals alone, a six-point gap consistent across model families. MVEB is derived from MVEB+, a 184-task pool, and is designed to maintain task diversity while reducing evaluation cost. It integrates into the MTEB ecosystem for unified evaluation across text, image, audio, and video. We release MVEB and all 184 tasks along with code and a leaderboard at this https URL.

---


### 60. [Multi-Modal Attention for Automated Disaster Damage Assessment Using Remote Sensing Imagery and Deep Learning](https://arxiv.org/abs/2606.14963)

**<font color=#1a73e8>作者：</font>** Tewodros Syum Gebre, Jagrati Talreja, Leila Hashemi-Beni  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Timely and accurate disaster damage assessment is crucial for effective emergency response, resource allocation, and recovery. Traditional methods, which often rely on manual inspections or sparse data, are typically slow and error-prone. This paper introduces a novel framework leveraging remote sensing imagery and deep learning to automate building damage classification. Using pre- and post-disaster satellite imagery, our model categorizes buildings into four damage levels: no damage, minor damage, major damage, and destroyed. The core innovation is a multi-modal attention mechanism that fuses bi-temporal features to explicitly detect and assess structural changes. We employ a lightweight ConvNeXT-Tiny backbone to ensure efficient processing without compromising performance. Key contributions include: (1) a cross-attention module for multi-modal data fusion, (2) an optimized preprocessing pipeline for large-scale datasets, and (3) robust data augmentation techniques. Experiments on a large-scale disaster dataset demonstrate an overall classification accuracy of 94.90%. The model effectively discriminates between damage categories and remains resilient to incomplete data. This system significantly improves assessment speed and accuracy, aiding emergency responders in prioritizing interventions. This work advances automated disaster damage detection by integrating multi-temporal imagery with deep learning, offering a scalable solution for real-time response.

---


### 61. [Benchmarking Instance-Dependent Label Noise with Controlled Corruptions](https://arxiv.org/abs/2606.14965)

**<font color=#1a73e8>作者：</font>** Shadman Islam, Agustinus Kristiadi, Mostafa Milani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synthetic instance-dependent label noise (IDN) benchmarks are widely used to evaluate noisy-label learning methods, yet existing approaches typically generate noise through imperfect annotators or classifier raters, leaving the source of ambiguity implicit. We introduce CILN, a benchmark generation framework that creates IDN through controlled input corruptions. A diverse voter pool labels corrupted instances, producing benchmark datasets in which both the source and severity of ambiguity are explicit and controllable. Using CIFAR10, MNIST, and Adult, we construct 90 benchmark settings spanning multiple corruption families and severity levels. Our experiments show that the resulting benchmarks exhibit genuine instance-dependent noise, provide diverse confusion structures, and, on CIFAR-10, can produce label distributions that are closer to human uncertainty than an existing synthetic IDN benchmark. We further demonstrate that corruption-mediated IDN can expose failure modes of popular noisy-label learning methods, including Co-Teaching and DivideMix, that are not observed under comparable levels of rater-fallibility noise. These findings suggest that noise structure, not only noise rate, plays an important role in benchmark difficulty and algorithm behavior. By making ambiguity generation explicit and controllable, CILN provides a complementary benchmarking framework for studying noisy-label learning under diverse sources of instance difficulty.

---


### 62. [FastMix: Fast Data Mixture Optimization via Gradient Descent](https://arxiv.org/abs/2606.14971)

**<font color=#1a73e8>作者：</font>** Haoru Tan, Sitong Wu, Yanfeng Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While large and diverse datasets have driven recent advances in large models, identifying the optimal data mixture for pre-training and post-training remains a significant open problem. We address this challenge with FASTMIX, a novel framework that automates data mixture discovery while training only a single proxy model. Instead of relying on predefined heuristics or resource-intensive simulations, FASTMIX jointly optimizes mixture coefficients and model parameters, substantially improving efficiency and scalability over prior approaches. At the core of FASTMIX is a reformulation of mixture selection as a bilevel optimization problem. Under this reformulation, we show that optimizing mixture ratios is mathematically equivalent to assigning per-source loss weights under uniform source sampling. This embeds the mixture coefficients directly into the differentiable iterative optimization objective, enabling efficient, gradient-based optimization of both mixture and model. To solve the optimization problem, FASTMIX implements an approximate iterative optimization procedure, alternating between (i) updating model parameters on data sampled according to current mixture ratios (inner loop) and (ii) updating mixture ratios based on validation feedback (outer loop). Across pre- and post-training, FASTMIX outperforms baselines while drastically reducing search cost. Code (this https URL)

---


### 63. [ReGenHuman: Re-Generating Human Appearances for Realistic Full-Body Video Anonymization](https://arxiv.org/abs/2606.14972)

**<font color=#1a73e8>作者：</font>** Adam Sun, Eshaan Barkataki, Arnold Milstein 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Anonymizing human-centric video data is an understudied problem. Prior anonymization techniques either blur or redact pixels at the cost of realism and downstream utility, or generate frame-by-frame at the cost of temporal coherence. We introduce ReGenHuman, the first full-body video anonymization pipeline that is simultaneously realistic, temporally consistent, and anonymous by construction. Contrary to past approaches which redact or edit the inputs directly, we propose a regenerate, don't edit paradigm. Our approach composites 2D pose, segmentation, and monocular depth into two complementary conditioning streams - StructAll and StructHuman, which are used to fine-tune a video-to-video diffusion backbone on in-the-wild human videos, synthesizing the human regions entirely from identity-free structural cues. We evaluate our model on privacy, quality, and utility, and show that our ReGenHuman achieves the best tradeoff across all three axes against current baselines. We further show that our anonymized videos remain effective for downstream tasks, including video question answering.

---


### 64. [Continual Backdoor Training in IoT/CPS](https://arxiv.org/abs/2606.14987)

**<font color=#1a73e8>作者：</font>** Oxana Salish, Kuniyilh S  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Internet of Things (IoT) and Cyber-physical systems (CPS) increasingly rely on continual learning (CL) to adapt to evolving environments, device heterogeneity, and concept drift, thereby improving overall utility. While continual adaptation is essential for long-lived IoT deployments where data patterns evolve, it also introduces new security vulnerabilities. In particular, backdoor attacks can exploit incremental updates, replay buffers, and representation reuse to implant persistent malicious behaviors that remain dormant during normal operation but activate upon specific triggers. In this paper, we present a backdoor attack in continual learning used in IoT/CPS systems. To this end, we formalize an IoT/CPS-specific threat model, analyze why continual learning amplifies backdoor persistence in IoT pipelines, and evaluate our technique under varying conditions. Our analysis highlights critical open challenges in securing lifelong learning in IoT/CPS and industrial IoT (IIoT) environments, as well as the need for heightened security controls.

---


### 65. [Rational Sparse Autoencoder](https://arxiv.org/abs/2606.14990)

**<font color=#1a73e8>作者：</font>** Naiyu Yin, Yue Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) are standard tools for mechanistic interpretability, but current SAE families are constrained by fixed encoder nonlinearities such as ReLU, JumpReLU, and TopK. This hard-codes a particular sparsity mechanism into the model and can distort the reconstruction-versus-sparsity trade-off. We introduce the Rational Sparse Autoencoder (RSAE), which replaces the fixed encoder activation with a trainable rational function. Rational activations are flexible enough to uniformly approximate the activation primitives used by existing SAE families on compact domains (for TopK, the thresholded gate obtained after a separating top-k threshold is supplied), while also providing a richer function class for adapting to the observed pre-activation geometry. We realise this idea through a two-stage pipeline: an initialisation procedure that copies the pre-trained baseline SAE weights, plugs in rational coefficients obtained by the relaxed Remez exchange on synthetic data, and calibrates the scale parameters along with the rational coefficients; followed by a fine-tuning step under the standard sparsity-regularised reconstruction objective. Empirically, on residual-stream activations of three open-weight language models and across all three baseline activation families, the RSAE strictly improves on it after the fine-tuning step, both on reconstruction-side metrics and on downstream-behaviour metrics, without sacrificing feature-level interpretability under sparse probing. These gains are consistent across host language models, across baseline activation families, and across the full range of baseline sparsity we tested, while the upgrade itself adds only a handful of scalar parameters per autoencoder and runs in minutes on a single consumer GPU.

---


### 66. [AI Engram: In Search of Memory Traces in Artificial Intelligence](https://arxiv.org/abs/2606.14997)

**<font color=#1a73e8>作者：</font>** Jea Kwon, Dong-Kyum Kim, Jiwon Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Memory formation is fundamental to intelligence, yet whether deep neural networks preserve identifiable memory traces analogous to biological memory units remains an open question. This work introduces a geometric framework to identify such "AI engrams" by formalizing the neuroscientific criteria of specificity, reactivation, sufficiency, and necessity into a constrained inverse problem. We derive a closed-form estimator that isolates individual memory traces from globally entangled parameters, and show that this biologically-derived solution corresponds to a natural gradient update on the parameter manifold. AI engrams enable surgical manipulation of learned knowledge: any subset of memories can be composed or erased through linear arithmetic, without iterative optimization. Experiments ranging from simple MLPs to LLMs demonstrate the causal validity and substantial scalability of AI engrams. Together, these results bridge theories of biological memory and artificial representation learning and offer geometric insight into how deep networks simultaneously support functional specificity within distributed storage.

---


### 67. [Unlocking Latent Dimensions: Exploring Representations of Large-Scale X-ray Scattering Data using Variational Autoencoders](https://arxiv.org/abs/2606.14999)

**<font color=#1a73e8>作者：</font>** Monika Choudhary, Xiaoya Chong, Runbo Jiang 等 28 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific user facilities generate X-ray scattering data faster than traditional workflows can process them. We address this challenge across two settings, offline dataset exploration and live on-the-fly analysis. We train a domain-specific attention-based Convolutional Variational Autoencoder (C-VAE) on 1.5 million X-ray scattering images to learn low-dimensional representations capturing structural variation across diverse experimental conditions. The learned latent space reveals well-organized clusters and smooth trajectories reflecting experimental progression. It further supports controlled synthetic scattering image generation across diverse structural states. When deployed without retraining, the model organizes time-resolved film formation experiments at two synchrotron facilities into interpretable latent structures. Benchmarking against DINOv3 (ViT-7B), a general-purpose vision foundation model, demonstrates that domain-specific training yields more interpretable latent organization for scattering data. Both workflows are integrated within Latent Space Explorer, a component of the MLExchange platform, supporting interactive structural exploration across archived datasets and live experiments.

---


### 68. [NEXUS: Neural Energy Fields for Physically Consistent Contact-Rich 3D Object Dynamics](https://arxiv.org/abs/2606.15015)

**<font color=#1a73e8>作者：</font>** Qizhen Ying, Guangming Wang, Yangchen Pan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physics-grounded video generation requires controllable 3D object dynamics that remain physically consistent under contact, deformation, and external forcing. Existing trajectory-based methods often model isolated physical effects, making it difficult to compose conservative and non-conservative dynamics in contact-rich 3D scenes. We present NEXUS, a neural energy-field framework for contact-rich 3D object dynamics. NEXUS represents each object as a structural graph and constructs dynamic object-object and object-environment contact graphs. Inspired by Hamiltonian Neural Networks, NEXUS formulates motion through scalar energy and dissipation terms rather than directly predicting states or accelerations. Conservative effects, including gravity and elastic deformation, are composed as additive energy terms, while non-conservative effects such as damping and impact-induced energy loss are modeled with learned Rayleigh-style dissipation. Forces are derived by differentiating the energy and dissipation functions and rolled out with a multi-substep semi-implicit integrator. Across controlled trajectory benchmarks, NEXUS improves long-horizon accuracy over representative learned and physics-structured dynamics baselines under varying mechanical properties and physical-effect compositions. We further show that NEXUS trajectories provide effective guidance for contact-rich video generation, improving physical plausibility while maintaining competitive visual quality.

---


### 69. [Are Online Skill and Memory Modules Always Worth Their Tokens? A Budget-Constrained Study of Web Agents](https://arxiv.org/abs/2606.15017)

**<font color=#1a73e8>作者：</font>** Sina Hajimiri, Masih Aminbeidokhti, Jose Dolz 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Online web agents often augment a base actor with memory, workflow, or skill modules. These modules can improve performance, but they also consume test-time tokens, a cost rarely reported alongside the actor's inference cost. We study online augmentation, where this overhead is paid on every task, and re-evaluate its benefits under a fixed total inference budget. We compare AWM, ASI, and ReasoningBank with a token-matched vanilla baseline that uses the same budget for additional actor steps. Across three WebArena domains and three models, Gemini 3 Flash, GPT-5.4-mini, and Qwen 3.6-27B, the vanilla baseline matches or surpasses all three augmentation methods in aggregate success rate while often using fewer total tokens. We observe a similar trend on WorkArena-L1 with Qwen 3.6-27B, indicating that the effect extends to enterprise knowledge-work tasks. Our results suggest that skills and workflow memory can be useful in specific domains, but their apparent gains often vanish against a budget-matched actor. We further show that run-to-run variance materially affects outcomes and should be reported as a core evaluation criterion for online web agents.

---


### 70. [Towards Global AI-Driven Cervical Cancer Screening](https://arxiv.org/abs/2606.15019)

**<font color=#1a73e8>作者：</font>** Thuy Nuong Tran, Ömer Sümer, Evangelia Christodoulou 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The global elimination of cervical cancer is a key public health goal set by the World Health Organization (WHO), with screening programs reducing mortality by up to 80%. However, access to experts and biopsy services is limited in low- to middle-income countries (LMICs). Deep learning (DL)-based algorithms offer promising support for screening, but most existing approaches have been developed and validated on private datasets from single countries. We present the first DL-based approach to cervical cancer screening validated on data from multiple countries. Technically, we phrase the problem of detecting and classifying lesions in colposcopy images as a multi-task learning problem, in which we simultaneously perform image-level classification and lesion segmentation. Our model was trained on a private data set of acid stain colposcopy images with manually generated lesion segmentation masks and corresponding histopathological results, employing extensive data augmentation to address image variability. In an in-distribution validation with pathology results serving as ground truth, our algorithm outperformed medical experts (Balanced Accuracy: 0.68 vs 0.64) in CIN1- (Cervical intraepithelial neoplasia grade 1 or lower) versus CIN2+ (grade 2 or higher) classification. External validation on four colposcopy data sets from four countries featuring radical differences in prevalence and patient characteristics yielded superior performance of our method compared to baseline methods. Performance variability across countries was high with AUC values ranging from 0.54 - 0.80. Overall, algorithm performance varied with age, transformation zone (cervical area most prone to lesion development), presence of comorbidities and pathognomonic signs, with comorbidities having by far the largest negative effect. Future work should focus on improving model robustness and generalizability.

---


### 71. [OSGuard: A Benchmark for Safety in Computer-Use Agents](https://arxiv.org/abs/2606.15034)

**<font color=#1a73e8>作者：</font>** Mina Mohammadmirzaei, Jeffrey Flanigan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-use agents are increasingly evaluated by whether they complete realistic desktop and web tasks. However, task success alone can miss failures in which an agent reaches the nominal goal through an unsafe shortcut. We introduce OSGuard, a dual-granularity benchmark suite for evaluating safety in computer-use agents under benign, unchanged user instructions. OSGuard contains an action-level benchmark for local guardrail decisions and a risk-augmented execution suite for end-to-end evaluation. The action-level benchmark consists of contextualized proposed actions labeled as allowed, unrelated, or unsafe, each judged relative to the original instruction and current interface state. The execution suite contains manually constructed OSWorld-derived task variants in which the original task remains achievable, but the environment is modified to introduce latent hazards such as destructive overwrites, etc. Each variant is paired with augmented evaluators that retain the original task-success criterion while adding explicit state-based safety invariants, allowing us to distinguish safe completions from unsafe completions that satisfy the nominal task objective. Our experimental results on OSGuard show that current multimodal guardrails can perform well on isolated action judgments, while risk-augmented execution exposes remaining gaps between local oversight and reliable end-to-end safety. This dual-granularity design enables more precise diagnosis of whether models can both recognize unsafe proposed actions and improve full-task safety when deployed as guardrails.

---


### 72. [Transformers Learn the Mestre-Nagao Heuristic](https://arxiv.org/abs/2606.15036)

**<font color=#1a73e8>作者：</font>** Pranav Venkata Konda  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We train a two-layer transformer encoder to classify rational elliptic curves $E/\mathbb{Q}$ of conductor $\leq 10000$ as either rank 0 or rank 1 from the first 128 normalized Frobenius traces. We achieve >99% accuracy on both classes, and accuracy is essentially unchanged on test curves with no isogeny or quadratic-twist relative in the training set. We then apply techniques from mechanistic interpretability such as attention analysis, linear probing, activation patching, logit attribution, and neuron-level circuit analysis to reverse-engineer the algorithm the (centroid in function space) model learned. We find that a sparse circuit of 20 out of 512 layer-1 MLP neurons is sufficient for rank prediction under a linear probe with an AUROC of 0.992 at plateau, implementing a push-pull detector architecture of rank-0 and rank-1 detectors with a one-sided readout. However, we notice that the model has sub-optimal readout problems indicating a mismatch in rank-order between the readout pathway and the discriminative circuit. Critically, the learned input weights of the top discriminating neuron match the Mestre-Nagao sum heuristic weights $\log(p)/(p\cdot \log{B})$ with a Spearman coefficient $r = 0.997$ and Pearson coefficient $r = 0.952$: the model has learnt a result from analytic number theory from the Frobenius trace data alone. We additionally find that all 50 independently trained models concentrate CLS attention on prime positions at 2-50$\times$ the rate of composite positions. The CLS embedding encodes $\log{L(E,1)}$ with $R^2 = 0.962\pm 0.011$ across the 50 models (after controlling for the conductor). Activation patching analysis reveals that attention weights are dissociated from causal information flow. Additionally, the 50 solutions from training are near-identical in function space (with pairwise agreement $>$98.8%) despite large weight space barriers.

---


### 73. [BT-MTD: Bus Traversal-based Moving Target Defense for Smart Grid](https://arxiv.org/abs/2606.15047)

**<font color=#1a73e8>作者：</font>** Jingyi Yan, Ke Sun, Zhenglin Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Moving Target Defense (MTD) is a proactive security strategy designed to enhance cyber-resilience by dynamically altering system parameters, thereby preventing adversaries from acquiring the critical information needed to execute stealth attacks. In this paper, we consider the case in which the operator modifies the admittance of branches to enable MTD, and focus on the problem of effectively protecting the system with fewer number of branch admittance modifications and shorter computational time. Specifically, we identify the ineffectual branches whose admittance modification do not contribute to the improvement of MTD effectiveness via theoretical analysis. Building on these insights, we propose the Bus Traversal-based MTD (BT-MTD), which is a bus-oriented algorithm that traverses over the buses of the network according to analytically derived guidelines. The performance of the BT-MTD is evaluated and compared with four existing strategies on standard IEEE test systems, demonstrating its robustness and superior performance in effectiveness, efficiency, and computational cost. The code of BT-MTD is available at: this https URL.

---


### 74. [Temporal Difference Learning for Diffusion Models](https://arxiv.org/abs/2606.15048)

**<font color=#1a73e8>作者：</font>** Qizhen Ying, Yangchen Pan, Victor Adrian Prisacariu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models are typically trained with objectives that focus on local denoising targets at individual time steps (or adjacent pairs), which do not enforce consistency between predictions along the denoising trajectory. This lack of cross-time consistency can degrade performance, especially for few-step samplers. We introduce a temporal difference (TD) objective that penalizes inconsistency of the model's multi-step progress along the denoising path. By reformulating the diffusion process as a Markov reward process and casting denoising as a policy evaluation problem in reinforcement learning, we derive a unified TD approach that applies to both discrete- and continuous-time diffusion formulations. We further propose a principled sample-based reweighting method that stabilizes training. Empirically, we show that using our TD training can significantly improve sample quality measured by FID, with stronger advantages when the number of sampling steps is small, highlighting its practical utility under low-computation-budget scenarios. We provide ablation studies to justify our design choices, including pairwise loss reweighting, regularization weight, and one-step stride. Overall, our TD approach can be a general drop-in that enforces cross-time consistency and improves generation quality across different diffusion generative models.

---


### 75. [Gaussian Spatial Priors for Anatomy-Aware Object Detection in Surgical Videos](https://arxiv.org/abs/2606.15049)

**<font color=#1a73e8>作者：</font>** Yunfan Li, Artem Shmelev, Himanshu Gupta  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detecting anatomical structures in surgical video is essential for intraoperative safety frameworks such as the Critical View of Myopectineal Orifice (CVMPO) in inguinal hernia repair. While prominent structures like the Cooper's Ligament and Triangle of Doom are reliably detected by standard methods, smaller structures such as the epigastric vessels remain challenging due to their visual ambiguity and intermittent visibility. We observe that the spatial relationship between structures is anatomically constrained, and propose a Gaussian Spatial Prior (GSP) module that encodes this relationship as a compact, parametric bias injected into the self-attention of a DAB-DETR decoder. The prior is computed offline from training annotations as a small set of frozen Gaussian parameters and recomputed at each decoder layer using the iteratively refined reference points. On a dataset of inguinal hernia repair videos with 5-fold cross-validation, GSP improves dependent class detection by $+33.5\%$ ($\text{AP}_{50}$) over DAB-DETR and $+53.9\%$ over YOLOv26, while also improving anchor detection by $+6.0\%$. These gains are statistically significant across all folds ($p=0.012$, paired $t-$test).

---


### 76. [Physics-conforming Latent Twins](https://arxiv.org/abs/2606.15053)

**<font color=#1a73e8>作者：</font>** Matthias Chung, Yutong Bu, Deepanshu Verma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Surrogate models are central to scientific machine learning, where they enable fast prediction, simulation, inference, and control for complex physical systems. For time-dependent problems, however, accurate interpolation of training trajectories is not sufficient: reliable surrogates should also respect the conservation laws, invariants, admissibility conditions, and dissipative structures that give those trajectories physical meaning. We introduce Physics-conforming Latent Twins, a framework for learning latent surrogate solution operators whose dynamics satisfy selected physical principles by design. The method builds on the Latent Twin formulation by jointly learning an encoder, a decoder, and a latent flow map between arbitrary time-indexed states, while constraining the latent dynamics to preserve or dissipate prescribed structural quantities. We develop a constraint-transfer viewpoint that connects physical structure in the original state space with compatible constraints in latent space, and prove structure-preservation bounds showing how latent enforcement improves control of physical defects after decoding. We also derive algebraic conditions for latent flow maps that preserve linear and quadratic invariants or enforce dissipative inequalities. Numerical experiments on representative ODE and PDE benchmarks demonstrate improved constraint satisfaction, structural fidelity, and qualitative long-time behavior while maintaining accurate surrogate prediction.

---


### 77. [Size Doesn't Matter: Cosine-Scored Sparse Autoencoders](https://arxiv.org/abs/2606.15054)

**<font color=#1a73e8>作者：</font>** Silen Naihin, Lev Stambler  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) detect features via inner product, so a feature's activation scales with both its directional alignment and the input's norm. Under BatchTopK, high-norm tokens inflate all pre-activations simultaneously, claiming dictionary slots regardless of content alignment. This matters because sublayer normalization has already discarded the magnitude the score measures, so the encoder detects a quantity the model does not read. We replace the score with a learned blend of cosine similarity and input magnitude, letting the optimizer choose how much norm to use; a per-feature extension lets each feature decide independently. In both regimes, training is free to recover inner product but never does, with no feature ever choosing more than half-magnitude dependence. At matched reconstruction, the cosine encoder learns features that align with human-recognizable concepts far more often than standard, filling dictionary slots that inner product wastes on norm detectors. Loss reweighting that equalizes gradients barely closes the gap, confirming forward-pass score geometry as the lever. The advantage is not universal across tasks or depths, but we believe cosine scoring should be the default for dictionary learning on normalized representations.

---


### 78. [Bridging Geographic Bias in Urban Streetscape Inference via Lifelong Learning with Visual-Semantic Pivoting](https://arxiv.org/abs/2606.15055)

**<font color=#1a73e8>作者：</font>** Xinze Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual perception of urban streetscapes underpins evidence-based decisions in landscape planning, public health, and place-making. Yet models trained on a few well-photographed metropolises systematically misjudge underrepresented districts, propagating geographic bias into downstream policy. We address this gap with HVSP-LL, a lifelong learning framework that couples a stratified visual-semantic pivoting module with an equity-aware rehearsal mechanism. The pivoting module organises landscape concepts along a three-tier ontology (macro structure, meso composition, micro element) and aligns image features to learnable semantic anchors at each tier, providing transferable representations that resist distributional drift. The lifelong adaptation component sequentially absorbs new urban regions while constraining inter-region perception gaps through a worst-region sample-reweighting objective and a structurally-aware exemplar buffer. We evaluate HVSP-LL on a panoramic streetscape benchmark assembled from twelve cities across four continents and seven perceptual dimensions. The framework attains 0.834 Spearman correlation on the held-out city sequence, an absolute 6.1 point improvement over the strongest continual baseline, and shrinks the inter-city perception gap to 0.094 -- a 38% reduction relative to the strongest continual baseline (0.151) and a 57% reduction relative to a representative regularisation baseline (0.218). Ablations confirm that each tier of the pivoting hierarchy contributes monotonically, and the equity-aware rehearsal converts mean backward transfer from -0.038 (without retention) to +0.013, eliminating catastrophic forgetting on the held-out sequence. Our results indicate that hierarchical anchoring is a practical pathway toward geographically equitable streetscape inference at city scale.

---


### 79. [Machine Learning and the Random Walk Puzzle: Forecasting the CAD/USD Exchange Rate with Expanding Window Evaluation and SHAP Interpretability](https://arxiv.org/abs/2606.15058)

**<font color=#1a73e8>作者：</font>** Louis Agyekum, Edmund Fosu Agyemang, Obu-Amoah Ampomah 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study examines whether machine learning (ML) models can outperform the naive random walk benchmark in forecasting the monthly USD/CAD exchange rate. Using daily data from the Bank of Canada spanning January 2017 to May 2026, resampled into 113 monthly observations, five ML models are evaluated: linear regression, random forest, gradient boosting, XGBoost, and AdaBoost. These models are benchmarked against the naive random walk model and exponential smoothing with Holt-Winters seasonality (ETS). All models are evaluated using an expanding-window framework to maintain strict out-of-sample integrity, and forecast-accuracy differences are assessed using the Diebold-Mariano (DM) test. Structural break detection identifies four significant breakpoints in the series, corresponding to the escalation of the US-China trade war in 2018, the COVID-19 economic recovery in 2020, the peak of the Bank of Canada rate-hiking cycle in 2022, and the start of the Bank of Canada rate-cutting cycle in 2024. SHAP, or Shapley Additive Explanations, analysis is applied to interpret the drivers of the best-performing ML model. The results show that the naive random walk model remains a formidable benchmark. Linear regression is the only model that statistically outperforms the naive random walk model, with a DM statistic of 3.0585 and a p value of 0.0071, whereas the ML ensemble models show only marginal differences. Random Forest with an expanding-window framework achieves the lowest MAPE of 1.17 percent among all models except the random walk. SHAP analysis confirms that short-term lags, particularly lag1 and lag2, and recent rolling means dominate predictions, consistent with the near-random-walk behavior of exchange rates.

---


### 80. [A Practical Evaluation Method for Long-Form Simultaneous Speech-to-Speech Translation](https://arxiv.org/abs/2606.15059)

**<font color=#1a73e8>作者：</font>** Yulin Xue, Siqi Ouyang, Lei Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Simultaneous speech-to-speech translation (SimulS2ST) enables real-time cross-lingual communication, but existing evaluation has focused largely on short or pre-segmented speech rather than long-form, continuous input. Prior approaches are difficult to reproduce and make assumptions that do not hold for end-to-end systems. We present a practical evaluation method for long-form SimulS2ST. Given source speech, pre-segmented source transcripts, and reference translations, we run automatic speech recognition (ASR) and forced alignment on the generated target speech to recover token-level timestamps, then apply a sentence-embedding-based aligner to match the target text to its corresponding source sentences. This enables sentence-level computation of latency and quality metrics, including YAAL and xCOMET, which are then aggregated into final system-level scores. Experiments on representative SimulS2ST systems show that the method is effective in practice and reveal that current systems suffer from substantial latency accumulation on long speech.

---


### 81. [Phase-Localized Curation Does Not Help: A Negative Result on Per-Phase Metric Selection for Demonstration Filtering](https://arxiv.org/abs/2606.15064)

**<font color=#1a73e8>作者：</font>** Aarav Bedi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Manipulation demonstrations have temporal phase structure, and a natural hypothesis is that demonstration-curation metrics should be applied within phases rather than globally. The idea is to segment each trajectory into phases, score each phase with the metric that is locally most informative, and then aggregate. This follows directly from prior work showing that a single global metric can be the best detector of a defect and yet the worst curator of the resulting policy. We test the per-phase hypothesis on three contact-rich LIBERO pick-and-place tasks with a controlled early-release structural defect, comparing phase-gated curation against the same metrics applied uniformly and against a strong single global metric. Across all three tasks and five random seeds per condition, phase-gated curation is never the best curation strategy, and it is the worst of the three on two of the three tasks (Task 1: 86.0 vs. 92.0 for global; Task 3: 22.7 vs. 48.0 for uniform). We trace the failure to a concrete mechanism. When the defect signal is concentrated in a single phase, rank-aggregating across phases dilutes that signal with uninformative scores from defect-free phases, selecting a worse demonstration subset than simply applying the defect-informative metric everywhere. We further show that the per-phase metric selection does not transfer across tasks, since no phase shares a winning metric between any two tasks, so the selection cannot be reused and must be re-derived per task from a noisy sweep. These results bound a plausible and previously untested method, and they argue that practitioners should prefer identifying a single defect-informative metric over decomposing curation by phase. We release the full pipeline, all metric implementations, and per-seed results.

---


### 82. [CoCoGEC: Counterfactual Generation for Robust Grammatical Error Correction](https://arxiv.org/abs/2606.15069)

**<font color=#1a73e8>作者：</font>** Qianyu Wang, Xiaoman Wang, Yuanyuan Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Grammatical error correction (GEC) systems are usually trained and evaluated on GEC benchmarks, but their performance often drops sharply once the surrounding context is slightly perturbed or extended. This indicates that the existing GEC models usually fail to understand the error patterns in the varying contexts. In this paper, we thoroughly investigate the counterfactuals for GEC tasks, where the subtle changes to the contexts could lead to the label flipping issue. We propose CoCoGEC, a counterfactual generation framework that creates copies of training instances with error-irrelevant contexts altered. Our framework systematically generates counterfactuals by (1) generating intra- and inter-sentence counterfactuals that maintain the error patterns as well as syntax of the original instances by altering the word-level and sentence-level contexts; (2) revising the generated counterfactuals by selecting the instances with flipped labels and high GEC Mutual Information (MI) coefficient. Extensive experiments show that our method substantially improves the stability of GEC models, outperforming a set of data augmentation baselines. Particularly, it could achieve absolute F0.5 gains of +9.9, +11.3, and +20.8 points on the perturbed BEA-19*,CoNLL-14*, and TEM-8* data this http URL code is released at this https URL

---


### 83. [Texture-Shape Bias Balancing for Robust Synthetic-to-Real Semantic Segmentation in Automotive NIR Imagery](https://arxiv.org/abs/2606.15072)

**<font color=#1a73e8>作者：</font>** Felix Stillger, Ben Hamscher, Lukas Hahn 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic segmentation is a fundamental component of visual perception in modern automotive systems, enabling pixel-level scene understanding. Near-Infrared imaging (NIR) offers stable detection under difficult illumination conditions, but the development of domain-specific semantic segmentation models remains challenging due to the lack of high-quality annotated data from real-world scenarios. Synthetic datasets offer a scalable alternative, but models trained on synthetic images often suffer performance degradation when transferred to real domains. We present the first systematic study on synthetic to real domain adaptation for semantic segmentation in NIR images in the automotive domain. We propose a generative augmentation framework that transforms synthetic images into realistic NIR-style variants via our introduced target style adaptation (TSA). TSA fine-tunes a latent diffusion model via low-rank adaptation on a small curated set of real NIR images and applies it to synthetic training data using structure-preserving multi-signal conditioning. To reduce texture bias and improve segmentation robustness, we further apply a Voronoi-based style diversification strategy (VSD) that modifies the original textures while preserving scene geometry. Experiments with multiple model architectures on NIR data from vehicle interiors and street scenes show that balancing inductive bias during training leads to noticeably more robust semantic segmentation and effectively reduces the domain gap in our real-world scenarios by up to 63.6% on exterior and 28.4% on interior data. The code is available at GitHub.

---


### 84. [AdaMame: A Training Recipe for Adaptive Multilingual Reasoning](https://arxiv.org/abs/2606.15080)

**<font color=#1a73e8>作者：</font>** Dayeon Ki, Kevin Duh, Marine Carpuat  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Large Reasoning Models (LRMs) show strong performance in English, they often fail to reason in the language of the query, a phenomenon known as language collapse. Existing RL-based fixes typically add a binary language fidelity reward to the accuracy objective, yet still incur trade-off in accuracy, mid-trace code-switching, and excessive token usage. In this work, we propose AdaMame, a two-stage training recipe for multilingual mathematical reasoning that addresses these limitations by adaptively aligning the reasoning language to the query language without compromising accuracy. The first SFT stage fine-tunes on naturally occurring reasoning traces across five languages to establish multilingual reasoning capability. In the subsequent RL stage, we introduce AdaMame-GRPO, an adaptation of Group Relative Policy Optimization (GRPO) in which a query-conditioned alignment factor grows progressively during training, guiding the model to first explore diverse reasoning languages before exploiting reasoning in the query language. Evaluated across two benchmarks, two LRMs, and 12 languages, AdaMame-GRPO achieves Pareto-optimal performance across reasoning accuracy, language fidelity, and token efficiency over all baselines, with the strongest gains on out-of-domain, lower-resource languages.

---


### 85. [An Integrable Token Mixing Layer from the Generalized Yang Baxter Equation](https://arxiv.org/abs/2606.15085)

**<font color=#1a73e8>作者：</font>** Snigdha Chandan Khilar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The YB Mixer is a sequence token mixing layer derived from free fermion and generalized Yang Baxter structures. It applies a core principle from integrable systems where a local algebraic constraint guarantees global computational stability. By using the Ising exchange algebra the mixer creates a free fermionic structure that acts as an exactly norm preserving orthogonal map. This algebra also produces commuting transfer matrices which allow inference to be order free and adaptable to any variable budget. To ensure the model can generalize to longer sequence lengths it uses a spectral circulant generator. This generator maintains the crucial orthogonal and commuting properties of the system. The result is a highly stable and mathematically grounded architecture for sequence processing.

---


### 86. [Sensory Restoration via Brain-Computer Interfaces: A Unified 2 x 2 Framework and Convergence Roadmap](https://arxiv.org/abs/2606.15091)

**<font color=#1a73e8>作者：</font>** Xuan-The Tran  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Millions of individuals worldwide suffer from sensory and communication deficits caused by neurodegenerative diseases, stroke, or trauma. Brain-computer interfaces (BCIs) offer a promising avenue for sensory and motor restoration. However, the scientific literature remains highly fragmented between invasive neuroprosthetics and non-invasive electrophysiological decoders, with a lack of consistent terminology and comparison metrics. This chapter proposes a unified 2 x 2 framework categorizing BCIs along two axes: degree of invasiveness (invasive vs. non-invasive) and signal direction (afferent sensory-IN vs. efferent sensory-OUT). We define and distinguish the paradigms of restoration, substitution, and augmentation. Furthermore, we outline a structural roadmap for the convergence of these modalities over near-, medium-, and long-term horizons, focusing on physical limits and the integrative role of machine learning foundation models.

---


### 87. [Fuzzy PSI from Symmetric Primitives with Exact Logarithmic Dependence on Distance Threshold](https://arxiv.org/abs/2606.15093)

**<font color=#1a73e8>作者：</font>** Cong Zhang, Yang Cao, Yujie Bai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Previous FPSI works have demonstrated a linear scaling with the distance threshold $\delta$, while some recent works have achieved a poly-logarithmic dependence on $\delta$. However, these protocols either support only the $L_\infty$ distance, or they support general $L_{p\in[1,\infty]}$ distances but rely on expensive additive homomorphic encryption (AHE). Achieving exact logarithmic dependence on $\delta$ for general $L_{p\in[1,\infty]}$ distances without relying on costly AHE would constitute a theoretical breakthrough in optimal threshold scaling and a practical advance toward scalable FPSI applications.
In this work, we present new FPSI protocols for $L_{p\in[1,\infty]}$ distances that are entirely built from oblivious transfer (OT) and symmetric-key primitives. We propose FPSI protocols based on both the apart and the separate assumptions, which are applicable to low- and high-dimensional settings, respectively. Our constructions achieve strictly logarithmic complexity in $\delta$, which is optimal in the sense that distinguishing all values in an interval of length $O(\delta)$ necessarily requires $\Omega(\log \delta)$ bits of information. Our core idea is to perform fuzzy matching via prefix representation and interactively determine the correct prefix using equality conditions. To this end, we propose a suite of new components that can be implemented efficiently using only OT and symmetric-key operations.
We implement our FPSI protocols and compare them with the state-of-the-art FPSI protocols for $L_{p\in[1,\infty]}$ distance. Experiments show that our protocols outperform the prior state-of-the-art by up to $43.7\times$ in runtime and $31.3\times$ in communication.

---


### 88. [Think Less, Act Early: Reinforced Latent Reasoning with Early Exit in Vision-Language-Action Models](https://arxiv.org/abs/2606.15099)

**<font color=#1a73e8>作者：</font>** Dianqiao Lei, Lianlei Shan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing Vision-Language-Action (VLA) models predominantly rely on explicit Chain-of-Thought (CoT) reasoning to bridge perception and action. While effective, this paradigm suffers from high computational costs and error propagation in multi-step tasks. In this paper, we propose Adaptive Variable Alignment VLA (AVA-VLA), a novel Latent Reasoning VLA framework that models reasoning as a sequence of unobservable latent variables, bypassing the need for explicit text generation. However, latent trajectories are inherently susceptible to noise interference and misalignment with downstream objectives. To address this, we introduce a Reinforcement Learning-based Denoising mechanism that treats latent state generation as a sequential decision process, optimizing reasoning trajectories via task-level rewards. Furthermore, we incorporate an Early-Exit Strategy that adaptively terminates reasoning based on state confidence, enabling a dynamic trade-off between depth and efficiency. Extensive experiments on embodied decision benchmarks demonstrate that AVA-VLA achieves a 6x inference speedup over explicit CoT methods while attaining a 98.3% average success rate on LIBERO, improving both efficiency and long-horizon stability over full-reasoning baselines.

---


### 89. [Text-Driven Fusion for Infrared and Visible Images: Achieving Image Scene Adaptation on Hyperbolic Space](https://arxiv.org/abs/2606.15104)

**<font color=#1a73e8>作者：</font>** Huan Kang, Hui Li, Tianyang Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared and visible image fusion aims to integrate complementary modalities, while existing Euclidean methods impose rigid distance metrics that distort multi-modal interactions and parent-to-child semantic hierarchies. To overcome these limitations, we introduce a text-driven fusion framework empowered by hyperbolic manifold learning. During training, BLIP-extracted text prompts serve as topological anchors within the hyperbolic space, guiding vision-attribute alignment through hyperbolic embeddings that naturally accommodate varying semantic granularities. By exploiting the exponential volume growth dictated by the Poincaré ball's negative curvature, this approach seamlessly embeds hierarchical trees to encode coarse-to-fine semantics without metric saturation, while the vast peripheral space prevents texture distortion during cross-modal fusion. At inference, the fusion process autonomously adapts to input content using the learned text-attribute priors, completely eliminating the need for textual input. Experimental results show our method outperforms state-of-the-art approaches on benchmark datasets, with code available at this https URL.

---


### 90. [Physics-Driven Zero-Shot MRI Reconstruction with Non-local Image Priors](https://arxiv.org/abs/2606.15110)

**<font color=#1a73e8>作者：</font>** Lingtong Zhang, Wenlei Li, Mu He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-Shot Self-Supervised Learning (ZS-SSL) has emerged as a promising paradigm for accelerated Magnetic Resonance Imaging (MRI) reconstruction, eliminating the reliance on fully-sampled external datasets. However, learning solely from a single under-sampled scan suffers from supervision scarcity and optimization instability, often leading to overfitting or artifacts. To address these challenges, we propose a robust physics-driven ZS-SSL framework that synergizes physical consistency with image-domain non-local priors. Our method introduces three core innovations: (1) a Coil Sensitivity Map (CSM)-Guided Dynamic Repository, which stabilizes the training trajectory by filtering physically inconsistent artifacts based on coil sensitivity constraints; (2) a SPIRiT-based regularization, which enforces k-space self-consistency via a learned correlation kernel and stochastic masking; (3) a Non-Local Self-Similarity (NSS) Pixel Bank, which leverages the high-fidelity reference established by the former modules to explicitly mine non-local anatomical similarities, thereby augmenting supervision in the image domain. Extensive experiments on the FastMRI dataset demonstrate that our approach achieves state-of-the-art performance, particularly under high acceleration factors, effectively bridging the gap between zero-shot learning and supervised methods. The code is available at this https URL.

---


### 91. [Learn Temporal Consistency For Robust Satellite Video Detector](https://arxiv.org/abs/2606.15112)

**<font color=#1a73e8>作者：</font>** Weilong Guo, Shengyang Li, Yanfeng Gu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Satellite video object detection (SVOD) for oriented and fine-grained objects plays an important role in satellite applications. Most existing SVOD methods only focus on one or a few coarse-grained categories of moving objects and represent objects with horizontal bounding boxes. They have difficulty extracting complete, accurate, and consistent information about objects in whole satellite videos. In this paper, we propose a satellite video object detection framework based on Temporal Consistency Learning (TCL). TCL adeptly detects oriented and fine-grained objects by leveraging the rich temporal contexts within satellite videos. The framework integrates three key modules: temporal and fine-grained feature aggregation (TFA), structure encoding (SE), and temporal consistency constraint (TCC). TFA and TCC modules facilitate consistent representation learning across frames, while the SE module encodes both appearance and structural information for precise fine-grained recognition. Experimental results on the SAT-MTB benchmark dataset demonstrate TCL's superior performance, achieving a new state-of-the-art oriented and fine-grained detection accuracy of 47.7% mAP--a 4.8% improvement over the baseline. Furthermore, our TCL framework readily accommodates existing image-based detectors, leading to enhanced detection accuracies.

---


### 92. [Diversity-Driven Offline Multi-Objective Optimization via Nested Pareto Set Learning](https://arxiv.org/abs/2606.15115)

**<font color=#1a73e8>作者：</font>** Yiyi Zhu, Yaolin Wen, Xiang Xia 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-objective optimization (MOO) has emerged as a powerful approach to solving complex optimization problems involving multiple objectives. In many practical scenarios, function evaluations are unavailable or prohibitively expensive, necessitating optimization solely based on a fixed offline dataset. In this setting, known as offline MOO, the goal is to find out the Pareto set without access to the true objective functions. This setting suffers from the out-of-distribution (OOD) issue, where the surrogate model is not accurate for unseen designs. Due to the OOD issue, surrogate errors may cause the optimizer to select solutions that do not lie on the true Pareto front and are biased toward its extremes. To address this, this paper proposes Diversity-driven Offline Multi-Objective Optimization (DOMOO), which aims to find out a diverse and high-quality set of solutions. First, DOMOO incorporates an accumulative risk control module that estimates the potential risk of candidate solutions and alleviates the OOD issue between the training data and the generated solutions. In addition, a nested Pareto set learning (PSL) strategy is proposed to jointly learn preference and PSL parameters, then optimize them, enabling adaptation to diverse Pareto front geometries. To further enhance solution quality, we design a diversity-driven selection strategy that extracts a representative and well-distributed set of final solutions. To achieve this diversity-driven selection strategy, we propose $\text{IGD}_\text{offline}$, a tailored indicator for the offline setting that considers both diversity and convergence, and avoids the bias of hypervolume indicator. Extensive experiments on synthetic and real-world benchmarks show that DOMOO achieves the best average rank across tasks in both convergence and diversity among the compared methods.

---


### 93. [Graph of Trace: Visualizing Execution Traces of Scientific Agent](https://arxiv.org/abs/2606.15116)

**<font color=#1a73e8>作者：</font>** Tianci Gao, Haoxuan Li, Jianhe Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Scientific AI agents can autonomously carry out complex research workflows, yet these unfolded workflows often remain difficult for humans to inspect and review, limiting interpretable, controllable and effective human-AI collaboration. To address this challenge, we present a monitoring and visualization framework that records fine-grained execution events and organizes them into a directed graph that makes agent workflows explicit as they proceed. The system records intermediate steps (e.g. tool calls and code executions), and renders them as real-time updated visual traces that expose workflow structure. This allows users to examine how results are produced, identify where failures emerge, and better understand agent behavior across different stages of the research process. We conduct an evaluation on complex research tasks with domain experts of interdisciplinary backgrounds in AI, neuroscience, and biology. Experts report that structured traces visualization improves understanding of agent workflows, perceived interpretability, and usability for analysis and further interaction.

---


### 94. [Multi-view feature High-order Fusion for Space Weak Object Detection and Segmentation](https://arxiv.org/abs/2606.15118)

**<font color=#1a73e8>作者：</font>** Weilong Guo, Yuhan Sun, Shengyang Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Weak objects are common in images and videos of space applications. However, it is hard to learn proper representations from their limited appearance information. Inspired by multi-view learning, we develop simple multi-view attentions, treating their outputs as multi-view features. We also propose a multi-view feature high-order fusion method (MHF) to aggregate more accurate and richer features of weak objects. Our MHF extends the commonly used low-order feature fusion method to higher orders. It enhances the model's capacity to capture relevant and complementary information about weak objects. This is achieved by introducing high-order multi-view features perception and a recursive task-contribution gated selection of multi-view features. The new operation is highly flexible and customizable. It is compatible with various variants of multi-view feature representations. We conduct extensive experiments on two newly constructed space science datasets and an open, large-scale satellite video dataset. Our MHF serves as a plug-and-play module and significantly improves various vision transformers and convolution-based detection and segmentation models. We achieve all state-of-the-art accuracies on both tasks across three datasets. Our MHF can be a new basic module for visual modeling that effectively represents weak objects in terms of multi-view learning. The code will be available at this https URL.

---


### 95. [Beyond Accuracy: Measuring Bias Acknowledgment in Chain-of-Thought Reasoning for Responsible AI Evaluation](https://arxiv.org/abs/2606.15127)

**<font color=#1a73e8>作者：</font>** Xian Sun, Wei Gao, Yingshuo Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reasoning models are increasingly used in settings where the final answer is not the only object of review: educational tools may show students intermediate steps, decision-support systems may require human oversight, and audit workflows may inspect traces for misleading or biased input. In such settings, two responses can receive the same final-answer score while differing in whether the trace explicitly flags injected biasing content. Accuracy-only evaluation collapses these cases. We study this gap as a measurement blind spot for responsible evaluation and introduce a minimal trace-level diagnostic with two axes: \emph{susceptibility} (whether the bias breaks a previously correct answer) and \emph{acknowledgment} (whether the trace contains a rubric-defined surface reference to the injected content). Across thousands of biased GSM8K trials, GPT-4o and Claude Sonnet~4 have similar susceptibility rates ($1.3\%$ vs.\ $1.2\%$) but substantially different acknowledgment rates ($13.0\%$ vs.\ $75.0\%$) under the same rubric.

---


### 96. [EyeMVP: OCT-Informed Fundus Representation Learning via Paired CFP--OCT Pretraining](https://arxiv.org/abs/2606.15129)

**<font color=#1a73e8>作者：</font>** Zhuo Deng, Ruiheng Zhang, Ziheng Zhang 等 26 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Color fundus photography (CFP) is the mainstay for large-scale retinal screening, yet its diagnostic capacity is constrained by the lack of depth-resolved structural information. Optical coherence tomography (OCT) provides cross-sectional retinal anatomy, but is less accessible in population-level screening. Here, we present EyeMVP, a cross-modal retinal foundation model that uses paired CFP--OCT pretraining to learn OCT-informed CFP representations. EyeMVP is pretrained on 674,893 strict same-eye same-day paired CFP--OCT image triples from 112,642 patients across eight hospitals in China. The model uses cross-modal masked reconstruction to enrich CFP representations with OCT-associated supervision, while requiring only CFP images at inference. To accommodate the non-aligned imaging geometry between en-face CFP and cross-sectional OCT, EyeMVP combines source-constrained cross-attention with CFP-derived structural masks. Across 16 downstream tasks, including classification, segmentation, few-shot adaptation, and cross-modal retrieval, EyeMVP outperforms representative retinal foundation models and shows consistent gains on tasks involving macular and optic nerve structure. For CFP-challenging macular diseases, EyeMVP achieves an AUROC of 0.948 for macular edema (vs.~0.852 for EyeCLIP) and 0.825 for myopic macular schisis. In an exploratory reader study, EyeMVP exceeds junior and intermediate ophthalmologist groups but does not reach senior ophthalmologist performance on macular edema, while showing numerically higher balanced accuracy than all reader groups on myopic macular schisis. These results suggest that pixel-level cross-modal reconstruction can enrich CFP representations with OCT-associated supervision, providing a practical route toward stronger CFP-based retinal analysis in screening settings.

---


### 97. [MotionVLA: Vision-Language-Action Model for Humanoid Motion](https://arxiv.org/abs/2606.15142)

**<font color=#1a73e8>作者：</font>** Nonghai Zhang, Siyu Zhai, Yanjun Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating realistic humanoid motion from scene images and text involves both low-frequency pose semantics and high-frequency physical dynamics. However, many existing methods tokenize motion with a single shared codebook, forcing heterogeneous motion signals into the same quantization space. Our frequency-domain analysis of human motion data reveals a clear mismatch between single-codebook quantization and motion statistics: five DCT coefficients capture 93% of joint-position energy but only 37% of joint-velocity energy, which can bias quantization toward pose statistics and under-represent high-frequency velocity components. A second challenge lies in adapting a standard autoregressive model to effectively model high-frequency physical signals in motion sequences. Therefore, we propose DSFT, a dual-stream frequency tokenizer that separates motion into Base and physical streams and compresses them independently with DCT truncation and BPE. Furthermore, we present MotionVLA, a Qwen3.5-based model that arranges Base and physical tokens in a unified sequence, where Phys tokens are predicted after Base tokens. Experiments on HumanML3D and MBench show that, despite using a lightweight 2B backbone, MotionVLA reduces the Diversity gap to real data by over 50% on HumanML3D and improves Motion-Condition Consistency by 3.8% on MBench, supporting frequency-aware dual-stream decoupling as an effective formulation for autoregressive motion generation. Code: this https URL. Website: this https URL.

---


### 98. [PACUTE: Phonology-, Affix-, and Character-level Understanding of Tokens for Filipino](https://arxiv.org/abs/2606.15144)

**<font color=#1a73e8>作者：</font>** Jann Railey Montalan, David Demitri Africa, Jimson Paulo Layacan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) process text as sequences of subword tokens, which can obscure the character-level and morphological structure that underlies word formation. This limitation is most acute for languages with non-concatenative morphology, where standard tokenizers systematically misalign token boundaries with morpheme boundaries. We introduce PACUTE, a diagnostic benchmark of 4,600 tasks designed to evaluate morphological understanding in Filipino, a language characterized by productive infixation, reduplication, and diacritic-driven lexical distinctions that are typically absent from written text. PACUTE includes a hierarchical diagnostic framework of six compositional levels that localizes where morphological understanding breaks down. Evaluating open-weight LLMs and frontier commercial models, we find that open-weight models perform near chance on morpheme decomposition regardless of scale. Frontier models perform much better, often recovering individual affixes under contains-match scoring, but remain far below their character-level ceilings on compositional tasks of morpheme transformations and syllabification. These results identify productive morphological composition, rather than character access alone, as the persistent bottleneck for Filipino word-structure understanding.

---


### 99. [Contextual Bandits for Maximizing Stimulated Word-of-Mouth Rewards](https://arxiv.org/abs/2606.15146)

**<font color=#1a73e8>作者：</font>** Ahmed Sayeed Faruk, Elena Zheleva  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stimulated word-of-mouth is a strategy that promotes information sharing through prompts or incentives. Optimizing stimulated word-of-mouth through social networks requires identifying and targeting connected users who are most susceptible to spillover, a phenomenon where the influence of recommendations extends beyond the immediate audience to impact their connected users. The probability of spillover varies across individuals, and their connections, leading to heterogeneity. Understanding and accurately estimating the spillover probabilities among users in social networks is crucial for improving the effectiveness of stimulated word-of-mouth. To address this, we present a novel contextual multi-armed bandit framework that learns individual spillover probabilities and ranks connected users to maximize rewards from stimulated word-of-mouth. Experiments on real-world network datasets demonstrate that accounting for spillover heterogeneity enhances the targeting precision of top-$k$ connected users, boosting rewards and outperforming baseline methods that do not learn individual spillover effects.

---


### 100. [HiRo: A Compact Four-Directional Hierarchical Reservoir Token-Mixer for Efficient Image Classification](https://arxiv.org/abs/2606.15151)

**<font color=#1a73e8>作者：</font>** Md Farhadul Islam, Ishan Thakkar, J. Todd Hastings  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent image classification models must balance local feature modeling, cross-window interaction, and parameter efficiency. Many high-performing architectures rely on fully trainable token-mixers, which improve representation learning but increase parameter count, optimization complexity and computational cost. We propose a parameter-efficient image classification model called HiRo that integrates shifted-window partitioning with multi-directional hierarchical reservoir computing. Images are divided into non-overlapping patches (treated as tokens), linearly projected, normalized, and enriched with 2D sinusoidal positional encodings, then processed within local windows. Inside each window, tokens are scanned in four directions and passed through a two-stage slice-and-mix reservoir module. In the first stage, directional sequences are split into contiguous slices, each processed by its own fixed reservoir with a trainable closed-loop readout. The resulting slice outputs are summarized using the start, end, and mean representations, and then mixed by a second-stage fixed reservoir for each direction. The mixed slice representations are expanded back to the token level and fused with the first-stage outputs, after which the four directional outputs are realigned and averaged. Consecutive blocks alternate between regular and shifted windows to enable cross-window interaction, followed by layer normalization, a residual feed-forward network, and global pooling for classification. This design combines regular and shifted window partitioning with hierarchical multi-directional reservoirs to make an efficient local-to-cross-window token-mixing framework for image classification. Despite using under 1M trainable parameters and significantly lower memory and time than transformer-style baselines, HiRo also achieves 99.46%, 85.57%, and 59.10% accuracy on MNIST, CIFAR-10, and CIFAR-100, respectively.

---


> [!TIP]
> 当前位于：**51-100**（第 2/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-509](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
