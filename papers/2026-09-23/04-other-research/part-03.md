# 📦 其他研究 | 2026年09月23日

> 本类共 **463** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-463](./part-10.md)

---

### 101. [Towards Robust Classroom Attendance: A Comprehensive Evaluation of Face Detection and Recognition Models](https://arxiv.org/abs/2609.22750)

**<font color=#1a73e8>作者：</font>** Himani Trivedi, Hiren Patel, Ridham Patel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Manual attendance methods, such as paper or register-based systems, take a lot of time, can lead to errors, and are easy to falsify. Face recognition is more reliable, but it frequently struggles in classrooms because lighting and other conditions can vary. Face recognition datasets are designed for regulated environments and do not capture the actual challenges found in classrooms. To address this, a new face detection and recognition dataset, the Visage Face dataset, comprising 16,234 face samples, is proposed for the task of face detection and recognition. The photos are taken from different angles and under varying lighting conditions, with students showing a range of expressions, and some faces partly covered to reflect real-life situations. A YOLO-based system is used to detect faces and tested seven advanced face recognition models with thirteen configurations: LVFace, QCFace, FaceLiVTv2, TopoFR, EdgeFace, TransFace, and GhostFaceNets. Of these, FaceLiVTv2-M performed best, with 99.75% Top-1/Top-5 accuracy and an inference time of 6.459 ms. These results show that the Visage Face Dataset is a realistic and challenging benchmark for face recognition in classroom attendance.

---


### 102. [D-IMPL: A Diffusion-based Solver for Parameterized BBOs](https://arxiv.org/abs/2609.22752)

**<font color=#1a73e8>作者：</font>** Yang Hu, Na Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models have demonstrated strong power in generative modeling tasks across multiple domains, exhibiting a remarkable capability of learning complex distributions from samples. In this paper, we leverage such capability to design an efficient universal diffusion-based solver for parameterized black-box optimizations (BBO), where the optimizer has only black-box access to queries of the objective function at the learning stage, yet is able to reduce the additional computational cost at the inference stage for each BBO instance while also capturing the potential multi-modal landscape of non-convex objectives. To cast our formulation as a compatible generative modeling task, we introduce the notion of minimization policy as a new solution concept, which defines a sampling distribution over the solutions that should concentrate around the minimizer set for each BBO instance. We then propose Diffusion-based Iterative Minimization Policy Learning (D-IMPL), a practical generative-model-based solver for solving parameterized BBOs that employs diffusion models to learn a minimization policy, whose density is proportional to the exponential of the negated objective values, thereby amortizing the computational costs across different BBO instances. Furthermore, we demonstrate the performance of our D-IMPL algorithm by establishing a sample complexity guarantee showing that a $\delta$-approximate minimization policy can be effectively learned within $O(\log(1/\delta))$ iterations, and by extensive empirical evaluations over a range of constrained and unconstrained BBO tasks.

---


### 103. [CTSpinoPelvic1K: spine, pelvis, ribs and femora in one coordinate frame, annotated for lumbosacral transitional anatomy](https://arxiv.org/abs/2609.22760)

**<font color=#1a73e8>作者：</font>** Gregory Schwing, Ashley Schehr, Annika Tekumulla 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Purpose: A vertebra at the lumbosacral junction is named by counting caudally from C2 on whole-spine imaging, but a lumbar case is planned on lumbar-only imaging (T12 to S1), without C2. Abdominopelvic CT holds that span plus the lowest ribs and pelvis. Where a lumbosacral transitional vertebra (LSTV) alters the count, the local anatomy is ambiguous: four rib-free vertebrae may be an L1 with a lumbar rib or an L5 assimilated to the sacrum, and six may be a sixth lumbar vertebra, a T12 with aplastic ribs, or a lumbarized S1. CTSpinoPelvic1K asks whether local morphology resolves it without the count. CTSpine1K's vertebrae and CTPelvic1K's pelvis covered these patients but were never joined; this release joins them on one series and adds the bones neither had. It provides 802 CT records with per-level ribs and femora, levels anchored on the lowest rib-bearing vertebra and S1, and classes for L6, T13, a separate S1 and lumbar ribs, so anomalies are recorded as such.
Acquisition and Validation Methods: Records pair CTSpine1K and CTPelvic1K labels on each patient's bone-richest series under a VerSe-native scheme. Validation covered geometric invariants (802/802 pass), rib-vertebra incidence across 5,749 ribs (0.035% offset), and spinopelvic measures matching published values.
Data Format and Usage Notes: NIfTI image/label pairs with patient-grouped LSTV-stratified five-fold splits and a loader; archived at this https URL.
Potential Applications: Classifying a vertebra from local features; updating cadaveric morphometry; spinopelvic assessment; opportunistic screening; and, absent a public preoperative lumbar cohort, surgical planning research (377 records prone). Limitations: thoracic ground truth is field-of-view limited; postural angles supine; no held-out test set; ribs are triaged-review pseudolabels; Castellvi grades two-reader consensus on 33 records.

---


### 104. [DriveReferee: Geometric Safety Verdicts Need Not Be Learned for Driving World-Action Models](https://arxiv.org/abs/2609.22762)

**<font color=#1a73e8>作者：</font>** Fengcheng Yu, Dhruv Parikh, Junjie Ye 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative world-action models (WAMs) jointly generate future video and vehicle actions, while their action branches remain primarily optimized by expert imitation. Yet imitation provides no explicit closed-loop geometric verdict for generated trajectories, making verification important during both training and deployment. Closed-loop evaluators can check collision and drivable-area violations, but require privileged scene state unavailable at deployment. Existing approaches often close this gap by learning a verifier from sensor features. For these geometric checks, the rule itself is explicit. For example, collision is determined by whether the rolled-out ego footprint overlaps occupied vehicle space. What is unavailable at deployment is the scene state needed to apply the rule. We introduce DriveReferee, which uses a learned geometry readout to predict the scene representation from camera observations and executes the geometric safety rule directly rather than learning it. The resulting analytic referee evaluates collision and drivable-area safety from a scene state and candidate trajectory. During training, it scores self-sampled trajectories on ground-truth state and distills the resulting preferences into the WAM policy. At deployment, the same referee evaluates generated trajectories on this predicted state and selects a safer alternative when needed. The analytic referee requires no verdict-specific training, and its decisions follow an explicit geometric rule. Under matched candidates and inference budgets, it matches or outperforms all learned-verifier and heuristic baselines. Given the same predicted state and trajectory, learning the verdict provides no measurable downstream gain despite requiring tens of thousands of evaluator-labeled training examples. On the full NAVSIM navtest, DriveReferee reaches 92.02 PDMS with single-camera visual input and no external training data.

---


### 105. [DVA-Neurons: Design and Verification of Adaptive LIF Neurons: From Single-Neuron Dynamics to Multi-Neuron Spiking Networks](https://arxiv.org/abs/2609.22775)

**<font color=#1a73e8>作者：</font>** Thanh Pham, Riadul Islam  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spiking Neural Networks (SNNs) offer a promising path toward ultra-low-power artificial intelligence inference by emulating the event-driven computation of biological neurons. However, two challenges limit their practical deployment. First, fixed-parameter Leaky Integrate-and-Fire (LIF) neurons lack the adaptation mechanisms observed in biology, where neurons modulate their excitability based on firing history. Second, scaling from single neurons to multi-neuron networks introduces challenges in synaptic weight distribution and inter-neuron spike routing that are absent in isolated designs. This paper addresses both issues through the extension, verification, and physical implementation of adaptive LIF neurons at three architectural scales. This work contributes: a 2nd-order neuron with two-stage synaptic filtering for richer temporal dynamics; a fully-connected 6-neuron spiking network with configurable weights (100 to 5) demonstrating weight-based inter-neuron communication; and a direct verification methodology enabling per-cycle observation of all internal states. All designs were synthesized targeting Selected Area Electron Diffraction (SAED) 14 nm Complementary Metal-Oxide-Semiconductor (CMOS) technology at 1 GHz and verified with Cocotb-based Python testbenches under pulsed current stimuli (amplitude 80, ISI=3). The results show that adaptation effectively modulates firing: 31% suppression in the 2nd-order neuron (25 vs.\ 36 spikes) and 31% reduction in postsynaptic firing in the network (18 vs.\ 26 spikes). Physically, the 2nd-order neuron costs 1.77x more area and 1.52x more power than the 1st-order baseline, while the 6-neuron network demonstrates near-linear scaling (5.7x area, 5.3x power). Seven verification bugs spanning testbench connectivity, fixed-point overflow, and Verilog expression-width semantics are documented.

---


### 106. [Improved Private Sparse Covariance Estimation with Multiscale Threshold Tests](https://arxiv.org/abs/2609.22783)

