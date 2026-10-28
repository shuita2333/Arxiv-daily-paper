# 📦 其他研究 | 2026年10月29日

> 本类共 **257** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-257](./part-06.md)

---

### 51. [A Smart Instant Book Filter Model based on Dual-Objective Optimization](https://arxiv.org/abs/2610.36287)

**<font color=#1a73e8>作者：</font>** Yi Hou, Li Fan, Huizhong Duan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hospitality service in online marketplaces has become increasingly popular over the past few years, not only because it helps people easily rent short-term lodging but also because it empowers travelers to connect with locals and feel belonging. A typical pattern of these industries is a central platform mediating the economic interactions between guests and hosts, where a successful booking experience is the key to user satisfaction. However, one of the biggest challenges is the possible delay of response and chance of rejection when guests try to book a request-to-book listing. Previously, we enabled the instant book feature to allow hosts to instantly accept qualified guests and guests to confirm bookings immediately. Yet the symptom has not been alleviated given mixed request-to-book and instant book listing supply in search results. One possible solution is to promote all instant book listings in search results; however, booking rate will be damaged due to some improperly promoted low quality listings.
In this paper, we present a novel smart instant book filter system that applies the instant book filter intelligently and shifts request-to-book to instant book without hurting booking rate. Compared with traditional two-sided markets research that targets finding strategies to maximize a single overall social welfare goal, our proposed system aims to maximize the instant book rate with the constraint that booking rate should not decrease, forming a dual-objective optimization problem.
We show A/B testing results for our system exposed to global users, demonstrating that our model performs better than previous human-expert-tuned models in terms of both instant book rate and overall booking rate. We also achieved improved metrics such as the host instant book adoption rate. The proposed system has been deployed to production and is serving millions of users every day.

---


### 52. [Compatibility and future-proof testing for multi-agent systems](https://arxiv.org/abs/2610.36289)

**<font color=#1a73e8>作者：</font>** Yueshan Li, Lorenzo Fiaschi, Andrea Censi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Independently developed autonomous agents, such as autonomous vehicles, must guarantee joint compatibility, such as safety and task-completion requirements, when they operate in a shared environment. Existing methods require a centrally designed specification, or interaction mechanism before any agent is deployed. However, such centralized design is unrealistic when agent designs are confidential to their developers, and it is not flexible enough to accommodate future agent designs. We study a bi-level structure in which a regulator coordinates developers by publishing seed agents, and each developer independently tests its agent to ensure that it is compatible with every seed-compatible agent, a property we call future-proofness. Under this structure, joint compatibility is guaranteed for any agents that are designed and tested independently, without any coordination with each other. In this work, we first formulate compatibility for general multi-agent systems and show why it is not trivially implied by seed-compatibility. We then characterize the future-proof agents as the closure of the seed and show that this closure is monotone in the seed. Finally, we study a class of executable tests that involve interaction with the seed alone, and we ask to what extent such tests can distinguish the future-proof agents.

---


### 53. [Spiking Neural Networks Are Harder to Steal: A Benchmark Study of Model Stealing Attacks](https://arxiv.org/abs/2610.36298)

**<font color=#1a73e8>作者：</font>** Ayana Moshruba, Maryam Parsa  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Machine learning models deployed behind query interfaces expose more than their predictions, because an adversary can use those predictions to rebuild the model itself. Model stealing attacks (MSAs) exploit this exposure by training a surrogate model that replicates the decision behavior of a target through black-box queries alone, without access to its parameters or training data. These attacks are well characterized for conventional artificial neural networks (ANNs), yet spiking neural networks (SNNs) process information in a fundamentally different way. SNNs communicate through sparse, discrete spikes, and their outputs depend on membrane potentials that evolve over time rather than on a static mapping from input to output. This temporal mode of computation suggests that the decision behavior of an SNN may be harder to reconstruct from its responses. This work tests that possibility by benchmarking four representative MSAs, namely the Papernot, Tramèr, T-RND, and color perturbation attacks, against SNNs and their ANN counterparts on MNIST, Fashion-MNIST, and CIFAR-10. Across every attack and dataset, SNNs prove consistently more difficult to steal. Surrogates of SNNs achieve 10% to 20% lower agreement with the target model and 15% to 25% lower adversarial transferability than surrogates of ANNs. We attribute this resistance to the way SNNs compute, as their spike-based and time-dependent dynamics yield decision boundaries that ANN-based surrogates struggle to approximate, even under large query budgets. These findings extend the known resilience of SNNs beyond attacks on training data to the replication of model functionality, strengthening the case for neuromorphic architectures in security-sensitive applications.

---


### 54. [Bridging Exploration and Loss of Plasticity in On-Policy Reinforcement Learning](https://arxiv.org/abs/2610.36309)

**<font color=#1a73e8>作者：</font>** Andrea Vasco Grieco, Evelyn D'Elia, Edoardo Caldarelli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep reinforcement learning (RL) algorithms have been observed to lose the ability to adaptively learn from new data, a phenomenon termed Loss of Plasticity (LoP). While many metrics have been shown to correlate with it, the causal mechanisms and the geometric conditions from which it can arise have not been clearly identified. We analyze LoP in Proximal Policy Optimization with isotropic Gaussian policies, the state-of-the-art formulation for many continuous action spaces in RL. We report multiple metrics which characterize the effect that the policy standard deviation $\sigma$ has on LoP, and we also suggest related explanations for the effectiveness of widely adopted LoP mitigation techniques. We observe a significant effect of $\sigma$ on the extent of LoP, and accompany this with both theoretical and experimental supporting arguments. Our experimental validation consists of LoP benchmark evaluations against standard baselines as well as real-world policy deployment on a 7-DoF robotic arm.

---


### 55. [Confidence Is Not a Promise: A Reference Audit of Typed Decision Models](https://arxiv.org/abs/2610.36311)

**<font color=#1a73e8>作者：</font>** Pedro Carvalho Brom  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Typed decision models return a probability distribution over options supplied by the caller, and software tends to act on that number as if it were a guarantee. We measure what it licenses, comparing the open-weight Laya, in five checkpoints, with Jev 1.13, available only through an API. A probability licenses a statement about groups of decisions, not about one decision, and a gate that promises an accuracy among the cases it decides alone keeps that promise only with a lower bound checked on data like its traffic. Across 190 exchangeable evaluations, a threshold chosen by point estimate breaks the promise in 147, Learn then Test keeps it in all of them, and a Beta lower-bound rule decides more items on average than Learn then Test in 128 and fewer in none, without its guarantee. Calibrated in English, Jev keeps a promise of 95% in 8 of 51 locales. Ordinary typing noise breaks a promise calibrated on clean text, and, in exploratory runs, training with noise raises the noisy accuracy with no loss on clean text. In four further domains, a fine-tuned Laya needs from 250 to 8,000 labels to be non-inferior to Jev, and does not get there on LIAR2. Under drift, the preregistered claim for a Bayesian retraining loop is not supported: the loop avoids needless retraining where the change does not degrade the model, at a cost equivalent to recalibration alone, and re-qualifying the threshold in every window keeps the promise more often where it does. On the monthly series of M3, neither decider predicts the direction of the next value better than a constant answer. Confidence separates right from wrong answers with an AUROC from 0.80 to 0.96, but it does not select faithful explanations, and exact coalition games of single decisions show what an explanation can still say through an API that rounds to two decimals. We release the frozen answers with a datasheet, a promise check and the code.

---


### 56. [AHEAD: Adaptive Neural Acceleration for Large-Scale Linear Programming](https://arxiv.org/abs/2610.36321)

**<font color=#1a73e8>作者：</font>** Sihao Liu, Zhichao Hou, Huayue Gu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale linear programs with millions of variables and constraints strain time and memory budgets. First-order methods such as the primal-dual hybrid gradient scale to this regime because they avoid matrix factorizations, but they require many iterations. Learned accelerators can reduce these iterations, yet fewer iterations do not guarantee a shorter solve. Learning inference also takes time, and running the accelerator longer trades solver time for inference time. Existing unrolled accelerators handle this trade-off poorly: each layer processes every variable and constraint, the predicted iterates still need solver refinement, and every instance runs the same layers. We therefore ask: What neural accelerator design achieves end-to-end speedups on large-scale linear programs across sizes and target accuracies? We introduce AHEAD, an accelerator that predicts step sizes for first-order linear programming solvers while keeping their update rules. Its weight-shared predictor reads compact solver statistics and rescales the primal and dual step sizes, so each warm-start iteration stays inexpensive and a short warm-start phase hands the solver a warm start. A learned handoff policy sets the number of warm-start iterations for each instance and target accuracy, after which the solver finishes under its own termination criterion. On packing linear programs with up to $10^7$ variables, AHEAD achieves $6.5$--$11.6\times$ end-to-end speedups over Gurobi's first-order solver from a cold start, including on instances of unseen sizes and distributions. The gains extend to PageRank linear programs and hold across difficulty levels and target accuracies.

---


