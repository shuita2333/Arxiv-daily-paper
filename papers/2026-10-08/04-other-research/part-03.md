# 📦 其他研究 | 2026年10月08日

> 本类共 **335** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-335](./part-07.md)

---

### 101. [AccentCL: Robust Accent Classification with Incremental Expansion](https://arxiv.org/abs/2610.07426)

**<font color=#1a73e8>作者：</font>** Mu-Ruei Tseng, Waris Quamer, Ghady Nasrallah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Accent classifiers are typically trained with a fixed label inventory and cannot accommodate new accent categories as new data becomes available. Moreover, accented speech corpora often exhibit substantial class imbalance and/or domain shift due to differences in recording conditions across corpora. We present AccentCL, a class-incremental learning framework for English accent classification that is robust to class imbalance and cross-corpus domain shift. AccentCL extracts multi-layer representations from a frozen Whisper-Large-v3 encoder, optimized with an imbalance-aware cross-entropy loss to reduce bias toward the majority accent classes and a domain mean alignment loss that minimizes distributional mean shift across training corpora. The label space is then expanded via replay-based continual learning, using the frozen base model for knowledge retention and an old-to-new margin loss to reduce overprediction on newly added classes. On a five-class accent classification task, AccentCL achieves 77.1% balanced accuracy and a 76.9% macro-averaged F1 score. We further evaluate the model's ability to incrementally incorporate two new accent categories: Spanish-accented and Chinese-accented English. When adding Spanish-accented English to the pretrained model, AccentCL attains an F1 of 83.3% on the new class while retaining 77.3% balanced accuracy on the base classes. When subsequently adding Chinese-accented English, it achieves 61.8% F1 on the new class while preserving 77.6% balanced accuracy on the previously learned classes. These results show that AccentCL enables robust regional accent classification while allowing new accent categories to be added without full retraining.

---


### 102. [Adaptive Gait Biofeedback With Participant-Held-Out Modeling and Participant-Specific Updating in Chronic Ankle Instability](https://arxiv.org/abs/2610.07428)

**<font color=#1a73e8>作者：</font>** Jaeyoon, Veronika Lebisova, Jeniya Sultana 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Adaptive gait biofeedback may support repeated practice in chronic ankle instability, but its evaluation must address model performance and human response. We evaluated a temporal convolutional classifier on protocol-defined, angle-derived GOOD/BAD gait-cycle labels using participant-held-out leave-one-subject-out (LOSO) cross-validation in 20 participants. Seven participants in the adaptive-intervention group completed nine sessions over three weeks, with one motion-capture recording analyzed per session. Models updated after failed sessions were compared offline with their parent models on the same-session validation subset used for candidate selection and the first subsequent adaptive-session recording. Frontal-plane ankle angle was compared between the adaptive group and 10 sequentially enrolled controls at Baseline, Post, and 7-day Retention. Across 20 held-out folds, mean fold-level area under the receiver operating characteristic curve (AUROC) was 0.948, sensitivity for angle-threshold-exceeding BAD cycles was 0.941, and specificity for angle-threshold-meeting GOOD cycles was 0.366. Mean BAD-class F1 was higher in candidate models by 0.187 on the same-session subset and 0.118 on the first subsequent recording. At Post, the adaptive group had a baseline-adjusted frontal-plane ankle angle 5.168 degrees lower than controls (95% confidence interval, 1.766-8.569 degrees lower); the Retention contrast was uncertain. These findings characterize population-model discrimination and offline participant-specific updating during repeated biofeedback use, alongside a nonrandomized Post frontal-plane ankle angle association. They do not establish independent clinical gait classification or a causal benefit of updating.

---


### 103. [StaFIR: Convex Learning of Stationarity-Aware Causal Filters](https://arxiv.org/abs/2610.07430)

**<font color=#1a73e8>作者：</font>** Lorena Egger, Mathis Linger  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reducing nonstationarity in a persistent time series entails deciding how much of its temporal dependence to remove. In finance, fractional differencing is often tuned using the Augmented Dickey--Fuller (ADF) test, limiting the search to a one-parameter family of lag profiles and addressing input preservation only indirectly. We propose StaFIR, a causal finite-impulse-response filter with a learned nonnegative mixture of exponential lag profiles. Its convex learning objective balances empirical stationarity with similarity to the input. We evaluate StaFIR on ARFIMA--GARCH controlled settings and rolling financial series, including a realized-volatility forecasting task. The experiments show that StaFIR adjusts its filtering strength to persistence while limiting unnecessary transformation in stationary regimes. In downstream forecasting, there is no clear accuracy difference from fixed half-order differencing, while StaFIR achieves higher measured similarity to the raw signal. A complementary direct forecasting experiment finds that greater input similarity is associated with smaller forecasting penalties, although the raw representation remains stronger.

---


### 104. [Artifact removal improves electrodermal waveforms but not downstream classification in a virtual-reality balance task](https://arxiv.org/abs/2610.07438)

**<font color=#1a73e8>作者：</font>** Haochen Chai, Qixu Zhu, Siyao Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Artifact removal routinely precedes the classification of electrodermal activity (EDA), on the assumption that a cleaner signal supports a better decision. We tested this assumption in a virtual-reality (VR) balance-disturbance task. A residual gating network was trained on a benchmark with expert-corrected EDA, frozen, and applied to VR recordings, where raw and gated signals were classified by five published time-series methods under identical leave-one-participant-out evaluation. On the benchmark the gate detected artifacts well (median record AUROC 0.94) and reduced error inside artifact regions by 17.8%. In the VR task it did not improve classification. Changes in balanced accuracy ranged from -1.35 to +0.93 percentage points, no classifier improved and two lost accuracy, and all five were equivalent to raw input within +/- 3.32 points. The benefit was lost between waveform and decision. The correction that lowered waveform error also reduced skin conductance response detection in all 43 benchmark records. Processing left 92.8% of predictions unchanged, and the predictions it did change were corrected and corrupted at similar rates. The VR recordings also carried little contamination (an estimated 4.6% of samples), and even perfect localization of deliberately injected artifacts recovered only 3.3 points in the most sensitive classifier. A pooled association between artifact level and accuracy (11.3 points) disappeared within participants (0.1 points), showing how differences between people can make cleaning look useful. Preprocessing should be judged by the decision it supports, against an unprocessed arm.

---


### 105. [Fork-and-Flush: Escaping Idea Basins in Autoresearch Agents](https://arxiv.org/abs/2610.07447)

**<font color=#1a73e8>作者：</font>** Ziyang Cai, Christos Ziakas, Vasilis Kontonis 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoresearch agents tackle open-ended problems by repeatedly proposing candidate solutions, evaluating them, and using feedback to guide subsequent experiments. We show that independent runs of the same agent on the same task often plateau at substantially different scores, with gaps that persist even after considerable additional compute. Embedding their candidate artifacts by functional similarity provides further evidence that trajectories remain in localized regions of the solution space, which we call idea basins. To help agents escape these basins, we study a simple periodic intervention, fork-and-flush. Our method forks the agent into parallel trajectories, each inheriting the accumulated workspace but starting with a fresh chat context. After running each trajectory for a fixed horizon, the agent continues from the highest-scoring one. Across 13 long-horizon research and engineering tasks, with individual agent runs lasting up to several days, fork-and-flush outperformed the single-run and best-of-N baselines by a relative improvement of 66.0% and 44.4%, respectively, on the min-max normalized average score under an equal compute budget.

---


### 106. [Active Feature Acquisition for Cost-Efficient Temporal Prediction with Reduced Participant Burden](https://arxiv.org/abs/2610.07452)

**<font color=#1a73e8>作者：</font>** Yunni Qu, Bing Cai Kok, Whitney Ringwald 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate forecasting of pathological outcomes is a central problem in psychology. To do so, psychologists often collect intensive longitudinal data. However, in such studies, the desire to acquire a large number of variables for the sake of accurate prediction is often counteracted by the need to minimize participant burden. Acquiring more variables per occasion can yield better predictions, but having too many acquisitions increase the risk of non-response and attrition. Longitudinal Active Feature Acquisition (LAFA) is a principled approach to resolve this conundrum. Instead of requiring responses to every item at every acquisition occasion, LAFA produces a policy that seeks to optimally select dynamic subsets of items to be acquired at each timepoint while preserving our ability to forecast a specific outcome. However, existing LAFA methods are mostly based on Neural Networks (NN) that are difficult to interpret in practice. In this work, we introduce a tree distillation method for learning an interpretable policy from NN-based LAFA networks. We validated our method through both a simulation and an empirical EMA dataset on forecasting daily alcohol consumption. In both cases, we find that we can meaningfully reduce the number of items acquired at each occasion with minimal loss in accuracy. Networks (NN) that are difficult to interpret in practice. In this work, we introduce a tree distillation method for learning an interpretable policy from NN-based LAFA networks. We validated our method through both a simulation and an empirical EMA dataset on forecasting daily alcohol consumption. In both cases, we find that we can meaningfully reduce the number of items acquired at each occasion with minimal loss in accuracy.

