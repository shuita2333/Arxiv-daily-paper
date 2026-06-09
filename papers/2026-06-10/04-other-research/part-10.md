# 📦 其他研究 | 2026年06月10日

> 本类共 **527** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**451-500**（第 10/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-527](./part-11.md)

---

### 451. [LargeMonitor: Monitoring Online Task-Free Continual Learning via Large Pretrained Models](https://arxiv.org/abs/2606.09430)

**<font color=#1a73e8>作者：</font>** Mingqi Yuan, Xiaoquan Sun, Shihao Luo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online task-free continual learning (TFCL) requires intelligent agents to sequentially accumulate knowledge from an unbounded, non-stationary data stream under strict single-pass constraints and without any explicit task identifiers. Existing online TFCL paradigms primarily rely on parameter-efficient prompt tuning or dynamic structure expansion driven by training-coupled optimization dynamics, such as empirical loss fluctuations or evolving latent distances. As a result, these training-coupled solvers remain agnostic to the structural origins of distribution drift, mechanically enforcing a fixed strategy across fundamentally distinct streaming variations. To address this gap, we propose LargeMonitor, a framework that leverages large pretrained foundation models to autonomously orchestrate task-free continuous adaptation. Specifically, LargeMonitor introduces a decoupled detection module utilizing the frozen, stable representation space of large vision models (LVMs) to achieve robust, zero-shot drift detection without training-dependent interference or brittle threshold tuning. Upon a confirmed drift, the framework activates a context-aware diagnostic module driven by large multimodal models (LMMs) to interpret the precise semantic etiologies of the stream variation (e.g., novel class emergence vs. environmental domain shift). This dual-stage capability empowers the continuous learner to dynamically deploy adaptive and shift-specific optimization strategies. Extensive experiments across multiple TFCL settings and benchmarks demonstrate that LargeMonitor achieves precise, robust detection and diagnosis of complex data streams while consistently improving the performance of existing online TFCL algorithms.

---


### 452. [Graph Mamba Operator: A Latent Simulator for Interacting Particle Systems](https://arxiv.org/abs/2606.09432)

**<font color=#1a73e8>作者：</font>** Karn Tiwari, Niladri Dutta, N M Anoop Krishnan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modeling interacting dynamical systems requires capturing spatial interactions alongside long-range temporal dependencies. Graph neural networks (GNNs) provide a natural representation but typically rely on autoregressive rollouts and treat spatial and temporal dynamics separately, leading to error accumulation over long horizons. Existing approaches also focus on local interactions and short temporal contexts, limiting their ability to capture multi-hop dependencies and global structure. We introduce the Graph Mamba Operator (GraMO), a latent-space simulator that integrates state-space models with graph-based interaction learning. In contrast to prior work that sequences nodes or applies spatial and temporal updates in separate stages, GraMO couples graph-based interactions and temporal state updates within a single recurrence. The update is linear in the latent state, with input-dependent coefficients that adapt across regimes. We evaluate GraMO on N-body systems, motion capture, and robotics datasets, achieving the lowest error across benchmarks and the largest gains in long-horizon prediction.

---


### 453. [Bayesian Selective Latent Inference for Wastewater-First Influenza Monitoring](https://arxiv.org/abs/2606.09433)

**<font color=#1a73e8>作者：</font>** Yixuan Zhang, Yang Song, Hao Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Wastewater influenza surveillance can reveal community circulation before clinical reporting, but wastewater alone is not a fully identifiable proxy for human burden. Existing wastewater models assume a fixed evidence set, while generic evidence-acquisition methods treat official surveillance streams as interchangeable costly features. We cast wastewater-first influenza monitoring as a selective decision problem: starting from mandatory wastewater evidence, the system must decide whether wastewater is sufficient, which delayed official stream to query next, and when abstention is the only scientifically defensible action under source ambiguity. We propose Bayesian Selective Latent Inference (BSLI), a principled Bayesian method that maintains a posterior over latent burden and identifiability, certifies answerability through explicit scientific gates, and optimizes query-stop decisions with an exact cost-calibrated Bellman policy. We prove the key variational, answerability, Bellman-optimality, and one-dimensional cost-calibration properties. On a fixed public-data benchmark with 5,933 forecasting episodes and 3,102 source-ambiguity episodes, BSLI improves the matched-budget cost-performance frontier while preserving conservative abstention under source ambiguity.

---


### 454. [Operator learning for solving Fokker-Planck equations with various initial conditions](https://arxiv.org/abs/2606.09434)

**<font color=#1a73e8>作者：</font>** Li Zeng, Xiaoliang Wan, Yaobin Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Fokker-Planck equation (FPE) plays a pivotal role in describing the time evolution of probability density functions (PDFs) for systems governed by stochastic dynamics. In this work, we propose a conditional normalizing flow-based physics-informed neural network (PINN) framework for efficiently approximating the solution operator of the FPE for a whole range of initial conditions. Leveraging the Chapman-Kolmogorov equation for Markovian stochastic processes, the problem is reformulated into approximating a transition PDF starting at initial time from a Dirac mass centered at an arbitrary point. The PDF of an associated linearized stochastic differential equation (SDE) is employed as the base distribution for the normalizing flow, providing a good approximation of the target PDF, especially for small times, and thereby avoiding the singularity of the map associated with the Dirac delta initial distribution. Furthermore, a time-weighted loss function is introduced to mitigate numerical instabilities arising at small times, achieving a balance between causality and training difficulty as time progresses. A variety of numerical experiments are presented to illustrate the effectiveness and robustness of the proposed method.

---


### 455. [Reasoning without Gold Standards: A Proxy-Judge Theory of Autoformalization](https://arxiv.org/abs/2606.09449)

**<font color=#1a73e8>作者：</font>** Lei Xu, Xin Quan, André Freitas  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Complex reasoning tasks increasingly require systems to produce outputs whose correctness cannot be judged by exact match against a single reference. Autoformalization (AF) is a representative example; it asks a model to translate informal mathematical or logical reasoning into a formally checkable object, yet expert-validated formalizations do not scale beyond toy cases and a single informal argument can admit many valid formal renderings. Progress therefore depends on whether partial, structured proxies can substitute for exact references.
We introduce a reference-free proxy-judge framework for AF that replaces gold-standard matching with a vector of per-axis property checks. The framework organizes the proxy along three structural scopes that cover global properties of the elicited object, per-module properties internal to its sub-components, and cross-domain properties that re-align it to the informal source, and aggregates each axis into a verdict vector. The vector drives a reflective refinement loop in which a violated coordinate routes the controller to a matching repair target, so each iteration changes only what is judged wrong.
Under bounded judge noise, the expected intrinsic gap contracts geometrically to a noise-dependent plateau. Across seven formalization backbones on miniF2F, ProofNet, e-SNLI, and ProntoQA, refinement consistently lifts Pass Rate over the single-shot ICL baseline, and the per-axis proxy outperforms a matched scalar proxy on benchmarks where the baseline has room to improve. Structured proxy judgments therefore provide both a practical refinement signal and a theoretical handle on convergence when exact references are unavailable.

---


### 456. [Escaping the KL Agreement Trap in On-Policy Distillation](https://arxiv.org/abs/2606.09471)

**<font color=#1a73e8>作者：</font>** Haoran Xin, Anhao Zhao, Ying Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) provides dense token-level supervision by asking a teacher to score student-generated rollouts. However, when the student drifts into an unrecoverable prefix, the teacher may locally agree with the degraded state, producing low reverse KL but little corrective training signal. We identify this persistent regime as a low-KL agreement trap. Further analyses show that tokens during and after such traps produce less useful supervision signals. We propose KAT (KL Agreement Trap Termination), an online OPD termination rule that detects persistent low-KL agreement with a dynamic training-adaptive threshold. By filtering weak supervision from degenerate agreement, KAT improves avg@k accuracy by 2.66% and pass@k by 3.43% across four mathematical benchmarks, while reducing average rollout length by 59.73%.

---


### 457. [Training-Free Generalized Few-Shot Segmentation through Open-Vocabulary Semantic Arbitration](https://arxiv.org/abs/2606.09474)

