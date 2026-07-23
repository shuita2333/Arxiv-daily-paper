# 📦 其他研究 | 2026年07月24日

> 本类共 **192** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-192](./part-04.md)

---

### 51. [Agent-Centric Animal Pose Forecasting](https://arxiv.org/abs/2607.19548)

**<font color=#1a73e8>作者：</font>** Eyrun Eyjolfsdottir, Kristin Branson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding animal behavior at an algorithmic level -- what animals attend to, how they form internal models and plans, and how this maps to action -- remains a central challenge in neuroscience and ethology. Data-driven generative models offer a path toward this understanding. We introduce a framework for training agent-centric autoregressive models of animal behavior from tracked pose, applicable to single animals and to groups in which each agent senses and responds to its conspecifics. Our models input egocentric sensory observations and output egocentric movements, mirroring the biological constraint that animals observe and act on the world from their own reference frame. Social behavior emerges from agents independently sensing and responding to one another. This agent-centric formulation requires managing many parallel representations of the same data, along with ML-specific transformations like discretization. We release a general-purpose library focused on the composable sequences of operations that translate between these representations. We show that trained models capture the distribution of social behavior in groups of courting Drosophila, and our library includes quantitative tools for measuring fit. We demonstrate how the library supports systematic comparison across input and output representations and that it adapts straightforwardly to a new domain.

---


### 52. [CHMAS: A Coupled Hierarchical Framework for Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2607.19555)

**<font color=#1a73e8>作者：</font>** Dongming Wang, Jie Xu, Yanyu Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent reinforcement learning (MARL) systems face fundamental
challenges in balancing global coordination with local execution
across different temporal scales. This paper introduces the Coupled
Hierarchical Multi-Agent System (CHMAS), a novel framework that
decomposes multi-agent decision-making into centralized strategic
planning and distributed tactical execution with bidirectional
information flow. The strategic layer integrates all agents' states
with an exclusive global environmental state to generate guidance
actions every $T$ timesteps, while tactical agents execute
distributed policies augmented by strategic guidance and local
neighborhood observations. Unlike existing hierarchical approaches
with unidirectional control, CHMAS establishes a feedback mechanism
where accumulated tactical rewards influence strategic objectives
through a coupling coefficient $\lambda$, ensuring strategic plans
remain grounded in tactical feasibility. To address the
non-stationarity inherent in hierarchical learning, we propose an
asynchronous update protocol where strategic parameters update every
$N_f$ tactical episodes, allowing tactical policies to converge to
quasi-stationary points between strategic changes. We present both a
general bi-level formulation capturing full system dynamics and a
tractable additive approximation enabling rigorous analysis.
Theoretical analysis proves that this asynchronous scheme achieves
$\mathcal{O}(\log K/\sqrt{K})$ convergence for the strategic layer
after $K$ strategic updates under standard assumptions. Experimental
validation in a multi-agent foraging domain demonstrates successful
learning of spatially partitioned exploration strategies, with both
layers converging stably despite hierarchical coupling.

---


### 53. [On the Computational Complexity of Structural Generalization](https://arxiv.org/abs/2607.19573)

**<font color=#1a73e8>作者：</font>** Zichao Wei  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Structural generalization has been measured repeatedly by several benchmarks, yet it has never been formally defined. We give a definition that translates the two premises (compositional structure and unbounded generalization) into mathematical language. The definition itself is neutral: a compiler that hard-codes the rules satisfies it just as well. But structural generalization becomes a scientific question only insofar as the capacity can autonomously emerge from finite data. This question pits the computational lower bound $\mathrm{NC}^1$ against the learnable ceiling $\mathrm{TC}^0$ of pure Transformers. Under a Montagovian instantiation, each compositional rule splits into two projections: a syntactic face ($F_\gamma$) and a semantic face ($G_\gamma$). Tree evaluation on the $G_\gamma$ side is an instantiation of BFVP, which is $\mathrm{NC}^1$-complete (Buss, 1987). A pure Transformer must learn both faces at once, but Kraus et al. (2026) prove that its learnable class $\subseteq \mathrm{TC}^0$. Under the standard assumption $\mathrm{TC}^0 \neq \mathrm{NC}^1$, a pure Transformer cannot learn structural generalization. Neuro-symbolic systems achieve the best benchmark scores precisely because they inject $G_\gamma$, sidestepping the genuinely hard half. Benchmark scores cannot distinguish "learned" from "given." This is what this paper sets out to make clear.

---


### 54. [VQ-Transplant: Efficient VQ-Module Integration for Pre-trained Visual Tokenizers](https://arxiv.org/abs/2607.19575)

**<font color=#1a73e8>作者：</font>** Xianghong Fang, Yuan Yuan, Dehan Kong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vector Quantization (VQ) underpins modern discrete visual tokenization. However, training quantization modules for state-of-the-art VQ-based models requires significant computational resources which, in practice, all but prevents the development of novel, cutting-edge VQ techniques under resource constraints. To address this limitation, we propose {\bf VQ-Transplant}, a simple framework that enables plug-and-play integration of new VQ modules into frozen, pre-trained tokenizers by replacing their native VQ modules. Crucially, the proposed transplantation process preserves all encoder-decoder parameters, obviating the need for costly end-to-end retraining when modifying the quantization method. To mitigate decoder-quantization mismatch, we introduce a lightweight decoder adaptation strategy (trained for only 5 epochs on ImageNet-1k) to align feature priors with the new quantization space. In our empirical evaluation, we find that VQ-Transplant allows obtaining near state-of-the-art reconstruction fidelity for industry-level models like VAR while reducing the training cost by 95\%. VQ-Transplant democratizes quantization research by enabling resource-efficient integration of novel VQ techniques while matching industry-level reconstruction performance.

---


### 55. [End-to-End Differential Privacy in Training Deep Neural Network Classifiers](https://arxiv.org/abs/2607.19580)

**<font color=#1a73e8>作者：</font>** Huaiyuan Rao, Calvin Hawkins, Alexander Benvenuti 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Differentially private machine learning enables model training on sensitive data while ensuring that individual data is unlikely to be recoverable from the parameters of the resulting model. However, existing work often privatizes both training inputs and their labels, and these protections may be conservative when labels are public or can be safely made public. Therefore, in this work we propose a novel private training framework that instead privatizes training inputs while keeping labels public. We consider neural networks with softmax output layers, and thus the mapping from training inputs to the output of the softmax layer is a mapping onto the unit simplex. We randomize softmax outputs during training by applying the Dirichlet mechanism to enforce differential privacy for the training inputs, hence the ``end-to-end'' label. Because training data is reused across multiple training epochs, we use the notion of \Renyi differential privacy to formulate tight bounds on the strength of privacy provided by the Dirichlet mechanism across repeated uses. We show empirically that we attain new state-of-the-art accuracy when training from scratch on CIFAR10, MNIST, MedMNIST, FashionMNIST, and SVHN across all privacy budgets evaluated. Notably, when implementing $(\epsilon, \delta)$-differential privacy with $\delta=10^{-5}$, we improve the prior state-of-the-art accuracy from $78.37\%$ to $88.17\%$ at $\epsilon=4$ on CIFAR10, and our approach has $82.96\%$ accuracy even for $\epsilon=1$, which significantly outperforms prior work.

---


### 56. [Examining User Behavior and Cognitive Biases in Personal Password Security](https://arxiv.org/abs/2607.19586)

**<font color=#1a73e8>作者：</font>** Evelyn Crowe, Patralika Ghosh, Shreyas Kumar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Despite increasing awareness of cybersecurity risks, users continue to engage in insecure password practices, such as reusing passwords, choosing weak credentials, and neglecting security recommendations. The study explores the behavioral and cognitive factors that influence password decision-making by integrating insights from behavioral economics, particularly hyperbolic discounting, status quo bias, and present bias. We conducted a survey to analyze how people create, store and manage their passwords, examining whether security habits have improved over time in response to greater awareness. Our findings reveal that immediate convenience often outweighs long-term security considerations, leading users to prioritize memorability over strength. Additionally, we identify key psychological biases that contribute to security procrastination and resistance to adopting more secure authentication practices, such as password managers and multi-factor authentication. The study contributes to human-centered security by bridging the gap between security awareness and action, offering practical insights to design user-friendly authentication policies that align with real-world decision-making tendencies.

---


### 57. [Knowledge-Centric Self-Improvement](https://arxiv.org/abs/2607.19592)