---


### 107. [Interpretable Hypergraph Learning via Neural Additive Models](https://arxiv.org/abs/2610.07458)

**<font color=#1a73e8>作者：</font>** Shihan Feng, Xin Zheng, Shiyi Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hypergraphs offer a natural framework for modeling networked data, where dependencies among entities are governed by higher-order interactions. While hypergraph learning methods such as hypergraph neural networks have demonstrated remarkable predictive performance, most existing approaches rely on black-box message-passing architectures, making it difficult to disentangle the contributions of node attributes and higher-order structural information. To address this challenge, we introduce the hypergraph neural additive network (HGNAN), an inherently interpretable framework for learning on hypergraph-structured data. HGNAN extends classical neural additive models to higher-order relational data by integrating feature-wise nonlinear decomposition with hypergraph-aware structural aggregation, enabling transparent prediction for both node- and hyperedge-level tasks. Extensive experiments on benchmark datasets demonstrate that HGNAN achieves performance comparable with state-of-the-art hypergraph learning methods while providing intrinsic and meaningful interpretability.

---


### 108. [Auditable Claims about AI Agents](https://arxiv.org/abs/2610.07459)

**<font color=#1a73e8>作者：</font>** Yue Zhao, Jiate Li, Li Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Organizations make claims about their AI agents: a person approves every external email, every action is logged, an evaluation shows the agent is safe to deploy. Article 12 of the EU AI Act requires high-risk systems to allow the automatic recording of events but does not say which records settle a given claim. The position is one sentence: to be checked, a claim about an agent must first name its policy, its scope, the records that would settle it, and who writes them. Adapting the preconditions of an assurance engagement, we call a claim auditable when these elements and a decision rule are fixed before any verdict and the records are obtainable. This extends the Policy Checkability dimension of our Auditable Agents framework from single actions to claims. Agents add three conditions: coverage by an independent record, authorization bound to each action's arguments, and completeness beyond integrity. Under an explicit model, we prove that support is impossible without each wherever its hypotheses hold. A claim-check table applies the method to six common claims, anchored in current NIST, IETF, and OWASP drafts. A worked case follows one claim through five evidence states. We close with a practice box and steps for operators, buyers, auditors, and standard setters.

---


### 109. [Protective Perturbations Must Survive the Resize: Scale-Robust Image Immunization against Malicious Editing](https://arxiv.org/abs/2610.07464)

**<font color=#1a73e8>作者：</font>** Zhongliang Guo, Yan Lin, Yifei Qian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Protective perturbations aim to stop malicious instruction-guided editing of personal photos, but they are optimized and evaluated at the editor's working resolution, whereas shared photos have 10 megapixels or more and editors first downscale them by an unknown factor. We model this resize as a frequency-selective channel. In this model, a perturbation computed at the native resolution decays with the downscaling factor and is weak even without a resize, and a perturbation computed at a fixed working resolution protects only a window of scales. The best worst-case protection over an unknown range of scales degrades only logarithmically with the width of the range, and averaging over scales does not reach it. Guided by this analysis, we propose SRIM, which samples a grid of anchor scales covering the whole range, with weights that favor the currently weakest scale, at the cost of standard expectation over transformation. On full-resolution photos of 9 to 30 megapixels and downscaling factors from 2 to 8, SRIM raises the worst-case disruption of FLUX.2-klein edits from 0.192 LPIPS, attained by the strongest published protection, to 0.463. At equal visibility, it roughly doubles the protection. The same protected photos also protect against the 9B model and against FLUX.2-dev, with worst cases of 0.450 and 0.386 against at most 0.184 for published protections, and SRIM leads on InstructPix2Pix as well.

---


### 110. [Efficient Multimodal Inference through Adaptive Acquisition and Sequential Fusion](https://arxiv.org/abs/2610.07466)

**<font color=#1a73e8>作者：</font>** Payal Mohapatra, Haodong Yang, Yueyuan Sui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal systems often encode every available input, even when a subset suffices for prediction. Adaptive acquisition can reduce this cost by using predictions from incrementally fused evidence to decide which modality to encode next and when to stop. However, sequential fusion makes these predictions order-dependent, so decisions based on them may need to distinguish factorially many histories of the same acquired set. We introduce SemARC, which couples a Sequential Modality Aggregator (SeMA) with an Adaptive Runtime Controller (ARC) and uses acquired evidence to select each modality before its encoder runs. SeMA executes only selected encoder and fusion branches, updates a fixed-size state, and predicts after each acquisition without recomputing earlier branches. We supervise every acquisition prefix under randomized modality subsets and orders to encourage consistent predictions across acquisition orders. ARC combines a set-dependent marginal-utility prior with residual fitted-Q learning to select the next available modality or stop, without inspecting unacquired inputs or retaining acquisition order. Across six multimodal classification datasets and eleven baselines, SemARC achieves 3.2% higher macro-F1 and 61.4% lower total inference GFLOPs on average relative to each dataset's most accurate baseline. End-to-end latency falls by 44.0% across GPU and CPU and by 47.2% on Android INT8 relative to the fastest measured baseline, on average. Under varying runtime modality missingness, SemARC still skips available modalities, matching or exceeding the best baseline macro-F1 in 21 of 24 conditions with 14.8% lower total GFLOPs on average. SemARC thus offers a practical path toward efficient multimodal inference across heterogeneous devices.

---


### 111. [Adapting to Changes in Agent Behavior via Finite-Depth Policy Sensitivity](https://arxiv.org/abs/2610.07475)

**<font color=#1a73e8>作者：</font>** Lan Shi, Daigo Shishika, Xuan Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adapting a reinforcement learning policy to changes in another agent's behavior typically requires a large amount of new interaction data. Policy sensitivity provides a first-order prediction of how a locally optimal policy changes with a behavioral parameter, but its computation requires second-order derivatives whose effects propagate across future interactions. We develop a finite-depth framework to estimate this sensitivity by approximating the policy Hessian and mixed derivative using information from a reference environment. The method features an adjustable propagation depth which determines where derivative propagation along the trajectory is truncated. We characterize the derivative contributions omitted by finite-depth propagation and derive truncation-error bounds for the approximated derivatives and resulting policy sensitivity. The bounds are nonincreasing with propagation depth and vanish at full-horizon propagation. Using a belief-driven pursuit-evasion game as a validation scenario, the proposed method generally achieves lower derivative-estimation errors as the propagation depth increases and outperforms the baseline methods in both estimation accuracy and policy adaptation. The sensitivity-based initialization improves zero-shot return over direct transfer, and also shows advantages for the subsequent fine-tuning in the target environment.

---


### 112. [Robust Importance Sampling for Rare Events via Constrained Gaussian Mixtures](https://arxiv.org/abs/2610.07485)

**<font color=#1a73e8>作者：</font>** Paweł Lorek, Rafał Nowak, Rafał Topolnicki 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study estimating rare-event probabilities $I = \mathbb{P}(g(\mathbf{X}) > \gamma)$ with $\mathbf{X} \sim \mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ and general $g : \mathbb{R}^d \to \mathbb{R}$. We address this problem through importance sampling, and propose a framework that substantially improves efficiency and robustness over baselines such as crude Monte Carlo, adaptive cross-entropy, variational-inference-based methods (including reverse- and forward-KL approaches), as well as Safe-ICE, Subset Simulation, and Sequential Monte Carlo, drawing on ideas from both rare-event estimation and cross-entropy optimization. The key contribution has two parts: first, we separate the problem into coverage, to overcome the cold-start barrier, and fitting, to refine proposals once a meaningful signal is available; second, we constrain the final GMM proposal so that it has finite importance-sampling variance (since coverage alone is not sufficient -- without safeguards, importance sampling may still suffer from infinite variance). Together, these ingredients yield expressive proposals; finite variance does not by itself guarantee practical stability at a fixed sampling budget. Extensive experiments demonstrate substantial variance reduction, strong robustness across diverse benchmarks, and favorable cost--efficiency trade-offs, with the proposed approach often outperforming these baselines, particularly in high-dimensional and multimodal settings where competing methods frequently become unstable or fail. Our code is available at this https URL.

---


### 113. [Deep Defence on Wheels: A Dual Intrusion Detection System Architecture for Comprehensive In-Vehicle Network Security](https://arxiv.org/abs/2610.07489)

