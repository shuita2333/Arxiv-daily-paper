# 📦 其他研究 | 2026年05月23日

> 本类共 **347** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-347](./part-07.md)

---

### 251. [BeLink: Biomedical Entity Linking Meets Generative Re-Ranking](https://arxiv.org/abs/2605.22501)

**<font color=#1a73e8>作者：</font>** Darya Shlyk, Stefano Montanelli, Lawrence Hunter  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite recent progress, Biomedical Entity Linking (BEL) with large language models (LLMs) remains computationally inefficient and challenging to deploy in practical settings. In this work, we demonstrate that instruction-tuning of open-source generative models can offer an effective solution when applied at the re-ranking stage of the BEL pipeline. We propose a set-wise instruction-tuning formulation that enables fast and accurate candidate selection. Our method demonstrates strong performance on multiple BEL benchmarks, yielding significant improvements in linking accuracy (3%-24%) while reducing inference time compared to the state-of-the-art. We integrate our generative re-ranker into BeLink, a modular, end-to-end system designed for practical real-world BEL applications.

---


### 252. [LACO: Adaptive Latent Communication for Collaborative Driving](https://arxiv.org/abs/2605.22504)

**<font color=#1a73e8>作者：</font>** Tianhao Chen, Yuheng Wu, Dongman Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Collaborative driving aims to improve safety and efficiency by enabling connected vehicles to coordinate under partial observability. Recent approaches have evolved from sharing visual features for perception to exchanging language-based reasoning through foundation models for behavioral coordination. Though communicating in language provides intuitive information, it introduces two challenges: high latency caused by autoregressive decoding and information loss caused by compressing rich internal representations into discrete tokens. To address these challenges, we analyze latent communication in collaborative driving under inherent limitations of multi-agent settings. Our analysis reveals agent identity confusion, where direct fusion of latent states entangles decision representations across vehicles. Motivated by this, we propose LACO, a training-free \textbf{LA}tent \textbf{CO}mmunication paradigm that seamlessly adapts pretrained driving models to collaborative settings. LACO introduces Iterative Latent Deliberation (ILD) for latent reasoning, Cross-Horizon Saliency Attribution (CHSA) for communication-efficient information selection, and Structured Semantic Knowledge Distillation (SSKD) to stabilize ego-centric decision making. Closed-loop experiments in CARLA show that LACO notably reduces communication and inference latency while maintaining strong collaborative driving performance.

---


### 253. [Towards Direct Evaluation of Harness Optimizers via Priority Ranking](https://arxiv.org/abs/2605.22505)

**<font color=#1a73e8>作者：</font>** Kai Tzu-iunn Ong, Minseok Kang, Dongwook Choi 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Harness optimization enables automated agent creation by having an optimizer agent iteratively update the harness of target agents. Despite its success, current studies evaluate optimizers solely by observing target agents' performance gains. This indirect end-improvement evaluation neglects optimizers' actions at intermediate steps, which are often erroneous and hinder agent performance. Therefore, it is unclear whether harness optimization is driven by optimizers' informed update actions or simply trial-and-error. This necessitates direct evaluation of harness optimizers. However, evaluating harness optimizers directly is non-trivial and costly due to the lack of oracle harnesses. To address this, we present a simple, low-cost design to directly evaluate them, namely priority ranking. By asking harness optimizers to rank components (e.g., tools) in a given harness by their potential to improve/hinder agent performance when updated, our design quantifies optimizer ability at the step level without expensive rollouts or manual examination. More importantly, optimizers' ranking performance correlates with their ability to improve agents in actual multi-step harness optimization, establishing priority ranking as a reliable predictor of optimization ability. Priority ranking is enabled by Shor, a collection of 182 human-verified optimization scenarios spanning across domains, designs, and time stages. Codes and data can be found at this https URL.

---


### 254. [EnCAgg: Enhanced Clustering Aggregation for Robust Federated Learning against Dynamic Model Poisoning](https://arxiv.org/abs/2605.22506)

**<font color=#1a73e8>作者：</font>** Tianyun Zhang, Zhen Yang, Haozhao Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated learning faces increasing threats from model poisoning attacks, which harms its application to improve privacy. Existing defense methods typically rely on fixed thresholds or perform clustering with a fixed number of clusters to distinguish malicious gradients from benign ones. However, these methods are difficult to adapt to dynamic poisoning strategies of malicious clients, and often result in the loss of benign gradients due to the heterogeneity of clients' local datasets. To address these problems, we propose a novel robust aggregation method that leverages a small number of known benign clients as references, enabling accurate identification and filtering of malicious gradients while retaining as many benign gradients as possible, even when the number of malicious clients is unknown and variable. First, we introduce a density-based low-dimensional gradient clustering method, which projects gradients onto the two most divergent dimensions and applies density-based clustering to identify malicious gradients while retaining clustered benign gradients and potentially benign outliers. Second, we design an enhancing clustering low-dimensional gradient generator model, which learns to generate pseudo-gradients aligned with the boundary of the benign cluster. These pseudo-gradients act as bridges to connect sparse benign gradient outliers. Third, we introduce low-dimensional gradient re-clustering that clusters the generated pseudo-gradients together with real gradients to recover benign gradients misclassified as noise points, enabling more benign gradients to participate in aggregation. Extensive experiments on the MNIST, CIFAR-10, and MIND datasets demonstrate that our method exhibits superior fidelity and robustness under dynamic poisoning scenarios.

---


### 255. [Generative Modeling by Value-Driven Transport](https://arxiv.org/abs/2605.22507)

**<font color=#1a73e8>作者：</font>** Pablo Moreno-Muñoz, Adrian Müller, Gergely Neu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a new framework for generative modeling based on a discrete-time stochastic control formulation of measure transport. Adapting classic results from control theory, we formulate our problem as a linear program whose dual variables correspond to the \emph{optimal value function} of the control problem, which directly encodes the optimal control policy. Exploiting this LP formulation, we develop an efficient simulation-free primal-dual algorithm for computing approximately optimal value functions and the associated \emph{value-driven transport} (VDT) policies which approximate the true optimal policy. We show that well-trained VDT policies enjoy numerous favorable properties in comparison with other state-of-the-art methods based on flows, diffusions, or Schrödinger bridges: they lead to straight transport paths which can be simulated quickly and robustly, and can be enhanced in all the same ways as diffusion and flow-based models (e.g., conditional generation, classifier-free guidance, unpaired data-to-data translation are all easy to incorporate). We evaluate our methodology in a range of experiments, with results that indicate strong performance and good potential for scalability.

---


### 256. [Reflecti-Mate: A Conversational Agent for Adaptive Decision-Making Support Through System 1 and System 2 Thinking](https://arxiv.org/abs/2605.22509)

**<font color=#1a73e8>作者：</font>** Morita Tarvirdians, Senthil Chandrasegaran, Hayley Hung 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Making high-stakes personal decisions involves cognitive, emotional, and intuitive processes, and individuals differ in how they allocate attention across these modes. Integration of these processes has shown to benefit decision making. Yet, most current decision-support systems focus primarily on supporting cognitive aspects, rather than adapting to the individual's thinking profile to support integration of different types of thoughts. In this study, we investigate an agent designed to encourage integration by adapting to the individual user's thought patterns. We explore its effects on participants' perceptions of the agent and their reflective behavior, in comparison with unaided pre-reflection and a baseline agent. In a between-subjects study (N = 128), our agent, which fostered broad and elaborated thinking, enabled more personalized reflective trajectories, elicited more integrative reflective language, and was perceived as providing stronger support for holistic reflection. In contrast, the baseline agent produced homogenized profiles dominated by cognitive language across participants.

---


### 257. [Meta-Learning for Rapid Adaptation in Reference Tracking of Uncertain Nonlinear Systems](https://arxiv.org/abs/2605.22513)

