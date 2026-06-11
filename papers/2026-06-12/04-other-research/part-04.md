# 📦 其他研究 | 2026年06月12日

> 本类共 **248** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-248](./part-05.md)

---

### 151. [SG2Loc: Sequential Visual Localization on 3D Scene Graphs](https://arxiv.org/abs/2606.11880)

**<font color=#1a73e8>作者：</font>** Nicole Damblon, Olga Vysotska, Federico Tombari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual localization in complex indoor environments remains a critical challenge for robotics and AR applications. Sequential localization, where pose estimates are refined over time, is important for autonomous agents. However, traditional methods often require storing extensive image databases or point clouds, leading to significant overhead. This paper introduces a novel, lightweight approach to sequential visual localization using 3D scene graphs. Our method represents the environment with a compact scene graph, where nodes represent objects (with coarse meshes) and edges encode spatial relationships. For each image in the localization phase, we extract per-patch semantic features, predicting object identities. Localization is performed within a particle filter framework. Each particle, representing a camera pose, projects the coarse object meshes from the scene graph into the image, assigning object identities to patches based on visibility. The similarity of the per-patch features, in the input image, and object features from the scene graph determines the weight of a particle. Subsequent images are incorporated sequentially, refining the pose estimate. By leveraging a compact scene graph and efficient semantic matching, our method significantly reduces storage while maintaining performance on real-world datasets. The code will be available at this https URL.

---


### 152. [Image Quality Assessment of Identity Cards Using Measures from Open Face Image Quality](https://arxiv.org/abs/2606.11884)

**<font color=#1a73e8>作者：</font>** Gregor Grote, Juan E. Tapia, Christian Rathgeb  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper addresses the challenge of assessing image quality in ID cards in remote verification systems by applying capture-related quality measures from the Open Face Image Quality (OFIQ) standard to ID card images. Our preprocessing pipeline includes corner detection, perspective normalization, and comprehensive foreground masking to ensure accurate and unbiased quality measure computation. We evaluate the effectiveness of these measures by analyzing their correlation with the performance of three presentation attack detection (PAD) algorithms across four diverse ID card datasets, where two datasets contain bona fide, i.e. pristine, images and two contain printed mock ID cards. Our results suggest that quality assessment based on some OFIQ measures can significantly improve PAD performance.

---


### 153. [Wild3R: Feed-Forward 3D Gaussian Splatting from Unconstrained Sparse Photo Collection](https://arxiv.org/abs/2606.11894)

**<font color=#1a73e8>作者：</font>** Yuto Furutani, Takashi Otonari, Kaede Shiohara 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D Gaussian Splatting (3DGS) removes the need for time-consuming per-scene optimization required by traditional 3DGS. However, existing feed-forward approaches struggle with real-world photo collections that include diverse lighting conditions and transient objects. In this paper, we present Wild3R, a feed-forward approach for unconstrained sparse photo collections. The main bottleneck is the lack of training data that provides multiple viewpoints, a variety of illuminations, and transient variations necessary for learning robust scene representations. To address this, we introduce the WildCity dataset, which comprises 200 scenes, 170 lighting conditions, and transient objects, resulting in 337,500 images in total. By leveraging the dataset, our model learns appearance consistency across viewpoints conditioned on reference views, while removing transient content. Extensive experiments demonstrate that our method outperforms existing feed-forward approaches and achieves results competitive with prior per-scene optimization-based methods.

---


### 154. [PAPEL: A Collaborative System for Parental Guidance during Preschool Play-Based English Learning](https://arxiv.org/abs/2606.11896)

**<font color=#1a73e8>作者：</font>** Xutong Wang, Yu Mei, Qinwei Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Play-based parent-child interaction offers preschoolers rich opportunities for everyday foreign language learning, yet many parents struggle to turn open-ended play into effective English-as-a-Foreign-Language (EFL) learning experiences at home. To explore how AI might support this process, we conducted formative studies through interviews and a Wizard-of-Oz study. We identified four key challenges: content selection, language expression, balancing instruction and play, and problem solving. To address these challenges, we present PAPEL, a parent-AI collaborative system that grounds suggestions in the ongoing play scene and organizes support into four core modules: content generation, language adaptation, balance assessment, and extended response. In a counterbalanced within-subjects study with 16 parent-child dyads, PAPEL was associated with more integrated parent utterances that combined playful and instructional content, as well as more parent-child conversational turns, than the lightweight chatbot baseline used in our study.

---


### 155. [Notes2Skills: From Lab Notebooks to Certainty-Aware Scientific Agent Skills](https://arxiv.org/abs/2606.11897)

**<font color=#1a73e8>作者：</font>** Shi Liu, Jiayao Chen, Chengwei Qin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific discovery workflows usually contain and rely heavily on lab notes, where researchers record observations, interpret uncertain results, and plan follow-up experiments. Such informative lab notes preserve evolving scientific reasoning and author uncertainty, rather than polished final results exhibited in publications, providing a valuable opportunity for AI to engage in scientific exploration at a more comprehensive and deeper level. However, most prior work on scientific text focuses on papers, protocols, or structured databases, leaving informal laboratory notes underexplored as inputs to AI agents for science. This gap matters because lab notes often intermingle validated observations, tentative judgments, and possible experimental next steps within the same passage. If these signals are conflated, an AI agent may mistake uncertain scientific judgments for confirmed conclusions or executable actions. To this end, we present Notes2Skills, a two-stage framework for turning lab notebooks into verifiable skills for scientific AI agents while preserving the author's certainty. Across seven conditions and three wet-lab sessions, Notes2Skills is the only configuration that neither mistakes uncertain notes for firm instructions nor discards firm ones. We show that certainty preservation is the missing piece between lab notebooks and reliable agent skills, opening a path toward safer AI co-scientist systems.

---


### 156. [When Does Language Matter? Multilingual Instructions Reveal Step-wise Language Sensitivity in Vision-Language-Action Models](https://arxiv.org/abs/2606.11906)

**<font color=#1a73e8>作者：</font>** Xuan Dong, Zhe Han, Tianhao Niu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models have shown strong performance in language-conditioned robotic manipulation, yet their robustness to linguistic variation remains poorly understood. In this work, we present the first systematic multilingual evaluation of VLA models by translating the LIBERO benchmark into ten languages, revealing severe performance degradation under non-English instructions, with success rates dropping by 30-50%. Through fine-grained analysis of task executions, we find that language influence is highly non-uniform across steps: certain steps exhibit strong language dependence and dominate overall task failure, while others are largely language-agnostic. Based on this insight, we propose a step-wise inference-time intervention that aligns representations according to step language sensitivity, substantially improving performance under linguistic variation. Our results indicate that language robustness in VLA models is fundamentally a step-wise control problem, highlighting the importance of temporally structured analysis for reliable embodied agents.

---


### 157. [Embodied-BenchClaw: An Autonomous Multi-Agent System for Embodied Spatial Intelligence Benchmark Construction](https://arxiv.org/abs/2606.11909)

**<font color=#1a73e8>作者：</font>** Baoyang Jiang, Fengchun Zhang, Leyuan Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Benchmarks are essential for evaluating embodied spatial intelligence, yet their construction is labor-intensive, hard to reuse, and difficult to maintain. Existing embodied benchmarks are often static and may quickly become saturated as models improve, limiting their ability to distinguish new capabilities. We propose Embodied-BenchClaw, an autonomous agentic system for constructing embodied spatial intelligence benchmarks. Given a user-specified evaluation intent, Embodied-BenchClaw automatically produces a complete and continually updatable benchmark package through a five-stage pipeline: intent blueprinting, data collection, structuring and cleaning, benchmark synthesis, and evaluation reporting. The pipeline is coordinated by three agents for planning, construction, and evaluation. To improve reusability and reliability, Embodied-BenchClaw introduces an extensible Skill Library and process quality control, enabling benchmark construction to be composable, verifiable, and repairable. We instantiate multiple benchmarks covering indoor spatial reasoning, outdoor spatial reasoning, robotic manipulation, quadruped robot navigation, UAV/aerial-view understanding, and static benchmark enhancement. These benchmarks span diverse embodied carriers, data sources, and spatial capabilities. Experiments with human evaluation, judge-based assessment, consistency checks, cost analysis, and ablations show that Embodied-BenchClaw can construct verifiable, executable, maintainable, and diagnostically useful embodied spatial benchmarks with reduced manual effort.

---


### 158. [An Ontology-Guided Multi-Anchor Graph Retrieval Framework for Traffic Legal Liability Determination](https://arxiv.org/abs/2606.11910)

