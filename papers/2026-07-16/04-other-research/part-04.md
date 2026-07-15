# 📦 其他研究 | 2026年07月16日

> 本类共 **203** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-203](./part-05.md)

---

### 151. [The Geometry of Memorization: Finite-Time Spectral Sensitivity as a Diagnostic for Flow Matching Models](https://arxiv.org/abs/2607.12616)

**<font color=#1a73e8>作者：</font>** Shuchan Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous-time generative frameworks construct probability paths between base and target domains by optimizing time-dependent velocity fields. While theoretical targets favor straight trajectories, empirical networks develop complex path deformations. This paper presents the Finite-Time Spectral Sensitivity (FTSS) g(t), a gradient-free, forward-pass metric that exposes flow geometry by tracking the root-mean-square singular value of the state-transition matrix. Serving as a continuous proxy for stable rank, g(t) reveals a distinct geometric pathology under data scarcity: while generalizing models maintain stable effective dimensions, overfitting causes a spectral collapse. We leverage this structural phenomenon to develop an internal geometric audit based on g(t). Our framework detects generative memorization using purely internal trajectory dynamics, removing the need for external membership queries or baseline data comparison.

---


### 152. [KnowAct-GUIClaw: Know Deeply, Act Perfectly, Personal GUI Assistant with Self-Evolving Memory and Skill](https://arxiv.org/abs/2607.12625)

**<font color=#1a73e8>作者：</font>** Yunxin Li, Jinchao Li, Shibo Su 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> OpenClaw has emerged as a leading agent framework for complex task automation, yet it faces insufficient cross-platform GUI interaction support and a well-built self-evolution mechanism. These flaws limit its adaptation to diverse device ecosystems and prevent performance improvements through continuous learning from execution experience. To resolve these issues, we propose the Know Deeply, Act Perfectly paradigm for personal assistants, which holds that accumulated user interaction and task-running experience directly improve execution accuracy and efficiency, unifying cognitive comprehension and operational execution. Based on this paradigm, we introduce KnowAct-GUIClaw, a novel Know-Route-Act-Reflect framework designed to address OpenClaw's GUI manipulation deficits and break through its cross-platform and recursive self-improvement constraints. First, the host agent leverages accumulated interaction experience and task-relevant knowledge for long-horizon task decomposition and allocation (Know). Second, a pluggable GUI subagent with an experience-attributable memory system (Know) and self-evolving skill library (Act), enabling seamless cross-platform migration and fast-path integration. Especially, this framework continuously stores user profiles and feedback to improve the accuracy of task decomposition and tool calls. Extensive experiments across Android, iOS, HarmonyOS and Windows show that KnowAct-GUIClaw achieves superior efficiency, accuracy and cross-platform adaptability. Especially, the GUIClaw with open-source Kimi-2.6 models achieves the best performance (64.1%) on the long-horizon MobileWorld benchmark, beating all agentical frameworks and closed-source agentical models, e.g., Seed-2.0-Pro and GPT-5.5. Additionally, the knowledgeable memory and execution skills supported by our framework are transferable across diverse base models, improving by 8.5% with Kimi-2.6.

---


### 153. [Learning Forced Multibody Dynamics on Lie Groups](https://arxiv.org/abs/2607.12627)

**<font color=#1a73e8>作者：</font>** Martine Dyring Hansen, Marta Ghirardelli, Elena Celledoni 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose an architecture for learning the dynamics of mechanical systems based on discrete forced Euler-Lagrange equations on Lie groups using only position data. By formulating the dynamics directly on manifold-valued configuration spaces, the method naturally respects the geometric structure of the systems and preserves geometric invariants and conservation laws. The reliance on position measurements alone makes the framework applicable in settings where velocity data are unavailable or noisy. The approach extends naturally to multibody systems, accommodates external control inputs, and demonstrates strong performance on both synthetic and real-world datasets.

---


### 154. [Atomic Units of X: The Compression Layer of Intelligence](https://arxiv.org/abs/2607.12634)

**<font color=#1a73e8>作者：</font>** Sachin Dev Duggal, Pradyumna Swarnalatha Ramanna, Alexandros Vassiliades  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper proposes a theoretical framework for understanding intelligence as a process of atomic compression and compositional reuse. We argue that cognitive, biological, computational, and organizational systems achieve scalable intelligence by decomposing complex phenomena into reusable atomic units that can be recombined into higher-order structures. Drawing on evidence from cognitive science, information theory, evolutionary biology, software engineering, medicine, legal reasoning, education, music, and artificial intelligence, the paper develops the concept of atomic units as fundamental compression layers that support efficiency, transfer, interpretability, and evolvability. The central contribution is the Compression Calculus, a formal framework for comparing surface-level representations with atomic representations and for describing how compression gains compound across abstraction layers. We introduce the Compounding Cascade thesis, according to which each additional layer of abstraction multiplicatively increases representational efficiency rather than merely adding incremental savings. The paper further argues that contemporary AI systems often operate at suboptimal levels of representation, relying on token-level processing or document-level retrieval rather than stable, concept-level atomic structures. In this view, large language models are best understood not as complete knowledge architectures, but as dynamic fusion engines capable of navigating, sequencing, and recombining atomic units. The framework provides a foundation for designing self-evolving knowledge systems that can discover, refine, and compose new primitives over time. By reframing intelligence as compression through compositional abstraction, the paper offers a unifying perspective on expertise, knowledge representation, explainable AI, and the future architecture of adaptive intelligent systems.

---


### 155. [AdaPCLA: Adaptive Prior-Calibrated Logit Adjustment for Long-Tailed Longitudinal EHR Generation](https://arxiv.org/abs/2607.12645)

**<font color=#1a73e8>作者：</font>** Shuai Cui, Chen Wenxuan, Wenjie Du 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative modeling of longitudinal Electronic Health Records is increasingly important for privacy-preserving research, yet standard autoregressive models tend to underrepresent the co-occurrence structure of tail events (i.e., diseases, symptoms), reducing the fidelity and faithfulness of generated data for rare subpopulations. To this end, we propose AdaPCLA framework, which enables generative models to adaptively fit and generate EHR data through a data distribution-aware training strategy; this is achieved by internalizing data knowledge parameters by simulated annealing training. It also supports training-free adaptation to a diverse clinical population for generation through zero-shot distribution control. Moreover, our theoretical analysis characterizes rare-code logit updates through the label-wise empirical NTK and derives a prior-internalization bound for how annealing speed and NTK conditioning affect retained prior signals. Experiments on real-world data show that AdaPCLA achieves consistent gains in tail plausibility, downstream utility, and zero-shot control; in particular, it improves TailPairSeen over HALO by 114.2% on MIMIC-III and 65.1% on MIMIC-IV, outperforms GPT-style generation by 3.5% F1 for zero-shot cross-population adaptation.

---


### 156. [Extractable Memorization From First Principles](https://arxiv.org/abs/2607.12649)

**<font color=#1a73e8>作者：</font>** A. Feder Cooper, Marika Swanberg, Jamie Hayes 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work on extractable memorization in LLMs suffers from two contrasting validity problems. Some studies overstate extraction, e.g., relying on sequences too short to distinguish memorization from predictability. Others imply that extraction is unreliable evidence of memorization, since models can also reproduce real-world text they weren't explicitly trained on. In different ways, both overlook what makes a valid extraction claim: the model must generate a training sequence with high enough probability to indicate memorization. To determine what's high enough, one has to perform a matched comparison: measuring the generation probabilities of both the training sequences of interest and comparable non-training sequences. Because non-training sequences cannot have been memorized, their probabilities provide a baseline for predictability; a training sequence exceeding this baseline provides evidence of memorization. We formalize matched comparisons in two ways: (1) a conformal test that calibrates a threshold to a chosen FPR when training and non-training sequences are sampled from populations, and (2) a census that calibrates against a matched non-training document when the object is a single document (e.g., a book). We show that matched comparisons enable rigorous, calibrated memorization claims, and reveal where prior setups have validity issues. For instance, on Wikipedia OLMo 2 32B reproduces non-training 10-token suffixes roughly 24% as often as training ones: that share of the training generation rate reflects false positives, not memorization. For Llama 3.1 70B on books, the thresholds we calibrate are as low as 1e-27, supporting memorization claims for sequences that no feasible sampling budget would extract. Based on these results, we refine "extractable memorization" to require a valid memorization claim and near-certain generation within a realistic budget.

---


### 157. [MAGE: Color-Invariant and Spatial Knowledge Distillation for Gastric Neoplasm Classification](https://arxiv.org/abs/2607.12663)