### 57. [Plenty of Room in the Middle: Revealing Opportunities on a GPU Cluster via Fine-Grained Monitoring](https://arxiv.org/abs/2610.36329)

**<font color=#1a73e8>作者：</font>** Andrew Sheinberg, Samyak Gupta, Kai Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> GPU clusters have become essential computing resources for AI and scientific research in academia and industry. However, their high cost and growing demand often result in long queueing delays. While previous monitoring efforts have operated at second- or minute-level frequencies, they primarily informed job-level scheduling for clusters and lacked the detail needed to optimize GPU-level utilization.
This paper presents an in-depth study of a university research GPU cluster, analyzing resource usage at 100 ms intervals. We have developed a lightweight monitoring tool that leverages Nvidia's DCGM library to capture fine-grained "compute utilization" metrics within GPUs. Deployed on a cluster with 89 nodes and 319 GPUs, our tool collected data over several months. This paper focuses on a 10-day period with 7,399 jobs submitted by 150 users from 12 departments. Our study reveals three key findings: (1) the GPU cluster exhibits significant underutilization, with over 70% of jobs using less than 20% of GPU memory and 50% averaging below 5% Streaming Multiprocessor (SM) utilization; (2) 80% of jobs have a drastic mismatch between their requested and actual durations, significantly limiting the scheduler's effectiveness; and (3) the multi-GPU jobs we examined show highly periodic communication patterns. These findings suggest there is plenty of room in the middle: substantial utilization gains are available through better job scheduling and GPU multitasking, independent of hardware or application improvements.
Our monitoring solution is available as open-source software at this https URL.

---


### 58. [PHP2Shell and the Future of AI-Discovered Vulnerability Disclosure: Evidence, Verification, and Human Authority](https://arxiv.org/abs/2610.36334)

**<font color=#1a73e8>作者：</font>** Toqeer Ali Syed, Asadullah Abdullah Khan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI-assisted vulnerability discovery can produce technically plausible findings faster than maintainers can validate, coordinate, and safely disclose them. The resulting challenge is not only to establish whether a vulnerability claim is credible, but also to ensure that its supporting evidence, human authorization, intended recipients, and applicable policy remain bound to the same case revision. We present FedTrust-CVDv2, a federated coordinated vulnerability disclosure framework that separates evidence validation, interorganizational coordination, human governance, and permissioned auditing. The framework binds independently signed observations to exact evidence revisions and scopes external actions to approved payloads, audiences, expiry, policy, and revocation state while preserving existing CVE Numbering Authority (CNA) roles. A local reference implementation accepted all 25 valid fixtures and rejected all 650 invalid fixtures across 27 constructed policy families; six single-safeguard ablations admitted 25-75 invalid fixtures. Supporting experiments exercised signed messaging, authenticated encryption, audit certificates, and finite quorum-set conditions. A PHP2Shell case formulation illustrates how runtime evidence, patch state, emergency coordination, and CNA authority can be represented without attributing unsupported claims to AI or treating audit integrity as vulnerability truth. This short version focuses on the architecture, evidence-to-action contract, selected conformance results, and case formulation. An expanded version containing the full implementation, extended experiments, operational analysis, and additional results will be submitted to a journal.

---


### 59. [CRLoMTL: Conflict-Resolution through Low-rank matrices for Multi-Task Learning](https://arxiv.org/abs/2610.36337)

**<font color=#1a73e8>作者：</font>** Ahmed Agiza, Tasneem Shaffee, Rahil Badkul 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-task learning (MTL) improves model efficiency by sharing representations across related vision tasks, but it often suffers from negative transfer when task updates interfere with one another. Existing conflict-mitigation methods typically operate in gradient space, requiring explicit task-gradient manipulation and additional optimization steps. We propose Conflict-Resolution through Low-Rank Matrices for Multi-Task Learning (CRLoMTL), a parameter-efficient framework that mitigates task interference in the low-rank parameter-update space. CRLoMTL learns task-specific LoRA updates through task-specific passes, where each task updates its own low-rank matrices, and integrates these updates through global shared-subspace fusion. Specifically, we introduce a shared-subspace resolver based on singular value decomposition (SVD), referred to as the SVD resolver, which extracts a common low-dimensional orthonormal basis across task adapters and projects task updates into this shared space before merging them into a single deployment-time update. The resulting update can be folded into the backbone, preserving the inference structure of the original model without additional runtime branches. Experiments with Swin Transformer backbones on PASCAL-Context, NYUD-v2, and CelebA show that CRLoMTL achieves a favorable accuracy-parameter trade-off, improving over single-task baselines by up to 2.77% on PASCAL-Context, 5.03% on NYUD-v2, and 3.50% on CelebA, while training only a small fraction of the parameters used by single-task models.

---


### 60. [CrowdCC: Jointly Benchmarking Corruption Robustness and Deployment Quantization in Crowd Counting](https://arxiv.org/abs/2610.36340)

**<font color=#1a73e8>作者：</font>** S Mahmudul Hasan, Lu Peng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Crowd-counting models deployed on edge devices face two shifts: inputs are degraded along the capture and transmission pipeline, while models are quantized to satisfy resource constraints. Yet corruption robustness and deployment quantization are typically evaluated separately. We introduce CrowdCC, a controlled corruption benchmark that jointly evaluates these effects using 23 deployment-motivated corruptions at three severity levels, four crowd-counting datasets, and 26 models using A100 TensorRT engines at FP32, FP16, and post-training INT8 precision, paired with throughput and energy measurements from corresponding Jetson Orin NX configurations. The corruptions span six families, with head annotations adjusted when geometry or visibility changes. Our evaluation shows that capture-chain corruptions consistently produce the largest degradation across the evaluated models, while crowd density affects absolute and relative error differently. Clean accuracy does not fully predict corrupted performance. INT8 alters corruption robustness substantially more than FP16, with no systematic direction, and does not consistently improve latency or energy. INT8 inference efficiency is strongly associated with reformat overhead in the compiled engine, while slowdowns are also observed under limited INT8 coverage. Precision changes corrupted-error rankings and robustness-cost frontiers, showing why model selection must consider corruption robustness and measured deployment cost together. The code is available at this https URL.

---


### 61. [AK_QMUL at ArGuard Shared Tasks: A Single Fine-Tuned JAIS for Arabic Harmful-Prompt Detection](https://arxiv.org/abs/2610.36360)

**<font color=#1a73e8>作者：</font>** Ali Khairallah, Arkaitz Zubiaga  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present AK_QMUL's submissions to the ArGuard-2026 shared tasks on Arabic harmful-prompt detection: a binary safe/unsafe task (B1) and a seven-way harm-domain task (B2). Both submissions use one backbone -- JAIS-6.7B fine-tuned with 4-bit QLoRA and a linear classification head over its last-token representation. For B1 we train a four-way head that factors the label by dialect register {safe, unsafe} x {MSA, other}, we augment the training fold with MSA prompts from AraSafe, and decode with a plain argmax to score safe/unsafe. For B2 we fine-tune the same backbone as a seven-way classifier and average the softmax outputs of five random seeds. Both submissions ranked first on their track, with macro-F1 0.984 on B1 and 0.790 on B2. We report results by dialect and by class: on B1 the model is accurate across all six dialects (93.6--99.8%) and its predicted unsafe rate tracks the true rate closely; on B2 six of the seven classes reach F1 between 0.73 and 0.98, with the residual error concentrated in the Bully class, which overlaps semantically with harassment and harm-to-others.

---


### 62. [Reliability-Aware Short-Term Glycemic Risk Prediction Using an Anchor-Based Comparative Framework of Sequence, Multimodal, and State-Updating Digital-Twin Models](https://arxiv.org/abs/2610.36363)

**<font color=#1a73e8>作者：</font>** Pir Bakhsh Khokhar, Carmine Gravino, Fabio Palomba  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Anticipating short-term hypoglycemic and hyperglycemic risk is essential for proactive diabetes management. However, existing machine learning approaches often use inconsistent evaluation protocols and emphasize predictive performance over reliability. This study introduces an anchor-based benchmarking framework integrating longitudinal glucose sequences and multimodal patient information. Using the T1DiabetesGranada dataset, 5,503,441 standardized prediction anchors were constructed from 736 individuals with type 1 diabetes to evaluate hypoglycemia and hyperglycemia prediction at 30-, 60-, and 120-minute horizons. Three neural architectures, a Hybrid LSTM-Transformer, a Multimodal Digital Twin, and a State-Updating Digital Twin with gap-aware longitudinal state progression, were compared under identical patient-level validation protocols. Beyond predictive performance, the evaluation examined calibration, classification thresholds, explanation reliability, cross-model disagreement, and robustness to controlled perturbations. No statistically significant predictive differences were observed after Holm correction, although the models exhibited complementary reliability characteristics. The Multimodal Digital Twin achieved the lowest mean Brier score, while the State-Updating Digital Twin demonstrated the lowest mean expected calibration error (ECE-10). The Hybrid LSTM-Transformer showed strong explanation faithfulness and stability under its temporal attribution protocol. These findings highlight the importance of evaluating digital-twin models beyond predictive accuracy and emphasize the need for reliability assessment and external validation before clinical deployment.