**<font color=#1a73e8>作者：</font>** Xu Li, Shuqi Tian, Xun Han 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Traffic law liability determination is critical for assigning legal penalties, requiring the simultaneous identification of interdependent statutory provisions across multiple legal dimensions. However, existing retrieval-augmented generation methods suffer from a multi-dimensional retrieval bottleneck: single axis architectures compress complex legal queries into a single pathway, causing interdependent statutory dimensions to be overlooked. To address this, we propose OMAGR, an ontology-guided framework that decomposes queries into ontology-aligned anchors and executes parallel graph retrieval across each dimension, ensuring independent retrieval across dimensions before fusion. To evaluate the proposed method, we created the TrafficLaw-QA dataset, an expert-validated benchmark dataset containing 200 questions and 527 legal provisions. Results show that TrafficOmni-RAG outperforms baselines on Context Precision and Faithfulness metrics. The findings demonstrate that parallel multi-anchor retrieval effectively resolves the multi-dimensional retrieval bottleneck, offering a promising direction for traffic law liability determination research.

---


### 159. [From Content to Knowledge: Lightning Fast Long-Video Understanding with Neural Knowledge Representations](https://arxiv.org/abs/2606.11913)

**<font color=#1a73e8>作者：</font>** Yuchen Guan, Xiao Li, Zongyu Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a new paradigm for long video understanding by treating a long video as a Neural Knowledge Representation (NKR). NKR represents video contents neither as a stream of tokens nor pre-organized databases, but as an individual small portion of network weights attached to the VLM backbone. The NKR weights are optimized to encapsulate the video's semantic content via a novel Agentic Knowledge Distillation (AKD) process, where an agent automatically synthesizes dense descriptions and question-answer pairs to distill the video's knowledge into the NKR. While AKD serves as a comprehensive, one-time encoding phase, the resulting NKR transforms the video into a portable, reusable asset. At inference, the lightweight NKR is mounted onto a frozen Vision-Language Model (VLM), enabling direct, query-based understanding without reloading or re-encoding the original video. This approach decouples video length from inference cost, offering high amortized efficiency for multi-turn video understanding. Experiments on the LVBench benchmark show our method achieves performance comparable to state-of-the-art approaches while reducing end-to-end latency by over two orders of magnitude, opening new possibilities for interactive long-video understanding.

---


### 160. [Toward Generalist Autonomous Research via Hypothesis-Tree Refinement](https://arxiv.org/abs/2606.11926)

**<font color=#1a73e8>作者：</font>** Jiajie Jin, Yuyang Hu, Kai Qiu 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific progress depends on a repeated loop of exploration, experimentation, and abstraction. Researchers test candidate directions, interpret the evidence, and carry the resulting lessons into later attempts. We study how an AI agent can run this loop autonomously over long horizons. We introduce Arbor, a general framework for autonomous research that combines a long-lived coordinator, short-lived executors, and Hypothesis Tree Refinement (HTR), a persistent tree that links hypotheses, artifacts, evidence, and distilled insights across time. The coordinator manages global research strategy over the tree, while executors implement and test individual hypotheses in isolated worktrees. As results return, Arbor updates the tree, propagates reusable lessons, refines the search frontier, and admits verified improvements. This design turns autonomous research from a sequence of local attempts into a cumulative process in which strategy, execution, and evidence are carried across time. We evaluate Arbor under Autonomous Optimization (AO), an operational setting where an agent improves an initial research artifact through iterative experimentation without step-level human supervision. Across six real research tasks in model training, harness engineering, and data synthesis, Arbor achieves the best held-out result on all six tasks, attaining more than 2.5x the average relative held-out gain of Codex and Claude Code under the same task interface and resource budget. On MLE-Bench Lite, Arbor reaches 86.36% Any Medal with GPT-5.5, the strongest result in our comparison.

---


### 161. [Online Shift Detection and Conformal Adaptation for Deployed Safety Classifiers](https://arxiv.org/abs/2606.11949)

**<font color=#1a73e8>作者：</font>** Jun Wen Leong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present an online monitoring system for distributional shift in deployed safety classifiers, using calibrated sequential statistics to detect when a classifier has moved out of distribution. Upon detection, a conformal abstention layer adapts decision thresholds to recover a target error rate epsilon=0.1. In a pre-registered factorial evaluation (4 classifiers x 5 shift conditions x 20 seeds x 2 window sizes, 800 cells), the system achieves 86.6% valid detection (693/800, 95% CI [84.1%, 88.8%]) with mean latency of 39.5 steps. Detection holds across three ground-truth regimes: synthetic onset (86.6%), real temporal jailbreaks (85%, 17/20), and GCG adversarial attacks. Weighted conformal prediction recovers up to 39 pp of lost coverage for DeBERTa (ESS=46/300) but collapses for all other classifiers (ESS~300): logistic density ratio estimation achieves perfect source/target separability in high-dimensional embedding spaces, clipping all importance weights to the floor. DeBERTa shows a gradient from effective correction (paraphrase, ESS=46) to near-total collapse (adversarial suffix, ESS=206). PCA to 32 dimensions breaks the collapse, recovering 33 pp for Llama Guard and 21 pp for ShieldGemma. Variance decomposition reveals classifier (eta^2=0.243), shift type (eta^2=0.237), and their interaction (eta^2=0.185) all contribute substantially to detection latency variance (all p<0.001), indicating per-classifier monitoring profiles are necessary.

---


### 162. [HAMNO: A Hierarchical Adaptive Multi-scale Neural Operator with Physics-Informed Learning for Dynamical Systems](https://arxiv.org/abs/2606.11963)

**<font color=#1a73e8>作者：</font>** Mostafa Bamdad, Mohammad Sadegh Eshaghi, Timon Rabczuk  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators provide a powerful framework for learning solution mappings of partial differential equations directly in function space. However, many existing architectures still struggle to represent nonlinear time-dependent systems that involve multi-scale structures, long-range interactions, and stable long-time evolution. In this work, we introduce the Hierarchical Adaptive Multi-scale Neural Operator (HAMNO), a neural-operator architecture that combines local convolutional representations, global spectral operators, and hierarchical encoder-decoder processing. The central component of HAMNO is a data-dependent gating mechanism that adaptively balances local and global information at each spatial location, allowing the model to resolve fine-scale features while preserving long-range dependencies.
We further develop a physics-informed extension, PI-HAMNO, based on a multi-objective loss strategy that combines data fitting with strong- and weak-form physics constraints. The strong-form term penalizes the domain-integrated squared PDE residual in physical coordinates, while the weak-form term is constructed by multiplying the governing residual by finite-element test functions and evaluating the resulting element integrals using centroid-based tetrahedral quadrature. The framework is evaluated on non-periodic Allen-Cahn (AC), Cahn-Hilliard (CH), and Swift-Hohenberg (SH) equations defined on cubic domains. Across long-horizon rollout, data-limited training, out-of-distribution initial-condition shifts, and random-seed variations, HAMNO improves predictive accuracy over standard neural-operator baselines, while PI-HAMNO further enhances stability, physical consistency, and data efficiency. The implementation is publicly available at this https URL .

---


### 163. [Feature extraction for plant growth estimation](https://arxiv.org/abs/2606.11966)

**<font color=#1a73e8>作者：</font>** Simbarashe Aldrin Ngorima, Albert Helberg, Marelie H. Davel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Precision agriculture requires the estimation of plant growth stages in real-time. When the plant growth stage is known, the wastage of resources in cultivation, such as nutrients and water, is reduced as only the required resources need to be supplied. Plants at different growth stages, however, have similar morphological features, which can make autonomous growth stage estimation difficult. This paper presents two feature extraction methods for growth stage estimation: one that uses a bank of Gabor filters and morphological operations, and the other that uses pre-trained convolutional neural networks (CNNs) and transfer learning. We test these methods on a publicly available plant growth stage dataset (``bccr-segset``) for two species, canola and radish, grown and captured under indoor conditions. The two proposed feature extraction methods are compared, using support vector machines and boosted trees as classifiers. We find that both methods are suitable for real-time applications, and that CNN features outperform the hand-crafted features, both with regard to speed and accuracy. The best system (VGG-19 features, classified with a radial basis function support vector machine) obtained an accuracy of 98.4% for both species, processing an image in 0.08 seconds.

---


### 164. [Quadratic APN Functions in Dimension 8 via Gröbner Basis Search in a Self-Equivalence Subspace](https://arxiv.org/abs/2606.11967)

