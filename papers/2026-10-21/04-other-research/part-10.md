# 📦 其他研究 | 2026年10月21日

> 本类共 **534** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**451-500**（第 10/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-534](./part-11.md)

---

### 451. [Temporal Dynamics and Security Assessment of SRT Protocol: A 96-Day Longitudinal Analysis of Production Streaming Infrastructure](https://arxiv.org/abs/2610.26402)

**<font color=#1a73e8>作者：</font>** Ahmed F. K. Koysha, Ferdi Sönmez  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This study presents a 96-day longitudinal analysis of Secure Reliable Transport (SRT) protocol behavior in a production streaming environment between Iraq and Turkey, examining 262,672 transport metric samples and 5,033,104 system resource measurements collected between October 2025 and January 2026. The research addresses temporal patterns, system-resource relationships, attack vulnerability, and anomaly detection. Results reveal significant temporal variation: Negative Acknowledgment exhibits 7.6-fold hourly variation and 11.5-fold daily variation (p < 0.001), though with small effect sizes (eta^2 < 0.04), indicating that temporal period explains less than 4 percent of total variance. Central Processing Unit (CPU) utilization emerges as the strongest system-level correlate of transport variation (r = 0.617 with NAK rate). Controlled User Datagram Protocol (UDP) flood experiments at 500 packets per second cause CPU increases of 176 to 806 percent, while SRT transport metrics change by only plus or minus 13 percent demonstrating protocol resilience through the Automatic Repeat Request mechanism. An unexpected anomaly reaching 97.7 percent CPU enabled signature-based differentiation between attack types. A Z-score anomaly detection method outperforms fixed thresholds, detecting all 7 security events. This study contributes the longest temporal characterization of SRT metrics reported to date, the first system-SRT correlation analysis, and the first controlled security assessment of SRT infrastructure. These findings provide actionable guidance for capacity planning, security hardening, and multi-metric monitoring of production SRT deployments.

---


### 452. [LaMER: Language-Conditioned Multi-Expert Routing for Weakly Supervised Referring Expression Comprehension](https://arxiv.org/abs/2610.26404)

**<font color=#1a73e8>作者：</font>** Yu Yu Chang, Tzu-Hsuan Weng, Youssef Mohamed Amin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Referring Expression Comprehension (REC) localizes the image region described by a natural language expression, underpinning applications such as autonomous navigation, human-robot interaction, and medical image analysis. Under weak supervision, REC is challenged by the visual-linguistic semantic gap and the difficulty of inferring region-text correspondences from coarse image-level signals alone. Moreover, no single visual encoder captures all complementary properties---semantic alignment, fine-grained texture, and boundary awareness---while naively fusing multiple pretrained encoders yields heterogeneous, hard-to-reconcile representations. We propose LaMER, a weakly supervised REC framework that dynamically aggregates four frozen expert encoders through a language-conditioned Cross-Modal Routing Fusion module, adapting expert selection to each referring expression without instance-level bounding-box supervision. A Cell-Text Matching Head with Negative Anchor Augmentation, trained with a multi-objective loss combining contrastive, reconstruction, alignment, and load-balancing terms, further stabilizes optimization. LaMER achieves 77.67\%, 62.81\%, and 69.49\% Acc@IoU\(\geq 0.5\) on RefCOCO, RefCOCO+, and RefCOCOg, surpassing DViN and WeakMCN by up to 16.49 and 14.49 points, with ablations validating each component.

---


### 453. [Expert L2 English Speech Evaluation on a Gaming PC: Accuracy, Fluency, and Prosody with XLS-R, XEUS, and PhoneticXeus](https://arxiv.org/abs/2610.26406)

**<font color=#1a73e8>作者：</font>** Richard Rose  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> oollim is a locally executable system for evaluating L2 English pronunciation accuracy, fluency, and prosody on a consumer computer. The system combines pretrained XLS-R, XEUS, and PhoneticXeus representations with reference-text features and ridge regressions trained on SpeechOcean762, the Korean Learners' L2 Speech Corpus (English), J-AESOP, and their combinations. On 305 independently held-out recordings assessed by three expert raters, several ridge configurations substantially outperform archived Azure API scores obtained in January 2026 in both Spearman correlation and quadratic weighted kappa across all three constructs. These results support expert speech evaluation on consumer hardware using pretrained representations and construct-specific regressions, without neural-model fine-tuning or calibration on the private evaluation data.

---


### 454. [A Simple and General Approach to top-$k$ Selection](https://arxiv.org/abs/2610.26407)

**<font color=#1a73e8>作者：</font>** Motti Goldberger, Nils Rudi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper considers the Bayesian top-$k$ identification problem, wherein a decision maker is tasked with selecting $k$ items from a pool of items of unknown quality. To assess the items, the decision maker adaptively allocates a fixed sampling budget, where each sample of an item yields a noisy observation of its quality, with the objective of minimizing the expected opportunity cost of the selected set. We propose an approach that allocates each batch of samples by minimizing a surrogate objective derived from an upper bound on the expected opportunity cost. The approach is general: samples can be allocated in batches, the selection size $k$ is arbitrary, and it applies to many sampling distributions. It is also simple and intuitive. We prove that the method's posterior expected opportunity cost decays at an exponential rate of at least half the best rate achievable by any sampling rule. In simulations across a wide range of settings, the method is competitive with, and often improves upon, the best existing algorithm in each setting.

---


### 455. [Policy-Adaptive Credit Assignment for Spatial Reasoning with Verifiable Rewards](https://arxiv.org/abs/2610.26410)

**<font color=#1a73e8>作者：</font>** Hailiang Yang, Shengchao Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image-based spatial reasoning requires perception, decomposition, and inference, but the stage that limits accuracy can change during training. Answer-level rewards neither localize failures to individual stages nor provide discriminative group-relative feedback when all rollouts receive the same reward. Process supervision provides intermediate feedback, but fixed weights cannot adapt reward allocation to these changing bottlenecks. To address this gap, we propose CALIPER, an adaptive process-reward framework supported by SpatialTrace, a corpus of stage-decomposed spatial reasoning traces. CALIPER jointly estimates the associations between stage-wise reference coverage and answer correctness through within-group ridge regression, using these associations as utility proxies to gradually update reward weights. The resulting process reward supervises all rollout groups, including uniformly failing ones. Because utility estimates can become unreliable when answer-discriminative groups are scarce, a closed-loop harness monitors estimator reliability and validation performance to guide checkpoint rollback, rollout diversification, and early stopping. Extensive experiments across eight benchmarks and three backbones show that CALIPER achieves the highest mean under both one-shot and harness training, with consistent gains over fixed allocation across RL optimizers. Further analyses confirm the benefits of adaptive reward allocation and harness control, with favorable scaling in model/data size.

---


### 456. [Local data augmentation for imbalanced binary classification](https://arxiv.org/abs/2610.26418)

**<font color=#1a73e8>作者：</font>** Harold Gu{é}neau, Alain Celisse, Pascal Delange  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Facing imbalanced binary classification, we aim at maximizing the recall while limiting the proportion of false detections in the minority class. For doing that, the present work studies the effect of several rebalancing strategies, from the uniform subsampling of the observations from the minority class, to a more involved local data augmentation scheme. To be more specific, we establish that only rebalancing class proportions cannot modify the classification performance, whereas local data augmentation is proved to have an impact on the final results. The local augmentation scheme is introduced by means of a two-step procedure. The first step randomly subsamples anchor points among the training observations. These anchor points are used in the second step, for drawing new augmentation data following an ''augmentation kernel'' to be specified. This enables us to decouple the impact of the anchor points subsampling from the one of drawing augmentation data accounting (or not) for the local geometry of the support. The experiments on synthetic data illustrate the practical performance of several strategies for subsampling anchor points combined with either a Gaussian or a diffusion-based augmentation kernel. Compared to SMOTE-like data augmentation procedures, a better performance is achieved when subsampling in the close neighborhood to the classification boundary combined with a Gaussian augmentation kernel. Furthermore in specific settings where the geometric structure of the support matters, the experimental results show that using a diffusion-based augmentation kernel outperforms the Gaussian one.

---


### 457. [Self-Consistency of Entity Sets and Citations in a Deep Research System under Repeated Prompting](https://arxiv.org/abs/2610.26421)