**<font color=#1a73e8>作者：</font>** Jiho Jun, Jeongwon Woo, Jaemin Song 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate differentiation between gastric adenoma and carcinoma during endoscopy is critical for clinical decision-making. Yet, this task is highly challenging due to high inter-class similarity and ambiguous boundaries between the two classes. Existing ROI-based classification methods often suffer from detection/segmentation error propagation and loss of surrounding global context. In contrast, full-image classification lacks the necessary spatial focus. Furthermore, we observe that deep neural networks gravitate towards domain-specific texture biases(e.g. bleeding, lighting artifacts), often causing models to predict based on spurious correlations instead of intrinsic morphological features. To address these limitations, we propose a novel framework, Masked Achromatic Guidance Expert (MAGE). During training, we introduce an auxiliary local expert branch trained on masked achromatic views of the neoplasm. By suppressing background context and color, this branch is forced to learn highly discriminative, purely structural features. We then employ a dual-objective distillation strategy, transferring both classification logits and spatial attention maps to provide implicit spatial supervision to the main branch that receives full WLI as input. This dual-objective distillation forces the model to ground its predictions in morphology rather than relying on shortcuts, while still retaining clinically relevant color cues. At inference time, our deployable model operates on images without annotated masks, ensuring real-time deployability . Extensive experiments on a clinical gastric endoscopy dataset show that our method significantly outperforms existing detection-based methodologies (e.g. YOLO) and classification-based methodologies (e.g. Swin-Transformer), providing not only superior classification performance but also interpretable attention maps for clinical reliability.

---


### 158. [Text-Aided Multi-Modal Panoptic Symbol Spotting for CAD Floor Plan Drawings](https://arxiv.org/abs/2607.12678)

**<font color=#1a73e8>作者：</font>** Yan Gong, Bohao Li, Bowen Du 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computer-Aided Design (CAD) floor plan drawings contain both graphical primitives and textual annotations, which provide complementary geometric and semantic cues for intelligent design understanding. Among CAD analysis tasks, panoptic symbol spotting has become increasingly important with the growing demand for industrial digitalization and deep learning-based automation. However, most existing methods remain primarily primitive-centric and underexploit textual annotations, despite their critical semantic value. Even the few text-aware approaches often treat annotations only superficially, without properly modeling complex syntax and hierarchical semantics of CAD annotations, which leads to semantic loss and suboptimal spotting performance. To address these limitations, we propose TextCAD, a multimodal framework that jointly models graphical primitives and textual annotations for panoptic symbol spotting. Specifically, we design a Type-Attribute Correlation Encoder (TACE) to explicitly encode the compositional semantics within annotations by jointly modeling their types and attributes. We further introduce a Semantic Hierarchy Alignment framework with Multi-level Semantic Filtering (MSF) and primitive downsampling, which adaptively aligns annotation semantics with graphical primitives at different semantic levels and enables accurate cross-modal semantic injection and fusion. Experiments on real-world building-design datasets show that TextCAD effectively improves symbol spotting performance and achieves state-of-the-art results.

---


### 159. [ReflectVLN: Training Vision-Language Navigation Agents with Reflective Reasoning](https://arxiv.org/abs/2607.12680)

**<font color=#1a73e8>作者：</font>** Jiahang Wang, Yirong Yang, Yanqing Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing vision-language navigation methods often couple a VLM with waypoint decoders to produce multi-step action plans, but they typically lack an explicit closed-loop mechanism for tracking semantic progress, diagnosing execution failures, and recovering from error accumulation in long-horizon navigation. To address this gap, we propose ReflectVLN, an agentic VLN framework that organizes decision-making through bidirectionally interactive intention and execution agents. The intention agent performs subtask decomposition and reflection, generating executable subtask descriptions as corrective plans. Conditioned on these descriptions, the execution agent grounds them into short-horizon actions under current observations while monitoring sub-goal progress and detecting off-track behavior. Crucially, ReflectVLN enables closed-loop bidirectional communication: the execution agent emits progress and deviation signals to trigger reflection and subtask updates on demand, and the intention agent returns structured guidance that reconditions subsequent actions for recovery. To encourage temporally coherent decisions with interpretable intermediate rationales, we introduce Action Chain-of-Thought (Action-CoT), a path-conditioned dual-query training scheme for action generation. Experiments on standard VLN benchmarks show that ReflectVLN improves success rates and path efficiency under a constrained data budget, with favorable training cost and fewer high-level intention calls at inference time, while providing interpretable intermediate decisions for analysis and collaboration. Code is available at: this https URL

---


### 160. [MambaPSA: A Mamba-based Replacement for C2PSA in YOLO26](https://arxiv.org/abs/2607.12681)

**<font color=#1a73e8>作者：</font>** Sheng-Wei Chan, Chia-Min Lin, Hsin-Jui Pan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> State space models (SSMs), notably Mamba, have recently emerged as efficient alternatives to self-attention with linear computational complexity. We investigate the integration of Mamba into YOLO26, the latest non-maximum suppression (NMS)-free object detection framework, by proposing MambaPSA, a lightweight Mamba-based replacement for the C2PSA block at the end of the backbone. To complement this study, we additionally insert a bidirectional Vision Mamba (BiViM) module at the P3, P4, and P5 levels of the neck. Experiments on PASCAL VOC 2007+2012 show that MambaPSA reduces parameters by 2.9%, FLOPs by 12.1%, and improves CPU inference throughput by 17.6% (from 17 to 20 FPS) with negligible accuracy change (-0.1 mAP50:95), while the P4 BiViM placement yields the best accuracy gain (+0.9 mAP50:95). These results suggest that SSMs offer a favorable efficiency-accuracy trade-off when replacing attention-based blocks in NMS-free lightweight detectors.

---


### 161. [Lesion Segmentation in Moderate to Severe Traumatic Brain Injury: An nnU-Net Based Approach with Adaptive Normalization in the AIMS-TBI 2025 Challenge](https://arxiv.org/abs/2607.12684)

**<font color=#1a73e8>作者：</font>** Inhwa Son, Gaeun Lee, Sohyeon Sim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The segmentation of lesions in Moderate to Severe Traumatic Brain Injury (msTBI) from T1-weighted MRI presents a significant clinical challenge due to the profound heterogeneity of lesion characteristics in terms of size, shape, and location. To address this, the AIMS-TBI 2025 Challenge was organized to promote the development of robust and accurate segmentation algorithms. In this paper, we present our deep learning-based solution. Our methodology employs the nnU-Net framework with an adaptive intensity normalization strategy confined to the brain parenchyma, effectively reducing inter-subject variability and mitigating artifacts from non-brain structures. Upon final evaluation on the held-out test set, our method demonstrated highly competitive performance on the official leaderboard, achieving an Overall Dice Coefficient of 0.6305. The model obtained a Dice score of 0.4805 for lesion segmentation and 0.9324 for non-lesion tissue. While the lesion Dice reflects the difficulty of detecting highly heterogeneous lesions, the high non-lesion Dice primarily indicates the model's strong ability to correctly identify non-lesion voxels, demonstrating good specificity in differentiating lesion from non-lesion regions. These results demonstrate that incorporating anatomically constrained normalization within the nnU-Net pipeline is a powerful and effective strategy for tackling the complexities of msTBI lesion segmentation.

---


### 162. [From Critic to Confidence: PPO for Language-Based Quantitative Prediction with Confidence Estimation](https://arxiv.org/abs/2607.12687)

**<font color=#1a73e8>作者：</font>** Mehak Dhaliwal, Rasta Tadayon, Andong Hua 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs can perform language-based quantitative prediction from unstructured inputs, but remain susceptible to hallucinations and overconfident errors, making it critical to know not only what a model predicts, but when its predictions can be trusted. We introduce CARE-PPO, a reinforcement learning framework that establishes a connection between loss prediction for uncertainty estimation and actor-critic PPO fine-tuning, enabling joint learning of accurate numerical estimates and reliable confidence signals in language-based quantitative prediction. CARE-PPO uses a Confidence-Aligned Reward for Estimation, defined as a function of prediction error, to provide dense error-aware feedback to the actor while inducing the critic to learn a value function aligned with prediction quality. During inference, we repurpose the critic as a confidence estimator. Across two real-world tasks in healthcare and finance and two Qwen-3 model scales (4B and 8B), CARE-PPO achieves strong quantitative prediction performance, while producing significantly better-aligned confidence estimates through the critic than logit-based and verbalized baselines. These gains persist under realistic out-of-distribution settings across domains, spanning linguistic and domain shifts. Finally, CARE-PPO reduces task-specific overfitting on general instruction-following prompts, consistent with the broader generalization advantages of RL fine-tuning over supervised approaches.

---


### 163. [Label-Decoupled Style Augmentation for Domain Generalization in Multi-Label Remote Sensing Scene Classification](https://arxiv.org/abs/2607.12704)