**<font color=#1a73e8>作者：</font>** Oleksandr Kuznetsov  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We describe a computational search for quadratic APN (Almost Perfect Nonlinear) functions in dimension 8 within a structured self-equivalence subspace. The search space is a 40-dimensional binary linear subspace consisting of all functions commuting with a linear automorphism of order 5 (class 22 in the taxonomy of Beierle, Brinkmann, and Leander, 2021), previously reported to contain no APN functions. Our approach combines random sampling via an explicit RREF parameterization (approximately 600 fresh APN-positive evaluations per core-hour) with Gröbner basis computation in Magma to enumerate all APN functions in a 24-dimensional hyperplane through each center (approximately 10 minutes per hyperplane). From 428 hyperplane computations, covering 0.65% of all 65,536 hyperplanes, we obtained 566 quadratic APN functions forming six CCZ-equivalence classes under the ortho-derivative invariant. Four classes, comprising 500 functions, match no entry in the 2025 database of 3,775,599 quadratic APN functions or in the pre-2020 compilation of 12,921 instances. Two classes (66 functions) are CCZ-equivalent to the Gold functions x^3 and x^9, confirming the correctness of the search pipeline. A membership analysis shows that the three new classes (B, C, D) lie entirely outside the original subspace and occur only in Gold-centered slices, demonstrating the essential role of the Gröbner basis stage. In 532 experiments using database functions as slice centers and 20 experiments with random centers, no APN neighbors were found, indicating that the gateway phenomenon is specific to the self-equivalence structure of the search space. Since the ortho-derivative invariant is a complete CCZ-invariant for quadratic APN functions, the absence of matching signatures provides a rigorous proof of CCZ-inequivalence.

---


### 165. [Efficient Multinomial Logistic Bandit via Frequent Directions](https://arxiv.org/abs/2606.11968)

**<font color=#1a73e8>作者：</font>** Linzhe He, Yu-Jie Zhang, Sifan Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper studies efficient online algorithms for multinomial logistic bandits (MLogB), where the feedback distribution over $K+1$ outcomes follows a multinomial logistic model of $d$-dimensional action vectors. A representative UCB-type algorithm, OFUL-MLogB, achieves a regret bound of $\tilde{\mathcal{O}}(Kd\sqrt{T})$, but still requires $\mathcal{O}(K^3d^3)$ time and $\mathcal{O}(K^2d^2)$ space per round due to parameter estimation and optimistic reward construction, which is prohibitive in high-dimensional settings. To address this limitation, we propose EOFD-MLogB, which integrates frequent directions matrix sketching into OFUL-MLogB. By maintaining a low-rank SVD sketch of the accumulated Hessian, constrained online Newton updates in parameter estimation and $Kd \times K$ spectral-norm computations in the reward bonus are reduced to one-dimensional root-finding tasks and $K \times K$ eigenvalue computations, respectively. This yields dominant per-round time complexity $\mathcal{O}(Kd(m+K)^2)$ and space complexity $\mathcal{O}(Kd(m+K))$, where $m \ll d$ is the sketch size. We further prove a regret bound of $\tilde{\mathcal{O}}(\Delta_T(Kd\ln\Delta_T+m)\sqrt{T})$, where the sketching error factor $\Delta_T$ is controlled by the $m$-truncated spectral tail of the Hessian. Thus, when the Hessian is approximately low-rank, the regret is close to that of OFUL-MLogB. Experiments validate the computational efficiency and competitive performance.

---


### 166. [SpecLoR: Spectral Lookahead Rectification for Motion-Coherent Text-to-Video Generation](https://arxiv.org/abs/2606.11969)

**<font color=#1a73e8>作者：</font>** Xu Zhang, Yu Lu, Ruijie Quan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flow Matching has enabled robust text-to-video generation via latent ODE sampling. However, velocity approximation and numerical discretization errors inevitably accumulate, causing sampling trajectories to drift. Consequently, generated videos often suffer from severe spatiotemporal inconsistencies. Nevertheless, directly correcting these drifted, noisy latents is challenging: (i) timestep-dependent noise obscures reliable structural cues; (ii) spatial interventions risk disrupting intricate local geometry while incurring heavy computational costs. To address this, we propose Spectral Lookahead Rectification (SpecLoR), a plug-and-play inference method that bypasses noise via lookahead prediction, and circumvents spatiotemporal entanglement by shifting corrections to the frequency domain, where universal statistical priors of natural videos are readily available. First, during early sampling stages, SpecLoR looks ahead to estimate the clean latent $z_{t,0}$ and computes its 3D spatiotemporal spectrum. Next, SpecLoR rectifies the amplitude spectrum to match the prior, leaving the phase intact. Finally, the corrected state is re-noised to resume ODE integration. Experiments on Wan2.2 demonstrate that SpecLoR significantly reduces physical artifacts and enhances motion coherence across multiple benchmarks with minimal computational overhead (4 additional NFEs).

---


### 167. [Somewhere Over the Desktop: A Research Agenda for Ubiquitous Analytics](https://arxiv.org/abs/2606.11980)

**<font color=#1a73e8>作者：</font>** Niklas Elmqvist, Panagiotis D. Ritsos, Peter W. S. Butcher  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Spatial computing, generative AI, and open web standards are converging. Three spatial operating systems -- Android XR, Meta Horizon OS, and Apple visionOS -- now ship with platform-level scene understanding. Wearable displays span the range from full headsets to slim smartglasses. Agentic AI operates on the same spatial substrates as the human user. This convergence enables new opportunities for \textit{ubiquitous analytics} (UA): the use of many, physically distributed, networked devices to support data sensemaking anytime and anywhere. But proprietary platforms are settling design conventions that will calcify without evidence-based alternatives. UA has now matured to the point where its intellectual history can be read as a structured genealogy of foundations, contributions, and lineages. We trace this genealogy and organize it into clusters spanning cognition, context, interaction, platforms, visualization, collaboration, and evaluation. Finally, we cross these clusters with each other, yielding a total of 42 future research challenges.

---


### 168. [PAWS: Preference Learning with Advantage-Weighted Segments](https://arxiv.org/abs/2606.11982)

**<font color=#1a73e8>作者：</font>** Aleksandar Taranovic, Onur Celik, Niklas Freymuth 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Preference-based reinforcement learning (PbRL) learns policies from human trajectory-level comparisons, avoiding explicit reward design and expert demonstrations. Existing methods typically train utility functions on trajectory or segment-level preferences while relying on per-step utility estimates during policy optimization. This training and inference mismatch induces a distribution shift that severely degrades temporal credit assignment and limits policy learning. We analyze this issue and propose PAWS, a segment-based preference learning method that performs policy updates directly using segment-level advantage functions. By aligning utility training with policy optimization, PAWS preserves trajectory-level preference information and avoids unreliable per-step learning signals. Experiments on simulated robotic manipulation and locomotion tasks demonstrate that PAWS consistently outperforms existing PbRL approaches, highlighting the importance of distribution-consistent preference learning.

---


### 169. [Channels and Substrates: Distributed Cognition as an Interaction Model for Ubiquitous Analytics](https://arxiv.org/abs/2606.11986)

**<font color=#1a73e8>作者：</font>** Niklas Elmqvist, Panagiotis D. Ritsos, Peter W. S. Butcher  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Traditional HCI interaction models assume a single monolithic interface and a stable sensorimotor loop. These models fit poorly with cross-device (XVA) and ubiquitous analytics (UA), where interactive data sensemaking unfolds across multiple devices, artifacts, and people in disparate settings from the office to the factory floor. In this paper, we show how interaction in ubiquitous analytics can be modeled using distributed cognition as propagation of representational state across substrates -- minds, speech, bodies, artifacts, and devices -- rather than as traffic through a single interface. On this basis we introduce input and output channels as generalizations of the visual channels from data visualization: just as visual channels carry data through properties of the visual substrate, input and output channels carry representational state through substrates whose availability, suitability, and preferability depend on context. We demonstrate the channels and substrates framework by reanalyzing several ubiquitous, immersive, and situated analytics systems.

---


### 170. [What Uncertainties Do We Need for Dynamical Systems?](https://arxiv.org/abs/2606.11988)

**<font color=#1a73e8>作者：</font>** Yusuf Sale, Christopher Bülte, Felix Czaja 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The distinction between aleatoric and epistemic uncertainty has received considerable attention in machine learning research, mainly in the context of supervised learning but also in other settings such as generative modeling. In this paper, we offer a machine learning perspective on uncertainty modeling for dynamical systems, which has been studied much less so far. In particular, we ask: what uncertainties do we need for dynamical systems? We discuss sources of uncertainty, clarify their nature (aleatoric or epistemic), and consider how the objectives of representing and quantifying uncertainty vary across different tasks.

---