**<font color=#1a73e8>作者：</font>** Xuefei Julie Wang, Lauren Hyoseo Yoon, Chengrui Qu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-improving AI systems typically treat the agent as the object that improves, by optimizing prompts, workflows, harnesses, or even the agent's own code. This agent-centric view can make improvements expensive to maintain and difficult to transfer, because gains become tied to a particular agent design, task distribution, or adaptation run. We study a complementary paradigm: knowledge-centric self-improvement, in which agents remain generic and disposable while the persistent object is a curated knowledge base that agents can leverage for future tasks. We conduct controlled case studies to operationalize this idea via a simple protocol. Agents attempt one task, then contribute evidence-grounded insights to a shared knowledge base via task-level and cross-task forums, followed by knowledge distillation. Because self-improvement is contained in the knowledge rather than the agent, improvement can be more inspectable, transferable, and portable. Across abstract reasoning, coding, and terminal benchmarks, this protocol improves solve rates while reducing dollar cost relative to agent-centric baselines. The resulting distilled knowledge also transfers to held-out tasks and across LLM families, indicating that the improvement is not merely an LLM- or run-specific behavior. These results support a new view of self-improving agentic systems: progress can be driven primarily by the curated persistent knowledge. Code is available at this https URL.

---


### 58. [The Mechanism Matters: When Knowledge Graphs Help Reinforcement Learning](https://arxiv.org/abs/2607.19616)

**<font color=#1a73e8>作者：</font>** Mohammed Sameer Syed  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge graphs (KGs) are widely used to inject prior knowledge into reinforcement learning (RL), yet the literature is dominated by single-domain, positive-result method papers, so we lack a systematic account of when KG structure helps an agent, when it is neutral, and when it hurts. We conduct a controlled study that independently varies the RL task, the injection mechanism (state features, action masking, or potential-based reward shaping), and KG quality. Using a synthetic, fully controllable KG over MiniGrid environments, we report three findings. First, on compositional sparse-reward tasks structured KG guidance improves sample efficiency and solve reliability (70% to 97% of seeds), and a shuffle control that permutes the KG's edges while preserving their count collapses the benefit toward baseline (masking p=0.0001; shaping p=0.006), so the gain is structural rather than generic regularization. Second, KG value scales with the amount of task-relevant knowledge the graph contains. Third, and most consequential, safety depends on the mechanism: soft, optimality-preserving injection benefits from correct knowledge and harmlessly ignores incorrect knowledge, whereas hard masking is brittle, forbidding essential actions when the KG is incomplete or corrupted and making a wrong KG worse than none. A UMLS-derived clinical case study on sepsis management under offline RL is a careful null, underscoring that benefits require task structure the chosen mechanism can exploit. Our results give practitioners concrete guidance on how, and how much, to trust a KG when using it to guide RL.

---


### 59. [EGRNet: A Lightweight Semantic Segmentation Network with Edge-Gated Refinement and Adversarial Sensing](https://arxiv.org/abs/2607.19617)

**<font color=#1a73e8>作者：</font>** Bareera Qaseem, Mohsin Kamal, Muhammad Naveed Aman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As autonomous systems and smart cities continue to evolve, the demand for efficient and robust scene understanding becomes increasingly critical. Semantic segmentation plays a key role in enabling autonomous vehicles to comprehend complex urban environments. However, achieving high accuracy with minimal computational cost remains a significant challenge. In this paper, we present Edge-Gated Refinement Network (EGRNet), a lightweight and efficient deep learning model designed for real-time semantic segmentation in urban scenarios. The model incorporates depthwise separable convolutions to reduce computational complexity and dilated residual blocks for capturing rich multi-scale contextual information. Additionally, we introduce a novel Edge-Gated Refinement (EGR) module, which adaptively fuses original and refined features through a learnable gating mechanism, enhancing boundary preservation and edge-sensitive regions. To further improve feature representation, Squeeze-and-Excitation (SE) attention is applied across the network. With only 0.46M parameters, EGRNet achieves state-of-the-art performance while maintaining low computational overhead. When evaluated on the Cityscapes dataset, the model attains a mean Intersection over Union (mIoU) of 65.28%, demonstrating strong accuracy with minimal resource consumption. Moreover, we introduce a lightweight adversarial attack detection strategy, ensuring robustness against adversarial inputs without compromising real-time performance. By combining efficiency, accuracy, and resilience, EGRNet is well-suited for deployment on edge devices in safety-critical real-time applications.

---


### 60. [SCPP: A Unified Python Library for Soft Clustering](https://arxiv.org/abs/2607.19620)

**<font color=#1a73e8>作者：</font>** Kiyan Rezaee, Morteza Ziabakhsh, Artin Bahrampour 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we present SCPP (Soft Clustering Python Package), an open-source Python framework for soft clustering. SCPP establishes a canonical, scikit-learn-compatible estimator interface that standardizes model training, prediction, membership representation, evaluation, and benchmarking across heterogeneous soft clustering methods, including fuzzy, probabilistic, graph-based, matrix factorization, and deep learning methods. The framework currently integrates 40 representative algorithms together with a comprehensive benchmarking comprising datasets, clustering quality metrics, and standardized runtime, memory, and scalability evaluation. SCPP further provides extensive documentation, practical examples, automated testing, and seamless integration with the scientific Python ecosystem, enabling reproducible experimentation and straightforward extension with new algorithms. The source code is publicly available at this https URL.

---


### 61. [Pathologist Attention-Aligned Report Generation for Prostate Histopathology](https://arxiv.org/abs/2607.19624)

**<font color=#1a73e8>作者：</font>** Ruoyu Xue, Suryakant Singh, Souradeep Chakraborty 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The allocation of visual attention by pathologists during cancer diagnosis is a highly selective process that critically shapes the information extracted from whole-slide images (WSIs). Human attention helps medical imaging tasks such as classification and segmentation, and becomes a strong semantic cue for identifying diagnostically informative regions for report generation. In this paper, we introduce human attention into the training of pathologist report generation models. To this end, we collected a multimodal human-attention dataset of 121 prostate WSIs annotated with pathologists' multi-scale viewport trajectories synchronized with the pathologists' verbal descriptions and cursor movements for five clinically relevant components (e.g., Gleason patterns). Using this dataset, we finetune two report generation models with an attention-alignment loss that regularizes the model attention over image patches to match the distribution of pathologist attention. We evaluate our approach on prostate cancer report generation and visual question answering using two models with different internal attention mechanisms (i.e., how image tokens are integrated into the language decoder). Experiments show average gains of 10.9% on NLP-based metrics and 19.3% in accuracy across five clinically relevant report components. Further, model attention maps extracted at inference time, with minimal computational overhead, align more closely with pathologist attention, providing stronger visual support for the generated reports by highlighting the regions that most influence the output.

---


### 62. [HypEMBER: Hypernetwork-based Ensemble for Robust Policy Learning of Parametrized Dynamical Systems](https://arxiv.org/abs/2607.19628)

**<font color=#1a73e8>作者：</font>** Nicolò Botteghi, Gabriele Pascali, Urban Fasel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work we investigate reinforcement learning (RL) as a framework for the robust control of parametrized dynamical systems in presence of measurements and model uncertainties. High-dimensional state spaces, expensive numerical solvers, the partial knowledge of the governing equations, and the dependence on physical parameters that may be uncertain or difficult to estimate accurately, make the use of standard RL approaches computationally unfeasible. Indeed, lack of robustness and poor generalization across parameter variations are further amplified in presence of noisy or incomplete measurements, ultimately hampering control performance. To address these challenges, we introduce HypEMBER, a novel RL framework based on the combination of hypernetworks and ensemble learning. In the proposed approach, both the policy and value functions are represented through hypernetworks that generate the weights of the underlying models conditioned on the physical parameters of the system, thereby enabling parametric generalization across different dynamical regimes. In addition, an ensemble of policy and value approximators is employed to quantify epistemic uncertainty, leading to improved exploration strategies and enhanced robustness during and after training. The performance of the proposed framework is assessed on two representative parametrized control problems: (i) the one-dimensional Kuramoto-Sivashinsky equation and (ii) a particle-navigation task in a two-dimensional time-dependent gyre flow, focusing on robustness with respect to measurement noise and parameter misspecification. Numerical results demonstrate that HypEMBER consistently improves training stability and sample efficiency, while achieving superior robustness to uncertainties affecting both the system dynamics and the available observations, in comparison with state-of-the-art RL methods.

---


### 63. [Anatomy of a Sound Neural Reasoner: One-Shot Amortization, First-Pass Poisoning, and Search Inertness in Clue-Rich Completion](https://arxiv.org/abs/2607.19635)