**<font color=#1a73e8>作者：</font>** Alaa Almouradi, Erchan Aptoula  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-label classification assigns several co-occurring labels to each aerial scene, yet deployed models often encounter data distributions different from their training. Feature-statistics augmentation such as MixStyle, EFDMix, and correlated style uncertainty improves generalization at low cost but perturbs channel statistics globally, treating each image as a single style; one class can then contaminate the augmentation of another. Domain generalization is understudied for multi-label remote sensing; no prior method or multi-source benchmark targets it. A label-decoupled augmentation framework is therefore proposed, confining style perturbation to label-specific regions. Per-label attention, obtained from a learnable module or from gradient class-activation maps, yields per-label feature statistics; these statistics are mixed with cross-domain samples that share present labels, under independent per-label coefficients, and features are recomposed by attention-weighted normalization. Three operators combined with two attention sources produce six variants, evaluated on a leave-one-domain-out benchmark from multi-label UCM, AID, and DFC15 over six shared labels. Averaged over three splits and five seeds, the best variant attains 71.5% mean average precision, exceeding empirical risk minimization by 5.0 points and the strongest global-statistics baseline by 1.3 points, with the largest gain on the hardest transfer (up to 7.7 points). Ablations indicate that spatial attention and refreshed localization maps are most influential. The framework adds at most 0.35% parameters, leaves inference unchanged, and appears to offer a generic, inexpensive upgrade path for multi-label statistics-based domain generalization. Code is available upon acceptance at this https URL.

---


### 164. [Bulkhead: Automated Semantic Detection and Remediation of Container Escape Vulnerabilities](https://arxiv.org/abs/2607.12723)

**<font color=#1a73e8>作者：</font>** Qiyuan Fan, Zhi Li, Junjie Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Filesystem isolation in container ecosystems is often weakened by cross-boundary path misresolution, causing path traversal (PaTra) vulnerabilities. These vulnerabilities stem from insecure host-container interactions and have become increasingly pervasive as cloud systems mount shared resources, such as GPUs and agent workspaces, into containers to support AI workloads. Existing defenses remain inadequate. Kernel-level protections are intrusive, can destabilize system calls, and have therefore not been accepted into the Linux mainline. Detection methods rely on static rule matching or manual code auditing. Static rules can flag path-related functions but fail to capture the semantics needed to determine whether a host-container interaction exists, causing many false positives. Manual review requires domain expertise, making it costly, inefficient, and difficult to scale.
To address this threat, we present Bulkhead, an automated framework that integrates large language models (LLMs) with formal methods for semantic vulnerability discovery and remediation. Bulkhead uses a multi-agent system to identify and repair PaTra vulnerabilities through multi-dimensional knowledge patterns generalized from known cases. It first applies high-risk functional patterns to locate entry points for cross-boundary interactions in containerized code, then uses call-chain patterns to recover the corresponding execution paths at suitable depth. The Detection pipeline analyzes these call chains against the application scenarios and threat model, identifying vulnerabilities such as missing security checks and TOCTOU flaws in cross-boundary interactions, and generating proof-of-concept (PoC) exploits for validation. These PoCs then guide patch generation. To ensure remediation correctness, the Patch pipeline performs assertion-driven verification using predefined model-checking templates.

---


### 165. [Learning-based Probabilistic Load Forecasting with Post-hoc and In-model Uncertainty](https://arxiv.org/abs/2607.12730)

**<font color=#1a73e8>作者：</font>** Sarah Al-Shareeda, Gulcihan Ozdemir, Heung Seok Jeon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Smart-building load forecasters are often trained offline on dense, multivariate, high-frequency data, but deployment may provide only hourly, feature-limited inputs. Missing features must then be reconstructed, and their errors can propagate through the model. If this input uncertainty is not reflected, prediction intervals may become miscalibrated, affecting demand-response scheduling. Our work examines where uncertainty should be placed once inference inputs are reconstructed. We develop a unified one-day-ahead probabilistic forecasting framework that aligns temporal resolution, reconstructs the unavailable inputs, and derives causal features, and we compare a modular post-hoc residual-quantile scheme with an integrated in-model quantile-learning scheme. The comparison uses three mid-scale Deep Learning (DL) backbones: recurrent, hybrid recurrent, and attention-based Temporal Fusion Transformer (TFT) models, under identical inputs, forecasting horizon, preprocessing rules, and training budgets. Results show that uncertainty placement is backbone-dependent. Integrated quantile learning is most reliable with the TFT, yielding 2.2-3.6% MAPE and 28-83W RMSE on the labeled test window, while producing intervals about 5x narrower than the modular intervals at the closest-to-nominal coverage level. Diebold-Mariano tests support the TFT ranking and the mixed behavior of the recurrent backbones. A reconstruction-sensitivity test shows that reconstructed inputs increase the Quantile Score (QS) by 106% while interval width remains nearly unchanged, indicating that the model does not automatically absorb reconstruction-induced uncertainty. Robustness checks against non-DL baselines and seasonal hold-out weeks support this ranking. Our results expose the limits of post-hoc residual quantiles when inference depends on reconstructed inputs.

---


### 166. [What Makes a Representational Prior Work? Feature Families, Label-Free Invariances, and Critical Windows in Grokking](https://arxiv.org/abs/2607.12735)

**<font color=#1a73e8>作者：</font>** Gunner Levi Howe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Companion work showed the grokking delay is causally the time to form task-structured representations, injectable via a contrastive prior. Here we characterize what makes such a prior work, across four axes, in 188 new runs. Content: a coherent, learnable prior built from the wrong feature family (magnitude bands) blocks generalization like a random partition (1/15 vs 0/20 grok; $p=0.43$ between them), confirming the companion's prediction that priors act at the level of the circuit's features. Supervision: a fully label-free invariance prior -- positives are commuted pairs $(a,b)\sim(b,a)$ only -- generalizes in 15/15 runs at a median $2.7\times$ speedup, more reliably than the label-supervised prior itself ($p=0.038$), and combined with a weight-norm clamp yields the strongest method we test (median $17\times$, 5/5) -- strongest meaning reliably fast: plain cross-entropy with a clamp matches this speed only at the exact critical norm, while the prior keeps it fast across the entire clamp range. Timing: the prior is only needed early -- applied solely during the first 2000 epochs (4% of budget) it generalizes 10/10 at $2.7\times$, beating continuous application (8/10, $1.25\times$) and a duration-matched later window ($2.1\times$). Setting: the dissociation replicates on modular multiplication and across depths and normalization variants, and a clamp sweep quantifies the companion's central claim: structure injection flattens the weight-norm delay-law exponent about 17-fold (plain cross-entropy slows $31\times$ per +10 norm units, a lower bound as higher cells are censored, versus $1.22\times$ with the prior). Honest boundary: tasks that generalize before memorizing have no delay to control. Feature-family alignment decides whether a prior permits generalization; invariance content suffices for acceleration without labels; a brief early window captures nearly all of the benefit.

---


### 167. [Aïra: Rethinking AI Research Assistants for Interdisciplinary Science](https://arxiv.org/abs/2607.12736)

**<font color=#1a73e8>作者：</font>** Diya Mirji, Tiffany Degbotse, Sharmil Nanjappa 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Scientific discovery increasingly depends on interdisciplinary teams whose members contribute distinct expertise, conceptual frameworks, vocabularies, assumptions, and standards of evidence. Today's AI research assistants are largely designed to support individual researchers through literature review, writing assistance, coding, and data analysis. While these capabilities improve personal productivity, they provide little support for the collaborative reasoning required to integrate knowledge across disciplines. We argue that AI research assistants should evolve from tools that optimize individual workflows to systems designed for interdisciplinary teams. We introduce aïra, an AI research assistant built around this idea. Rather than focusing solely on summarization or question answering, aïra identifies disciplinary perspectives, translates terminology, highlights assumptions, and synthesizes collaborative research opportunities. We describe the design principles underlying aïra, present its system architecture, illustrate its outputs through interdisciplinary research meetings, and outline future research directions for AI systems that support collaborative scholarship.

---


### 168. [Stability Buys Time: A Re-Keying Game for Encrypted Multi-Agent Control](https://arxiv.org/abs/2607.12742)

**<font color=#1a73e8>作者：</font>** Sai Sandeep Damera, John S. Baras  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Encrypted control lets a cloud coordinate a fleet of agents on fully homomorphically encrypted state, keeping their positions and commands private. The approximate scheme for real-valued control, CKKS, returns decryptions that carry the encryption noise, a key-recovery leak; the loop must decrypt to actuate, so the leak is unavoidable. Yet the security of approximate FHE is studied statically, encrypted control assumes an honest-but-curious cloud, and persistent-threat games never reach inside the cryptosystem. We model the loop's security under an advanced persistent threat as a two-phase game, passive reconnaissance then active manipulation, separated by a measured residual detector that sees only the manipulation. The passive phase reduces to the known flooding tradeoff; the active defense is re-keying, not bootstrapping, since only re-keying resets accumulated leakage. The active phase is a detection-evasion timing game: overt manipulation is caught, so the rational adversary stays stealthy, and at its Stackelberg equilibrium the defender re-keys on the laziest cadence that denies it, set by the control-theoretic fragility of the graph topology. The marginally-stable graph must re-key far more often than the well-connected one. A three-way tension among FHE precision, control accuracy, and re-key cadence sets where this game lives, between a securability floor and a static-suffices ceiling. The efficient secure point is that window, where re-keying is the price of precision efficiency. More broadly, security for an approximate cryptosystem in a feedback loop is a dynamic game whose defender's move is the scheme's own refresh, applying beyond control to any system that must repeatedly decrypt to act.