**<font color=#1a73e8>作者：</font>** Lauri Pykälä, Kimmo K. Kaski  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deep research agents (DRA) are commonly used for open-ended synthesis tasks where closed-world QA benchmarks are poorly suited to characterize relevant aspects of performance. We study the self-consistency of one commercial deep research system under repeated identical prompting, representing each report with the set of named entities it mentions, categorised by a custom schema, and the set of citations it retrieves. Across repeated runs of a single open-ended cybersecurity related prompt, we quantify pairwise overlap to characterize how stable the retrieved and synthesized output structure is under repeated identical prompts. In ten runs, the pairwise entity Jaccard results in a median of 0.12 and the pairwise citation Jaccard is below 0.02, with discovery curves that do not visibly saturate. The magnitude and structure of (dis)agreement between entity sets varies by entity class, which suggests that self-consistency in a DRA is better understood as a function of the underlying entity space than as a stable property of the system.

---


### 458. [Governing the Rule Space. Ruliology, Computational Irreducibility and Anticipatory Governance of Quantum Technologies](https://arxiv.org/abs/2610.26423)

**<font color=#1a73e8>作者：</font>** Antonio Felice Uricchio, Francesco Scagliola  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The regulation of emerging technologies is often conceived as a strategy of catching up, because legislators arrive too late. Yet gathering signals, constructing scenarios and adapting rules to an anticipated future are fundamental tasks for those entrusted with governance, including the governance of rules themselves. The literature on so-called future law has already shown that anticipation means building institutional capabilities rather than predicting outcomes precisely (anticipatory governance). Taking this premise as its starting point, this article proposes to understand regulation as an exploration of the transformations that may occur. The Ruliological Framework for Anticipatory Regulation distinguishes rules, transformations and trajectories, assessing alternatives and possible developments. Within this approach, computational irreducibility is adopted conditionally, not as a demonstrated property of legal systems. The Quantum Europe Strategy provides a case study and further grounds for reflection.

---


### 459. [SNO-PI: Label-Scarce SNOMED CT Entity Linking with Pre-trained Encoders and Curated Terminology Knowledge](https://arxiv.org/abs/2610.26425)

**<font color=#1a73e8>作者：</font>** Piyawoot Songsiritat  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present SNO-PI, the top-performing submission on SNOMED International's SNOMED CT Entity Linking Benchmark as of 18 October 2026. SNO-PI achieves a macro character IoU of 0.5387, outperforming the organisers' reference system (0.4582; based on the 2024 challenge winner's approach) by 18% relative. Linking clinical mentions to SNOMED CT is a zero- and few-shot problem over a very large label space: the 272 annotated MIMIC-IV discharge summaries cover only 6,595 of the roughly 219,000 eligible concepts, and a third of those occur only once. This motivates a design built on transfer from pre-trained models and human-curated knowledge. SNO-PI combines high-recall span proposal, SapBERT candidate retrieval and listwise ensemble reranking with three BERT-family encoders, each further pre-trained with masked language modelling on unlabelled MIMIC-IV notes and then on SNOMED CT synonyms and hierarchy before task fine-tuning. We find that curated knowledge helps most on concepts never seen in training, yet these concepts remain the main source of error.

---


### 460. [HarnessRL: Co-Evolving Policies with a Just-in-Time Training Harness for Open-Ended RL](https://arxiv.org/abs/2610.26426)

**<font color=#1a73e8>作者：</font>** Xiaoqiang Wang, Ting-En Lin, Yuchuan Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rubric-based reinforcement learning (RL) trains policies for open-ended generation with natural-language criteria as rewards, but these rewards can become ineffective as training progresses. We identify two failure modes. Under non-discriminative rewards, scores collapse to uniformly low or high values due to insufficient exploration or a mismatch between task difficulty and policy capability. Under spurious rewards, higher scores do not correspond to better responses. Both reflect a training configuration whose task sampling, exploration, and evaluation stay fixed as the policy evolves. We introduce HarnessRL, a training-time harness that co-evolves with the policy through three interfaces for task sampling, rollout guidance, and rubric criteria. HarnessRL maintains a training-time memory from which a harness evolver retrieves within-task history and cross-task evidence. Using this evidence, the evolver attributes each reward failure to the interface whose update can address it. It then runs a proposer and just-in-time critic loop in which the critic accepts a candidate update only after measuring its effect on the current frozen policy, returning rejected candidates for revision. We also curate Rubric-Mix-10k, a five-domain training and evaluation suite for open-ended RL across medical, science, writing, role-play, and instruction-following tasks. On Rubric-Mix-10k, HarnessRL outperforms the strongest baselines by 2.8 to 3.1 points across both 4B and 9B model scales and nearly halves the training steps to its best checkpoint. Code and data are available at this https URL.

---


### 461. [Physiology-Aware Graph Attention for Early Ventricular Reentry Prediction](https://arxiv.org/abs/2610.26430)

**<font color=#1a73e8>作者：</font>** Ma{ë}lis Morier, Jairo Rodr{í}guez Padilla, Patrick Gallinari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sudden cardiac death mostly originates from post-infarct ventricular tachycardia. This reentry is sustained by propagation around scar tissue, but its risk remains difficult to predict from infarct imaging alone. While in silico induction studies can reveal these mechanisms, exploring many substrates and pacing locations remains computationally expensive. We propose a graph attention classifier for early prediction of sustained ventricular reentry from simulated cardiac electrophysiology. Each simulation is represented as a graph with early nodal voltage samples and edge attributes encoding geometry, stimulation frequency, tissue labels, amplitude, and diastolic interval. These descriptors are computed only from the first two paced activations, before sustained reentry is observed. On a balanced independent test set of 1000 simulations, the classifier achieves 94.6% accuracy, 95.4% sensitivity, 93.8% specificity, 94.6% F1-score, 0.987 ROC-AUC, and 0.985 PR-AUC. Ablation experiments show that diastolic interval is the most critical descriptor. Qualitative attention inspection suggests that different heads focus on border-zone, stimulation location, and early propagation path. These results support graph attention as a fast early-prediction approach for large-scale in silico ventricular reentry studies.

---


### 462. [Exact Compilation and Resource Laws for Hidden Integer Feedback](https://arxiv.org/abs/2610.26442)

**<font color=#1a73e8>作者：</font>** Ganxuan Yang, Siqi Wen, Shuyan Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hidden randomized rounding couples the privacy loss of successive integer releases. We study a rational-feedback mechanism under predictable signed-unit participation and full observation of every physical output. A preparation's lifetime connects three results. First, preserving complete carries until an observed echo synchronizes the worlds gives exact finite-law point compilation, with support-width exponent $3C-2$ at every fixed budget $C\ge2$. Second, releasing commitments earlier gives a monotone hierarchy whose exact endpoint, strict gaps and numerical brackets quantify calibration loss. At one fixed discrete Gaussian, a loss allowance of 0.09 requires all four commitments. Third, legal regeneration yields an unrestricted KL rate with a square-root testing remainder and a complete asymptotic frontier under joint physical-time and participation constraints. At fixed rational parameters, finite-window occupation programs approximate that frontier to error $2^{-b}$ in polynomial bit time in $b$. Verified countable-transcript semantics and independently checked finite certificates support these analyses. A matched static workload illustrates the resulting design tradeoff: a structured finite integer matrix improves error and fresh randomness, while the scalar feedback instance retains fewer noise-state and source-table bits.

---


### 463. [TeleASR-Amharic: A Benchmark for Robust Amharic ASR in Realistic Telecommunication Conditions](https://arxiv.org/abs/2610.26448)

**<font color=#1a73e8>作者：</font>** Dagnachew Mekonnen Marilign, Enrique Molero, Abrham Haile 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The real-world usability of ASR models remains challenging, particularly for low-resource languages, where existing speech resources are often collected in clean studio environments. In this work, we introduce TeleASR-Amharic, a benchmark for evaluating Amharic ASR under various acoustic and telecommunication conditions. We analyze the major degradations observed in real telecommunications recordings and develop a benchmark that covers multiple channel conditions, environmental disturbances, and telecom-domain variations. Our results show that telecommunication degradation can substantially reduce recognition performance, making even high-performing ASR models impractical under severe conditions. For example, the WER of the best-performing model increases from 0.23 to 0.79 under severe telecommunication degradation, corresponding to a relative increase of 243% in recognition errors. We further investigate the effects of different noise and channel distortions and show that scaling training data and applying carefully designed telecommunication-aware augmentation substantially improve robustness. In particular, our best training configuration achieves a 23.6% relative WER reduction under extreme noise conditions. Together with the release of our telecommunications-domain data, these findings provide a reproducible benchmark for measuring progress in Amharic ASR while highlighting open challenges in developing robust speech technologies for real-world deployment.

