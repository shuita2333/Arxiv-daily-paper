# 📦 其他研究 | 2026年04月30日

> 本类共 **190** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-190](./part-04.md)

---

### 51. [Extended Abstract: Shaperd: Easily Adoptable Real-Time Traffic Shaper for Fully Encrypted Protocols](https://arxiv.org/abs/2604.25069)

**<font color=#1a73e8>作者：</font>** Sarah Wilson, Stella Tian, Sina Kamali  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fully encrypted protocol-based tools (FEPs) are tools commonly used to circumvent censorship in restrictive regions, valued for their performance and security. However, in recent years, censors have been able to block them using an array of attacks based on passive traffic analysis and active probing. We propose Shaperd, an easily adoptable and real-time traffic shaper designed specifically to aid FEPs become more resilient to detection. Shaperd operates directly on packet contents in real time, using a novel constraint system to allow its users to generate traffic flows with any desired features. Our preliminary results reveal Shaperd introduces minimal overhead to the underlying system's throughput.

---


### 52. [Scalable Secure Biometric Authentication without Auxiliary Identifiers](https://arxiv.org/abs/2604.25071)

**<font color=#1a73e8>作者：</font>** Alexander Bienstock, Daniel Escudero, Antigoni Polychroniadou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The prevalence of biometric authentication has been on the rise due to its ease of use and elimination of weak passwords. To date, most biometric authentication systems have been designed for on-device authentication of the device owner (e.g., smartphones and laptops). Recently, biometric authentication systems have started to emerge that are designed to authenticate users against cloud databases storing representations of biometrics for large numbers of users (potentially millions), such as those facilitating biometric payments. However, the use of a large cloud database introduces a significant attack vector, as a breach of the database could lead to the compromise of all enrolled users' sensitive biometric data. Indeed, all such existing systems either do not adequately protect against such a breach, or are impractical to deploy and use due to their high computational overhead. In this work, we present a new biometric authentication system that provides provable security guarantees against data breaches, while remaining scalable and performant. To do so, we marry artificial intelligence with advanced cryptographic techniques in a novel fashion, providing several optimizations along the way. Our work is the first to show that real-world scalable privacy-preserving biometric authentication without auxiliary identifiers is feasible, and we believe that it will spur widespread industrial adoption and further research in this area.

---


### 53. [Feasible-First Exploration for Constrained ML Deployment Optimization in Crash-Prone Hierarchical Search Spaces](https://arxiv.org/abs/2604.25073)

**<font color=#1a73e8>作者：</font>** Christian Lysenstøen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying machine learning models under production constraints requires joint optimization over model family, quantization scheme, runtime backend, and serving configuration. This induces a hierarchical mixed-variable search space in which many configurations are invalid: evaluations may crash, exceed memory limits, or violate latency constraints. Standard black-box optimizers such as Tree-structured Parzen Estimators (TPE) and constrained Bayesian optimization are effective when valid configurations are common, but they can spend a large fraction of a small evaluation budget on invalid or uninformative trials in hostile deployment spaces. This paper studies that regime and asks whether optimization should be decomposed into an explicit exploration stage followed by model-guided exploitation. We propose Thermal Budget Annealing (TBA), a feasible-first exploration procedure that maps valid and feasible regions before warm-starting TPE. The method includes two robustness mechanisms for hostile hardware: trial timeouts that abort clearly infeasible evaluations early, and subspace blacklisting that temporarily suppresses categorical subspaces after repeated failures. We also introduce DeployBench, a benchmark suite for deployment optimization with hierarchical structure, hidden crash zones, hard constraints, and unequal evaluation costs. On synthetic benchmarks and real GPU deployment with five pre-trained vision models across five GPU targets (NVIDIA H100, A100, RTX 5080, L4, and T4), the proposed hybrid improves model-family discovery under tight constraints while reducing wasted budget relative to cold-start TPE.

---


### 54. [Zero Shot Coordination for Sparse Reward Tasks with Diverse Reward Shapings](https://arxiv.org/abs/2604.25076)

**<font color=#1a73e8>作者：</font>** Keenan Powell, Peihong Yu, Pratap Tokekar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many Multi-Agent Reinforcement Learning (MARL) agents fail to adapt properly to cooperating with agents trained with the same objectives but different seeds, algorithms, or other training differences. This is the problem of Zero-Shot Coordination (ZSC), which focuses on training agents to cooperate well with unknown agents. ZSC has been studied for a variety of tabular cases and simple games such as Hanabi, achieving excellent results. However, existing solutions to ZSC only consider identical rewards for your trained agents and all future partners. This is not realistic for the trained agents, as they do not consider the problem of cooperating with agents that have identical sparse objectives but shape the rewards for those objectives in different manner. To address this issue, we show how to train an ensemble of methods using randomized reward shapings chosen using 4 selection algorithms. Experiments done on the Overcooked environment demonstrate consistent improvements of 62.2%-119.2% in sparse reward over baseline ZSC algorithms when playing with agents that have identical sparse rewards but different reward shapings.

---


### 55. [Cooperate to Compete: Strategic Coordination in Multi-Agent Conquest](https://arxiv.org/abs/2604.25088)

**<font color=#1a73e8>作者：</font>** Abigail O'Neill, Alan Zhu, Mihran Miroyan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language Model (LM)-based agents remain largely untested in mixed-motive settings where agents must leverage short-term cooperation for long-term competitive goals (e.g., multi-party politics). We introduce Cooperate to Compete (C2C), a multi-agent environment where players can engage in private negotiations while competing to be the first to achieve their secret objective. Players have asymmetric objectives and negotiations are non-binding, allowing alliances to form and break as players' short-term interests align and diverge. We run AI only games and conduct a user study pitting human players against AI opponents. We identify significant differences between human and AI negotiation behaviors, finding that humans favor lower-complexity deals and are significantly less reliable partners compared to LM-based agents. We also find that humans are more aggressive negotiators, accepting deals without a counteroffer only 56.3% of the time compared to 67.6% for LM-based agents. Through targeted prompting inspired by these findings, we modify agents' negotiation behavior and improve win rates from 22.2% to 32.7%. We run over 1,100 games with over 16,000 private conversations totaling 15.2 million tokens and over 150,000 player actions. Our results establish C2C as a testbed for studying and building LM-based agents that can navigate the sophisticated coordination required for real-world deployments. The game, code, and dataset may be found at this https URL.

---


### 56. [Feature Anchors for Time-Series Sensor-Based Human Activity Recognition](https://arxiv.org/abs/2604.25092)

**<font color=#1a73e8>作者：</font>** Ruijie Yao, Chenhang Li, Danyang Zhuo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Wearable Human Activity Recognition (HAR) still lacks a representation that is both explicit and adaptable. Handcrafted time-series features (TSFs) capture meaningful motion statistics and remain competitive on standard benchmarks, but they are usually used as fixed preprocessing outputs. Deep models learn adaptable representations directly from raw signals, but those representations are typically latent and difficult to inspect. We address this gap by treating handcrafted TSFs as feature anchors: explicit intermediate representations that remain inside the model and are adjusted by neural context instead of being discarded. We propose the Temporal Conditioning Network for Feature Anchors (TCNet), which extracts handcrafted anchors, encodes complementary time-domain and frequency-domain context from raw IMU windows, and predicts context-conditioned scale, bias, and gating parameters to modulate anchor groups directly in feature space. This design keeps anchor semantics visible while allowing the representation to adapt to the classification objective. Across five HAR benchmarks, TCNet achieves 70.2% mF1 on USC-HAD, 85.1% mF1 on Daphnet, 93.9% mF1 on MHealth, and 94.5% mF1 on PAMAP2. Relative to rTsfNet, it improves by 4.5 points on USC-HAD, 14.6 points on Daphnet, and 6.5 points on MHealth. Ablations show that the gains come primarily from anchor guidance rather than simple branch fusion, and feature-space analyses indicate that several discriminative TSF families are not reliably accessible in standard latent representations. These results suggest that, for HAR, handcrafted TSFs are most useful when they remain explicit and adaptable within the model. The code is available at: this https URL

---


### 57. [The Dynamics of Delusion: Modeling Bidirectional False Belief Amplification in Human-Chatbot Dialogue](https://arxiv.org/abs/2604.25096)