**<font color=#1a73e8>作者：</font>** Zihan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study differentially private covariance estimation in operator norm for mean-zero sub-Gaussian distributions with unknown covariance support and at most $k$ nonzero entries per row. We develop a multiscale random-threshold algorithm with sample complexity $\ot(k^2/\alpha^2+k\sqrt d/(\alpha\varepsilon))$ for $(\varepsilon,\delta)$-differential privacy and error at most $\alpha\sigma^2$, where $d$ is the dimension and $\sigma$ is a known sub-Gaussian scale. The bound improves the privacy-dependent term of the existing $\ot(k^2/\alpha^2+k^{3/2}\sqrt d/(\alpha\varepsilon))$ \citep{kumar2026curse} upper bound by a factor of $\sqrt k$, and matches the lower bound of $\widetilde{\Omega}(k^2/\alpha^2 + k\sqrt{d}/(\alpha\varepsilon))$ in its applicable parameter regime.
Our key technical ingredient is a direct operator-norm bound on the centered fluctuations of an ideal reconstruction, exploiting conditional independence rather than accumulating entrywise errors across each row. A multiscale allocation of threshold tests balances reconstruction variance against query sensitivity. Together, these ingredients sharpen the trade-off between approximation error and privacy protection, removing the additional $\sqrt{k}$ factor from the privacy-dependent sample complexity.

---


### 107. [Robust Market Making with Hawkes Order Flow and Price Impact via Adversarial Reinforcement Learning](https://arxiv.org/abs/2609.22785)

**<font color=#1a73e8>作者：</font>** Hao Yang, Zhenguo Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Market-making strategies in real limit order book markets face substantial model uncertainty and regime-shift risk. Existing adversarial reinforcement learning approaches improve robustness by formulating the Avellaneda--Stoikov market-making problem as a zero-sum game between a market maker and an environmental adversary. However, these approaches typically rely on Poisson order arrivals and neglect trade-induced price impact, limiting their ability to capture important high-frequency market microstructure effects such as clustered order flow, self-excitation, and post-trade price feedback.
We extend adversarial reinforcement learning for market making to a more complex environment with Hawkes self-exciting order arrivals and trade-induced price impact. To mitigate the increased non-stationarity introduced by the expanded regime space, we incorporate an LSTM module that explicitly models the temporal structure of recent observations. We further characterize the equilibrium properties of the proposed framework through both game-theoretic analysis and numerical experiments, and introduce a robustness evaluation protocol focused on improvements in the left tail of the return distribution.
Experimental results across a range of market regimes show that the proposed method achieves improved left-tail performance in most complex microstructure environments. In particular, the gains are pronounced in regimes with strong Hawkes excitation and low-to-moderate price impact. Bootstrap tests provide no evidence that these improvements are obtained through a stronger terminal directional inventory bias. These results suggest that combining adversarial training with temporal state representation can improve the robustness of reinforcement-learning-based market-making strategies under order-flow self-excitation, price impact, and regime uncertainty.

---


### 108. [Human-Level Accuracy, Non-Human Strategies: Revealing Model-Human Divergence in Video Physical Reasoning](https://arxiv.org/abs/2609.22788)

**<font color=#1a73e8>作者：</font>** Fanhong Li, Shurui Zheng, Zi Yin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video foundation models now reach human-level accuracy on physical-reasoning benchmarks, yet such tasks require predicting unobserved physical outcomes. Do these models perform human-like forward simulation, or do they exploit statistical regularities in visible scenes? Accuracy alone cannot distinguish these strategies. We introduce a distributional evaluation framework that treats model seeds and human raters as populations, enabling comparison of consensus, uncertainty, and strategy. On the Physion benchmark, we evaluate three ViT-L architectures (V-JEPA2, VideoMAEv2, DINOv2). V-JEPA2 narrows the accuracy gap to ~1 percentage point (73.2% vs. 74.2%), yet model-human disagreement reaches 26.4%, far exceeding human-human disagreement (4.8%), with substantially lower agreement (kappa ~ 0.48 vs. 0.91). The divergence follows forward-simulation demands: models outperform humans on geometric reasoning (linking, +11.8 pp) but underperform on gravitational dynamics (rolling, -11.8 pp) and causal chains (dominoes, -10.5 pp). Strategy fingerprinting confirms all three architectures share non-human strategies while none aligns with humans. Attribution analysis suggests that unobservable outcome features, rather than visible scene properties, predict this divergence, consistent with models relying more on scene-level statistical regularities than on explicit forward simulation, a systematic divergence that accuracy alone cannot reveal. Code is available at this https URL.

---


### 109. [From Research Frontier to Laboratory Bench: Design of a Four-Tier Experimental Teaching System for Multimodal Medical Image Intelligent Diagnosis](https://arxiv.org/abs/2609.22790)

**<font color=#1a73e8>作者：</font>** Dongjing Shan, Yamei Luo, Jin Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Undergraduate programmes in intelligent medical engineering are expanding, yet laboratory curricula lag behind the multimodal, long-tailed, and distributionally shifting realities of clinical AI. This design paper presents an advanced experimental teaching system that translates an ongoing multimodal deep learning research project on endometrial carcinoma into a structured undergraduate lab sequence. We identify three educational gaps (modality, authenticity, and deployment) and derive four pedagogical principles from constructive alignment, experiential learning, the research teaching nexus, and the CDIO framework. The curriculum comprises four progressive tiers plus an engineering layer, with 32 laboratory units over 64 contact hours, delivered via a custom virtual clinical workstation using de-identified multi-institutional data. Each tier maps to a specific technical bottleneck, prerequisite coursework, and criterion-referenced deliverables. Data governance, safety, and assessment protocols are specified. Learning outcome data will be collected across two implementation cycles.

---


### 110. [AlexandriaX 2026: The First Shared Task on Dialectal Arabic Machine Translation](https://arxiv.org/abs/2609.22796)

**<font color=#1a73e8>作者：</font>** Abdellah El Mekki, AbdelRahim A. Elmadany, Samar M. Magdy 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dialectal Arabic machine translation (MT) remains challenging despite recent progress in Arabic language technologies, particularly because effective translation requires modeling not only semantic content but also dialectal variation, conversational context, speaker and addressee characteristics, and sociolinguistic appropriateness. Moreover, conventional MT metrics provide limited insight into the linguistic errors produced by dialectal systems. We present the AlexandriaX 2026 Shared Task on Dialectal Arabic MT, which addresses these challenges through three complementary subtasks: (1) context-aware English-to-Dialectal Arabic dialogue translation across 13 Arabic varieties, (2) cross-dialect Arabic translation in the financial domain covering six Arabic dialects, and (3) span-level MT error detection and classification using linguistically motivated error categories across five Arabic varieties. The shared task attracted 38 registrations for Subtask 1, 33 for Subtask 2, and 35 for Subtask 3. Twelve unique teams submitted their system description papers, all of which we accepted for publication. The best system on Subtask 1 achieved 30.42 spBLEU in the constrained track and 33.49 spBLEU in the unconstrained track. On Subtask 2, the top system obtained 28.40 spBLEU. On Subtask 3, the best system achieved an overall score of 49.82, outperforming the 24.29 baseline. Taken together, the results of the leading systems across the three subtasks highlight the benefits of explicit dialect modeling, context-aware generation, retrieval and reranking, and specialized approaches to interpretable MT error analysis. All the resources of AlexandriaX 2026 shared task are publicly available, including data, baselines, and evaluation code on our project page: this https URL.

---


### 111. [Coral: Contextual Gists for Blind and Low Vision Screen Reader Users' Understanding of Dynamic User Interfaces](https://arxiv.org/abs/2609.22799)

**<font color=#1a73e8>作者：</font>** Ritesh Kanchi, Jianna So, Krzysztof Z. Gajos  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Blind and low vision (BLV) screen reader users construct mental models of user interfaces (UIs) through incremental screen reader interaction, a time-consuming and cognitively demanding process complicated by modern interfaces that may not convey dynamic content accessibly. We interviewed eleven BLV screen reader users about UI understanding and derived design objectives that informed Coral, a context-aware browser extension. Coral synthesizes interface and user context to generate screen reader-narrated gists which holistically notify users of interface states and changes relevant to their likely goals and ongoing interaction. In a comparative evaluation with eight BLV screen reader users, participants used Coral to form initial expectations and interpret interface changes, and reported spending less time and effort manually verifying interaction outcomes. Together, our findings provide deeper insight into how BLV screen reader users navigate gaps in their UI understanding, and how intelligent support that combines interface and user context can bridge these gaps.

---


### 112. [To Consolidate or not to Consolidate? Evaluating the Impact of Consolidation in Multi-Reference Training using Peer Reviews](https://arxiv.org/abs/2609.22805)

**<font color=#1a73e8>作者：</font>** Maitreya Prafulla Chitale, Ketaki Mangesh Shetye, Yash More 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural language generation (NLG) tasks span the spectrum of conditional entropy, ranging from highly constrained machine translation to open-ended dialogue generation. Structured tasks like automated peer-review generation occupy the intermediate region, where a single input admits multiple valid, overlapping outputs. In this work, we demonstrate that traditional single- and multi-reference training paradigms are suboptimal for these intermediary tasks. We provide empirical evidence that consolidating diverse references into a unified training signal is crucial for developing effective systems. To facilitate this, we introduce MERC-36K, a large-scale corpus of over 36,000 papers paired with original and consolidated peer reviews. Using this dataset, we train specific architectures to isolate the impact of different reference paradigms and benchmark against existing state-of-the-art systems. Through extensive automatic and human evaluation, we demonstrate that models trained on consolidated references significantly outperform those trained on unconsolidated references. Dataset and code will be released upon acceptance.

---


### 113. [C$^{2}$-INR: Customized Convolutional Implicit Neural Representation](https://arxiv.org/abs/2609.22807)