**<font color=#1a73e8>作者：</font>** Shashwat Khandelwal, Shanker Shreejith  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Increasing connectivity to the outside world and the lack of inbuilt security mechanisms have made legacy intra-vehicular networks vulnerable to cyberattacks. Initial research focused on maximising detection accuracy for known and unknown attacks, often using large, full-precision machine learning models. However, embedding IDSs into vehicular electronic systems also requires low detection latency, energy efficiency and minimal electronic control unit (ECU) resource overhead to process about 2,000 CAN frames/s. Lightweight models must balance accuracy with these deployment constraints. We propose a dual IDS framework comprising supervised and unsupervised learning-based solutions, each optimised for real-time, resource-constrained automotive platforms. A quantised LSTM-based IDS (QLSTM-IDS) achieves over 99.9% detection accuracy for DoS/Flooding, Fuzzing and Spoofing/Malfunction attacks using a single model architecture evaluated on two widely used datasets. The model is trained using the Brevitas quantisation-aware training library, transformed into a dataflow accelerator with custom blocks compatible with AMD's FINN toolchain, and synthesised using Vitis HLS. Complementing this, an 8-bit quantised convolutional autoencoder-based IDS (QCAE-IDS), quantised using AMD's Vitis-AI toolchain, detects previously unseen anomalies that alter CAN-ID sequence patterns with over 99% accuracy. An integration architecture enables both models to operate on a single FPGA, bridging the network interface IP and processing system to minimise software overhead. QLSTM-IDS achieves 0.25 ms inference latency and 0.8 mJ energy consumption per message, while QCAE-IDS achieves 0.42 ms and 1.1 mJ per block. Both solutions are deployed and evaluated on the ZCU104 SoC (XCZU7EV FPGA), demonstrating a flexible hardware/software co-design for real-time detection of known and unknown attacks on high-speed CAN buses.

---


### 114. [Who Bears the Burden? Learning Responsibility for Shared Constraints in Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2610.07491)

**<font color=#1a73e8>作者：</font>** Xiaoyang Cao, Jingqi Li, Zhe Fu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When multiple agents share a cost budget, a common Lagrange multiplier can enforce the aggregate constraint but does not determine how its penalty should be allocated across agents. Uniform penalties ignore heterogeneity in the rewards agents sacrifice, while agent-specific multipliers may still rely on the same aggregate cost signal. We introduce Lagrangian Responsibility Allocation (LiRA), which learns each agent's share of a common multiplier by optimizing social welfare over a finite training horizon. The multiplier enforces the aggregate budget, while responsibility shares redistribute its influence without modifying the original rewards or constraints. For convex games under standard regularity conditions, varying these shares induces a smooth family of normalized generalized Nash equilibria in which active constraints remain at their budgets while welfare varies. To optimize responsibility before convergence, we derive a welfare gradient that accounts for both learning updates and the induced change in data distribution. Across CityLearn, MABIM, Harvest, and MetaDrive, spanning 3 to 400 agents, LiRA improves average social welfare by up to 29% over uniform and agent-specific multiplier baselines. Grid and driving costs remain within budget, inventory violations decrease, and Harvest makes more effective use of available budget.

---


### 115. [Does Muon Need Fine-Grained Spectral Shaping?](https://arxiv.org/abs/2610.07497)

**<font color=#1a73e8>作者：</font>** Meher Chaitanya, Tianyi Zhou, Aristides Gionis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Muon combines current and past gradients into matrix momentum. For $M=U\Sigma V^\top$, the idealized polar update $Q=UV^\top$ gives every singular direction the same weight. We refer to this as the flat profile. Several recent optimizers replace this flat profile with fine-grained spectral maps that give each direction its own gain. We ask how much of this spectral detail a Muon update needs. Our spectral diagnostics show that approximately $94$--$97\%$ of measured singular modes lie below an estimated noise edge, yet collectively align positively with a reference gradient.
We introduce BulkBoost, a two-band spectral reweighting framework with fixed-rank and noise-calibrated variants. The latter uses split-minibatch gradient differences to calibrate a Marchenko--Pastur reference edge for Muon's Nesterov input, separating the bulk below the edge from the spikes above it. Both variants increase the bulk's relative weight through one shared gain while preserving the Frobenius norm of each matrix's unreweighted direction. For a fixed partition, our theory gives the first-order condition under which moving weight toward the bulk lowers the loss. It also quantifies the fraction of the maximal first-order improvement rate, over all per-mode reallocations, that two bands can capture. Across 30 continued-pretraining settings spanning Pythia-14M to 410M and six corpora, two-band reweighting is competitive with the fine-grained power-law profile of Freon and outperforms Spectra. Measured against Muon's flat profile, Freon reduces final loss by $0.022\%$ of the pre-adaptation loss on average, whereas the two-band variants achieve reductions of $0.073$--$0.147\%$. These observations suggest that useful departures from the flat profile are surprisingly low-dimensional: a single bulk-to-spike gain captures at least as much benefit as the fine-grained spectral profiles.

---


### 116. [Source-Learned Reliance for Selective Test-Time Adaptation of Multimodal Time Series](https://arxiv.org/abs/2610.07499)

**<font color=#1a73e8>作者：</font>** Payal Mohapatra, Yueyuan Sui, Haodong Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal wearable systems must remain reliable when sensor streams become noisy or unavailable. Existing multimodal test-time adaptation (TTA) methods often assess reliability online, but cross-modal agreement can be misleading when sensors measure different physical processes, and evaluating alternative modality configurations adds inference cost. We propose CARAT, which decouples model reliance from runtime corruption detection to guide omission or attenuation, amortizing reliance estimation through source training. An asymmetric modality-dropout curriculum prepares a missingness-resilient backbone for omission and derives a frozen, backbone-specific reliance proxy from windowed input-projection gradient norms. At deployment, a lightweight one-class detector flags suspect streams, and the proxy guides a joint choice between replacing the suspect set with the backbone's trained missingness symbol and attenuating its representations before fusion, without candidate-subset evaluation. Across four wearable datasets, five corruption types, three backbones, and eight TTA baselines, CARAT achieves the highest overall macro-F1 and best mean rank (2.42), exceeding EATA, the strongest baseline, by 1.58 F1 points across 12 equally weighted dataset-backbone settings. Across five profiled configurations, CARAT uses 9.49% fewer GFLOPs and updates 47.82% fewer parameters than EATA. A pattern also emerges across sensing regimes: multimodal TTA methods such as PTA are competitive on IMU-dominated homogeneous datasets, whereas unimodal TTA methods like TENT and EATA match or exceed it on heterogeneous datasets. These results position CARAT as a practical default to wearable TTA, offering competitive robustness with modest computational requirements and benefits that vary across backbones and dataset regimes.

---


### 117. [MARS: Multi-resolution Adaptive Routing for Sequential Recommendation](https://arxiv.org/abs/2610.07505)

**<font color=#1a73e8>作者：</font>** Ming Yin, Sixun Dong, Yudong Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-history recommenders often compress each user's history into a compact, candidate-independent memory that is cached and reused to score large candidate pools. We show that real user histories exhibit multi-scale semantic structure, with short-lived intent, medium-term interests, and long-term preferences coexisting in one sequence, and that monolithic cached memories preserve these scales unevenly: linear probes recover recent and mid-range content far worse than long-range content. We call this failure mode \textit{temporal aliasing}. We propose \textbf{MARS}, a multi-resolution user memory that writes the full history into recurrent state tracks anchored to different half-lives, and a sparse routing reader that materializes compact seed memories by selecting the relevant temporal resolutions for each seed, preserving fixed-size candidate scoring. MARS outperforms strong baselines on three public datasets, with gains that grow with history length. Component-matched ablations with paired tests show that temporal diversity and selective routing each contribute beyond what hard-window memories or added capacity provide. The advantage of MARS over its interface-matched baseline also widens after within-user behavioral shifts, at about $1.02\times$ that baseline's warm-cache serving latency for $1{,}000$ candidates per user.

---


### 118. [Jarvis: A Proactive Speech Agent for Multi-Party Conversations](https://arxiv.org/abs/2610.07506)