---


### 63. [LoRA on a Budget: Function-Aware Post-Hoc Compression for Adapter Fleets](https://arxiv.org/abs/2610.36386)

**<font color=#1a73e8>作者：</font>** Shenghui Li, Thiemo voigt  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Low-Rank Adaptation (LoRA) has become a key mechanism for efficiently specializing foundation models into many task- and user-specific variants. Serving many LoRA adapters under a shared resource budget turns post-hoc compression into a two-level allocation problem: rank must be distributed across layers within each adapter and across adapters within the fleet. Although trained LoRAs contain substantial spectral redundancy, spectral reconstruction alone does not determine how much compression an adapter can functionally tolerate. We formulate fleet compression through a functional rank-distortion frontier for each adapter, followed by fleet-level minimax allocation under a shared rank budget. Given exact frontiers, this decomposition is equivalent to joint optimization over all layer ranks. We introduce Functional Rank Allocation (FRA), an unlabeled method for constructing practical frontiers. FRA measures isolated module truncations end to end, uses these measurements as an additive search surrogate solved by dynamic programming, remeasures every complete candidate, and takes the lower-risk envelope with a complementary spectral proposal before exact minimax allocation over the constructed frontiers. Across 78 adapters from three public fleets, FRA improves worst-case and tail utility over uniform spectral compression in constrained-budget regimes. Fixed-budget probes show that isolated costs rank candidates well, but their calibration shifts across proposal shapes; end-to-end verification and the spectral proposal therefore limit functional-search error.

---


### 64. [When Can a Learned Design Surrogate Be Trusted in a Self-Driving Microfluidics Laboratory? An Offline Closed-Loop Framework Built and Tested on Six Public Tables](https://arxiv.org/abs/2610.36395)

**<font color=#1a73e8>作者：</font>** Zhiyuan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-driving laboratories couple a learned design surrogate to an instrument, and on every new target domain it must answer four questions: when it can be trusted, how many target measurements it needs, which to make first, and when to stop adapting, switch models or escalate. We state a framework making each measurable (a competence ratio, a budget $k^*(\varepsilon)$, a time-to-target and a priced decision) and instantiate it without wet experiments on six public droplet-microfluidic and liposome tables as offline laboratories: 107 leave-one-group tiers whose rows are hidden labels. A sealed, pre-registered programme (two sealed negative validations and a pre-registered test on three more tables) and seven frozen closed-loop protocols, each run twice, yield 23 findings. Shift cost is stratified by shift type; no label-free statistic certifies individual candidates; random-split model-family rankings predicted neither the sealed nor the loop rankings. Warm-start residual boosting returns a surrogate to $1.25\times$ its development reference within 20 target rows in 94% of chemistry tiers (27% under a strict noise-floor reading), 90% of laboratory and 40% of device tiers, and a budget planned from the shift type on other tables is not measurably worse on a new one. In the loop, one gain survives drift and shuffled-label controls on all tiers, carried by the sparsely sampled ones: proposing at once and warm-starting on every measurement reaches a 10% target in 2.80 measurements against 3.31 for the reference, and in 5.72 against 11.35 for random proposals on 301 hard units at a 3% tolerance. No label-free acquisition rule survives the shuffled-label control, no interval-aware proposal or other model family does better, and no threshold rule on the tested diagnostics beats always continuing once escalation is priced. No wet-lab validation is claimed.

---


### 65. [ORBITAL: Optimization of Robust Brain--Computer Inference Through Architecture-Aware Low-Precision Compression](https://arxiv.org/abs/2610.36411)

**<font color=#1a73e8>作者：</font>** Saim Rehman, Muhammad Shafique  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Compact electroencephalography (EEG) decoders enable embedded brain--computer interfaces (BCIs), but compression can alter adversarial robustness without proportional hardware savings. We present ORBITAL, a robustness-constrained framework combining hardware-realizable structured compression, recovery-aware operating-point selection, multi-attack evaluation, and native edge validation. Across nine subjects and three seeds on BCI Competition IV-2a, S25-TRADES achieves the highest observed mean true-union robustness among compressed EEGNet models (23.06% vs 21.27% for standard Full), with 26.27% fewer parameters and 25.10% fewer MACs. Matched controls identify TRADES as the main source of robustness recovery, improving S25 union accuracy by 6.74 percentage points over clean recovery (p=0.0039), while per-example analysis reveals boundary redistribution rather than uniform margin expansion. On Jetson Orin Nano, FP16 compression reduces board energy by up to 16.20% and latency by 8.00%. Despite 99.3% prediction agreement, native INT8 Q/DQ incurs about twice the FP16 latency and energy, demonstrating the need for joint robustness and hardware-aware optimization.

---


### 66. [Persistence, Exposure, and Credit Routing in Linear Temporal Predictive Coding](https://arxiv.org/abs/2610.36412)

**<font color=#1a73e8>作者：</font>** Akira Tanase, Julian Gould, Jeffrey Seely  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temporal Predictive Coding (tPC) networks offer a layer-local alternative to backpropagation. For linear tPC, we show, by applying tools from cellular sheaf theory, that temporal credit assignment is a tug-of-war between spatial displacement and temporal errors, whose ratios are modulated by persistence and exposure operators $P$ and $Q$. Spatial inference therefore gives us the effective recurrent transition $F=PA$, whilst future credit is filtered by $P^\ast$. This creates a persistence--error tradeoff in spatial modes: under non-amplifying invariant recurrence, modes that preserve influence over long delays simultaneously fail to expose that influence strongly as temporal error. Recurrence can circumvent this via routing between persistent and exposed modes.

---


### 67. [SpeeDiff: Scalable Pixel-Anchored End-to-End Latent Diffusion Model](https://arxiv.org/abs/2610.36419)

**<font color=#1a73e8>作者：</font>** Bingliang Zhang, Wenda Chu, Yizhuo Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Scalable Pixel-anchored End-to-end Diffusion (SpeeDiff), a latent diffusion method that jointly trains the VAE and the diffusion model from scratch. In principle, joint training allows the diffusion loss gradient to directly guide the VAE encoder, encouraging the formation of a generation-friendly latent space and potentially yielding faster convergence than the conventional two-stage approach with a pretrained frozen VAE. However, a naive end-to-end implementation severely degrades performance, as unrestricted backpropagation of the diffusion loss leads to latent space collapse. Our main technical contribution is a simple yet effective Tweedie Pixel Reconstruction (TPR) loss, which provides additional pixel-level feedback by decoding a predicted clean latent from an intermediate noisy state using Tweedie's formula, thereby alleviating collapse. Furthermore, our method enables jointly scaling a fully transformer-based architecture and enhances representation alignment within the end-to-end framework. Our SpeeDiff-XL model achieves over 140x and 61x faster training compared to Vanilla SiT and REPA, respectively, while attaining an FID of 1.50 without guidance on ImageNet 256x256 generation. With a more efficient 32x compressed VAE, our model further reaches an FID of 1.53 without guidance on ImageNet 512x512 generation.

---


### 68. [Property-Based Testing for Robust Softmax and Cross-Entropy](https://arxiv.org/abs/2610.36427)

**<font color=#1a73e8>作者：</font>** Muhammad Maaz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A recent paper of Barron et. al. (2026) identified two numerical issues with the softmax and cross-entropy functions in virtually all standard machine learning libraries (e.g., PyTorch and JAX). We show that these issues can be recovered through simple property-based tests in Hypothesis. However, our tests identify an additional edge case where their implementation fails. We then propose an even more robust softmax implementation which passes these tests and also supports use in causal attention masking. We compare our implementation with theirs and discuss some of the differences. Overall, this work shows that property-based testing can be a powerful tool for discovering and fixing numerical issues in machine learning libraries. Our implementations and property-based tests can be found at this https URL.

---


### 69. [FORESEE-MS: Toward Prospective Spatial Forecasting of Future Multiple Sclerosis Lesions from Baseline FLAIR MRI](https://arxiv.org/abs/2610.36428)

**<font color=#1a73e8>作者：</font>** Maryam Akhavan Aghdam, Sudip Mittal, Noorbakhsh Amiri Golilarz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traditional multiple sclerosis (MS) image analysis has primarily focused on retrospectively detecting and segmenting lesions. This study investigates whether baseline FLAIR MRI can identify regions at risk for future lesion formation beyond population-level spatial patterns. We introduce FORESEE-MS, an evaluation protocol that uses a fold-specific population-prior atlas as a baseline and assesses predictions using pooled voxel-level discrimination (AUROC and AUPRC) and within-patient lesion localization (Recall@Top-K%), with patient-level bootstrap confidence intervals. We evaluated five deep learning models (3D U-Net, Attn+ResBlock+VAE, ViT, and two SwinUNETR variants) using 5-fold cross-validation on 39 subjects from the MSSEG-2 dataset. The atlas achieved the highest pooled voxel-level AUROC and AUPRC, with no deep learning model reliably outperforming it on either metric. However, the 3D U-Net and Attn+ResBlock+VAE achieved higher mean voxel-level within-patient Recall@Top-K% than the atlas at all evaluated thresholds, although most paired confidence intervals for the differences included zero. These findings suggest that baseline FLAIR may contain patient-specific predictive information, but in this small cohort, it remains uncertain whether this information improves lesion forecasting beyond a population-prior atlas.