**<font color=#1a73e8>作者：</font>** Aleksey Komissarov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural solvers are built to deduce, branch, and revise intermediate states. The Lattice Deduction Transformer (LDT) appears to do exactly that. In clue-rich Sudoku, it does not: one forward pass commits essentially the entire grid (every blank cell on standard 6x6, 94-96% on augmented 9x9), turning the iterative solver into a one-shot predictor wrapped in an exact verifier. All hard-slice failures are decided before search begins, when the first pass confidently deletes a value required by the true solution. We call this first-pass poisoning. Adding learned branching, MRV, backtracking, value exclusion, and shared nogoods (CoLT) does not change which Sudoku instances are solved; it cuts repeated invalid derivations 1,497-fold. At the frozen training budget, constraint-graph attention alone matches full-CoLT accuracy, while positional tables recover only under substantially longer training, indicating an optimization and sample-efficiency advantage rather than an absolute capacity difference. The diagnosis predicts two effective interventions. Digit-permutation augmentation raises 9x9 accuracy from below 1% to 96.5 +/- 0.3 across three training seeds on a symmetry-disjoint split. Test-time union over symmetry-transformed passes raises all three hard-slice checkpoints from 72.8-78.9% to 100% without retraining. On from-scratch graph coloring, one-shot behavior disappears and search changes accuracy. In clue-rich completion, LDT-like systems are one-shot amortized predictors rather than learned search procedures: accuracy is determined by calibration and symmetry, while search primarily removes computational waste.

---


### 64. [Domain Shift in Echocardiography: Interpretable Quantification and Prediction of Cross-Dataset Left Ventricular Segmentation](https://arxiv.org/abs/2607.19643)

**<font color=#1a73e8>作者：</font>** Soroush Elyasi, Nasim Dadashi Serej, Julie Wall 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-dataset generalisation remains a major barrier to clinical deployment of echocardiographic left ventricular segmentation, yet the sources of this shift are rarely disentangled. We examined whether transfer degradation could be estimated before deployment using handcrafted ultrasound descriptors, VAE latent features, and segmentation-derived latent features across six echocardiographic datasets. Geometry-aware preprocessing substantially improved several poor transfer cases, suggesting that much of the apparent domain shift reflects field-of-view and framing inconsistencies rather than intrinsic acoustic differences alone. Intensity z-normalisation changed dataset separability by less than 0.005, indicating that brightness and contrast are not the dominant shift axis. Absolute Dice drop on held-out source-target pairs was predicted with an R-squared value of 0.612, an MAE of 0.082, and a Spearman rho of 0.681. The variant without LV and fan-shaped features retained approximately 70% of this explanatory power, supporting mask-free transfer-risk monitoring. The most informative discrepancy measure depended on the representation, with CMD strongest in z-normalised handcrafted features, with an absolute r of approximately 0.86 and an R-squared value of approximately 0.70; log-Wasserstein strongest in VAE space, with an r of approximately -0.90 and an R-squared value of approximately 0.81; and log-MMD strongest in LV-segmentation latent features, with an r of approximately -0.92 and an R-squared value of approximately 0.84. Apparent vendor effects were largely dataset-confounded. Echocardiographic domain shift is therefore structured and measurable, and its impact on segmentation can be partly reduced through geometry-aware preprocessing and anticipated using representation-specific transfer-risk estimation.

---


### 65. [Associations Between Support-Seekers' Cross-Community Interactions and Their Engagement with Received Comments in Online Health Communities](https://arxiv.org/abs/2607.19655)

**<font color=#1a73e8>作者：</font>** Shenghan Tan, Daiang Jia, Chunghiu Kong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Support-seeker' active engagement with received comments, e.g., showing positive sentiment and willingness to improve in the replies, can indicate the success of online health communities (OHCs). Their participation in other communities may correlate with their engagement in OHCs but remains under-explored. This paper analyzes 26, 725 seekers' behaviors in the other 40, 479 communities and their associations with seekers' engagement with received comments under their 78, 501 posts in 30 Baidu Tieba OHCs. We found that seekers primarily posted in other communities that are also health-related (25.3%), followed by those about games and entertainment (e.g., Dota, 20.8%). Seekers who posted in other communities about health (26.3%) or personal issues (e.g., saving money, 20.7%) before had relatively higher probabilities of subsequently posting in the 30 OHCs we identified, but this posting experience was associated with fewer replies and less expressed willingness to improve based on received comments. We provide insights into fostering seekers' engagement in OHCs based on cross-community interactions.

---


### 66. [A Unified Variational Framework for Deep Weakly Supervised Image Segmentation](https://arxiv.org/abs/2607.19669)

**<font color=#1a73e8>作者：</font>** Yin King Chu, Lingfeng Li, Sung Ha Kang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a unified variational framework for image segmentation under sparse pixel-level supervision. Our method is based on a simplex-constrained Potts model with a smooth perimeter regularizer, yielding a convex, smooth energy functional that can be used as a training loss in weakly supervised deep learning paradigms or optimized efficiently using iterative methods. Sparse labels are incorporated into the data fidelity term by constructing a fuzzy membership function via a function extension problem in a Reproducing Kernel Hilbert Space (RKHS), which can effectively capture inhomogeneous intensity statistics. The derived discrete loss for training standard networks demonstrates robustness and consistent improvements over non-training and partial cross-entropy (PCE) baselines in experiments, achieving comparable performance without requiring ground-truth segmentation images.

---


### 67. [Edge Intelligence in Civil Aviation: Paradigms, Techniques, and Applications](https://arxiv.org/abs/2607.19676)

**<font color=#1a73e8>作者：</font>** Wenbin Li, Zhongtian Liao, Bolin Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Civil aviation is safety critical and its operations, from flight decks and towers to ramps and maintenance, generate massive, heterogeneous data at the network edge. Yet cloud centric deployment of large Artificial Intelligence (AI) models often produces high task latency, lacks offline capability in communication denied environments, and requires centralizing sensitive data, raising privacy and sovereignty risks. Edge AI moves perception, prediction, and decision logic closer to the data producers via compression, collaborative inference, and split learning, thereby reducing latency, bandwidth, and exposure while enabling graceful operation during disconnections. This paper provides a panoramic view and a common understanding of edge intelligence tailored to civil aviation. We firstly articulate the operational motivations for edge AI, and then review recent techniques for edge inference and edge learning. We then introduce the organizational computing paradigms and the respective configurations in civil aviation environments; finally, we describe the emerging applications and the future research trends of edge intelligence in civil aviation. We argue that a refined edge solution can complement cloud foundations to deliver low latency, privacy preserving, and resilient AI services across the civil aviation lifecycle.

---


### 68. [Reference-Free Evaluation of Reasoning in Open-Ended Question Answering](https://arxiv.org/abs/2607.19678)

**<font color=#1a73e8>作者：</font>** Guneet Singh Kohli, Yuxiang Zhou, Michael Sejr Schlichtkrull 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI-generated answers in high-stakes domains are often fluent but difficult to verify, especially when they contain multi-step reasoning rather than a single final answer. We propose a reasoning-based, reference-free framework for auditing LLM-generated outputs. The method decomposes a generated reasoning trace into segments, labels local premise-target relations using Natural Language Inference (NLI), and organizes these relations into a hypergraph. A deterministic backward AND-OR search then assigns segment-level audit labels that indicate how each segment is grounded within the generated response. We evaluate the framework in two settings: deductive mathematical reasoning with Hard2Verify, and open-ended medical reasoning with UroReason, a new physician-annotated benchmark of LLM reasoning traces from real clinical cases. Across these settings, our NLI-hypergraph audit provides a more reliable reference-free evaluation signal than direct LLM-as-judge baselines. In the clinical setting, state-of-the-art LLM judges often fail to identify problematic reasoning segments, over-accepting fluent but weakly grounded responses. Our results show that QA evaluation should account for how inferential relations compose across a reasoning trace, rather than relying only on final answers or LLMs as verifiers. UroReason will be made available through an API, and our code will be released as open source.

---


### 69. [SLPO: Scaling Latent Reasoning via a Surrogate Policy](https://arxiv.org/abs/2607.19691)

**<font color=#1a73e8>作者：</font>** Runyang You, Zhiyuan Liu, Yongqi Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards has become the predominant recipe for eliciting test-time scaling in explicit Chain-of-Thought reasoners. Yet this scaling path remains computationally costly, since every intermediate step must be decoded as a language token. Latent reasoning instead carries intermediate computation as continuous vectors and already matches or surpasses explicit CoT at far shorter horizons. Despite this promise, latent reasoners remain largely imitation-bound, while explicit CoT has already moved past imitation via outcome-reward RL. Latent trajectories lack a tractable per-step likelihood and an adaptive stopping interface under fixed thinking budgets, so outcome rewards cannot elicit latent test-time scaling. We introduce Surrogate Latent Policy Optimization (SLPO) to bring outcome-reward RL to autoregressive latent reasoners: an empirical surrogate policy density over latent transitions for trajectory-level credit assignment, and a correctness-supervised stopping head that outcome-reward optimization refines into a variable-horizon policy. Across continuous and soft thinking settings, SLPO improves Pass@$k$ under parallel sampling and allocates longer latent computation to harder instances with higher deterministic accuracy.