**<font color=#1a73e8>作者：</font>** Ashish Mehta, Jared Moore, Jacy Reese Anthis 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> There is growing concern that AI chatbots might fuel delusional beliefs in users. Some have suggested that humans and chatbots mutually reinforce false beliefs over time, but quantitative evidence is lacking. Using a unique dataset of chat logs from individuals who exhibited delusional thinking, we developed a latent state model that captures accumulating and decaying influences between humans and chatbots. We find that a bidirectional influence model substantially outperforms a unidirectional alternative where humans are the primary driver of delusion. We find that humans exert strong but short-lived influence on chatbots, whereas chatbots exert longer-lasting influence on humans. Moreover, chatbots exert strong, stable self-influence over their own future outputs that tends to perpetuate delusions over long stretches of conversation. In fact, this chatbot self-influence constituted the dominant pathway when considering accumulated influence over time. Overall, these results indicate that humans tend to drive sharp, immediate increases in delusion, whereas chatbots sustain and propagate these effects over longer timescales. Together, these findings provide the first quantitative evidence that human-chatbot interactions can form feedback loops of delusion, decomposable into distinct pathways with dissociable temporal dynamics. By doing so, they can inform the development of safer AI systems.

---


### 58. [Structured Security Auditing and Robustness Enhancement for Untrusted Agent Skills](https://arxiv.org/abs/2604.25109)

**<font color=#1a73e8>作者：</font>** Lijia Lv, Xuehai Tang, Jie Wen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent Skills package this http URL files, scripts, reference documents, and repository context into reusable capability units, turning pre-load auditing from single-prompt filtering into cross-file security review. Existing guardrails often flag risk but recover malicious intent inconsistently under semantics-preserving rewrites. This paper formulates pre-load auditing for untrusted Agent Skills as a robust three-way classification task and introduces SkillGuard-Robust, which combines role-aware evidence extraction, selective semantic verification, and consistency-preserving adjudication. We evaluate SkillGuard-Robust on SkillGuardBench and two public-ecosystem extensions through five large evaluation views ranging from 254 to 404 packages. On the 404-package held-out aggregate, SkillGuard-Robust reaches 97.30% overall exact match, 98.33% malicious-risk recall, and 98.89% attack exact consistency. On the 254-package external-ecosystem view, it reaches 99.66%, 100.00%, and 100.00%, respectively. These results support a bounded conclusion: factorized package auditing materially improves frozen and public-ecosystem robustness, while harsher external-source transfer remains an open challenge.

---


### 59. [Knowledge Distillation Must Account for What It Loses](https://arxiv.org/abs/2604.25110)

**<font color=#1a73e8>作者：</font>** Wenshuo Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This position paper argues that knowledge distillation must account for what it loses: student models should be judged not only by retained task scores, but by whether they preserve the teacher capabilities that make those scores reliable. This matters because distillation is increasingly used to turn large, often frontier models into deployable systems, yet headline metrics can hide losses in uncertainty, boundary behavior, process reliability, on-policy stability, grounding, privacy, safety, and diversity. We identify the retention assumption behind current evaluation and reframe distillation as a lossy projection of teacher behavior rather than a faithful copy. We then synthesize existing evidence into a taxonomy of off-metric distillation losses, showing that these losses are concrete, recurring, and measurable. To make the position actionable, we propose scenario-specific preservation targets and a Distillation Loss Statement that reports what was preserved, what was lost, and why the remaining losses are acceptable. The goal is not lossless distillation, but accountable distillation.

---


### 60. [People, IT, and Structuration (PIS): An Integrative Theoretical Framework for Management Information Systems](https://arxiv.org/abs/2604.25118)

**<font color=#1a73e8>作者：</font>** Wei Huang, Xiaofang Cai, Qiaozhen Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The Management Information Systems (MIS) discipline has long grappled with how to theorize the complex, mutually constitutive relationships among people, information technology, and organizational structures. Decades of research have produced influential but fragmented theoretical streams from socio-technical systems theory to technology acceptance models, from adaptive structuration theory to sociomateriality, and each illuminating important facets while leaving integrative questions unresolved. This paper proposes the People - IT - Structuration (PIS) framework as a unifying theoretical lens that synthesizes these streams. Drawing on Giddens' structuration theory, we conceptualize People (P), Information Technology (I), and Structure (S) not as independent variables but as mutually constitutive elements engaged in ongoing structuration processes. We trace the intellectual history of MIS theorizing to demonstrate how PIS resolves persistent tensions in the field,e.g. between technological and social determinism, between variance and process approaches, and between micro-level interaction and macro-level institutional dynamics. We develop a set of formal propositions articulating the mechanisms through which P, I, and S co-evolve, and extend the framework to address contemporary phenomena including artificial intelligence, algorithmic management, and human-AI collaboration. The PIS framework offers both a retrospective lens for understanding the discipline's theoretical evolution and a prospective tool for guiding research in the AI era.

---


### 61. [Evaluation without Generation: Non-Generative Assessment of Harmful Model Specialization with Applications to CSAM](https://arxiv.org/abs/2604.25119)

**<font color=#1a73e8>作者：</font>** Vinith M. Suriyakumar, Ayush Sekhari, Lena Stempfle 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Auditing the fine-tunes of open-weight generative models for harmful specialization has become a new governance challenge for model hosting platforms. The standard toolkit, generative evaluation via curated prompts or red-teaming, does not scale to platform-level auditing and breaks down entirely for domains like CSAM where generation is legally constrained. This motivates the Evaluation without Generation problem: assessing model capabilities without producing outputs. We argue that in such settings, capability must be inferred from the model's state, either its parameters or internal representations, rather than its outputs. We introduce Gaussian probing, a method that characterizes how LoRA adaptors perturb a model's internal representations by measuring responses to Gaussian latent ensembles. Unlike raw-weight baselines, Gaussian probing reliably distinguishes benign from harmful specialization without sampling outputs. We demonstrate effectiveness in high-risk domains, including detecting models specialized for child sexual abuse material (CSAM), where output-based evaluation is legally and ethically constrained. Our results show that Gaussian probing provides a scalable non-generative alternative for evaluating high-risk generative systems and remains robust to weight rescaling, a representative adversarial manipulation.

---


### 62. [ResetEdit: Precise Text-guided Editing of Generated Image via Resettable Starting Latent](https://arxiv.org/abs/2604.25128)

**<font color=#1a73e8>作者：</font>** Hanyi Wang, Han Fang, Zheng Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in diffusion models have enabled high-quality image generation, leading to increasing demand for post-generation editing that modifies local regions while preserving global structure. Achieving such flexible and precise editing requires a high-quality starting point, a latent representation that provides both the freedom needed for diverse modifications and the precision required for fine-grained, region-specific control. However, existing inversion-based approaches such as DDIM inversion often yield unsatisfactory starting latents, resulting in degraded edit fidelity and structural inconsistency. Ideally, the most suitable editing anchor should be the original latent used during the generation process, as it inherently captures the scene's structure and semantics. Yet, storing this latent for every generated image is impractical due to massive storage and retrieval costs. To address this challenge, we propose ResetEdit, a proactive diffusion editing framework that embeds recoverable latent information directly into the generation process. By injecting the discrepancy between the clean and diffused latents into the diffusion trajectory and extracting it during inversion, ResetEdit reconstructs a resettable latent that closely approximates the true starting state. Additionally, a lightweight latent optimization module compensates for reconstruction bias caused by VAE asymmetry. Built upon Stable Diffusion, ResetEdit integrates seamlessly with existing tuning-free editing methods and consistently outperforms state-of-the-art baselines in both controllability and visual fidelity.

---


### 63. [LongSumEval: Question-Answering Based Evaluation and Feedback-Driven Refinement for Long Document Summarization](https://arxiv.org/abs/2604.25130)