---


### 70. [Simulated petrological labels enable probabilistic mineralogy prediction from whole-rock geochemistry](https://arxiv.org/abs/2610.36429)

**<font color=#1a73e8>作者：</font>** Matthew J. Liu, Aaron D. Kaplan, Michael L. Whittaker 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modal mineralogy, the mineral identities and abundances in rocks, guides geological studies and industrial resource extraction. While measuring modal mineralogy is time-intensive, whole-rock chemical measurements furnish elemental concentrations at higher throughput. Predicting mineralogy from elemental data, however, poses a one-to-many inverse problem, and labeled mineralogical datasets are too sparse to train on at scale. We address both challenges by simulating petrological labels that express multiple formation conditions per composition and at a scale unattainable by measurements. Nearly one million simulated labels supervise the middle component of a three-part model: a transformer encoder self-supervised on roughly 788,000 whole-rock compositions, the simulation-trained heads that predict distributions over mineral assemblages, and a recalibration layer that aligns the predictions with measured mineralogy. Zero-shot on 640 volcanic rocks, the model discriminates the presence of most mineral categories and predicts which rocks are richer in each mineral. However, the predicted abundances are systematically offset from measured values. Recalibration fit on as few as 25 labeled rocks recovers 76 percent of the likelihood improvement from fitting on the full 368-rock fitting set, while abundance error responds more slowly (11.0% zero-shot and 9.5% with the full fitting set). This work demonstrates how a machine learning model in the geochemical sciences can both leverage an imperfect simulator and mitigate its systematic biases.

---


### 71. [No Tokenizer, Still a Gap: Cross-Lingual Fairness of Homoglyph and Invisible-Character Watermarking](https://arxiv.org/abs/2610.36432)

**<font color=#1a73e8>作者：</font>** Alexander Nemecek, Yuqiao Xu, Joseph Falkenburg 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Homoglyph and invisible-character watermarks are edit-based watermarks. Instead of changing how a model generates text, they hide a signal in the text after it is written. They swap some characters for homoglyphs, which look the same, or very similar, but have different Unicode code points, or they insert characters that do not display, all without access to the model that wrote the text. Generation-time watermarks work less well for lower-resourced languages due to how tokenizers split their text. Because they work on individual characters, these watermarks never touch a tokenizer, so we ask whether they escape this gap. Across 40 language varieties in 24 scripts, we measure capacity (the hidden bits each character can carry), how much of it survives routine handling and targeted removal, and how much text a keyed detector needs. Capacity varies 3.3-fold and script accounts for 96\% of that variation. Within Latin script, resource level makes no detectable difference ($\rho=+0.095$, $p=0.78$), but across scripts capacity rises with it ($\rho=+0.54$, 95\% CI $[+0.14,+0.83]$), because lower-resourced languages tend to use scripts with few homoglyphs. Ordinary copy-paste, which strips invisible characters, widens the gap: a detector then needs about 2 code points of English or Persian but 93 of Lao. Removing the tokenizer does not remove the inequity, but instead only changes its source.

---


### 72. [Learning atomic interactions for the thermodynamics of liquid mixtures](https://arxiv.org/abs/2610.36440)

**<font color=#1a73e8>作者：</font>** Marco Hoffmann, Sebastian Schmitt, Hans Hasse 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive models for activity coefficients, which describe the non-ideality of liquid mixtures, are foundational for process design and optimization. Group-contribution methods, such as UNIFAC, are computationally cheap and well established in process simulators. Modern machine learning models, such as HANNA, offer higher accuracy and broader applicability, but their integration into process simulation is expensive or even infeasible. In this work, we introduce COGNAC, a graph neural network that learns atom-level geometry and interaction parameters that depend on the molecular neighborhood and evaluates them in the UNIFAC framework. Trained on about 820,000 experimental data points, COGNAC achieves significantly higher accuracy than UNIFAC and HANNA for binary and multi-component mixtures, reduces error relative to HANNA by 13-63%, reliably predicts multi-phase equilibria and identifies azeotropes, yields interpretable parameters, and is strictly thermodynamically consistent. COGNAC evaluations run at a cost comparable to UNIFAC, thereby unlocking the potential of machine-learning models for process simulations.

---


### 73. [High-Fidelity Aerostructural Dataset of Transonic Wings in Cruise Conditions](https://arxiv.org/abs/2610.36442)

**<font color=#1a73e8>作者：</font>** Pavankumar Koratikere, Abhijnan Dikshit, Leifur Leifsson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in machine learning (ML) have the potential to substantially accelerate aircraft wing design, a process that has traditionally required extensive high-fidelity simulation and design iteration. Existing public datasets for ML-based wing design have focused primarily on aerodynamic performance, with limited consideration of the multidisciplinary interactions that govern practical aircraft design. In particular, efficient wing design requires simultaneous consideration of aerodynamic performance and structural integrity, yet no publicly available datasets capture this coupled aerostructural behavior at high-fidelity. To address this need, a high-fidelity multidisciplinary dataset for static aerostructural analysis of transonic wings is introduced. The dataset includes 2471 samples, along with three out-of-distribution samples. The wing planform geometry is parameterized by span, sweep, dihedral, tip chord, and tip twist, while the airfoil cross-sections are parameterized using the class-shape transformation method. The analysis is further parameterized by Mach number, angle of attack, altitude, and structural load factor. The utility of the dataset is demonstrated by training state-of-the-art ML models to predict aerodynamic surface quantities, integrated aerodynamic performance quantities, and the failure distribution of the wingbox. ML models achieve at most 0.0309 normalized root mean squared error (NRMSE) in the prediction of aerodynamic quantities and at most 0.1189 NRMSE in the prediction of failure distribution of the wingbox. By providing coupled aerodynamic and structural responses for a diverse set of transonic wings, this dataset establishes a benchmark for developing, evaluating, and comparing multi-physics ML models for wing design. Broadly, it is intended to encourage creation of similar high-fidelity multi-physics benchmark datasets across engineering domains.

---


### 74. [LociArt: A Unified Paradigm for Free-Style Local Video Stylization](https://arxiv.org/abs/2610.36456)

**<font color=#1a73e8>作者：</font>** Yuxuan Chen, Feng Xie, Jiagao Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video stylization typically transforms entire scenes, while local artistic editing requires precise region--style association, spatial control, and temporal consistency. We introduce LociArt, a unified paradigm for free-style local video stylization that explicitly specifies where to stylize and what style to apply while preserving non-target content. At its core, GRNStyle builds on Generative Refinement Networks (GRN) and introduces a polar style-aware mask that embeds style identities as equal-norm directions within selected regions. Complementary representation--geometry conditioning combines encoded mask features with raw-mask spatial support, integrating spatiotemporal context with geometric control. To provide paired supervision, we develop an automated pipeline combining global stylization, video object removal, matting, and compositing, and construct the LociArt-100K Dataset with 100K local stylization pairs. We further establish the LociArt Benchmark, comprising 80 source videos and 84 target masks covering 168 foreground/background stylization cases, with a Style Prototype Similarity (SPS) evaluation scheme for regional style quality and complementary measures of non-target preservation and temporal consistency. Experiments show that GRNStyle outperforms existing methods in regional style quality and spatial control while maintaining strong temporal consistency. Qualitative examples further illustrate joint stylization of multiple regions with the same or different learned styles, despite training only on single-region, single-style pairs. Together, these components provide a unified foundation for learning and evaluating controllable local video stylization. Project page: this https URL.

---


### 75. [A Simple Presentation of Robust Membership Inference Attacks](https://arxiv.org/abs/2610.36458)

**<font color=#1a73e8>作者：</font>** Renaud Gaucher, Ephraim Linder, Adam Smith 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In a membership inference attack, an attacker is given the data of a particular individual, and tries to determine if that individual was included in a particular dataset, given some kind of statistics derived from the dataset or a model trained on the dataset. Roughly, a membership inference attack is robust if it succeeds even when the statistics are highly noisy, regardless of how that noise is introduced. We give a simple presentation of robust membership inference attacks for mean estimation, covering both multivariate Gaussian distributions and binary product distributions. We also give a summary of the literature on robust membership inference, covering history, extensions, and connections to other research areas.

---


### 76. [Full Collapse Is Suboptimal: Controlled Partial Neural Collapse for Long-Tailed Recognition](https://arxiv.org/abs/2610.36460)