---


### 169. [Color Pass-Through via Camera-Display Coupling](https://arxiv.org/abs/2607.12746)

**<font color=#1a73e8>作者：</font>** Ruikang Li, Molin Li, Jiarui Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When a real-world scene is captured by a smartphone camera and viewed on its screen, the displayed image often differs noticeably from the original scene in color, brightness, and contrast. This gap persists despite substantial advances in both modern cameras and displays. A key reason is that most pipelines factor the high-dimensional capture-to-display process into two separately calibrated camera and display stages, and then connect them through low-dimensional color transforms, leading to information bottlenecks and inevitable error accumulation. To address this systemic challenge, we propose Color Pass-Through, an end-to-end learned framework that operates directly on captured images. Our key insight is to treat the camera and display as a coupled system rather than calibrating them in isolation. Coupling the camera and display yields two practical advantages: (1) it brings the entire real-world scenes to the display via end-to-end optimization, and (2) it allows efficient one-step calibration for each distinct observer via complete capture-to-display path. We validate Color Pass-Through using both digital and human observers. Compared with representative baselines, our method achieves an average gain of +2.0 points on a 5-point user study and more than 2x improvement on quantitative metrics, demonstrating improved reproduction of the perceived color of the original scene.

---


### 170. [Weakly Supervised Spatio-Temporal Candidate Discovery of Dairy Farm Sites from Seasonal Satellite Imagery](https://arxiv.org/abs/2607.12748)

**<font color=#1a73e8>作者：</font>** Usman Haider, Fatima Khalid, Karl Mason  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Farm site discovery from satellite imagery is a spatiotemporal candidate ranking problem because farm evidence is distributed across pasture, field boundaries, roads, buildings, and seasonal vegetation patterns. Direct farm labels are often incomplete, which makes fully supervised detection difficult. This paper proposes a weakly supervised pipeline for ranking dairy farm candidate clusters from seasonal Sentinel imagery and open map priors. The method uses aligned spring, summer, and autumn image tiles from County Cork, Ireland, with spectral bands, vegetation indices, built area indices, and a pasture channel. A Barlow Twins encoder learns multi-season tile embeddings without farm labels. In parallel, weak OpenStreetMap farm priors are split into a prior and a held-out set. Prior features support a rule-based tile score that combines farm proximity, seasonal pasture evidence, and summer greenness, while held-out features are reserved only for proxy evaluation. The rule score is smoothed over a spatial representation graph using geographic proximity and embedding similarity, and high-scoring tiles are grouped into ranked candidate clusters. From 26,722 valid tiles, the main run selects 535 high-confidence tiles and forms 71 candidate clusters. The top 5 clusters achieve 0.60 precision within 500 m and 0.80 precision within 1000 m of held-out OpenStreetMap farm features. The top 10 clusters achieve 0.40 precision within 500 m and 0.80 precision within 1000 m. The results show that seasonal representation learning and weak geographic priors can reduce large satellite image collections into compact candidate sets for human review.

---


### 171. [CRC-HGD: A Histopathological Image Dataset for Grading Colorectal Cancer](https://arxiv.org/abs/2607.12750)

**<font color=#1a73e8>作者：</font>** Elham Amjadi, Amin Bahreini, Sayed Mohammad Hasan Emami 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Colorectal cancer (CRC) is the third most common cancer worldwide and the second leading cause of cancer-related deaths globally, with approximately 1,926,425 new cases and 904,019 deaths reported in 2022. Accurate histologic grading plays a critical role in prognosis and treatment planning for colorectal adenocarcinoma. In recent years, artificial intelligence and its subcategories, including machine learning and deep learning, have been increasingly employed for automated cancer detection and classification. An appropriate and well-organized dataset is the essential first step to achieve this goal. This paper introduces CRC-HGD, a histopathological microscopy image dataset of 1,914 images obtained from 214 colorectal adenocarcinoma patients (Grade I: 106, Grade II: 75, Grade III: 33). The specimens are H&E-stained colorectal tissue sections acquired at the Poursina Hakim Research Center of Isfahan University of Medical Sciences, Iran, diagnosed between 2014 and 2019, and graded according to the World Health Organization (WHO) criteria into three grades: well-differentiated (Grade I), moderately differentiated (Grade II), and poorly differentiated (Grade III). For each specimen, four magnification levels are provided: 4x, 10x, 20x, and 40x. The dataset is accessible via Mendeley Data (this https URL) and at this http URL, where the latest version is also available. The distinctive feature of this dataset is the provision of labeled specimens across all three differentiation grades at multiple magnification levels, enabling comprehensive computational analysis of colorectal cancer grading.

---


### 172. [RFMSR: Residual Flow Matching for Image Super-Resolution](https://arxiv.org/abs/2607.12753)

**<font color=#1a73e8>作者：</font>** Shuwei Huang, Tianyao Luo, Jicheng Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image super-resolution (ISR) has witnessed remarkable progress with diffusion models and flow matching. The dominant text-to-image (T2I) based approaches leverage large-scale foundation models as generative priors, achieving impressive perceptual quality but at the cost of massive model sizes and prohibitive training expenses. Recent flow-matching-based vision-only approaches have made significant strides; however, they adopt standard flow formulations that transport from a pure Gaussian prior to the data distribution, discarding the rich structural information already present in the low-quality (LQ) input. Furthermore, existing single-step acceleration techniques often forfeit the model's multi-step inference capability. In this paper, we propose Residual Flow Matching for Image Super-Resolution (RFMSR), a vision-only framework that centers the source distribution at the LQ latent, reducing transport distance and preserving structural priors throughout the flow trajectory. We further introduce a two-phase training strategy: Phase I pretrains the velocity field via conditional flow matching, while Phase II applies end-to-end supervision to the single-step prediction while retaining the velocity loss across all timesteps, achieving high-quality single-step generation without sacrificing multi-step refinement. Extensive experiments demonstrate that RFMSR achieves comparable or even superior perceptual quality compared to state-of-the-art (SOTA) methods. The source code is available at this https URL.

---


### 173. [Practical Judgment, Virtue, and Intuition in the Use of Opaque AI-Enabled Systems](https://arxiv.org/abs/2607.12755)

**<font color=#1a73e8>作者：</font>** Nathan G. Wood, Andrew P. Rebera  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI-enabled systems are seeing increasing deployment across numerous domains, with many being "black boxes" with respect to core functions and capabilities. I.e., many systems take inputs and give outputs, but without users having any ability to see how the former lead to the latter. AI-enabled systems are also being used to augment autonomy in systems, and autonomy coupled with opacity raises numerous concerns surrounding, e.g., the reliability of systems, their regularity in functioning, human ability to control them, or whether deploying opaque and potentially autonomous systems is in compliance with ethical and legal norms. In this article, we argue that many of these worries can be mitigated by leveraging practical judgment, virtue, and intuition in the deployment and use of opaque AI-enabled systems. We show that focusing on these distinctly human capabilities provides a means for bridging between the practical challenges created by opacity and the ethical, legal, and social norms underpinning particular domains. We argue that a core element in doing this is a recognition that many positive human traits are not quantifiable and we therefore must develop training regimen and guidelines on AI deployment anchored in humanistic but non-quantifiable values. Throughout the article, we focus on the military domain as an exemplar of the importance of practical judgment, virtue, and intuition as drivers for ethical and effective human decision-making surrounding AI deployments, but the underlying arguments apply to all domains where opaque and potentially autonomous systems are being deployed (subject to domain-specific alterations).

---


### 174. [Constraint-Aware Aggregation for Federated Reinforcement Learning in Microgrid Energy Coordination](https://arxiv.org/abs/2607.12763)

**<font color=#1a73e8>作者：</font>** Usman Haider, Karl Mason  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Reinforcement Learning (FedRL) enables coordination of distributed energy resources without sharing raw local data, but standard aggregation methods such as FedAvg do not account for system-level constraints, often leading to unsafe global behavior. In this work, we study constraint-aware aggregation for federated reinforcement learning in distributed energy coordination. We propose aggregation rules that incorporate both local performance and estimated constraint violation into the server-side update. Among these, a simple penalty-based rule, $w_i \propto R_i - \alpha V_i$, consistently provides the most reliable trade-off between reward and safety, without requiring dual optimization or modifications to local training. \textcolor{black}{We evaluate our approach on DairyGridEnv, a benchmark modeling multiple farms coordinating battery storage under stochastic demand and a shared grid capacity constraint, and further assess robustness using real load-driven demand profiles from Finland and the German FIELD dataset. Across multiple seeds, penalty-based aggregation substantially reduces violations while improving reward relative to FedAvg in both synthetic and real load-driven settings.} A combined reward-violation scheme exposes a tunable trade-off via $\lambda$, but is less stable. These results demonstrate that lightweight aggregation strategies can substantially improve empirical safety in federated reinforcement learning while preserving standard communication protocols.

---