**<font color=#1a73e8>作者：</font>** Jiaqi Yan, Ankush Chakrabarty, Niklas Schmid 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this paper, we address the problem of reference tracking for uncertain nonlinear systems. Since collecting data from the target system (i.e., the system of interest) is often challenging, our objective is to design optimal controllers using limited target system data. Meta-learning provides a promising paradigm by leveraging offline data from source systems (systems sharing structural similarities with the target system) to accelerate training and enhance control performance. Motivated by this idea, we propose a meta-learning-based control framework that tailors the implicit model-agnostic meta-learning (iMAML) algorithm to the control setting. The framework operates in two phases: an (offline) meta-training phase, where an aggregated representation is learned from source data to capture the shared system dynamics among similar systems, and an (online) meta-adaptation phase, where this representation is fine-tuned on the target system using only a few data samples and limited adaptation steps. We formulate this framework as a bi-level optimization problem and provide an efficient solution with reduced storage complexity and few approximations. The proposed framework is general, allowing various learning algorithms to be integrated. To demonstrate this flexibility, we propose two specific learning algorithms that can be incorporated into our framework based on a neural state-space model and a deep Q-network, respectively. The primary distinction between these approaches is whether explicit system identification is required. Numerical simulations and hardware experiments demonstrate that the proposed methods enhance control performance and consistently outperform baseline approaches.

---


### 258. [A Subjective Logic-based method for runtime confidence updates in safety arguments](https://arxiv.org/abs/2605.22530)

**<font color=#1a73e8>作者：</font>** Benjamin Herd, Jessica Kelly, Clarissa Heinemann 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present a method for dynamic quantitative assurance that enhances static safety cases with continuous, runtime-driven confidence updates. The method quantifies and propagates confidence across the development lifecycle by integrating design-time evidence and windowed runtime Safety Performance Indicators (SPIs) within a single Subjective Logic (SL)-based assurance case. At runtime, SPI evidence is continuously evaluated, and targeted claims are updated using a rule that increases confidence in the absence of violations and imposes prompt penalties when violations occur. This design prioritizes safety-relevant responsiveness over exact classical Bayesian posterior updates. We demonstrate the method using a simulation-based construction zone assist function, focusing on an ML-based construction cone detection component, and show how confidence evolves as SPI evidence is observed in operation.

---


### 259. [Disentanglement Beyond Generative Models with Riemannian ICA](https://arxiv.org/abs/2605.22531)

**<font color=#1a73e8>作者：</font>** Edmond Cunningham  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> There is a gap between the theoretical foundations of disentanglement and the practice of modern representation learning. Existing theoretical frameworks, particularly Independent Component Analysis (ICA) and its nonlinear variants, assume a generative model with statistically independent latent variables underlying the data so that disentanglement amounts to identifying the latents that could have generated the data. This generative framework is interpretable and theoretically justified, but its strong assumptions make it difficult to apply to modern representation learning. Modern pretrained encoders often learn features that exhibit disentangled properties without making generative assumptions, yet there is no general theory for interpreting these features as independent factors of variation. We take a step toward such a theory by introducing Riemannian ICA (RICA), which replaces ICA's global generative model with local geometric structure. RICA is founded on the observation that in ICA, the factors of variation underlying a data point can be understood through radial curves emanating from the point that map to axis-aligned lines in the latent space. We formalize this perspective using Riemannian geometry and introduce our theory in a way that is consistent with the existing generative approach. Our main contribution is the disentanglement tensor, which encodes a second-order notion of disentanglement that we call pointwise disentanglement. This tensor depends on the Hessian of the data log likelihood as well as the Ricci curvature induced by the model. In a controlled source recovery setting with known ground-truth sources, RICA recovers sources across several manifolds, while the success of ICA baselines depends on the coordinates used to represent the observations. Our work provides a theoretical basis for studying local disentanglement without assuming a global generative model.

---


### 260. [TerminalWorld: Benchmarking Agents on Real-World Terminal Tasks](https://arxiv.org/abs/2605.22535)

**<font color=#1a73e8>作者：</font>** Zhaoyang Chu, Jiarui Hu, Xingyu Jiang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce TerminalWorld, a scalable data engine that automatically reverse-engineers high-fidelity evaluation tasks from "in-the-wild" terminal recordings. Processing 80,870 terminal recordings, the engine yields a full benchmark of 1,530 validated tasks, spanning 18 real-world categories, ranging from short everyday operations to workflows exceeding 50 steps, and covering 1,280 unique commands. From these, we curate a Verified subset of 200 representative, manually reviewed tasks. Comprehensive benchmarking on TerminalWorld-Verified across eight frontier models and six agents reveals that current systems still struggle with authentic terminal workflows, achieving a maximum pass rate of only 62.5%. Moreover, TerminalWorld captures real-world terminal capabilities distinct from existing expert-curated benchmarks (e.g., Terminal-Bench), with only a weak correlation to their scores (Pearson r=0.20). The automated engine makes TerminalWorld authentic and scalable by construction, enabling it to evaluate agents in real-world terminal environments as developer practices evolve. Data and code are available at this https URL.

---


### 261. [F-TIS: Harnessing Diverse Models in Collaborative GRPO](https://arxiv.org/abs/2605.22537)

**<font color=#1a73e8>作者：</font>** Nikolay Blagoev, Oğuzhan Ersoy, Wendelin Boehmer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning methods such as GRPO have seen great popularity in LLM post-training. In GRPO, models produce completions to a set of prompts, which are rewarded, and the policy is updated towards the relatively high reward completions. Due to the auto-regressive nature of models, the generation phase of such style of training can be extremely time consuming. As a solution, prior work has sought to distribute the inference step across many nodes, working parallel. These works assume primarily homogeneous models in the training in order to keep samples as close to on-policy as possible. This assumption may be impractical in decentralized systems, where parties with various computes and preferences may wish to collaborate on the same task. Thus, decentralized training requires an approach that can handle heterogeneous models - different models collaborating on the same tasks. However, this leads to highly off-policy samples presented during training, which prior work has identified that off-policy samples can hurt GRPO convergence. To enable heterogeneity, we propose Filtered Truncated Importance Sampling (F-TIS) - a GRPO-style training paradigm that can use off-policy samples to improve local model's learning. Our framework allows various models to collaborate in the same RL training run while being communication efficient. We extensively evaluate F-TIS in various heterogeneous setups and we show that it exhibits identical final model convergence to purely on-sample training. Furthermore, we observe in some setups better generalization on out-of-distribution tasks than on-policy training, increasing model's performance by up to 12\%.

---


### 262. [Segment Anything with Motion, Geometry, and Semantic Adaptation for Complex Nonlinear Visual Object Tracking](https://arxiv.org/abs/2605.22538)

**<font color=#1a73e8>作者：</font>** Deyi Zhu, Yuji Wang, Yong Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traditional visual object tracking (VOT) methods typically rely on task-specific supervised training, limiting their generalization to unseen objects and challenging scenarios with distractors, occlusion, and nonlinear motion. Recent vision foundation models, exemplified by SAM 2, learn strong video understanding priors from large-scale pretraining and offer a promising foundation for building more robust and generalizable trackers. However, directly applying SAM 2 to VOT remains suboptimal, as it does not explicitly model target motion dynamics or enforce geometric and semantic consistency across frames, both of which are essential for reliable tracking. To address this issue, we propose SAMOSA, a new tracking framework that adapts SAM 2 to complex VOT scenarios by explicitly leveraging motion, geometry, and semantic cues. Specifically, we introduce a lightweight nonlinear motion predictor to model target dynamics and guide mask selection as well as memory filtering. We further exploit semantic cues to detect target shifts and recover from tracking failures, while geometric cues are incorporated as structural constraints to improve tracking stability. In this way, SAMOSA bridges the gap between the implicit video understanding prior of SAM 2 and explicit tracking-oriented modeling. Extensive experiments show that SAMOSA consistently outperforms state-of-the-art SAM 2--based approaches on general benchmarks, demonstrates stronger generalization than supervised VOT methods, and achieves substantial gains on anti-UAV datasets, which typify complex nonlinear motion scenarios. Our code is available at this https URL.

---


### 263. [Scene Abstraction for Lexical Semantics: Structured Representations of Situated Meaning](https://arxiv.org/abs/2605.22542)