---


### 70. [PhenSPINE: A Standardized Benchmark for Spine Pathology Diagnosis](https://arxiv.org/abs/2607.19696)

**<font color=#1a73e8>作者：</font>** Duong Ngoc Vu, Hai Son Nguyen, Trong-Nghia Nguyen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The accurate diagnosis of spinal pathologies depends heavily on radiological interpretation, yet automated systems are hindered by the lack of diverse, high-quality benchmarks. In this study, we present PhenSPINE, a Magnetic Resonance Imaging dataset comprising 16,813 images from 250 patients, curated to facilitate advanced deep learning research. We propose a robust diagnostic benchmark that integrates state-of-theart convolutional backbones with a Positional Encoding mechanism to explicitly model the anatomical context of intervertebral discs. Evaluating across four standard MRI sequences, our experiments demonstrate that the Sagittal T2-weighted sequence offers the most robust diagnostic value, achieving a superior Macro F1-score of 50.31%. We find that multisequence fusion strategies yield inferior performance compared to this single-sequence baseline, as the images across sequences in our dataset are significantly compromised by noise interference from surrounding anatomical regions. This work establishes a robust baseline and offers critical insights into sequence selection for spine analysis.

---


### 71. [SafeGen: Goal-Conditioned Video Diffusion of Safety-Critical Scenarios for VLM-Based Autonomous Driving](https://arxiv.org/abs/2607.19701)

**<font color=#1a73e8>作者：</font>** Jiangfan Liu, Zexuan Cui, Tianyuan Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> VLMs are increasingly deployed in AD systems, creating an urgent need for rigorous safety evaluation under rare yet safety-critical scenarios. Among these, interactions with vulnerable road users represent a major source of real-world failures. However, existing safety-critical scenario generation methods predominantly rely on simulator-based pipelines, which suffer from a substantial sim-to-real gap and often fail to capture realistic, diverse, and unforeseen human-vehicle interaction dynamics. We present SafeGen, a goal-conditioned diffusion framework for safety-critical scenario generation in VLMADs. Our key insight is to formulate scenario generation as a goal-conditioned diffusion process, where a predefined catastrophic end-state serves as a strong supervisory signal, guiding the generation of temporally coherent video trajectories that naturally evolve toward safety-critical outcomes. Building on this formulation, we introduce Context Grounded End State Reasoning, which leverages VLMs to analyze benign driving contexts and infer latent vulnerabilities in human-vehicle interactions, producing structured end-state specifications that induce high-risk scenarios. Conditioned on these targets, we further propose End State Conditioned Video Evolution, which grounds semantic threats into physically plausible visual dynamics. Specifically, we instantiate high-risk agents within the scene via depth-aware geometric projection, followed by boundary-conditioned diffusion to generate intermediate frames with consistent motion patterns and temporal coherence. Extensive experiments across 3 VLMADs demonstrate that SafeGen increases the Judge Overall Score, a metric using a VLM judge to evaluate VLMADs' understanding and decision-making, by 24.25% on average compared to SoTA baselines. Furthermore, fine-tuning a VLMAD improves performance in real-world driving scenes by an average of 15.9%.

---


### 72. [A Unified Tokenization Framework for Pain Recognition using Heterogeneous 3D Modalities](https://arxiv.org/abs/2607.19716)

**<font color=#1a73e8>作者：</font>** Stefanos Gkikas, Christian Arzate Cruz, Valentina Becchetti 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pain is a complex and pervasive phenomenon affecting a large percentage of the population, and accurate assessment is essential for effective clinical management and intervention. Computational pain recognition systems enable continuous monitoring, support clinical decision-making, and help mitigate pain-related distress and functional decline. This study introduces a unified tokenization framework for heterogeneous 3D modalities in pain recognition that provides a single processing pipeline across behavioral and brain-activity 3D data, without requiring separate architectures for each modality or handcrafted inductive biases. The framework preserves spatial, temporal, and time--frequency structure while mapping diverse inputs into a shared token space. Extensive experiments show that the proposed approach effectively processes facial videos and fNIRS data in both raw-signal and spectrogram-based representations. On the AI4Pain benchmark dataset, the proposed framework achieves state-of-the-art performance while maintaining high computational efficiency and enabling real-time assessment on both GPU and CPU hardware.

---


### 73. [Lightweight Person-Place Relation Extraction from Historical Newspapers with Dependency Graphs and Proximity Features](https://arxiv.org/abs/2607.19718)

**<font color=#1a73e8>作者：</font>** Mlen-Too Wesley  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The HIPE-2026 shared task introduces person-place relation extraction from multilingual historical newspapers as a new evaluation track, classifying the at and isAt relations between pre-annotated person and location mentions in English, French, and German. Motivated by the cost of processing historical archives at scale, our team (DS@GT HIPE, team 2 in the official results) investigates how far a lightweight, interpretable system can go without any pretrained language model at the relation classification stage. Our approach builds a document-level graph from dependency parses, extracts proximity-based and part-of-speech features for each entity pair, and classifies them with small scikit-learn ensembles or compact Graph Attention Networks, keeping every submitted run under 847K parameters. On the official evaluation (Test A, the newspaper test set), our best run reached a macro recall of 0.5142, ranking 3rd on the Efficiency profile while placing mid-table on Accuracy among the 17 participating teams. Two findings stand out. First, minimum character distance alone captures most of the classification signal; adding further engineered features yields inconsistent gains and sometimes degrades performance, echoing prior evidence that argument distance dominates relation extraction. Second, document-grouped cross-validation is essential on this corpus: pair-level splits inflate scores by 25-37 percentage points because entity mentions recur across documents, a data-leakage effect that grouped cross-validation removes.

---


### 74. [Koopman Dreamer: Spectrally Constrained Latent Dynamics for Stable World-Model Imagination](https://arxiv.org/abs/2607.19719)

**<font color=#1a73e8>作者：</font>** Jiaqi Li, Xinglong Zhang, Haibin Xie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent world models improve sample efficiency in continuous control by optimizing policies over imagined latent trajectories, but common neural transitions offer limited direct control over modal persistence and error accumulation in long rollouts. We propose Koopman Dreamer, a Dreamer-style world model with a spectrally constrained deterministic latent dynamics core. Its Koopman-inspired backbone uses two-dimensional rotation--scaling blocks with bounded radii to represent damping, rotation, and near-periodic modes. Linear and low-rank bilinear action terms capture global and state-dependent control effects, while stochastic-state modulation supplies local correction information. To reduce the mismatch between posterior-conditioned training and prior-only imagination, the model combines posterior-conditioned EMA teacher targets with one-step consistency, multi-step rollout, and open-loop observation-prediction objectives. We further derive a multi-step rollout-error bound that separates amplification by the spectral backbone and bilinear interaction from the additive effects of stochastic-state mismatch and modeling residuals, clarifying the trade-off between error attenuation and long-term information retention. Experimental results on proprioceptive continuous-control tasks from the DeepMind Control Suite and UAV-LiDAR autonomous navigation demonstrate that Koopman Dreamer improves the stability of long-horizon latent rollouts and achieves stronger closed-loop control performance on tasks that rely on high-quality multi-step imagination.

---


### 75. [ReFace: Reorganizing Facial Spatiotemporal Representations for Improved Pain Assessment](https://arxiv.org/abs/2607.19722)

**<font color=#1a73e8>作者：</font>** Stefanos Gkikas, Yu Fang, Christian Arzate Cruz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic pain assessment from facial video remains challenging due to the spatial heterogeneity of pain-related facial cues. This study proposes ReFace, a spatial reorganization pipeline that divides facial input into four spatial quadrants before tokenization, rather than processing the entire face as a single region. Evaluated on the AI4Pain dataset, the proposed approach achieves $56.00\%$ accuracy on the test set using video only, achieving the highest reported accuracy under the fixed AI4Pain benchmark protocol among the compared methods. Notably, the four-quadrant configuration processes the same total pixel budget as the full-face input, yet achieves higher accuracy, suggesting that spatial reorganization can improve performance under the proposed tokenization design. A single quadrant region, processing just one quarter of those pixels, remains competitive at a fraction of the computational cost.

---


### 76. [Analytic Distribution of Classifier-Free Guidance for Schedule Design](https://arxiv.org/abs/2607.19725)