### 175. [A Scalable Cloud-Orchestrated and Service-Oriented Multi-Domain QKD Network with PQC Integration](https://arxiv.org/abs/2607.12765)

**<font color=#1a73e8>作者：</font>** Konstantinos Krilakis, Antonia Tsili, Aikaterini Mandilara 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Quantum key distribution (QKD) offers unconditional security but existing QKD networks remain difficult to scale across heterogeneous infrastructures and administrative domains due to vendor-specific interfaces, trusted-node constraints, and limited interoperability. This work presents a flexible multi-domain and multi-site quantum-secure network architecture integrating vendor-agnostic QKD, SDN orchestration, and cloud-managed trust services. Communication is based on Zero Trust Network Access protocols featuring multi-level authentication mechanisms building upon post-quantum cryptography (PQC) signature and key encapsulation algorithms. The system is deployed on a real-world testbed with domains incorporating QKD nodes from 3 vendors, as well as domains without QKD infrastructure elements. Experimental results show that PQC and SDN overhead remain relatively low even on constrained devices, with the main bottleneck being QKD key retrieval and vendor-specific key streaming limitations. The proposed framework extends quantum-safe key transport beyond native QKD boundaries while preserving flexibility, interoperability, and compatibility with existing infrastructures.

---


### 176. [Accuracy and Normalized Accuracy under Length Bias: Analysis, Guidelines, and a Bayesian Alternative](https://arxiv.org/abs/2607.12767)

**<font color=#1a73e8>作者：</font>** Koen Oostermeijer  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multiple-choice benchmarks that rank candidate completions by conditional log-probability suffer from a length bias: because log-probabilities sum over tokens, longer answers tend to be penalized relative to shorter ones in practice. A common mitigation is to normalize scores by completion length, but we show empirically that this heuristic frequently over-corrects, introducing a bias toward longer answers instead. We first analyze these scoring rules, characterizing when standard and length-normalized accuracy are appropriate and how their length biases depend on the distribution of completion lengths. Motivated by this analysis, we introduce \emph{Bayesian accuracy}, a scoring rule that computes the posterior probability of each candidate under an explicit prior over answer length, thereby removing linear length effects. Bayesian accuracy is a drop-in replacement for likelihood-based multiple-choice evaluation, requires no additional forward passes, and consistently exhibits lower empirical length bias than both standard and length-normalized accuracy across benchmarks and few-shot settings.

---


### 177. [HSEmotion Team at the 11th ABAW Challenge: Multi-Task Learning and Ambivalence/Hesitancy Video Recognition](https://arxiv.org/abs/2607.12774)

**<font color=#1a73e8>作者：</font>** Aleksei Bakin, Andrey V. Savchenko  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This article presents our results for the 11th Affective Behavior Analysis in-the-Wild (ABAW) competition. For multi-task learning with simultaneous prediction of valence, arousal, facial expressions, and action units on s-Aff-Wild2 dataset, we use frozen lightweight facial extractors, MT-EmotiDDAMFN and MT-EmotiEffNet-B0, with separate heads and systematic post-processing: temporal Gaussian smoothing, per-class expression bias, AffectNet blending, per-AU threshold tuning, and weighted backbone fusion. On the official validation set, our ensemble significantly exceeds the performance of the ConvNeXt baseline. For ambivalence/hesitancy video recognition on the expanded BAH dataset, we extend the audiovisual pipeline to video-level Macro F1 by late fusion of face, HuBERT audio, and RoBERTa text classifiers, temporal aggregation, and a global-text gate. Frame-level Weighted F1 on validation set rises from 0.74 in ABAW-8 to 0.79, while the best public-test video-level Macro F1 reaches 0.73. In both tasks, competitive performance is achieved without fine-tuning heavy backbones. These results indicate that systematic prediction calibration and lightweight multimodal fusion can rival substantially heavier end-to-end approaches while offering improved efficiency and deployment flexibility.

---


### 178. [AVQ-Attention: Adaptive Vector-Quantized Attention](https://arxiv.org/abs/2607.12789)

**<font color=#1a73e8>作者：</font>** Winfried van den dool, Patrick Forré, Amir Habibian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The $\mathcal{O}(N^2)$ complexity of attention over $N$ tokens remains a computational bottleneck in transformer models. Vector-Quantized (VQ) attention reduces this to $\mathcal{O}(MN)$ by representing keys with $M$ codewords, but applies uniform codebook capacity regardless of where attention mass concentrates: high-attention regions of key space may be coarsely approximated while low-attention regions waste representational capacity. We propose Adaptive Vector-Quantized (AVQ) Attention, which adaptively allocates codebook capacity based on attention importance. Starting from a small set of codewords, our method identifies the most important codes during the forward pass and refines them with pre-learned child codewords, achieving fine-grained quantization where it matters most while maintaining coarse quantization elsewhere. We develop an implementation using custom Triton kernels that enables the full adaptive refinement process, including importance scoring, child codeword insertion, and parent contribution replacement, to be carried out within the tiled computation paradigm of Flash Attention with minimal overhead. Our approach maintains $\mathcal{O}(MN)$ complexity while achieving improved accuracy-efficiency trade-offs compared to fixed-codebook VQ-attention.

---


### 179. [UniVR: Thinking in Visual Space for Unified Visual Reasoning](https://arxiv.org/abs/2607.12800)

**<font color=#1a73e8>作者：</font>** Zhongwei Ren, Yunchao Wei, Yao Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning broad world knowledge directly from raw visual data is a fundamental capability of intelligence. We introduce UniVR, the first investigation into simultaneously learning complex reasoning, fine-grained physical dynamics, and long-term planning from pure visual demonstrations. At its core, UniVR features VR-GRPO, a reinforcement learning paradigm with complementary global and step-level rewards. This approach enforces logical coherence and physical consistency throughout the reasoning process without requiring task-specific heuristics or image-text pairs. To train and evaluate UniVR, we construct VR-X, a large-scale benchmark curated from 16 diverse sources spanning long-horizon manipulation, spatial puzzles, and physical reasoning. It is the first comprehensive suite to assess these heterogeneous capabilities under a purely visual protocol. Remarkably, UniVR achieves up to a 25% improvement on VR-X, and its superior visual reasoning also boosts performance on various multimodal understanding benchmarks. These findings underscore the vast potential of reasoning within visual spaces, with all code, data, and models are open-sourced for further research.

---


### 180. [Breaking Déjà Vu: Independent Auditing of Visual Place Recognition through Vision-Language Reasoning](https://arxiv.org/abs/2607.12818)

**<font color=#1a73e8>作者：</font>** Sania Waheed, Michael Milford, Sarvapali D. Ramchurn 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual place recognition (VPR) is a key enabler of accurate localization and long-term autonomous navigation in robotics applications, such as loop closure detection for simultaneous localisation and mapping (SLAM). However, real-world VPR deployment relies on selecting an image matching threshold that balances precision and recall. These thresholds are typically tuned using labeled validation data and fixed during deployment, making them unreliable under environmental changes where ground truth is unavailable. This is particularly problematic in safety-critical robotics, where accepting a false loop closure can corrupt the estimated trajectory and map. In this work, we introduce Visual Place Recognition Auditing, an independent post-retrieval verification framework that leverages Vision-Language Models (VLMs) to assess retrieved matches by reasoning jointly over query and candidate images. Unlike conventional verification methods, our approach performs instance-level verification without requiring architecture-specific confidence measures, dataset-dependent thresholds, or prior knowledge of the deployment environment. We evaluate our method on six benchmark datasets using five state-of-the-art VPR methods and four VLMs. Results show that VLM-based auditing improves recall@1 by 13.6% on average as compared to state-of-the-art methods while reducing false acceptance rates to 12%, maintaining precision above 95% and coverage above 75%.

---


### 181. [Human-AI Agent Interaction as a Neuroplastic Training Environment](https://arxiv.org/abs/2607.12823)

**<font color=#1a73e8>作者：</font>** Eranga Bandara, Ross Gore, Asanga Gunaratna 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interaction with AI agents has become one of the most frequent activities of everyday digital life. Whether conversing with an assistant, working with a coding copilot, or generating images, the interaction follows a common iterative loop: a request is issued, a result returned, appraised, and the request revised. We observe that this loop is a high-frequency stream of contact events -- moments at which a result meets a person and a conditioned response may fire before deliberate appraisal -- making everyday agent interaction an unrecognised neuroplastic training environment. When a result disappoints, reactive patterns of impatience, perfectionism, frustration, and self-criticism are repeatedly evoked, and under activity-dependent synaptic plasticity each uninterrupted cycle deepens the underlying pathway through long-term potentiation. Ordinary agent use may thus quietly strengthen the very patterns it provokes. We propose that the same training environment can be engaged to the opposite effect. Treating conditioned reactive patterns as physical neurone paths -- activated through a pre-cognitive feeling tone that opens a brief regulatory gap -- we develop a framework in which, at that gap, in place of the reactive re-prompt, a person performs behind-the-scenes observation: watching the neural process operate so the cascade does not complete and long-term depression weakens the path rather than potentiation strengthening it. We characterise this practice through three layers of observation and two modes of application: a user-guided mode requiring no change to existing tools, and an agent-assisted mode in which an ordinary agent is lightly configured to support observation at the gap. We illustrate the framework through generative image prompting, showing how a single frustrating session is behaviourally nearly identical whether or not it is observed, yet neurologically opposite.