---


### 464. [When Guidance Becomes a Guard: Early Interception of Unsafe Inputs in Text-to-Image Generation](https://arxiv.org/abs/2610.26452)

**<font color=#1a73e8>作者：</font>** Yanchun Li, Yujin Wu, Gangkai Shen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image diffusion models can produce unsafe content, while output filtering intervenes only after synthesis. We investigate whether native generation signals enable early detection of unsafe and adversarial inputs. We find that classifier-free guidance exposes strong safety signals in conditional responses, accessible through compact statistics and linear readouts. Based on this finding, we propose Conditional Semantic Trajectory Interception (CSTI), which aggregates activation contrasts between conditional and unconditional responses at early checkpoints for calibrated risk detection. CSTI fits concept-specific detectors using canonical concept and safe examples, without attack samples, intermediate image decoding, or generator modification. Across five generators, four adversarial attack collections, and two general NSFW datasets, CSTI achieves the strongest overall performance among six baselines at a matched 5% FPR. Early interception reduces generation latency by over 60% on intercepted paths. These results demonstrate the effectiveness of native conditional responses for early safety interception.

---


### 465. [Remembering Has a Price: Learning Memory Worth under Resource Constraints](https://arxiv.org/abs/2610.26453)

**<font color=#1a73e8>作者：</font>** Guannan Lai, Zi-Yang Bai, Jun-Peng Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Lifelong agents continually accumulate and reuse experience to improve after deployment, yet in practice they often operate under tight generation, interaction, and memory budgets. Under such stringent joint constraints, we find that existing lifelong-memory methods can become ineffective, with several sophisticated approaches offering little advantage over simple retrieval or even no-memory agents. This reveals a more fundamental problem: resource scarcity makes each memory decision more consequential. When only a small amount of past experience can be retained or reused and opportunities for reasoning and recovery are limited, retrieving a relevant but ineffective memory can consume scarce context and hinder downstream execution. The key challenge is therefore not simply to retrieve relevant experience, but to determine which experiences are actually worth retaining and reusing. To address this challenge, we propose TokenWorth, a lightweight online memory framework that learns query-dependent memory worth from sparse execution feedback and applies it consistently to memory retrieval and bounded memory management. Across three LifelongAgentBench environments and both local and API-based deployments, TokenWorth achieves the highest task success rate while using the fewest output tokens among the evaluated methods. These results suggest that effective lifelong adaptation under resource constraints depends not on remembering more, but on learning what is worth remembering. Our code is publicly available at this https URL.

---


### 466. [Differential privacy with adjustable preservation of multivariate relationships](https://arxiv.org/abs/2610.26460)

**<font color=#1a73e8>作者：</font>** Nicolas Ruiz  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper derives an exact attenuation formula for multivariate cross-moments under differential privacy achieved through randomized response. From a proposed alternative formulation of randomization matrices compliant with differential privacy guarantees we show that, under attribute-level randomization and where the randomization of the whole distribution is characterized by Kronecker products, any cross-moment of the anonymized dataset involving distinct attributes is equal to the original cross-moment multiplied by attenuation parameters, themselves determined by the part of the overall privacy budget allocated to each attribute. This characterization enables explicit and transparent controls of multivariate relationships preservations in differential privacy through privacy budget allocation. A simple numerical illustration demonstrates that identical total budgets can yield substantially different covariance-preservation profiles. The results also make the multiplicative loss of higher-order interactions explicit and thus can support mechanism design guided by analytical priorities.

---


### 467. [YUTELA: A Scalable Edge Cloud AIoT System for Multi-Site Video Anomaly Detection with Scene Specific Adaptation](https://arxiv.org/abs/2610.26468)

**<font color=#1a73e8>作者：</font>** Shanle Yao, Babak Rahimi Ardabili, Amir Kimiyaie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Building upon our previous Ancilia framework, this work presents \emph{YUTELA}, an edge--server--cloud AIoT system for long-term, multi-site video anomaly detection. YUTELA replaces workstation-based on-site processing with NVIDIA Jetson Thor edge devices and redesigns the multi-camera pipeline through camera batching and redistribution, shared memory, reduced inter-stage data transfer, task integration, and TensorRT-accelerated inference. It maintains a separate anomaly model per camera, retrained on a centralized GPU server once enough recent pseudo-normal data are collected, with updated weights returned to the edge. With eight cameras, TensorRT increases throughput from 14.17 to 29.94 FPS under normal density, and the optimized edge node exceeds the throughput of the workstation-based Ancilia system in seven of nine workload settings, reaching up to 2.03 times its throughput at extreme density. This gain comes at the cost of higher latency under lighter loads with four or eight streams. YUTELA was then operated continuously for 170 hours at four public sites using 31 existing CCTV cameras. The deployment shows that runtime load is driven by scene activity and input frame rate rather than by camera count, and that retraining frequency varies by about three times across sites. The 101 automatically triggered training events occupied only about 6.6\% of a single GPU, indicating that one global node can support adaptation for tens of sites. Mean end-to-end alert latency ranged from 6.8 to 15.4~s depending on site traffic and anomaly type. These results show that YUTELA enables practical multi-camera edge processing with low-cost, camera-specific adaptation across heterogeneous sites.

---


### 468. [On Learning Expand-and-Sparsify Representations](https://arxiv.org/abs/2610.26470)

**<font color=#1a73e8>作者：</font>** Alireza Asghari, Parikshit Ram, Kaushik Sinha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Expand-and-sparsify ($\texttt{EaS}$) representations lift an input to a much higher dimension through a linear map and keep only the $k$ largest coordinates. Existing theory builds that map at random and needs the expanded dimension to grow exponentially in the input dimension, which puts the construction out of practical reach. We ask what is gained by learning the map by gradient descent instead, and how that gain depends on how wide the expansion is. We sweep $73$ OpenML classification tasks and $48$ regression tasks under a protocol that holds the datasets, expanded dimensions, sparsity levels and splits fixed across every method, and we summarise each comparison by a median over datasets and a Wilcoxon signed rank test. We report four findings. First, learning the expansion helps most when the expansion is narrowest, and its advantage over a random map decays to nothing by the widest expansions we run, so a learned $\texttt{EaS}$ layer can be made small. Second, with the map learned, a top-$k$ representation that keeps at most a tenth of its coordinates is indistinguishable from a dense $\texttt{ReLU}$ layer of the same expanded dimension at every expansion factor we test, while GELU and SiLU are not. Third, when the representation is forced to be binary the sparse code is the better of the two, and the reason is that binarization costs it nothing while it costs the dense layer accuracy. Fourth, how sparse the representation can be is governed by how wide it is: the sparsity level that is free rises as the expansion grows, so there is no fixed limit on how sparse it can be. The regression tasks reproduce the first finding and qualify the second and third.

---


### 469. [A Simple and Unified Method for Gradient-Variation Regret](https://arxiv.org/abs/2610.26473)

**<font color=#1a73e8>作者：</font>** Hang Yu, Peng Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gradient-variation online learning has attracted increasing attention for its connections to game theory and optimization. It has been studied in both non-stationary online learning, which aims to minimize dynamic regret against time-varying comparator sequences, and universal online learning, which seeks to adapt to unknown loss curvature. Prior work obtained gradient-variation bounds using different techniques tailored to each setting. We propose a simple and unified method based on surrogate losses with a quadratic penalty on decision movement, yielding gradient-variation bounds in both settings. For non-stationary online learning, the method induces an optimistic-to-gradient-variation reduction, enabling a broad class of algorithms to match the rate established by Zhao et al. (2024). For universal online learning, it yields a simple algorithm that matches the optimal universal regret bounds of Yan et al. (2024) while relaxing the extended smoothness assumption. Finally, we apply our method to online games and improve on existing guarantees.

---


### 470. [3D Diffusion Models for Medical Imaging](https://arxiv.org/abs/2610.26475)

**<font color=#1a73e8>作者：</font>** Frank-Peter Schilling, Daniel Barco, Philipp Denzel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative deep learning methods such as Variational Autoencoders, Generative Adversarial Networks or Diffusion Models have achieved remarkable results in image synthesis. In particular, Diffusion Models have demonstrated superior image fidelity and sample diversity compared to other approaches on standard benchmarks, while also offering more flexible training dynamics as evidenced both in natural image domains and in medical applications. In medical imaging including Computed Tomography, Magnetic Resonance Imaging or Positron Emission Tomography, such models have various important use-cases including data augmentation, domain transfer, image reconstruction, inpainting, image augmentation and artifact correction. Further, generated images can be conditioned on patient characteristics, medical reports, segmentation masks or other images. Specific challenges arise due to the 3D volumetric nature of medical images, which translate to substantial demands in terms of memory, compute, and training data. This article provides a comparative overview of 3D Diffusion Models which have been developed for medical images, with a focus on current performance, limitations, and an outlook for future work.