**<font color=#1a73e8>作者：</font>** Seunghyun Oh, Hirotaka Hiraki, Shuyue Stella Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Speech agents are reactive and dyadic: they speak when spoken to, and to one person at a time. We ask what it takes for a speech agent to instead take part in a conversation among several people and speak up only when it can help. We introduce Jarvis, a real-time proactive speech agent that audibly participates in multi-party human conversations. Grounded in a document shared beforehand, Jarvis follows the discussion and intervenes when the group misses or misstates a fact and does not correct itself within a few turns. We make three contributions: a problem setting based on epistemic breakdowns that makes proactive intervention measurable, realized as CHI-180-proactive, a synthetic multi-party dataset seeded with known gaps, errors, and self-corrections; a proactive backbone that harnesses a small, open-weight model with deterministic checks and grounds every claim in a source sentence; and interaction techniques for taking the floor in live speech and showing the cited evidence on screen. On CHI-180-proactive, Jarvis is correct on most events it addresses and stays silent 97% of the time when the group resolves an issue itself. A live study with 23 participants confirms these trends with real-time interventions.

---


### 119. [The Relationship Between Blood Pressure and Self-Reported Stress During Sound-Based VR Relaxation Videos](https://arxiv.org/abs/2610.07507)

**<font color=#1a73e8>作者：</font>** Md Alamin Hossain, M. Rasel Mahmud  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Virtual reality (VR) relaxation environments are increasingly proposed as accessible tools for stress management, yet the physiological correlates of self-reported stress during VR exposure remain unclear, particularly for blood pressure (BP). We conducted a within-subjects study (N = 18) in which participants viewed relaxing 360-degree videos, grouped into four sound-design categories, such as videos with rhythmic (RHYT), aperiodic (APRD), continuous (CONT), and low-ambient (LOWE) sound through an HTC Vive Focus Vision headset. Systolic (SYS) and diastolic (DIA) BP were recorded after each category using an Omron 3 Series monitor, and self-reported stress was collected via a 0-100 Visual Analogue Scale (VAS) with fixed intervals. While overall BP did not differ significantly across sound categories, self-reported stress did (Friedman chi-square(4) = 12.07, p = .017), with rhythmic sound eliciting significantly lower stress than aperiodic and continuous sound. Critically, DIA, but not SYS, correlated significantly with self-reported stress across conditions (r = .31, p = .003). This suggests that DIA may be a more sensitive physiological indicator of subjective stress than SYS in short VR exposures. We discuss implications for designing and evaluating VR mental health interventions and the value of low-cost physiological sensing alongside self-report.

---


### 120. [Not What a Child Expressed: Auditing the Sign-to-Text Safety Interface in Child-Facing AI](https://arxiv.org/abs/2610.07519)

**<font color=#1a73e8>作者：</font>** Muhammad Rafiullah Memon, Viet Vo, Wanlun Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic sign language translation (SLT) has entered consumer products, turning American Sign Language into English text for dictation, messaging, and queries put to a conversational assistant. Child-facing AI and platform trust-and-safety tooling decide on text, using filters on minor accounts and grooming classifiers that score chat messages. A signing child who uses SLT therefore reaches these safeguards through a translation. We found no publicly documented system in which the two have been jointly evaluated, and the leading deployed SLT model was neither trained nor formally evaluated on signers under 18. Errors that alter negation, participant roles, secrecy, urgency or help-seeking could change a safety decision without disturbing fluency. This paper proposes a Deaf-informed pre-deployment audit of that boundary, with a failure taxonomy, a sanitised scenario schema, four comparison conditions, and four outcome measures. Auslan is the planned first case study.

---


### 121. [Grounding What Shapes the Plan: Rethinking Groundedness for Physical Intelligence in Autonomous Driving](https://arxiv.org/abs/2610.07521)

**<font color=#1a73e8>作者：</font>** Minkyoung Cho, Zewei Zhou, Wenhao Ding 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Driving models increasingly ground reasoning in causal relations, spatial structure, perceptual evidence, and predicted futures. These advances make reasoning more faithful to the driving scene, but leave a fundamental question unresolved: what should groundedness mean when the model ultimately outputs an action? Correctly grounded reasoning does not, by itself, ensure desirable driving outcomes. We introduce GroundAct, which starts from a simple premise: driving unfolds through physical entities and their interactions. Entities therefore become the unit of grounding; a lightweight reference token keeps each selected entity's continuous state addressable through symbolic reasoning; and only the referenced entities' interactions with the evolving proposal correct the plan. The result is an explicit path from what reasoning grounds to what the plan does, which we call grounded planning. To assess its practical value, we evaluate GroundAct in both open- and closed-loop settings. GroundAct shows strong open-loop planning across normal, out-of-distribution, and safety-critical scenarios, with closed-loop results extending this evidence to driving in simulation.

---


### 122. [PAIR: Perceptual Affective Inference and Regulation in a Real-Time Multimodal Conversational Agent](https://arxiv.org/abs/2610.07523)

**<font color=#1a73e8>作者：</font>** Kexin Quan, Zijian Ding, Jiaye Yong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Sustained emotional support requires generative agents to connect momentary emotion inference and regulation with continuity across encounters. We present PAIR (Perceptual Affective Inference and Regulation), a real-time multimodal agent that reconstructs how an event is appraised into an emotional state. Appraisal scaffolds produce a valence-arousal-dominance estimate and select regulation guidance, delivered through conversation with coordinated speech, color, and avatar cues. Rolling memory carries context across sessions, and the scaffold re-runs after guidance. In a 14-day deployment with 19 participants, 1,093 sessions paired initial and post-guidance estimates with unanchored self-reports. Initial valence reached MAE 1.20 on the 9-point SAM scale (r=.68), dominance reached MAE 1.30, and arousal showed weak agreement even after coarsening. Self-reported emotional change varied with initial state, with the largest valence increases in sessions that began at negative valence. Perceived understanding was associated with greater valence increase and showed little correspondence with numerical prediction error. Over two weeks, helpfulness increased while input shortened; interviews traced personalization and companionship to relevant recall, context updates, and familiar dialogue. These findings connect inference accuracy to conversational and temporal patterns of support through per-event, first-person evaluation.

---


### 123. [Targeted search shows that random-device testing underestimates worst-case error in a simulated wave-based neural operator](https://arxiv.org/abs/2610.07529)

**<font color=#1a73e8>作者：</font>** Samrendra Roy, Jason Yoo, Souvik Chakraborty 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wave-based processors promise fast, energy-efficient Fourier layers for neural operators. They are usually validated on randomly sampled devices, but using them requires knowing how large their error can become under fabrication and alignment variation. In a stylised numerical case study, a hybrid Fourier neural operator runs its four spectral layers on simulated coherent 4f processors with 32 toleranced knobs, whose half-widths are representative rather than calibrated. For 120 models (four tasks, six training methods, five seeds), we compared the worst of N random in-spec devices with a searched one. On a deterministic simulator with one frozen draw of the random static errors, the searched device's held-out error was 1.08-3.10 times the maximum over 200 Monte Carlo devices and 1.06-2.71 times that over 1000. With 20 fresh static draws, it still exceeded the maximum over 200 random devices in 116 of 120 models. Under uniform sampling, the probability of drawing such a device is at most 0.37% per model (two-sided 95% Clopper-Pearson), which says nothing about how large its error is. The gap persisted with uniform or Sobol' sampling at the search's budget, shared knobs, a second crosstalk model, box scales of 0.25-2 and a pixel-level device model. Models trained only with random static errors reached 3.7-39.9 times their nominal error on searched devices, and fine-tuning on random and gradient-searched devices gave the lowest searched error of the six in all 20 task-seed pairs. For two heat-exchanger quantities, a search targeted at each exceeded the worst of 1000 random devices in all 39 models, and hence the Wilks 95/95 limit (worst of 59). For the mean pressure of 11 models, no random device exceeded a 1% error threshold, but the searched device did. Random testing estimates how often errors exceed a threshold; worst-device search gives a lower bound on how large they can be.

---


### 124. [BVI: Lightweight, Data-Centric Blockchain-Based Verification of Identity Claims](https://arxiv.org/abs/2610.07531)

**<font color=#1a73e8>作者：</font>** Harshith Pothapala, Gagandeep Singh, Samudi Amarasinghe 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A person who answers an unexpected call claiming to come from a bank has no way to check the claim. Australian text messaging has labelled a message as unverified when the sender identifier is not registered since 1 July 2026, but a voice call still arrives with nothing behind it, and voice cloning has removed the last cue recipients relied on. We present BVI, which answers one question for the recipient: did the calling party prove it holds a credential a registered organisation issued for this call? BVI keeps the organisational record, its authorised channels and its revocation state on a public ledger in a directly queryable form, and puts all decision logic in the handset, which performs eleven checks, pays no transaction fee and holds no full-chain state. We define ten attack classes plus the case in which revocation cannot be resolved, compare them in a 10-by-4 coverage matrix spanning BBCA, the content digest, the detector and composed BVI, and run 27 automated scenario tests against isolated Hardhat fixture states of the BVI contract; all 27 pass. For media substitution and synthetic speech, the contract tests validate commitment and gating properties rather than claiming detector accuracy. The mandatory per-session anchor costs about 91.5k gas and is invariant in call duration and hop count; each participating intermediary additionally contributes one optional attestation write. In a 20,000-session-per-cell path simulation, at one quarter carrier participation BVI detects 20.6 per cent of randomly located in-path rewrites versus 0.1 per cent for the every-hop comparison, while identity and content evidence remain available even when path evidence is indeterminate. We also quantify the throughput ceiling of the anchoring design.