---


### 182. [Solution of the Hempel's statistical ambiguity problem and Causal AI](https://arxiv.org/abs/2607.12826)

**<font color=#1a73e8>作者：</font>** Evgenii Vityaev  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper addresses Carl Hempel's longstanding problem of statistical ambiguity in inductive-statistical inference, in which contradictory predictions are derived from statistical laws. To avoid such predictions, Carl Hempel proposed the Requirement of Maximal Specificity (RMS) for the statistical laws used in the inference. An analysis of the RMS refinements made by Wesley Salmon, Alberto Coffa, and James Fetzer led to the following definition of maximally specific statistical laws: "the lawlike premises of an adequate explanation must specify all and only those properties whose presence or absence made a difference to the occurrence of its explanandum-phenomenon." However, there was no proof of a solution to the statistical ambiguity problem based on this definition. We use Nancy Cartwright's definition of causes that raise probabilities across background contexts, and then introduce the concept of Causal Rules. Then we define a special semantic probabilistic inference procedure that incrementally refines these causal rules by incorporating all statistically relevant information. This procedure yields Maximally Specific Causal Relationships (MSCRs), for which we prove (Theorem 1) that predictions derived from them are consistent. This resolves the statistical ambiguity problem. The semantic probabilistic inference procedure provides a probabilistic causal learning system, which may be used in such new areas as Causal AI and Causal Machine Learning. They fundamentally explore causal inference as a tool for understanding cause-and-effect relationships within complex systems. Properties similar to RMS remain under discussion. Several notions related to RMS are considered: invariant feature learning, invariant causal prediction, and spurious association.

---


### 183. [GraphPolaris: A System for Query, Analysis, and Visualization of Graph Databases](https://arxiv.org/abs/2607.12845)

**<font color=#1a73e8>作者：</font>** Michael Behrisch, Sjoerd Vink, Leonardo Christino 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Graph databases are increasingly adopted as alternatives to tabular, aggregation-focused data models used in business intelligence (BI) systems such as Tableau, Power BI, and Looker. They capture complex relationships between entities, processes, and events, enabling analysis of information propagation in networks. As a result, graph analysis is central to applications such as fraud detection, social influence analysis, and supply chain resilience. Despite these advantages, existing tools do not adequately support interactive analysis of graph databases. Tabular BI systems lack mechanisms for reasoning over nodes and edges, while graph databases require specialized query languages and fragmented workflows that hinder accessibility. We present GraphPolaris, a no-code Visual Analytics system that enables users to explore, analyze, and visualize graph databases without programming skills. At its core, GraphPolaris features the GRAPHPOLARIS QUERY LANGUAGE (GPQL), a formal query grammar that facilitates flexible and composable graph queries, providing a formal foundation for analyzing relationships and graph patterns. GPQL serves as an intermediary between user interactions and the underlying database. Its formal foundation enables no-code query construction, database-agnostic query generation, and guarantees that every interaction produces a valid executable query. Informed by a formative user study, we designed GraphPolaris' interface and visualizations to lower technical barriers and foster iterative, collaborative exploration of complex networks. We evaluate GraphPolaris through two real-world case studies in telecommunications and supply-chain analysis and a 22-month-long formative mixed-method study, including a MILC-based assessment of its fit to analysts' graph analytics workflows.

---


### 184. [LARAD: Layout-Aware Road Anomaly Detection via Spatial-Logic Reasoning](https://arxiv.org/abs/2607.12858)

**<font color=#1a73e8>作者：</font>** Shiyi Mu, Xujie Chen, Shugong Xu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate open-world obstacle detection is critical for autonomous driving. Current anomaly segmentation methods suffer from a fundamental blind spot: they over-rely on texture novelty to identify out-of-distribution (OoD) objects while ignoring contextual spatial logic. Furthermore, mitigating the resulting false positives often requires cascading massive vision models, introducing unacceptable inference latency. To address these issues, we propose Layout-Aware Road Anomaly Detection (LARAD), shifting the paradigm from appearance matching to spatial-logic reasoning. First, we introduce the Spatial-Logic Violation Synthesis (SLVS) pipeline, which generates training samples that are texture-consistent yet spatially invalid, forcing the model to learn contextual violations. Second, we augment a standard closed-set segmentation network with a lightweight, OoD-guided attention branch. Extensive experiments demonstrate that LARAD significantly enhances robustness against logical anomalies and establishes a new state-of-the-art, all while retaining the high efficiency of a single-model architecture.

---


### 185. [Statistical Non-linear Reconstruction Loss for Image Anomaly Detection](https://arxiv.org/abs/2607.12866)

**<font color=#1a73e8>作者：</font>** Nguyen Minh Tri, Hoang Khuong Duy, Huynh Cong Viet Ngu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstruction-based methods are a cornerstone of unsupervised image anomaly detection, but they remain vulnerable to \emph{outlier leakage}, where standard mean squared error (MSE) loss drives the model to faithfully reconstruct anomalous patterns. We propose a Non-linear Reconstruction Loss that applies a sigmoid-based squashing function to suppress high-magnitude features, preventing outliers from dominating optimization while preserving sensitivity to normal patterns. In addition, we introduce a statistical calibration scheme that selects the scaling factor $k$ from the confidence interval (CI) of the normal feature distribution, enabling data-driven control of the suppression strength. Our approach achieves competitive or superior anomaly detection performance compared to state-of-the-art methods, reaching 99.0\% Image-AUROC and 97.3\% Pixel-AUROC on MVTec-AD, and 95.3\% Image-AUROC and 99.0\% Pixel-AUROC on VisA. These results indicate that non-linear gradient suppression is an effective mechanism for mitigating outlier leakage and improving anomaly localization in unified industrial inspection settings. The implementation is available at this https URL.

---


### 186. [Inhibited Self-Attention: Sharpening Focus in Vision Transformers](https://arxiv.org/abs/2607.12881)

**<font color=#1a73e8>作者：</font>** Peter R.D. van der Wal, Nicola Strisciuglio, George Azzopardi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) have demonstrated remarkable performance in computer vision tasks. However, their self-attention mechanism often diffuses focus across background regions, relying on spurious correlations rather than object-relevant cues. Inspired by inhibitory mechanisms observed in biological vision systems, we propose the Inhibited Self-Attention (ISA), a novel self-attention that integrates inhibitory signals to enhance feature selectivity and suppress spurious responses. In contrast to conventional self-attention, which relies solely on positive attention values due to softmax normalization, our approach retains and utilizes negative attention scores to suppress irrelevant features and sharpen focus on objects of interest. Experiments across multiple datasets, including ImageNet-1k and COCO, and several robustness benchmarks demonstrate that ISA enhances object-centric selectivity, reduces shortcut reliance, and improves out-of-distribution generalization. Our analysis of relevance maps confirms that ViTs with ISA exhibit sharper, more localized focus on object-relevant regions while reducing distractions from non-relevant (background) features, enabling more reliable models. We release our code at this https URL

---


### 187. [Energy-Based Physics-Informed Form Finding for Clustered Tensegrity Structures](https://arxiv.org/abs/2607.12888)

**<font color=#1a73e8>作者：</font>** Jing Qin, Muhao Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tensegrity form-finding and physical property prediction are fundamental inverse problems in structural mechanics, which aim to determine equilibrium configurations and internal force distributions. These problems are challenging due to strong nonlinearity arising from the coupling between geometry and forces, the need to ensure structural stability, and the enforcement of constraints such as boundary conditions and symmetry. Moreover, traditional methods often lack robustness to noise and outliers. This paper proposes an energy-based learning framework for clustered tensegrity form finding and physical property prediction. The proposed approach incorporates total potential energy minimization and constitutive relations into the training objective, enabling the simultaneous prediction of equilibrium nodal configurations and associated physical quantities, including member forces and force densities. By incorporating energy-based physical losses directly into the learning process, the framework improves physical consistency, robustness, and data efficiency. Numerical experiments on tensegrity structures, including prism and lander systems, show the great potential of the proposed approach and demonstrate its capability for scalable form finding and accurate prediction of structural properties.

---


### 188. [MemOps: Benchmarking Lifecycle Memory Operations in Long-Horizon Conversations](https://arxiv.org/abs/2607.12893)