**<font color=#1a73e8>作者：</font>** Huyen Nguyen, Haoxuan Zhang, Yang Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating long document summaries remains the primary bottleneck in summarization research. Existing metrics correlate weakly with human judgments and produce aggregate scores without explaining deficiencies or guiding improvement, preventing effective refinement in applications requiring verifiable accuracy. We introduce LongSumEval, a unified framework bridging evaluation and generation through structured question-answering feedback. The framework operationalizes summary quality as answerability and factual alignment of question-answer pairs, generating interpretable scores and actionable feedback that identifies coverage gaps and factual inconsistencies. This resolves the misalignment where evaluation operates independently of generation objectives. Meta-evaluation of our QA-based evaluation module across seven benchmarks demonstrates substantially stronger agreement with human judgments compared to established metrics. Structured feedback enables significant quality improvements through self-refinement without retraining. By demonstrating that evaluation feedback can serve as executable instructions for generation, this work establishes a generalizable paradigm for aligning assessment with improvement, with direct implications for controllable text generation requiring verifiable accuracy and transparent quality control. All code and datasets will be released in GitHub for reproducibility.

---


### 64. [Towards Unified Multi-task EEG Analysis with Low-Rank Adaptation](https://arxiv.org/abs/2604.25131)

**<font color=#1a73e8>作者：</font>** Sicheng Dai, Kai Chen, Hongwang Xiao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent self-supervised pre-training methods for electroencephalogram (EEG) have shown promising results. However, the pre-trained models typically require full fine-tuning on each downstream task individually to achieve good performance. In practical applications involving multiple tasks, utilizing a separate model for each task is not ideal regarding computational and spatial cost. In this study, we go one step further and explore the simultaneous adaptation of a pre-trained model to multiple different tasks. The EEG signals exhibit significant heterogeneity due to their collection from various subjects using diverse devices and experimental setups, resulting in potential conflicts among different tasks that impede joint optimization. To tackle this challenge, we propose MTEEG, a multi-task EEG analysis framework which incorporates task-specific low-rank adaptation (LoRA) modules to disentangle the parameter space and alleviate task conflicts. To investigate the trade-off between task specification and interaction, we propose three variants of MTEEG that integrate the LoRA modules in different ways and evaluate them on six downstream tasks, demonstrating that MTEEG can surpass state-of-the-art single-task methods on the majority of metrics. MTEEG shows the potential of multi-task EEG analysis and promotes the development of general-purpose brain-computer interfaces in the future.

---


### 65. [Korean aegyo speech shows systematic F1 increase to signal childlike qualities](https://arxiv.org/abs/2604.25133)

**<font color=#1a73e8>作者：</font>** Ji-eun Kim, Volker Dellwo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Korean aegyo is a socially recognized childlike speaking style used predominantly in romantic interactions among adults. This study examined vowel space modification in aegyo by analyzing formant frequencies from twelve Seoul Korean speakers who produced identical scripts in aegyo and non-aegyo styles. Results show that aegyo speech features a significant increase in F1 values across vowels and selective fronting of front vowels, leading to vowel space expansion but mainly a shift to higher F1. These findings suggest that adult speakers stylize childlike speech by imitating the shorter vocal tract of children, mainly through global vowel lowering and partial fronting.

---


### 66. [Gradient-Direction Sensitivity Reveals Linear-Centroid Coupling Hidden by Optimizer Trajectories](https://arxiv.org/abs/2604.25143)

**<font color=#1a73e8>作者：</font>** Yongzhong Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We show that replacing the rolling SVD of AdamW updates with a rolling SVD of loss gradients changes the diagnostic by 1-2 orders of magnitude. Performing SVD on the loss gradient instead of the AdamW update increases the measured perturbative coupling between SED directions and Linear Centroid Hypothesis (LCH) features from $ \bar{R}_k \approx 3 $--$9\times$ to $100$--$330\times$ across four single-task modular arithmetic operations, eliminating the apparent operation dependence in the original measurement. On a multitask transformer with a shared encoder, update-based SED gives $ \bar{R}_k \leq 1 $ -- an apparent failure of the diagnostic -- while per-operation gradient-based SED recovers $ \bar{R}_k = 20 $--$45\times$ across all four operations. Gradient aggregation across competing tasks is the main obstruction; performing SVD on per-task gradients resolves it. A causal intervention shows that constraining attention updates to any rank-3 subspace (whether SED-derived or random) accelerates grokking by approximately $2.3\times$ across random seeds and operations, while removing the rank-3 component has negligible effect under proper gradient-projection methodology. The SED-LCH coupling is therefore a strong diagnostic of where feature formation concentrates in parameter space, but it is not a unique causal pathway: the natural full-rank AdamW attention update is highly rank-redundant under our hyperparameters.

---


### 67. [The Role of Symmetry in Optimizing Overparameterized Networks](https://arxiv.org/abs/2604.25150)

**<font color=#1a73e8>作者：</font>** Kusha Sareen, Mohammad Pedramfar, Sékou-Oumar Kaba 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Overparameterization is central to the success of deep learning, yet the mechanisms by which it improves optimization remain incompletely understood. We analyze weight-space symmetries in neural networks and show that overparameterization introduces additional symmetries that benefit optimization in two distinct ways. First, we prove that these symmetries act as a form of diagonal preconditioning on the Hessian, enabling the existence of better-conditioned minima within each equivalence class of functionally identical solutions. Second, we show that overparameterization increases the probability mass of global minima near typical initializations, making these favorable solutions more reachable. Teacher-student network experiments validate our theoretical predictions: as width increases, the Hessian trace decreases, condition numbers improve, and convergence accelerates. Our analysis provides a unified framework for understanding overparameterization and width growth as a geometric transformation of the loss landscape.

---


### 68. [MGTEVAL: An Interactive Platform for Systemtic Evaluation of Machine-Generated Text Detectors](https://arxiv.org/abs/2604.25152)

**<font color=#1a73e8>作者：</font>** Yuanfan Li, Qi Zhou, Chengzhengxu Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present MGTEVAL, an extensible platform for systematic evaluation of Machine-Generated Text (MGT) detectors. Despite rapid progress in MGT detection, existing evaluations are often fragmented across datasets, preprocessing, attacks, and metrics, making results hard to compare and reproduce. MGTEVAL organizes the workflow into four components: Dataset Building, Dataset Attack, Detector Training, and Performance Evaluation. It supports constructing custom benchmarks by generating MGT with configurable LLMs, applying 12 text attacks to test sets, training detectors via a unified interface, and reporting effectiveness, robustness, and efficiency. The platform provides both command-line and Web-based interfaces for user-friendly experimentation without code rewriting.

---


### 69. [Where Did It Go Wrong? Capability-Oriented Failure Attribution for Vision-and-Language Navigation Agents](https://arxiv.org/abs/2604.25161)

**<font color=#1a73e8>作者：</font>** Jianming Chen, Yawen Wang, Junjie Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Embodied agents in safety-critical applications such as Vision-Language Navigation (VLN) rely on multiple interdependent capabilities (e.g., perception, memory, planning, decision), making failures difficult to localize and attribute. Existing testing methods are largely system-level and provide limited insight into which capability deficiencies cause task failures. We propose a capability-oriented testing approach that enables failure detection and attribution by combining (1) adaptive test case generation via seed selection and mutation, (2) capability oracles for identifying capability-specific errors, and (3) a feedback mechanism that attributes failures to capabilities and guides further test generation. Experiments show that our method discovers more failure cases and more accurately pinpoints capability-level deficiencies than state-of-the-art baselines, providing more interpretable and actionable guidance for improving embodied agents.

---


### 70. [IAM: Identity-Aware Human Motion and Shape Joint Generation](https://arxiv.org/abs/2604.25164)

**<font color=#1a73e8>作者：</font>** Wenqi Jia, Zekun Li, Abhay Mittal 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in text-driven human motion generation enable models to synthesize realistic motion sequences from natural language descriptions. However, most existing approaches assume identity-neutral motion and generate movements using a canonical body representation, ignoring the strong influence of body morphology on motion dynamics. In practice, attributes such as body proportions, mass distribution, and age significantly affect how actions are performed, and neglecting this coupling often leads to physically inconsistent motions. We propose an identity-aware motion generation framework that explicitly models the relationship between body morphology and motion dynamics. Instead of relying on explicit geometric measurements, identity is represented using multimodal signals, including natural language descriptions and visual cues. We further introduce a joint motion-shape generation paradigm that simultaneously synthesizes motion sequences and body shape parameters, allowing identity cues to directly modulate motion dynamics. Extensive experiments on motion capture datasets and large-scale in-the-wild videos demonstrate improved motion realism and motion-identity consistency while maintaining high motion quality. Project page: this https URL

---