---


### 471. [Wet-Biased Data Pipelines Mislead the Training and Evaluation of Generative Precipitation Nowcasting](https://arxiv.org/abs/2610.26486)

**<font color=#1a73e8>作者：</font>** Christoph Metzl, Stefan Kapsreiter, Kianusch Vahid Yousefnia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models for precipitation nowcasting are trained and evaluated predominantly on wet-biased datasets, which over-represent precipitation events to emphasize rare extremes. Selecting test cases based on target observations is known to favor forecasts that match the selected distribution rather than the intended deployment distribution. We show analytically how this target-dependent sampling also shifts the conditional distribution learned by generative models. When training and test sampling match, even an ideal model learns precisely the distribution favored by evaluation, allowing the evaluation bias to conceal the training bias. Using a fixed satellite-to-radar diffusion model, we demonstrate that target-dependent test sampling can reverse the calibration assessment. The model appears under-predictive on a wet-biased test set but over-predictive on a deployment-representative test set. This result is replicated outside the model's training domain after a seven-year gap. Utilizing classifier-free guidance as an example, we demonstrate how the contradictory calibration assessment can misdirect downstream model development.

---


### 472. [Mal-AAEGAN: Adversarial Autoencoder with Double-Critic WGAN-GP for Malware Generation](https://arxiv.org/abs/2610.26488)

**<font color=#1a73e8>作者：</font>** Nam Hoang Thanh, Trung Pham Duy, Lam Bui Thu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine-learning (ML) malware detectors are known to be vulnerable to adversarial samples. Generative adversarial networks (GANs) such as MalGAN, Mal-LSGAN, and our previous Mal-D2GAN can craft adversarial malware to probe and harden these detectors, yet they operate directly on a high-dimensional, discrete binary feature space, which leads to unstable training, vanishing gradients, and adversarial samples of limited diversity. To address these problems we propose Mal-AAEGAN. First, an adversarial autoencoder (AAE) learns a low-dimensional, regularized and continuous latent representation of the $M$-dimensional binary API feature vector, and the generator performs an additive perturbation in this latent space rather than in the raw binary space. Second, training follows the Wasserstein GAN with gradient penalty (WGAN-GP) scheme using two critics: a mimic-black-box critic that inherits the role of the substitute detector and a naive critic that inherits the role of the additional detector. A decode-binarize-OR pipeline guarantees that the original API calls of the malware are preserved. The model is evaluated on two malware datasets of different input dimensionality ($M\in\{139,215\}$) against eight common ML detectors and compared, under an identical protocol, with MalGAN, Mal-LSGAN and Mal-D2GAN. Mal-AAEGAN trains stably in the continuous latent space and attains an evasion rate on par with or higher than these binary-space baselines across both datasets, while its generator stays responsive to the noise input rather than reducing to a single fixed perturbation per malware.

---


### 473. [PDNet: Exploring Pruning and Distillation for Real-Time Worker Activity Recognition in Industrial Assembly](https://arxiv.org/abs/2610.26491)

**<font color=#1a73e8>作者：</font>** Malek Baba, Thinesh Thiyakesan Ponbagavathi, Alina Roitberg  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we address real-time fine-grained human activity recognition (HAR) in industrial assembly and introduce PDNet, a new framework that jointly exploits structured pruning and knowledge distillation for 3D convolutional networks. We start by training a 3D-CNN backbone in a supervised manner. Then, PDNet applies channel-wise structured pruning to obtain a more compact network. In the third step, our method is optimized using knowledge distillation from the large unpruned teacher to recover accuracy lost due to pruning. On the challenging MECCANO dataset with an X3D-M backbone, the pruned model without distillation reaches a Top-1 accuracy of 25.54 %, while PDNet raises this to 39.46 %, with only 6.90 MB model size and 3.78 GFLOPs. These results show that distillation within PDNet is highly effective in restoring pruned model performance and highlight its high potential for resource-constrained HAR in industrial assembly.

---


### 474. [Connection Escrow: Holding AI-Agent Pod Egress in the Kernel Until an Isolated Verifier Rules](https://arxiv.org/abs/2610.26501)

**<font color=#1a73e8>作者：</font>** Ashok Subbabhatta Gopalakrishna  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents in containers act by opening network connections, and the text that drives them can be hostile. Controls placed between the agent and its tools are bypassed by a child process or a direct socket, and their approval is not tied to the connection the kernel later opens. We present connection escrow: every outbound TCP connection from a supervised pod is parked inside the kernel's connect() path, before any packet exists, by a 98-instruction eBPF program on the pod's cgroup. A node interceptor attributes the held socket to its kernel socket cookie, process, executable digest, cgroup and pod identity, parks the first bytes the agent writes, and asks a verifier in a separate container with its own key. The connection is released only on a signed verdict naming that one socket cookie and destination, unexpired and unused; no verdict by the deadline resets it, and a late approval is refused. The agent is unmodified. A 36-check adversarial suite with real cgroups passes on the eBPF hold point (33 of the checks also apply, and pass, on an iptables hold point): refused connections never reach the destination; forged, rebound, replayed, expired and late verdicts are refused; the agent's attempt to reach the verifier is itself escrowed; child-process and renamed-binary bypasses fail; UDP is pinned to the resolver. On a Kubernetes cluster, unmodified pods are held per connection and attributed to their SPIFFE identity, a raw socket that bypasses a sidecar proxy is held, and 600 connections from six pods are gated. The hold adds 4.5 ms median per released connection, of which 24 us is policy. Finally, we gate on request content without terminating TLS: an eBPF uprobe reads the plaintext at the agent's TLS-library boundary (shared OpenSSL, static OpenSSL, Go crypto/tls), a model scores it, and the connection is held on that verdict while TLS stays end-to-end and the enforcer holds no key.

---


### 475. [Interpretable Face Contrast Modeling for Smartphone Portrait Rendering](https://arxiv.org/abs/2610.26517)

**<font color=#1a73e8>作者：</font>** Yujin Cho, Benoît Pochon, Jean-Michel Morel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The quality of smartphone portrait photography has become increasingly important to both manufacturers and users. Recent devices use complex computational pipelines to improve facial rendering under varied lighting. These pipelines vary widely across manufacturers, so the same portrait can look noticeably different across smartphones. These differences affect multiple aspects of facial appearance, making perceptual preference difficult to characterize with a single measure. To address this, we propose an interpretable framework that decomposes face contrast into three components: overall facial tonal separation, eye-region contrast, and micro-contrast of fine skin details. We formulate dedicated metrics for each component and validate them via pairwise human judgments, demonstrating that our approach correlates more closely with human contrast perception than traditional contrast measures. To support this analysis, we introduce a realistic mannequin-based dataset designed for systematic facial contrast evaluation, comprising 508 full-resolution captures from 29 smartphones under diverse lighting, with region-specific masks and extensive pairwise perceptual annotations. As a downstream analysis, we show that combining the three component-wise metrics provides a meaningful basis for modeling balanced facial contrast preference in a controlled setting, and we present a preliminary evaluation on a smaller real-portrait dataset indicating that insights derived from the mannequin study can extend to real images. Our work provides a controlled first step toward defining and evaluating face contrast in portrait imaging.

---


### 476. [A Semantic Knowledge Graph Construction Pipeline for Vehicle Intention Prediction in nuScenes](https://arxiv.org/abs/2610.26528)