**<font color=#1a73e8>作者：</font>** Jinglei Shi, Xinran Chang, Jiaqi Cui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Implicit Neural Representation (INR) leverages neural networks to represent discrete signals such as images as continuous ones, where the network weights serve as a compact form of the signal itself. Most existing INR methods adopt Multi-Layer Perceptrons (MLPs) as their backbone. Since these models render each pixel independently, they inherently fail to exploit the spatial correlations that exist between neighboring pixels. In contrast,convolutional INRs can process pixels in parallel while inherently accounting for inter-pixel dependencies, making them a more natural fit for representing images. Nevertheless, convolutional INRs remain relatively underexplored, and the majority of them rely on fixed architectural settings, leaving little room for image-specific adaptation. In this paper, we investigate network customization for convolutional INRs. We replace conventional filters with irregular directional kernels, whose allocation is guided by the directional energy in the image spectrum, i.e., directions exhibiting stronger energy are assigned a larger number of kernels, enabling content-tailored convolution settings. These kernels are further reformulated via an orthogonal basis to achieve a superior sparse representation. Moreover, we introduce an annealed Gumbel-Softmax-based mechanism for kernel-level activation function selection, which gives the most suitable activation function for each convolution kernel. Extensive experiments demonstrate that our method, namely C$^{2}$-INR, achieves superior performance against state-of-the-art approaches under comparable parameter budgets across a wide range of image processing tasks, including representation, inpainting, and super-resolution.

---


### 114. [FIRM-WM: State-factorized factual-interventional recurrent modeling for reward-free visual planning](https://arxiv.org/abs/2609.22816)

**<font color=#1a73e8>作者：</font>** Yilun Wu, Yunjian Zhang, Aobo Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reward-free latent world models can learn from offline videos and solve new image--goal tasks by optimizing actions through predicted latent futures. This setting places two demands on the planning state: its coordinates must be comparable with a goal image. Moreover, its dynamics must retain velocity, motion trend, contact, and other history--dependent information beyond those goal coordinates. Offline training creates a second mismatch: each recorded trajectory reveals one factual future, whereas a sampling--based planner compares many actions that were not taken from the same state. We introduce FIRM-WM (Factual--Interventional Recurrent World Model), a compact pixel world model designed around these two gaps. Its recurrent state separates a typed, goal--comparable configuration from a 128-dimensional dynamic fiber used for prediction but excluded from the terminal goal cost. Broad factual trajectories provide state coverage, while common--reset intervention branches provide observed outcomes for alternative action sequences. Before executing each branch, we reset the environment and restore the same recorded values exposed by the environment's state--setting interface. Under matched CEM planning and three independent full-pipeline seeds, FIRM-WM reaches 99.0$\pm$1.0% on TwoRoom, 92.7$\pm$2.1% on Reacher, and 88.0$\pm$3.0% on OGBench-Cube, compared with 89.0%, 88.0%, and 70.0% for LeWM. The deployed model uses 2.98--3.42M parameters and records 2.13--11.60$\times$ lower planning time on these tasks.

---


### 115. [Beyond Average Error through Oracle-Informed Stress Tests for Time-Series Forecasting](https://arxiv.org/abs/2609.22820)

**<font color=#1a73e8>作者：</font>** Xu Lin, Runheng Zuo, Shengxuan Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Average squared error cannot reveal whether forecasting performance degrades because the future becomes less predictable or because forecasts move farther from the conditional mean. We introduce paired, mechanism-controlled stress tests that decompose changes in expected squared error at each lead time into environmental risk and forecast-oracle distance, using an origin-conditioned predictive oracle unavailable to the evaluated models. Three end-to-end controls have known attribution. Specifically, the null, environmental-only, and information-gap controls verify that the pipeline assigns changes to the correct component. We then apply the benchmark to 24 deployable forecasters. Under frequent switching, 14 methods have higher realized MSE but lower oracle distance; under outlier-variance feedback, 19 have higher MSE but lower scale-standardized MSE. Short- and long-lead stress-response rankings have Spearman correlation 0.624, revealing substantial horizon-dependent reordering. We then study multivariate relation shifts. Across six models and three coupling severities, oracle distance accounts for only 0.7-3.9% of the decomposed expected-risk increase, and environmental-risk majority persists in an eight-channel system and a matched-difficulty audit of Ring, Block, and Hub relations. Finally, prespecified contrasts on independent data-generating process (DGP) realizations show that several visually compelling discovery profiles, including trend accumulation and the hypothesized switching reversal, do not replicate. The benchmark thus combines component-wise diagnosis with a held-out stability audit. It complements real-data out-of-distribution evaluation, which measures performance under realistic shifts when exact oracle attribution is unavailable.

---


### 116. [Personalized Federated Reinforcement Learning via Model-Agnostic Meta-Learning: Convergence of Exact and Hessian-Free Meta-Policy Gradients](https://arxiv.org/abs/2609.22833)

**<font color=#1a73e8>作者：</font>** Ali Beikmohammadi, Sarit Khirirat, Sindri Magnússon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study personalized federated reinforcement learning, in which $n$ agents, each acting in its own Markov decision process, collaborate through a server to learn a shared MAML-style policy initialization that becomes effective for an individual agent once that agent adapts it with a single local policy-gradient step. We propose Per-FedAvg-PG, in which agents take $\tau$ local stochastic meta-policy-gradient steps between communication rounds, and prove that it reaches an $\varepsilon$-approximate first-order stationary point of the personalized objective in $K=\mathcal O(\varepsilon^{-3/2})$ rounds with $\tau=\Theta(\varepsilon^{-1/2})$ local steps. The analysis rests on a structural feature of the reinforcement learning setting: under standard policy-class regularity, the per-agent objectives have uniformly bounded gradients and Hessians with explicit constants, so the bounded-gradient and bounded-heterogeneity conditions imposed by the supervised theory hold automatically and no separate heterogeneity assumption is needed. The exact meta-gradient requires the inner-loop policy Hessian, which our experiments identify as the practical bottleneck. We therefore analyze the Hessian-free variant, bound its bias, and exhibit fixed points at which the meta-gradient is nonzero and of order $\alpha$, showing that the resulting stationarity floor is a property of the method rather than of the bound. Experiments on tabular and neural navigation confirm the predicted behavior and show transfer to unseen agents at an order of magnitude lower sample cost than independent training. Together these results identify the adaptation step size as a tunable personalization knob and the curvature estimate as the quantity that governs whether exact meta-gradients are affordable.

---


### 117. [SatOV: Restoring Spatial Priors for Training-Free Open-Vocabulary Segmentation in Remote Sensing Imagery](https://arxiv.org/abs/2609.22834)

**<font color=#1a73e8>作者：</font>** Changhao Zhao, Linglin Zeng, Hai Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary semantic segmentation (OVS) of remote sensing imagery is a challenging pixel-level task requiring strong generalization and adaptation to the spatial characteristics of remote sensing data. Although existing vision-language foundation models perform well in general domains, their image-level classification design weakens the spatial priors needed for high-resolution remote sensing segmentation: structural spatial relations are degraded during deep feature transformation, and fine-grained spatial details are lost during downsampling. To address these complementary deficiencies, we propose SatOV, a training-free framework for open-vocabulary remote sensing segmentation that restores spatial priors at two stages of the representation pipeline. Specifically, Residual QQ Attention (ResQQ) extracts Query-Key self-attention from an intermediate CLIP layer and fuses it with final-layer Query-Query attention via a residual combination, restoring structural spatial priors suppressed by the final-layer representation. Spatially Modulated Upsampling (SatUp) uses the original high-resolution RGB image as spatial guidance, combining spatial feature modulation with guided cross-attention to reconstruct pixel-level textures and boundaries. Extensive experiments on DOTA, UDD, LoveDA, and Vaihingen show that SatOV consistently improves training-free OVS and achieves competitive quantitative and qualitative results against state-of-the-art methods. These results validate the effectiveness of restoring spatial priors at both the representation and spatial-resolution stages for remote sensing open-vocabulary segmentation.

---


### 118. [When Label Noise Meets Class Imbalance: A Robust Framework for Android Malware Family Classification](https://arxiv.org/abs/2609.22835)

**<font color=#1a73e8>作者：</font>** Haolan Zhang, Cuiying Gao, Fulin Zhao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine learning methods for Android malware family classification have achieved high accuracy, but their application is hindered by two major challenges. First, the widely used code obfuscation severely disrupts the automated labeling process and introduces substantial label noise into training datasets. Second, training datasets often exhibit severe class imbalance, leading to poor performance of family classification models. Although existing studies have proposed various solutions to either label noise or class imbalance, they often overlook the interplay between these two factors. Under class imbalance, the presence of hard-to-learn minority-class samples can significantly impair the effectiveness of existing countermeasures for noisy samples. To jointly address label noise and class imbalance, we propose a robust Android malware family classification framework, RoMaC. It employs a self-training strategy to correct noisy labels and, more importantly, discriminately treats head-family and tail-family samples. This design effectively mitigates the adverse impact of class imbalance on noise-robust learning. Moreover, RoMaC integrates a class reweighting mechanism with multi-model ensemble learning, thereby enhancing both classification accuracy and noise robustness. We evaluate RoMaC on a combined dataset constructed from two public datasets. When 30% of the samples are obfuscated, RoMaC achieves an overall Macro-F1 score of 0.803 and an accuracy of 0.871, as well as a tail-class Macro-F1 score of 0.672 and an accuracy of 0.784. Compared with existing methods, RoMaC demonstrates performance improvements of 6%-20% across various obfuscation scenarios and noise levels.