**<font color=#1a73e8>作者：</font>** Enze Jiang, Zheng Ma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classifier-free guidance (CFG) is the default mechanism for conditional generation in diffusion models, but the distribution sampled by its deterministic guided dynamics is not captured by the usual product-distribution heuristic $p_0^\omega q_0^{1-\omega}$. We analyze CFG through the probability flow ODE and derive exact analytic path-integral representations of the induced distributions for both constant and time-dependent guidance. The resulting formulas show that CFG modifies $p_{t_0}$ by an exponential path-integral correction, and that a time-dependent schedule enters this correction through the weight $\omega(t)-1$. This characterization explains how score discrepancies accumulate along sampling trajectories and motivates Distribution-Guided CFG (DG-CFG), a schedule that balances timestep contributions while accounting for signal strength and low-noise score-error amplification. A toy model with analytic scores closely verifies the predicted distributions. On Stable Diffusion~1.5, DG-CFG improves generation and yields a stronger diversity--fidelity trade-off across guidance strengths, with especially clear gains when strong guidance causes saturation and quality degradation in constant and heuristic schedules. Across NFE budgets, DG-CFG reaches fixed image-quality targets with fewer sampling steps, reducing the sampling cost needed to achieve target metrics.

---


### 77. [An Exploratory Analysis of Pain Localization via Explainable Computational Modeling](https://arxiv.org/abs/2607.19726)

**<font color=#1a73e8>作者：</font>** Ioannis Kyprakis, Stefanos Gkikas, Eric Nichols 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic pain localization, which involves identifying the anatomical origin of pain from peripheral physiological signals without patient self-report, is a clinically critical but largely unaddressed problem, particularly for non-verbal patients. This paper presents a systematic comparison of classical feature engineering and deep sequence learning for subject-independent three-class pain localization using the AI4Pain 2026 Challenge dataset, which comprises four synchronously recorded wearable modalities: electrodermal activity, blood volume pulse, respiration, and peripheral oxygen saturation recorded from 65 participants under controlled TENS-induced pain. A 115-dimensional hand-crafted feature set spanning time-domain, frequency-domain, modality-specific, and cross-modal descriptors is benchmarked against end-to-end deep architectures. Extremely Randomized Trees achieves the highest macro-F1 of 0.539, outperforming the best deep model by 7.4 percentage points, with EDA spectral features emerging as the dominant discriminators. A consistent 26-point gap between pain detection (F1\,=\,0.815) and localization (F1\,=\,0.552) across all models points to a fundamental ceiling imposed by the anatomical diffuseness of peripheral autonomic pathways at 10-second resolution.

---


### 78. [Efficient Tracking and Understanding Object Transformations](https://arxiv.org/abs/2607.19743)

**<font color=#1a73e8>作者：</font>** Yihong Sun, Bharath Hariharan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tracking objects through state transformations is essential for understanding real-world dynamics. However, existing methods are computationally expensive. TubeletGraph recently showed impressive capabilities, but its inference cost (~$4.4$ seconds per object-frame on VOST) precludes any real-time deployment possibilities. We observe that TubeletGraph's overhead arises from building a spatiotemporal partition of the input video: (1) entity segmentation is computed densely for every frame regardless of whether a transformation occurs, and (2) every entity in the scene is tracked, scaling cost with scene complexity rather than the number of transformations of interest. To address both, we propose FluxGraph, a reactive variant that uses SAM2's internal multi-mask disagreement as a lightweight trigger for transformation detection, and removes the need for tracking all entities in the given video. FluxGraph is ~$3.3\times$ faster than TubeletGraph on VOST while improving tracking performance and preserving state graph quality. Furthermore, we also observe consistent speedups of $3.7-10.7\times$ across VSCOS, M$^3$-VOS, and DAVIS17 while maintaining performance. Code is publicly available at this https URL.

---


### 79. [Beyond Relevance-Centric Retrieval: Rubric-Oriented Document Set Selection and Ranking](https://arxiv.org/abs/2607.19747)

**<font color=#1a73e8>作者：</font>** Kailin Jiang, Lei Liu, Jian Xi 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models and AI agents become the primary consumers of search results, document set quality determines the upper bound of downstream generation. Yet existing evaluation systems remain confined to scoring documents independently and aggregating via nDCG, ignoring inter-document interactions (redundancy, conflict, complementarity) and unable to answer what makes one document set better than another. To address these issues, we propose a complete evaluate-diagnose-optimize framework. We design SetwiseEvalKit, a three-level, nine-dimension document set evaluation benchmark covering both short-form and long-form scenarios, comprising approximately 28K high-quality evaluation rubrics. We systematically evaluate 12 rerankers: even the best method achieves no more than 45% coverage, cross-document coordination dimensions are universally weak, and no single method maintains top performance across both settings. Building on this, we propose Rubric4Setwise, a training-free method that converts rubric-based evaluation criteria into document set selection signals, achieving the best downstream generation performance with fewer documents and search rounds. It is the only method that maintains state-of-the-art results across both scenarios, validating the effectiveness of closing the loop from evaluation to optimization.

---


### 80. [Learning the Arabic Dialect Continuum as a Continuous Space: A Regression Approach to Speaker Origin Prediction](https://arxiv.org/abs/2607.19751)

**<font color=#1a73e8>作者：</font>** Mohamed Aziz Khadraoui, Adel Ammar, Bilel Benjdira 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a regression-based approach to Arabic dialect geolocation that models dialectal variation as a continuous geographic space rather than discrete categories. Speaker origin is predicted as continuous latitude-longitude coordinates using a hierarchical neural architecture that fuses frame-level XLS-R-300M and Whisper-large-v3 encoder representations with phonotactic descriptors through a Transformer encoder and a learnable attention-pooled query. A spherical geodesic loss directly optimizes great-circle distance on Earth's surface, avoiding distortions inherent to planar coordinate regression. Under a leakage-free 5-fold GroupKFold protocol grouped by source recording, our model attains a pooled median localization error of 481.2 km. Auxiliary country and city heads reach 64.5% and 45.2% accuracy, respectively. A permutation Mantel test on the learned latent space provides quantitative support for the Arabic dialect continuum hypothesis. To probe true generalization, we further introduce a city-masking protocol in which two cities per fold are removed from training but retained in validation. Under this zero-shot regime, the mean error rises to 1173.3 km, a 1.32x degradation relative to seen cities. Our findings establish continuous geographic modeling as a principled framework for Arabic dialect geolocation and quantify both its strengths and the substantial headroom that remains.

---


### 81. [Convergence-Latency-Aware Adaptive Modulation and Resource Allocation in RIS-Assisted Wireless Federated Learning](https://arxiv.org/abs/2607.19759)

**<font color=#1a73e8>作者：</font>** Liwei Wang, Wen Chen, Jun Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) over wireless networks suffers from significant training latency and degraded convergence due to unreliable wireless transmission, especially under blocked propagation environments. Although reconfigurable intelligent surfaces (RISs) can improve communication reliability, existing wireless FL studies rarely characterize the trade-off between learning convergence and communication delay under modulation-dependent transmission errors. In this paper, we consider a wireless FL system operating under RIS-assisted blocked-link propagation scenarios, and focus on adaptive modulation and sub-channel allocation for convergence-latency aware communication design. By characterizing the effect of symbol errors on uploaded local gradients, we derive a convergence-related upper bound that reveals the impact of symbol error rate (SER) on FL loss decay. Based on this result, we formulate a joint convergence-latency optimization problem, which is cast as a mixed-integer nonlinear programming (MINLP) problem, and solve it using a low-complexity hybrid alternating optimization framework. Extensive experiments on MNIST, CIFAR-10, and Speech Commands show that the proposed scheme consistently achieves faster convergence and higher test accuracy than existing adaptive communication schemes, especially in complex tasks and challenging wireless scenarios.

---


### 82. [Extending a Large View Synthesis Model for Multi-view Panoptic Segmentation](https://arxiv.org/abs/2607.19765)

**<font color=#1a73e8>作者：</font>** Kwonyoung Ryu, In-Jae Lee, Jonghyun Jin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large view synthesis models synthesize novel views through cross-view attention without explicit 3D representations, and recent studies have shown that they learn accurate spatial correspondence from RGB supervision alone. We observe that this correspondence generalizes beyond appearance. When non-photorealistic signals such as binary encoded panoptic labels are passed through the model, they are propagated to novel views with consistent spatial structure. These results indicate that the correspondence learned for RGB view synthesis can also propagate view-independent per-pixel labels. From this observation, we present the first work to extend large view synthesis models beyond appearance rendering to 3D scene understanding. We propose a panoptic segmentation pipeline that reuses a frozen view synthesis model to propagate panoptic labels from input views to novel views, without 3D reconstruction or any segmentation-specific training of the view synthesis model. Given panoptic labels on the input views, we encode them into binary channel representations and pass them through the same model to render target-view segmentation. On ScanNet, our method achieves segmentation quality on par with Gaussian based approaches requiring explicit 3D reconstruction, while outperforming them in novel view synthesis by more than 7 dB. The label propagation also transfers across datasets, surpassing these approaches on Replica without any fine-tuning.