**<font color=#1a73e8>作者：</font>** Silas Kwabla Gah, Ebenezer Owusu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generalized Few-Shot Semantic Segmentation (GFSS) has traditionally been approached as a representation-learning problem, requiring task-specific adaptation to incorporate novel classes from limited support examples. Recent foundation models, however, already exhibit strong open-vocabulary recognition and segmentation capabilities, raising a different question: can GFSS be solved through inference-time coordination of frozen semantic priors rather than parameter adaptation? We answer this question with Open-V, a training-free GFSS framework that combines Segment Anything (SAM3) Promptable Concept Segmentation (PCS) with a K-shot CLIP support centroid through calibrated per-pixel semantic arbitration. OpenV introduces no trainable components and supports arbitrary semantic categories at inference time. Beyond segmentation performance, our study contributes three broader findings. First, we show that support information can be incorporated through inference-time semantic grounding, and that its contribution increases as foundation-model text priors weaken on label-disjoint vocabularies. Second, we identify a reproducibility confound in foundationmodel segmentation, demonstrating that preprocessing and evaluation-space mismatches can silently distort reported performance. Finally, we validate Open-V across PASCAL5i, COCO-20i, and ADE-OW, showing that training-free coordination of foundation-model priors generalizes across both conventional GFSS and open-vocabulary evaluation settings. On PASCAL-5i (1-shot), Open-V attains base/novel/harmonic mIoU of 78.4/77.5/77.9, without GFSS-specific training surpassing the strongest trained baseline by +17.7 HM.

---


### 458. [Efficient Minimal Solvers for Visual-Inertial Relative Pose Estimation in Multi-Camera Systems](https://arxiv.org/abs/2606.09477)

**<font color=#1a73e8>作者：</font>** Tao Li, Zhenbao Yu, Banglei Guan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Estimating the relative poses of multi-camera systems is a fundamental problem in computer vision, with critical applications in autonomous vehicles, mobile devices, and unmanned aerial vehicles (UAVs). However, existing solutions often suffer from high computational complexity or rely on an excessive number of point correspondences, limiting their real-world applicability. To address these limitations, we propose two efficient minimal solvers for estimating the relative poses of multi-camera systems using a novel parameterization. The first solver leverages the vertical direction prior provided by Inertial Measurement Units (IMUs), while the second utilizes the rotation axis direction prior from IMUs. Our methods require only four point correspondences and reduce the problem of multi-camera relative pose estimation to solving a univariate 6th-degree polynomial, a significant improvement over existing approaches, which typically involve 8th-degree polynomials. This reduction in computational complexity and correspondence requirements makes our solvers particularly effective when integrated into RANSAC frameworks, demonstrating strong potential for visual odometry applications. Through rigorous evaluations on synthetic data and the KITTI benchmark, our methods achieved superior computational efficiency and competitive accuracy compared to state-of-the-art algorithms.

---


### 459. [Optical Music Recognition for Real-World Manuscripts with Synthetic Data](https://arxiv.org/abs/2606.09479)

**<font color=#1a73e8>作者：</font>** Jiří Mayer, Martina Dvořáková, Vojtěch Dvořák 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical Music Recognition (OMR) has seen major progress in model design, with end-to-end methods now capable of recognising notation at all levels of complexity. However, the impact of this progress has been limited by the visual domains of available training datasets, which are largely born-digital. Existing large collections of sheet music in libraries and other heritage institutions contain predominantly manuscripts, whose visual domains are highly diverse and different, so existing OMR systems fail when applied in the real world. These institutions are often resource-constrained, so large in-domain datasets cannot be expected. We provide a first baseline on real-world manuscripts with complex piano notation in the resource-constrained scenario. Using fine-grained music notation graph (MuNG) annotations and the Smashcima synthesis tool, we then show that while some direct transcriptions of in-domain data remain essential, domain adaptation using synthetic musical manuscript images brings significant improvement. Furthermore, the symbols used do not need to be in-domain, so the expensive fine-grained annotation can be avoided. We thus bring OMR closer to one of its stated goals: preserving and promoting musical cultural heritage.

---


### 460. [Loss-Guided Adaptive Scale Refinement for Molecular Force Prediction](https://arxiv.org/abs/2606.09480)

**<font color=#1a73e8>作者：</font>** Limin Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular systems involve interactions across multiple spatial scales, from local coordination and short-range perturbations to long-range electrostatic and solvent-mediated effects. However, most molecular representation learning methods rely on manually predefined scales, and the task-optimal modeling scale may not coincide with these fixed levels. This study introduces a loss-guided adaptive scale refinement framework for molecular force prediction, treating predefined scales as initial anchors and discovering task-effective resolutions through interpolation, routing, differentiable scale updates, and scale pool refinement.
Using a NaCl aqueous ionic system as a minimal testbed, this study constructs short-scale and long-range force prediction branches and analyzes their complementarity. Oracle hard routing reduces the overall force MAE from 399.65 to 382.67, while continuous oracle interpolation further reduces it to 380.96. In close-contact regimes with nearest-ion distance below 0.6 nm, the close-contact MAE decreases from 327.22 to 260.51. A minimal scale pool update experiment shows that starting from endpoint anchors {0,1}, loss-guided updates automatically generate intermediate scales and recover most of the continuous oracle performance. The final updated scale pool {0,0.125,0.25,0.375,0.5,0.75,1} achieves an overall MAE of 381.23.
These results support adaptive scale refinement as a promising direction for molecular representation learning, especially when fixed-scale modeling is insufficient.

---


### 461. [ContextShift: A Controlled Benchmark for Context Dependence in Object Detection](https://arxiv.org/abs/2606.09495)

**<font color=#1a73e8>作者：</font>** Dan Zlotnikov, Alex Lazarovich, Ohad Ben-Shahar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern object detectors achieve strong performance on standard benchmarks, yet their robustness to contextual variation remains insufficiently understood. Prior evaluations largely rely on aggregate metrics such as AP on uncontrolled distribution shifts, which can obscure how performance degrades under context change. We introduce ContextShift, a controlled benchmark that systematically manipulates object--context relationships while preserving object appearance. Built on COCO 2017, it isolates context as an independent variable through geometric transformations and synthetic and natural background substitutions, including a continuous compatibility axis based on normalized pointwise mutual information (NPMI). Across diverse detector architectures, we observe a consistent degradation pattern: false negatives increase by up to 227% and prediction volume decreases by up to 44%, while false positives remain stable or decline. This suppression behavior is not captured by aggregate metrics such as AP, which can mask substantial recall loss and changes in prediction dynamics. Further analysis suggests that degradation is driven less by reduced confidence than by a reduced formation of valid detection candidates. Moreover, performance along the statistical compatibility axis is non-monotonic, peaking at intermediate NPMI and degrading toward both extremes, indicating that statistical co-occurrence does not correlate linearly with effective visual context. Finally, we show that context-aware augmentation improves robustness: every augmented variant outperforms the dataset-only baseline on both original and manipulated test images, partially recovering performance lost to prediction-suppression failures by exposing models to object--context decoupling during training.

---


### 462. [Self-Harness: Harnesses That Improve Themselves](https://arxiv.org/abs/2606.09498)

**<font color=#1a73e8>作者：</font>** Hangfan Zhang, Shao Zhang, Kangcong Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The performance of LLM-based agents is jointly shaped by their base models and the harnesses that mediate their interaction with the environment. Because different models exhibit distinct behaviors, effective harness design is inherently model-specific. Yet agent harnesses are still largely engineered by human experts, a paradigm that scales poorly as modern LLMs become increasingly diverse and rapidly evolving. In this paper, we introduce Self-Harness, a new paradigm in which an LLM-based agent improves its own operating harness, without relying on human engineers or stronger external agents. We operationalize Self-Harness as an iterative loop with three stages: Weakness Mining, which identifies model-specific failure patterns from execution traces; Harness Proposal, which generates diverse yet minimal harness modifications tied to these failures; and Proposal Validation, which accepts candidate edits only after regression testing. We instantiate Self-Harness on Terminal-Bench-2.0 using a minimal initial harness and three base models from diverse families: MiniMax M2.5, Qwen3.5-35B-A3B, and GLM-5. Across all three models, Self-Harness consistently improves performance, with held-out pass rates increasing from 40.5% to 61.9%, 23.8% to 38.1%, and 42.9% to 57.1%, respectively. Qualitative analyses further show that Self-Harness does not simply add generic instructions, but effectively turns model-specific weaknesses into concrete, executable harness changes. These results suggest a path toward LLM-based agents that are not merely shaped by their harnesses, but can also participate in reshaping them.