**<font color=#1a73e8>作者：</font>** Yejin Cho, Katrin Erk  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Coffee and tea share many properties, yet they evoke strikingly different situations, atmospheres, and affective associations. These situated dimensions of word meaning are real and systematic, but they remain implicit in most computational representations of lexical meaning. We propose Scene Abstraction, a framework for constructing structured representations of the interpretive scenes that words participate in across usage contexts. Each scene consists of a Contextual Scene (Events, Entities, Setting) and an expression-centered Expression Profile (Engaged events, Generalizable properties, Evoked emotions), operationalized through few-shot prompting of a large language model. Our contributions are three-fold: (1) a structured representation framework for situated lexical meaning; (2) COCA-Scenes, a dataset of 520 usage instances across 26 keywords for distinct scene identification; and (3) empirical evidence from two experiments suggesting that scenes are reliably identifiable across human observers (82.4% accuracy, +11.8 pp over text-only embeddings) and that our scene profiles more closely align with human interpretation of words in context than ATOMIC-based alternatives (86.4% preference across three semantic dimensions).

---


### 264. [One prompt is not enough: Instruction Sensitivity Undermines Embedding Model Evaluation](https://arxiv.org/abs/2605.22544)

**<font color=#1a73e8>作者：</font>** Yevhen Kostiuk, Kenneth Enevoldsen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Instruction embedding models have become common among state-of-the-art models, however are evaluated using a single prompt per task. The single-point evaluation ignores a main problem of the instruction-based approach namely: sensitivity to the phrasing of the instruction. We present an empirical study of prompt sensitivity across 6 embedding models, 11 datasets, and 15 task-specific prompts per dataset, a total of 990. We show that reported scores misrepresent the distribution of scores over plausible prompts. The default prompt can both systematically understate or overstate performance. Furthermore, we show that the leaderboard ranking is not robust to prompt selection: by choosing prompts favorably, any model in our study can be promoted to first place. Our findings suggest that single-prompt evaluation is insufficient for instruction-tuned embedding models and that benchmarks should incorporate prompt robustness, either by evaluating over multiple prompts or by reporting sensitivity alongside point estimates.

---


### 265. [ImplicitTerrainV2: Wavelet-Guided Spatially Adaptive Neural Terrain Representation](https://arxiv.org/abs/2605.22556)

**<font color=#1a73e8>作者：</font>** Haoan Feng, Xin Xu, Leila De Floriani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Digital elevation models (DEMs) underpin terrain analysis in Geographic Information Systems (GIS), but in their common raster form, they rely on interpolation for off-grid sampling and finite-difference operators for derivative-based analysis. Implicit neural representations (INRs) offer a continuous alternative, but prior terrain INRs lack explicit frequency control, neglect the gradient structure of terrain, and remain too large and costly to train for practical deployment. We present ImplicitTerrainV2, which advances terrain INRs toward a compact, efficient neural terrain data format by combining a spectral control mechanism with wavelet-guided spatial adaptivity, derivative-aware supervision, and post-training model compression. At its core, a wavelet complexity field (WCF) derives spatially-adaptive frequency masks from analytically computed wavelet coefficients, localizing high-frequency capacity to complex terrain regions. The same field guides complexity-aware adaptive sampling that concentrates training in high-complexity regions, while gradient matching applies extra supervision to enforce the smooth manifold structure of terrain DEMs for improved derivative fidelity. Post-training mixed-precision quantization and entropy coding reduce storage to 1.23 bpp with a 0.28 dB PSNR drop. On 50 Swiss terrain tiles, ImplicitTerrainV2 reaches 66.25 dB end-to-end PSNR, improving over the prior work by 5.70 dB while using 3.2x fewer parameters and training in 55 s per tile on a single GPU. Our compressed neural format is competitive with several established DEM codecs in rate-distortion performance, while additionally supporting off-grid point queries, closed-form derivative evaluation, and resolution-independent reconstruction, which may benefit many downstream GIS applications.

---


### 266. [Neural Flow Operators can Approximate any Operator: Abstract Frameworks and Universal Approcimations](https://arxiv.org/abs/2605.22557)

**<font color=#1a73e8>作者：</font>** Shuang Chen, Juncai He, Xue-Cheng Tai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce an abstract neural flow framework for neural networks and neural operators. The framework contains two continuous-depth models, namely neural flows with composition and separation structures, and covers both finite-dimensional function approximation and infinite-dimensional operator approximation. We prove well-posedness and universal approximation properties for the corresponding neural flows, including, to the best of our knowledge, the first universal approximation result for flow-based models between infinite-dimensional spaces. We also obtain universal approximation results for convolutional neural flow models. Through suitable time discretizations, the composition structure recovers ResNet-type architectures, while the separation structure, via a splitting-based discretization, yields plain architectures. This gives a unified flow-based route to both residual and plain architectures for neural networks and neural operators with fully connected or convolutional linear layers.

---


### 267. [Regret-Based $(ε,δ)$-optimal Stopping Criteria for Bayesian Optimization](https://arxiv.org/abs/2605.22561)

**<font color=#1a73e8>作者：</font>** Haowei Wang, Jingyi Wang, Qiyu Wei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian optimization (BO) is a widely used iterative black-box optimization method that utilizes Gaussian process (GP) surrogate models. In practice, BO is typically terminated after a fixed evaluation budget is exhausted, which can incur unnecessary cost and provides no optimality guarantee on solution quality. Recent research in developing a practical stopping criterion has made empirical progress, yet a theoretically sound stopping criterion remains a work in progress. In this work, we present provably tighter instantaneous regret bounds for GP upper confidence bound (GP-UCB) at any given iteration. Then, we propose stopping criteria for GP-UCB based on this tighter bound that ensures an $\epsilon$-optimal solution with high probability $1-\delta$ upon termination. Numerical experiments are performed to validate and demonstrate the effectiveness and efficiency of our stopping criteria.

---


### 268. [Cell Phantom Video Generation in Elliptical Fourier Descriptor Domain](https://arxiv.org/abs/2605.22563)

**<font color=#1a73e8>作者：</font>** Francesco Benedetto, Roberto Basla, Luca Magri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training Deep Neural Networks for tracking individual cells in biomedical videos requires a large amount of annotated data. The annotation of videos for cell tracking is very time consuming and often requires domain expertise; this explains the limited availability of public annotated data to address important medical problems like tissue repair or cancer treatment. Generating synthetic videos along with their Ground Truth annotations is a promising solution that relies, as a foundational first step, on the synthesis of single cell annotations (or phantoms). Phantoms need to be time consistent, as they have to replicate biological processes that are specific to the cell types. In this work, we propose a novel framework for generating videos of cell phantoms in the Elliptical Fourier Descriptors (EFDs) domain, a compact and geometrically interpretable representation for 2D closed contours. We represent the cell phantom evolution as a multivariate time series of EFD coefficients, introducing a strong prior for cell morphology and enabling the efficient generation of sequences that evolve coherently in time. Our experimental validation proves that modelling the temporal evolution in EFD space enables the generation of biologically plausible phantom videos. Our method can be used in generative pipelines for synthesizing annotated data for cell tracking, thus strongly mitigating the annotation effort for creating new datasets. Our code is available for download here: this https URL.

---


### 269. [SynAE: A Framework for Measuring the Quality of Synthetic Data for Tool-Calling Agent Evaluations](https://arxiv.org/abs/2605.22564)