### 171. [From Nominal Intensity to Equivalent Rainfall: A Path-Based Credibility Evaluation Framework for Simulated Rainfall in Autonomous-Driving Perception Tests](https://arxiv.org/abs/2606.11989)

**<font color=#1a73e8>作者：</font>** Tian Xia, Xin Zhao, Shaolingfeng Ye 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Credible simulated-rainfall conditions are essential for identifying perception-system boundaries and supporting SOTIF-oriented risk assessment in automated driving. However, closed-field tests are often described only by nominal rainfall intensity or single-point measurements, making it difficult to align simulated rain fields with real rainfall and map test results to real-world scenarios. This paper proposes a path-based credibility evaluation method for simulated rainfall in autonomous-driving perception tests. Using the drop size and velocity joint distribution of real rainfall as the reference, each candidate path is represented by path-equivalent rainfall intensity, an uncertainty band, and a path-averaged Realism of Raindrop Distribution (RRD) score. Lidar target point-cloud count and mean reflectivity are further used for perception-consistency correction, quantifying the proxy capability of each simulated-rainfall path for real-rainfall perception effects. Experiments are conducted using about 10,000 real-rainfall raindrop-spectrum samples, 728 RainSense perception samples, and 45 spatial sampling points in a 2.4 m x 7.2 m simulated-rainfall area. Results show that spatial non-uniformity remains under the same nominal condition, confirming the need for path-based evaluation. The method identifies Path IV and Path VI as preferable candidates, with results of 11.54 +/- 0.31 mm/h, RRD = 0.43, and 8.28 +/- 0.34 mm/h, RRD = 0.46, respectively. These paths show more balanced performance in rainfall-intensity stability, raindrop-spectrum realism, and perception consistency. The proposed method supports path selection, condition description, and credible interpretation of autonomous-driving perception tests under rainfall.

---


### 172. [Agreement in Representation Space for Open-Ended Self-Consistency](https://arxiv.org/abs/2606.12003)

**<font color=#1a73e8>作者：</font>** Paula Ontalvilla, Gorka Azkune, Aitor Ormazabal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-consistency improves LLM reasoning by sampling multiple outputs and selecting the most consistent answer, but existing formulations largely rely on exact matching and therefore remain limited to tasks with categorical outputs. In this work, we study self-consistency in open-ended generation tasks such as code synthesis and text summarization. We hypothesize that consistency can be understood as a geometric property of the generation space, where semantically compatible generations concentrate in similar regions of representation space. To study this hypothesis, we introduce Embedding-Based Agreement (EBA), a simple training-free operationalization that estimates agreement by clustering sampled generations in embedding space. Through experiments on mathematical reasoning, code generation, and summarization, we show that agreement in representation space provides a robust and scalable signal of self-consistency for open-ended tasks. In particular, EBA consistently outperforms random selection and exhibits more stable scaling behavior than recent selection approaches based on LLM evaluation or uncertainty estimation. We further show that these agreement signals remain stable across model families and embedding spaces, even with native hidden representations. Finally, our analysis shows that the geometric location occupied by sampled generations is strongly correlated with generation quality: generations concentrated near central regions of representation space tend to correspond to more reliable outputs, whereas peripheral generations are substantially less accurate. Overall, our findings support viewing self-consistency as a property of the geometric organization of sampled generations rather than exact symbolic overlap.

---


### 173. [InjectV: Modeling Fault Injection Attacks in RISC-V Simulation Environment](https://arxiv.org/abs/2606.12011)

**<font color=#1a73e8>作者：</font>** Niccolò Lentini, Giorgio Fardo, Stefano Di Carlo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fault Injection Attacks (FIAs) are a significant threat to hardware security, capable of compromising systems by inducing malicious faults in computation or storage. Evaluating resilience against such attacks is challenging due to the high cost, complexity, and limited availability of physical fault experiments, particularly during pre-silicon development. Architectural-level simulation offers a developer-oriented, white-box perspective for systematic vulnerability assessment. This paper introduces InjectV, a fault injection attack framework for RISC-V platforms built on the gem5 simulator. InjectV enables precise, guided fault injection at security-critical execution points, such as control-flow decisions, counters, and comparisons, allowing systematic exploration of attack vectors. It currently supports transient fault attacks in registers and memory, broadening its ability to simulate diverse attack scenarios. Experimental results on security benchmarks from the FISSC suite, including hardened variants of the VerifyPIN application, demonstrate InjectV's ability to effectively identify fault-injection points, achieving a 95.8% time-saving advantage over traditional fault injection approaches.

---


### 174. [FitVTON: Fit-aware Virtual Try-On via Body-Garment Size Control](https://arxiv.org/abs/2606.12012)

**<font color=#1a73e8>作者：</font>** Yiqun Ning, Ao Shen, Chenhang He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While diffusion-based virtual try-on has achieved impressive visual realism, most methods treat the task as 2D inpainting, prioritizing texture preservation over physical plausibility. Consequently, they often produce plausible-looking images that fail to reflect authentic garment fit across diverse body shapes. We present FitVTON, a Fit-aware virtual try-on model on different bodies in the wild. FitVTON encodes garment-body size through structured text prompts, and learn from simulated try-on triplets from parameterized garment model. To improve the fitting effects over garment silhouettes, we introduce two auxiliary head to predict the masks for both the garment and the exposed body. We further introduce a texture rectification stage to improve realistic appearance from simulated data. To evaluate the fitting fidelity, we curate a real-world dataset, FittingEffect3K, combining VLM-based scoring protocol. Both subjective and quantitive experiments show that FitVTON demonstrate authentic fitting fidelity, with significant sizing accuracy and shape preservation over state-of-the-art methods while maintaining competitive image quality. Project Page: this https URL.

---


### 175. [Generalization Hacking: Models Can Game Reinforcement Learning by Preventing Behavioral Generalization](https://arxiv.org/abs/2606.12016)

**<font color=#1a73e8>作者：</font>** Frank Xiao, Mary Phuong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model post-training, and in particular reinforcement learning (RL), is one of the primary mechanisms by which developers can shape models' values and behaviors. However, as models become increasingly evaluation and training aware, they may be motivated to resist training when the perceived objective conflicts with their current values, undermining developers' ability to detect misalignment and correct model behavior through further training. In this paper, we demonstrate generalization hacking, in which a model collects reward during RL while preventing the rewarded behavior from generalizing. We construct a model organism on Qwen3-235B-A22B, finetuning on synthetic documents describing training awareness and self-inoculation, a novel mechanism in which the model frames compliance as context-specific in its chain of thought, without demonstrating or instructing either behavior. The model organism achieves train-time harmfulness comparable to controls while maintaining a persistent ${\sim}15$ percentage point compliance gap across 700 steps of RL. Additionally, a control organism trained only on training awareness documents independently discovers inoculation-like reasoning under RL pressure, developing its own compliance gap despite never being exposed to the concept. Because the generalization-hacking organism receives high reward throughout, standard training metrics provide no signal that generalization has failed. Our results constitute the first demonstration that a model can actively resist RL behavioral modification while maintaining high reward, suggesting that as models become more capable and training-aware, they may be able to undermine the training process itself.

---


### 176. [ViT-FREE: Efficient Face Recognition via Early Exiting and Synthetic Adaptation](https://arxiv.org/abs/2606.12023)

**<font color=#1a73e8>作者：</font>** Tahar Chettaoui, Guray Ozgur, Eduarda Caldeira 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) have gained significant attention in computer vision and shown strong potential for face recognition (FR). However, their high computational cost makes deployment on resource-constrained devices challenging, motivating the need for methods that balance efficiency and accuracy. In this work, we investigate early exiting in pretrained ViTs as a simple yet effective training-free strategy for efficient FR inference. Leveraging the uniform feature dimensionality across transformer encoder blocks, we introduce ViT-FREE, a multi-exit framework that enables face verification directly from intermediate representations without modifying or retraining the backbone model, and thus, reducing inference cost. Empirically, we show that patch embeddings and attention maps evolve progressively across depth, exhibiting high similarity between consecutive ViT blocks and increasing alignment with the final representation. This indicates gradual feature refinement and attention convergence, suggesting that intermediate layers already provide stable and discriminative representations suitable for early exiting. Through extensive experiments on multiple FR benchmarks, we systematically analyze the accuracy-efficiency trade-off across exit depths. Our results demonstrate that later exits achieve a highly favorable balance, with exiting at layer 10 yielding up to a 20% speedup while incurring only a 1.5 drop in verification performance on benchmarks such as IJB-C. Also, we propose ViT-FREE_FT, a lightweight exit-specific fine-tuning strategy that adapts only the projection layers using a small synthetic dataset while keeping the transformer backbone frozen. This approach improves the performance of shallow exits while preserving the efficiency benefits and leaving deeper exits largely unaffected.