---


### 463. [SwiftVR: Real-Time One-Step Generative Video Restoration](https://arxiv.org/abs/2606.09516)

**<font color=#1a73e8>作者：</font>** Jiaqi Yan, Xiangyu Chen, Xinlin Zhong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time video restoration (VR) for live streams requires high-resolution outputs under strict per-frame latency constraints. Existing one-step diffusion-based VR models remain difficult to deploy on consumer-grade GPUs due to two main bottlenecks: quadratic spatial attention at high resolutions and the latency-memory overhead of large video autoencoders. We present SwiftVR, a streaming one-step generative VR framework that reduces both bottlenecks under a causal chunk-wise protocol. For attention, mask-free shifted-window self-attention gathers each spatial window into a dense tensor via deterministic indexing, keeping all attention calls on the dense scaled dot-product attention path without masks, cyclic shifts, padding, or hardware-specific sparse kernels. Because SwiftVR uses only standard dense SDPA calls, the trained model transfers to consumer GPUs without retraining or custom kernels. For autoencoding, a lightweight Restoration-aware Autoencoder enables fast chunk-wise decoding while preserving reconstruction quality. On a single H100, SwiftVR sustains 31~FPS at 2560x1440 and 14~FPS at 3840x2160, whereas all compared diffusion-based VR baselines exceed the memory limit at 4K. On a consumer RTX~5090, SwiftVR reaches 26~FPS at 1920x1080. To our knowledge, SwiftVR is the first generative VR model to achieve real-time 1080p streaming on a consumer-grade GPU, while attaining strong no-reference perceptual quality with lower inference cost. Project is available at this https URL.

---


### 464. [Investigating Calibration Challenges in Probabilistic Electricity Price Forecasting](https://arxiv.org/abs/2606.09517)

**<font color=#1a73e8>作者：</font>** Jan Niklas Lettner, Hadeer El Ashhab, Benjamin Schäfer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As renewable energy integration increases market volatility, probabilistic electricity price forecasting has become essential for effective risk management. However, current-proper-scoring rules often prioritize forecast sharpness at the expense of calibration, leading to overconfident and statistically unreliable uncertainty estimates. This work highlights the critical gap between theoretical scoring and practical calibration, demonstrating that models can become mere proxies for deterministic forecasts when reliability is neglected. We conclude that future research must shift toward calibration-aware objectives and architectures to ensure the distributional integrity of energy market forecasts.

---


### 465. [Overcoming Decoder Inconsistencies in Whisper for Dravidian and Low-Resource Languages](https://arxiv.org/abs/2606.09535)

**<font color=#1a73e8>作者：</font>** Chowdam Venkata Kumar, Kumud Tripathi, Pankaj Wasnik  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual ASR models such as Whisper perform well on high-resource languages but exhibit substantially higher Word Error Rates (WER) for Dravidian languages compared to Indo-Aryan ones. Through linguistic and dataset analysis, we show that Dravidian languages have longer words, higher vocabulary diversity, and lower repetition, resulting in sparse token distributions and frequent character-level substitution errors. Baseline fine-tuning further reveals decoder imbalance between self-attention (linguistic context) and cross-attention (acoustic cues). Although synthetic token-repetition experiments indicate potential gains, they are impractical. Motivated by these observations, we introduce two decoder-level enhancements: Weighted-Attention, which adaptively balances attention sources, and Self-Conditioning, which reinjects intermediate predictions to improve token consistency. Experiments demonstrate consistent WER reductions for low-resource and agglutinative languages.

---


### 466. [Adversarial Attack and Disturbance Detection by Hadamard-Coded Output Representations for Object Detection and Semantic Segmentation](https://arxiv.org/abs/2606.09536)

**<font color=#1a73e8>作者：</font>** Lucas Görnhardt, Timo Bartels, Niklas Schwarz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conventional one-hot encodings often yield poorly calibrated models, being overconfident under attack, and letting entropy-based detection algorithms fail. Previous image classification works have demonstrated that Hadamard-coded output representations can improve adversarial robustness. However, attempts to integrate Hadamard codes into semantic segmentation fall far behind state-of-the-art models in mean intersection-over-union performance. Regarding object detection, such output encodings have not yet been investigated at all. Further, no prior art addressed intrinsic codeword inconsistencies or actually exploited intrinsic codeword redundancy. Accordingly, we first derive a novel decoding procedure for Hadamard codewords towards optimal class-wise probabilities, solving the underlying optimization problem by using the projection onto the probability simplex. Second, our optimization delivers a measure of prediction inconsistency. Third, we are the first to show how to exploit these inconsistencies for adversarial attack and disturbance detection. Fourth, we introduce HadamardNet, a framework employing Hadamard codes as output representations for semantic segmentation and object detection models and tasks. We conduct a comprehensive evaluation both on disturbances and adversarial attacks, achieving state-of-the-art perturbation detection performance for both tasks in only a single detection pass, while delivering equivalent or close-by reference performance on clean data.

---


### 467. [Efficient Traffic Prediction at Scale: A Systematic Study of STGCN Architectural Depth](https://arxiv.org/abs/2606.09539)

**<font color=#1a73e8>作者：</font>** Soban Nasir Lone, Mohamed Abouelela, Taeyoung Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatio-temporal graph neural networks (STGNNs) have become the dominant approach for traffic prediction, yet their computational requirements pose challenges for practical deployment in intelligent transportation systems (ITS). While recent work has proposed efficient alternatives to STGNNs, a fundamental question remains unexplored: are these architectures themselves over-parameterised? We examine this question using the Spatio-Temporal Graph Convolutional Network (STGCN), one of the most widely adopted models in this domain. Through systematic experiments across four diverse traffic datasets, we compare 1-block, 2-block (standard), and 3-block STGCN variants. Our findings reveal that the single-block architecture achieves optimal performance for short-term prediction (10 mins) on three of four datasets, while incurring only marginal degradation ($\leq$1.8% relative error) at longer horizons. Crucially, the 2-block variant incurs 61% higher CPU inference latency and 37% lower throughput relative to 1-block -- substantial overhead for resource-constrained ITS deployment. The 3-block architecture offers no favourable tradeoff, more than doubling computational cost for $<$0.5% relative improvement. These results suggest that the default 2-block STGCN may be over-parameterised for many applications, with implications for both practitioners deploying traffic prediction systems and researchers benchmarking efficiency-focused methods.

---


### 468. [A VideoMAE-v2 Approach to Zero-Shot Traffic Accident Anticipation](https://arxiv.org/abs/2606.09542)

**<font color=#1a73e8>作者：</font>** Siyuan Li, Xiaoyang Bi, Mengshi Qi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traffic accident anticipation -- predicting the likelihood of an imminent collision at every frame of a dashcam video -- is safety-critical yet difficult to scale, because collecting in-domain annotated accident footage for every deployment scenario is prohibitively expensive. We study this task under a zero-shot setting where no target-domain training data is available: the model must learn exclusively from a publicly available binary-labelled driving-accident dataset and generalise to unseen dashcam footage. We propose a framework that bridges the gap between the frame-level temporal risk estimation task and coarsely labelled binary accident datasets by coupling a VideoMAE-v2 backbone with a per-frame prediction head under a sliding-window protocol. Our method achieves 2nd place in the 2026 CVPR@AUTOPILOT Zero-Shot Accident Anticipation competition. Code is available at this https URL.

---


### 469. [From Genes to Tokens: a GWAS-inspired Approach for Interpretable Stylometric Analysis](https://arxiv.org/abs/2606.09543)

**<font color=#1a73e8>作者：</font>** Dmitry Pronin, Evgeny Kazartsev  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This short paper introduces a stylometric interpretation method inspired by genome-wide association studies (GWAS). Each "gene" token's association with "phenotype" authorship is tested using logistic regression with multiple-comparison correction. Applied to English, German, and Russian corpora, the method detects statistically significant lexical markers distinctive of individual authors.

---


### 470. [Model Poisoning Against Federated Model Adaptation with Chain of Bit-Flips](https://arxiv.org/abs/2606.09548)