**<font color=#1a73e8>作者：</font>** Xixuan Hao, Zeyu Zhang, Zehao Lin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term memory has become a foundational capability for LLM-based agents that accompany users across extended, multi-session interactions. Existing benchmarks, however, evaluate such memory almost exclusively through downstream question answering, scoring only the correctness of a final answer. This black-box formulation conflates the heterogeneous causes of memory failure, such as missing the introduction of a relevant fact, binding an operation to the wrong target, or relying on stale values after a correction. As a result, it can credit correct answers despite their reliance on inconsistent or unsafe memory states. In this paper, we argue that, in dynamic long-horizon interactions, memory is not a static collection of facts but a lifecycle of explicit operations, including remembering, forgetting, updating, reflecting, and their compositions. We introduce MemOps, a benchmark that reformulates conversational memory as a sequence of lifecycle operations and represents each memory event with a structured trace specifying its trigger, target, scope, state transition, and supporting evidence. A controllable generation pipeline embeds these operations into long, task-oriented conversations and produces gold operation traces together with six categories of operation-level probes, evaluated under both adjacent-evidence and long-context settings. Across long-context, retrieval-based, parametric and managed-memory systems, MemOps disentangles failure modes that final-answer accuracy alone conceals, revealing that current systems remain far from uniformly reliable. For instance, session-level retrieval outperforms turn-level retrieval, and long-context models remain notably weak at reconstructing ordered memory-state trajectories. These results move long-term memory evaluation from final-answer scoring toward interpretable, operation-level diagnosis.

---


### 189. [Contrastive-Collapsed Loss for Flexible and Geometrically Optimal Embeddings and Faster Convergence](https://arxiv.org/abs/2607.12916)

**<font color=#1a73e8>作者：</font>** Blanca Cano-Camarero, Ángela Fernández-Pascual, José R. Dorronsoro  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work, we introduce CoCo, a loss function aimed at learning normalized and well-structured representations. The proposed loss encourages intra-class collapse and inter-class contrast while preserving sufficient flexibility for neural networks to approximate geometrically optimal embeddings with large angular separation between classes. We provide a theoretical analysis positioning CoCo with respect to related objectives such as dot regression and cross-entropy, showing that the new proposed loss benefits from closer initialization to the optimal configuration, more informative gradients, and stronger incentives for class-wise representation collapse. Extensive experiments on diverse tabular datasets from the OpenML-CC18 benchmark show that CoCo achieves competitive performance with state-of-the-art methods, including kernel SVM, Random Forest, dot regression, and cross-entropy-based neural networks. In addition, both theoretical arguments and empirical analyses demonstrate that the proposal promotes tighter class clustering and faster convergence. These results highlight CoCo loss as an effective objective for learning discriminative representations while maintaining competitive predictive performance.

---


### 190. [Knowledge- and Gradient-Guided Reinforcement Learning for Parametrized Action Markov Decision Processes](https://arxiv.org/abs/2607.12924)

**<font color=#1a73e8>作者：</font>** Jonas Ehrhardt, René Heesch, Oliver Niggemann  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this paper, we study Reinforcement Learning in Parametrized Action Markov Decision Processes (PAMDP), where each decision consists of a symbolic action and numerical parameters. In such settings Reinforcement Learning algorithms typically determine parameters with one-shot estimators, which makes their training sample inefficient. Though in most PAMDP environments explicit but incomplete knowledge (e.g., rules, safety constraints, or expert heuristics) is available, it is rarely directly used to increase the sample-efficiency of training Reinforcement Learning agents. We step into this gap and propose our novel Neuro-Symbolic Knowledge- and Gradient-Guided Reinforcement Learning (KGRL) algorithm. KGRL uses domain knowledge in a Datalog knowledge base to derive the set of applicable actions and feasible parameters for a given state. This allows it to prune non-applicable actions from the decision-space and constrain the parameter spaces of the remaining actions. We then use a gradient-based parameter refinement loop to estimate the optimal parameters during training and deployment of the agent. By recording activated rules along the trajectory, KGRL additionally provides local procedural explanations on the pruning of actions and constraining of parameters. Overall, KGRL guides the agent's exploration and deployment toward feasible and constraint-aware decisions, while increasing sample efficiency during training. KGRL outperforms state-of-the-art RL baselines for PAMDPs in both, sample efficiency and episodic return.

---


### 191. [Efficient Sequential Calibration with $O(T^{2/3-ε})$ Error Bound](https://arxiv.org/abs/2607.12928)

**<font color=#1a73e8>作者：</font>** Zihan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the online binary sequential calibration problem. A recent breakthrough by \citet{dagan2024breaking} overcomes the classical \(T^{2/3}\) barrier for calibration error. Building on this result, we present an efficient randomized forecaster that achieves an expected calibration error \(O(T^{2/3-\varepsilon})\) for some constant \(\varepsilon>0\).
Our forecaster combines the \textsc{SPR-Calibration} procedure \citep{dagan2024breaking} with an outer Blackwell-style correction layer. The \textsc{SPR-Calibration} procedure controls calibration with respect to a surrogate sequence of conditional-mean estimates, while the correction layer controls the additional error incurred when these surrogates are used to approximate the true outcomes. The analysis decomposes the total calibration error into the surrogate calibration error and the residual discrepancy between the surrogate sequence and the true outcomes. The former is bounded by the \textsc{SPR-Calibration} guarantee in \citet{dagan2024breaking}, and the latter is controlled using a quadratic potential argument together with the sparsity of the \textsc{SPR-Calibration} forecaster.

---


### 192. [Domain-Incremental Remote Sensing Change Detection via Difference-Guided Adaptation and Frequency-Decoupled Distillation](https://arxiv.org/abs/2607.12934)

**<font color=#1a73e8>作者：</font>** Daifeng Peng, Yaning Li, Haiyan Guan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing change detection (RSCD) models are prone to catastrophic forgetting when incrementally adapted to new domains. Existing domain-incremental learning (DIL) methods mainly preserve image-level representations but often overlook bitemporal discrepancy cues, which are critical for robust change detection under domain shifts. To address this limitation, we propose DG-FDD, a domain-incremental change detection framework that integrates Difference-Guided Adaptation and Frequency-Decoupled Distillation. Specifically, the Difference-Guided Dynamic Adapter (DGDA) models bitemporal feature discrepancies to promote change-aware feature adaptation and reduce domain-specific interference. Meanwhile, the Frequency-Decoupled Knowledge Distillation strategy with Cross-domain Synthesis (FDKD-CS) separates structural information from domain style in the frequency domain, enabling stable knowledge transfer without historical data. Extensive experiments on three public high-resolution RSCD datasets under two- and three-domain incremental protocols demonstrate that DG-FDD effectively mitigates catastrophic forgetting. Compared with independently trained single-task models, DG-FDD records mean relative changes in F1 and IoU of only -0.23% and -0.45%, respectively, across six two-domain sequences, and -0.69% and -1.31%, respectively, across the three evaluated three-domain sequences. These results indicate a favorable stability-plasticity balance between historical knowledge retention and new-domain adaptation in continual cross-domain change detection.

---


### 193. [Point Tracking in Surgery--The 2025 Surgical Tattoos in Infrared Challenge (STIRC2025)](https://arxiv.org/abs/2607.12939)

**<font color=#1a73e8>作者：</font>** Adam Schmidt, Mert Asim Karaoglu, Zijian Wu 等 35 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Point tracking in surgery is crucial to enable applications in downstream tasks such as segmentation, 3D reconstruction, virtual tissue landmarking, autonomous probe-based scanning, and subtask autonomy. This paper introduces the 2025 iteration of a point tracking challenge to address this, wherein participants submit their algorithms for quantification. Their algorithms are evaluated using a dataset named surgical tattoos in infrared (STIR), with the challenge named the STIR Challenge 2025 (STIRC2025). The STIR Challenge 2025 comprises two quantitative components: accuracy and efficiency. The accuracy component tests the accuracy of algorithms on in vivo and ex vivo sequences. The efficiency component tests algorithm inference latency. The challenge was conducted as a part of MICCAI EndoVis 2025, and seven teams participated in this challenge. In this paper we summarize the challenge results and participant methods. The challenge dataset is available at: this https URL, and the code for baseline models and metrics calculation is available here: this https URL

---


### 194. [The Illusion of Robustness: Aggregate Accuracy Hides Prediction Flips under Task-Irrelevant Context](https://arxiv.org/abs/2607.12963)

**<font color=#1a73e8>作者：</font>** Yanzhe Zhang, Sanmi Koyejo, Diyi Yang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) grow more capable, they are increasingly deployed in context-rich settings where task inputs are often accompanied by long, partially irrelevant context. In a controlled setting, we find that state-of-the-art models often appear robust to task-irrelevant context at the aggregate level: prepending it to benchmark questions causes little change in overall accuracy. This aggregate stability, however, masks significant per-example instability. Even semantically meaningless pseudo-words, formed by randomly combining characters, can markedly shift model predictions on a small fraction of examples, degrading performance on some while improving it on others. This two-sided effect holds consistently across a wide range of models and datasets, yet the affected examples are largely model-specific. We further show that this instability is modulated by context type, context length, test-time compute, and model development stage. Together, our findings reveal context-induced tail risks concealed by aggregate accuracy, motivating per-example reliability evaluation of language models.

---