---


### 119. [A Hybrid Attention Model Learning Unified Time-aware Patch Representation for Irregular Multivariate Time Series Forecasting](https://arxiv.org/abs/2609.22836)

**<font color=#1a73e8>作者：</font>** Zhihao Lin, Li Lin, Qi Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series foundation models (TSFMs) have recently delivered impressive zero-shot performance across diverse forecasting tasks. However, real-world decision-making frequently relies on \emph{irregular multivariate time series} (IMTS), where inconsistent inter-observation intervals and asynchronous sampling across variables coexist with informative missingness. Existing TSFMs handle such inputs either through imputation that injects spurious values or through index-based positional encodings that ignore continuous time. There is still a gap in the foundation model that follows the original IMTS patterns. In this paper, we propose a hybrid attention model that learns a unified time-aware patch representation for IMTS forecasting. We first design a \emph{time-aware patch encoding} that maps a variable number of intra-patch timestamps into a fixed-size embedding, producing a uniform format for irregular patches without resorting to imputation. We then introduce a \emph{time bias attention} mechanism that calibrates inter-patch temporal misalignment and asynchronous cross-channel dependencies as auxiliary attention offset. Finally, on top of a decoder-only Transformer backbone, we adopt a \emph{hybrid causal mask} that preserves a bidirectional full view over the historical context while keeping the forecast horizon strictly autoregressive. To support large-scale pretraining under irregular settings, we also curate VersaTSA, an archive of $30$B observations that retains the native sampling sparsity of its sources. Experiments on three IMTS benchmarks and a standard regular-MTS benchmark show that our model achieves state-of-the-art zero-shot performance on IMTS and remains competitive when transferred to regular forecasting.

---


### 120. [LINGO: Latent Initialization and Gradient Optimization for Sparse-view X-ray Novel View Synthesis and CT Reconstruction with 3D Gaussian Splatting](https://arxiv.org/abs/2609.22849)

**<font color=#1a73e8>作者：</font>** Lifeng Xing, Dequan Jin, Kunpeng Bu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In novel view synthesis and Computed Tomography (CT) reconstruction with sparse-view X-ray imaging, insufficient angular coverage leads to structural ambiguity and accumulated noise. Integrating 3D Gaussian Splatting (3DGS) with X-ray absorption physics can achieve promising results, but it suffers from noisy initialization, positional insensitivity, and weak gradients in low-density regions. In this paper, we propose a unified Latent Initialization and Gradient Optimization (LINGO) framework to address these issues. LINGO combines latent mask-space initialization with dynamic gradient optimization to improve point cloud structural completeness while accelerating training. It constructs voxel-level 3D filters from X-ray masks to robustly suppress background noise and provide reliable geometric priors. By employing an adaptive voxel scaling strategy and dynamically scaling loss, LINGO can adjust spatial resolution and explicitly amplify gradients in low-density structures. To evaluate the quality of initialization, we introduce the Initialization Point Cloud Structural Deviation (IPSD) metric. Experiments on the X3D dataset indicate that for the novel view synthesis task, LINGO improves the Peak Signal-to-Noise Ratio (PSNR) and Structural Similarity Index (SSIM) by an average of 0.72 and 0.0039, respectively, over baselines under identical sparse-view settings, achieving comparable reconstruction quality within 5k steps to state-of-the-art models typically trained with 30k iterations. For the CT reconstruction task, LINGO also demonstrates consistent improvements, with average PSNR and SSIM gains of 0.36 and 0.0134. These results highlight LINGO's effectiveness in both accelerating training and enhancing reconstruction quality across different sparse-view imaging scenarios.

---


### 121. [Image Frame Dynamic Object Segmentation and Ego Motion Estimation using Radar Image Fusion](https://arxiv.org/abs/2609.22857)

**<font color=#1a73e8>作者：</font>** Astik Srivastava, Suhani Grover, Avinash Sharma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic object segmentation and ego-motion estimation are closely coupled problems in autonomous driving, as accurate ego-motion estimation typically requires static scene observations, while identifying static observations requires knowledge of the ego motion. We present Radar-Dot, a radar--RGB framework that exploits radar Doppler measurements to address this coupling. Radar returns are first used to estimate ego velocity through a linear Doppler constraint, with residual-based static/dynamic segmentation and robust estimation used to reduce the influence of moving objects. The estimated motion is then combined with metric depth and dense optical flow to identify image regions whose observed motion is inconsistent with the rigid scene motion. Experiments on 10 nuScenes scenes (part of nuscenes-mini) demonstrate that the resulting geometric pipeline achieves 20.24% dynamic IoU and 33.67% F1-score over 394 frame pairs, while radar-based static-point filtering improves ego-velocity estimation compared with using all radar returns. These results demonstrate the potential of radar as a modality for jointly improving ego-motion estimation and dynamic object segmentation.

---


### 122. [CurvFlow-DTA: dual-graph discrete Ricci curvature flow for drug--target affinity prediction](https://arxiv.org/abs/2609.22862)

**<font color=#1a73e8>作者：</font>** Jicheng Ma, Yunyan Yang, Juan Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks are widely used for drug--target affinity (DTA) prediction, and discrete Ricci curvature has recently been used to characterize molecular graph geometry. Existing curvature-aware DTA approaches mainly use static curvature on the drug graph while representing proteins primarily with sequence-derived features. This leaves pair-adaptive use of graph geometry underexplored, which may limit adaptation to unseen entities in cold-start settings relevant to practical screening.
We present CurvFlow-DTA, which replaces a single static curvature representation with weighted Forman curvature flow on both molecular and protein residue--residue contact graphs. A label-independent flow trajectory is precomputed for each entity, and a pair-conditioned selector determines the horizons read by a dual-branch Flow-GINE. A frozen ESM-2 supplies residue-level representations and contact scores used to construct the protein graph. Inference requires only SMILES strings and protein sequences, without a bound complex structure.
On Davis and KIBA, CurvFlow-DTA improves on the protocol-matched Ricci-GraphDTA baseline in every warm and cold-start setting. Warm-split mean squared error (MSE) decreases by $19.9\%$ on Davis and $18.9\%$ on KIBA. Across the six cold-start comparisons, MSE decreases by $14.3$--$27.4\%$, with higher concordance index (CI) throughout. Within our compiled set of literature baselines, CurvFlow-DTA achieves the lowest MSE on both warm benchmarks and across four out of six cold-start evaluation settings.

---


### 123. [Causilo Technical Report](https://arxiv.org/abs/2609.22866)

**<font color=#1a73e8>作者：</font>** Minyong Cho, Minho Jeong, Dooho Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Causilo, a tabular foundation model (TFM) that combines frontier predictive performance with exceptionally fast inference. On TabArena, Causilo achieves 1785.4 Elo, at a median inference time of 0.10 seconds per 1K test samples. It outperforms TabPFN-3.5-Fast with 31.6% less inference time, placing it on the performance--efficiency Pareto frontier. Causilo follows TabICL's column-then-row architecture but introduces another row-refinement module before row compression. This module exchanges information among cell representations within each row after column encoding. The refined cells then visit the context set again through an additional column stage before being compressed into row embeddings. For inference efficiency, both row stages use cross-attention through a fixed number of summary tokens, keeping their attention cost linear in the number of features. Pretrained on approximately 36M synthetic tables, Causilo delivers strong benchmark results across TabArena, BeyondArena, and ScoringBench, achieving frontier-level performance with substantially faster inference.

---


### 124. [Leveraging Inference-Time Compute for Diffusion Models via Global Scheduling of Denoising Trajectories](https://arxiv.org/abs/2609.22867)

**<font color=#1a73e8>作者：</font>** Yuan Cao, Yifu Tang, Hangqi Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models generate a sample by traversing a denoising trajectory, a sequence of stochastic noise-reduction steps that transforms pure noise into a draw from a target distribution. At deployment time, additional computation can improve sample quality without retraining: at each step, the sampler draws several candidate noise samples, scores the resulting predictions with a quality criterion called the verifier, and retains the best candidate at the cost of one network evaluation per candidate. This raises a resource allocation question: given a fixed budget of function evaluations, how should search effort be distributed across the steps of the denoising trajectory? We formulate this as a computational budget allocation problem. First, we show that, to leading order in the step size, the expected gain from evaluating $K$ candidates at a step factorizes into an endogenous, step-specific sensitivity parameter times a universal sample-size factor equal to the expected best of $K$ standard-normal draws. Second, for a fixed sensitivity profile, the optimal allocation solves a separable concave integer program with water-filling structure; at fixed total sensitivity, its advantage over uniform allocation increases with sensitivity dispersion in the majorization order. Third, we prove that when sensitivities vary across instances, no adaptive policy can avoid worst-case regret that grows linearly in the trajectory length, which motivates a design that anchors the allocation offline and adapts online only to recover instance-specific slack. We extend the analysis from independent random search to a broader family of local search operators, and instantiate it as an implementable algorithm. Experiments on three families of diffusion samplers show that the proposed allocation attains the quality of the uniform benchmark with 20 to 50 percent fewer function evaluations.

---


### 125. [Planning-Aligned Pretraining of BEV Representations with Sparse Action-Conditioned Targets for End-to-End Autonomous Driving](https://arxiv.org/abs/2609.22868)