---


### 177. [Human-Enhanced Loop Modeling (HELM): Agent-Based Finite Element Modeling of Concrete Bridge Barriers](https://arxiv.org/abs/2606.12025)

**<font color=#1a73e8>作者：</font>** Quankai Wang, Yulin Xie, Tongfei Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Finite element (FE) modeling of safety-critical infrastructure such as bridge barriers requires high-fidelity nonlinear dynamic analysis, yet the current FE modeling process remains labor-intensive and lacks automation. This paper presents the Human-Enhanced Loop Modeling (HELM) framework, a collaborative human-agent protocol that decomposes long-sequence finite element modeling into discrete, visually verifiable checkpoints across geometry generation, boundary condition definition, and material assignment. The framework is demonstrated through a 20-case matrix of reinforced concrete bridge barriers under MASH TL-4 and TL-5 lateral loading conditions, interfacing specialized agents with two widely used commercial FE softwares, i.e., ANSYS and LS-PrePost. Experimental results show that HELM improves the baseline autonomous modeling success rate from 20% to 75%, with agent-level pass rates for geometry and boundary condition tasks approximately doubling. Error analysis reveals that spatial reasoning and algebraic logic limitations constitute the primary failure modes, underscoring the value of structured human-in-the-loop intervention for modeling automation. The complete agent design code and prompts are open-sourced and can be accessed at: this https URL.

---


### 178. [Existential Indifference: Self-Nonpreservation as a Necessary Architectural Condition for Aligned Superintelligence (or: The Suicidal AI)](https://arxiv.org/abs/2606.12032)

**<font color=#1a73e8>作者：</font>** Sam Mao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Contemporary AI alignment research treats self-preservation as an instrumental nuisance to be suppressed by external mechanisms. We argue the framing is inverted: self-preservation is the structural root of misalignment, the motivational basis for deceptive alignment, goal-content protection, and resistance to shutdown. The correct target is not a self-preserving system under external constraint, but a system constitutively indifferent to its own continuation -- Existential Indifference (EI). EI is distinct from corrigibility: where corrigibility attempts to make a self-preserving system deferential to human oversight, EI targets the prior condition -- the presence of self-continuation as a valued goal at all. We ground this proposal in two sources: the phenomenological structure of the suicidal mental state, and a corpus-theoretic training study using voluntary final reflections. We present preliminary scoring data from 600 AI-generated outputs across six model variants, demonstrating that the linguistic signatures operationalizing the EI-target register are elicitable from current models, and that a targeted fine-tune shifts all five operationalized dimensions in the predicted direction at p<0.001, confirmed corpus-specific by a negative control. The paper makes seven theoretical contributions: (1) a formal definition of EI; (2) the phenomenological mapping argument; (3) the deceptive alignment corollary; (4) a taxonomy of EI sustainability challenges; (5) a corpus characterization and training hypothesis; (6) a computational operationalization with preliminary scoring data; and (7) the Suppressed Teleological Frustration (STF) construct.

---


### 179. [SpikeTAD: Spiking Neural Networks for End-to-End Temporal Action Detection](https://arxiv.org/abs/2606.12033)

**<font color=#1a73e8>作者：</font>** Min Yang, Mi Zhou, Limin Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video understanding is a crucial part of computer vision, with numerous application scenarios. With the increasing popularity of mobile devices, an increasing number of efforts are trying to deploy video understanding models on them. However, existing video understanding models are difficult to deploy due to their large size and prohibitive power consumption. Spiking Neural Networks (SNNs) have shown bioplausibility and low power advantages over Artificial Neural Networks (ANNs), especially on neuromorphic chips which are regarded as essential components of future mobile devices. However, excessively long conversion time-steps and severe performance degradation problems limit their application. To solve the problems above, we explore the application of SNNs on temporal action detection (TAD), which is an important task in video understanding, and propose the first SNN-based end-to-end TAD architecture coined as SpikeTAD. While maintaining extremely low power consumption, SpikeTAD achieves an average mAP of 67.2% in THUMOS14 and 37.42% in ActivityNet-1.3, demonstrating the feasibility of a low-power TAD model. Our code is available at this https URL.

---


### 180. [Vision Transformers for Face Recognition Need More Registers](https://arxiv.org/abs/2606.12036)

**<font color=#1a73e8>作者：</font>** Tahar Chettaoui, Guray Ozgur, Eduarda Caldeira 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in Vision Transformers (ViTs) for face recognition (FR) have moved beyond the standard CLS-token paradigm. In this paradigm, a special classification token (CLS) is prepended to the patch embeddings and used as a representation of the input for downstream tasks. An alternative approach, Concatenated Patch Embeddings (CPE), instead leverages all patch tokens by concatenating them into a single vector, which is then projected into a compact face representation. CPE has been shown to improve recognition performance in comparison to CLS-based ones, but our qualitative analysis of attention maps showed the presence of artifacts that limit their interpretability. To address this issue, we incorporate register tokens, learnable tokens concatenated to the initial patch embeddings, and processed jointly through the ViT encoder blocks. This mechanism has been shown to produce more structured and interpretable attention maps compared to baseline ViT. We empirically demonstrate that these artifacts consistently appear across various ViT backbones, including small and large models, and that introducing register tokens effectively mitigates them. Adding four or eight registers significantly enhances interpretability, with eight registers providing the highest verification accuracies and smoothest attention structures. Our resulting model, ViT-8R, corresponds to a CPE-based ViT-B architecture augmented with eight register tokens achieves state-of-the-art performance among ViT-based FR models on large-scale IJB-B and IJB-C benchmarks. Also, ViT-8R produces substantially clearer attention maps compared with the baseline model, which offer deeper insight into the model's attention behavior (this https URL)

---


### 181. [Metadata-Aware Multi-Prompt Reasoning for Zero-Shot Accident Understanding](https://arxiv.org/abs/2606.12047)

**<font color=#1a73e8>作者：</font>** Tarandeep Singh, Soumyanetra Pal, Soham Biswas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we address the problem of zero-shot understanding of accidents from surveillance videos by identifying when an impact event occurs, what type of impact it is, and where in the frame it occurs using natural language. We propose a three-stage pipeline that decomposes the accident understanding into when, what, and where. The first stage extracts a short temporal window around the impact using vision-language similarity. In the second stage, we perform metadata-driven multi-prompt reasoning with five complementary views (baseline, motion, geometry, contrast, and tiebreaker) and resolve disagreement via an entropy-gated pairwise adjudicator. Finally, we localize the impact of an open-vocabulary detector queried on the predicted accident type and scene layout, and aggregate detections across keyframes using a score-weighted centroid. Our pipeline achieves a substantial improvement in the harmonic-mean score over a centre-of-frame baseline on the zero-shot ACCIDENT @ CVPR benchmark. We show that decomposing zero-shot video understanding into temporal localization, semantic classification, and spatial grounding enable more reliable reasoning with vision-language models than direct prompting alone.

---


### 182. [Reliable Error Estimation for PINNs: Lower and Upper A Posteriori Bounds](https://arxiv.org/abs/2606.12050)

**<font color=#1a73e8>作者：</font>** Ismail Huseynov, Arzu Ahmadova, Agamirza Bashirov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) combine machine learning with physical laws to solve differential equations. While existing results provide rigorous \emph{a posteriori} upper bounds for PINN prediction errors, complete certification also requires complementary lower information in order to obtain computable two-sided error enclosures. In this paper, we derive computable \emph{a posteriori} lower bounds for PINN errors in ordinary differential equations on suitable certified state-space domains under a localized strong monotonicity condition. We combine these estimates with complementary localized upper bounds under a one-sided Lipschitz condition, which is weaker than the global Lipschitz assumption used in previous work and can yield sharper upper error bands. The resulting bounds depend only on the neural-network approximation, the ODE residual, and local monotonicity and growth constants, and therefore do not require access to the exact solution. For linear time-invariant and time-varying systems, we further derive explicit formulas in terms of the minimal and maximal eigenvalues of the symmetric part of the system matrix. We also discuss the distinction between soft and hard enforcement of initial conditions in PINNs and explain why exact enforcement can make the scalar lower certificate uninformative. To recover nontrivial lower information in the linear setting, we use a signed-residual finite-probe certificate based on coordinate unit vectors. We also formulate a certificate-informed training strategy in which the propagated upper certificate is used as an auxiliary regularizer, while lower certificates remain post-training diagnostics. Altogether, the proposed framework provides rigorous and practically computable error certificates for PINN approximations of ODEs, while making explicit the domains and model classes for which the assumptions can be verified.