**<font color=#1a73e8>作者：</font>** Shuaiqi Wang, Aadyaa Maddi, Zinan Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Today, tool-calling agents are commonly evaluated or tested on static datasets of execution traces, including input commands, agent responses, and associated tool calls. However, internal production datasets are often insufficient or unusable for testing; for example, they may contain sensitive or proprietary data, or they may be too sparse to support comprehensive testing (especially pre-deployment). In these settings, practitioners are increasingly replacing or augmenting real datasets with synthetic ones for evaluation purposes. A key challenge is quantifying the relation between these synthetic datasets and the real data. We introduce SynAE, an evaluation framework for assessing how well synthetic benchmarks for multi-turn, tool-calling agents replicate and augment the characteristics of real data trajectories. SynAE assesses the validity, fidelity, and diversity of synthetic data across four metric categories: (i) task instructions and intermediate responses, (ii) tool calls, (iii) final outputs, and (iv) downstream evaluation. We evaluate SynAE using recent agent benchmarks and test common synthetic data failure modes via realistic and controlled generation schemes. SynAE detects fine-grained variations in data validity, fidelity and diversity, and shows that no single metric is sufficient to fully characterize synthetic data quality, motivating a multi-axis evaluation of synthetic data for agent testing. A demo of SynAE is available at this https URL, with code at this https URL.

---


### 270. [Measuring Security Without Fooling Ourselves: Why Benchmarking Agents Is Hard](https://arxiv.org/abs/2605.22568)

**<font color=#1a73e8>作者：</font>** Sahar Abdelnabi, Chris Hicks, Konrad Rieck 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The benchmarks used to evaluate AI agents in security-critical roles suffer from crucial weaknesses. Building on recent empirical evidence, we characterize three core challenges that undermine security evaluations: benchmark vulnerabilities, temporal staleness, and runtime uncertainty. We then outline practical directions toward building more robust and trustworthy evaluation frameworks.

---


### 271. [A Formal Basis for Quantum Cryptographic Exposure Measurement under HNDL Threat](https://arxiv.org/abs/2605.22569)

**<font color=#1a73e8>作者：</font>** Matheus Rufino, Rafael Duarte Marcelino, Julio Smanioto Garcia  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> An adversary copies your encrypted traffic today and waits for a quantum computer to decrypt it later. How exposed are you?
We show that the functional form of the answer is not merely a calibration choice -- it is structurally justified by three assumptions about adversarial production and value-decay dynamics. Under those assumptions, the HNDL compromise probability factorises into a temporal hazard, a multiplicative cryptographic-vulnerability and operational-exposure term, and a saturation denominator governed by the defense-attack intensity ratio; the marginal sensitivity to each dimension is endogenous to the organisation's position in the vulnerability-exposure plane, not a fixed global constant. Additive scoring frameworks cannot reproduce this structure because the interaction between cryptographic vulnerability and operational exposure is absent by construction, regardless of calibration. The resulting framework provides a structurally grounded basis for operational HNDL exposure prioritisation under partial observability.

---


### 272. [SegGuidedNet: Sub-Region-Aware Attention Supervision for Interpretable Brain Tumor Segmentation](https://arxiv.org/abs/2605.22572)

**<font color=#1a73e8>作者：</font>** Hasaan Maqsood, Saif Ur Rehman Khan, Sebastian Vollmer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate segmentation of brain tumour sub-regions from multi-parametric MRI is critical for treatment planning yet remains challenging due to morphological variability, class imbalance, and overlapping appearances of tumour regions across imaging sequences. We propose SegGuidedNet, a three-dimensional residual encoder--decoder network introducing a novel SegAttentionGate module that explicitly supervises the decoder to produce spatially discriminative attention maps for each tumour sub-region necrotic core, peritumoral oedema, and enhancing tumour via a lightweight auxiliary loss, adding less than 0.2% parameter overhead. This sub-region supervision maintains decoder discriminability between visually ambiguous classes while providing free-of-cost spatial interpretability at inference without any post-hoc explanation method. Evaluated independently on BraTS2021 and BraTS2023 GLI across 251 held-out subjects each, SegGuidedNet achieves mean Dice of 0.905 (ET= 0.873, TC=0.906, WT=0.935) and 0.897 (ET=0.859, TC=0.902, WT=0.931) respectively, surpassing ensemble-based nnU-Net and HNF-Netv2 as a single model and approaching Swin UNETR a 10-model ensemble within 2--4 Dice points at a fraction of the inference cost. The consistency of results across two benchmark editions further confirms the generalisability of the proposed approach, offering competitive accuracy with built-in interpretability in a lightweight, clinically practical framework.

---


### 273. [Beyond Chamfer Distance: Granular Order-aware Evaluation Metric For Online Mapping](https://arxiv.org/abs/2605.22578)

**<font color=#1a73e8>作者：</font>** Chouaib Bencheikh Lehocine, Adam Lilja, Junsheng Fu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online map estimation is a crucial component of autonomous driving systems that reduces the reliance on costly high-definition maps. State-of-the-art (SOTA) methods commonly predict map elements as ordered sequences of points that form polylines and polygons. The evaluation of these methods relies predominantly on mean average precision (mAP) based on thresholded Chamfer distance (CD). This framework lacks sensitivity to point ordering and provides limited granularity in assessing geometric quality, making it difficult to distinguish which methods truly excel over others. In this work, we address these limitations on two fronts. For the single-instance similarity measure, we introduce sequence optimal sub-pattern assignment (SOSPA), an order-aware metric that enables fine-grained evaluation of individual geometries while satisfying all metric axioms. For the multi-instance evaluation framework, we propose polyline localisation and detection (PLD), a soft metric that jointly captures detection quality and geometric accuracy, replacing the hard thresholding of mAP with a principled soft assignment. Through evaluations on nuScenes, we demonstrate that PLD effectively ranks SOTA online mapping methods (MapTRv2, StreamMapNet, MapTracker) while providing a decomposed error analysis. This analysis identifies detection capability as the dominant bottleneck in current methods, revealing a performance trend that mAP fails to capture. Code for evaluation using our metrics will be released.

---


### 274. [SceneAligner: 3D-Grounded Floorplan Localization in the Wild](https://arxiv.org/abs/2605.22581)

**<font color=#1a73e8>作者：</font>** Junhyeong Cho, Ruojin Cai, Hadar Averbuch-Elor  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many public buildings provide floorplans with a "you are here" indicator to help visitors orient themselves. Floorplan localization seeks to computationally replicate this capability by determining where visual observations were captured within a floorplan. However, existing methods typically assume controlled small-scale environments and precise vectorized floorplans, limiting their ability to operate in large-scale buildings and rasterized floorplans. In this work, we present an approach for performing floorplan localization in the wild by grounding the task in a reconstructed 3D representation of the scene. Given an unconstrained image collection, our method reconstructs a gravity-aligned 3D scene and projects it into a 2D density map that serves as a floorplan proxy. Floorplan localization is then formulated as aligning this proxy with the input floorplan via a 2D similarity transform. To bridge the appearance gap between density maps and architectural floorplans, we adapt a 2D foundation model to learn cross-modal correspondences, introducing a fine-tuning scheme that encourages semantically aligned matches while preserving structural consistency. Extensive experiments demonstrate substantial improvements over prior methods, including in extremely sparse settings with as little as a single input image. Our code and data will be publicly available.

---


### 275. [A Tutorial on Diffusion Theory: From Differential Equations to Diffusion Models](https://arxiv.org/abs/2605.22586)

**<font color=#1a73e8>作者：</font>** Jiayi Fu, Yuxia Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This tutorial develops diffusion models from the viewpoint of differential equations. We begin with the conditional Gaussian forward process and show that this path admits both an ordinary differential equation (ODE) representation and a stochastic differential equation (SDE) representation. Averaging the conditional process over the data distribution then yields marginalized forward ODE and SDE formulations that transport the data distribution $p_0=p_{\mathrm{data}}$ to a Gaussian prior $p_1=\mathcal{N}(0,I)$. We next derive the corresponding reverse-time dynamics, namely the reverse SDE and the reverse probability-flow ODE, both of which are governed by the marginal score $\grad\log p_t(x)$. This leads to a training objective for score estimation and shows that the standard noise-prediction objective is equivalent to score matching up to an additive constant independent of the model parameters. We then discuss sampling methods for the learned reverse dynamics, including DPM-Solver, as well as guided sampling through classifier guidance and classifier-free guidance. Finally, we compare DDPM and DDIM with the reverse SDE/ODE framework and show that they share the same training objective, while DDPM sampling corresponds to discrete reverse-SDE sampling and DDIM sampling corresponds to reverse-ODE sampling.