**<font color=#1a73e8>作者：</font>** Bastien Vuillod, Kevin Hector, Pierre-Alain Moellic 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) allows a set of clients to collectively train a global model without sharing local training data. Giving the responsibility of the training to decentralized actors may lead to poisoning attacks: clients controlled by malicious third party potentially poison the training dataset to install a backdoor in neural networks. In FL, these backdoor attacks rely solely on algorithmic approach, however, recent advances in hardware faults threats (e.g, Rowhammer) have widen the overall attack surface. In the context of federated model adaptation, we introduce a novel category of backdoor attack against FL systems that relies on model poisoning based on hardware-fault attacks. More precisely, we propose a task-agnostic backdoor attack that is implanted during the FL training time by inducing hardware faults (bit-flips) in parameters of a single local model. The backdoor is crafted during a previous offline phase from the pretrained model initially used by the FL system. Our results show that a backdoor can be successfully applied on different type of models and datasets. Typically, with up to 10 faults per malicious client occurrence and 19 total occurrences on a ResNet-18 are enough to reach 94% of attack success rate. Finally, we discuss the practicality and the robustness of the attack potential defenses, while putting into perspective the practical constraints of Rowhammer, which is the preferred attack vector for this type of threats.

---


### 471. [OpenBibleTTS: Large-Scale Speech Resources and TTS Models for Low-Resource Languages](https://arxiv.org/abs/2606.09553)

**<font color=#1a73e8>作者：</font>** David Guzmán, Luel Hagos Beyene, Jesujoba Oluwadara Alabi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in neural text-to-speech (TTS) and multilingual speech generation have substantially improved synthetic speech quality, yet these gains remain unevenly distributed across the world's languages. Existing models are still dominated by a small set of high-resource languages, while many studies of low-resource TTS are simulated on artificially downsampled high-resource corpora that do not reflect the orthographic variation and limited phonetic coverage encountered in genuinely underrepresented settings. As such, we introduce OpenBibleTTS, which is a large-scale benchmark for low-resource speech synthesis spanning 37 underrepresented languages. Moreover, a systematic comparison of various TTS architectures and large-scale speech generation models is conducted across in-domain Biblical text and out-of-domain material. Results show that no single system dominates across languages and metrics: Gemini-TTS achieves the highest listener ratings on most evaluated languages, but monolingual EveryVoice models trained on OpenBibleTTS remain strongest for intelligibility and are preferred in several African languages, while open from-scratch systems degrade sharply on out-of-domain text, revealing a persistent gap between broad multilingual coverage and reliable synthesis quality in underserved linguistic communities. We complement automatic evaluation with subjective human judgments, and open-source all processed datasets, alignments, and trained models to support future low-resource TTS research.

---


### 472. [AI Scientists Are Only as Good as Their Evidence: A Stratified Ablation of Proprietary Data and Reasoning Skills in Drug-Asset Valuation](https://arxiv.org/abs/2606.09556)

**<font color=#1a73e8>作者：</font>** Yinan Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI Scientist agents are often evaluated as if capability were mainly a function of model quality, prompting, or reasoning scaffolds. We test a different hypothesis in drug-asset valuation: for knowledge-intensive scientific decisions, the limiting factor is often the evidence substrate the agent can access. We run a controlled three-arm ablation on a production valuation agent: A is a plain web-only LLM analyst, B adds public structured tools plus a 14-dimension valuation playbook, verifier, objectivity policy and red-team, and C adds the proprietary Noah AI corpus of curated pipeline, trial and deal intelligence. Across a 13-asset stratified benchmark, B improves calibration and audit discipline: tier-in-range accuracy rises from 0.80 to 0.89 and objectivity from 3.16 to 3.30. But B does not remove the factual ceiling. Under capability-superset accounting, A and B recover only 0.25 and 0.38 of the curated gold competitive record, while C recovers 0.96; on the curated long-tail subset, C reaches 0.93 vs. 0.26/0.30. Raw blind-panel decision quality is similar for A and B (7.01 vs. 6.96), so we introduce completeness-aware decision utility: informed decision-quality = decision-quality x gold-coverage. On this metric, C reaches 7.43 vs. 1.76/2.57 for A/B. Even a perfect non-proprietary-data report would be capped at 3.83 by B's coverage. The result is not that reasoning scaffolds are unimportant; they improve calibration and discipline. Rather, proprietary evidence sets the upper bound of what the AI Scientist can know and therefore decide.

---


### 473. [Safe-RULE: Safe Reinforcement UnLEarning](https://arxiv.org/abs/2606.09559)

**<font color=#1a73e8>作者：</font>** Shixiong Jiang, Taozheng Zhu, Fanxin Kong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline safe reinforcement learning (Safe RL) enables policy learning without online interactions, making it suitable for safety-critical systems such as robotics systems. However, its reliance on static datasets exposes offline Safe RL to data poisoning attacks, where adversaries inject malicious samples that compromise safety and induce unsafe policy behavior. In this work, we propose a new learning paradigm, named safe reinforcement unlearning (Safe-RULE), used as a defense framework to remove the influence of poisoned data without retraining from scratch or requiring access to the original training environment. We further extend reinforcement unlearning to offline Safe RL by explicitly accounting for both task performance and safety constraints during the unlearning process. Experiments across benchmark Safe RL tasks demonstrate that our approach effectively enhances safety performance against data poisoning attacks.

---


### 474. [Self-Explainability in Self-Adaptive and Self-Organising Systems: Status and Research Directions](https://arxiv.org/abs/2606.09568)

**<font color=#1a73e8>作者：</font>** Tom Beyer, Svea Wisy, Sven Tomforde  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The growing complexity of self-adaptive and self-organising systems, fuelled by advances in Artificial Intelligence (AI), has made them increasingly difficult to understand and trust. While Explainable AI aims to provide insight into AI decision-making, a more advanced goal is for systems to explain themselves - an ability referred to as Self-Explainability (SX). This article presents a systematic literature review on SX, analysing existing approaches, including their domains, targets, and evaluation methods. The review develops a unified definition and taxonomy of SX and introduces Levels of Self-Explainability, providing a framework for positioning current and future research. Our results show that most SX approaches remain conceptual, with few practical implementations. Moreover, there is currently no formal or de facto standard for evaluating SX, highlighting a major research gap. This work thus establishes a foundation and roadmap for advancing Self-Explainability in complex systems.

---


### 475. [UXBench: Benchmarking User Experience in AI Assistants](https://arxiv.org/abs/2606.09570)

**<font color=#1a73e8>作者：</font>** Mengze Hong, Xia Zeng, Zeyang Lei 等 27 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As AI assistants serve millions of users daily, evaluating user experience (UX) beyond general model capability has become increasingly important. We present UXBench, the first user-centric benchmark grounded in real user feedback signals for evaluating preference alignment and dialogue generation. The benchmark consists of three interconnected tasks, UX Judge, UX Eval, and UX Recovery, with 7,400 test instances extracted from over 70K interaction logs of a mainstream Chinese AI assistant. The dataset closely reflects real user distributions, covering 8 scenarios, 83 domains, and diverse failure patterns that pose severe challenges. Extensive experiments on 26 frontier language models provide novel insights into how well models perceive user experience and how improvements in model capability contribute to better dialogue engagement. Through comprehensive analysis of model behavior and performance gaps, we show that user feedback prediction is a learnable capability, where a reward model trained from in-the-wild feedback signals can achieve well-calibrated accuracy. We further document the systematic biases of LLM-as-a-judge evaluation protocols and compare typical response strategies that directly affect user experience. UXBench establishes a new evaluation landscape and calls for greater attention to tailored UX optimization, contributing to a user-centric scaling law that shapes the success of AI assistants.

---


### 476. [On Choosing the $μ$ Parameter in Gaussian Differential Privacy](https://arxiv.org/abs/2606.09582)

**<font color=#1a73e8>作者：</font>** Bogdan Kulynych, Antti Honkela  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work argues for using Gaussian differential privacy (GDP) to report the privacy guarantees in privacy-preserving machine learning. We provide principled mappings from pure-DP $\varepsilon$ to GDP $\mu$ by matching the worst-case success of a strong-adversary membership inference attack in terms of three metrics: multiplicative advantage at fixed FPR, precision at fixed recall, and the standard privacy profile. We tabulate $\mu$ values across a useful range of parameters and recommend $\mu \approx \varepsilon/5$ as a conservative general-purpose conversion.