**<font color=#1a73e8>作者：</font>** Jaeha Song, Soonmin Hwang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> End-to-end driving requires planning-relevant bird's-eye-view (BEV) representations, but existing pretraining approaches often rely on task annotations or dense scene reconstruction. We introduce PAVER, Planning-Aligned BEV Encoder Pretraining. From a single LiDAR sweep, PAVER constructs sparse risk and unknown targets describing occupied and unobserved evidence along rule-based ego motions. A 10K-parameter head predicts these targets from masked BEV features conditioned on the action state, directing supervision toward geometric constraints on candidate motions. Pretraining requires no driving-task annotations or dense reconstruction. Only the BEV encoder is transferred, preserving the downstream architecture and camera-only inference. On nuScenes, PAVER reduces VAD-Tiny's average collision rate from 0.51% to 0.19%, while improving planning L2, motion prediction, detection, and mapping. The selected VAD-Tiny and VAD-Base schedules use about 36% less estimated total training time than scratch training, including pretraining. On Bench2Drive Town05 Long, PAVER improves UniAD-Tiny's closed-loop Driving Score from 48.45 to 58.79. The project page is available at this https URL.

---


### 126. [Merge++: Universal Merge Refinement Through Data-Free Checkpoint Inversion](https://arxiv.org/abs/2609.22886)

**<font color=#1a73e8>作者：</font>** Aditya Pola, Vineeth N. Balasubramanian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model merging consolidates fine-tuned experts into one multi-task model without retraining. All existing data-free methods approach this problem entirely in weight space. Restricted to arithmetic on parameters, these methods never observe how each expert behaves, a signal that only emerges through forward evaluation. Accessing this behavioral signal requires inputs to evaluate on, which the data-free setting prohibits. We propose Merge++, a post-hoc method that addresses this by inverting the expert checkpoints to synthesize task-representative images, then distilling expert knowledge into the merged model using those images. Merge++ requires no additional data beyond the checkpoints themselves. It applies universally across merging algorithms and operates as a complementary refinement stage independent of the underlying weight-space method. The method consistently improves merging algorithms ranging from simple task arithmetic to state-of-the-art spectral methods, with average gains of +2 to +8 points and up to +25.9 on individual configurations.

---


### 127. [Are Coreset Selection Methods Worth Their Cost?](https://arxiv.org/abs/2609.22894)

**<font color=#1a73e8>作者：</font>** Yangze Liu, Zhongyi Han  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Coreset selection picks a representative subset of the labeled training set to make training cheaper. However, it is usually evaluated by downstream accuracy at a fixed subset size, ignoring both the time spent selecting the subset and the training recipe behind each reported number. We introduce an end-to-end benchmark that standardizes downstream training and charges selection and training to the same auditable wall-clock budget, spanning 4 datasets from CIFAR-10 to ImageNet-1K, 11 selectors, 5 fractions, and 3 seeds, with over 1,500 released runs. Repeated-sampling work has shown that budget-aware evaluation already favors random strategies. Our two budget studies test whether that verdict survives when every selector is granted its most favorable operating point. Across eight wall-clock budget anchors on each of CIFAR-10 and Tiny ImageNet, no anchor is won by a sophisticated selector: every winner is class-balanced random sampling, repeated random sampling, or full-data training. In fixed-budget duels on ImageNet-1K, training on all data for fewer epochs beats every selection strategy we probe while also costing the least. A per-dataset cost audit shows that selection cost is dominated at every scale by a fixed full-dataset scan, so it cannot be amortized away by selecting a smaller fraction, and its absolute size does not extrapolate from one dataset to another. We further quantify when selection does pay back through subset reuse, and document 9 correctness fixes to a widely used codebase, one of which shifts a standard Herding baseline by nearly 6 points. Selection time is not free preprocessing, and an evaluation that ignores it measures the wrong quantity.

---


### 128. [SMS-delivered network-initiated SUPL on Pixel 8: a privacy assessment](https://arxiv.org/abs/2609.22900)

**<font color=#1a73e8>作者：</font>** Douglas Leith  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A SUPL\_INIT message is a network-initiated trigger that can be sent to a handset using an SMS to unilaterally start a location session: on receipt, the handset is instructed to determine its own position and report it, together with an identifier such as its IMSI, to a server specified in the message, without any action by the phone's user. The concern motivating this investigation is whether such a message could be used to silently exfiltrate a handset's location and subscriber identity to a server under an attacker's control. We investigated this on a Google Pixel 8 handset, which uses a Samsung Exynos modem and a Broadcom GPS/GNSS subsystem. We find no privacy issue: the handset never sends location data to an attacker-chosen server as a result of an unsolicited SUPL\_INIT delivered by SMS.

---


### 129. [AVTR-1: Open Stack for Real-Time Interactive Avatars](https://arxiv.org/abs/2609.22913)

**<font color=#1a73e8>作者：</font>** Artem Kravtsov, Dmitrii Ziganshin, Vsevolod Poletaev 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Talking-head and dyadic models now achieve real-time inference, yet fast motion generation alone does not produce an interactive conversation. A live system must synchronize the model's output with speech from an external voice agent, schedule video frames for playback, and handle interruptions. We introduce AVTR-1, an open stack for real-time interactive avatar conversations, built around a compact 153M-parameter autoregressive flow-matching motion generator conditioned on both participants' audio. We adapt its audio encoder for streaming through self-distillation. The stack turns the model's chunk-based generation into a continuous, synchronized audio-video stream driven by an external voice agent, and we analytically derive its contribution to the user-facing latencies and validate the resulting bounds with two commercial voice agents. Further experiments demonstrate that AVTR-1 leads the compared dyadic systems on all reported visual-quality metrics and most conventional listening-motion metrics while remaining competitive in lip synchronization. Its inference runtime operates in real time on data-center and consumer GPUs. However, conventional listening metrics do not establish whether the paired speaker's speech contributes to generated motion. We therefore introduce the Reference-Based Directed Granger Gain (R-DGG), which measures the additional predictive information carried by speaker speech after accounting for listener history and speaker motion. R-DGG finds statistically supported predictive dependence for recorded listeners and all evaluated dyadic systems, but not for talking-head generators without paired audio or mismatched speaker-listener pairs. We release the model weights, renderer, and serving backend under component-specific licenses.

---


### 130. [An Iterative LangGraph Agent for Text-to-SQL: Natural Language Access to the Chicago Crime Database](https://arxiv.org/abs/2609.22917)

**<font color=#1a73e8>作者：</font>** Vigneshwar Ravi Rao, Rupesh Swarnakar, Fayeq Jeelani Syed†  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Non-technical stakeholders frequently cannot write the SQL needed to extract insights from operational databases. We built and evaluated a Text-to-SQL agent that closes this gap end to end: a six-node LangGraph StateGraph checks question relevance, fetches the live schema, generates PostgreSQL, validates it with a dry run, retries on failure, executes the query, and narrates the result set in plain English. The agent uses prompt engineering only; no model was fine-tuned. We evaluated it on the Chicago Crime dataset (approximately 8.5 million records, 22 attributes) against a hand-built benchmark of 100 natural language questions with ground-truth SQL, stratified into 30 Easy, 40 Medium and 30 Hard items. Comparing two prompt revisions of the same agent, the revised system (V2) reached a Valid SQL Rate of 93% (from 87%), an Execution Accuracy of 60% under a hybrid relational equivalence metric (from 47%; 19% from 12% under strict JSON matching), and a mean Synthesis Quality of 4.34 out of 5 (from 3.91). The single largest driver was removing a LIMIT 10 instruction from the system prompt, which had been truncating multi-row answers. Error analysis attributes the residual failures to relevance-checker false rejections, ambiguous question semantics, and free-tier API rate limits rather than to the language generation step. We report no comparison against an external baseline system or a public benchmark; the study is a single-model engineering evaluation.

---


### 131. [Computationally efficient safe exploration in reinforcement learning](https://arxiv.org/abs/2609.22919)

**<font color=#1a73e8>作者：</font>** Shreeram Murali, Shankar A. Deka, Dominik Baumann  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning in real-life applications requires safety guarantees during exploration. Typical reinforcement learning algorithms do not provide such guarantees, and many modifications that do rely on Gaussian processes (GPs), which have a large computational cost. We propose a computationally lightweight algorithm based on the Nadaraya-Watson estimator that safely explores and optimizes constrained Markov decision processes (MDPs). Our algorithm, \textsc{CoLSafe-MDP}, uses an estimator that scales in constant-time with bounds on the estimates, a significant improvement from its GP-based counterparts that scale cubically with the number of data points. We then evaluate its performance in a grid-based environment and on observational Martian terrain data.

---


### 132. [Joint Domain-Class Modeling for Federated Learning Under Feature Skew](https://arxiv.org/abs/2609.22932)

**<font color=#1a73e8>作者：</font>** Sina Najafi, Mostafa Tavassolipour, Seyed Pooya Shariatpanahi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) enables collaborative model training without centralizing private data, but performance often degrades under feature skew: clients share labels while the conditional input distributions $p_i(x\!\mid\!y)$ vary due to latent, client-specific appearance factors. We propose Joint Domain-Class Federated Learning (JDFL), a lightweight, optimizer-agnostic extension that makes this latent domain variation usable without sharing raw data. JDFL first infers domain clusters called pseudo-domains from brief local update signals. It then expands the classifier head to output $M\times C$, joint (domain-class) logits. This allows the model to represent domain-conditioned appearance while keeping a shared backbone. To train the expanded head we introduce two complementary supervision strategies based on simple intuitions: a similarity-aware soft-labeling that transfers evidence between nearby inferred domains while allowing domain-specific specialization, and a per-sample randomized target assignment that perturbs supervision across the joint outputs and serves as a low-cost training-time regularizer. JDFL integrates with existing standard FL methods (e.g., FedAvg, SCAFFOLD) with minimal changes. Empirically, both supervision modes consistently improve global test accuracy on standard domain-shifted image benchmarks; ablations and sensitivity studies show the gains stem from the proposed supervision and parametrization rather than mere capacity increase.