**<font color=#1a73e8>作者：</font>** Hyeontaek Hwang, Cheonghwan Hur, Daeyoung Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent long-tailed recognition (LTR) methods incorporate neural collapse (NC) and align features to a fixed Equiangular Tight Frame (ETF) as a uniform target for all classes. However, forcing tail classes to fully collapse over-contracts their samples and weakens generalization. To address this, we propose a controlled partial neural collapse, realized through two coordinated controls on a backbone: the Class-Adaptive Sparse Activation (CASA) classifier and the ETF-constrained adaptive margin (ETF-AM) loss. Rather than forcing a uniform full collapse, this regime allows head classes to collapse along the ETF while tail classes retain within-class diversity. This prevents the tail from being forced into full collapse, which is suboptimal under imbalance. To set the dimensionality of collapse, CASA induces class-related node specialization through feature-conditioned gating so that tail classes occupy their own feature directions. For the clearance axis, ETF-AM applies a frequency-adaptive margin, with smaller margins for head classes and larger for tail classes. On CIFAR100-LT, ImageNet-LT, Places-LT, and iNaturalist-2018, our method achieves the best overall accuracy over prior methods. In the empirical analysis, within-class spread increases monotonically from head to tail classes, consistent with tail classes retaining variability rather than fully collapsing.

---


### 77. [ClusterSplat: Semantic Cluster Selection for 3D Visual Grounding in Gaussian Splatting](https://arxiv.org/abs/2610.36462)

**<font color=#1a73e8>作者：</font>** Jaesung Lee, Hyeontaek Hwang, Gabriel Manalu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study 3D visual grounding in 3D Gaussian Splatting (3DGS), where a referring expression should identify a target object as both a rendered 2D mask and a set of explicit 3D Gaussians. Prior methods typically extract 3D targets by applying heuristic thresholding or top-ratio filtering to dense primitive-level relevance scores. However, these scores often vary substantially across scenes and prompts, making such heuristics sensitive and leading to unstable targeting. ClusterSplat addresses this by reframing 3D target selection as cluster-level selection over scene-adaptive candidates. The method first learns instance-aware Gaussian features, forms feature-aware seed voxels, and merges neighboring seed voxels when a description-length criterion decreases, producing a scene-specific set of cluster candidates. Given a referring expression, a query-conditioned cluster scorer ranks the cluster candidates with a lightweight MLP, and the selected cluster directly defines the explicit 3D target while its cluster score is rendered for the 2D mask. On ScanRefer, ClusterSplat achieves the best rendered 2D segmentation and explicit 3D target metrics among the compared 3DGS baselines. It also obtains the best average Ref-LERF scores, supporting the same trend under fine-grained referring descriptions. On ScanNet v2 class name queries, ClusterSplat achieves the strongest rendered 2D results and the highest 3D matching accuracy, while maintaining competitive 3D IoU. Our project page is available at this https URL .

---


### 78. [Split Federated Unlearning](https://arxiv.org/abs/2610.36465)

**<font color=#1a73e8>作者：</font>** Jia Chen, Yecheng Lv, Xinrong Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Split federated learning (SFL) combines partitioned model execution with federated aggregation to support collaborative learning across distributed Web and edge environments. However, removing learned contributions in SFL is challenging due to cross-partition coupling and historical influence propagation through dual-side aggregation. To the best of our knowledge, we provide the first systematic formulation of Split Federated Unlearning (SFU), encompassing client-wise and class-wise removal, counterfactual retraining, and partition-specific update constraints. We theoretically characterize historical influence propagation and mode-dependent unlearning feasibility, revealing structural limitations of restricted model updates. As an initial solution, we propose SURE, integrating dual-importance estimation, selective parameter perturbation, and importance-guided recovery. Extensive experiments with existing unlearning methods adapted to SFL reveal substantial forgetting-utility trade-offs across model architectures, data distributions, and update modes. SURE achieves competitive agreement with mode-matched retraining at modest additional cost, while further analyses highlight the impact of split position and update constraints on unlearning behavior. These findings establish SFU as a distinct research problem and provide a foundation for unlearning in partitioned federated systems.

---


### 79. [Confident First, Reflective Second: Reinforcement Learning of Confidence-Preserving Reflection for Video Understanding](https://arxiv.org/abs/2610.36467)

**<font color=#1a73e8>作者：</font>** Zihao Lin, Jingyuan Liu, Yucheng Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video models answer from sampled frames and may miss the decisive moment. A common remedy is to commit to an answer, re-examine the video, and confirm or revise it, a loop now mainly learned with reinforcement learning (RL). We find that RL erodes the initial answer, a phenomenon we term confidence erosion, where confidence means the label-verified reliability of the initial answer instead of self-reported certainty: because errors can be repaired later, a correct initial answer earns less reward, and the initial answer stalls even as the final answer's gain over it rises. We propose the principle confident first, reflective second: the initial answer must stay reliable on its own, above a floor set by a reference policy, and reflection may only add to it. Our method, CoFire, implements this principle with one mechanism for each erosion channel: reward incentives, parameter drift, and gradient interference. CoFire reaches 67.0% mean accuracy on Video-MME, MLVU, and LongVideoBench, 1.7 points above the strongest compared 7B method, and improves initial-answer and final accuracy over outcome-reward RL by 4.1 and 3.7 points on average: a stronger initial answer carries through to a stronger final one.

---


### 80. [Underdamped Anchored Langevin Dynamics](https://arxiv.org/abs/2610.36470)

**<font color=#1a73e8>作者：</font>** Qi Feng, Hoang M. Nguyen, Lingjiong Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classical Langevin Monte Carlo algorithms, such as the unadjusted Langevin algorithm (ULA), are based on discretization schemes of the overdamped Langevin dynamics and are widely used for sampling in machine learning because they scale to high dimensions and large datasets. However, they require differentiable log-densities, and are less efficient for sampling heavy-tailed distributions. Although various approaches have been proposed in the literature for sampling non-differentiable and heavy-tailed targets, all of them are developed in the overdamped setting only. We propose a novel momentum-based underdamped anchored Langevin dynamics (UALD), and underdamped anchored Langevin Monte Carlo (UALMC) algorithm based on a discretization scheme of UALD. Our paper is the first to provide a kinetic (momentum-based) Langevin algorithm for non-differentiable and heavy-tailed targets that is free of asymptotic bias. The method replaces the original potential with a smooth reference potential and modifies the underdamped Langevin dynamics via multiplicative scaling in the drift term. We establish non-asymptotic guarantees in the 2-Wasserstein distance to the target distribution and show that the resulting iteration complexity has better dependence on dimension and accuracy level compared to overdamped-based anchored Langevin algorithms. We provide numerical experiments to illustrate the theory and practical performance of our proposed approach.

---


### 81. [FIDES-Live: Evaluating Behavioral Concordance in Sequential Trading Agents](https://arxiv.org/abs/2610.36476)

**<font color=#1a73e8>作者：</font>** Arther Tian, Alex Ding, Simon Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Sequential trading agents produce decisions, orders, execution receipts, account states, and reports that need not agree, even when the final portfolio value is correctly computed. We present FIDES-Live, an operational extension of FIDES from generated strategy concordance to the audit of sequential agent traces. The protocol separates structured decision validity, optional numerical commitment adherence, execution and ledger reconciliation, and receipt- grounded reporting, with explicit coverage and unscorable outcomes. We retrospectively audit ten requested inference routes over 7,299 cryptocurrency account-rounds and a 310-round equity pilot, using real market observations and local paper execution. Cryptocurrency decision validity is 97.35% and structured reporting accuracy is 90.81% among scorable responses, but route-level decision and reporting performance can diverge sharply. Commitment adherence is 94.36% overall; it falls to 62.63% on constraints emitted with nonempty order proposals, compared with 97.56% for valid empty proposals. All retained cash and position transitions reconcile with recorded fills, while execution controls and unavailable quotes explain separate rejection populations. Short-window marked returns provide descriptive context rather than a new test of whether concordance predicts alpha. These observations motivate reporting concordance, evidence coverage, activity, and financial outcomes separately. They do not establish long-run trading skill, semantic faithfulness of explanations, or causal benefits from audit feedback.

---


### 82. [Spatial-Frequency Learning for Scanning Transmission Electron Microscopy Image Enhancement](https://arxiv.org/abs/2610.36487)

**<font color=#1a73e8>作者：</font>** Hesong Li, Ying Fu, Ziqi Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scanning Transmission Electron Microscopy (STEM) enables the observation of atomic arrangements at sub-angstrom resolution and plays a key role in the discovery and characterization of advanced materials. Raw STEM images are often noisy and blurred due to multiple degradations. Although recent deep learning methods improve STEM images, their performance remains limited under severe degradations. In this work, we propose a spatial-frequency learning framework for STEM image enhancement. Specifically, we design a spatial-frequency fusion network that exploits periodic atomic arrangements in the frequency domain and restores local atomic details in the spatial domain. Spatial- and frequency-domain features are enhanced separately and then fused. We also present a STEM noise calibration method for synthesizing more realistic STEM images. The parameters of scan noise, pointwise noise, and background noise are estimated through statistical analysis and fitting of real STEM images. Using these calibrated parameters, we construct a diverse dataset containing a wider range of atomic arrangements, imaging modes, and degradations. Random masks combine different atomic arrangements to simulate interfaces between multiple materials. Experimental results demonstrate that our method achieves state-of-the-art enhancement performance on synthetic datasets and real images of advanced materials while improving atomic localization accuracy.