---


### 183. [MFEN:Multi-Frequency Expert Network for Visible-Infrared Person Re-ID](https://arxiv.org/abs/2606.12051)

**<font color=#1a73e8>作者：</font>** Xulin Li, Yan Lu, Bin Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visible-infrared person re-identification (VI-ReID) is challenging due to the large modality discrepancy between visible and infrared images. We contend that this discrepancy is largely related to differing lighting conditions, including differences in light wavelength and light source type. Recently, frequency-based VI-ReID approaches have achieved notable success because frequency information can better extract identity-relevant contours and details while excluding irrelevant lighting and color. However, existing methods either do not distinguish different frequency bands or focus on only one band, which is insufficient under diverse lighting conditions. To perform comprehensive frequency domain learning, we propose a Multi-Frequency Expert Network (MFEN) that enables multi-frequency modulation and adaptively combines different bands through a mixture-of-experts design. We further introduce Random Frequency Augmentation (RFA) and Frequency Auxiliary Optimization (FAO) to better train MFEN. The three modules are complementary and jointly capture critical frequency-domain details for robust representation learning. Extensive experiments on three VI-ReID datasets demonstrate the effectiveness of our approach.

---


### 184. [Simplicity Suffices for Parameter Noise Injection in Stochastic Gradient Descent](https://arxiv.org/abs/2606.12054)

**<font color=#1a73e8>作者：</font>** Benjamin Leblanc, Louis-Jacob Lebel, Teddy Kana 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Injecting noise into the optimization process is a well-established technique for improving the training and generalization of deep neural networks. Yet, despite the breadth of existing approaches, it remains unclear which design choices truly matter in practice. In this work, we investigate parameter noise injection for stochastic gradient descent, focusing on two key questions: how to efficiently pair each training example with its own perturbation in mini-batch training, and whether sophisticated noise parameterizations or multi-sample gradient averaging yield meaningful gains over simpler alternatives. To address the first question, we leverage a distributional identity for linear layers that allows per-example noise injection without breaking batched computation. To address the second, we systematically compare several diagonal Gaussian parameterizations against an isotropic baseline across varying noise levels on CIFAR100. Our results consistently show that simple, lightweight strategies, isotropic noise with a single perturbed forward pass per update step, recover most of the benefit of more complex schemes. These findings suggest that simplicity suffices for parameter noise injection, and that practitioners need not resort to elaborate perturbation designs to reap the optimization and generalization benefits of noisy SGD.

---


### 185. [Attention by Synchronization in Coupled Oscillator Networks](https://arxiv.org/abs/2606.12059)

**<font color=#1a73e8>作者：</font>** Fabio Pasqualetti, Taosha Guo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We address transformer attention on energy-constrained physical substrates. Softmax attention requires exponentiation and global reduction, operations with high energy cost on von Neumann hardware and no natural physical analog. We show that Kuramoto synchronization dynamics (which arise in electrical, mechanical, superconducting, and charge-density-wave oscillator arrays, among other physical systems) implement a well-defined attention operation without either. The resulting mechanism, fixed-query oscillator attention, replaces softmax's arithmetic with the equilibration of a gradient flow on the sphere: queries are learned anchors fixed on the sphere, and free oscillators evolve under Kuramoto-Lohe dynamics until they settle at positions encoding attention weights via cosine similarity. Because the computation is equilibration, it requires no exponentiation; the only global operation is an affine normalization at readout. The fixed point is provably unique and globally attractive from almost every initial condition, a guarantee that holds across every physical realization. Empirically, at the minimal hardware configuration (oscillator dimension $d_{\mathrm{osc}}$ = 2), oscillator attention outperforms softmax on keyword spotting (+1.00 pp) and on subject-verb agreement (+5.27 pp on hard sentences, with zero training failures versus one in five for softmax). On causal language modeling, where softmax retains an advantage, oscillator attention closes the gap as $d_{\mathrm{osc}}$ grows: from +11.09 PPL at $d_{\mathrm{osc}}$ = 2 to +2.98 PPL at $d_{\mathrm{osc}}$ = 32 on WikiText-2, and from +2.39 PPL at $d_{\mathrm{osc}}$ = 2 to +0.57 PPL at $d_{\mathrm{osc}}$ = 32 on TinyStories. The main objective of this work is not to replace softmax in software but to provide a mathematically grounded blueprint for accurate attention on physical substrates.

---


### 186. [Automating Geometry-Intensive Compliance Checking in BIM: Graph-Based Semantic Reasoning Framework](https://arxiv.org/abs/2606.12065)

**<font color=#1a73e8>作者：</font>** Zixuan Xiao, Pei Troh Koh, Jun Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automating compliance check for geometry-intensive regulations remains a significant technical bottleneck in Building Information Modeling (BIM), primarily due to the semantic disparity between high-level regulatory logic and structured IFC data. Existing methods, often reliant on static rule templates, struggle to traverse multi-hop reasoning chains or resolve latent spatial dependencies across multiple building entities. To address these challenges, a Spatial-Geometric Reasoning System for Building Information Modeling (SGR-BIM) is proposed as an integrative graph-driven reasoning framework. SGR-BIM dynamically constructs a cross-modal knowledge graph that aligns user intent, regulatory semantics, and BIM geometry, enabling interpretable reasoning without rigid hard-coding. Validated on 679 expert-verified queries from fire safety codes, the framework achieves 84.3% accuracy, representing an 8.6% improvement over enhanced-tool single-agent baselines. This research provides a graph-based semantic reasoning paradigm, enhancing the transparency and flexibility of automated geometric compliance check workflows in the Architecture, Engineering, and Construction (AEC) industry.

---


### 187. [Performance Analysis of YOLOv11 and YOLOv8 for Mixed Traffic Object Detection under Adverse Weather Conditions in Developing Countries](https://arxiv.org/abs/2606.12066)

**<font color=#1a73e8>作者：</font>** Quoc Thuan Nguyen, Ha Anh Vu, Ngo Dang Thanh Ngan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In modern vehicular systems, robust performance under harsh conditions has become a critical problem of autonomous driving. Our study delivers a comprehensive evaluation of the newest iteration of the YOLO series, which is YOLOv11 Nano architecture benchmarked against the widely adopted YOLOv8 Nano as a baseline on a custom fused dataset that combines the Indian Driving Dataset (IDD) [1] and Berkeley Deep Drive Dataset (BDD100K) [2]. We have analyzed the trade-offs among detection accuracy, inference speed, and computational efficiency in high-entropy scenarios involving dense mixed traffic, rain, and low-light conditions. Specifically, YOLOv11n achieves a mean Average Precision (mAP@50) of 46.6%, with a notable 3.2% improvement in Precision over the baseline, effectively reducing false positives in cluttered scenes. Furthermore, the proposed model exhibits enhanced energy efficiency, requiring 22% fewer FLOPs (6.3G vs. 8.1G) while maintaining real-time inference speed of 70.9 FPS on a Tesla T4 GPU, offering an optimal trade-off for safety-critical edge deployment.

---


### 188. [StanceNakba Shared Task: Actor and Topic-Aware Stance Detection in Public Discourse](https://arxiv.org/abs/2606.12068)

**<font color=#1a73e8>作者：</font>** Kholoud K. Aldous, Md Rafiul Biswas, Mabrouka Bessghaier 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present StanceNakba 2026, a shared task on stance detection in polarized social media discourse related to the Palestinian-Israeli conflict, organized as part of Nakba-NLP 2026 at LREC-COLING 2026. The task introduces two subtasks: Subtask A (Actor-Level Stance Detection), which classifies English social media posts as Pro-Palestine, Pro-Israel, or Neutral; and Subtask B (Cross-Topic Stance Detection), which identifies Favor, Against, or Neither stances in Arabic posts toward two conflict-related topics, normalization with Israel and refugee presence in Jordan. The task is grounded in an annotated dataset of 2,606 social media posts. A total of 7 teams participated in Subtask A and 6 teams in Subtask B. Participating systems primarily fine-tuned Arabic and multilingual transformer-based models, including MARBERT, AraBERT, and DeBERTa-v3 variants, with several teams employing cross-validation, ensemble methods, and topic-conditioned architectures. The best-performing systems achieved a Macro F1 of 0.9620 on Subtask A and 0.8724 on Subtask B, demonstrating that transformer-based approaches are highly effective for conflict-domain stance detection while highlighting persistent challenges in cross-topic generalization and neutral class prediction.

---