**<font color=#1a73e8>作者：</font>** Khaled Nowara, Mohamed Manzour, Catherine Elias  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge graphs (KGs) are increasingly used in autonomous driving (AD) to make traffic scene entities and relations explicit for prediction and reasoning. Existing traffic-scene KGs, however, primarily emphasize trajectory forecasting or general scene understanding. This paper presents the nuScenes Intention Knowledge Graph (NIKG), a focused Web Ontology Language (OWL)-based semantic representation and construction pipeline for ego-centric vehicle intention context. NIKG instantiates nuScenes scenes as a self-describing Turtle graph and promotes three intention-relevant relations to first-class properties of each scene participant: ego-relative motion, spatial configuration, and time to collision (TTC) risk. The pipeline uses a small input contract available in many ego-centric driving datasets: ego pose, tracked object annotations, and temporal keyframe order. NIKG is released as an ontology-backed, self-describing graph artifact together with a reproducible construction pipeline and validation protocol for ego-centric intention context. Applying this pipeline to nuScenes mini yields a graph of 211,335 triples across 404 keyframes; under the validation protocol, ego-relative motion labels achieve 92.5% forward consistency. Coverage, semantic consistency, and temporal coherence analyses over this artifact are further reported. NIKG occupies the space between scene-oriented traffic KGs and intention-prediction models: a small, explicit semantic layer intended to support downstream work such as knowledge graph embedding (KGE), SPARQL-based feature extraction, or hybrid neuro-symbolic reasoning.

---


### 477. [Agentic Orchestration of EDC Data Space Retrieval and Natural Language Driven Data Processing](https://arxiv.org/abs/2610.26548)

**<font color=#1a73e8>作者：</font>** Marla Grunewald, Fin Gentzen, Iulisloi Zacarias 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Participating in a data space still requires the Dataspace Protocol (DSP) negotiation flow to be hand-coded against each provider's access policy. We present a multi-agent architecture that automates this process using natural language requests. Built on LangGraph over an Eclipse Dataspace Components (EDC), the design separates concerns into cooperating agents. The orchestrator's role is to route and plan. The data extraction agent's role is to expose the DSP protocol's three composable tools (catalog discovery, contract negotiation and download). The agent also gates negotiations on the consumers' verifiable credentials, refusing assets rather than fabricating them. Furthermore, there are downstream Machine Learning (ML) and Visualization agents, as well as a final Verification agent, which confirms that the request was actually fulfilled and rechecks the intended operation against the contract's usage policy. In a primary benchmark involving 600 runs, the system achieved 89% task success with zero policy violations when evaluating multi-dimensional policy reasoning with a locally hosted open-weight model. It failed safely through refusal rather than misrouting. The reliability of the system is largely dependent on the phrasing of requests: technical and expert requests succeed up to 98% of the time, whereas casual and under-specified requests succeed 72% of the time. Furthermore, in a secondary evaluation of 600 runs isolating hierarchical geographic access control, the framework successfully blocks 100% of unauthorized regional requests. While the verification agent hallucinates that 1% of these requests, the system logs confirm that no data is ever extracted and the framework simultaneously achieves an end-to-end verified delivery rate of 86% for eligible consumers.

---


### 478. [Holi-World: Building Holistic World Intelligence from Human-Ego Experience](https://arxiv.org/abs/2610.26549)

**<font color=#1a73e8>作者：</font>** Hao Li, Xiyuan Zheng, Yuanyuan Gao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human egocentric experience offers a rich foundation for learning how the world is organized and how it changes through interaction. Realizing this potential at scale requires turning growing volumes of recordings into learning resources that connect scene structure, object semantics, and interaction histories across viewpoints and time, while reducing dependence on costly manual annotation. We introduce HOLI-WORLD, an integrated ecosystem connecting experience capture, world representation, automated data construction, model learning, and independent evaluation. To sup- port learning at scale, HOLIWORLD-Foundry combines complementary static and dynamic perception to automatically construct world records that connect persistent scene structure and evolving object states with interaction histories and supporting observations. HOLIWORLD-Data organizes these records from approximately 100 self-collected scenes into grounded learning resources, including approximately 80K QA pairs used to train HOLIWORLD-VL-4B. Independent human annotations of heldout recordings form HOLIWORLD-Bench, supporting evaluation of both annotation quality and learned spatial and temporal understanding. Experiments on ScanNet, ScanNet++, Aria Digital Twin, and HOLIWORLD-Bench demonstrate strong performance in static perception and dynamic tracking, while training on HOLIWORLD-Data substantially improves HOLIWORLD-VL-4B's spatial and temporal reasoning on HOLI- WORLD-Bench and EgoDynamic4D. HOLIWORLD provides a practical foundation for expanding learning resources from the continuous flow of human experience and advancing machine understanding of the dynamic world.

---


### 479. [MRI Reconstruction Risk Estimation from Inference Dynamics](https://arxiv.org/abs/2610.26558)

**<font color=#1a73e8>作者：</font>** Tamir Shor, Alex Bronstein  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Iterative MRI reconstructors produce intermediate estimates before returning a final image. We study these inference trajectories as a model-internal representation of realized reconstruction risk, measured by log-NMSE. Model-native states are projected to magnitude images, summarized by a fixed 16-dimensional descriptor, and mapped to risk using a source-trained ridge readout. Across three reconstruction backbones, trajectory features are strongly predictive of reconstruction risk on held-out source data. Under zero-shot target shift, their behavior is backbone-dependent, exhibiting both preserved positive association and readout reversal. Conditional analyses show that trajectory information can remain associated with error beyond an initialization-only predictor. A prefix analysis further shows that useful trajectory information can emerge before reconstruction completes. Repeated-mask and low-shot calibration studies indicate that trajectories primarily encode persistent case difficulty, while their orientation and calibration can change under domain shift.

---


### 480. [PrismWAM: Decoupling State Representations in World Action Models](https://arxiv.org/abs/2610.26564)

**<font color=#1a73e8>作者：</font>** Tianyu Xin, Wanqi Zhong, Bowen Hu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World Action Models (WAMs) typically represent the world through latent embeddings from pretrained video models, which entangle heterogeneous aspects of the world, from how it looks (e.g., texture and color) to how it is physically configured (e.g., occupancy and pose). This raises an underexplored question: $\textbf{what should constitute the state of a WAM?}$ We argue that the world state should separate how the world appears from how the world evolves under action: the former captures semantic context, while the latter is governed by physical state. To this end, we propose $\textbf{PrismWAM}$, which decouples physics from semantics while jointly modeling state and action. PrismWAM factorizes an embodied task into a $\mathrm{Semantic\ Planning}\rightarrow\mathrm{Physical\ Rollout}\rightarrow\mathrm{Executable\ Action}$ pipeline: given only the initial RGB observation, semantic planning learns to predict the final goal image, while physical rollout predicts the fine-grained evolution toward this goal in depth space; executable actions are then generated from the depth rollout. Without any embodied action pretraining or additional data augmentation, PrismWAM achieves strong manipulation performance in both simulation and the real world. Notably, PrismWAM even surpasses a broad range of models with large-scale embodied action pretraining (e.g., OpenWAM-$\alpha$). More broadly, we reframe World Action Models from modeling how the world looks to how it responds to action, paving the way for action-centric world models grounded in occupancy, flow, tactile sensing, proprioception, and beyond.

---


### 481. [Reward Objectives for Robust (PO)MDPs: A Law-Preserving Equivalence with (Partially Observable) Games](https://arxiv.org/abs/2610.26568)

**<font color=#1a73e8>作者：</font>** Durgam Latha, Dion Reji, Dorde Zikelic 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Robust partially observable Markov decision processes model agents that act under partial observability while adversarial environment resolves uncertainty in the transition probabilities. Reward objectives such as discounted-sum, long-run average and cumulative reward under finite and infinite horizons allow quantifying the utility of an agent. We consider the problem of solving RPOMDPs under all four reward objectives, where the goal is to decide whether the value of a risk measure with respect to a reward objective exceeds a given threshold. We consider different risk measures, such as (1)~expected value, (2)~mean-variance (MV), (3)~conditional value-at-risk (CVaR), and (4)~entropic risk (ERisk). Our results can be summarized as follows. First, we formalize the class of law-invariant risk measures, that subsume all four risk measures above. Second, we propose a unified framework for solving RPOMDPs with discounted-sum, long-run average and cumulative reward objectives under any law-invariant risk measure, by reducing the problem to solving partially observable stochastic games (POSGs). Our unified framework applies to (s,a)-rectangular RPOMDPs with polytopic uncertainty sets, which we show to be {\em equivalent} to POSGs, for each of the four reward objectives and any law-invariant risk measure. We prove equivalence by designing logspace reductions between the RPOMDP and POSG models, that map strategies to strategies and preserve the distribution of the reward objective, up to a constant rescaling factor. Third, as a corollary, we derive new computational complexity results for R(PO)MDPs and POSGs. In particular, we show that solving (s,a)-rectangular RMDPs is as hard as solving simple stochastic games.

---


### 482. [DenseHap: Dense Hand Haptic Estimation from Monocular Images](https://arxiv.org/abs/2610.26583)