---


### 276. [Building an Open Source Operational Technology Pentesting Platform: Lessons from LINICS](https://arxiv.org/abs/2605.22590)

**<font color=#1a73e8>作者：</font>** Awais Rashid, Joseph Gardiner, Louise Evans  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Information Technology (IT) security professionals have ready access to open-source platforms such as Kali Linux. But no such platform exists for Operational Technology (OT) that underpins Industrial Control Systems. We discuss experiences of architecting, building and releasing LINICS, an open-source platform for OT pentesting and security analysis.

---


### 277. [Do Deep Ensembles Actually Capture Uncertainty in Graph Neural Networks?](https://arxiv.org/abs/2605.22593)

**<font color=#1a73e8>作者：</font>** Pedro C. Vieira, Pedro Ribeiro, Viacheslav Borovitskiy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While deep ensembles are widely considered to be the default method for uncertainty quantification in deep learning, their effectiveness for graph-structured data is often simply assumed based on successes in domains like computer vision. We investigate standard deep ensembles specifically for message-passing graph neural networks. Benchmarking across seven datasets representing varied tasks and complexities, we reveal that ensembles provide surprisingly little improvement over a single model. Instead, the observed marginal gains stem primarily from stabilizing optimization noise in point predictions rather than yielding meaningfully better uncertainty estimates. Through an aleatoric-epistemic decomposition, we identify epistemic collapse: independently trained networks consistently converge to overly similar predictions. Because disagreement is the fundamental mechanism through which ensembles capture epistemic uncertainty, this lack of diversity neutralizes their key advantage. Analyzing this phenomenon further, we suggest this collapse is driven by functional rather than weight-space convexity, where distinct parameter solutions induce almost identical behavior. Our results suggest that deep ensemble success does not seamlessly transfer to graph machine learning.

---


### 278. [Factored Diffusion Policies:Compositionally Generalized Robot Control with a Single Score Network](https://arxiv.org/abs/2605.22596)

**<font color=#1a73e8>作者：</font>** Sayan Mitra, Ege Yuceel, Noah Giles 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Robotic tasks are typically specified by a tuple of factors, such as the object to be grasped, the obstacles to be avoided, the color of the target, and so on. Collecting expert demonstrations for every combination of factor values grows combinatorially. We present factored diffusion policies: a single shared diffusion network trained with per-factor null-token dropout, whose score decomposes additively across factors at inference. Under approximate conditional independence between factors given the action-observation pair, this composition approximates the true joint score with a bounded uniform error, reducing the training-task budget from a product of factor cardinalities to a sum. A trajectory-tube certificate chains this score-level bound through the reverse-time sampling ODE and a contracting tracking controller into a closed-loop state-trajectory tube whose radius factors into an ODE-sensitivity constant and a per-factor score-error budget. Unlike compositional-diffusion methods for control that combine separately trained networks, we use one shared network. Drone racing experiments confirm both the generalization bound and the certificate. On state-based multi-gate racing, the factored policy passes 90% of held-out gates -- matching an oracle -- while a K-network composition baseline collapses to 3%; on vision-based single-gate traversal, it transfers zero-shot to an unseen venue with +11.7pp success-rate gain and 2.4X crash-rate reduction.

---


### 279. [MoSA: Motion-constrained Stress Adaptation for Mitigating Real-to-Sim Gap in Continuum Dynamics via Learning Residual Anisotropy](https://arxiv.org/abs/2605.22597)

**<font color=#1a73e8>作者：</font>** Jiaxu Wang, Junhao He, Jingkai Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning real-world dynamics from visual observations is crucial for various domains. A common strategy is to calibrate simulators by estimating physical parameters, yet accuracy is ultimately bounded by the underlying physical models, which often assume materials are homogeneous and isotropic. Even if reasonable, real-world objects typically exhibit mild anisotropy and heterogeneity. After the near-isotropic backbone is well calibrated, these residual effects become the key bottleneck for further closing the real-to-sim gap. Although neural networks can fit dynamics end-to-end, such black-box modeling discards strong physical priors, leading to poor data efficiency and overfitting. Therefore, we propose MoSA, a motion-constrained stress adaptation framework that targets these residual effects to further improve real-to-sim dynamics learning. MoSA uses an isotropic model as a physics prior and learns residual stress operators to capture mild anisotropy and heterogeneity. It progressively adapts stresses via microplane-constrained redistribution in a physics-informed cascaded network. We further impose motion constraints by supervising temporal and spatial derivatives of the deformation field. Experimentally, our learned dynamics achieves superior accuracy, generalization, and robustness, while learning physically meaningful residual anisotropy. Finally, we validate MoSA in a robot manipulation setting, showing that better real-to-sim dynamics modeling translates into more reliable sim-to-real transfer. Project Page is available at this https URL.

---


### 280. [Innovations in Cardless Artificial Intelligence Banking: A Comprehensive Framework for Cyber Secure and Fraud Mitigation using Machine Learning Algorithms](https://arxiv.org/abs/2605.22604)

**<font color=#1a73e8>作者：</font>** Md Israfeel  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The advent of cardless artificial intelligence (AI) banking heralds a paradigm shift in the financial landscape, offering users unprecedented security and convenience. This paper outlines a comprehensive framework designed to enhance cybersecurity, introduce auto-generated virtual cards, and mitigate fraud risks within cardless AI banking systems. The framework envisions a future banking architecture that employs AI-powered data cryptography to create secure virtual cards for seamless transactions. By emphasizing secure communication channels, it ensures the integrity of financial activities among banking systems, cardholders, and third-party vendors. AI-based authorization methodologies play a pivotal role in authenticating each transaction while proactively identifying potential fraud, demonstrating the framework's efficacy in fortifying cardless AI banking security. The initial approach, featuring an AI-driven, feature-based banking system, ensures the generation of virtual cards with encrypted data, minimizing information exposure and reducing fraud risks. Integrating a machine learning algorithm adds an additional layer of protection against potential fraudulent activities. In conclusion, the proposed framework establishes a holistic cybersecurity and fraud-mitigation paradigm for cardless AI banking systems. Its implementation empowers financial institutions to address security concerns associated with traditional banking, paving the way for a future banking landscape that is not only fraud-resistant but also secure and convenient for users.

---


### 281. [Benchmarking Machine Learning Architectures for Antimicrobial Stewardship in Pediatric ICUs](https://arxiv.org/abs/2605.22611)

**<font color=#1a73e8>作者：</font>** Niklas Raehse, Luregn J. Schlapbach, Daphné Chopard  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Antimicrobial stewardship (AMS) is critical in pediatric intensive care units (PICUs), where diagnostic uncertainty often drives broad-spectrum antibiotic use, increasing antimicrobial resistance and potential long-term harms. Machine learning offers a promising approach for identifying patient-level opportunities for stewardship interventions from electronic health record data, yet prior work has focused largely on adult populations and static tabular representations. We present a systematic benchmarking study of AMS intervention prediction in the PICU across a public dataset and a private institutional cohort. We define four clinically relevant proxy targets for reducing antibiotic exposure: intravenous-to-oral switching, de-escalation, discontinuation, and short-course therapy. Under a unified evaluation framework, we compare tabular, sequence-based, and graph-based temporal models at multiple temporal resolutions. We find that predictive performance is driven primarily by target prevalence and dataset characteristics rather than model complexity. Sequence models improve the precision-recall trade-off over tabular approaches at coarse (24-hour) resolution, while finer temporal modeling provides limited additional benefit. However, these gains come at the cost of poorer calibration, with simpler tabular models yielding more reliable probability estimates. Multi-task learning produces only marginal improvements, suggesting limited shared structure across stewardship targets. Our findings highlight the importance of target design, temporal representation, and calibration in clinical machine learning, and provide practical guidance for developing reliable decision support systems for pediatric AMS.

---


### 282. [Chinese sensorimotor and embodiment norms for 3,000 lexicalized concepts](https://arxiv.org/abs/2605.22616)