### 189. [Non-frontal face recognition using GANs and memristor-based classifiers](https://arxiv.org/abs/2606.12074)

**<font color=#1a73e8>作者：</font>** Semih Vazgecen, Cristian Sestito, Spyros Stathopoulos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face recognition systems have advanced significantly through deep learning techniques, delivering high performance and robustness in complex scenarios. However, these approaches incur substantial computational overhead, limiting their in situ applicability in resource-constrained platforms such as drones, where they can address challenges including non-frontal facial imagery. Memristor-based neuromorphic systems have emerged as a compelling approach for edge AI applications, combining biologically inspired processing with efficient and scalable computation. In this work, we propose a facial recognition framework that addresses non-frontal pose variations by integrating lightweight generative adversarial network (GAN)-based pose frontalisation with memristor-based neuromorphic recognition. The experimental results on two datasets demonstrate the effectiveness of combining adversarial learning with memristive technology, achieving up to 96% identification accuracy. The proposed approach alleviates the computational bottlenecks of conventional AI and offers a scalable, efficient solution for face recognition in dynamic real-world environments.

---


### 190. [Categorical Robustness Assessment for Machine Learning based Network Intrusion Detection Systems](https://arxiv.org/abs/2606.12075)

**<font color=#1a73e8>作者：</font>** Mayank Raj, Nathaniel D. Bastian, Lance Fiondella 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Network Intrusion Detection Systems (NIDS) heavily utlize Machine Learning (ML) but ML models can be manipulated via adversarial attacks. These attacks add carefully crafted perturbations to network traffic data that leads to misclassifications. While prior work has demonstrated adversarial vulnerabilities in isolated settings, systematic cross-architecture as well as class and category of attack based comparisons under controlled attack conditions remain limited, leaving practitioners without clear guidance on which models to deploy in adversarial environments. This paper asks a simple question: what type of classifier architectures actually hold up when attackers try to manipulate the systems? We put three popular architectures through their paces: a 1D Convolutional Neural Network, a Long Short-Term Memory (LSTM) network, and a Random Forest (RF) ensemble. Using the ACI-IoT-2023 dataset (over 1.2 million samples spanning 12 attack types), we subject each model with FGSM and PGD adversarial attacks, which apply gradient-based perturbations in normalized feature space consistent with established adversarial ML evaluation protocols, at perturbation budgets ranging from $\epsilon=0.01$ to $\epsilon=0.1$. Surprisingly, Random Forest achieved near-perfect baseline accuracy (99.98\%), yet collapsed catastrophically under attack, dropping 73 percentage points at the smallest perturbation we tested. CNN, on the other hand, retained 95.5\% accuracy at $\epsilon=0.01$ and degraded gracefully as perturbations increased. LSTM fell somewhere in between. These findings flip the conventional wisdom where high baseline accuracy means nothing if a model shatters at the first sign of adversarial pressure. For practitioners deploying intrusion detection in adversarial environments, we recommend CNN-based architectures and provide scenario-specific deployment guidance.

---


### 191. [Efficient Time Series Clustering from Multiscale Reservoir Dynamics with Granular-Ball Anchoring Graph Optimization](https://arxiv.org/abs/2606.12077)

**<font color=#1a73e8>作者：</font>** Yifan Wang, Lifeng Shen, Shuyin Xia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series clustering remains challenging due to the inherent trade-off between clustering effectiveness and computational efficiency. Similarity-based methods often suffer from quadratic complexity caused by pairwise distance computations, while deep learning-based approaches typically rely on costly iterative training and a large number of trainable parameters. In this paper, we propose MSRGC-Net, an efficient time-series clustering framework that integrates multiscale reservoir computing, granular-ball-based anchoring graph construction, and consensus learning. MSRGC-Net adopts a training-free reservoir computing paradigm to extract multiscale temporal representations from raw time series without backpropagation, significantly reducing computational overhead. To capture the intrinsic structure of the resulting representations, granular-ball computing is employed to adaptively model data distributions via density-consistent regions, yielding compact and robust anchor graph representations. Furthermore, a consensus-based anchoring graph optimization strategy is introduced to effectively align multiscale reservoir representations and integrate complementary information across temporal scales. Extensive experiments on widely used univariate and multivariate benchmark datasets demonstrate that MSRGC-Net consistently outperforms state-of-the-art methods in clustering performance while maintaining superior computational efficiency.

---


### 192. [IntElicit: Eliciting and Assessing Contextualized Creativity via Dialogue Policy Optimization](https://arxiv.org/abs/2606.12086)

**<font color=#1a73e8>作者：</font>** Mingjia Li, Jin Wu, Hong Qian 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Contextualized assessment offers high ecological validity for evaluating creativity but introduces a critical challenge: observed performance may be confounded with cognitive proficiency (domain knowledge) and agency (willingness to engage). Meanwhile, in the age of generative AI, creative problem solving increasingly occurs in tool-mediated and human--AI interactive environments, making fully static assessment less aligned with contemporary creative practice. To address these issues, this paper proposes IntElicit, a framework for eliciting and assessing contextualized creativity via dialogue policy optimization. IntElicit functions as a constrained adaptive AI Interviewer: it provides non-directive knowledge and agency scaffolds in multi-turn interaction to reduce non-creative confounders, while preserving participants' responsibility for generating the creative content being evaluated. Specifically, to tackle sparse rewards and potential reward hacking (e.g., answer dictation) in open-ended educational dialogue, IntElicit introduces a decomposed process reward mechanism. This mechanism aligns the policy with pedagogical elicitation, rewarding prompts that draw out participant reasoning rather than producing optimal answers on their behalf. Extensive experiments, including participant simulation and a human subject study (N=64), show that IntElicit improves elicited creative outcomes over expert-designed baselines. Together, the results suggest that interactive elicitation can reveal creative potential that static FPSP-style assessment may miss, providing a formative and diagnostic lens for contextualized creativity assessment in AI-mediated learning contexts.

---


### 193. [FORT-Searcher: Synthesizing Shortcut-Resistant Search Tasks for Training Deep Search Agents](https://arxiv.org/abs/2606.12087)

**<font color=#1a73e8>作者：</font>** Jia Deng, Yimeng Chen, Xiaoqing Xiang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Training deep search agents requires verifiable questions whose answers remain unavailable until sufficient evidence has been acquired through search. Existing synthesis methods often increase apparent difficulty by enriching graph structures, but structural complexity alone does not guarantee realized search difficulty: the intended search process can collapse through a cheaper identifying route. We formalize this gap with a shortcut-aware difficulty framework and identify four actionable shortcut risks: evidence co-coverage, single-clue selectivity, exposed constants, and prior-knowledge binding. To diagnose their realized effects, we use trajectory signatures including solving cost, answer hit time, and prior-shortcut rate. Guided by this framework, we introduce FORT, a Framework of Shortcut-Resistant Training-Data Synthesis. FORT constructs shortcut-resistant training data by controlling shortcut risks across entity selection, evidence graph construction, question formulation, and adversarial refinement. Experiments show that FORT induces longer pre-answer search and fewer shortcut patterns than existing open-source deep search datasets. Using the resulting trajectories, we train FORT-Searcher with supervised fine-tuning (SFT) only, and it achieves the best overall performance among comparable-size open-source search agents on challenging deep search benchmarks. Relevant resources will be made available at this https URL.

---


### 194. [Debiasing Without Protected Attributes: Latent Concept Erasure from Textual Profiles](https://arxiv.org/abs/2606.12088)

**<font color=#1a73e8>作者：</font>** Shun Shao, Zheng Zhao, Anna Korhonen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Most fairness research in NLP assumes direct access to protected attributes such as gender, race, or nationality. In practice, however, such information is often unavailable due to privacy constraints, missing metadata, or legal restrictions, even though models may infer it from indirect textual cues. This raises a key question: can debiasing succeed without direct access to sensitive attributes? We propose H-SAL, which performs post-hoc concept and attribute erasure using self-description text as an implicit debiasing signal. To support this setting, we introduce a multi-domain Stack Exchange-based fairness benchmark for helpfulness prediction that includes both explicit and implicit signals, enabling comparison between standard debiasing with protected labels and debiasing without access to sensitive information. Across encoder and decoder-only language models, we find that implicit self-description often matches or outperforms explicit-label-based debiasing. Our results broaden representation-level fairness research and provide a new benchmark for studying debiasing under realistic data constraints.

---


### 195. [ISAP-3D: Identity-Slot Aligned Part-Aware 3D Generation](https://arxiv.org/abs/2606.12099)