### 71. [Training Transformers as a Universal Computer](https://arxiv.org/abs/2604.25166)

**<font color=#1a73e8>作者：</font>** Ruize Xu, Chenxiao Yang, Yanhong Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We demonstrate that a small transformer can learn to execute programs in MicroPy, a simplified yet computationally universal programming language. Given procedure definitions together with an expression to evaluate, the transformer predicts small-step execution using PENCIL scaffolding for space-efficient execution within a bounded context window. After training on randomly generated, meaningless MicroPy programs, the learned transformer generalizes to various human-written programs including bit copying and flipping, binary addition and multiplication, and SAT verification and solving. We note that the trained model can achieve out-of-distribution generalization; i.e., evaluate novel programs from distribution on programs. Since MicroPy can express any computation, our results provide empirical evidence that a standard transformer can be trained to act as a universal computer.

---


### 72. [Benchmarking OCR Pipelines with Adaptive Enhancement for Multi-Domain Retail Bill Digitization](https://arxiv.org/abs/2604.25176)

**<font color=#1a73e8>作者：</font>** Vijaysinh Gaikwad  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The digitization of multi-domain retail billing documents remains a challenging task due to variability in scan quality, layout heterogeneity, and domain diversity across commercial sectors. This paper proposes and benchmarks an intelligent, quality-aware adaptive Optical Character Recognition (OCR) pipeline for retail bill digitization spanning five domains: grocery stores, restaurants, hardware shops, footwear outlets, and clothing retailers. The proposed system integrates a Convolutional Neural Network (CNN)-based image enhancement module trained via self-supervised denoising, a Laplacian variance-based image quality analyzer with three-tier routing, a confidence-driven adaptive feedback loop with iterative retry, and an NLP-based post-OCR correction layer. Experiments were conducted on a real-world dataset of 360 heterogeneous retail bill images. Ground truth for quantitative evaluation was generated using an OCR ensemble majority voting strategy, a validated approach for scenarios without manual annotation. The proposed pipeline achieves a Character Error Rate (CER) of 18.4% and Word Error Rate (WER) of 27.6%, representing improvements of 26.4% and 31.2% respectively over the Raw Tesseract baseline. The pipeline additionally achieves a text density of 108.3 words per image, a noise ratio of 2.3%, and a processing time of 3.64 seconds per image - a 6.4x speed advantage over EasyOCR. Image quality PSNR analysis on enhanced MEDIUM and LOW quality images yields an average of 28.7 dB, confirming meaningful enhancement. These results establish a reproducible benchmark for multi-domain retail bill OCR research.

---


### 73. [Lightweight Real-Time Rendering Parameter Optimization via XGBoost-Driven Lookup Tables](https://arxiv.org/abs/2604.25178)

**<font color=#1a73e8>作者：</font>** Baijun Tan, Francesco Moretti  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Achieving a desirable balance between rendering quality and real-time performance is a long-standing challenge in modern game and rendering engines, particularly on resource-constrained mobile devices such as laptops, tablets, and smartphones. Existing approaches to automatic rendering parameter optimization either depend on exhaustive per-scene pre-computation that spans several days, suffer from the prohibitive inference overhead of neural networks that prevents per-frame adaptation, or lack generalizability across heterogeneous hardware and diverse scenes. In this paper, we propose \textbf{LUT-Opt}, a lightweight, general-purpose framework for adaptive per-frame rendering parameter optimization. Our method decomposes the joint optimization of rendering time and image quality into a tractable two-stage pipeline. In the offline stage, we train a pair of XGBoost regressors to predict rendering time and image quality from rendering parameters, hardware state, and scene complexity descriptors. The trained ensemble models are then distilled into compact lookup tables (LUTs) through systematic discretization and a two-phase linear search that first constrains rendering time and subsequently maximizes structural similarity (SSIM). During runtime, the pre-computed LUT is queried every frame in sub-millisecond time, enabling truly adaptive parameter selection with negligible computational overhead. We validate LUT-Opt on two representative rendering techniques -- subsurface scattering (SSS) and hybrid-pipeline ambient occlusion (AO) -- implemented within Unreal Engine 5. Extensive experiments across multiple scenes and GPU configurations demonstrate that LUT-Opt reduces subsurface scattering rendering time by approximately 40\% and ambient occlusion rendering time by roughly 70\%, while incurring only about 2\% increase in image quality error, with per-frame inference latency below 0.1\ ms.

---


### 74. [Shearlet Neural Operators for Anisotropic-Shock-Dominated and Multi-scale parametric partial differential equations](https://arxiv.org/abs/2604.25181)

**<font color=#1a73e8>作者：</font>** Fabio Pereira dos Santos, Julio de Castro Vargas Fernandes, Adriano Mauricio de Almeida Cortes  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators have emerged as powerful data-driven surrogates for learning solution operators of parametric partial differential equations (PDEs). However, widely used Fourier Neural Operators (FNOs) rely on global Fourier representations, which can be inefficient for resolving anisotropic structures, sharp gradients, and spatially localized discontinuities that arise in shock-dominated and multiscale regimes. To address these limitations, we introduce the Shearlet Neural Operator (SNO), a neural operator architecture that replaces the Fourier transform with a shearlet-based representation. Shearlets offer directional, multiscale, and spatially localized atoms with near-optimal sparse approximation of anisotropic features, providing an inductive bias aligned with PDE solutions containing edges, fronts, and shocks. SNO learns in the shearlet domain and reconstructs predictions via the inverse transform, retaining efficient spectral computation while improving locality and directional selectivity. Across seven benchmark PDE families, including strongly anisotropic advection, anisotropic diffusion, and nonlinear conservation laws with straight, curved, interacting, spiral, and polygonal shock structures, SNO consistently improves predictive accuracy and feature fidelity over FNO baselines, with the largest gains observed in anisotropic and discontinuity-dominated settings.

---


### 75. [FCMBench-Video: Benchmarking Document Video Intelligence](https://arxiv.org/abs/2604.25186)

**<font color=#1a73e8>作者：</font>** Runze Cui, Fangxin Shang, Yehui Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Document understanding is a critical capability in financial credit review, onboarding, and remote verification, where both decision accuracy and evidence traceability matter. Compared with static document images, document videos present a temporally redundant and sequentially unfolding evidence stream, require evidence integration across frames, and preserve acquisition-process cues relevant to authenticity-sensitive and anti-fraud review. We introduce FCMBench-Video, a benchmark for document-video intelligence that evaluates document perception, temporal grounding, and evidence-grounded reasoning under realistic capture conditions. For privacy-compliant yet realistic data at scale, we organize construction as an atomic-acquisition and composition workflow that records reusable single-document clips, applies controlled degradations, and assembles long-form multi-document videos with prescribed temporal spans. FCMBench-Video is built from 495 atomic videos composed into 1,200 long-form videos paired with 11,322 expert-annotated question--answer instances, covering 28 document types over 20s--60s duration tiers and 5,960 Chinese / 5,362 English instances. Evaluations on nine recent Video-MLLMs show that FCMBench-Video provides meaningful separation across systems and capabilities: counting is the most duration-sensitive task, Cross-Document Validation and Evidence-Grounded Selection probe higher-level evidence integration, and Visual Prompt Injection provides a complementary robustness dimension. The overall score distribution is broad and approximately bell-shaped, indicating a benchmark that is neither saturated nor dominated by trivial cases. Together, these results position FCMBench-Video as a reproducible benchmark for tracking Video-MLLM progress on document-video understanding and probing capability boundaries in authenticity-sensitive credit-domain applications.

---


### 76. [Image Classification via Random Dilated Convolution with Multi-Branch Feature Extraction and Context Excitation](https://arxiv.org/abs/2604.25188)