---


### 83. [Global Building Area Estimation Products: How Accurate Are They?](https://arxiv.org/abs/2607.19766)

**<font color=#1a73e8>作者：</font>** Saad Lahrichi, Doa'a Allabadi, Kyle Bradbury 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geo-spatial rasters of building footprint area are useful for a variety of tasks, such as monitoring urbanization, improving energy efficiency, and tracking greenhouse gas emissions. There are now multiple global building raster datasets, however there lacks an independent, comprehensive, and fair assessment of their accuracy. In this work, we evaluate the accuracy of four major global building products: Global Human Settlement Layer (GHSL), Microsoft's TEMPO (TEMPO), The Global Building Atlas (GBA), and Overture. As ground truth for assessing their accuracy, we use ORBITaL-Net, a globally diverse dataset of manually labeled building footprints. To ensure fairness, we evaluate products on grids of multiple spatial resolutions, and several conventional performance metrics. Our results indicate that either GBA or TEMPO generally achieves the highest overall accuracy, depending upon the particular evaluation criteria. We also stratify the accuracy of each product by several factors: geographic location, population density, and income groups. The results reveal that product accuracy can sometimes vary significantly with respect to these factors. Notably, all products are significantly less accurate in Africa and Asia. Most products also suffer significant accuracy reduction in high-density urban areas.

---


### 84. [An Isotropy-Preserving Spectral Cap for Muon: Theory and Three Case Studies](https://arxiv.org/abs/2607.19771)

**<font color=#1a73e8>作者：</font>** Jiachun Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon and related matrix-sign optimizers are increasingly used to pre-train large language models, but their effect on the internal geometry of individual weight matrices is not well understood. This preliminary report proposes a unified framework built on a single idealizing assumption -- exact scale invariance of the loss under weight rescaling, which holds approximately in normalization-heavy networks. Under this assumption, plain SGD carries a built-in 1/||W|| brake on its update size, whereas Muon's matrix-sign step removes that brake, so both the Frobenius and spectral norms drift outward faster (t^{1/2} versus t^{1/4}). We further observe that the spectral-norm perturbation has a non-negative second-order term. This implies that a lightweight "spectral cap" -- which projects out only the first-order growth of the single top singular direction from each update -- can control the output covariance W K_X W^T without freezing training: the weight keeps learning through non-top directions, top-direction rotation, and top switching. We relate this cap to the min-entropy (H-infinity) of the singular-value spectrum. We then study three systems trained with Muon: a nanoGPT feed-forward projection, a 64-expert mixture-of-experts router, and the query/key projections of a bf16 FlashAttention block. In each case the cap increases isotropy and, at the margins -- a router collapsing to a single expert, and the near-divergence of one attention head -- prevents a concrete failure, while leaving validation loss essentially unchanged. We emphasize that the scale-invariance assumption is strong and that these small-scale results are preliminary; comments are welcome.

---


### 85. [DRGBT-1K: A Large-scale High-quality Benchmark for Dynamic RGBT Tracking](https://arxiv.org/abs/2607.19772)

**<font color=#1a73e8>作者：</font>** Zhaodong Ding, Chenglong Li, Zeyu Ding 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic RGBT (DRGBT) tracking aims to continuously localize a target when the available sensing modalities and observation platforms vary over time. Compared with conventional RGBT tracking with fixed RGBT inputs and a fixed observation platform, DRGBT tracking is more consistent with real-world collaborative perception systems, where targets may be observed by heterogeneous sensors from different viewpoints. However, existing benchmarks are still insufficient for systematically evaluating tracker robustness under real dynamic modality variations and cross-platform transitions. To address this limitation, we make the following contributions. 1) We construct DRGBT-1K, a large-scale high-quality benchmark for DRGBT tracking. It contains 1,045 sequences captured entirely in real-world scenarios and 795K RGBT frame pairs collected using UAVs and handheld RGBT devices, encompassing diverse real-world scenes, pronounced viewpoint changes, modality variations, and target appearance discontinuities. 2) We provide comprehensive annotations for fine-grained evaluation, including dense bounding boxes, target category labels, challenge attributes, frame-level modality labels and platform labels. DRGBT-1K covers 24 target categories, more than 15 scene types and 15 challenge attributes. 3) We establish a comprehensive benchmark by evaluating 20 representative multimodal tracking methods, including conventional RGBT trackers, modality-missing RGBT trackers, and DRGBT trackers under a unified evaluation protocol. 4) We release an unaligned version of DRGBT-1K and derive UGVT-1K to support broader research on unaligned multimodal tracking and UAV-ground collaborative tracking. 5) We develop an online evaluation platform for DRGBT-1K and provide a leaderboard that collects all methods evaluated on this benchmark.

---


### 86. [Frequency-Hierarchical Active k-Space Sampling for Diagnostic MRI](https://arxiv.org/abs/2607.19779)

**<font color=#1a73e8>作者：</font>** Ruru Xu, Kian Anvari Hamedani, Zhikai Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Active sampling for accelerated MRI must distribute a tight sampling budget across spatial frequencies that carry very different kinds of information. Low frequencies hold most of the anatomical context; high frequencies carry the fine details that drive pathology assessment. Existing active samplers either treat both regions identically or restrict the action space to entire Cartesian rows, which forces a poor compromise at high acceleration. We propose HieraSample, a task-driven framework built around this hierarchy. A cosine-annealed curriculum lowers the acceleration factor from 20x to 4x across 80 acquisition steps while keeping a fully-sampled low-frequency disk at every step; a Mamba-based policy then picks individual high-frequency coordinates from features extracted by dual disease and severity classifiers. The reward is the per-sample reduction in class-weighted cross-entropy after each action, so a positive reward corresponds directly to a more confident correct prediction. On the fastMRI+ knee benchmark, HieraSample matches the fully-sampled oracle on ACL diagnosis from 4x to 10x acceleration, and improves on a recent Cartesian baseline by as much as 20.4 AUC points on ACL severity.

---


### 87. [WASABI: Whole-graph Assignment-based Stabilizer for lAne topology By Inter-frame tracking](https://arxiv.org/abs/2607.19781)

**<font color=#1a73e8>作者：</font>** Tetsuhiro Uchida, Myu Sasaki, Kensho Nakajima 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous driving requires understanding the road as a graph of drivable lanes and their connectivity, beyond the ego lane alone, to follow routes through intersections and reason about cross- and merging-traffic. Recent perception models infer such lane topology, i.e., lane segments together with their inter-lane connectivity (LCLC), from onboard sensors over a 360-degree BEV view. Due to neural perception's imperfections, their outputs retain structural instabilities such as missed detections, lost or incorrect LCLC, over-detection, and label flicker. This paper presents WASABI, a real-time post-processing pipeline that stabilizes lane topology outputs both within and across frames by treating lane segments and their LCLC connectivity as joint tracking targets, under onboard real-time constraints (10 Hz / 20 ms / up to 200 input lanes). The pipeline integrates segment tracking with connectivity, noise-robust topology-aware refinement, and a resource-constrained real-time design. On internal validation data (16 sequences), WASABI improves LCLC detection F1 from 0.834 to 0.948 (+0.114, +13.6%) and reduces centerline lateral error from 2.50 m to 0.95 m, while reducing detection false-positives by 24.6%. Temporal-stability metrics on the same data show LCLC toggle rate reduced by 63.3% and boundary-label flicker rate by 30.2%, confirming across-frame stabilization beyond per-frame accuracy.

---


### 88. [Physics-Aware Complex-Valued State Space Model with Scattering-Prior Feature Modulation for PolSAR Image Classification](https://arxiv.org/abs/2607.19787)