---


### 133. [D3GS: Depth, DINO, and RGB Diffusion Co-Guided 3D Gaussian Splatting for Sparse-View Reconstruction](https://arxiv.org/abs/2609.22941)

**<font color=#1a73e8>作者：</font>** Yunqi Gao, Zhanfeng Liao, Hanzhang Tu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Novel view synthesis from sparse inputs remains challenging for 3D Gaussian Splatting (3DGS) due to ambiguous geometry, cross-view inconsistency, and missing details in under-constrained regions, resulting in degraded reconstruction and unstable rendering. To tackle these issues, we propose D$^{3}$GS, a Depth-DINO-Diffusion guided sparse-view Gaussian reconstruction framework that jointly enhances geometry and appearance. D$^{3}$GS first recovers a high-resolution, metric depth map via diffusion-based completion and DPT (Dense Prediction Transformer) refinement, providing robust Gaussian initialization and geometric constraints. Then, a DINO-guided view-consistent learning is introduced to augment Gaussian attributes with structural features, improving multi-view consistency. Finally, a diffusion-based Gaussian refinement module injects generative priors into an iterative optimization strategy, enhancing high-frequency geometric and appearance details within the Gaussian representation. Experiments on DTU, LLFF, and Mip-NeRF 360 show that D$^{3}$GS achieves consistent and substantial improvements over strong baselines, with ablation studies validating the effectiveness and complementary roles of each component.

---


### 134. [RewardVerse: Rubric-Guided Policy Optimization for Video Reward Modeling](https://arxiv.org/abs/2609.22947)

**<font color=#1a73e8>作者：</font>** Zhenchen Tang, Yang Li, Songlin Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) is vital for optimizing video generation models, with a robust reward model (RM) serving as the cornerstone. However, existing video reward models often produce unstable scalar scores because they directly map complex, subjective video quality into a single score without explicit evaluation criteria. This leads to scalar drift, where the scoring scale collapses or shifts across different prompts, making the reward unreliable for RL. Drawing inspiration from professional human annotation engineering, we address this problem with RewardVerse, a rubric-based video reward framework that introduces a dynamic rubric as an intermediate representation between the evaluation query and the scorer. Instead of unconstrained direct scoring, RewardVerse first generates explicit evaluation criteria and then performs rubric-guided scoring, providing a stable semantic anchor that mitigates scalar drift. To efficiently optimize this collaborative pipeline, we propose Rubric-Guided Policy Optimization (RGPO), a two-stage training algorithm. RGPO first warms up the scorer using self-evolving seed rubrics and then jointly optimizes the rubric generator to produce query-adaptive evaluation criteria while continuously aligning the scorer with human ratings. Extensive experiments on the 16-dimensional EvalVerse benchmark and external datasets demonstrate that RewardVerse mitigates scalar drift, achieves state-of-the-art performance on both pointwise and pairwise evaluation, and provides a robust and interpretable reward signal for RL in video generation.

---


### 135. [CLEAR: Complex Learned Explicit Analytical Regularization for Ultra-Accelerated 4D Flow CMR Reconstruction](https://arxiv.org/abs/2609.22950)

**<font color=#1a73e8>作者：</font>** German Shâma Wache, Sebastian Neumayer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While compressed-sensing regularizers enable interpretable reconstruction of 4D Flow CMR through transparent variational objectives, their hand-crafted nature is too restrictive under high acceleration. State-of-the-art learning-based approaches mitigate this, but typically encode regularization implicitly through unrolled network modules, which limits their interpretability. To address this limitation, we propose CLEAR, designed to combine the interpretability of compressed sensing with the flexibility of learned models. To the best of our knowledge, it is the first learned regularizer for a 4D reconstruction task. In the ultra-accelerated \(10\times\)--\(50\times\) regime of the CMRx4DFlow2026 challenge, CLEAR outperforms compressed sensing locally low-rank (LLR) and the popular variational network FlowVN, while using less than 10k parameters and preserving an interpretable regularization structure.

---


### 136. [A Compact Stance-Indexed Anterior-Posterior COP Representation for Parkinson's Disease Classification from Plantar VGRF](https://arxiv.org/abs/2609.22956)

**<font color=#1a73e8>作者：</font>** Md. Sifat, Sania Akter, Akif Islam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Parkinson's disease alters gait and bilateral coordination, but machine-learning performance also depends on how continuous gait signals are represented. This study investigates whether preserving anterior-posterior center-of-pressure (AP-COP) information at fixed locations across normalized stance provides a compact and informative representation of plantar-force gait signals. Bilateral vertical ground reaction force recordings from 165 participants in the Gait in Parkinson's Disease Database were evaluated using repeated fully nested participant-level cross-validation. We propose AP-COP10, comprising AP-COP position and bilateral asymmetry across five stance windows. AP-COP10 achieved an AUC of 0.894 and outperformed three harmonized literature-derived COP representations under the same evaluation pipeline. The complementary 25 non-AP-COP descriptors alone achieved an AUC of 0.856, while the complete 35-feature representation achieved 0.908. Removing AP-COP10 from the complete representation produced a statistically supported loss in discrimination, whereas adding the complementary descriptors to AP-COP10 yielded only a small, unsupported improvement. Feature competition indicated that the most informative stance-indexed descriptors were concentrated in early and early-mid stance, while source-study holdout and sensor-perturbation analyses supported the robustness of the representation. These findings indicate that stance-indexed AP-COP retains discriminative information that is not readily recovered by broader engineered gait descriptors, supporting compact and interpretable representations for machine-learning analysis of pathological gait.

---


### 137. [R-GEAN: Regimen-Guided Edit Action Network for Within-Admission Medication Change Prediction](https://arxiv.org/abs/2609.22959)

**<font color=#1a73e8>作者：</font>** Regan Mahat, Mansu Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The medications prescribed to a patient often change during a hospital admission as clinicians start, stop, or continue therapies. We study whether models can predict which medication classes are added or removed between 24 hours after admission and discharge. Metrics that compare the complete discharge regimen can reward models for copying medications that remain unchanged, even when they identify no actual changes. We therefore introduce a leakage-controlled benchmark that predicts net ATC3 additions and removals using only prior completed admissions and information available within the first 24 hours of the current admission. Addition candidates are classes not active at 24 hours, whereas removal candidates are classes active at that time. We also introduce R-GEAN, an asymmetric candidate-scoring network with independent addition and removal predictors. Across 240,480 admissions from 82,286 patients, R-GEAN achieves the highest predefined summary of addition, removal, changed-regimen, and action-pattern performance, termed the edit composite (0.464), compared with 0.435 for the strongest primary comparator. Reimplemented RETAIN, GAMENet, and MICRON baselines obtain 0.428, 0.420, and 0.288, respectively. R-GEAN's advantage is concentrated in correctly identifying medication classes no longer active at discharge, while rare additions and admissions with multiple medication changes remain difficult. Rankings based on micro-F1 over the reconstructed discharge regimen and the edit composite correlate weakly across the evaluated models (Spearman r = 0.20). The continuation baseline achieves the highest complete-regimen score despite predicting no additions or removals. These results show that complete-regimen and edit-level evaluation measure different aspects of medication prediction. The benchmark evaluates observed prescribing changes, not treatment appropriateness

---


### 138. [When Agentic Trust Crosses Organizational Boundaries: Structural Externalization and a Reference Model for Trust Evidence](https://arxiv.org/abs/2609.22961)

**<font color=#1a73e8>作者：</font>** Huafu Li, Jia Xia  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic systems increasingly invoke tools, services, data, and other agents across organizational boundaries, yet a relying party cannot assess a delegated action solely from producing-domain controls and records. This paper develops Trustworthiness as a Service (TaaS) through a synthesis of trustworthy-AI governance, agent security, distributed trust management, identity, provenance, assurance, and control-plane research. The analytical unit is a cross-domain reliance proposition that names the issuer, subject and action, relying party, administrative boundary, evidence dependencies, adverse condition, and required verification or adjudication semantics. The three-condition structural-externalization diagnostic identifies propositions that depend on multiple domains, require producer-independent reliance, and must remain reviewable after revocation, failure, conflicting records, or dispute. For such propositions, the paper specifies a trust-evidence envelope: an immutable workflow manifest linked to append-only, issuer-attributed attestations for task-scoped authority, policy and execution decisions, provenance, validity, disclosure, status, challenge, and recovery. A topology-neutral logical reference model assigns these functions to explicit roles and trust domains. Three analytical scenarios and the TaaS-Eval protocol proposal define manifests, independent consumers, hard gates, adversarial evidence tests, metrics, and reproducible artifact reporting. By composing established identity, authorization, provenance, assurance, and governance mechanisms around a bounded delegated action, TaaS provides a reusable profile for cross-domain reliance. It makes evidence dependencies, independent verification, challenge, and recovery explicit, supporting interoperable governance and future evaluation without treating producer assertions as ground truth.