**<font color=#1a73e8>作者：</font>** Junhan Xue, Rolandos Alexandros Potamias  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As dexterous robotic manipulation advances, scalable annotations of human hand-object interactions are becoming increasingly important. Furthermore, previous hand contact estimation methods suffered from issues such as dorsal-side misclassifications and insufficient precision, while lacking a unified framework for integrating multiple hand to environment interaction modalities, including distance fields, contact thresholds, and pressure. To address that, we present DenseHap, a unified end-to-end approach to estimate hand distance field recognition, comprehensive hand contact detection, hand pressure analysis, and hand reconstruction from a single monocular image. By incorporating three distinctly defined heads, along with a pretrained 3D reconstructed skeleton and an enhanced dataset, DenseHap outperforms previous state of the art models on four evaluation datasets, improving the F1 score by 8.5 percentage points (a 16% relative improvement) on untrained datasets and by 3 percentage points (5% relative improvement) on in-distribution datasets. Furthermore, DenseHap has effectively improved short-range hand estimate and pressure evaluation. Code and models will be publicly available upon the paper's acceptance.

---


### 483. [Drive2Gauss: FeedForward 4D Gaussian Reconstruction from Multimodal Generative Driving Videos](https://arxiv.org/abs/2610.26585)

**<font color=#1a73e8>作者：</font>** Tong Zhao, Zhiyuan Han, Lin Chen 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating reusable driving environments requires both controllable future observations and an explicit representation that supports rendering from different viewpoints, yet existing methods still recover explicit scenes from generated RGB videos through optimization for each sequence. To overcome these limitations, we present Drive2Gauss, a feedforward framework that converts jointly generated RGB, metric depth, and dynamic flow into dynamic 4D Gaussian scenes. A Multimodal Video Generator predicts the three modalities from reference multiview images and future control signals. Furthermore, we introduce a Gaussian Query Decoder that uses depth to initialize sparse 3D queries and flow to associate the queries across time, and integrates appearance information through spatiotemporal feature aggregation and iterative query refinement. The reconstruction stage operates in a single feedforward pass without optimization for each scene. Extensive results on nuScenes demonstrate that our approach attains an FID of 6.38 and an FVD of 12.43 for future RGB generation, a PSNR of 29.91 dB when reconstructing its generated observations, and supports both direct rendering under lateral camera shifts and downstream video fixing. Code and more visualizations are available at https://zttt04. this http URL.

---


### 484. [TapID: Rapid touch interaction in virtual reality using wearable sensing](https://arxiv.org/abs/2610.26598)

**<font color=#1a73e8>作者：</font>** Manuel Meier, Paul Streli, Andreas Fender 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Current Virtual Reality systems typically use cameras to capture user input from controllers or free-hand mid-air interaction. In this paper, we argue that this is a key impediment to productivity scenarios in VR, which require continued interaction over prolonged periods of time---a requirement that controller or free-hand input in mid-air does not satisfy. To address this challenge, we bring rapid touch interaction on surfaces to Virtual Reality---the input modality that users have grown used to on phones and tablets for continued use. We present TapID, a wrist-based inertial sensing system that complements headset-tracked hand poses to trigger input in VR. TapID embeds a pair of inertial sensors in a flexible strap, one at either side of the wrist; from the combination of registered signals, TapID reliably detects surface touch events and, more importantly, identifies the finger used for touch. We evaluated TapID in a series of userstudies on event-detection accuracy (F1 = 0.997) and hand-agnostic finger-identification accuracy (within-user: F1 = 0.93; across users: F1 = 0.91 after 10 refinement taps and F1 = 0.87 without refinement) in a seated table scenario. We conclude with a series of applications that complement hand tracking with touch input and that are uniquely enabled by TapID, including UI control, rapid keyboard typing and piano playing, as well as surface gestures.

---


### 485. [ITU-DESC: a missingness-aware machine-learning dementia risk score in the UK Biobank cohort](https://arxiv.org/abs/2610.26604)

**<font color=#1a73e8>作者：</font>** Abdullah Kavaklı, Faik Boray Tek  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Background: Existing dementia risk scores rely on fixed, pre-selected features and linear models, or ignore bias from informative missingness in cohort data. Here we introduce the Istanbul Technical University Dementia Risk Score (ITU-DESC), an explainable machine-learning score for incident all-cause dementia that combines broad feature selection across roughly 8,000 candidate features with explicit control of missingness bias.
Results: We studied approximately 500,000 UK Biobank participants with a median follow-up of 16.6 years. We withheld missingness patterns from the model using unconditional random hot-deck imputation. We stabilized feature selection by repeating BorutaSHAP-based feature selection with ten random-imputation seeds and selecting predictors chosen in at least eight of the ten seeds, which yielded 38 predictors. We trained a CatBoost gradient-boosted decision-tree model and evaluated it on a holdout test set of 50,041 participants. For all-cause incident dementia, ITU-DESC achieved an average precision of 0.138 (95% confidence interval 0.123-0.156) and an area under the receiver operating characteristic curve (ROC AUC) of 0.853 (0.844-0.863), significantly outperforming other risk scores, including the strongest comparator, the UK Biobank Dementia Risk Prediction model (0.118 and 0.841). We identified dementia risk predictors absent from established scores, including leukocyte telomere length and liver enzymes. Conclusions: ITU-DESC is the first dementia risk score to combine broad feature selection with explicit control of missingness bias.

---


### 486. [Degree Bounds for Separating Polynomial and Neural Invariants for Point Clouds](https://arxiv.org/abs/2610.26612)

**<font color=#1a73e8>作者：</font>** Snir Hordan, Harm Derksen, Mircea Petrache 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural networks that respect the symmetries of point clouds commonly compute high-order representations of the rotation group to improve their expressivity. Such models are known to be universal, and thus able to separate any pair of point clouds, when using representations of sufficiently high order, yet no precise bound on this order, as a function of the number of points, was previously known. We establish the first quadratic lower and upper degree bounds for polynomials that separate point clouds of n points up to rotations and permutations. By showing Tensor Field Networks and MACE can express all invariant polynomials of a given degree with sufficient representation order, we additionally derive the first explicit, quadratic bound on the representation order sufficient for these architectures to be complete, replacing previous existence results with concrete guarantees. We further show that, under local regularity assumptions, point cloud separation can be achieved with a message-passing-based model using invariants whose degree depends only on the size of a local neighborhood, rather than on the size of the full point cloud. Finally, we provide counterexamples showing MACE must compute high order irreducible representations to separate locally regular point clouds.

---


### 487. [Conducting Reliable Keyword Estimation with Unreliable ASR in Police Audio Data](https://arxiv.org/abs/2610.26614)

**<font color=#1a73e8>作者：</font>** Robert Cole Molloy, Rhiannon N. Miller, Stephen Morgan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Extracting insights from large audio data sets using human transcription is expensive and time-consuming. Off-the-shelf Automatic Speech Recognition (ASR) systems offer an easy-to-use scalable alternative, but systematic transcription errors, especially in domain-specific settings, can bias downstream analyses and lead to unreliable conclusions. We investigate whether imperfect ASR transcripts can still be used to obtain statistically valid keyword frequency estimates by combining model outputs with a small set of human-labeled examples, following Prediction Powered Inference and Design-based Supervised Learning frameworks. We evaluate this approach on police radio communications from Baltimore and Chicago, a domain in which keyword distributions could provide valuable insights into police activity, but off-the-shelf ASR systems exhibit systematic errors on operationally important terminology. Using bootstrap-based confidence interval coverage as our evaluation metric, we find that our approach substantially increases the number of domain-specific keywords that can be analyzed with statistically valid confidence intervals, from 43.0% using ASR alone and 27.2% using only a small set of human-labeled transcriptions to 56.2% in the Baltimore dataset, with similar improvements observed in Chicago data. Our results demonstrate that post-hoc error correction can improve statistical validity of downstream analyses even for poor-quality transcriptions, offering an avenue for better leveraging off-the-shelf ASR models for large-scale speech analysis.

---


### 488. [Global Time-Aware Conditioning (GTC): A Mechanism for Time-Aware Pediatric Sleep Representation Learning](https://arxiv.org/abs/2610.26618)