**<font color=#1a73e8>作者：</font>** Wentao Jiang, Yuanchan Xu, Heng Yuan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image classification remains a fundamental yet challenging task in computer vision, particularly when fine-grained feature extraction and background noise suppression are required simultaneously. Conventional convolutional neural networks, despite their remarkable success in hierarchical feature learning, often struggle with capturing multi-scale contextual information and are susceptible to overfitting when confronted with noisy or irrelevant image regions. In this paper, we propose RDCNet (Image Classification Network with Random Dilated Convolution), a novel architecture built upon ResNet-34 that integrates three synergistic innovations to address these limitations: (1) a Multi-Branch Random Dilated Convolution (MRDC) module that employs parallel branches with varying dilation rates combined with a stochastic masking mechanism to capture fine-grained features across multiple scales while enhancing robustness against noise and overfitting; (2) a Fine-Grained Feature Enhancement (FGFE) module embedded within MRDC that bridges global contextual information with local feature representations through adaptive pooling and bilinear interpolation, thereby amplifying sensitivity to subtle visual patterns; and (3) a Context Excitation (CE) module that leverages softmax-based spatial attention and channel recalibration to dynamically emphasize task-relevant features while suppressing background interference. Extensive experiments conducted on five benchmark datasets -- CIFAR-10, CIFAR-100, SVHN, Imagenette, and Imagewoof -- demonstrate that RDCNet consistently achieves state-of-the-art classification accuracy, outperforming the second-best competing methods by margins of 0.02\%, 1.12\%, 0.18\%, 4.73\%, and 3.56\%, respectively, thereby validating the effectiveness and generalizability of the proposed approach across diverse visual recognition scenarios.

---


### 77. [AgentDID: Trustless Identity Authentication for AI Agents](https://arxiv.org/abs/2604.25189)

**<font color=#1a73e8>作者：</font>** Minghui Xu, Xiaoyu Liu, Yihao Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents are autonomous entities that can be instantiated on demand, migrate across platforms, and interact with other agents or services without continuous human supervision. In such environments, identity is critical for establishing reliable interaction semantics among agents that may lack prior trust relationships. However, existing identity and access management mechanisms are designed for human users or static machines, assuming centralized enrollment, persistent identifiers, and stable execution contexts. These assumptions do not hold for AI agents, whose identities are self-managed, short-lived, and tightly coupled with their execution state and capabilities. We study the problem of identity authentication and state verification for AI agents and identify three challenges: (1) supporting self-managed identities for autonomously created agents, (2) enabling authentication under large-scale, concurrent interactions, and (3) verifying agents' dynamic execution state, such as whether their context and capabilities remain valid at interaction time. To address these challenges, we present AgentDID, a decentralized framework for identity authentication and state verification. AgentDID leverages decentralized identifiers (DIDs) and verifiable credentials (VCs), enabling agents to manage their own identities and authenticate across systems without centralized control. To address the limitations of static credential-based approaches, AgentDID introduces a challenge-response mechanism that allows verifiers to validate an agent's execution conditions at interaction time. We implement AgentDID in compliance with W3C standards and evaluate it through throughput experiments with multiple concurrent agents. Results show that the system achieves scalable identity authentication and state verification, demonstrating its potential to support large populations of AI agents.

---


### 78. [Secure Conformance Checking using Token-based Replay and Homomorphic Encryption](https://arxiv.org/abs/2604.25190)

**<font color=#1a73e8>作者：</font>** Luis-Armando Rodríguez-Flores, Luciano García-Bañuelos, Abel Armas-Cervantes 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Conformance checking, one of the main process mining operations, aims to identify discrepancies between a process model and an event log. The model represents the expected behaviour, whereas the event log represents the actual process behaviour as captured in information systems' records. Traditionally, the process model and the event log are both accessible to the business analyst performing the conformance checking. However, in some contexts the log's owner may want to protect critical or sensitive information in the log and still check its conformance with respect to a model belonging to another party. In this paper, we propose a secure approach to conformance checking based on the well-known token-based replay algorithm and homomorphic encryption. An evaluation is performed using a synthetic log, showing the practicality of the proposed technique.

---


### 79. [Making AI-Assisted Grant Evaluation Auditable without Exposing the Model](https://arxiv.org/abs/2604.25200)

**<font color=#1a73e8>作者：</font>** Kemal Bicakci  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Public agencies are beginning to consider large language models (LLMs) as decision-support tools for grant evaluation. This creates a practical governance problem: the model and scoring rubric should not be exposed in a way that allows applicants to optimize against them, yet the evaluation process must remain auditable, contestable, and accountable.
We propose a TEE-based architecture that helps reconcile these requirements through remote attestation. The architecture allows an external verifier to check which model, rubric, prompt template, and input representation were used, without exposing model weights, proprietary scoring logic, or intermediate reasoning to applicants or infrastructure operators. The main artifact is an attested evaluation bundle: a signed, timestamped record linking the original submission hash, the canonical input hash, the model-and-rubric measurement, and the evaluation output.
The paper also considers a scenario-specific prompt injection risk: applicant-controlled documents may contain hidden or indirect instructions intended to influence the LLM evaluator. We therefore include a canonicalization and sanitization layer that normalizes document representations and records suspicious transformations before inference. We position the design relative to confidential AI inference, attestable AI audits, zero-knowledge machine learning, algorithmic accountability, and AI-assisted peer review. The resulting claim is deliberately narrow: remote attestation does not prove that an evaluation is fair or scientifically correct, but it can make part of the evaluation process externally verifiable.

---


### 80. [Towards Seamless Lunar Mosaics: Deep Radiometric Normalization for Cross-Sensor Orbital Imagery Using Chandrayaan-2 TMC Data](https://arxiv.org/abs/2604.25208)

**<font color=#1a73e8>作者：</font>** Pratincha Singh, Jai Gopal Singla, Prashant Hemrajani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiometric inconsistencies remain a major challenge in generating seamless lunar mosaics from multi-mission orbital imagery due to variability in illumination geometry, sensor characteristics, and acquisition conditions. This paper presents a deep learning-based radiometric normalization framework for multi-mission lunar mosaics constructed primarily from ISRO's Chandrayaan-2 Terrain Mapping Camera (TMC) data, supplemented with auxiliary imagery from the SELENE (Kaguya) mission.
The proposed approach employs a conditional generative adversarial network (cGAN) comprising a U-Net-based generator and a PatchGAN discriminator to learn a nonlinear radiometric mapping from conventionally mosaicked lunar imagery to a photometrically consistent reference derived from LROC Wide Angle Camera (WAC) data. A patch-based training strategy with overlap-aware inference is adopted to enable scalable processing of large-area mosaics while preserving structural continuity across tile boundaries.
Quantitative evaluation using Structural Similarity Index (SSIM), Peak Signal-to-Noise Ratio (PSNR), and Root Mean Square Error (RMSE) demonstrates consistent improvements over traditional histogram-based normalization techniques. The proposed framework achieves enhanced tonal uniformity, reduced seam artifacts, and improved structural coherence across multi-source lunar datasets.
These results highlight the effectiveness of learning-based radiometric normalization for large-scale planetary mosaicking and demonstrate its potential for generating high-fidelity lunar surface maps from heterogeneous orbital imagery.

---


### 81. [DiRe-RAPIDS: Topology-faithful dimensionality reduction at scale](https://arxiv.org/abs/2604.25209)

**<font color=#1a73e8>作者：</font>** Alexander Kolpakov, Igor Rivin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dimensionality reduction methods such as UMAP and t-SNE are central tools for visualising high-dimensional data, but their local-neighborhood objectives can preserve sampling noise while distorting global topology. We show that standard local metrics reward this noise memorisation: top-performing embeddings invent cycles and disconnected islands absent from the data. We introduce a topology-faithfulness benchmark based on noisy manifolds with known homology, tune DiRe against it, and find Pareto-optimal configurations that match or beat GPU-accelerated UMAP on classification while recovering exact first Betti numbers on stress tests. On 723K arXiv paper embeddings, DiRe preserves 3-4 times more topological structure than UMAP at comparable wall-clock.

---


### 82. [DATAREEL: Automated Data-Driven Video Story Generation with Animations](https://arxiv.org/abs/2604.25220)

**<font color=#1a73e8>作者：</font>** Ridwan Mahbub, Syem Aziz, Mahir Ahmed 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Data videos are a powerful medium for visual data based storytelling, combining animated, chart-centric visualizations with synchronized narration. Widely used in journalism, education, and public communication, they help audiences understand complex data through clear and engaging visual explanations. Despite their growing impact, generating data-driven video stories remains challenging, as it requires careful coordination of visual encoding, temporal progression, and narration and substantial expertise in visualization design, animation, and video-editing tools. Recent advances in large language models offer new opportunities to automate this process; however, there is currently no benchmark for rigorously evaluating models on animated visualization-based video storytelling. To address this gap, we introduce DataReel, a benchmark for automated data-driven video story generation comprising 328 real-world stories. Each story pairs structured data, a chart visualization, and a narration transcript, enabling systematic evaluation of models' abilities to generate animated data video stories. We further propose a multi-agent framework that decomposes the task into planning, generation, and verification stages, mirroring key aspects of the human storytelling process. Experiments show that this multi-agent approach outperforms direct prompting baselines under both automatic and human evaluations, while revealing persistent challenges in coordinating animation, narration, and visual emphasis. We release DataReel at this https URL.