---


### 125. [Preserving Unstable Modes Through Inverse Dynamics in JEPA World Models](https://arxiv.org/abs/2610.07540)

**<font color=#1a73e8>作者：</font>** Leonardo F. Toso, Yann LeCun, James Anderson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Robotic systems often exhibit unstable modes, along which small perturbations and disturbances can cause unbounded growth unless corrected through feedback. Controlling such systems from high-dimensional visual observations requires representations that preserve these modes. Joint-embedding predictive architectures (JEPAs) provide a natural framework for learning such representations and their dynamics from visual data. However, we demonstrate that next step prediction combined with anti-collapse regularization does not guarantee that controllable unstable modes are preserved: the training loss can be minimized while these modes are collapsed, making stabilization from the learned representation impossible. To address this, we augment world-model training with an action reconstruction objective (i.e., an inverse dynamics loss) that encourages control-aware representations, namely, visual representations that preserve crucial features for control. We prove that exact action reconstruction makes the encoder injective on the finite-horizon reachable subspace. Thus, the encoder cannot discard any state direction reachable by an action sequence within $H$ steps. Moreover, we show that, as $H$ grows, the dominant eigenspace of the finite-horizon controllability Gramian converges to the controllable unstable subspace. We establish our theoretical results for linear systems and demonstrate empirically that our findings extend to nonlinear visual control tasks (CartPole, Walker2D, and PointMaze), highlighting the benefits of control-aware representation learning.

---


### 126. [Quality-Aware Self-Correcting Speech Translation on an Edge Device](https://arxiv.org/abs/2610.07545)

**<font color=#1a73e8>作者：</font>** Zubair Ajmal Farooq, Diptesh Kanojia  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a fully offline speech-to-speech translation pipeline that runs on a Jetson Nano (4 GB) and corrects its own weak translations without retraining. A Whisper-tiny ASR feeds an Opus-MT translator; multilingual BERT cosine similarity acts as a Quality Estimation (QE) gate, triggering a secondary-pass correction when confidence falls below a pre-defined threshold $\tau$. We compare three correction methods: QE reranking (M1), Minimum Bayes-Risk decoding (M2), and constrained beam search (M3). On 1,012 FLORES-200 sentences (English-Spanish), M2 at $\tau=0.90$ produces statistically significant improvements over greedy decoding on BLEU (+0.67, p<0.001), ChrF (+0.51, p<0.001), and COMET (+0.0020 at N=3, p=0.002); M1 yields no significant gains, and M3 is significantly worse than baseline (p>0.99). Our central finding is that QE functions effectively as a gate but poorly as a ranker: removing the QE model from candidate selection (M1$\to$M2) does not hurt quality and frees 680 MB from the critical path. Using a gain-to-edit ratio adapted from the post-editing-effort literature, we further show that smaller candidate pools (N=3) yield more surgical corrections with better semantic adequacy, while larger pools (N=10) maximise lexical reward. We release the system and demonstrate live translation across six language pairs.

---


### 127. [Global Transport Couplings for Classifier-Free Guided Flows](https://arxiv.org/abs/2610.07555)

**<font color=#1a73e8>作者：</font>** Katarina Petrović, Zander W. Blasingame, Danyal Rehman 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimal-transport couplings have been shown to reduce training variance in unconditional flow models, but their role in conditional generation remains unclear. A natural approach constructs separate couplings for each condition, but this is impractical for large or continuous conditioning spaces found in modern image foundation models. We introduce Global Transport (GT), a global class-agnostic optimal-transport coupling, computed without class labels. GT can associate different conditions with different regions of the source noise, and consequently worsens performance without guidance. However, when combined with classifier-free guidance (CFG), GT consistently improves generation across domains, model scales, and sampling budgets. This reversal suggests that couplings for conditional flows should be evaluated both empirically and theoretically under the guided flow used at inference, rather than on unguided generation. We evaluate GT over both discrete class and continuous text conditioned image generation across model scales, and investigate how coupling choice alters guided trajectories. These results identify coupling design in the guided flow setting as a simple training time axis to improve performance without modifying existing architectures, samplers, or guidance mechanisms.

---


### 128. [Navigating Route Latent Space for Synthesizable Molecular Design](https://arxiv.org/abs/2610.07560)

**<font color=#1a73e8>作者：</font>** Tao Li, Tuan Vinh, Monika Raj 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Goal-directed molecular design has advanced rapidly, yet a substantial proportion of designed molecules remain difficult to synthesize in practice, limiting their real-world utility. Prior synthesizability-aware methods either project generated molecules back to synthesizable analogs that deviate from the intended target, or optimize directly in discrete synthesis spaces that lack a continuous landscape for efficient search. We argue that this limitation mainly comes from the search space rather than the optimizer. To address this, we propose RouteFlow, a framework that reformulates synthesizable molecular design as a search over a continuous route latent space, where each latent maps back to a complete synthesis route and synthesizability is inherently preserved. To navigate this space, we adopt reward-guided flow matching as an efficient sampler that steers toward high-property regions. Since reward optimization may push latents off the manifold of real synthesis routes, where decoding becomes unreliable, we further introduce a cycle-consistency mechanism to stabilize fine-tuning. Across 16 optimization tasks from Therapeutic Data Commons, RouteFlow achieves the best sample efficiency among synthesizability-aware baselines, with the best synthetic accessibility and the highest retrosynthesis success rate. Our results also confirm that the proposed cycle-consistency reliably keeps optimization on-manifold while improving target properties, supporting effective synthesizable molecular discovery.

---


### 129. [LARK: A Low-Cost, Accurate, Occlusion-Resilient, Kalman Filter-Assisted Tracking System for Image-Guided Surgery](https://arxiv.org/abs/2610.07561)

**<font color=#1a73e8>作者：</font>** George Sideris, Justin Cree, Andrew Stirling 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image-guided surgery (IGS) depends on accurate tracking of surgical instruments to provide real-time navigation relative to anatomical structures. Commercial stereo infrared trackers are accurate but prone to occlusion and cost-prohibitive for many settings. This work presents LARK, a multi-camera optical tracking system using commodity RGB hardware and multi-view redundancy and fusion. We develop and evaluate two complete tracking methods: multi-view monocular pose fusion and multi-view triangulation. Both methods are assessed under varying occlusion levels using a precision-machined grid and an anatomical head phantom, and compared against a gold-standard stereo infrared system. With five cameras and adaptive Kalman filtering, LARK achieves median target registration errors of 0.64 mm for point localization with triangulation and 0.73 mm for trajectory tracking with pose fusion on the machined grid. Camera-subset experiments show graceful degradation in adaptive pose-fusion accuracy as fewer views remain available. With tracking hardware costing under $1,000 USD, LARK provides a low-cost platform for image-guided surgery research. Hardware designs and software are publicly available at this https URL , and datasets at this https URL .

---


### 130. [Learning a Mixture of GFlowNets](https://arxiv.org/abs/2610.07562)

**<font color=#1a73e8>作者：</font>** Tiago da Silva, Amauri H. Souza, Salem Lahlou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning an ensemble of GFlowNets to sample from a discrete target distribution has become a common approach for achieving better state space exploration and convergence than that of a monolithic sampler. However, these methods often add a substantial runtime overhead to the base model, and their conceptual connection remains elusive. To address this, we first propose a general-purpose theoretical framework for describing a mixture of GFlowNets, which we specialize into continuously (CI) and discretely indexed (DI) collections. On the one hand, we show CI GFlowNets can be interpreted through the lens of a random features expansion, provably boosting the sampler's expressivity in graph-structured tasks and reducing learning instability via spectral shifting. On the other hand, we demonstrate DI GFlowNets encompass prior approaches for GFlowNet training and provide the foundation for the newly proposed Stratum-Conditioned (SC) GFlowNets. This method, which is inspired by the Doob's h-transform of Markov chains, decomposes the state space according to a prescribed modular function and restricts each component to sample from a distinct subset of it. Importantly, SC GFlowNets support centralized and component-wise embarrassingly parallel training, and we show both of them significantly speed up learning convergence and mode coverage without introducing any non-negligible extra computation.