---


### 477. [Seeing the Hivemind: A Consensus-Aware Interaction Technique for Mitigating AI Homogenization](https://arxiv.org/abs/2606.09587)

**<font color=#1a73e8>作者：</font>** Muhammad Haris Khan, Joel wester  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> People are increasingly using AI for creative tasks such as writing. While adoption continues to grow, this form of use risks undermining individual creativity locally and reducing the heterogeneity of creative output at scale. In response, we introduce the Semantic Repulsion Technique (SRT) and evaluate it both computationally and through a study with 16 participants who regularly use AI for creative tasks. Our computational assessment reveals that SRT increases semantic diversity by 85--167\% while reducing consensus phrases by 43--95\% across task modes. In the user study, SRT outputs received higher usefulness ($p = .019$, $W = .208$) and coherence ratings ( $p = .006$, $W = .260$); 68.8\% of participants were willing to use SRT-Strong for multiple tasks versus 18.8\% for baselines. Originality and coherence ratings were positively correlated across all systems ($\rho = +.40$ to $+.67$), suggesting that divergence need not compromise readability. Taken together, these preliminary findings can inform the design of AI systems that aim to support everyday creativity without contributing to homogenization.

---


### 478. [Clinically Grounded Privacy Evaluation of Medical LMs](https://arxiv.org/abs/2606.09590)

**<font color=#1a73e8>作者：</font>** Sasha Ronaghi, Sana Tonekaboni, Lena Stempfle 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medical language models (LMs) can memorize and reproduce protected health information, but privacy evaluations often focus on recovery of training text rather than disclosure under realistic threat models. We introduce a clinically grounded framework that evaluates leakage along a graded axis of adversarial access, ranging from publicly inferable demographics to leaked note fragments. At each tier, we measure verbatim memorization of patient-specific text and semantic leakage of sensitive diagnoses. Applying the framework to an LM pretrained on 378k clinical notes, we find that routine encounter metadata (i.e. name, date of birth, provider, practice, visit date) elicits high rates of verbatim memorization across a patient's timeline and sensitive-diagnosis recovery (AUROC 0.91 for abortion, 0.81 for HIV). At the same time, exact-match memorization can overstate disclosure: 36% of memorized tokens reflect templated documentation. Our work highlights the risks of training on longitudinal clinical data, providing a practical framework for contextual privacy evaluation of medical LMs.

---


### 479. [Assessing Sample Quality in Conditional Generation under Compositional Shift](https://arxiv.org/abs/2606.09601)

**<font color=#1a73e8>作者：</font>** Berker Demirel, Valentino Maiorca, Marco Fumero 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conditional generators provide a natural tool for controllable generation, including settings where the desired condition is a new composition of observed attributes or experimental factors. In many applications, especially in scientific domains, such models are attractive to explore conditions for which real samples are rare, expensive, or not yet observed. However, this creates a circularity for evaluation: standard conditional quality metrics require a reference target distribution, but in the extrapolative regime that distribution is unavailable by definition. We address this problem with a post-hoc, per-sample trust score for assessing conditional samples using only the training distribution. The score combines two estimable quantities: global realism, measuring compatibility with the real data manifold, and attribute-wise faithfulness, measuring whether a sample is closer to the requested attributes than to plausible alternatives. We show that the score can recover meaningful comparisons across extrapolated generations, under a mild coverage condition on the observed attributes. These comparisons enable effective filtering, ranking, and abstention of generations and can be used directly on off-the-shelf pretrained models. In biological imaging, selected samples preserve real morphological structure better and improve downstream predictive performance, while similar gains are observed on controlled vision benchmarks. Finally, we show how the score can be applied during generation, enabling abstention before full decoding. Code is available at this https URL.

---


### 480. [Next-Token Prediction Learns Generalisable Representations of Sleep Physiology](https://arxiv.org/abs/2606.09605)

**<font color=#1a73e8>作者：</font>** Jonathan F. Carter, Lionel Tarassenko  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Foundation models offer a promising route to compress multi-modal physiological signals into compact representations of human health, with broad applications across sleep medicine, cardiology, neurology and other healthcare domains. Existing models have typically been trained with masked-reconstruction or contrastive objectives. However, masked reconstruction may be poorly suited to the stochastic nature of these signals, while contrastive approaches rely on positive-pair definitions despite the semantic invariances of physiological signals being poorly understood. In this work, we show that next-token prediction is a simple and scalable alternative. We develop Hypnos, a multi-modal sleep foundation model trained using eight different sensing modalities (e.g. EEG, ECG, respiratory signals) drawn from over 20,000 overnight polysomnography recordings. We tokenize each modality into streams of discrete tokens using residual vector quantization, then train a large auto-regressive RQ-Transformer to jointly predict the next token across all modalities in parallel. After training, Hypnos can be applied to continuous streams of sensor data from any subset of supported modalities, generating embeddings for downstream tasks. Across a range of benchmarks, Hypnos significantly outperforms existing foundation models. In sleep stage classification, we match the performance of strong supervised baselines on held-out test sets whilst using \(100\times\) less labelled data. Hypnos even generalises to daytime physiology, surpassing a dedicated ECG foundation model at detecting atrial fibrillation. Our results demonstrate that next-token prediction is a strong self-supervised objective for representation learning from multi-modal physiological signals.

---


### 481. [Closure-Validated Circuit Discovery in Attention Heads: Co-activation Proposes, Ablation Disposes](https://arxiv.org/abs/2606.09607)

**<font color=#1a73e8>作者：</font>** Yongzhong Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Interpretability increasingly treats groups of components, not individual units, as the basic object, and proposes to find them by clustering co-activation statistics. We ask whether such a cheap signal actually identifies an attention-head circuit. Adapting a sparse-autoencoder clustering recipe to attention heads -- but validating by causal ablation rather than reconstruction -- we cluster heads and then run a closure test: ablate the discovered community and compare per-example damage to matched-random controls. Across two dense 1B-scale models (Pythia 1B, OLMo 1B) and two input distributions, the communities pass closure. In a Mixture-of-Experts model (OLMoE-1B-7B), route-conditional clustering recovers a statistically real signal that nonetheless does not survive closure -- ablation improves loss, the wrong direction. Extending closure across training, attention-target selectivity and participation ratio decouple from function in both directions. We conclude that a cheap signal is a circuit proposal, not a confirmed circuit; closure is what separates them.

---


### 482. [TUDSR: Twice Upsampling-Diffusion for Higher Super-Resolution](https://arxiv.org/abs/2606.09608)

**<font color=#1a73e8>作者：</font>** Zhiqiang Wu, Yitong Dong, Xian Wei  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based generative models have achieved remarkable success in real-world image super-resolution (SR). With tiled diffusion techniques, these models can produce high-resolution images that exceed their native-supported resolution. However, the quality of such high-resolution (e.g $2048^2$) outputs often remains extremely poor, primarily due to two factors we consider: the image upsampling ratio (e.g $\times8$) exceeding the model's native-supported upsampling ratio (e.g $\times4$), and the model's native-supported resolution. In practice, training a native high-resolution model requires larger architectures, which incur significant computational overhead and GPU memory costs, making it hard on limited-resource equipment. Thus, we present TUDSR, a Twice Upsampling-Diffusion framework for higher SR. The TUDSR framework mainly consists of two stages: the first involves training at $R$-resolution, and the second introduces a looped chunk-based training strategy at $NR$-resolution. Each stage adapts a one-step GAN architecture comprising a generator and a discriminator. Based on SD2.1-base, we develop TUDSR-S, which achieves state-of-the-art performance across multiple benchmarks. Extensive experiments further demonstrate that TUDSR-S generates high-quality images at the resolutions of $1024^2$ and even $2048^2$, significantly outperforming existing approaches. Code is available at this https URL.

---


### 483. [Constrained user-item allocation for e-commerce marketing campaigns](https://arxiv.org/abs/2606.09623)