---


### 83. [AC-JEPA: Anchored Cross-Modal Joint Embedding Predictive Architecture for Visual-to-Symbolic Translation](https://arxiv.org/abs/2610.36493)

**<font color=#1a73e8>作者：</font>** Chaofei Hong, Ziyang Chen, Baochen Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cross-modal translation requires models to capture shared semantics across modalities while preserving the fine-grained structure required by the target modality. Yet in real-world scientific domains, paired data are often imperfect, while obtaining clean pairs at scale is costly. Supervised fine-tuning (SFT) directly optimizes cross-modal translation through categorical token-level supervision, but this objective is sensitive to errors in the target sequences. JEPA offers a complementary representation-space objective, but most existing formulations focus on prediction within a modality rather than translation across modalities. We introduce Anchored Cross-Modal JEPA (AC-JEPA), an SFT-compatible plug-in that predicts masked intermediate states in both cross-modal directions using paired data. The joint-embedding objective targets cross-modal structure predictable from context, while the causal SFT path retains direct token-level supervision for the target sequence. During self-training, AC-JEPA learns from continuous latent targets derived from imperfect pseudo-labeled pairs, offering intrinsic tolerance to local data errors without promoting pseudo-tokens to hard categorical supervision. Using optical chemical structure recognition as a testbed, AC-JEPA trained on clean pairs achieves 76.07% accuracy on the Simple set of the WildMol benchmark, compared with 67.40% for SFT alone. Using the same pseudo-labeled data for both approaches, AC-JEPA-based self-training further raises accuracy to 80.23%, whereas accuracy under direct SFT drops from 67.40% to 63.47%. These results support SFT-anchored joint-embedding prediction as an effective strategy for cross-modal translation under both curated and imperfect supervision.

---


### 84. [GarmentSegAgent: Autonomous Garment Segmentation for Web Fashion Images via Textual Self-Refinement](https://arxiv.org/abs/2610.36506)

**<font color=#1a73e8>作者：</font>** Jia Chen, Chao Huang, Xinrong Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Web fashion images support applications such as visual product search and consumer-to-shop matching, yet their visual heterogeneity makes reliable garment segmentation challenging. Despite advances in promptable segmentation, autonomously identifying and correcting garment-specific errors without human-provided spatial prompts remains difficult. We propose GarmentSegAgent, an autonomous framework that integrates semantic planning, spatial execution, and visual evaluation through iterative textual self-refinement. At its core, we introduce CAST (Constrained Attribution-guided Selective TextGrad), which connects visual error attribution with targeted textual optimization. CAST identifies instruction components responsible for segmentation errors, selectively updates them through textual gradients, and validates the resulting instructions against garment-specific constraints. This enables image-specific error correction at inference time while keeping the underlying foundation models frozen. Experiments on DeepFashion2, ModaNet, and Fashionpedia demonstrate consistent improvements in region overlap and boundary accuracy, alongside more reliable refinement than conventional TextGrad. By enabling visual feedback to guide controlled instruction updates, GarmentSegAgent offers a promising direction for autonomous garment understanding, with potential applications in scalable fashion content analysis, visual retrieval, and consumer-to-shop matching on the Web.

---


### 85. [Identity or Evidence? Auditing Evidence Dependence in Agentic Life-Science Benchmarks](https://arxiv.org/abs/2610.36510)

**<font color=#1a73e8>作者：</font>** Danai Brilli, Maria Georgila  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Agentic life-science benchmarks give an agent evidence about a named entity and score an answer against a recorded outcome. That score tests reasoning over evidence only if the evidence, rather than the name, determines the answer. We examine this distinction by varying identity and evidence independently on a clinical-outcome benchmark and published tasks from Biomni and LAB-Bench. Blinding identity matters little when a prompt contains a decisive sequence or passage. It matters a great deal when the prompt is mostly a name and candidate list (0.742 named versus 0.082 blinded; chance 0.093). Across 96 LAB-Bench LitQA2 questions, the gap increases under one fixed passage-redaction scheme (+0.000 to +0.135; per-instance slope +0.147, p= 0.004). On the clinical benchmark, a no-evidence recall probe matches prediction accuracy and recovers a database-specific programme count. So, we argue that benchmarks intended to measure evidence-dependent reasoning should report identity-blinded results, retrieval telemetry, and positive controls.

---


### 86. [Benchmarking Task Takeover Across Agent Handoffs](https://arxiv.org/abs/2610.36523)

**<font color=#1a73e8>作者：</font>** Wenyuan Li, Guang Li, Dongyuan Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As agents collaborate on longer tasks, responsibility may pass between models before the work is complete. The receiving model must build on prior decisions, observations, and actions while addressing the remaining requirements. Evaluating this transition requires connecting the information preserved at handoff to how the receiver continues the work, a relationship that task-success and memory-retention scores alone do not capture. We introduce the Handoff State Continuity Benchmark (HSC-Bench), comprising 1,039 tasks that evaluate two complementary aspects of task takeover: recovering relevant repository evidence and continuing from established conversational, tool, and file-work state. Comparisons across six receiving models show that structured handoff state improves repository evidence recovery for every model and continuation performance for most models. The strongest receivers differ between the two tracks, showing that evidence-recovery rankings alone do not characterize performance when continuing from inherited state. By combining these comparisons with checks of subsequent responses and actions, HSC-Bench evaluates both access to prior evidence and adherence to established commitments and completed work. This provides a basis for selecting receiving models and assessing handoff representations according to the work that must be carried forward.

---


### 87. [ATEMPO: Amortized Transfer Entropy Model Per-lag Over-Time](https://arxiv.org/abs/2610.36536)

**<font color=#1a73e8>作者：</font>** Emma Andrews, Konstantinos Kontras, Keane Ong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When one time series informs another, the delay at which that information arrives determines if models can utilize this relationship effectively. A source may be strongly predictive at one delay but uninformative at neighboring lags. Therefore, fixed input windows may obscure this structure by bundling informative and irrelevant history together. Transfer entropy (TE) can recover these delays by measuring how much a source's past tells us about a target beyond the target's own history. However, existing TE estimators require separate fits across source and conditioning depths, with further estimation on local windows to track delays over time. We introduce ATEMPO, a diffusion-based transfer entropy estimator amortized over lags and time. ATEMPO samples source and conditioning depths during training and conditions explicitly on temporal position, allowing a single score network to estimate the full TE surface without refitting. Differencing this surface recovers when information arrives. Across synthetic datasets with ground-truth TE, ATEMPO achieves the lowest mean relative error among baselines, and on datasets with known lags, ATEMPO achieves $0.98\pm0.04$ lag-detection accuracy. ATEMPO requires a single fit across source depths $K=6$ and target depths $L=3$, whereas existing estimators require 18 separate fits to evaluate the same $K \times L$ grid. On three systems with time-varying lag, ATEMPO is the only estimator to maintain perfect lag-detection accuracy across all evaluated window lengths. These recovered delays improve downstream forecasting: ATEMPO-selected inputs reduce MSE on WEATHER-5K by 7.25%, while 120 selected inputs outperform the benchmark's 240-feature default by 4.6%. Across three brain-computer interface tasks, using ATEMPO-selected lags achieves the highest or equal-best $R^2$, improving mean $R^2$ by 4.1% relative to the strongest competing baseline.

---


### 88. [Frugal Handwritten Text Recognition for Sub-Saharan Civil-Status Registers: A Smartphone-to-Records Pipeline with CPU-Only Inference](https://arxiv.org/abs/2610.36540)

**<font color=#1a73e8>作者：</font>** Ousmane Hamadou, Jean Louis Kedieng Ebongue Fendji  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Handwritten civil-status registers across Sub-Saharan Africa are being photographed, but rarely transcribed, which leaves their content unsearchable. Local administrations that hold these records typically lack GPUs, reliable connectivity, and the budget for external digitization services. We study whether a frugal pipeline, with consumer-grade capture and CPU-only inference, can make such registers machine-readable. We introduce a corpus of 1,568 smartphone images of handwritten birth, marriage, and death records from a municipal registry in Chad, with line-level transcriptions for 185 records. Our pipeline combines a fully classical preprocessing stage, running at about 2.6 images per second on a laptop CPU, with a Kraken recognizer fine-tuned from a pretrained model in about four hours on a free-tier GPU. On manually corrected line segmentation and a single-registry test set whose writers also appear in training, fine-tuning reduces the character error rate from 14.53% to 0.50% and the word error rate from 56.93% to 3.37%. On a six-core laptop CPU, the recognizer weighs 61 MiB, peaks below 2.6 GiB of RAM, and processes an image in under 6 s on average, excluding line segmentation. Finally, a downstream information-extraction task shows that residual recognition errors cost about 9 F1 points on role resolution, compared with a 36.7-point gap between the fine-tuned and pretrained recognizers. These results are evidence of feasibility within one registry, not of performance on unseen writers or sites; we discuss these limitations in detail.