---


### 131. [Complementary Feature Domains: Information Preservation Does Not Imply Predictive-Contribution Preservation](https://arxiv.org/abs/2610.07565)

**<font color=#1a73e8>作者：</font>** Timothy Oladunni, Farouk Ganiyu-Adewumi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Complementary Feature Domains (CFD) theory characterizes predictive value as a context-indexed contribution system induced jointly by representations and their realization family. We show that Shannon-information preservation does not imply preservation of this contribution system: an invertible representation transformation can leave target information unchanged while altering predictive contribution under a restricted decision family. We formalize the resulting transition through a CFD contribution defect that measures how contextual contributions change under controlled recoding. For bounded Lipschitz utility, we show that each coalition utility shift is bounded by the behavioral distance between the attainable action sets before and after recoding; consequently, every contextual contribution defect is bounded by the sum of the corresponding coalition incompatibilities. Exact behavioral closure yields invariance, while increasingly accurate compensation yields restoration. A controlled ECG experiment illustrates the mechanism: a nonlinear bijective recoding preserves the information in a frozen time-frequency representation but changes accuracy under a fixed affine learner; applying the exact inverse restores all tested coalition accuracies. The result separates information preservation from realization-dependent contribution and provides a quantitative transition law for multi-representation prediction.

---


### 132. [AIMS: Anchor-Integrated Multi-View Synthesis for Scalable Novel View Rendering](https://arxiv.org/abs/2610.07566)

**<font color=#1a73e8>作者：</font>** JooHyun Park, HanYoung Jang, HyeongYeop Kang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward novel view synthesis methods achieve strong generalization from posed multi-view inputs, but scaling them to large input view sets remains challenging. Transformer-based approaches that jointly process all input-view tokens incur rapidly increasing computation and memory as the number of views grows, while simple view subsampling discards potentially useful observations. We introduce Anchor-Integrated Multi-View Synthesis (AIMS), a scalable framework that decouples the number of available observations from the number of views processed by the global synthesis model. AIMS selects a fixed set of spatially distributed anchor views using farthest point sampling, groups nearby observations around each anchor, and uses a lightweight learnable integrator to fuse their information into enriched anchor representations. This allows additional observations to contribute to synthesis while keeping the downstream global view budget fixed. Evaluations on RealEstate10K and ScanNet demonstrate a favorable quality--efficiency trade-off against transformer-based and Gaussian-based baselines. AIMS achieves 29.41 dB and 17.73 dB PSNR on the two datasets, respectively, with rendering averaging 7.24 ms per view.

---


### 133. [CETUS: How Far Do Representations Trained on Earth Transfer to Cassini SAR of Titan?](https://arxiv.org/abs/2610.07576)

**<font color=#1a73e8>作者：</font>** Kevin Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cassini synthetic aperture radar (SAR) images reveal the dunes, plains, and lake basins of Titan, providing an instance of representations learned from Earth imagery for planetary terrain classification. Cross-domain Evaluation of Earth-to-Titan Transfer Using SAR (CETUS) compares features from DINOv2, DOFA and CROMA with classical image measurements and features from an untrained vision transformer on the U.S. Geological Survey's Cassini SAR mosaic. The classifiers learn terrain labels from an expert geomorphological map and predict those labels in geographically separate Titan regions. Under logistic regression settings, pretrained encoders achieve higher mean macro F1 than the combined classical features. Encoder rankings change when feature scaling, optimization, and regularization change together. Further training on Titan improves DINOv2 performance, degrades DOFA performance, and leads to mixed results for CROMA under the tested settings. Architectural and input processing differences prevent these comparisons from isolating the effect of pretraining. Classifier fitting and performance on individual terrain classes matter when assessing representation transfer for planetary mapping. Since the map draws partly on the same radar observations, the scores measure agreement with expert interpretation.

---


### 134. [Cooperating with Future Collaborators: Multi-Agent RL under Staggered Participation](https://arxiv.org/abs/2610.07578)

**<font color=#1a73e8>作者：</font>** Jianglin Qiao, Siyi Hu, Thien Hoang Nguyen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In cooperative Multi-Agent Reinforcement Learning (MARL), agents are often trained under concurrent participation, while in many tasks some agents act earlier and leave task-relevant information that becomes useful to agents participating later. We study this setting as staggered participation (SP), which introduces a cross-time, cross-agent learning dependency because an early action may affect the return through the information it provides and the later policy that uses it. Learning under SP therefore requires both identifying what information is useful for future decisions and learning how later agents should use it. We propose Staggered Participation Learning (SPL), a training-time augmentation that addresses these two parts with prospective acquisition supervision for earlier agents and outcome-supervised receiver learning for later agents. We evaluate SPL across multiple policy-based MARL backbones, environments, and staggered-participation patterns. Across 60 MPE/RWARE backbone setting comparisons, SPL achieves higher observed mean task completion in every case, with an average difference of 14.1%. The gains also extend to eight-agent teams and a physics-based UAV-UGV environment in Isaac Lab, providing evidence across algorithmic, temporal, and embodied settings.

---


### 135. [Representation Bias, Correction Transfer, and Resolution Sensitivity in Three-Dimensional Mitochondrial Morphometry](https://arxiv.org/abs/2610.07582)

**<font color=#1a73e8>作者：</font>** Farouk Ganiyu Adewumi, Timothy Oladunni  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Quantitative imaging pipelines can produce precise but systematically different measurements of the same object. We present an empirical reliability assessment of three-dimensional mitochondrial morphometry that connects representation bias, a controlled processing intervention, correction transfer, and resolution sensitivity. Using 2,720 development objects from the 3D Mitochondria Shape Library for Optical Microscopy, we find that occupancy-derived volumes exceed reference mesh volumes by 3.665% on average despite an intraclass correlation coefficient of 0.994. Boundary analysis identifies an outward label displacement of 0.00304 normalized units. In a controlled label-pipeline reimplementation, removing the depth offset reduces volume error in all 55 analyzed objects by a mean of 1.57 percentage points, approximately 45% of mean reproduced inflation; the source of the remainder is not isolated. A frozen regression using occupancy-derived features reduces median absolute percentage error from 3.481% to 0.664% in 2,728 previously unused objects from the same resource. However, its calibrated error bound covers only 92.1% overall and 49.2% in a low-occupancy subgroup, demonstrating that accuracy and uncertainty transfer must be evaluated separately. In 550 rat-cortex objects from the MitoEM resource, coarsening in-plane spacing from 8 to 24 nanometers changes median surface area by minus 10.60% and sphericity by plus 11.76%, despite a rank correlation of 0.994. These results provide quantitative checks for distinguishing processing-induced descriptor changes from candidate biological differences, without establishing biological invariance or cross-source correction transfer.

---


### 136. [Mechanistic Interpretability of Atmospheric Rivers in GraphCast](https://arxiv.org/abs/2610.07583)

**<font color=#1a73e8>作者：</font>** Madelyn Mathai, Timothy B. Higgins, Kevin M. Grise 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While AI weather models now rival operational forecasts, how they represent the atmosphere internally remains an open question: feature attribution reveals which input patterns matter, not what the model computes or how it combines information internally. We train sparse autoencoders (SAEs) on GraphCast to uncover its learned concepts, using atmospheric rivers as our phenomenon of focus. Both standard and Matryoshka SAEs show GraphCast computes atmospheric river intensity, measured by integrated vapor transport (IVT), as a stable internal variable, despite IVT being neither an input nor a target. In contrast to the unstructured concept retrieval of the standard SAE, the Matryoshka SAE orders concepts by importance and exposes their relations. Atmospheric river concepts persist across depth and direct interventions confirm causality. This method offers a way to find internal variables and determine which of them the model actually relies on, which is a prerequisite for asking whether those variables remain meaningful as the phenomenon changes under a warming climate.

---


### 137. [REViT-v2: Hierarchical Windowed Roto-reflection Equivariant ViT for Equivariant Feature Extraction](https://arxiv.org/abs/2610.07585)

**<font color=#1a73e8>作者：</font>** Sheir A. Zaheer, Jihwan Moon, Chan Y. Park  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a scalable roto-reflection-group-equivariant vision transformer based on windowed group-convolutional self-attention and a hierarchical feature architecture. We demonstrate that our approach can be scaled to group-equivariant vision transformers (ViTs) with millions of parameters and large datasets with practically sized images, i.e., ImageNet. The code and pretrained weights for the proposed Hierarchical Windowed Roto-reflection Equivariant ViTs (REViT-v2) are available at this https URL.

---


### 138. [Recurrent Looped Transformer](https://arxiv.org/abs/2610.07591)