**<font color=#1a73e8>作者：</font>** Maja Lindström, Natalija Glisovic, Jan von Pichowski 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When running marketing campaigns, retailers must decide which products to promote and which users to target. These decisions are inherently coupled: effective campaigns match users and items with strong mutual affinity into non-overlapping groups of predefined sizes. However, existing approaches assume predefined campaign structure or decouple item selection from user assignment, and cannot discover campaign groupings directly from joint interaction patterns. We therefore formalize this campaign problem as auto-targeting: jointly selecting users and items to construct multiple disjoint campaigns. To solve this combinatorial problem, we propose three complementary strategies: (i) constrained spectral biclustering to find dense regions in the user-item affinity matrix, (ii) greedy local search with pairwise swaps for combinatorial refinement, and (iii) a multi-armed bandit framework to escape local optima through exploration. We evaluate these methods on a synthetic dataset, the Amazon Reviews benchmarks, and large-scale proprietary commercial data, and compare the results to simulated annealing as a baseline. The results show that biclustering consistently achieves the highest campaign quality, lift, and fairness scores. While biclustering runs efficiently on smaller datasets, its runtime increases substantially on very large ones, where bandit-based methods instead offer a scalable alternative.

---


### 484. [ATN3D: Density-Aware LiDAR-Radar Early 3D Object Detection Under Extreme Sparsity](https://arxiv.org/abs/2606.09634)

**<font color=#1a73e8>作者：</font>** Debojyoti Biswas, Xianbiao Hu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D object detection is the backbone of perception for automated vehicles (AV) and broader intelligent transportation systems applications. Long-range detection is challenging because sensing evidence is sparse; yet this ``long-range'' scenario is routine in traffic. Although >30m is often labeled long-range in computer vision, on roadways it affords only approx. 1-2s for perception and decision-making. Under such extreme sparsity, two core challenges arise. First, early multimodal fusion tends to discard sparsity information and inject noise from empty or falsely occupied cells, degrading long-range recall. Second, context-agnostic uniform channel supervision favors dense and near-range samples, leaving far and small objects under-optimized, delaying the earliest detection of distant objects. We propose ``Ask The Neighbor'' (ATN3D), a LiDAR-Radar framework tailored for sparse-range conditions. ATN3D introduces (i) Density-aware early fusion with cross-modal gating that conditions fusion on per-voxel density/sparsity and Radar evidence, (ii) Occupancy-gated neighborhood aggregation with circular kernels to aggregate only from credible cells, (iii) Evidence-conditioned channel self-attention to adapt channel weights with weather/range, and (iv) a Range-aware loss that re-balances classification and localization by distance, aligning training with distance-stratified evaluation. On the VoD benchmark across clear and foggy conditions, ATN3D surpasses strong baselines: +3.55% mAP in clear weather and +8.41% mAP under simulated heavy fog; for >30m objects, gains are +3.33% (clear) and +2.09% (heavy fog). These results indicate earlier and more reliable long-range detections under sparse sensing in on-road traffic.

---


### 485. [Data-driven discovery of governing differential equations across physical systems](https://arxiv.org/abs/2606.09638)

**<font color=#1a73e8>作者：</font>** Siyu Lou, Hao Xu, Wenguan Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Differential equations play a critical role in scientific discovery because they provide a mathematical framework to describe the behaviour of physical phenomena. As a promising alternative to traditional first principles, data-driven differential equation discovery has attracted increasing attention for its ability to infer governing laws directly from experimental or simulated data, especially when the underlying physics is unclear. However, the field has expanded rapidly along diverse methodological directions, particularly with the emergence of AI-based approaches, and still lacks a clear organizing perspective. In this Review, we propose a problem-oriented perspective on data-driven differential equation discovery. We first introduce a two-dimensional phase diagram of equation discoverability, where discovery problems are organized according to structural complexity and coefficient complexity. This phase diagram shows how the field has moved from the discovery of sparse equations with simple coefficients toward more complex governing laws with richer structures and more flexible parameterizations. It also clarifies why different methodological families succeed or fail in different problem settings. We then present the representation-evaluation-optimization (REO) framework as a fundamental abstraction of the discovery process. By identifying the core problems of equation discovery that persist across algorithmic variations, REO shifts the discussion from individual algorithms to the fundamental principles that determine discoverability. We connect these perspectives to applications across physics and adjacent sciences, and argue that the next challenge is not merely recovering equations, but using them to revise existing theories, distil mechanisms and form new scientific concepts.

---


### 486. [CineDance: Towards Next-Generation Multi-Shot Long-Form Cinematic Audio-Video Generation](https://arxiv.org/abs/2606.09639)

**<font color=#1a73e8>作者：</font>** Yuheng Chen, Teng Hu, Yuji Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The fidelity and structural diversity of training datasets fundamentally determine the capabilities of video generation models. While commercial systems showremarkableabilitytogeneratecinematicnarratives, the progress of open-source models remains limited by the scarcity of high-quality training data. To bridge this gap, we introduce CineDance-1M, a large-scale, open research Text-to-Audio-Video (T2AV) dataset designed specifically for multi-shot, long-form joint audio-video generation. Averaging 92.8 seconds and 24.2 continuous shots per video, it provides configurable, structured annotations for both audio and video modalities. This exceptional quality is achieved through a rigorous three-stage curation pipeline: i) diverse sourcing and comprehensive cleansing, ii) film-theory-inspired narrative parsing, and iii) hierarchical dual-modal captioning. For a comprehensive assessment, we propose CineBench, featuring a diverse prompt suite and a six-dimensional, human-aligned metric system tailored for complex narrative audio-video evaluation. Furthermore, we adapt LTX-2.3 into CineDance, which demonstrates exceptional single-modality quality alongside precise audio-video alignment and robust subject and environment consistency, effectively validating our curation strategy and the high quality of CineDance-1M. We anticipate that this work will serve as a solid foundation for accelerating future research in multi-shot, long-form joint audio-video generation. Our project page is available at this https URL.

---


### 487. [MAVIS: Multi-Agent Video Retrieval via Structured Video Understanding](https://arxiv.org/abs/2606.09641)

**<font color=#1a73e8>作者：</font>** Jie Zhang, Qilang Ye, Hao Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The dominant paradigm in video retrieval relies on embedding-based full-corpus scanning, which suffers from inherent computational inefficiency and the semantic asymmetry between information-dense videos and sparse textual queries. To bridge this gap, we introduce \textbf{MAVIS}, a novel multi-agent framework that rethinks retrieval as cooperative reasoning rather than brute-force search. MAVIS first bridges the granularity mismatch by parsing raw videos into a \textbf{Structured Semantic Library}, enabling explicit attribute-level indexing. During retrieval, a planner decomposes complex user intents into atomic sub-tasks, dispatching specialized agents to independently nominate candidates. Crucially, MAVIS employs a \textbf{Logic-aware Debate} mechanism with a strict veto protocol, where agents collaboratively prune logical mismatches to identify a compact set of ``controversial'' candidates for fine-grained verification. This agentic workflow effectively bypasses the inefficiency of full-library traversal. Extensive experiments on MSR-VTT, MSVD, and ActivityNet demonstrate that MAVIS achieves competitive performance without task-specific fine-tuning, offering a scalable and interpretable alternative to traditional dual-encoder approaches.

---


### 488. [A Unifying Framework for Concept-Based Representational Similarity](https://arxiv.org/abs/2606.09653)

**<font color=#1a73e8>作者：</font>** Grégoire Dhimoïla, Victor Boutin, Agustin Martin Picard 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learned representations across models and modalities often exhibit striking structural similarities, suggesting shared underlying concept decompositions. However, concept alignment remains poorly defined: existing approaches optimize different objectives under the same terminology, obscuring what is actually aligned.
We propose a unifying framework that decomposes alignment along two axes: what is aligned (representations vs. concepts) and at what level (instance-wise vs. distributional). This induces four corresponding properties -- instance-wise and distributional variants of translation and concept consistency -- and reveals precisely which of these guarantees existing methods provide. We further introduce \InterVenchA, an intervention-based benchmark that separately measures extraction quality, translation quality, and concept consistency. Through theory and experiments, we show that commonly assumed equivalences between alignment objectives fail in practice: optimizing one property does not reliably recover the others, and purely unsupervised objectives fail to recover meaningful instance-level alignment. We then propose the Coupled Sparse Autoencoder (CoSAE), which jointly enforces complementary alignment objectives. Strong alignment emerges only in this regime. Surprisingly, as little as 0.1\% paired data is sufficient to recover instance-level alignment when anchoring distributional objectives.
Overall, our results show that concept alignment is fundamentally multi-objective: it must be defined, measured, and optimized as such.