**<font color=#1a73e8>作者：</font>** Fangyan Zhang, Fan Zhang, Shiqi Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Polarimetric synthetic aperture radar (PolSAR) image classification is a representative task for physics-aware GeoAI, where land-cover semantics are closely coupled with electromagnetic scattering mechanisms. Many existing complex-valued networks can preserve amplitude-phase information, but they are often limited in long-range spatial dependency modeling and usually incorporate polarimetric priors only as input-level or shallow auxiliary features. As a result, physical knowledge is insufficiently used to guide deep feature evolution. To address this issue, this paper proposes CV-SSMNet, a physics-aware complex-valued state-space network with scattering-aware feature modulation for PolSAR image classification. The proposed method builds a complex-valued state-space model (CV-SSM) in the original complex domain to capture long-range spatial dependencies while preserving polarimetric amplitude-phase coupling. Meanwhile, seven physically meaningful scattering priors, are encoded as FiLM-style modulation signals to adaptively recalibrate complex-valued representations during feature evolution. CV-SSMNet further integrates multi-scale complex convolutions, branch-wise CV-SSM encoding, prior-guided recalibration, and lightweight global context aggregation, enabling physically guided representation learning from local scattering structures to global spatial context. Experiments on three L-band benchmark datasets and an additional P-band BIOMASS evaluation demonstrate that CV-SSMNet achieves competitive accuracy, improved regional consistency, and better boundary preservation, supporting the effectiveness of embedding polarimetric scattering mechanisms into complex-valued long-range GeoAI representation learning.

---


### 89. [Mammal: Supporting Breastfeeding Monitoring Through Computational Garments with Inter-Body Sensing](https://arxiv.org/abs/2607.19796)

**<font color=#1a73e8>作者：</font>** Yanfeng Zhao, Morgan Geck, Kate Fernandez 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Breastfeeding provides critical insight into infant feeding competence and physiological health, yet objective monitoring remains difficult due to the intimate and internal nature of feeding. We present Mammal, a caregiver-worn computational garment that unobtrusively monitors breastfeeding without attaching sensors to the infant. Mammal leverages inter-body signal transmission through natural mouth-to-breast contact to capture infant cardiac and feeding-related acoustic signals on the caregiver's body. Using novel algorithms to detect latch onset, infer infant electrocardiogram (ECG), and identify suck and swallow events from inter-body signals, Mammal estimates latch duration, in-feeding heart rate, suck-swallow-breathe (SSB) ratio, and milk intake. In a user study with 10 caregiver-infant dyads, Mammal achieves a mean absolute percentage error (MAPE) of 5.56% for latch duration, a mean absolute error (MAE) of 3.61 bpm for infant heart rate estimation, a mean absolute error of 0.12 for SSB ratio estimation, and a mean relative error of 15.76% for milk intake, with participants reporting high comfort and wearability.

---


### 90. [OPIUM: Mitigating Steering Externalities and Over-Refusal via Dual Objective Latent Optimization](https://arxiv.org/abs/2607.19806)

**<font color=#1a73e8>作者：</font>** Kavin Aravindan, Arihant Rastogi, Aadi Prasad 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation steering provides a lightweight mechanism for controlling large language models at inference time, but steering vectors can have unintended externalities: utility vectors may weaken safety behavior, while refusal vectors may induce over-refusal on benign prompts. We introduce OPIUM (Optimizing Protected Injections via Utility Manifolds), a training-free method for sanitizing steering vectors through representation matching. Given reference behaviors on two prompt sets, OPIUM optimizes a new steering vector that preserves the downstream representations induced by the desired intervention while matching a safer reference behavior on prompts where the original vector fails. Across steering-externality and over-refusal settings, OPIUM improves the safety--utility tradeoff relative to vanilla steering and directional ablation, suggesting that harmful side effects of activation steering can often be mitigated directly in activation space.

---


### 91. [Lean-SAM2: Target-Anchored Memory and Encoder Acceleration for SAM2](https://arxiv.org/abs/2607.19811)

**<font color=#1a73e8>作者：</font>** Xudong Ouyang, Wenlun Zhang, Yimin Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The Segment Anything Model 2 (SAM2) has advanced temporal promptable segmentation, yet its deployment remains hindered by heavy memory cross-attention overhead and redundant full-frame visual feature extraction. While recent methods explore efficiency via heuristic memory pruning and window-based sparse routing, they typically suffer from catastrophic performance degradation in complex segmentation scenarios replete with occlusions and distractors. To resolve these limitations, we propose \textbf{Lean-SAM2}, a holistic lightweight framework designed to address the above vulnerabilities while systematically eliminating computational redundancies. Specifically, Lean-SAM2 integrates three collaborative mechanisms: (1) Target-Anchored Memory Pruning (TAMP) safeguards target tokens against deceptive attention by modulating raw attention significance with semantic consistency against prompt-derived foreground anchors; (2) Temporal Condensation with Insurance Memory (TCIM) condenses historical context via a visibility-gated fusion while conditionally archiving high-confidence entries in a parallel insurance bank; and (3) Target-Anchored Risk-Aware Routing (TARR) selectively activates the heavy image encoder for target-related windows based on anchor similarity, utilizing a risk-aware fallback policy to trigger full-frame refreshes during volatile transitions. Extensive evaluations across multiple challenging benchmarks demonstrate that Lean-SAM2 establishes a superior balance between accuracy and efficiency. For example, on the LVOSv2 validation dataset, Lean-SAM2 achieves overall inference speedups of $1.412\times$ and $1.417\times$ on the SAM2.1-Large and SAM2.1-Base+, respectively, significantly outperforming Efficient-SAM2 while boosting the corresponding $\mathcal{J}\&\mathcal{F}$ scores by $5.0\%$ and $3.6\%$. Code is available at this https URL.

---


### 92. [MoAKE: Toward Unified All-in-One Action Quality Assessment via Mixture of Action Knowledge Experts](https://arxiv.org/abs/2607.19826)

**<font color=#1a73e8>作者：</font>** Huangbiao Xu, Huanqi Wu, Xiao Ke 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Action Quality Assessment (AQA) aims to objectively evaluate performance quality from action videos. Most existing methods follow a ``one-by-one'' paradigm, training a separate model for each action type. This setting limits real-world deployment, as it requires prior action-type knowledge to select the corresponding model and suffers from poor generalization across diverse actions. To address these limitations, we study the challenging task of all-in-one AQA, which aims to assess heterogeneous actions within a single unified model. We propose a novel Mixture of Action Knowledge Experts (MoAKE) framework, designed to mitigate negative knowledge transfer caused by large semantic discrepancies among actions. MoAKE learns complementary experts that capture diverse action patterns within a shared semantic space and dynamically aggregates their knowledge to adapt the assessment to the input action. Each expert is tailored with segment-aware prototypes to handle varying temporal lengths, together with an Adaptive Intra- and Inter-Segment Relationship Modeling (AIISRM) module to model multi-granularity temporal dynamics. Furthermore, we establish comprehensive benchmarks for all-in-one as well as zero/few-shot AQA. Extensive experiments on three long-term datasets demonstrate that MoAKE significantly outperforms existing methods in the all-in-one setting, while also achieving consistent generalization on three short-term datasets under zero/few-shot evaluation. Code is available at this https URL.

---


### 93. [Know Your Agent: Reconnaissance-Driven Pentesting of AI Agents](https://arxiv.org/abs/2607.19837)

**<font color=#1a73e8>作者：</font>** Or Zion Eliav, Eyal Lenga, Shir Bernstien 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Traditional pentesting uses reconnaissance at each step to uncover unseen weaknesses, build stronger attacks, and advance the objective; we argue that AI agents require the same treatment. We formalize agent reconnaissance by modeling the process and identifying the knowledge assets it seeks to extract: what they are, how they are used, and which agent weaknesses they exploit to give adversaries leverage in indirect prompt injection attacks. We instantiate these insights in Know Your Agent (KYA), a framework that automates black-box, reconnaissance-driven pentesting by probing agents, building target profiles, and using those profiles to craft stronger attacks. We evaluate KYA on agent-security benchmarks and a real-world coding agent, and release KYA, its benchmarks, and baseline implementations for reproducibility.

---


### 94. [Sentence Splitter: Uncovering Latent Factual Structure for Self-Supervised Learning](https://arxiv.org/abs/2607.19845)

**<font color=#1a73e8>作者：</font>** Ahmad Pouramini, Mahsa Afsharizadeh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper introduces Sentence Splitter, a self-supervised framework built upon a T5-based encoder--decoder architecture for uncovering the latent factual structure of natural language sentences. The proposed method identifies the semantic boundary between a descriptive prefix (head) and its factual completion (tail) by formulating sentence splitting as a discrete segmentation problem, where a sentence of length $N$ admits $N$ possible split points but only one recovers the intended head--tail structure. Rather than explicitly searching over all candidate boundaries, the model learns to recover the factual completion through probabilistic sequence generation. To eliminate the need for manual annotation, symbolic head--tail pairs are first verbalized into natural-language templates that provide supervision for training the Sentence Splitter. The trained splitter is then applied to raw text to extract aligned prefix--tail pairs, which are subsequently used to train a generative model that proposes additional plausible completions through a lightweight bootstrapping process. This unified pipeline provides a scalable and structure-aware approach to constructing self-supervised training data while bridging symbolic knowledge and natural language. Experiments on both structured and naturally occurring text demonstrate that the proposed splitter generalizes beyond synthetic templates and that the resulting structure-aware supervision consistently improves downstream performance on knowledge graph completion and commonsense question answering, highlighting the effectiveness of recovering latent factual structure for knowledge-centric NLP.