**<font color=#1a73e8>作者：</font>** Yifan Zhang, Jichen Feng, Shihan Qin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> State tracking requires an update at every input, but the depth a Transformer applies to each token is fixed regardless of sequence length. We introduce the Recurrent Looped Transformer (RLT), which splits its layers between a parallel causal encoder and a recurrent decoder. At each token, the decoder merges the encoder output with the previous token's final decoder state, so the computation path grows with sequence length at a fixed per-token cost. On six algorithmic tasks, we compare five splits of eight layers with an eight-layer Transformer over three seeds. Trained on at most 40 bits, two RLT splits generalize parity to 256 bits with 100% accuracy in every seed, while the Transformer stays at chance. On swap-based $S_5$ permutation tracking at eight times the training length, RLT reaches 97% final-state accuracy versus under 1% for the Transformer, and accuracy increases with decoder depth. On modular arithmetic beyond the training lengths, RLT reaches up to 93% versus 33% for the Transformer. Ablations show that these gains depend on the feedback: removing it drops parity and swap-based $S_5$ to chance at every split. Updating the feedback once per four-token chunk lets known tokens in a chunk run in parallel and keeps 64-bit parity at 99%, while permutation tracking depends on per-token feedback: chunking lowers length-64 swap-based $S_5$ from 100% to 20%.

---


### 139. [Beyond Scalar IoU: Structured Verification from Rollout Groups for Video Temporal Grounding](https://arxiv.org/abs/2610.07601)

**<font color=#1a73e8>作者：</font>** Youngjae Cho, Won Young Jhoo, Jongsuk Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) provides a natural framework for adapting pretrained models to video temporal grounding, where generated temporal intervals can be scored directly against ground truth intervals. Yet existing overlap verifiers typically score each rollout independently, leaving the joint structure of the rollout group unused. We introduce SUTURE, which conditions verification on the rollout group and exploits its structure at two complementary scales: disagreement across rollouts controls how strongly the target is reweighted, while coverage at each position determines where reward mass is redistributed. We show that the resulting verifier admits an exact decomposition into the standard IoU term and a covariance correction determined by the rollout group. A local gradient diagnostic finds a preference for responses covering relatively less supported target regions in the analyzed groups. Across five temporal grounding benchmarks, SUTURE improves grounding performance at every reported IoU threshold. Its trained policy also shows less video-start anchoring in reasoning traces: for later events, the first temporal mention more often overlaps the annotated target. Together, these results show that the joint structure of a rollout group can support a more informative temporal verifier.

---


### 140. [Emoception: Selective Affective Layer Fine-Tuning of Video Vision Transformers for Player Arousal Change Recognition From Gameplay Footage](https://arxiv.org/abs/2610.07603)

**<font color=#1a73e8>作者：</font>** Yi Xia, Ibrahim Khan, Mury Fajar Dewantoro 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This article proposes Selective Affective Layer Fine-Tuning (SALFT), an efficient adaptation framework for Video Vision Transformers in player arousal recognition from gameplay. To bypass computationally expensive full fine-tuning, SALFT introduces a selection criterion based on the L2-norm change in layer parameters after brief adaptation, directly measuring representational shifts and providing a more stable basis than gradient-based alternatives. Evaluated via five-fold cross-validation on the Arousal Video Game AnnotatIoN dataset, SALFT achieves performance comparable to full fine-tuning across all games without statistically significant degradation ($p>0.05$), while updating only $\approx$8% of parameters (over 92% reduction). Notably, in one game, SALFT consistently outperforms both full fine-tuning and the best baseline across all metrics and folds, reaching the theoretical minimum p-value (p=0.0625, exact two-sided Wilcoxon signed-rank test). In addition, we introduce an interpretability method to trace attention patterns, enhancing model transparency. These results establish SALFT as an effective and efficient approach for affective game computing.

---


### 141. [PhysLDM: Latent Diffusion for High-Fidelity Deformable Simulation](https://arxiv.org/abs/2610.07609)

**<font color=#1a73e8>作者：</font>** Yu Zhang, Xudong Xu, Xingang Pan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neural simulation of high-fidelity deformable bodies is a foundational challenge in computer graphics and physical AI. Long-horizon prediction for high-resolution 3D volumetric meshes is hard: autoregressive methods are susceptible to error accumulation, while direct multi-frame prediction at native resolution is computationally prohibitive. This motivates a compact spatiotemporal latent representation, which is largely unexplored for mesh-based volumetric physics. Meanwhile, it remains unclear whether deterministic regression or generative diffusion is the more appropriate predictive paradigm. To address these coupled challenges, we introduce PhysLDM, a unified latent-diffusion paradigm for one-shot volumetric deformable simulation. Its core is a holistic spatiotemporal VAE that avoids the "staircase" artifacts of standard temporal compression (as in common video VAEs), achieving ~2.48 mm reconstruction precision on meter-scale scenes at up to 78x token compression. Based on this reliable latent space, we systematically compare regression and diffusion methods. Our experiments uncover a key modeling insight: complex deformable dynamics are often chaotic, and in this regime deterministic regression tends to produce non-physical averages, whereas diffusion better models their distribution. Accordingly, we employ a latent diffusion model that effectively learns from the chaotic data to generate physically plausible trajectories. Trained purely kinematically on an Objaverse-scale dataset, a single PhysLDM generalizes zero-shot to unseen OOD datasets (GSO and Toys4K). Its differentiability further enables efficient solution of inverse problems and higher-order design optimization. To our knowledge, PhysLDM is the first high-fidelity spatiotemporal autoencoder and latent-diffusion paradigm for volumetric deformable dynamics, offering a scalable and robust approach to neural simulation.

---


### 142. [Hub for Outliers, Spokes for Inliers: Uniform Latent Space Construction for Dual-Mismatched Semi-Supervised Learning](https://arxiv.org/abs/2610.07610)

**<font color=#1a73e8>作者：</font>** Li Yuan, Yaxin Hou, Jiawei Tang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Semi-supervised learning typically assumes that labeled and unlabeled data share an identical class distribution and label space. However, this setting is often violated: unlabeled data may be imbalanced and contain unknown class samples, causing mismatches in both class distribution and label space. Such dual mismatch leads to majority classes dominating the latent space and unknown class samples being overconfidently misclassified, degrading feature discriminability and pseudo-label quality. To address this, we propose a hub-spoke latent geometry, where known classes are uniformly distributed around a central hub and each class forms compact clusters around its prototype, while the hub provides an anchor for a low-evidence region specifically designed for high-uncertainty unknown class samples. Integrated with an evidence-based classifier, this geometry ultimately enhances feature discriminability and uncertainty separation by mitigating majority-class domination through structured feature organization and guiding high-uncertainty unknown class samples toward the hub. Extensive experiments show that our method outperforms state-of-the-art methods, with a maximum improvement of 3.25% across various settings.

---


### 143. [BioStudyBench: Evaluating Agents on Post-Cutoff Biomedical Studies](https://arxiv.org/abs/2610.07614)

**<font color=#1a73e8>作者：</font>** David Li, Shaamil Karim, Christian Gensbigler  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We evaluate whether AI agents can match the reported findings of published biomedical studies using public data. Existing evaluations do not consistently separate analysis from prior knowledge or retrieval of the published answer. We introduce BioStudyBench, a benchmark of 25 long-horizon analysis tasks drawn from studies first published between July and September 2026, after the developer-reported knowledge cutoffs of the models we evaluate, semi-automatically filtered down from 404,019 PubMed records. In each task, the agent receives a neutral research question but no data files, so it must find and download the relevant public data, search the literature through tools that return only records dated before its cutoff, and report findings through data analysis. To measure gains over prior knowledge, we run every task both with and without access to data and tools. Across eight models, access to data and tools raises the pass rate by 47 percentage points on average over the no-data baseline. Open-weight models across sizes trail closed-weight models, with the best open-weight model passing 81.3% of tasks against 94.7% for the best closed-weight model.

---


### 144. [AFA-BANDIT: Provably Near-Optimal Online Multi-Feature Classification Under Budget Constraints](https://arxiv.org/abs/2610.07615)