---


### 139. [General Collaborative Intelligence: Architecting Cognition for Resilient Multi-Agent Ecosystems](https://arxiv.org/abs/2609.22967)

**<font color=#1a73e8>作者：</font>** Lei Zhang, Chun Ye, Le Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-agent unmanned systems are moving from isolated, ego-centric sensing toward collaborative intelligence, in which distributed agents exchange compact features to overcome a local observation trap that no single agent can escape: occlusions, finite sensor range, and environmental degradation. The field has matured across architectural, communication, embodied, resilience, and trust dimensions, yet existing surveys examine these dimensions in isolation and rarely expose their dependencies. This review offers a unified synthesis through two complementary lenses. The first is a five-dimensional taxonomy spanning collaboration stage, communication paradigm, fusion architecture, learning strategy, and application domain. The second is three cognitive synergy conditions, Semantic Disambiguation, Pragmatic Information Exchange, and Proactive Informational Foraging, that turn cognitive synergy into operational criteria. Across these lenses we survey collaboration architectures and topologies, neural-communication co-design that treats the channel as a differentiable pipeline component, embodied action-perception loops via multi-agent reinforcement learning, and resilience mechanisms for synchronization, uncertainty quantification, and label-efficient learning. We then map these advances onto four operational domains, V2X, unmanned aerial, industrial logistics, and smart cities, and onto the safety-privacy-utility triad. To counter benchmark saturation and evaluation fragmentation, we propose GCI-Bench, a five-pillar scoring protocol with a maturity model that makes the trade-offs of collaborative methods comparable across studies. A critical reflection on reproducibility, the sim-to-real gulf, and conditions under which collaboration degrades performance identifies open challenges and charts directions toward general collaborative intelligence under real-world uncertainty.

---


### 140. [Dual-Locking Learned AI Models: A PIN-Based Sparse QIM Watermarking and Adaptive Index Permutation Approach](https://arxiv.org/abs/2609.22981)

**<font color=#1a73e8>作者：</font>** Iva Vasic, Jesús Muñoz-Cádiz, Bata Vasic  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present a dual-locking method for securing trained neural networks that combines key-driven index permutation with PIN-based watermarking based on Sparse Quantization Index Modulation (QIM). Cryptographic randomness is introduced by independently applying a uniform random permutation to each row of adaptively selected index vectors. A robust blind binary watermark is then embedded into the bias coefficients by modulating their quantized values, binding the network to a user-defined Personal Identification Number (PIN). Without the correct key, the network retains its architecture but becomes functionally impaired due to disrupted internal representations. Inverse permutation fully restores the original model accuracy, while the embedded watermark remains imperceptible and enables blind verification of key association and model authorship. To improve both locking effectiveness and recoverability, an adaptive key selection strategy redistributes high-magnitude weights to low-sensitivity positions and vice versa, increasing degradation in the locked state while preserving full recovery. Experiments on MNIST, CIFAR-10/100, and ImageNet-1K using fully connected networks, ResNet CNNs, and transformer architectures show that locking reduces accuracy below 10\%, and even below 0.5\% for CNNs, while the correct key fully restores performance. The watermark introduces no measurable accuracy degradation and reliably authenticates ownership. Analysis of embedding distributions across CNNs and transformers further indicates potential diagnostic value for identifying undertrained or suboptimally designed models. The proposed approach therefore provides simultaneous model protection, recovery, and ownership verification.

---


### 141. [LPINNs: First-Layer Gated Localization for Physics-Informed Neural Networks](https://arxiv.org/abs/2609.22984)

**<font color=#1a73e8>作者：</font>** Lakshay Chawla, Hardik Jain  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) use one shared representation over the computational domain, which can become difficult to optimize on long domains and for high-order operators. We study a minimal alternative: multiply the first hidden activation of an otherwise unchanged dense PINN by input-dependent localization functions, giving first-layer units receptive fields without partitioning the domain or adding interface losses. We screen 13 families of localization functions, in up to three parameterizations each, on a nonlinear harmonic oscillator (HO), a heat equation on a long spatial interval, and a manufactured four-dimensional (4D) fourth-order problem, with ten paired seeds throughout. Three configurations give large reductions in solution error at matched budgets: (i) Fixed Gaussian localization functions on the $2\pi$ HO domain cut mean solution RMSE from $4.8369\times10^{-1}$ to $8.83\times10^{-3}$ at 3k epochs. (ii) The inverse-quadratic family with learnable centers and widths cuts it from $2.896\times10^{-1}$ to $3.06\times10^{-2}$ on the $8\pi$ heat domain at 10k epochs. (iii) Fixed bump localization functions cut it from $1.75947\times10^{1}$ to $2.260\times10^{-1}$ on the $4\pi$ 4D domain at 10k epochs. Every paired seed improves in these three comparisons. The screen also shows that the mechanism is not a free win: on HO only 2 of 13 families beat the baseline, and 10 of the remaining 11 are 9 to 23 times worse; on 4D four families are non-finite and five are more than three orders of magnitude worse than the baseline. The inverse-quadratic family is the only one that beats the baseline on all three equations. Overall, these results show that first-layer localization can provide measurable improvements to baseline PINNs on long-domain and high-order problems.

---


### 142. [Adaptive Scaffolding Needs Contingency: An AI Tutor That Escalates and Fades on What the Learner Does](https://arxiv.org/abs/2609.22993)

**<font color=#1a73e8>作者：</font>** Xinmeng Hou, Yuxuan Weng, Chin Hsien Yeh 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Coding assistants raise task performance, but learners plan and monitor less. Giving less away, the usual fix, conflates two things: how much work a system carries (cognitive load) and what the learner must decide before help arrives (metacognitive demand). Our principle, preserved metacognitive demand, holds the second constant and lets the first vary. CoMeT implements it: support rises when a learner fails at a decision point and fades on take-up. Within subjects, 131 adult learners used CoMeT, an unrestricted assistant and a question-only tutor on three Python tasks. CoMeT matched the question-only tutor's demand, delivered artifacts twice as often as the assistant, and frustrated learners less than the question-only tutor, with delegation and load unchanged. Learners often did not answer. Fading held when their turn addressed the decision under support, and CoMeT surrendered the full answer in one session in sixteen, against one in six for the question-only tutor.

---


### 143. [M3GA-Wild: A Large-Scale Dataset and Benchmark for Multi-Modal Multi-session Ground-to-Aerial Place Recognition in Forests](https://arxiv.org/abs/2609.23003)

**<font color=#1a73e8>作者：</font>** Ethan Griffiths, Maryam Haghighat, Simon Denman 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present M3GA-Wild, the first benchmark for multi-modal, multi-session ground-to-aerial place recognition in forests. M3GA-Wild unifies and extends existing forest localisation datasets, providing a holistic benchmark with synchronised RGB imagery and LiDAR from ground traversals spanning 36 km, aligned high-resolution aerial imagery and multi-altitude LiDAR covering 370 hectares, and accurate geo-referenced 6-DoF poses for precise evaluation. M3GA-Wild captures diverse forest scenes with varying viewpoints, occlusion, and environmental conditions, enabling systematic evaluation of visual, LiDAR, cross-modal, and multi-modal methods. Baseline experiments show that LiDAR-based approaches significantly outperform vision-only methods under severe viewpoint differences, while current multi-modal fusion strategies yield limited gains due to poor cross-modal alignment. By pairing aerial RGB imagery with geo-referenced aerial LiDAR, M3GA-Wild also enables evaluation of foundation models for monocular depth estimation as a cheap source of 3D geometry from forest imagery, with initial experiments revealing shortfalls of current methods. These results highlight key challenges in cross-platform localisation, including modality misalignment and severe domain gaps. M3GA-Wild establishes a new benchmark to support research in robust multi-modal localisation and long-term autonomy in unstructured natural environments. The dataset and code will be available upon acceptance.

---


### 144. [Compressing 3D Gaussian Splatting via Cross-Representation Priors](https://arxiv.org/abs/2609.23005)

**<font color=#1a73e8>作者：</font>** Yezheng Zhang, Huanxiong Liang, Chuqin Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) enables high-quality novel view synthesis but incurs high storage and transmission costs due to dense Gaussian primitives. Recent anchor-based compression reduces per-primitive redundancy, yet redundancy across anchors remains largely unexploited. We propose CRP-GS (Cross-Representation Priors for Gaussian Splatting), a rate-distortion optimized compression framework that leverages cross-representation priors to improve anchor-level entropy modeling. First, a Correspondence-Oriented Hierarchical Structure (COHS) organizes anchors by feature correspondence rather than spatial proximity, constructing root-leaf dependencies so that selected anchors can act as informative priors to conditionally encode others, yielding more accurate likelihood prediction and lower conditional entropy. Second, Shared Feature Aggregation (SFA) extracts globally shared features from a contextual hash grid and injects them into anchor representations, factoring out scene-consistent low-frequency information that would otherwise be redundantly embedded in individual anchors. Both modules are trained under a unified rate-distortion objective to balance bitrate reduction and rendering fidelity. Experiments across multiple benchmarks show that CRP-GS achieves a favorable overall rate-distortion trade-off, yielding around 30% average bitrate reduction compared to anchor-based baselines while maintaining comparable rendering quality.

---


### 145. [Interpretable Multi-Hypersphere Deep Anomaly Detection for Open-set Supervised Anomaly Detection](https://arxiv.org/abs/2609.23008)