**<font color=#1a73e8>作者：</font>** Jing Chen, Gábor Parti, Yin Zhong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding how conceptual knowledge is grounded in bodily experience, and to what extent machine systems can acquire such knowledge without direct sensorimotor experience, are central questions in both cognitive science and embodied artificial intelligence research. Large-scale normative resources are essential for investigating these questions empirically, yet such resources remain sparse for non-Indo-European languages. We present a novel normative database for 3,000 lexicalized concepts in Mandarin Chinese, comprising 11-dimensional sensorimotor ratings and unidimensional embodiment ratings collected from 378 native Mandarin speakers. The ratings demonstrate high reliability and strong cross-norm validity with existing Chinese resources, each of which covers fewer words and a subset of the 11 sensorimotor dimensions. In a validation study, we tested new variables derived from a theoretically motivated metric, Perceptual Strength of Embodiment (PSE) (Huang et al., 2025), together with seven common composite variables, on lexical decision tasks. The results suggest that PSE-Sensorimotor and Minkowski-3 are the strongest composite predictors of lexical decision performance, capturing the facilitatory effects of sensorimotor information on lexical processing. A further exploratory study showed that sensorimotor ratings are substantially recoverable from purely linguistic representations using simple regression models (mean Spearman r = .62 across dimensions), though recovery varied markedly: visual and auditory dimensions yielded higher correspondence than chemosensory ones. Representational similarity analysis further showed that the relational geometry of the sensorimotor space is also partially recoverable (r = .540), consistent with the view that distributional language use encodes aspects of embodied conceptual structure.

---


### 283. [GLeVE: Graph-Guided Lesion Grounding with Proposal Verification in 3D CT](https://arxiv.org/abs/2605.22619)

**<font color=#1a73e8>作者：</font>** Shuo Jiang, Yuhao Hong, Chunbo Jiang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Grounding radiology report descriptions to 3D CT volumes is essential for verifiable clinical interpretation, yet remains challenging due to the semantic-spatial gap between free-text narratives and volumetric anatomy. Existing report-assisted and vision-language grounding methods typically rely on phrase-level alignment or dense pixel supervision, resulting in limited lesion-wise correspondence and suboptimal localization accuracy. We propose GLeVE, a graph-guided lesion grounding framework with anatomical prior verification and octree-based autoregressive refinement. GLeVE treats each lesion description as an atomic semantic unit and encodes organ attribution, attributes, and inter-lesion relations through relation-aware graph reasoning to produce discriminative lesion-wise queries. Anatomy-aware proposal generation with region-level verification enforces one-to-one text-lesion alignment, while hierarchical octree refinement progressively improves boundary delineation. Experiments on AbdomenAtlas 3.0 demonstrate consistent gains over classical multimodal foundation models and report-supervised baselines in both segmentation accuracy and lesion-level localization.

---


### 284. [Two is better than one: A Collapse-free Multi-Reward RLIF Training Framework](https://arxiv.org/abs/2605.22620)

**<font color=#1a73e8>作者：</font>** Shourov Joarder, Diganta Sikdar, Ahsan Habib Akash 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has substantially improved the reasoning ability of LLMs, but often depends on external supervision from human annotations or gold-standard solutions. Reinforcement learning from internal feedback (RLIF) has recently emerged as a scalable unsupervised alternative, using signals extracted from the model itself. However, existing RLIF methods typically rely on a single internal reward, which can lead to reward hacking, entropy collapse, and degraded reasoning structure. We propose a multi-reward RLIF framework that decomposes the training signal into two complementary components: an answer-level reward based on cluster voting and a completion-level reward based on token-wise self-certainty. To combine these signals robustly, we apply GDPO-based normalization to reduce reward-scale imbalance. We further introduce KL-Cov regularization, which targets low-entropy token distributions responsible for disproportionate entropy reduction, preserving exploration and preventing late-stage collapse. Across mathematical reasoning and code-generation benchmarks, our method improves stability and robustness over prior unsupervised RL approaches, while achieving performance close to supervised RLVR methods. These results show that complementary internal rewards, combined with targeted regularization, can support stable long-horizon reasoning without relying on external ground-truth supervision. Code will be released soon.

---


### 285. [UNAD+: An Explainable Hybrid Framework for Unknown Network Attack Detection](https://arxiv.org/abs/2605.22621)

**<font color=#1a73e8>作者：</font>** Saif Alzubi, Frederic Stahl  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The detection of previously unseen network attacks remains a major challenge for intrusion detection systems. Although supervised learning methods often perform well on known attack classes, they are limited when new attack types are not represented in the training data. Unsupervised methods are more suitable for detecting zero-day attacks, as they do not require labelled attack samples, but they often suffer from high false positive rates, which limits their real-world usefulness. This paper presents UNAD+, an enhanced framework for unknown network attack detection derived from the previously proposed Unknown Network Attack Detector (UNAD). UNAD+ combines a benign-only unsupervised ensemble with Weighted Majority Voting (WMV), a supervised refinement stage trained on pseudo-labelled detections, and a post hoc explainability layer that provides both local and global explanations. The framework was evaluated on the CICIDS2017 and NSL-KDD benchmark datasets. The results show that UNAD+ improves on the original UNAD framework, achieving F1-scores above 98% across the benchmark datasets while significantly reducing false positives and enhancing transparency and deployment suitability through integrated explainability.

---


### 286. [A note on convergence of Wasserstein policy optimization](https://arxiv.org/abs/2605.22622)

**<font color=#1a73e8>作者：</font>** David Šiška, Yufei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wasserstein Policy Optimization (WPO) is a recently proposed reinforcement learning algorithm that leverages Wasserstein gradient flows to optimize stochastic policies in continuous action spaces. Despite its empirical success, the theoretical convergence properties of WPO in environments with continuous state and action spaces have yet to be fully established. In this note, we argue that WPO within the framework of entropy-regularised Markov Decision Processes converges linearly. This is done by leveraging recent advances in mean-field analysis for convergence of gradient flows using log-Sobole inequalities. Assuming existence of sufficiently regular solution to the gradient flow equation we demonstrate monotonic energy dissipation along the flow and establish a local log-Sobolev inequality. Ultimately, these properties allow us to argue that the value function should converge linearly to the global optimum.

---


### 287. [Summarizing Time-Varying Digital Image Correlation Strain Fields Using Sankey Diagrams](https://arxiv.org/abs/2605.22627)

**<font color=#1a73e8>作者：</font>** Victor Persson, Christofer Boo, Mohit Sharma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Digital Image Correlation (DIC) enables dense, time-resolved measurement of surface strain in deforming materials, providing insight into strain localization and failure mechanisms. However, the resulting strain fields are typically explored frame-by-frame through spatial visualizations, making global temporal patterns difficult to discern. We present a visual summarization approach that represents the evolution of high-strain regions as a single Sankey diagram constructed from superlevel sets of the von Mises equivalent strain field. By tracking connected components over time via spatial overlap, the diagram encodes the birth, persistence, merging, and disappearance of strain concentrations. Applied to four tensile test datasets with varying notch geometries, the approach compactly captures differences in deformation regimes and qualitative precursors to failure, complementing traditional spatial strain visualizations with a global temporal overview.

---


### 288. [H-Flow: Self-supervised Human Scene Flow via Physics-inspired Joint Multi-modal Learning](https://arxiv.org/abs/2605.22629)

**<font color=#1a73e8>作者：</font>** Zhanbo Huang, Xiaoming Liu, Yu Kong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Parametric human models capture global pose but cannot represent the non-rigid surface dynamics of clothing and soft tissue. Generic scene flow estimates dense motion but breaks down on articulated bodies, where pixel-level supervision is also intractable to acquire. We introduce H-Flow, a dense human scene flow that captures both skeletal kinematics and surface deformation. A unified multi-head transformer estimates flow from monocular video, jointly predicting pose and depth as companion outputs. The challenge lies in the lack of supervision. In place of unattainable labels, we anchor the network in the physics of human motion, encoding geometric, structural, and biomechanical priors as cross-modal training objectives. We further introduce DynAct4D, a high-fidelity synthetic benchmark providing dense flow annotations across diverse subjects, garments, and motions. On standard benchmarks, H-Flow outperforms scene-flow and parametric baselines, and generalizes zero-shot to in-the-wild video. Code, models, and the DynAct4D benchmark will be released upon publication