---


### 489. [Beyond Accuracy: Community Perspectives on Machine Translation](https://arxiv.org/abs/2606.09655)

**<font color=#1a73e8>作者：</font>** Yujun Wang, Ehud Reiter, Shimei Pan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite remarkable progress in machine translation (MT), non-AI communities have raised growing concerns about MT systems, suggesting a noticeable gap between technical advancement and the needs of real-world users. For instance, while NLP researchers focus on benchmark performance, end users care about ethical concerns, trust, reliability, costs, and more. We argue that listening to various user communities is essential so that research efforts would be directed towards the problems that the communities care about. To this end, we present a large-scale analysis, for the first time, that investigates what four stakeholder communities (AI developers, professional translators, language learners, and language service providers) post about MT technology on social media. To do so, we construct a dataset of 79,286 posts and comments from Reddit, Facebook, Bluesky, and Mastodon from 2019 to 2025, and analyse where these communities disagree, and how and why. Overall, we find that communities often disagree, and even show strong conflicts due to polarised sentiments on topics such as translation quality, efficiency, and reliability. This is because these communities approach these topics differently: the AI community frames them as technical and computational problems, while non-AI (user) communities care more about quality nuances, time savings, user trust, and broader social issues.

---


### 490. [End-to-End Context Compression at Scale](https://arxiv.org/abs/2606.09659)

**<font color=#1a73e8>作者：</font>** Ang Li, Sean McLeish, Haozhe Chen 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context language model inference is bottlenecked by memory, as the KV cache grows with context length. Recent techniques to compress the KV cache fall short: they either degrade model quality substantially or require considerable time and compute to compress a single long prompt. Furthermore, many methods require the input to fit within the target model's context window, and are generally incompatible with modern production inference engines. Encoder-decoder compressors, which map a long token sequence to a shorter sequence of latent embeddings consumed by a decoder, are an appealing alternative in principle. However, existing approaches are not competitive with KV cache compression on the accuracy-efficiency frontier. In this work, we revisit encoder-decoder compression and close this gap. We first perform an architecture search, pre-training many variants from scratch to determine how best to design and train encoder-decoder compressors. Guided by our findings, we continually pre-train a family of 0.6B-encoder, 4B-decoder models on over 350B tokens each, at compression ratios of 1:4, 1:8, and 1:16. We introduce Latent Context Language Models (LCLMs), a family of compressors that improve the Pareto frontier across general-task performance, compression speed, and peak memory usage. We demonstrate that LCLMs serve as efficient backbones for long-horizon agents, letting the agent skim through a compressed long context and adaptively expand relevant segments on demand.

---


### 491. [When Built-in Thinking Helps and Hurts: Constraint-Level Error Shifts in Instruction Following](https://arxiv.org/abs/2606.09662)

**<font color=#1a73e8>作者：</font>** Sai Adith Senthil Kumar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large reasoning models (LRMs) often improve math and coding performance, but their effect on instruction following is unclear. We study IFEval with Qwen3 models (1.7B-32B), using same-weights Thinking ON/OFF controls; four Hunyuan models provide directional cross-family support. Aggregate pass-rate changes are small (-0.55 to -3.52 pp), yet 10-20% of prompts switch between pass and fail across modes, suggesting that thinking changes the pattern of errors--some prompts improve while others worsen--rather than uniformly degrading performance. Under a post-hoc Qwen3-derived grouping, constraint types separate into Planning (global counting, structure, coordination), which improves at the class level under thinking, and Precision (exact local form), which consistently worsens; the class-level Planning/Precision sign pattern holds directionally for all four Hunyuan models despite Hunyuan's opposite aggregate direction. Thinking also changes final-answer length; matched-length analyses substantially reduce the Precision drop, but a residual penalty remains. Analyzing thinking traces with a cross-encoder relevance metric reveals three patterns: Neutral shows a positive relevance-compliance link (r approximately 0.15); Planning shows near-zero predictive correlation (r approximately 0.02) despite measurable trace engagement, consistent with an execution gap between CE-measured trace relevance and final-answer compliance; Precision shows a small negative correlation (r approximately -0.05), with failing instances having higher mean relevance than passing ones. Activation patching across four model sizes (1.7B-14B) shows that Precision flip instances are more often restored than Planning flip instances (32-58% vs. 14-40% mean layer-restoration), with the largest gap at 14B (about 30 pp).

---


### 492. [From 0-to-1 to 1-to-N: Reproducible Engineering Evidence for MetaAI Recursive Self-Design](https://arxiv.org/abs/2606.09663)

**<font color=#1a73e8>作者：</font>** Dun Li, Jiatao Li, Hongzhi Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recursive self-design refers to AI-assisted modification of the mechanisms by which an AI system is built, evaluated, and improved. This paper treats MetaAI not as a mature paradigm, but as a working term for a human-seeded, AI-expanded development pattern in which the design space itself becomes a target of modification. We propose an operational evidence framework with four criteria: inspectable target system, meta-level modifier, feedback-directed selection, and recursive continuation. We then map public systems, including Darwin Goedel Machine (DGM), STOP, Goedel Agent, and ShinkaEvolve, against these criteria. DGM provides the most direct currently reported evidence: its published results show improvement from 20% to 50% on SWE-bench Verified and from 14.2% to 30.7% on full Polyglot after 80 iterations, with ablations suggesting that both open-ended exploration and self-improvement contribute. Finally, we provide MetaAI-Mini, a reproducible HumanEval-based protocol and codebase. Because no completed model run is included in this build, MetaAI-Mini is reported as a protocol rather than as an experimental result.

---


### 493. [Frequency-based Constrained Sampling for Interval Patterns](https://arxiv.org/abs/2606.09666)

**<font color=#1a73e8>作者：</font>** Djawad Bekkoucha, Abdelkader Ouali, Bruno Crémilleux  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Output space pattern sampling is a powerful alternative to exhaustive pattern mining for exploring large pattern spaces, as it enables users to focus on representative patterns drawn according to a chosen interestingness measure. In this paper, we address the problem of sampling interval patterns under user-defined syntactic constraints. We introduce CFips, a sampling approach that incorporates constraints directly into the sampling procedure. The approach relies on a multi-step sampling framework and supports several syntactic constraints by decomposing them into elementary predicates on interval bounds while preserving exact sampling guarantees. We formally prove that CFips samples interval patterns proportionally to their frequency within the constrained pattern space. The experimental results show that integrating constraints into the sampling procedure enables to complete mining tasks that would otherwise fail within a given time out.

---


### 494. [Algorithm for Contextual Queueing Bandits with Rate-Optimal Queue Length Regret](https://arxiv.org/abs/2606.09668)

**<font color=#1a73e8>作者：</font>** Seoungbin Bae, Dabeen Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contextual queueing bandits provide a framework for learning to schedule heterogeneous jobs under unknown context-dependent service rates. Under stochastic contexts, existing algorithms achieve $\widetilde{\mathcal{O}}(T^{-1/4})$ queue length regret, defined as the expected difference between the learner's and oracle's queue lengths at horizon $T$. In this paper, we improve this rate to $\widetilde{\mathcal{O}}(T^{-1/2})$. The key observation is that random exploration is needed only up to a carefully chosen cutoff round, rather than throughout the entire horizon. We propose CQB-$\eta$-2, a three-phase algorithm: (i) pure random exploration to construct an initial estimator, (ii) $\eta$-random exploration combined with a UCB rule to continue learning while maintaining negative drift, and (iii) pure UCB after the exploration cutoff. Our proof decomposes the queue length regret at the cutoff round. Before the cutoff, negative drift suppresses queue length differences caused by suboptimal choices. After the cutoff, the first two phases provide sufficient random exploration samples, ensuring that UCB decisions incur small departure-rate gaps. Combining these two bounds yields queue length regret of order $\widetilde{\mathcal{O}}(T^{-1/2})$. We further prove a minimax lower bound of order $\Omega(T^{-1/2})$. The proof constructs two hard instances that are statistically indistinguishable up to the final service decision, and uses a queue-specific coupling argument to convert the resulting testing error into queue length regret. Together, our upper and lower bounds characterize the minimax dependence on the horizon $T$ up to logarithmic factors.