**<font color=#1a73e8>作者：</font>** Saurav Raj Pandey, Harlin Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sleep physiology evolves throughout the night, with changes in sleep cycles, respiratory stability, and cardiovascular dynamics. However, self-supervised learning (SSL) methods for sleep typically process short, fixed-duration windows without explicitly modeling where each window occurs within the full sleep session. We introduce Global Time-Aware Conditioning (GTC), a mechanism that complements local positional encodings by conditioning latent representations on the global time-of-sleep of each input window. We integrate GTC into three representative SSL frameworks and evaluate them on five clinically relevant tasks with extreme class imbalance across two independent pediatric cohorts. GTC generally improves F1 and AUPRC across architectures and tasks, with gains persisting under cross-cohort transfer, highlighting the value of global temporal context for sleep representation learning.

---


### 489. [EgoXperience: Learning World-Grounded Egocentric Representations from Human Experience](https://arxiv.org/abs/2610.26625)

**<font color=#1a73e8>作者：</font>** Xinhao Ji, Hui En Pang, Hao Li 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing human activity from egocentric video requires more than recovering individual 3D components: the observer's motion, surrounding geometry, and hand-object interactions must fit together in a consistent world. Achieving this coherence requires both joint reconstruction and aligned supervision, yet existing methods and datasets offer limited support for either. We present EgoXperience, a full-stack paradigm that addresses these needs through data collection, automatic annotation, unified modeling, and benchmarking. Central to EgoXperience is an automatic annotation engine, EgoX-Engine, that couples geometrically verified object tracking with SLAM-based world alignment, yielding consistent supervision for the camera, scene, hands, and objects. This yields EgoX-Data-6M, a 50-hour dataset of task-driven manipulation and locomotion within and across indoor and outdoor environments, with second-level task captions. We carefully select one hour across these activity categories as EgoX-Bench to evaluate joint reconstruction. To translate this supervision into reconstruction, we introduce EgoX, trained with EgoX-Data-6M and complementary annotations from additional public datasets. Given monocular egocentric video and first-frame object masks, our model achieves joint metric reconstruction of the camera, scene, hands, and objects in a shared world coordinate frame with a single forward pass. Extensive experiments demonstrate state-of-the-art performance across scene estimation and world-space hand-object pose recovery. Against the strongest evaluated baselines, EgoX reduces camera, hand, and depth errors by 68.9%, 65.6%, and 42.9%, and improves object pose scores by 28.0%.

---


### 490. [SleepPairNet: Learning Multimodal Pediatric Sleep Representations with Random-Pair Cross-Attention](https://arxiv.org/abs/2610.26628)

**<font color=#1a73e8>作者：</font>** Saurav Raj Pandey, Harlin Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Analyzing physiological sleep signals is important for assessing sleep quality and detecting sleep-related disorders. Learning inter-modal relationships across physiological signals can provide richer representations for downstream sleep analysis. We introduce SleepPairNet, a multimodal self-supervised learning (SSL) framework that learns pairwise interactions between physiological signals through cross-attention. We propose a random modality-pair selection strategy that exposes the model to diverse signal pairs during pretraining, enabling flexibility across modality combinations at test time. Pretrained on the NCH dataset, SleepPairNet outperforms the evaluated SSL baselines on all respiratory tasks while remaining competitive on EEG-related tasks, and shows even stronger results when transferred to the external CHAT dataset.

---


### 491. [VaDar: Implicit Goal Conditioning via Value Disaggregation](https://arxiv.org/abs/2610.26629)

**<font color=#1a73e8>作者：</font>** Shashwat Saxena, Mehul Goel, Sreyas Venkataraman 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon tasks are important for modern AI and robotics, yet pose a challenge for reinforcement learning. Historically, a popular approach has been to decompose a task into subgoals, and learn a subgoal-conditioned policy to execute each subtask in sequence.
We introduce an alternative called Value Disaggregation (VaDar), which trains a single subgoal-independent policy to maximize a linear combination of per-subgoal critic values. Because subgoal information is needed only at training-time, VaDar removes the need for possibly costly or cumbersome subgoal-selection during policy deployment. Moreover, through careful experiments, we show that VaDar (1) is always competitive with, and frequently outperforms, natural baselines like goal-conditioning and (2) succeeds on tasks with non-sequential goal structure and multiple optimization objectives. In particular, VaDar is the first algorithm to solve challenging, long-horizon tasks in the RoboCasa suite, even when starting from a policy pretrained from behavior cloning with near-zero initial task success. Taken together, VaDar's successes suggest that subgoal information benefits actor-critic reinforcement learning by enhancing the efficacy of critic learning, whereas policy goal-conditioning is often unnecessary.

---


### 492. [DM-RSA-OAEP: Formal Treatment of a Dual-Modulus Fault-Detection Countermeasure Based on Physical Diversity](https://arxiv.org/abs/2610.26642)

**<font color=#1a73e8>作者：</font>** Ramamonjy Andriamifidisoa, Rufine Marius Lalasoa  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We revisit DM-RSA, an RSA variant that uses two independent moduli, whose original version was broken by Håstad's attack and contained an incorrect compromise-tolerance claim. We give a formal treatment of its repaired variant, DM-RSA-OAEP: (i) a complete IND-CCA2 security proof in the random-oracle model via a two-step hybrid argument, upper-bounding the security of the scheme by that of the weaker underlying RSA-OAEP instance, with an explicit simulation loss; (ii) a fault-detection theorem in an explicit adversary model that covers computation, key, and verification faults, including safe-error attacks, under a clearly stated physical-diversity assumption; (iii) an explicit analysis of why the countermeasure degrades to uselessness when the diversity assumption is violated (common-mode faults on a single chip). We position the scheme against the countermeasure landscape and against the broken dual-modulus literature. The contribution is deliberately framed as a fault countermeasure with a provable detection guarantee, not as a computationally stronger RSA. We conclude with a concrete instantiation and a detailed measurement protocol.

---


### 493. [Dual-Scale Condition-Shift Editing for Robust Real-World Image Demoiréing](https://arxiv.org/abs/2610.26644)

**<font color=#1a73e8>作者：</font>** Shiyang Zhou, Haijin Zeng, Congpei Qiu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robust demoiréing of screen-recaptured images remains challenging: moiré varies in frequency, color, and spatial support across display-camera pairs and capture conditions. Dedicated restoration networks trained on finite paired data struggle with this diversity, especially when low-frequency color banding and high-frequency stripes co-occur. We present DemoiréEdit, a content-preserving editing framework that adapts the natural-image prior of a pretrained flow-matching editor to demoiréing. First, an endpoint-supervised training objective supplements velocity matching with pixel, perceptual, and frequency-domain restoration losses. Second, a dual-scale condition-shift strategy performs global correction at low resolution, then refines the image at full resolution by shifting the denoising condition from the first-stage output to the original input for detail recovery. We also introduce DailyMoiré130, a benchmark of challenging moiré in everyday screen photography, comprising 130 smartphone captures across diverse displays with low-frequency color banding, fine high-frequency stripes, and mixed-frequency interference. On the challenging DailyMoiré130 benchmark, our method achieves the lowest residual moiré area and receives 71.3% overall-quality preference in a blind Best-of-7 study with 31 participants. We also evaluate on paired FHDMi/UHDM, reducing residual moiré confidence by 47.1%/9.3% and increasing MUSIQ by 4.3%/2.0% over the best baseline for each metric.

---


### 494. [Tandem: Serving Hybrid Linear-Attention GUI Agents on Mobile NPUs](https://arxiv.org/abs/2610.26660)

**<font color=#1a73e8>作者：</font>** Zhuomin Chen, Jingchao Ni, Xu Zheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Smartphone GUI agents complete tasks in mobile apps by repeatedly reading the screen and asking a model for the next action. Mobile neural processing units (NPUs) enable local execution, keeping screen contents on the phone, but model latency accumulates with every action. Hybrid linear attention models reduce memory requirements, yet reusing their recurrent state requires checkpoints at the appropriate input positions. Agent requests retain instructions but rewrite recent history, so checkpoint policies designed for chat continuation can miss reusable prefixes. Retaining rollback states for speculative decoding can also move prompt processing off the NPU's matrix unit, adding overhead that outweighs decoding savings on short action outputs. A loaded model can further hold the NPU awake between tasks. We present Tandem, a runtime for hybrid GUI agents on mobile NPUs. Tandem saves recurrent state where consecutive prompts diverge, allowing later requests to reuse previously processed context. It keeps most prefill on the matrix unit and produces rollback states through a short per-token tail. Its verification kernel reads each weight block once for all proposed tokens. Between request bursts, Tandem releases NPU power votes without unloading the model. We implement Tandem in this http URL and evaluate it on recorded agent interactions across two Snapdragon generations. On a Snapdragon 8 Elite, Tandem reduces per-step latency by 30% for text-based screen descriptions and 16% for screenshots relative to this http URL's fastest NPU configuration, reduces energy per text step by 33%, and lowers standby power with the model loaded from 0.76 to 0.22 W.