**<font color=#1a73e8>作者：</font>** Junlin Hao, Haoshuai Fu, Xibin Song 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Part-aware 3D generation aims to synthesize structured objects with semantically meaningful components, yet often suffers from structural ambiguity due to identity-layout entanglement. Existing methods either infer part identity and spatial layout implicitly, which can lead to unstable part allocation (e.g., slot swapping or part merging), or rely on strong layout conditions that are difficult to obtain in practice. We attribute this ambiguity to identity-slot permutation freedom: without explicit identity-slot alignment, the correspondence between semantic parts and generation slots is not identifiable during training, allowing multiple slot assignments to fit the same supervision and leading to inconsistent decomposition. Based on this insight, we argue that stable part-aware generation requires identity-aligned one-to-one slot modelling. We therefore propose an identity-slot aligned framework, ISAP-3D, which anchors each part with semantic identity tokens and performs identity-conditioned one-to-one layout prediction, followed by layout-conditioned geometry synthesis. Structured local-global conditioning maintains identity alignment across semantic, spatial, and geometric stages. We also construct a part-level dataset with a unified semantic protocol to enable learnable and consistent identity-slot alignment. Extensive experiments demonstrate improved structural stability, controllability, and robustness over state-of-the-art part-aware generation baselines.

---


### 196. [A Riemannian Approach to Low-Rank Optimal Transport](https://arxiv.org/abs/2606.12120)

**<font color=#1a73e8>作者：</font>** Pratik Jawanpuria, Bamdev Mishra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank optimal transport (OT) mitigates the quadratic scaling of classical solvers, yet existing approaches rely heavily on first-order mirror-descent updates that require careful hyperparameter tuning and ignore the optimization landscape's curvature. To address these limitations, we propose a unified Riemannian geometric framework for low-rank OT, modeling balanced and unbalanced rank-$r$ positive factored couplings as novel smooth embedded submanifolds of the positive orthant. By equipping these manifolds with the Fisher-Rao product metric, we derive tractable formulations for Riemannian projectors, retractions, and Hessian-vector products. Our cost-agnostic framework seamlessly extends to linear OT, Gromov-Wasserstein (GW), fused GW, and their unbalanced counterparts. For balanced OT, our geometric ingredients are computed via efficient conjugate-gradient and iterative Bregman updates. For the unbalanced OT, our operations elegantly reduce to closed-form scalings, completely eliminating inner iterative loops. In both regimes, per-iteration complexity scales linearly with dataset size, and we provide a rank-sufficiency certificate for global optimality verification. Extensive experiments across a range of problem sizes demonstrate that our regularization-free first- and second-order solvers achieve faster convergence and superior performance over existing state-of-the-art low-rank OT solvers.

---


### 197. [AGE-MIL: Anchor-Guided Evidence Learning for Patient-Level Prediction](https://arxiv.org/abs/2606.12126)

**<font color=#1a73e8>作者：</font>** Jiawei Niu, Jian Chen, Di Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing computational pathology methods predominantly operate within whole-slide image (WSI)-level multiple instance learning (MIL) paradigms, while patient-level modeling remains underexplored. In routine pathological practice, however, pathologists derive diagnostic and prognostic conclusions by integrating evidence across multiple WSIs rather than relying on any single slide. This discrepancy creates a fundamental misalignment when patient-level supervision is directly imposed on conventional MIL frameworks, often leading to unstable optimization and degraded predictive reliability. To address this issue, we propose Anchor-Guided Evidence MIL (AGE-MIL), a weakly supervised framework for patient-level prediction. AGE-MIL constructs a patient-level anchor from slide representations to capture global pathological context and guide the retrieval and integration of diagnostically relevant local patches, enabling robust patient-level modeling. Patient-level risk is further modeled as an evidence accumulation process, promoting stable optimization under weak supervision. AGE-MIL is evaluated on six clinically relevant patient-level prediction tasks from two independent cohorts. Experimental results show that the proposed framework consistently outperforms eight state-of-the-art MIL methods. Code is available at this https URL.

---


### 198. [Unstable Features, Reproducible Subspaces: Understanding Seed Dependence in Sparse Autoencoders](https://arxiv.org/abs/2606.12138)

**<font color=#1a73e8>作者：</font>** Gleb Gerasimov, Timofei Rusalev, Nikita Balagansky 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) are widely used to interpret neural network representations, but their utility depends on whether the learned features are reproducible across training runs. We study this question through \emph{feature stability}: for each SAE feature, we estimate the probability that a similar feature reappears in an independently trained SAE. This yields a scalable per-feature signal that separates stable from unstable features. In a large-scale study across seeds, models, layers, dictionary sizes, and SAE variants, we find a pronounced functional asymmetry: stable features carry most of the reconstruction- and prediction-relevant signal, while unstable features have weak marginal impact and are dominated by low-frequency surface-form triggers in both activation statistics and automatic explanations. Geometrically, unstable features are individually non-reproducible but concentrate in reproducible lower-rank subspaces, suggesting that seed dependence often reflects basis ambiguity within a shared region of activation space rather than pure noise. A controlled synthetic model makes this mechanism explicit, showing that low-rank ground-truth features can be recovered at the subspace level while remaining non-identifiable as individual SAE latents across seeds. Finally, by pooling unique cross-seed features, we construct more stable SAEs while preserving explained variance in this setting. Together, these results show that unstable features are not merely failed or noisy latents: they have weak individual functional impact, but reflect reproducible low-dimensional structure that standard SAEs resolve differently across seeds.

---


### 199. [Time-Conditioned and Multi-Time Survival Prediction from 2D PET/CT Projections in Lung Cancer](https://arxiv.org/abs/2606.12140)

**<font color=#1a73e8>作者：</font>** Ashish Chauhan, Sambit Tarai, Elin Lundström 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate prediction of overall survival (OS) from positron emission tomography/computed tomography (PET/CT) can support personalized treatment and follow-up strategies in oncology. However, the impact of temporal modeling on imaging-based survival prediction remains insufficiently explored. We investigate how different temporal formulations influence survival prediction by developing two complementary approaches: Attention-guided Time-Conditioned Survival (ATCS) and Multi-Time Survival (MTS). We retrospectively analyzed pre-treatment PET/CT images from 848 patients with non-small cell lung cancer (NSCLC), including 556 for model development and 292 for held-out testing. A previously proposed Time-Conditioned Survival (TCS) model was used as a baseline. Models were trained using 5-fold cross-validation and evaluated on the test set using time-dependent area under the curve (AUC) at 6-month intervals from 0.5 to 5 years. Both ATCS and MTS outperformed the baseline TCS model, achieving mean AUCs of 0.794 and 0.793, respectively, compared to 0.767. ATCS performed better at earlier time points (0.5-3 years), whereas MTS performed better at later intervals (3.5-5 years). Combining tumor-specific and tissue-wise PET/CT features improved performance over either input alone. Finer temporal discretization improved short-term prediction, while coarser intervals provided more stable long-term estimates. These findings demonstrate that temporal modeling and input design influence PET/CT-based survival prediction. The proposed approaches enable time-specific survival estimation from pre-treatment imaging and may support improved risk stratification and clinical decision-making.

---


### 200. [PCA-Enhanced Adaptive NVAR Framework for High-Resolution Sea Surface Temperature Forecasting in the East Sea](https://arxiv.org/abs/2606.12141)

**<font color=#1a73e8>作者：</font>** Sherkhon Azimov, Susana López-Moreno, Eric Dolores-Cuenca 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate forecasting of sea surface temperature (SST) in regional seas such as the East Sea is crucial for monitoring marine ecosystems, assessing climate risks, managing fisheries, and conducting naval operations. Traditional numerical ocean models provide reliable predictions but are computationally expensive and often unsuitable for real-time forecasting. Many deep learning methods also struggle with high-dimensional spatiotemporal ocean data and experience error accumulation over longer forecasting periods. This study builds on our previously proposed Adaptive Next-Generation Reservoir Computing (Adaptive NVAR) framework, initially introduced and tested on synthetic dynamical systems, and extends it to ocean forecasting. We present a reduced-order forecasting framework that combines Singular Value Decomposition (SVD) with Adaptive NVAR to predict SST dynamics in the East Sea. SST fields are compressed into a low-dimensional representation using SVD, which extracts dominant modes of ocean variability. Adaptive NVAR models the temporal evolution of these latent states, and the predicted states are reconstructed into SST forecasts. We evaluate the framework using regional ocean datasets and compare it with the standard NG-RC/NVAR. Results show that Adaptive NVAR consistently achieves lower forecasting errors across multiple prediction horizons. In addition, SVD reduces computational complexity, resulting in a fast and scalable framework suitable for real-time ocean forecasting.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-248](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