---


### 89. [Monitor Accuracy Isn't the Answer: A Decision-Value Framework for Evaluating AI Agent Restart Monitors](https://arxiv.org/abs/2610.36544)

**<font color=#1a73e8>作者：</font>** Siddharth Jain, Venkat N. Vedam  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Classification accuracy and true-positive and false-positive rates alone do not determine whether restarting an AI agent improves success. Using an exact alarm-to-action identity for an independent clean restart with zero monitoring overhead, we show analytically that a monitor with fixed 90% accuracy can swing from a five-percentage-point loss to a 35-point gain in success rate, depending solely on the replacement attempt's residual-budget success probability. We introduce two techniques for evaluating monitors and progress signals in decision terms. First, a decision-sufficiency criterion, a binary-action specialization of Blackwell's comparison of experiments, identifies which progress representations or context compressions preserve the information needed to choose optimally between the specified actions, independent of trace reconstruction fidelity. Second, a finite-sample, model-free decision audit uses simultaneous binomial intervals over existing agent traces, without additional model calls, to certify a preference for "restart" or "continue" under stated sampling assumptions, or return "abstain" when evidence is insufficient. In a study of 194 externally evaluated model executions on 19 selected SymPy issues from SWE-bench Verified, with a retrospective audit of 130 of these traces, we find a 2.29-point apparent restart gain traced to a single surviving failed attempt, a 42.29-point loss on a second model, no positive replication of the initial gain on prospective task cohorts, and zero of 103 live comparisons meeting the specified certification bar. These results motivate evaluating agent monitors through recovery opportunity, decision value, and statistical support, rather than classification performance alone.

---


### 90. [Holomorphic Cauchy Networks for Efficient Stationary Tail Computation in High-Dimensional Reflected Brownian Motions](https://arxiv.org/abs/2610.36558)

**<font color=#1a73e8>作者：</font>** Kehan Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stationary tail computation for high-dimensional reflected Brownian motions (RBMs) remains computationally challenging. Building on NN4MGF's shared-coordinate basic-adjoint-relationship (BAR) framework, we develop Holomorphic Cauchy Networks (HCNs). Native complex-valued rational Cauchy subnetworks enforce holomorphicity on pole-free domains, removing sampled Cauchy-Riemann penalties and their input-derivative graphs. Exact origin anchoring and boundary-coordinate exclusion enforce structural identities, while anchored interactions represent dependent transforms. Under holomorphic-log assumptions, we establish simultaneous value and first-derivative approximation for the constrained architectures and a mixed-derivative lower bound for coordinate-only representations under nonzero cross-covariance. Closed-form real-axis derivatives and sequential backpropagation further control memory. On the same NVIDIA H100 NVL, the tested 30D HCN configuration uses approximately tenfold less peak allocated memory and has 9.7-fold lower mean update time than NN4MGF; extrapolation to the respective scheduled update counts gives a projected full-schedule update-time ratio of 58.2. With 64 million sampled base inputs per high-dimensional run, HCN reaches 50 dimensions on a laptop GPU with 6.367% mean relative error over thresholds 1 through 8. Degree-matched comparisons yield lower reported mean relative errors over the primary evaluation ranges, including 1.422% versus 6.684% on the 2D Harrison non-product benchmark. An exploratory 10D correlated example illustrates the interaction extension.

---


### 91. [Peak-DNA: Recurrent Morphology in Global Narrative Propagation](https://arxiv.org/abs/2610.36571)

**<font color=#1a73e8>作者：</font>** Joosung Kim, Luyonghe Li, Shanwen Wu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Global narrative streams exhibit noisy, fragmented, and asynchronous amplification bursts, making direct waveform comparison unreliable for recurrence analysis. This paper introduces Peak-DNA, a framework for identifying recurrent propagation morphology in global narrative streams. The proposed framework transforms hourly GDELT activity into normalized macro-peak episodes through denoising, macro-peak consolidation, and temporal alignment, and compares propagation morphology using DTW-based similarity analysis. Using GDELT narrative streams, we analyze five high-amplification narrative domains: Iran, Defense, AI, Space/Elon, and Quantum/PQC. The results show that amplification events repeatedly converge toward morphology-level propagation patterns within each narrative domain. DTW-based similarity analysis further demonstrates strong intra-domain structural compactness despite heterogeneous publication dynamics and severe observational noise. These findings suggest a measurable morphology layer beyond semantic content or anomaly intensity, providing an initial structural foundation for recurrence-aware narrative monitoring, propagation family discovery, and longitudinal Narrative Genome analysis.

---


### 92. [Learning from Points and Patches: A Pre-trained Hybrid Attention Transformer for Time Series Analysis](https://arxiv.org/abs/2610.36572)

**<font color=#1a73e8>作者：</font>** Peiwang Tang, Cheng HE, Yupeng Ye 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series data generated by Web services and connected systems support applications such as user activity analysis, service monitoring, and resource management. However, learning transferable representations from heterogeneous time series remains challenging due to diverse temporal patterns, variable sequence lengths, and limited high-quality annotations. Despite the success of pre-training in natural language processing and computer vision, effective time-series pre-training requires strategies tailored to temporal data.
We propose TimeHAT (Hybrid Attention Transformer), a general-purpose pre-training framework for time-series analysis that addresses two complementary questions: what to learn and how to learn. For what to learn, we introduce a Unified Point-Patch Masking Strategy (UPPMS) that integrates point-level and patch-level supervision within a unified framework for contextual reconstruction and causal extrapolation, enabling the model to capture both fine-grained temporal variations and broader temporal patterns. For how to learn, we develop a Hybrid Attention Encoder (HAE) that combines prefix-constrained bidirectional attention in initial layers with directional hybrid attention in deeper layers, aiming to preserve effective contextual interactions while mitigating rank degeneration.
We evaluate TimeHAT across real-world datasets and four downstream tasks: classification, long-term forecasting, imputation, and anomaly detection. Experiments cover fine-tuning, few-shot, and zero-shot transfer settings, demonstrating competitive performance across diverse time-series analysis tasks. Code is available at this https URL.

---


### 93. [Follow the Herd: A Data-Driven Approach for Actionable Recourse](https://arxiv.org/abs/2610.36580)

**<font color=#1a73e8>作者：</font>** Nishtha Madaan, Srikanta Bedathur  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As machine learning systems make increasingly greater decisions about people's lives, it is critical to provide users with actionable recourse about how they can achieve their desired outcomes. This problem is currently tackled by relying on expensive human supervision which involves hand-designing a cost function before searching for low-cost actions that achieve the desired outcome. In this paper, we propose \textit{``Data-Driven Action Recourse"} (DDAR), the first approach for providing action recourse without requiring costly supervision from humans about action costs. We build upon the notion that highly likely trajectories in the historical user data should be associated with lower costs. With this, DDAR first builds a dynamics model of historical user trajectories. Under this model, it then searches for trajectories that achieve the desired outcome. In experiments, we find that this simple approach recommends plausible action recourse without requiring human supervision, achieving lower action costs than the existing approaches.

---


### 94. [MM-Net: A Multimodal Multi-Task Network for Sleep Staging and Sleep Apnea Assessment After Ischemic Stroke](https://arxiv.org/abs/2610.36583)

**<font color=#1a73e8>作者：</font>** Md Wahiduzzaman Suva, Esm E Moula Chowdhury Abha, Md Imtiaj Alam Sajin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated polysomnography after ischemic stroke is challenging because of altered sleep-related neural activity and concurrent respiratory disturbances. Existing stroke-specific approaches mainly address sleep-stage classification, leaving joint analysis of sleep architecture and respiratory events underexplored. Moreover, adapting pretrained EEG encoders introduces a representation inconsistency when downstream models are trained on embeddings from previously seen patients but evaluated on unseen individuals. We propose MM-Net, a multimodal multi-task framework that resolves this inconsistency through cross-fitting and ridge-based embedding alignment. Sleep-adapted EEG-EOG representations and engineered neural descriptors are fused with learned cardiorespiratory features through cross-attention and shared temporal modeling for simultaneous sleep staging and respiratory-event detection. On iSLEEPS (99 patients with subacute ischemic stroke), ten-fold patient-independent evaluation achieved 76.3% staging accuracy (Cohen's $\kappa$ = 0.656) and 0.825 respiratory-event AUC, outperforming the evaluated baselines under matched protocols. The sleep-adapted encoder improved the downstream model when its embeddings were aligned, raising staging accuracy by 1.4 percentage points over the frozen encoder ($p$ = 0.020) versus 0.2 points without alignment. MM-Net also achieved 86.4% staging accuracy on Sleep-EDF, above every single-EEG architecture reimplemented on the same recordings, and 80.3% staging accuracy with 0.889 respiratory AUC on ISRUC-I, exceeding its retrained staging baselines. Without retraining, the iSLEEPS-trained model retained respiratory AUCs of 0.833 on ISRUC-I and 0.841 on UCD. These findings support representation-consistent neural adaptation and joint physiological modeling across stroke, healthy-sleep, and sleep-disorder cohorts.