**<font color=#1a73e8>作者：</font>** Zhiji Yang, Fangyong Wang, Yue Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-class open-set anomaly detection requires a model to characterize the normal acceptance domain formed by multiple heterogeneous subdistributions using only class-labeled samples from known normal classes, and to identify previously unseen anomalies at test time. Existing single-hypersphere methods cannot explicitly represent class-specific locations and acceptance ranges, while current multi-hypersphere or multi-class approaches do not fully integrate inter-class boundary constraints, learnable acceptance ranges, and interpretable decisions. To address these limitations, we propose Interpretable Multi-Hypersphere Deep Anomaly Detection (IMHD-AD). IMHD-AD constructs an independent hypersphere for each known normal class in a shared feature space. With target-inside and non-target-outside constraints, IMHD-AD embeds the class-specific hypersphere centers and radii directly into the final network layer and jointly optimizes them with the shared representation. The minimum signed boundary score across hyperspheres simultaneously determines open-set acceptance or rejection and provides a faithful geometric explanation of each decision. On MNIST, Fashion-MNIST, and CIFAR-10, IMHD-AD achieves the highest AUC in 28 of 30 open-set comparisons. A two-dimensional synthetic study further shows that model architecture must balance the compactness of known normal classes against the separability of unknown anomalies.

---


### 146. [MixiMotion: One-Step Text-to-Motion Generation via Asymmetric Set Distillation](https://arxiv.org/abs/2609.23010)

**<font color=#1a73e8>作者：</font>** Hung Dinh, Binh Mai, Tran Quoc Bao Le 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Iterative text-to-motion generation delivers high-quality and semantically aligned motions but requires multiple network evaluations, resulting in substantial inference latency. We present \textbf{MixiMotion}, a strict one-step text-to-motion generation framework based on offline set distillation. Instead of distilling a single teacher trajectory for each text prompt, MixiMotion constructs an offline bank of multiple teacher motions and aligns teacher and student sample sets through \textbf{asymmetric bidirectional matching}. The teacher-to-student direction promotes coverage of diverse teacher-supported motions, while the student-to-teacher direction suppresses unsupported generations. We further introduce differentiable decoded-space kinematic supervision to complement normalized representation matching with constraints in the decoded motion space. At inference, MixiMotion generates a complete motion sequence with a single network evaluation, without teacher queries, iterative sampling, or candidate ranking. On ViMoGen, MixiMotion achieves a semantic alignment score of $0.835$, outperforming the evaluated one-step baselines and approaching the $0.858$ score of its 50-step HY-Motion-1.0-Lite teacher. In blinded human evaluation, MixiMotion obtains an overall rating of $4.33$, compared with $4.50$ for the teacher, while outperforming the evaluated one-/few-step baselines. Meanwhile, generation latency is reduced from $829.58$\,ms to $9.30$\,ms, corresponding to an $89.2\times$ speedup. These results demonstrate an effective quality--efficiency trade-off for strict one-step text-to-motion generation.

---


### 147. [Reconstructed holograms and explanation-aware evaluation for low-cost computational pollen analysis in veterinary cytology](https://arxiv.org/abs/2609.23017)

**<font color=#1a73e8>作者：</font>** Swarn Warshaneyan, Joial Danyal, Blaž Cugmas 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated pollen analysis supports veterinary cytology, but brightfield microscopy is costlier and more complex than lens-less digital in-line holographic microscopy. We evaluate whether reconstructed holograms can narrow this gap and whether model explanations remain reliable under modality change. Six pollen species were imaged by brightfield and holographic microscopy. Raw, single back-propagation and iterative phase retrieval holograms were evaluated with YOLOv26s detection and MobileNetV4 classification after anchor-based annotation transfer. Six attribution methods were assessed for spatial grounding and faithfulness with the Attribution Health Inspection and Repair (AHIR) protocol, which tests model brittleness under weak noise and corrects attribution-map granularity when needed. Brightfield achieved 0.6890 mAP50-95 (0.8865 mAP50) for detection and 0.9687 macro-F1 (0.9705 accuracy) for classification. Reconstructed holograms narrowed the gap with a task-dependent split: p-type was strongest for detection at 0.5324 mAP50-95 (0.8229 mAP50), while r-type was strongest for classification at 0.7695 macro-F1 (0.7866 accuracy), both far above raw-hologram baselines. Activation-based explanations localized strongly on grains, and region-based methods retained ~60 to ~80% of faithfulness under holography. The holographic detector was highly brittle to weak perturbations, saturating deletion-based evaluation while insertion remained informative. Pixel-level gradient explanations approached random floor, yet spatial smoothing restored p-type gradient faithfulness from 0.05 to 0.51. For holographic classification, perturbation-based explanations remained faithful while gradient-based methods fell below random floor. Reconstruction improves low-cost holographic pollen analysis, while AHIR distinguishes genuine attribution failure from artifacts caused by model brittleness and map granularity.

---


### 148. [BrainIAC: Interactive 3D Brain Lesion Segmentation across Heterogeneous MRI Modalities with Online Adaptation](https://arxiv.org/abs/2609.23026)

**<font color=#1a73e8>作者：</font>** Wentian Xu, Anthony P Addison, Ziyun Liang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Brain lesion segmentation is a fundamental task in medical image analysis, playing a critical role in diagnosis, treatment planning, and longitudinal disease monitoring. Yet existing models still struggle to meet the demands of real clinical use, where deployments contain data distribution shifts, arising from differences in scanner hardware, imaging protocol (varying MRI modality sets), and new pathologies. We present BrainIAC (Brain lesion Interactive Adaptive Continuously learning segmentation), a unified framework that integrates (i) a multi-modal backbone network trained to segment multiple types of brain lesions and handle heterogeneous sets of modalities via zero-filling and random modality dropping; (ii) 3D interactive segmentation with bounding-box and click prompts that preserves fully automatic prediction when no prompt is given; and (iii) an online adaptation mechanism combining Mid-Interaction adaptation and Post-Interaction adaptation, supervised by the network's own predictions as pseudo labels and guided by an extra Click-Centered Gaussian loss. To our knowledge, this is one of the first 3D online adaptation methods for interactive segmentation, and the first to combine handling of heterogeneous modality sets with online adaptation. Experiments across seven brain MRI datasets demonstrate that the proposed components provide complementary and synergistic benefits. The method consistently outperforms existing approaches and generalizes well across heterogeneous imaging modalities, including those unseen during training, as well as previously unseen brain pathology types. The code and a 3D Slicer plug-in will be released at this https URL upon publication.

---


### 149. [VDGS: Visibility-Driven Large-Scale 3D Gaussian Splatting for Aerial Scene Reconstruction](https://arxiv.org/abs/2609.23049)

**<font color=#1a73e8>作者：</font>** Haolin Yu, Jiadong Tang, YiXian Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale scene reconstruction is a critical foundational technology in robotic autonomous systems such as 3D mapping and autonomous driving. In recent years, 3D Gaussian Splatting (3DGS) has demonstrated remarkable advantages in both visual quality and computational efficiency, making it a promising representation for large-scale scene reconstruction. However, it still faces challenges in large-scale scenes, including excessive memory consumption and uneven viewpoint coverage caused by UAV acquisition, limiting its real-world applications. To address this, we propose VDGS, a novel 3DGS framework that incorporates camera distribution into scene modeling. VDGS introduces visibility-driven statistics for scene anchors to quantify supervision strength. These statistics are further leveraged for scene partitioning and for gradient compensation in under-optimized regions, thereby promoting balanced optimization across different regions. Extensive experiments on multiple large-scale aerial scene datasets demonstrate that, under imbalanced viewpoint distributions, VDGS consistently outperforms existing methods, while maintaining competitive performance in scenarios with more uniform view distributions.

---


### 150. [LazyAgent: Demand-Driven Materialization and Physical Optimization of Agentic Programs](https://arxiv.org/abs/2609.23058)

**<font color=#1a73e8>作者：</font>** Xin Heng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current agent runtimes that plan before acting generally execute a step once it becomes ready. We present LazyAgent, a unified execution framework for agent-authored programs organized around a live, goal-derived demanded set. LazyAgent refreshes a backward closure from requested outputs as execution state changes and materializes a ready node only when the active goal requires it. This replaces repeated local judgments with one linear-time graph analysis followed by constant-time membership tests, allowing programs to remain broad while execution stays request-specific. On programs that describe more than the current request needs, LazyAgent consistently outperforms the strongest goal-stopping eager baseline by refusing unrelated work before it starts. Adding one unrelated product raises the eager bill by 22.5% and LazyAgent's by 0.0%. LazyAgent saves 42.0% of measured CPU on production scientific workflows and 51.7% of container time on a live release gate spanning four repositories. We also prove and verify exact equivalence when the request reaches the whole graph, leaving no unrelated work to avoid. Beyond permission, goal-relative output projection saves up to approximately 90% of a shared step on two third-party test suites while the identical eager control saves 0.0%; the advantage disappears when the omitted output has no other consumer or the request needs it. Ordering, reuse, and pruning can also save cost, but do not replace permission. Finally, we show that current public benchmarks are eager-shaped and contain almost no unrequested work. A pre-registered planning intervention did not broaden them. These findings motivate benchmarks built from standing programs and sequences.

---


> [!TIP]
> 当前位于：**101-150**（第 3/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-463](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