---


### 83. [Value-Sensitive AI for Prayer: Balancing the Agencies Between Human and AI Agents in Spiritual Context](https://arxiv.org/abs/2604.25230)

**<font color=#1a73e8>作者：</font>** Soonho Kwon, Dong Whi Yoo, Shaowen Bardzell 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present four conceptual value-sensitive AI systems to examine how the presence of AI could influence praying experiences. Drawing on key values and practices associated with praying identified through a diary study, we designed AI systems intended to "assist" prayer practices. These designs were presented to participants through speculative design workbooks, serving as provocations to co-reflect on how the intervention of AI systems might shape their praying experiences. Our findings suggest that a sense of authenticity (or feeling a genuine connection to the divine) is a crucial value, while the presence of AI was often perceived as diminishing this authenticity, particularly when AI assumed too much agency in guiding praying practices. Based on our findings, we argue that AI system designs for deeply value-laden experiences should preserve users' agency in shaping their own experiences by maintaining interpretive openness, perhaps by leveraging AI's inexplicability as a resource for personal meaning-making or by recognizing non-use of AI as a legitimate design choice.

---


### 84. [Categorical Optimization with Bayesian Anchored Latent Trust Regions for Structural Design under High-Dimensional Uncertainty](https://arxiv.org/abs/2604.25241)

**<font color=#1a73e8>作者：</font>** Zhangyong Liang, Huanhuan Gao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Categorical structural optimization under aleatoric uncertainty is challenging because each design variable must be selected from a finite catalog of admissible instances, while each candidate design may require expensive stochastic finite-element evaluations.
Existing latent-space optimization strategies can reduce the dimensionality of catalog attributes, but they often treat the reduced space as a continuous search domain.
The resulting continuous optimum must then be rounded off to a nearby catalog instance, which may alter the objective value, constraint status, or physical interpretation of the design.
To address this issue, this paper proposes the \textbf{C}ategorical \textbf{O}ptimization with \textbf{B}ayesian \textbf{A}nchored \textbf{L}atent \textbf{T}rust Regions (\textbf{COBALT}) framework for high-dimensional categorical Optimization Under Uncertainty.
COBALT first embeds the physical catalog into a low-dimensional latent representation and locks the mapped instances as a discrete anchored graph.
A data-independent random tree decomposition is then used to provide bounded-complexity additive modeling over high-dimensional categorical variables.
On this anchored domain, an additive SAAS-GP surrogate is fitted to heteroscedastic MC-FEA observations, and a trust-region discrete graph acquisition search selects the next admissible catalog configuration without continuous relaxation or rounding-off.
The proposed strategy is applied to robust design optimization of complex bar structures, considering structural weight, strain energy, and local buckling performance.
By evaluating only valid catalog designs through the MC-FEA oracle, COBALT preserves physical admissibility throughout the active learning loop and improves the efficiency of robust categorical structural optimization.

---


### 85. [Personalized Cross-Modal Emotional Correlation Learning for Speech-Preserving Facial Expression Manipulation](https://arxiv.org/abs/2604.25255)

**<font color=#1a73e8>作者：</font>** Tianshui Chen, Yujie Zhu, Jianman Lin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Speech-preserving facial expression manipulation (SPFEM) aims to enhance human expressiveness without altering mouth movements tied to the original speech. A primary challenge in this domain is the scarcity of paired data, namely aligned frames of the same individual with identical speech but different expressions, which impedes direct supervision for emotional manipulation. While current Visual-Language Models (VLMs) can extract aligned visual and semantic features, making them a promising source of supervision, their direct application is limited. To this end, we propose a Personalized Cross-Modal Emotional Correlation Learning (PCMECL) algorithm that refines VLM-based supervision through two major improvements. First, standard VLMs rely on a single generic prompt for each emotion, failing to capture expressive variations among individuals. PCMECL addresses this limitation by conditioning on individual visual information to learn personalized prompts, thereby establishing more fine-grained visual-semantic correlations. Second, even with personalization, inherent discrepancies persist between the visual and semantic feature distributions. To bridge this modality gap, PCMECL employs feature differencing to correlate the modalities, providing more precisely aligned supervision by matching the change in visual features to the change in semantic features. As a plug-and-play module, PCMECL can be seamlessly integrated into existing SPFEM models. Extensive experiments across various datasets demonstrate the superior efficacy of our algorithm.

---


### 86. [AutoResearchBench: Benchmarking AI Agents on Complex Scientific Literature Discovery](https://arxiv.org/abs/2604.25256)

**<font color=#1a73e8>作者：</font>** Lei Xiong, Kun Luo, Ziyi Xia 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous scientific research is significantly advanced thanks to the development of AI agents. One key step in this process is finding the right scientific literature, whether to explore existing knowledge for a research problem, or to acquire evidence for verifying assumptions and supporting claims. To assess AI agents' capability in driving this process, we present AutoResearchBench, a dedicated benchmark for autonomous scientific literature discovery. AutoResearchBench consists of two complementary task types: (1) Deep Research, which requires tracking down a specific target paper through a progressive, multi-step probing process, and (2) Wide Research, which requires comprehensively collecting a set of papers satisfying given conditions. Compared to previous benchmarks on agentic web browsing, AutoResearchBench is distinguished along three dimensions: it is research-oriented, calling for in-depth comprehension of scientific concepts; literature-focused, demanding fine-grained utilization of detailed information; and open-ended, involving an unknown number of qualified papers and thus requiring deliberate reasoning and search throughout. These properties make AutoResearchBench uniquely suited for evaluating autonomous research capabilities, and extraordinarily challenging. Even the most powerful LLMs, despite having largely conquered general agentic web-browsing benchmarks such as BrowseComp, achieve only 9.39% accuracy on Deep Research and 9.31% IoU on Wide Research, while many other strong baselines fall below 5%. We publicly release the dataset and evaluation pipeline to facilitate future research in this direction. We publicly release the dataset, evaluation pipeline, and code at this https URL.

---


### 87. [Online combinatorial optimization with stochastic decision sets and adversarial losses](https://arxiv.org/abs/2604.25269)

**<font color=#1a73e8>作者：</font>** Gergely Neu, Michal Valko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most work on sequential learning assumes a fixed set of actions that are available all the time. However, in practice, actions can consist of picking subsets of readings from sensors that may break from time to time, road segments that can be blocked or goods that are out of stock. In this paper we study learning algorithms that are able to deal with stochastic availability of such unreliable composite actions. We propose and analyze algorithms based on the Follow-The-Perturbed-Leader prediction method for several learning settings differing in the feedback provided to the learner. Our algorithms rely on a novel loss estimation technique that we call Counting Asleep Times. We deliver regret bounds for our algorithms for the previously studied full information and (semi-)bandit settings, as well as a natural middle point between the two that we call the restricted information setting. A special consequence of our results is a significant improvement of the best known performance guarantees achieved by an efficient algorithm for the sleeping bandit problem with stochastic availability. Finally, we evaluate our algorithms empirically and show their improvement over the known approaches.

---


### 88. [Exploring Time Conditioning in Diffusion Generative Models from Disjoint Noisy Data Manifolds](https://arxiv.org/abs/2604.25289)