---


### 95. [Recall or Relearn? A Mixture of In-Context Experts for Recurring Concept Drift](https://arxiv.org/abs/2610.36585)

**<font color=#1a73e8>作者：</font>** Zhangkai Wu, Xu Zhang, Zhihong Cui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models (TFMs) are being applied to Web data streams such as network intrusion detection, where they adapt by updating the labelled rows of their context without retraining. When a past concept returns after leaving the context, a TFM faces a recall-or-relearn decision between restoring stored rows of the concept and relearning it from new labels. We propose MICE (Mixture of In-Context Experts), a training-free learner that cuts the stream into segments at detected changes. It merges a closed segment into a stored context when the TFM's estimated additional error on the segment is within a tolerance, under a capacity limit on stored contexts. A fast level weights the stored contexts and first-in-first-out (FIFO) windows by the log-loss of their predictions on the last labelled batch. We show that, with pure stored contexts and a margin condition, this fast level gains over relearning, in expected accuracy, the normalised positive area between the stored context's accuracy and the TFM's learning curve, up to a first-batch term. A slow level mixes the fast level's prediction with that of the FIFO window of the last labelled rows and bounds the discounted half-Brier regret of MICE against this window at every time. Learning curves measured beforehand predict the ordering of the observed recall gains. MICE outperforms reset, which empties the context at detected drifts, on grid streams with random boundary phases. Merging keeps fewer experts than pools that store every segment, and with fixed segmentation a time-matched snapshot pool matches MICE on the shifted grid. On real streams, MICE has the highest mean accuracy of all policies we compare.

---


### 96. [LabWorld: Learning Interactive 4D Worlds for Scientific Experimentation](https://arxiv.org/abs/2610.36592)

**<font color=#1a73e8>作者：</font>** Suozhi Huang, Kelsey Fu, Binxu Li 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous scientific agents must not only reason about experiments but also interact with the physical environments in which they are executed. Existing laboratory simulators typically rely on manually constructed assets and predefined procedures, while laboratory videos capture real equipment, layouts, and interactions but leave this information implicit in pixels. We introduce LabWorld, an agent-driven Real2Sim framework for reconstructing interactive 4D laboratory worlds from monocular RGB video. LabWorld recovers reusable 3D assets, a metric scene, time-varying object states, and procedure events. Multi-frame observations provide complementary evidence for asset and scene reconstruction, while motion reconstruction combines visual and geometric observations with event constraints encoding the spatial and temporal requirements of laboratory interactions. We evaluate LabWorld on real pipetting and vortexing videos collected in our laboratory against general-purpose agentic and dedicated reconstruction baselines. For pipetting, LabWorld achieves a mean Mask IoU of 0.501, exceeding the strongest baseline by 0.033. For vortexing, it achieves a mean Tube-Length-Normalized PCK-AUC of 0.638, exceeding the strongest baseline by 0.035. On five pipetting videos, event-conditioned reconstruction increases the fraction of modeled physical constraints satisfied from 14.3% (5/35) to 100% (35/35). The resulting worlds expose geometry, motion, articulation, and events as explicit, editable state for replay, inspection, and future embodied scientific systems.

---


### 97. [WithinVAE: Compact Visual Autoencoding with Self-Distilled Semantics](https://arxiv.org/abs/2610.36593)

**<font color=#1a73e8>作者：</font>** Yuzhou Ji, Jiepeng Wang, Tianyu Jin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual autoencoders must balance reconstruction fidelity, compactness, and semantic structure. Existing semantic tokenizers typically inherit semantics from pretrained recognition encoders, whose invariances can discard the appearance detail required for inversion. We show that this inheritance is unnecessary: semantic structure can be learned inside an autoencoder's own reconstructive representation. We introduce WithinVAE, a compact variational visual autoencoder with a sequential bottleneck, DINO/iBOT-style self-distillation from an exponential-moving-average copy of the autoencoder itself, and position-dependent token masking to achieve a 4-fold compression ratio, which is free of pretrained representation encoder or external semantic target. On ImageNet-1K at $256\times256$, WithinVAE improves all four reported reconstruction metrics over RPiAE including PSNR by 1.36 dB, while using half its latent scalar capacity. Under frozen evaluation, the same latents improve linear probing by 6.5 points over RPiAE and 5.1 points over our reconstruction-only baseline, attributing the semantic gains to self-distillation rather than architecture or external supervision. An auxiliary latent-to-latent model reproduces the ordered-compression trend, and a pixel-to-latent model transfers the objective to a pretrained generative space. These results separate the origin of semantic supervision from its use: a compact visual autoencoder can organize semantic structure without borrowing a recognition representation.

---


### 98. [4D Reconstruction with Events & RGB](https://arxiv.org/abs/2610.36610)

**<font color=#1a73e8>作者：</font>** Dulanga Weerakoon, Darshana Rathnayake, Van Minh Do 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing dynamic 3D scenes over time (4D reconstruction) from a single moving camera is central to robotics and AR/VR applications, yet state-of the-art feed-forward methods rely solely on RGB frames and therefore inherit the failure modes of conventional cameras, including motion blur and temporal aliasing under fast or non-uniform camera and object motion. Event cameras report per-pixel brightness changes asynchronously at microsecond resolution, offering a complementary signal that is largely immune to these artifacts, but whether this modality can be incorporated into existing RGB based 4D reconstruction pipelines without a full architectural redesign remains an open question. In this preliminary study, we investigate a minimal extension: we augment Monst3R, an existing RGB-only 4D reconstruction model, with an additional event-camera input branch, leaving the rest of the architecture unchanged. Across 3 benchmark datasets, this simple RGB-event fusion reduces Abs Rel by 3.4% on average relative to the RGB-only Monst3R baseline, and a sensitivity analysis shows that the improvement grows with the magnitude of camera and object motion, with the largest gains observed under high object motion conditions where RGB-only reconstruction degrades most. These early results suggest that even a lightweight, non-invasive fusion of event data can meaningfully improve 4D reconstruction robustness, motivating a more thorough architectural investigation in future work.

---


### 99. [Silent Blindness: Fault Vulnerability of Hardware Malware Detectors](https://arxiv.org/abs/2610.36612)

**<font color=#1a73e8>作者：</font>** Alireza Abolhasani Zeraatkar, Parnian Shabani Kamran, Parsa Mirfasihi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hardware malware detectors (HMDs) classify hardware performance-counter measurements to identify malicious execution. Faults in their decision logic or parameters can weaken detection and allow malware to be classified as benign. We investigate this vulnerability through structural fault injection across a design space comprising 18 classifiers, four counter budgets, and AdaBoost and Bagging ensembles. The simulation evaluates 453,174 decision stuck-at and selected parameter bit-flip events on a 7,400-instance. Primary comparisons use 128 completed configurations. These completed-subset results are distinguished from the simulation summaries covering 140 configurations with enumerable fault sites. Fault outcomes are classified by their security consequences, including evasion, false-alarm increases, and metric silence. A fault is critical when malware recall decreases by at least five percentage points. Tree-based models exhibit a lower mean critical-fault fraction than function-based models, 5.3% versus 14.3%; exhaustive-only analysis preserves this ordering. Moreover, 72.3% of evaluated tree faults are metric-silent, changing both recall and false-positive rate by less than 0.1 percentage points without necessarily preserving individual predictions. Among the 27 completed matched comparisons, Bagging reduces criticality in 26, whereas AdaBoost increases it in two. Finally, an exact minimax selection method identifies protection candidates under additive unit costs and ideal correction. For a representative J48 detector, protecting 16 of 115 structural units reduces predicted maximum recall loss from 60.1 to 3.3 percentage points. These results characterize structural-model sensitivity and potential protection benefits; faulted RTL correspondence and physical hardening overhead remain unvalidated.

---


### 100. [Normalized Cuts and Data Clustering via Matrix Fractional Programming](https://arxiv.org/abs/2610.36616)

**<font color=#1a73e8>作者：</font>** Yannan Chen, Beichen Huang, Licheng Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The normalized cut (NCut) problem is a fundamental one in the area of data clustering. Despite its fractional structure, the NCut problem is seldom considered from a fractional programming (FP) perspective in the existing literature. The main reason is that the conventional FP method is inadequate for this problem case: the classical Dinkelbach's transform can only handle a single ratio and hence is limited to the two-class clustering, whereas the multi-class clustering involves multiple ratio terms. This work proposes a novel so-called multidimensional quadratic transform that is capable of dealing with the multi-ratio case; it recasts the NCut problem into a bipartite matching problem---which can be immediately solved by linear search. Furthermore, we explore the connection between the proposed FP method and the minorization-maximization (MM) theory, and in turn characterize the convergence behavior of our algorithm. Finally, we conduct experiments to numerically demonstrate the advantages of the proposed FP-based algorithm in a variety of data clustering and image segmentation tasks.

---


> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-257](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