### 195. [Sensing the properties of virtual objects without physical feedback](https://arxiv.org/abs/2607.12978)

**<font color=#1a73e8>作者：</font>** Rhoslyn Roebuck Williams, Harry J. Stroud, Luis E. Toledo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> People who have interacted with simulated worlds and simulated objects in extended reality (XR) often have a sense that they can 'feel' the objects being simulated despite them not being physical. Our sense of touch is essential for how we 'feel' the physical world, however, there is an open question as to what it means to 'feel' virtual objects when interacting with them in immersive digital environments. In prior research, we have reported that participants often describe a subjective experience of 'feeling' the properties of simulated molecular objects while using interactive molecular dynamics in extended reality (iMD-XR), a field-based interaction paradigm for manipulating real-time simulations of molecular objects without haptic feedback. To better understand these subjective reports of 'feeling', we used a psychophysics approach to quantify the threshold at which participants perceive differences in the rigidity of simulated molecular objects (C$_{60}$ molecules) in iMD-XR. To evaluate this, we carried out experiments to compare the just-noticeable differences (JNDs) in two conditions: (1) via direct interaction with a real-time C$_{60}$ simulation, and (2) via observation-only$\unicode{x2013}$i.e. watching another person interacting with the simulations. Our findings show that direct interaction enabled participants to perceive more subtle rigidity differences of 11.5%, compared to 18.5% for observation-only. Furthermore, participants who undertook interaction first were better able to distinguish rigidity differences in the subsequent observation-only condition, suggesting that interaction trained participants to better perceive differences in molecular properties. These findings demonstrate a novel and flexible approach for sensing the properties of virtual objects in XR, and offer new insights into iMD-XR's potential in molecular research and education.

---


### 196. [Controllable Generation of Diverse Dermatological Imagery for Fair and Efficient Malignancy Classification](https://arxiv.org/abs/2607.12987)

**<font color=#1a73e8>作者：</font>** Héctor Carrión, Narges Norouzi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate dermatological diagnosis naturally necessitates equitable performance across diverse populations, yet a systematic lack of expertly annotated images, especially for underrepresented skin tones and rare diseases, impedes progress toward measurably fair methods. We introduce cgDDI (Controllable Generation of Diverse Dermatological Imagery), a hybrid framework that (1) synthesizes realistic healthy skin samples without disturbing other input properties, (2) maps single-sample rare lesions onto novel skin-tones and locations non-parametrically, and (3) allows for efficient parametric generation with as few as 10 training samples. The framework supports both human and automated segmentation masking, enabling scalability to datasets without pre-made lesion masks. We grow a 656-image dataset by more than 400x and validate across two datasets: biopsy-confirmed Diverse Dermatology Images (DDI) and expert-verified Fitzpatrick17k (F17k). On the DDI benchmark, we achieve malignancy classification accuracy of 86.4% under synthetic-only training and 90.9% state-of-the-art performance with real data fine-tuning, alongside leading fairness metrics. Cross-dataset experiments show +13.9% accuracy improvements on unseen F17k data despite minimal disease overlap. We openly release 266k+ synthetic images, code, and generative models to further support fairness research at this https URL.

---


### 197. [X-Lens: Real-Time Metric Depth Estimation with Heterogeneous Cameras](https://arxiv.org/abs/2607.12993)

**<font color=#1a73e8>作者：</font>** Heng Zhou, Shuhong Liu, Yonghao He 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present X-lens, a compact feed-forward model for metric depth estimation from a variable number of calibrated fisheye and pinhole views. To support real-time downstream perception, X-lens is built around a geometry-aware heterogeneous camera formulation with two key components. Learnable calibration tokens provide a coarse alignment between fisheye and pinhole projective spaces, while a Jacobian-parameterized distortion bias injected into cross-attention models local projection changes and promotes cross-camera consistency, enabling robust generalization with only 0.04B parameters and up to 41 FPS. The model predicts dense depth together with a global metric scale, avoiding auxiliary reconstruction targets that increase computation and optimization complexity. To learn such cross-camera generalization at scale and depth, X-lens is trained on multiple public datasets and OmniScene, our newly released large-scale synthetic dataset containing approximately 266K synchronized six-view frames, 1.7M individual images, and 103 indoor and outdoor scenes. Extensive experiments on both real-world and synthetic indoor and outdoor datasets demonstrate superior heterogeneous-camera metric depth accuracy, reducing AbsRel by 25.4\% on OmniScene-Full over the strongest baseline while using 88.9\% fewer parameters, with competitive performance on conventional fisheye-only and pinhole-only settings.

---


### 198. [Watermark Forensics for Generative Models: An Information-Theoretic Perspective](https://arxiv.org/abs/2607.13003)

**<font color=#1a73e8>作者：</font>** Xiaoyu Li, Zheng Gao, Xiaoyan Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A watermark in a generative model's output is usually asked only whether a text is machine-made. The same mark can do more: attribute it to the user who produced it, extract a hidden payload, or localize the part that survives editing. These form a forensic ladder, and we ask what each rung costs in the sample length $n$.
One object organizes the answers. Let $S$ be the secret the mark carries (a user's identity or payload), and let the information profile $\nu(t)=I(S;X_t\mid X_{<t})$ record how much the $t$-th token reveals about $S$ given the earlier ones. Its total mass pays for attribution and extraction; how that mass is spread pays for localization; and detection alone is paid for not by information but by presence, the distance from the marked to the unmarked distribution. The literature's two quality models, a mark subtle on every token and one that stamps a few tokens loudly, are two incomparable ways of capping this profile.
Our main theorem settles the ladder's entropy column. For statistically distortion-free schemes, attributing a text to one of $N$ users costs $\Theta(\log N/h)$ tokens over every stationary-ergodic source of entropy rate $h$, sharp to a $(1+o(1))$ factor: to our knowledge the first tight entropy-rate law for multi-user attribution (via exact alignment). The natural collision-counting analysis overcharges without bound; only a decoder thresholding each candidate by its own realized surprisal attains the rate while almost never implicating an innocent user. A matching converse makes the law two-sided, and extraction of an $\ell$-bit payload costs $\Theta(\ell/h)$. Two gaps are real, not modeling artifacts: a $\Theta(\log N)$-token window in which a text is provably machine-made yet unattributable, and a footprint-resolution uncertainty principle. Experiments on GPT-2, Pythia-410M, and Qwen2.5 recover the predicted constants.

---


### 199. [The Spectrum Is Not Enough: When Context Helps Time-Series Forecasting](https://arxiv.org/abs/2607.13006)

**<font color=#1a73e8>作者：</font>** Mert Onur Cakiroglu, Mehmet Dalkilic, Hasan Kurban  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A growing family of indices scores how predictable a series is from its spectrum. Practitioners increasingly read these scores as answering a different question: whether \emph{adding context}, a longer lookback, a retrieval plug-in, or a pretrained model, will help. These are not the same question. The value of context is a property of the operating point, not of the series. Any index built from the power spectrum is invariant under phase randomization, whereas the beyond-second-order value that retrieval and foundation models supply is not, because a phase-randomized series is asymptotically Gaussian. We state this as an impossibility result and isolate it with surrogate pairs that fix the spectrum and the marginal by construction. We then give a label-free, configuration-level diagnostic, the coverage deficit, whose principal term measures beyond-spectrum structure as the gain of analog over linear prediction. On seven benchmarks the prediction holds: window-keyed retrieval's value collapses across surrogate pairs (ECL median $+33\%\!\to\!-35\%$, $p{<}10^{-40}$) while every spectral index stays frozen; a foundation model's value splits into a surviving second-order part and a small beyond-linear margin that collapses; a longer linear window's value survives. Leave-one-dataset-out, the structure term predicts the sign of beyond-spectrum value where the spectral indices trail it, and the reverse holds for the second-order mechanism. We introduce no new forecaster; the contribution is the distinction, a controlled comparison, and a diagnostic for the deployment decision. Code: this https URL.

---


### 200. [Dynamic Resource Allocation for Ensemble Determinization MCTS](https://arxiv.org/abs/2607.13007)

**<font color=#1a73e8>作者：</font>** Jakub Kowalski, Adam Ciężkowski, Artur Krzyżyński 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Simulation-based algorithms are especially suited for high-uncertainty environments such as adversarial board games with significant elements of randomness and hidden information. In particular, several Monte Carlo Tree Search (MCTS) variants are commonly used in such domains. In this paper, we propose a series of enhancements for Ensemble Determinization MCTS, introducing two axes for dynamic resource allocation. First, Dynamic Number of Determinizations, increases or decreases the number of currently used determinization trees depending on the behavior of so-far search. Second, Dynamic Simulation Allocation, splits the simulation budget nonuniformly across the determinization trees, using simulation-to-simulation decisions to choose the tree with potentially the best knowledge gain. As benchmark domains, we used three popular tabletop games: Jaipur, Lost Cities, and Splendor. Testing our proposed enhancements in iteration- and time-based settings showed that particular configurations yield a statistically significant increase in the algorithm's strength.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-203](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