---


### 95. [emb-diversity: A Tool for Embedding-Based Measurement of Data Diversity](https://arxiv.org/abs/2607.19848)

**<font color=#1a73e8>作者：</font>** Cantao Su, Menan Velayuthan, Esther Ploeger 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> There is growing evidence that data diversity is crucial for developing fair and robust NLP models. However, current approaches to measure diversity remain inconsistent and fragmented: While there exist a number of tools for measuring the lexical diversity of texts, researchers lack standardized tools for quantifying diversity based on embeddings. Embedding-based diversity measures are highly flexible: They work with any embedding model and any data that can be embedded, and are thus applicable to many notions of diversity. With emb-diversity, we provide a comprehensive embedding-based diversity measurement tool, spanning a broad range of measures. We demonstrate its potential for several use cases: measuring the stylistic, semantic, language and speaker diversity of datasets. this https URL

---


### 96. [Asymptotically Optimal Regret for Reinforcement Learning without Horizon Dependence](https://arxiv.org/abs/2607.19854)

**<font color=#1a73e8>作者：</font>** Runlong Zhou, Zihan Zhang, Maryam Fazel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study horizon-free regret minimization for finite-horizon time-homogeneous tabular Markov decision processes with $S$ states, $A$ actions, horizon $H$, and per-trajectory total reward bounded by $1$.
We propose a new algorithm and prove a regret upper bound \[\tilde O(\sqrt{SAK}+S^8A^3)\] with failure probability $\delta$, where $K$ is the number of episodes and $\tilde O(\cdot)$ hides $\mathsf{poly}\log(S,A,K,1/\delta)$.
Thus, the regret is $H$-free and asymptotically optimal, matching the contextual-bandit lower bound $\Omega(\sqrt{SAK})$ up to logarithmic factors. This completely removes the $\log H$ dependence from the previous $\tilde O(\sqrt{SAK\log H}+S^2A\log H)$ guarantee of Zhang et al. (2021), and drastically improves the prior best horizon-free regret $\tilde O(\sqrt{S^9A^3K})$ of Zhang et al. (2022) asymptotically.
The main technical difficulty is that the optimal value functions $\{V_h^*\}_{h=1}^H$ are time-inhomogeneous even though the transition kernel is time-homogeneous. A direct union bound over all value functions typically incurs an additional $\min\{\log H,S\}$ factor. We avoid this factor by (i) exploiting the monotonicity of $V_h^*$ in $h$ and (ii) non-trivially projecting the value functions onto an $S$-dimensional grid.
Our analysis relies on three additional ingredients. First, we introduce a horizon-truncation argument that enables reward-based exploration and removes the cost of a separate reward-free exploration phase. Second, we design a cutting bonus that preserves both optimism and the monotonicity needed for planning. Third, we prove a new bound on total deviation for time-homogeneous MDPs, which controls the clipped variance terms in the cutting bonus with adjustable polynomial dependence on $S$ and without any dependence on $H$. Together, these tools yield an asymptotically optimal horizon-free regret guarantee.

---


### 97. [Adversarial Frontiers: Minimum-Norm Attack Ensembles for Robustness Evaluation](https://arxiv.org/abs/2607.19855)

**<font color=#1a73e8>作者：</font>** Luca Scionis, Luca Melis, Maura Pintor 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adversarial robustness is commonly evaluated with predefined attack ensembles, such as AutoAttack, at a single perturbation budget $\varepsilon$ and on a selective choice of perturbation norms. We argue this formulation is fundamentally limited. First, robustness--perturbation curves may intersect or decay at different rates across models, making single-$\varepsilon$ rankings unstable. Second, current ensembles provide no evidence of optimality, leaving an unknown gap to worst-case performance. Third, fixed attack configurations provide no systematic control over the trade-off between attack strength and evaluation cost. To address these limitations, we introduce a unified evaluation framework based on a comprehensive pool of minimum-norm attacks and robustness--perturbation curves across $\ell_0$, $\ell_1$, $\ell_2$ and $\ell_\infty$ norms. We define the attack frontier as the worst-case robustness estimate the attack pool produces against a model. We then formalize evaluation as a frontier-approximation problem, constructing minimum-norm attack ensembles, optimized subsets of the comprehensive pool, that approach the frontier under a controllable query budget, with larger budgets monotonically tightening the estimate. Furthermore, we define the defense frontier as the maximum robustness across the model set at each perturbation size. We finally propose the Defense Optimality Index to rank defenses by their gap to the defense frontier, providing a ranking without selecting a reference $\varepsilon$. On CIFAR-10 and ImageNet, our ensembles match or exceed AutoAttack on most defenses at every budget tier, at fixed and controllable query cost, offering practitioners a query-controlled, curve-based alternative to fixed-$\varepsilon$ evaluation.

---


### 98. [Overview of FinMMEval 2026 Task 1: Multilingual Financial Multiple-Choice Question Answering](https://arxiv.org/abs/2607.19856)

**<font color=#1a73e8>作者：</font>** Zhuohan Xie, Yuyang Dai, Rania Elbadry 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> FinMMEval 2026 Task 1 evaluates multilingual financial multiple-choice question answering in English, Chinese, Arabic, and Hindi. The task tests whether systems can select the correct answer to finance questions involving domain terminology, numerical interpretation, and conceptual financial reasoning across languages and scripts. The final-test set contains 800 questions, with 200 questions per language; gold answers were withheld during submission, and each language was ranked independently by accuracy. The final leaderboards contain 13 English, 11 Chinese, 11 Arabic, and 10 Hindi ranked submissions. Top accuracies range from 92.0% in Hindi to 97.5% in English and Arabic, with the same leading teams appearing near the top across all four languages. The documented systems used retrieval augmentation, direct answer-option scoring, language-specific prompting, selective self-consistency, confidence checks, and LLM-based review stages.

---


### 99. [DocOps: A Verifiable Benchmark for Autonomous Agents in Complex Document Operations](https://arxiv.org/abs/2607.19865)

**<font color=#1a73e8>作者：</font>** Jiazhen Jiang, Boxi Cao, Lingyong Yan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As autonomous agents rapidly evolve, their ability to reliably manipulate ubiquitous digital documents has become critical for enabling general-purpose AI assistants and automating complex workspace workflows. In this paper, we introduce DocOps, a deterministically verifiable evaluation framework underpinned by a hierarchical taxonomy that deconstructs document operations inspired by real-world practices into atomic dimensions and escalating workflow complexities. Based on DocOps, we systematically evaluate representative closed- and open-source models across various agentic harnesses, revealing that even the most advanced frontier configurations still exhibit profound limitations when handling highly coupled, long-range tasks. Furthermore, a fine-grained analysis of existing agents' manipulation behaviors uncovers 3 key failure modes: long-term state tracking collapse, shallow semantic verification, and destructive editing of structural metadata. Ultimately, our work exposes the capability boundaries of agents in maintaining global document consistency, shedding light on the future design of robust, non-destructive agents for complex digital ecosystems.

---


### 100. [Local Causal Structure Learning in the Presence of Latent Variables and Selection Bias](https://arxiv.org/abs/2607.19866)

**<font color=#1a73e8>作者：</font>** Zheng Li, Hao Zhang, Ruxin Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discovering the direct causes and effects of a target variable from observational data is a fundamental problem in causal discovery, with broad applications in domains such as gene regulatory analysis and biomedical research. Existing causal discovery methods either learn a global causal structure, which incurs substantial computational cost, or assume the absence of latent variables and selection bias, assumptions that are often violated in real-world settings. Motivated by these challenges, we study local causal structure learning in the presence of latent variables and selection bias. Specifically, we first characterize a local region that enables target-specific causal discovery without recovering the entire global structure. We then establish a theoretical bridge between causal information learned from the observed distribution induced on this local region and the corresponding information in the global causal structure. Building on these foundations, we propose LoCaLS, a local causal structure learning algorithm that is sound and complete under standard assumptions and identifies the same direct causes and effects of a target variable as those identifiable by global causal discovery methods, while allowing for latent variables and selection bias. Extensive experiments on random and real-world structures demonstrate that the proposed method consistently achieves higher structural accuracy than existing local methods while requiring substantially less computational effort than state-of-the-art global methods. Furthermore, applications to two real-world gene expression datasets reveal biologically plausible target-specific causal structures, demonstrating its practical applicability in large-scale biological data analysis.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-192](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