---


### 495. [PACT: Plan-Augmented Coordination via Trace-Graphs for Dynamic Multi-Agent Combinatorial Optimization](https://arxiv.org/abs/2610.26671)

**<font color=#1a73e8>作者：</font>** Xiao Zhou, Alex Schutz, Victor-Alexandru Darvariu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-agent approaches have been investigated recently as a means of improving the scalability of reinforcement learning for neural combinatorial optimization. Existing methods assume that all problem instance information is known upfront. However, real-world problems are often dynamic: relevant information is progressively revealed as the agents take actions (e.g., arriving at an edge in a routing problem only to discover it is untraversable). In such cases, existing methods fail to coordinate agents to explore and exploit the progressively revealed information. To address the arising coordination challenge, we introduce PACT (Plan-Augmented Coordination via Trace-graphs). PACT augments the environment graph with auxiliary nodes representing the plans of agents, which are connected to the resource nodes to indicate future dependencies. The proposed message-passing scheme over the augmented graph grounds inter-agent coordination in the environment and enables proactive, rather than reactive, conflict resolution. We show that PACT improves solution quality in dynamic problems relative to baselines and exhibits the best transfer to larger instances on which, remarkably, it outperforms centralized oracles with privileged access to instance uncertainty.

---


### 496. [StepBench: Diagnosing Real-World Procedural Understanding in AI Agents](https://arxiv.org/abs/2610.26679)

**<font color=#1a73e8>作者：</font>** Hossein A. Rahmani, Bin Wu, Chaeeun Lee 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating an agent's planning ability remains challenging for open-domain tasks, where verifying procedures through execution is often impractical. Existing evaluations typically assess only the final plan and do not distinguish procedural errors such as missing, incorrect, or misordered actions. We introduce STEPBENCH, a benchmark of 6,885 verified procedures crawled from wikiHow across 81 open-domain categories. From each procedure, we derive 5 diagnostic tasks: four with deterministic answers involving withheld, incorrect, or shuffled steps, and one requiring next-step generation. We additionally evaluate full-plan generation to examine how diagnostic performance correlates with end-to-end plan validity. Using the same procedures across tasks lets us directly compare different planning capabilities. For generation, STEPEVAL identifies critical failures that prevent goal completion. Across 14 configurations of 12 models, we find substantial differences across planning capabilities, with step ordering proving the most difficult: the strongest model correctly orders only 63.0% of procedures, dropping to 33.1% for those with nine or more steps. Incorrect-step detection also predicts judged plan validity across models, suggesting a lower-cost alternative for evaluating generation quality. On STEPBENCH-Val, comprising 214 procedures published in 2026, comprehension scores and rankings remain stable, suggesting limited influence from memorisation.

---


### 497. [From Short Clips to Real-Time Streams: Identity-Aware Supervision and Context-Efficient Generation for Video Face Swapping](https://arxiv.org/abs/2610.26681)

**<font color=#1a73e8>作者：</font>** Zekai Luo, Yuwei Liang, Ruiqi Ma 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video face swapping transfers the reference identity to a target video while preserving its other attributes and motion. Despite recent progress in reference-guided flow-based methods, jointly achieving faithful identity transfer, high fidelity, and real-time generation over long video streams remains challenging. To address this challenge, we rethink the task-specific structure of reference-guided video face swapping. First, face swapping changes only identity while preserving most visual content, yet flow-matching supervision is weakly sensitive to these changes. We therefore develop Joint Rec-ID Loss, which balances explicit identity supervision and latent reconstruction according to the noise level. Second, the target video already provides non-edited attributes and temporal dynamics, enabling generation with fewer spatial tokens and shorter temporal contexts through Face-RoI Generation and Short-Context Rollout Training. By integrating these designs, we propose StreamingSwap, a reference-guided flow-matching framework for real-time streaming video face swapping. We also introduce HumanFaceVid, comprising 1,000 hours of cinematic training data and evaluation sets of 200 short and 200 long videos. Experiments demonstrate that our method achieves competitive identity transfer and visual quality at 20 FPS on a single NVIDIA RTX 4090 GPU, with stable generation over videos up to 10 minutes long. Project webpage: this https URL

---


### 498. [BrushOff: Stroke-Based Re-rendering as a Watermark Removal Attack on Painting](https://arxiv.org/abs/2610.26682)

**<font color=#1a73e8>作者：</font>** Hao Chen, Junnan Xu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Invisible watermarks are used to mark who owns a painting. We show that a simple attack removes the most robust one we test. The attack redraws the watermarked painting with brush strokes, using a pretrained stroke-based renderer. We call this attack BrushOff. It needs no training, no knowledge of the watermark, and no generative model. We test four watermarks on 500 paintings from five styles. VINE, a recent watermark built to survive image editing, survives all 14 conventional distortions we test, with at least 97.8% detection. Repainting lowers its detection to 1.8%, while the output keeps a no-reference quality score close to that of the clean paintings. Diffusion regeneration can also remove VINE, but at the same removal level it moves the image twice as far from the painting in DreamSim distance, and it changes what the painting shows. Because the renderer draws a countable number of strokes, we can control the attack strength step by step. Finally, we test what kind of signal survives. A simple probe that stores bits in the relative brightness of neighboring regions survives repainting, while a probe that uses absolute brightness does not. The same probe fails under diffusion regeneration, while VINE fails under repainting. Robustness to these two attacks is therefore a separate property, and benchmarks should test both.

---


### 499. [Intra-Rubric Reward Divergence: Mitigating Rubric Hacking through Latent Dimension Recovery and Balancing](https://arxiv.org/abs/2610.26685)

**<font color=#1a73e8>作者：</font>** Jianqiang Xia, Han Xu, Dianxi Shi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rubric hacking limits both performance and training robustness in rubric-based reinforcement learning. By decomposing rubrics into sub-dimensions, we reveal the Intra-Rubric Reward Divergence: as the total rubric score increases, certain sub-dimension scores systematically decrease, suggesting the model sacrifices specific quality aspects to optimize the aggregated objective. From the sub-dimension perspective, we observe two phenomena: (1) dimension imbalance, causing the policy to favor heavily covered dimensions; (2) dimension absence, leading to a systematic gap between rewards and true quality. To mitigate these issues, we propose Fair-Race Dimension Aggregation (FRDA), which has generations compete within each dimension separately to mitigate rubric imbalance, and Residual Semantic Dimension Completion (RSDC), which mines evaluation dimensions implicitly encoded in a holistic preference signal to complete rubric coverage. Experiments in chat, science, and medical domains indicate that FRDA mitigates rubric hacking with more stable improvements, while RSDC outperforms both single-reward training and naive multi-reward aggregation, yielding generally higher-quality responses.

---


### 500. [Hierarchical Token Merging with Recursive Autoencoders for Unsupervised Grammar Induction](https://arxiv.org/abs/2610.26695)

**<font color=#1a73e8>作者：</font>** Murat Guney Kemal, Robert Lieck  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hierarchical abstraction is a fundamental principle across many data modalities, enabling complex sequences to be represented compositionally at multiple levels. Learning such hierarchies directly from data, without explicit structural supervision, remains a central challenge in representation learning. We investigate whether meaningful hierarchical structure can emerge from compression alone. While autoencoders learn compressed representations through reconstruction, this objective does not necessarily favour meaningful compositional structure. We study this challenge through unsupervised grammar induction, where the underlying hierarchy can be evaluated explicitly. We introduce a hierarchical token-merging autoencoder that recursively combines adjacent tokens into increasingly abstract representations, compressing entire sequences through a variational information bottleneck. The model jointly learns representations and hierarchical structure by marginalising over possible binary trees using dynamic programming. To address training instability, we combine independently trained models through unsupervised consensus and distillation. Experiments on a synthetic, ambiguous grammar demonstrate the emergence of meaningful hierarchical structure without structural supervision. The resulting model achieves 93% grammatical parse-validity and 93% exact reconstruction on held-out sequences, compared with 42% parse-validity for the strongest trivial baseline. These findings establish a proof of concept for hierarchical token merging as a mechanism for unsupervised structure discovery and abstraction learning.

---


> [!TIP]
> 当前位于：**451-500**（第 10/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-534](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