---


### 495. [Visual Prompting Meets Feature Reconstruction-Based Anomaly Detection with Dual-Teacher Supervision](https://arxiv.org/abs/2606.09670)

**<font color=#1a73e8>作者：</font>** Mateo Diaz-Bone, Daniel Caraballo, Florian Scheidegger 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent Anomaly Detection methods achieve perfect detection and segmentation scores on well-established datasets, such as MVTec. However, many of these methods face challenges when foundational assumptions - such as consistent object scale, viewpoint, background, illumination, and centered placement - are violated. Those variations that occur render anomaly detection methods unusable in many real-world scenarios. To address these limitations, we introduce three key contributions: (1) a visual prompting pipeline that isolates objects using foreground-background masking; (2) a mechanism for unfreezing the teacher in student-teacher models to improve domain adaptability; and (3) a data augmentation strategy leveraging diffusion-generated synthetic images to enhance anomaly detection performance. We achieve a 3.5 percentage point improvement over the previous state-of-the-art on the challenging AeBAD dataset by using the Masked Multiscale Reconstruction (MMR) model as our backbone.

---


### 496. [Transition-Based Digital Twin Modelling for Alzheimer's Disease under Sparse Longitudinal Data](https://arxiv.org/abs/2606.09671)

**<font color=#1a73e8>作者：</font>** Yinyu Huang, Yilin Zhang, Sofia Michopoulou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Alzheimer's disease (AD) progression is highly heterogeneous and is typically observed through sparse and irregular longitudinal data, posing challenges for prediction and personalised monitoring. Existing machine learning approaches have improved AD prediction using multimodal data, yet often focus on static classification or cohort-level risk estimation, providing limited support for subject-specific modelling and uncertainty-aware reasoning. To address these limitations, we present a personalised digital twin framework for AD prediction and scenario-based analysis using multimodal longitudinal data. The proposed approach integrates complementary modelling strategies to capture clinical transitions and temporal dependencies across visits. Using data from the Alzheimer's Disease Neuroimaging Initiative (ADNI), including cognitive assessments, clinical variables, and MRI-derived phenotypes, the framework predicts cognitive status and diagnostic categories while quantifying predictive uncertainty and enabling patient-specific what-if trajectory analysis. Evaluation on leak-free subject-level splits demonstrates strong performance in score forecasting and diagnosis classification. In this sparse and irregular ADNI setting, transition-based modelling of adjacent visits achieved higher predictive accuracy than the sequence-based branch, suggesting that local transition modelling may be more data-efficient. While sequence models remain valuable for uncertainty-aware trajectory forecasting, local transition modelling offers a more data-efficient and robust predictive strategy. These findings highlight the importance of aligning temporal modelling strategies with clinical data structure and suggest that transition-based digital twin formulations may provide a practical and interpretable approach for personalised disease forecasting in neurodegenerative disorders.

---


### 497. [Correlation Is Not Enough: Embedding Human Metadata for Individual Causal Discovery](https://arxiv.org/abs/2606.09672)

**<font color=#1a73e8>作者：</font>** Suraj Biswas, Saurabh Gupta, Pritam Mukherjee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ask a pretrained biomedical language model whether "cortisol 28 ug/dL" and "stock-market volatility" are related, and it returns a cosine similarity of 0.83 on a scale where 1.0 means identical. The two share no mechanism. This is not a corner case: every off-the-shelf biomedical encoder we tested (BioBERT, PubMedBERT, BioM-ELECTRA) scores unrelated cross-domain pairs between 0.76 and 0.92 when the answer should be near zero. Accuracy on cross-domain discrimination is 0%.
Retrieval systems survive this, because a language model downstream filters the noise. A Large Behavioural Model (LBM), a foundation model whose subject is a person rather than a sentence, does not: it reasons over a graph of a user's life and treats embedding proximity as evidence that two events are causally linked. False proximity writes a false causal edge, and everything downstream inherits the error. Here, embedding geometry is not a tuning knob; it is correctness.
We report the fix. A contrastive pass over 72,034 pairs raises PubMedBERT BIOSSES correlation from 0.633 to 0.828 and within-vs-across-domain separation from 1.05x to 1.63x. A second pass, BODHI, mines hard negatives from edges absent in a biomedical knowledge graph and lifts separation to 2.30x and the discrimination gap to +0.392, at a 4.5% BIOSSES cost. On an Intel Xeon 6737P with AMX, OpenVINO cuts single-query latency from 1367 ms to 10 ms (133x) and reaches 555 sentences/sec. One finding contradicts standard advice: FP16 beats INT8 on this silicon at every serving batch size, and we explain why. The same model on a no-AMX Ice Lake instance runs 13-27x slower. We release the benchmark suite, training corpora, the BODHI generator, and the OpenVINO scripts.

---


### 498. [(Auto)formalization is supposed to be easy: Trellis process semantics for spelling out rigorous proofs](https://arxiv.org/abs/2606.09674)

**<font color=#1a73e8>作者：</font>** Wesley Pegden  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present Trellis: an autoformalization system that leverages LLM agents in a deterministically constrained workflow to enforce incremental progress in Lean autoformalization tasks through iterative refinement of natural language proofs. Our approach is motivated by the common mathematician's notion of what it means to have a rigorous proof in the first place: namely, that it would be routine to elaborate any part of the proof in further detail. The result is a system which aims to achieve reliable autoformalization on a modest budget and with generalist agents, with specialization to autoformalization coming not from any task-specific agent training but instead from a meaning-of-rigor inspired workflow enforced by process semantics. We link to an end-to-end Lean formalization of a recent Ramsey theory breakthrough produced by the process.

---


### 499. [SoccerNet 2026 Player-Centric Ball-Action Spotting:Retraining and Post-Processing Extensions to the FOOTPASS Baselines](https://arxiv.org/abs/2606.09679)

**<font color=#1a73e8>作者：</font>** Parthsarthi Rawat  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We describe our system for the SoccerNet 2026 Player-Centric Ball-Action Spotting Challenge, which requires predicting who performs which action and when, across eight classes in broadcast soccer. Building on the three FOOTPASS baselines [1] (TAAD, TAAD+GNN, and TAAD+DST), we contribute four extensions: (1) gradient check pointing to enable full-backbone fine-tuning on a single GPU; (2) fusion of GNN logits into the DST encoder, combining graph-based tactical context with per-player visual features; (3) square-root frequency class weighting to address the 213:1 pass-to-tackle imbalance in the training data; and (4) a post processing pipeline comprising per-class logit gating, temporal frame refinement, jersey re-assignment, and a two-model ensemble. Our system achieves 0.548 Macro F1 on the test set and 0.446 on the challenge set (server evaluation).

---


### 500. [GenEyePose: Patient-Free, Knowledge-Based Saccadic Eye Movement Modeling for Digital Neurophysiologic Biomarker Development](https://arxiv.org/abs/2606.09681)

**<font color=#1a73e8>作者：</font>** Tianyu Lin, Jooyoung Ryu, Puvada Sreevarsha 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Eye movements, including saccades, are widely regarded as highly sensitive and objective biomarkers of neurophysiologic states. Detecting saccadic signatures in neurologic diseases offers a rapid, portable alternative to brain imaging, avoiding access and cost barriers. Currently, there are no robust AI-enabled video-oculographic solutions (e.g., digital biomarkers) for screening, triaging, or localizing brain abnormalities due to privacy issues and scarce datasets. In this work, we propose the first fully synthetic, patient-free, multimodal eye movement generation pipeline for generalizable saccade analysis. Using this synthetic dataset, we trained a deep learning classifier to distinguish between normal and abnormal (hypometria and hypermetria) saccadic accuracies and evaluated its performance on real-world clinical data. The model achieved an AUROC of 0.76 and a sensitivity of 0.71, showing that the synthetic data has strong potential to generalize for clinical applications, including as a screening tool in at-home and emergency room settings or a tool for precise neuroanatomic localization.

---


> [!TIP]
> 当前位于：**451-500**（第 10/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-527](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