**<font color=#1a73e8>作者：</font>** AbdAlRahman Odeh, Teng-Hui Huang, Hesham El Gamal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Active Feature Acquisition (AFA) is a classification problem in which an agent decides which costly features to acquire before predicting each sample's label. Unlike batch AFA, which trains a fixed policy and classifier offline on fully observed data, online AFA updates its predictor from revealed labels as samples arrive. Existing online methods either use deep reinforcement learning (RL) without performance guarantees or maximize cost-adjusted reward rather than enforce a global budget. We formulate online AFA as a combinatorial Bandits with Knapsacks (BwK) problem that couples acquisition and prediction. Unlike prior bandit-based AFA and classical BwK, our setting has combinatorial complexity, evolving rewards, a global budget, and structured side information. We obtain an improved regret upper bound over standard BwK bounds in this framework, leveraging a cardinality-aware confidence bound and the subset update structure. To avoid an exponentially large action space, we propose \emph{LP-Chain}, a variant that searches a cost-aware chain of feature subsets with a size that grows linearly with the number of features. While the regret upper bound is specific to the combinatorial framework, \emph{LP-Chain} empirically achieves comparable predictive performance. On synthetic data, \emph{LP-Chain} outperforms HEDGE-based BwK and deep RL-based online AFA baselines and scales favorably to more features.

---


### 145. [Beyond screen time: Explaining cross-national differences in digital literacy through socioeconomic and psychological mechanisms](https://arxiv.org/abs/2610.07619)

**<font color=#1a73e8>作者：</font>** Hyejeong Lee, Daeyoung Ham, Suyoun Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This study provides a structural explanation for cross-national variation in the relationship between screen time and digital outcomes. While prior research and large-scale assessments such as ICILS have documented inconsistent associations between screen time and digital competence, the mechanisms underlying these differences remain unclear. Using ICILS 2023 data, this study employs multigroup structural equation modeling to examine the relationships among socioeconomic status, screen time regulation, ICT self-efficacy, and digital literacy outcomes. Results reveal substantial cross-country differences in the effects of screen time regulation. In contrast, ICT self-efficacy emerges as a consistent and robust predictor across all countries. Moreover, screen time regulation influences outcomes indirectly through self-efficacy in some contexts but not others. These findings challenge the use of screen time as a standalone indicator of digital engagement and highlight the importance of psychological mechanisms. By integrating socioeconomic, behavioral, and psychological factors, this study advances a more nuanced understanding of digital competence and moves beyond quantity-based approaches to digital learning.

---


### 146. [Learning to Outgrow a Theory: Experimental Discovery Beyond the Initial Hypothesis Space](https://arxiv.org/abs/2610.07627)

**<font color=#1a73e8>作者：</font>** SiYuan Ma, Albert Gao, Chunzheng Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific discovery systems typically optimize experiments within a fixed hypothesis space. This creates a failure mode when all available candidates omit the same missing mechanism: candidate disagreement can collapse even while the model class is systematically wrong. We formulate experimental model-class revision, in which a discovery policy jointly proposes a structural edit and a diagnostic experiment that tests whether that edit is necessary. The method couples a class-level distinguishability objective, in which one shared parameterization must explain all selected experiments, with anytime-valid sequential evidence that triggers structural revision only after the current class is rejected. On 400 held-out controlled dynamical environments, the joint policy reaches 89.5% exact recovery with a budget of 32 real experiments, improving the strongest matched baseline by 10.0 percentage points while requiring fewer executed experiments and candidate fits. The learned revision-experiment pairing transfers across unseen mechanism combinations, held-out but expressible primitives, parameter extrapolation, and shifted experiment costs; when the true mechanism is outside the edit grammar, it detects library insufficiency in 88% of cases with a 5.5% false-support rate. Revision gains also transfer to ODEBench and ODEBase model-library tasks, as well as DiscoverPhysics worlds. These results support a view of scientific discovery in which deciding what mechanisms a theory should make expressible and where to collect evidence are treated as a single sequential decision problem.

---


### 147. [Complementary Supervised and Self-Supervised Representations for Out-of-Distribution Graph Learning](https://arxiv.org/abs/2610.07628)

**<font color=#1a73e8>作者：</font>** Qingying Hao, Zikang Chen, Chuxuan Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Out-of-distribution (OOD) generalization remains challenging for graph neural networks (GNNs), as graph distributions can vary substantially across time and domains. Supervised and self-supervised graph representation learning are guided by distinct objectives and offer different perspectives on graph representations. In this work, we study whether self-supervised representations (SSL) can provide complementary signals to improve supervised OOD node classification. We develop two backbone-agnostic frameworks that exploit such information at different stages of learning and prediction. Co-Train jointly learns supervised and SSL representations and adaptively integrates them during training, while Dual-Space Retrieval performs non-parametric prediction in the two representation spaces and combines their predictions through confidence-aware fusion at inference time. The supervised and SSL encoders are separately parameterized and need not share the same GNN architecture.
We evaluate multiple GNN backbones and two distinct SSL objectives, DGI and GRACE, on four graph benchmarks spanning temporal and cross-domain distribution shifts. Extensive experiments show that Co-Train consistently outperforms strong supervised OOD baselines, while Dual-Space Retrieval achieves competitive performance as a flexible non-parametric alternative. Results across different backbones and SSL objectives, together with representation analyses and ablations, demonstrate that SSL representations provide complementary information to supervised representations and can improve OOD node classification across diverse settings.

---


### 148. [Measuring climate backlash in Twitter and Reddit archives: Lexical definitions, recorded responses and participant turnover](https://arxiv.org/abs/2610.07634)

**<font color=#1a73e8>作者：</font>** Wentao Xu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Social media archives are often used to study resistance to climate action, but words, response counters and observed participants do not measure the same social process. We examine four supplied Twitter and Reddit archives by processing all registered files without sampling and applying transparent, non-exclusive lexical rules. The study links frame co-occurrence to source-specific temporal and response models, then separates event-period changes among returning authors from participant turnover. Renewable-energy terms accompany cost-related language on Reddit, yet narrower backlash phrases sharply reduce cross-source contrasts and reverse the sign of the Paris Agreement contrast in submissions. Cross-discourse history does not improve eligible primary-context forecasts. Denial/hoax terms are associated with higher recorded Twitter likes, whereas Reddit response associations depend on frame, outcome and author specification. Around the 2019 global climate strike, returning-author expression and participant turnover both contribute to increased protest-language shares. An archive endpoint prevents the corresponding Climate Twitter migration inference. Most crossed-cluster estimates lack released intervals, and joint author/month response covariance estimates fail, restricting formal inference. These results show how operational definitions, platform-specific response fields and observation boundaries shape what can be claimed about climate backlash. The contribution is an archive-based account of these measurement consequences, rather than a measure of individual opposition, persuasion or advocacy-induced backlash.

---


### 149. [CISB-Bench: An Auditable Source--IR Dataset of Compiler-Introduced Security Bugs](https://arxiv.org/abs/2610.07635)

**<font color=#1a73e8>作者：</font>** Saatvik Pradhan, Anuroop Saini, Pranav Attrey 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Compiler-introduced security bugs (CISBs) arise when an optimization, lowering, or instrumentation decision changes a security-relevant property of the generated program. They are difficult to study because their evidence is distributed across issue reports, reduced tests, historical configurations, and compiler artifacts; a security-related report also does not imply that every associated reduction establishes a security-bearing compiler failure. We present CISB-Bench, an auditable dataset of 429 exact C-program rows mined from GCC and LLVM. Each row contains its C reduction, a standardized LLVM IR analysis bundle at -O0 through -O3, public provenance, a final binary label, and a primary mechanism or boundary annotation. Two reviewers independently labeled the fixed corpus, agreeing on 369 rows (86.0%, Cohen's kappa=0.662); the 60 disagreements were adjudicated. The final dataset comprises 280 CISBs and 149 hard non-CISB cases. The prediction task is to recover this reviewed exact-row label from the supplied artifacts; it is not a claim that standardized IR alone reproduces every historical compiler failure. We characterize the security mechanisms and evidence boundaries represented by the corpus, and demonstrate how its paired artifacts support source-only, IR-aware, and joint analyses. CISB-Bench provides a reusable, inspectable target for compiler-security mining and detection research.

---


### 150. [Learning Explainable Representations of Complex Game-playing Strategies](https://arxiv.org/abs/2610.07638)

**<font color=#1a73e8>作者：</font>** Abhijeet Krishnan, Colin M. Potts, Arnav Jhala 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As part of learning to play complex games, human players develop develop abstractions for concepts and strategies of gameplay consistent with game rules to improve their performance. These concepts are applied to explain other players' actions, and to inform their own actions in-game. Understanding other players' strategies is a crucial part of such improvement, but requires time and effort. In this paper, we propose a strategy similar to human cognition for training RL agents to synthesize learned strategies and policies as executable procedures based on sequences of gameplay actions. We present methods to automatically learn such programs to play chess and to solve tasks in a grid-based environment. We show that the learned strategies produce effective actions, and can be learned from gameplay data.

---


> [!TIP]
> 当前位于：**101-150**（第 3/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-335](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