---


### 289. [AtomicMotion: Learning Human Motion From Different Human Parts](https://arxiv.org/abs/2605.22631)

**<font color=#1a73e8>作者：</font>** Runzhen Liu, Chuhua Xian, Fa-Ting Hong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurately reconstructing full-body poses from sparse head and hand trajectories is a foundational challenge for immersive AR/VR telepresence. Current methods often struggle with error accumulation and unnatural joint coordination, primarily because they treat the human body as a monolithic entity, thereby failing to capture the fine-grained ``atomic intents'' embedded in subtle signal variations and overlooking the inherent structural topology. To bridge this gap, we present AtomicMotion, a framework designed to decouple and re-integrate body dynamics through three core innovations. First, we introduce a logical body partitioning scheme that decomposes the skeleton into five distinct clusters based on functional intent; this ensures that each partition preserves internal joint synergies while isolating local motion primitives. Second, to robustly map sparse inputs to high-dimensional poses, we employ a masked full-body pre-conditioning strategy during training, forcing the model to internalize global skeletal topology and latent kinematic constraints. Finally, addressing the limitations of vanilla spatial attention, which often ignores fixed physiological connectivity, we propose Kinematic Attention. By embedding the classical kinematic tree structure into the attention mechanism, we ensure biological plausibility in the synthesized motions. Extensive evaluations on the AMASS dataset demonstrate that AtomicMotion significantly outperforms existing baselines, yielding higher reconstruction fidelity and superior biomechanical realism.

---


### 290. [The Double Dilemma in Multi-Task Radiology Report Generation: A Gradient Dynamics Analysis and Solution](https://arxiv.org/abs/2605.22635)

**<font color=#1a73e8>作者：</font>** Erjian Zhang, Yatong Hao, Liejun Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While multi-task learning based automatic radiology report generation (RRG) is widely adopted to ensure clinical consistency, most focus on architectural designs yet remain limited to coarse linear scalarization strategies. These strategies cannot effectively balance the hard constraints of discriminative clinical supervision with the smoothness requirements of report generation. To address these problems, we analyze the failure mechanism of linear scalarization from the perspective of gradient dynamics, utilizing the stochastic differential equation (SDE) framework to characterize it as a "Double Dilemma" of drift term deviation and diffusion term decay. Based on this, we propose a backbone-agnostic optimizer named Conflict-Averse Magnitude-Enhanced Gradient Descent (CAME-Grad). Through conflict-averse direction rectification and magnitude-enhanced energy injection, the algorithm not only ensures geometric validity, but also avoids local optimal solutions. Then, the adaptive gradient fusion mechanism is used to establish a dynamic balance between the theoretical optimal direction and the task-specific inductive bias. Experiments show that as a universal plug-and-play optimizer, CAME-Grad brings substantial and consistent improvements across eight diverse RRG methods, elevating overall clinical efficacy performance by an average of 2.3\% on MIMIC-CXR and 1.9\% on IU X-Ray. Our code is available at this https URL.

---


### 291. [More Context, Larger Models, or Moral Knowledge? A Systematic Study of Schwartz Value Detection in Political Texts](https://arxiv.org/abs/2605.22641)

**<font color=#1a73e8>作者：</font>** Víctor Yeste, Paolo Rosso  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Detecting Schwartz values in political text is difficult because implicit cues often depend on surrounding arguments and fine-grained distinctions between neighboring values. We study when context and explicit moral knowledge help sentence-level value detection. Using the ValuesML/Touch{é} ValueEval format, we compare sentence, window, and full-document inputs; no-RAG and retrieval-augmented settings with a curated moral knowledge base; supervised DeBERTa-v3-base/large encoders; and zero-shot LLMs from 12B to 123B parameters. The results show that more context is not uniformly better: full-document context improves supervised DeBERTa encoders by 3.8--4.8 macro-F1 points over sentence-only input, but does not consistently help zero-shot LLMs. Retrieved moral knowledge is more consistently useful in matched comparisons, improving each tested model family and context condition under early fusion. However, scaling from DeBERTa-v3-base to large and from 12B to larger LLMs does not guarantee gains, and simple early fusion outperforms the tested late-fusion and cross-attention RAG variants for encoders. Per-value analyses show that context and retrieval help most for socially situated or conceptually confusable values. These findings suggest that value-sensitive NLP should evaluate context, knowledge, and model family jointly rather than treating longer inputs or larger models as universal improvements.

---


### 292. [Why SGD is not Brownian Motion: A New Perspective on Stochastic Dynamics](https://arxiv.org/abs/2605.22644)

**<font color=#1a73e8>作者：</font>** Igor Ignashin, Anna Radovskaya, Andrew Semenov 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stochastic Gradient Descent (SGD) is commonly modeled as a Langevin process, assuming that minibatch noise acts as Brownian motion. However, this approximation relies on a continuous-time limit and a sqrt(eta) noise scaling that does not match the discrete SGD update at finite learning rate. In this work, we propose an alternative formulation of SGD as deterministic dynamics in a fluctuating loss landscape induced by minibatch sampling. Starting directly from the discrete update, we derive a master equation for the parameter distribution and obtain a discrete Fokker--Planck equation that differs from the standard Langevin form at order eta^2. Using this framework, we analyze SGD dynamics near critical points of the loss. We show that the behavior decomposes along the eigenbasis of the mean Hessian into qualitatively distinct regimes. In particular, nearly-flat directions do not admit a stationary distribution: the variance grows over time, corresponding to effective diffusion along valleys with a coefficient proportional to the learning rate. We provide empirical evidence supporting these predictions on neural network models in computer vision and natural language processing, observing a clear qualitative separation between confined and diffusive modes.

---


### 293. [From Baseline to Follow-Up: Counterfactual Spine DXA Image Synthesis in UK Biobank Using a Causal Hierarchical Variational Autoencoder](https://arxiv.org/abs/2605.22649)

**<font color=#1a73e8>作者：</font>** Yilin Zhang, Nicholas C. Harvey, Nicholas R. Fuggle 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dual-energy X-ray absorptiometry (DXA) is widely used for large-scale skeletal assessment, yet learning controllable and interpretable factor-specific anatomical variation remains challenging. We propose a metadata-conditioned causal hierarchical variational autoencoder (CHVAE) for causally consistent generation of anteroposterior (AP) spine DXA images from the UK Biobank (UKB). The model is trained on 3,743 raw AP spine scans from the first imaging visit and conditioned on basic participant attributes and lumbar morphometry. Causal consistency is evaluated in a baseline-to-follow-up setting using abduction--action--prediction (AAP): latent variables are abducted from baseline images, age is intervened to the repeat-imaging value, and the resulting counterfactual follow-up morphometry is compared with observed repeat-imaging measurements. Results show strong absolute-level agreement for key vertebral morphometry variables under age intervention, supporting intervention-aligned synthesis of anatomically plausible DXA images.

---


### 294. [Whose Voice Counts? Mapping Stakeholder Perspectives on AI Through Public Submissions to the U.S. Government](https://arxiv.org/abs/2605.22650)

**<font color=#1a73e8>作者：</font>** Alina Karakanta, Alex Christiansen, Tomás Dodds 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As artificial intelligence (AI) systems become more common in our daily lives, it is important to understand how different stakeholders comprehend and envisage the role that these technologies play in shaping social, political, and economic realities. In this paper, we investigate public perceptions of AI based on a corpus of letters submitted during the public consultation for the Trump Administration's US AI Action Plan. To this aim, we release a corpus cleaning pipeline and perform topic modelling and frequency analysis to explore predominant topics discussed by different subgroups (e.g., academia, individuals, private sector) and those appearing in the AI Action Plan. Our results show that individuals voice strong concerns related to the impact of AI on life, while other stakeholders are more concerned with AI development. Our comparison of topics suggests that the AI Action Plan reflects predominantly the concerns of the private sector on security, policies, and development, with individuals' concerns less represented.