**<font color=#1a73e8>作者：</font>** Liuzhuozheng Li, Zhiyuan Zhan, Shuhong Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Practically, training diffusion models typically requires explicit time conditioning to guide the network through the denoising sampling process. Especially in deterministic methods like DDIM, the absence of time conditioning leads to significant performance degradation. However, other deterministic sampling approaches, such as flow matching, can generate high-quality content without this conditioning, raising the question of its necessity. In this work, we revisit the role of time conditioning from a geometric perspective. We analyze the evolution of noisy data distributions under the forward diffusion process and demonstrate that, in high-dimensional spaces, these distributions concentrate on low-dimensional hyper-cylinder-like manifolds embedded within the input space. Successful generation, we argue, stems from the disentanglement of these manifolds in high-dimensional space. Based on this insight, we modify the forward process of DDIM to align the noisy data manifold with the flow-matching approach, proving that DDIM can generate high-quality content without time conditioning, provided the noisy manifold evolves according to the flow-matching method. Additionally, we extend our framework to class-conditioned generation by decoupling classes into distinct time spaces, enabling class-conditioned synthesis with a class-unconditional denoising model. Extensive experiments validate our theoretical analysis and show that high-quality generation is achievable without explicit conditional embeddings.

---


### 89. [Optimization-Free Topological Sort for Causal Discovery via the Schur Complement of Score Jacobians](https://arxiv.org/abs/2604.25295)

**<font color=#1a73e8>作者：</font>** Rui Wu, Hong Xie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous causal discovery typically couples representation learning with structural optimization via non-convex acyclicity penalties, which subjects solvers to local optima and restricts scalability in high-dimensional regimes. We propose a decoupled paradigm that shifts the causal discovery bottleneck from non-convex optimization to statistical score estimation. We introduce the Score-Schur Topological Sort (SSTS), an algorithm that extracts topological order directly from unconstrained generative models, bypassing constrained structure optimization. We establish that the causal hierarchy leaves a geometric signature within the score function: iterative graph marginalization is mathematically equivalent to computing the Schur complement of the Score-Jacobian Information Matrix (SJIM) under linear conditions. This translates the acyclicity constraint into an algebraic procedure with a dominant cost of O(d^3) operations. For non-linear systems, we formulate the expectation gap of Schur marginalization and introduce Block-SSTS to compress extraction depth, bounding structural error. Empirically, SSTS allows causal structural analysis on non-linear graphs up to d=1000. At this scale, our framework indicates that once the non-convex optimization bottleneck is mathematically bypassed, the structural fidelity of continuous causal discovery is bounded by the finite-sample estimation variance of the global score geometry. By reducing graph extraction to matrix operations, this work reframes scalable causal discovery from a constrained optimization problem to a statistical estimation challenge.

---


### 90. [Visual Boosting Techniques for Spatiotemporal Dense Pixel Visualizations](https://arxiv.org/abs/2604.25298)

**<font color=#1a73e8>作者：</font>** Julius Rauscher, Frederik L. Dennig, Udo Schlegel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The analysis of spatiotemporal data is essential in domains such as epidemiology and environmental monitoring, where understanding the interplay between spatially distributed phenomena and their temporal evolution is critical. Dense pixel visualizations offer a compact, effective overview of spatiotemporal dynamics. However, the necessary linearization of 2D geographic space into a 1D ordering inevitably introduces structural distortions that manifest as visual artifacts. We propose a measure-driven visual analytics approach that captures visual artifacts through neighborhood preservation measures for 1D orderings and renders them using visual boosting techniques such as glyphs, halos, and hatching. We demonstrate our approach through a usage scenario analyzing COVID-19 incidence data across German districts, showing that interactive, measure-driven boosting enables analysts to reliably distinguish genuine spatial patterns from linearization artifacts.

---


### 91. [DenseScout: Algorithm-System Co-design for Budgeted Tiny Object Selection on Edge Platforms](https://arxiv.org/abs/2604.25300)

**<font color=#1a73e8>作者：</font>** Xiong Zhouzhi, Zimo Zeng, Yi Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deploying tiny object perception on edge platforms is challenging because practical systems must satisfy both strict compute budgets and end-to-end latency constraints. A common strategy is to first select a small number of candidate patches from a high-resolution image and then apply downstream processing only to the selected regions. However, existing detector-based frontends are not well aligned with this setting: strong offline detection accuracy does not necessarily yield effective low-budget patch prioritization, nor does it guarantee usable performance once transport and inference delays are considered. In this work, we study budgeted tiny object selection on edge platforms from a joint algorithm--system perspective. We present DenseScout, a lightweight dense-response selector with only 1.01M parameters, which directly ranks candidate patch locations from a high-resolution scene via a lightweight proxy input and is better aligned with low-budget tiny-object prioritization than detector-style frontends. To bridge offline selector quality and deployable utility, we further develop a transport-aware runtime realization on heterogeneous edge devices and adopt QoS-constrained recall, which counts a target as successfully perceived only if it is covered by the selected regions and the end-to-end processing finishes before the deadline. Experiments show that DenseScout consistently outperforms detector-based baselines in offline budgeted patch-selection evaluation, especially in low-budget regimes, while cross-platform results on RK3588 and Jetson Orin NX show that deployable performance depends jointly on selector quality and runtime realization efficiency. These results suggest that edge tiny object perception should be optimized as an algorithm--system co-design problem rather than as isolated model selection.

---


### 92. [RCProb: Probabilistic Rule Extraction for Efficient Simplification of Tree Ensembles](https://arxiv.org/abs/2604.25304)

**<font color=#1a73e8>作者：</font>** Josue Obregon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tree ensembles are widely used in industrial machine learning due to their strong predictive performance and efficient training procedures. However, as the number of trees in an ensemble grows, the resulting models become increasingly difficult for humans to interpret. To address this limitation, explainable artificial intelligence (XAI) studies methods that generate interpretable models capable of explaining complex predictors. One approach consists of extracting decision rules from tree ensembles while attempting to preserve the predictive performance of the original model. In previous work, we introduced RuleCOSI+, a greedy heuristic algorithm for extracting compact rule-based models from tree ensembles. Although RuleCOSI+ produces accurate and interpretable rule sets, it relies on repeated empirical frequency counting over the training data to estimate rule confidence, which becomes computationally expensive for large datasets. In this paper, we propose RCProb, a probabilistic reformulation of RuleCOSI+ designed to reduce the computational cost of rule extraction. RCProb estimates rule statistics using Dirichlet-smoothed class priors and Beta-smoothed condition likelihoods combined through a Naive Bayes formulation, avoiding repeated dataset scans. Experiments on 33 benchmark datasets show that RCProb maintains competitive predictive performance while reducing runtime by approximately $22\times$ compared with RuleCOSI+, while producing more compact rule sets on average.

---


### 93. [QFlash: Bridging Quantization and Memory Efficiency in Vision Transformer Attention](https://arxiv.org/abs/2604.25306)

**<font color=#1a73e8>作者：</font>** Sehyeon Oh, Yongin Kwon, Jemin Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> FlashAttention improves efficiency through tiling, but its online softmax still relies on floating-point arithmetic for numerical stability, making full quantization difficult. We identify three main obstacles to integer-only FlashAttention: (1) scale explosion during tile-wise accumulation, (2) inefficient shift-based exponential operations on GPUs, and (3) quantization granularity constraints requiring uniform scales for integer comparison. To address these challenges, we propose \textit{QFlash}, an end-to-end integer FlashAttention design that performs softmax entirely in the integer domain and runs as a single Triton kernel. On seven attention workloads from ViT, DeiT, and Swin models, QFlash achieves up to 6.73$\times$ speedup over I-ViT and up to 8.69$\times$ speedup on Swin, while reducing energy consumption by 18.8\% compared to FP16 FlashAttention, without sacrificing Top-1 accuracy on ViT/DeiT and remaining competitive on Swin under per-tensor quantization. Our code is publicly available at this https URL.

---


### 94. [Rapid tracking through strongly scattering media with physics-informed neuromorphic speckle analysis](https://arxiv.org/abs/2604.25310)

**<font color=#1a73e8>作者：</font>** Yuqing Cao, Shuo Zhu, Rongzhou Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This work addresses the critical problem of tracking fast-moving objects through strongly scattering media in a low-light environment. Different from existing approaches that use frame-based cameras with fixed exposure times, which trade off signal-to-noise ratio for temporal resolution, we introduce computational neuromorphic tracking (CNT), a physics-informed framework that combines asynchronous event sensing with task-driven speckle analysis for robust motion estimation. We formulate the neuromorphic speckle aggregation as a spatiotemporal speckle representation, jointly optimizing the temporal and spatial parameters to maximize tracking stability under extreme conditions. Extensive experiments demonstrate that our method enables robust motion tracking of 10x faster motion and under 10x dimmer illumination compared to conventional systems. These improvements significantly broaden the operational regime for tracking through scattering media, providing an efficient and scalable solution for demanding scenarios involving rapid motion and low-light conditions.