---


### 295. [What Does the Caption Really Say? Counterfactual Phrase Intervention for Compositional Data Selection in Vision-Language Pretraining](https://arxiv.org/abs/2605.22651)

**<font color=#1a73e8>作者：</font>** Hyejin Go, Semi Lee, Hyesong Choi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> CLIP-style contrastive pretraining typically curates web-scale image-text pairs using sample-level filtering signals, often based on pair-level alignment. We show that this signal saturates: once coarse mismatches are removed, stricter global filtering no longer tracks the compositional supervision provided by the retained captions. The reason is structural - a global score conflates whether a pair is broadly plausible with whether the individual object, attribute, and relation phrases inside the caption materially support the image-text match. The latter is what compositional generalization demands, yet pair-level filters are blind to it. We address this with Counterfactual Phrase Intervention (CPI), a phrase-level curation framework that converts controlled nonce-token substitutions into image-conditioned phrase-sensitivity scores. CPI uses global alignment only for coarse mismatch removal, then ranks the surviving pool by whether caption phrases measurably affect the image-text score under controlled substitution. We frame CPI as a first-order phrase-sensitivity signal rather than a grounding or identification result, and evaluate it at CC3M scale. Ranking by this signal yields a 50%-data subset that improves VL-CheckList-VG Relation by +1.91 over the full-data baseline and +1.00 over alignment-only filtering at matched budget, while improving SugarCrepe overall and preserving general transfer. CPI is loss-orthogonal: applied unchanged to NegCLIP, it further improves VL-CheckList-VG Relation by +3.84, with additional CE-CLIP gains in the main text.

---


### 296. [Student programming behavior with and without phone notification suppression](https://arxiv.org/abs/2605.22657)

**<font color=#1a73e8>作者：</font>** Gavin Eddington, Christopher Warren, Seth Poulsen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Background and Context. Computer programming often involves extended periods of sustained activity and mobile phone notifications introduce frequent opportunities for interruption. Prior work demonstrates that suppressing phone notifications may reduce these disruptions.
Objectives. Our primary research question is: How does suppressing phone notifications affect students' task engagement and productivity while programming?
Method. We report on a replication and methodological extension study conducted in a CS1 course involving 22 students. Using a within-subject design, selected programming assignments were randomly designated for enabling notification suppression. Phone state logs were synchronized with millisecond-resolution IDE keystroke data to measure student attention and focus when in the control and notification-suppression conditions.
Findings. Assignments completed with notification suppression enabled significantly lower break rates and longer intervals of focus compared to assignments completed in the control condition for many, but not all, students. This study provides evidence that notification suppression is associated with measurable differences in programming engagement and behavior. We also find a remarkable bimodality in the effect across students -- many students are positively affected, a small number are negatively affected, and very few experience little or no effect. This finding is consistent with other studies in diverse disciplines.
Implications. Our results show that, for many students, phone notification suppression tools, such as Do Not Disturb, can improve attention and focus. Implications apply to educational settings (do-not-disturb as an intervention) and scholarship (understanding the effects of phone distraction).

---


### 297. [A Generalized Nash Equilibrium-Seeking Scheme for Trauma Resuscitation](https://arxiv.org/abs/2605.22661)

**<font color=#1a73e8>作者：</font>** Promise Ekpo, Angelique Taylor, Lekan Molu  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Trauma resuscitation is a clinical process for treating life-threatening physiological disorders in safety-critical environments, driven by the experience of healthcare workers (HCWs). Designing and optimizing quantifiable metrics that accurately capture HCW decisions may augment current resuscitation procedures with the potential to improve patient outcomes. This motivates our socio-technical formulation of trauma resuscitation as a distributed generalized Nash equilibrium (GNE)-seeking game with coupled inequality constraints. This method is optimized over a time-varying communication graph. We introduce novel insights from clinical experience to model HCWs behavior. This work facilitates the best possible resuscitation outcome given HCWs workloads, schedules, competencies, and limited resources.

---


### 298. [Claw AI Lab: An Autonomous Multi-Agent Research Team](https://arxiv.org/abs/2605.22662)

**<font color=#1a73e8>作者：</font>** Fan Wu, Cheng Chen, Zhenshan Tan 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present Claw AI Lab, a lab-native autonomous research platform that advances automated research from a hidden prompt-to-paper pipeline into an interactive AI laboratory. Rather than centering the system around a single agent or a fixed serial workflow, we allow users to instantiate a full research team from one prompt, with customizable roles, collaborative workflows, real-time monitoring, artifact inspection, and rollback/resume control through a unified dashboard. The platform also supports distinct research modes for exploration, multi-agent discussion, and reproduction, making autonomous research substantially more steerable and laboratory-like in practice. A key practical contribution of Claw AI Lab lies in its Claw-Code Harness, which connects local codebases, datasets, and checkpoints to runnable experiments and feeds execution artifacts back into the research loop. As a result, the harness improves not only execution integration, but also experimental completion and result integrity: experiments are easier to inspect, iterate on, and faithfully transfer into final papers, reducing common failure modes such as partial runs and malformed result reporting. In our internal evaluation on five AI research case studies, using AutoResearchClaw as the baseline, Claw AI Lab is consistently preferred by AI expert judges on idea novelty, experiment completeness, and paper presentation quality. We view Claw AI Lab as an early step toward a new paradigm: autonomous research as usable, interactive, and reliability-aware scientific infrastructure.

---


### 299. [SEGA: Spectral-Energy Guided Attention for Resolution Extrapolation in Diffusion Transformers](https://arxiv.org/abs/2605.22668)

**<font color=#1a73e8>作者：</font>** Javad Rajabi, Kimia Shaban, Koorosh Roohi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion transformers (DiTs) have emerged as a dominant architecture for text-to-image generation, yet their performance drops when generating at resolutions beyond their training range. Existing training-free approaches mitigate this by modifying inference-time attention behavior, often through Rotary Position Embeddings (RoPE) extrapolation combined with attention scaling. However, these strategies apply a uniform and content-agnostic scaling across RoPE components with distinct frequency characteristics, inducing a trade-off between preserving global structure and recovering fine detail. We introduce SEGA, a training-free method that dynamically scales attention across RoPE components according to the latent's spatial-frequency structure at each denoising step. This adaptive scaling improves both structural coherence and fine-detail fidelity. Experiments show that SEGA consistently improves high-resolution synthesis across multiple target resolutions, outperforming state-of-the-art training-free baselines.

---


### 300. [From Abstraction to Instantiation: Learning Behavioral Representation for Vision-Language-Action Model](https://arxiv.org/abs/2605.22671)

**<font color=#1a73e8>作者：</font>** Bing Hu, Zaijing Li, Rui Shao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models often suffer from performance degradation under distribution shifts, as they struggle to learn generalized behavior representations across varying environments. While existing approaches attempt to construct behavior representations through action-centric latent variables, they are often limited by short-horizon temporal fragmentation and static execution-alignment, leading to inconsistent behaviors in complex scenarios. To address these limitations, we propose \textbf{BehaviorVLA}, a framework that facilitates robust manipulation through the learning of a temporally coherent behavioral representations. Our approach features two symmetric components: (1) the \textbf{Visuomotor Behavior Encoder (VBE)}, which utilizes a causal Mamba-based architecture to aggregate long-horizon trajectory information into a unified behavior representation; and (2) the \textbf{Phase-conditioned Behavior Decoder (PBD)}, which decodes this representation into precise actions by dynamically aligning task-level priors with real-time execution progress. Experiments on RoboTwin 2.0, LIBERO, and CALVIN demonstrate state-of-the-art success rates of 58\%, 98\%, and 4.36 (this http URL), respectively. Notably, in real-world sim-to-real transfer, BehaviorVLA matches the performance of OpenVLA-OFT using only 50\% of the demonstration data, showcasing its superior data efficiency and generalization.

---


> [!TIP]
> 当前位于：**251-300**（第 6/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-347](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