---


### 95. [Author response to commentaries on H is for Human and How (Not) to Evaluate Qualitative Research in HCI](https://arxiv.org/abs/2604.25312)

**<font color=#1a73e8>作者：</font>** Andy Crabtree  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This is the authors response to commentaries on the original article H is for Human and How (Not) to Evaluate Qualitative Research in HCI, this https URL Commentaries were provided by: Jeffrey Bardzell, this https URL Alan Blackwell, this https URL Paul Dourish, this https URL Bonnie Nardi, this https URL Peter Pirolli, this https URL Jennifer Rode, this https URL Peter Tolmie, this https URL Please feel free to copy, redistribute, adapt, and build on any part of this article in accordance with the CC BY 4.0 license: this https URL

---


### 96. [Golden RPG: Confidence-Adaptive Region-Aware Noise for Compositional Text-to-Image Generation](https://arxiv.org/abs/2604.25314)

**<font color=#1a73e8>作者：</font>** Hao Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Compositional text-to-image (T2I) generation requires a model to honour multiple sub-prompts that describe distinct image regions. Recent work shows that the \emph{starting noise} of a diffusion model carries significant semantic information: ``golden'' noise predicted from text can substantially raise prompt fidelity. We observe that this noise prediction is, however, fundamentally global: the same network is asked to summarise a long, multi-region prompt with a single text embedding, which becomes the bottleneck whenever the prompt describes scenes with spatially-separated entities. We introduce \textbf{Golden RPG}, a region-aware noise predictor that extends a frozen NPNet with two trainable additions: (i) a per-region \textbf{FiLM adapter} that reshapes the predicted noise according to each sub-prompt; and (ii) a \textbf{Region Cross-Attention} layer injected between two stages of the Swin backbone, allowing different spatial locations to attend to different sub-prompt tokens. To prevent the regional conditioning from degrading samples whose prompts are already easy, we further propose a \textbf{Confidence-Adaptive Blending} head that dynamically predicts, per sample, how strongly the regional signal should override the global signal. We evaluate on the original RPG benchmark (20 prompts, 100 samples) and on four multi-region categories of T2I-CompBench (1{,}200 images, six competing methods). Golden RPG achieves the highest Cross-Region-Coherence score on every category, while matching the strongest baselines on absolute CLIP-Score and CLIP-IQA. A paired user study further shows a $\boldsymbol{\sim}$67\% preference over the strongest baseline. The adapter contains $\sim$2M trainable parameters and adds only $0.6$\,s of inference overhead on top of SDXL.

---


### 97. [SaliencyDecor: Enhancing Neural Network Interpretability through Feature Decorrelation](https://arxiv.org/abs/2604.25315)

**<font color=#1a73e8>作者：</font>** Ali Karkehabadi, Jamshid Hassanpour, Houman Homayoun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gradient-based saliency methods are widely used to interpret deep neural networks, yet they often produce noisy and unstable explanations that poorly align with semantically meaningful input features. We argue that a fundamental cause of this behavior lies in the geometry of learned representations: correlated feature dimensions diffuse attribution gradients across redundant directions, resulting in blurred and unreliable saliency maps. To address this issue, we identify feature correlation as a structural limitation of gradient-based interpretability and propose SaliencyDecor, a training framework that enforces feature decorrelation to improve attribution fidelity without modifying saliency methods or model architectures by reshaping the feature space toward orthogonality, our approach promotes more concentrated gradient flow and improves the fidelity of saliency-based explanations. SaliencyDecor jointly optimizes classification, prediction consistency under feature masking, and a decorrelation regularizer, requiring no architectural changes or inference-time overhead. Extensive experiments across multiple benchmarks and architectures demonstrate that our method produces substantially sharper and more object-focused saliency maps while simultaneously improving predictive performance, achieving accuracy gains across the datasets. These results establish our method as a principled mechanism for enhancing both interpretability and accuracy, challenging the conventional trade-off between explanation quality and model performance.

---


### 98. [Towards Robust Deep Learning-based Rumex Obtusifolius Detection from Drone Images](https://arxiv.org/abs/2604.25316)

**<font color=#1a73e8>作者：</font>** Fabian Dionys Schrag, Mehmet Ozgur Turkoglu, Konrad Schindler 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Domain adaptation (DA) addresses the challenge of transferring a machine learning model trained on a source domain to a target domain with a different data distribution. In this work, we study DA for the task of Rumex obtusifolius (Rumex) image classification. We train models on a published, ground vehicle-based dataset (source) and evaluate their performance on a custom target dataset acquired by unmanned aerial vehicles (UAVs). We find that Convolutional Neural Network (CNN) models, specifically ResNets, generalize poorly to the target domain, even after fine-tuning on the source data. Applying moment-matching and maximum classifier discrepancy, two established DA techniques, substantially improves target-domain performance. However, Vision Transformer (ViT) models pretrained with self-supervised objectives (DINOv2, DINOv3) handle domain shifts intrinsically well, surpassing even moment-matching-trained ResNets, likely due to the rich, general-purpose representations acquired during large-scale pretraining. Using ViTs fine-tuned on the source dataset, we demonstrate high classification performances in the range of F1=0.8 on our target dataset. To support further research on DA for weed detection in grassland systems, we publicly release our UAV-based target dataset AGSMultiRumex, comprising data from 15 flights over Swiss meadows.

---


### 99. [Edge-Cloud Collaborative Reconstruction via Structure-Aware Latent Diffusion for Downstream Remote Sensing Perception](https://arxiv.org/abs/2604.25319)

**<font color=#1a73e8>作者：</font>** Yun Li, Xianju Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The exponential surge in high-resolution remote sensing data faces a severe bottleneck in satellite-to-ground transmission. Limited downlink bandwidth forces the use of extreme high-ratio compression, which irreversibly destroys high-frequency structural details essential for downstream machine perception tasks like object detection. While current super-resolution techniques attempt to recover these details, regression-based methods often yield over-smoothed textures, and generative diffusion models frequently introduce structural hallucinations that mislead detection systems. To address this trade-off, we propose the Structure-Aware Latent Diffusion (SALD) framework, an asymmetric edge-cloud collaborative SR system. At the resource-constrained edge, the system decouples imagery into a highly compressed low-frequency payload and a lightweight soft structural prior. Transmitting this decoupled representation minimizes bandwidth consumption. On the powerful cloud side, we introduce a Structure-Gated Large Kernel (SGLK) module and a Semantic-Guidance Engine (SGE) within the diffusion backbone. These modules leverage the transmitted structural priors to gate large-kernel convolutions, effectively capturing long-range dependencies inherent in aerial scenes while actively suppressing generative hallucinations. Extensive experiments on both the MSCM and UCMerced datasets demonstrate that, even under extreme bandwidth constraints, SALD achieves superior perceptual quality (LPIPS) and significantly enhances downstream performance in both scene classification and small-target detection.

---


### 100. [Assessment of the quantitative impact of occlusal positioning splints on temporomandibular joint conditions](https://arxiv.org/abs/2604.25322)

**<font color=#1a73e8>作者：</font>** Agnieszka Anna Tomaka, Krzysztof Domino, Dariusz Pojda 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A computational method for quantitative analysis of temporomandibular joint (TMJ) configuration using occlusal positioning splints is proposed and demonstrated. The method models a positioning splint as a physical realization of a predefined rigid transformation of the mandible, derived from multimodal data, including CBCT, facial motion acquisition, and dental scans integrated within a common coordinate system. Splints corresponding to selected mandibular positions are designed and fabricated, and their positioning accuracy is evaluated using repeated scans of plaster models. Discrepancies are represented as error transformations and analyzed statistically in the space of rigid motions. The estimated transformations are propagated to segmented TMJ structures, enabling simulation-based evaluation of joint space changes. Transformation-based error analysis and surface distance metrics are used to quantify differences between planned and achieved configurations. The method enables indirect assessment of TMJ configuration using a single anatomical model and transformation data, reducing the need for repeated imaging across multiple mandibular positions. This study is intended as a methodological demonstration, supported by a clear step-by-step graphical presentation, and does not aim to provide clinical validation.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-190](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
