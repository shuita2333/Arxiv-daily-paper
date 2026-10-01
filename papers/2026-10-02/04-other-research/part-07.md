# 📦 其他研究 | 2026年10月02日

> 本类共 **382** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-350**（第 7/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-382](./part-08.md)

---

### 301. [Path-Finding, Orbit State Preparation, and the Security of Invariant Quantum Money](https://arxiv.org/abs/2609.39774)

**<font color=#1a73e8>作者：</font>** Hans Schmiedel, Jiangshan Yu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The security of quantum money from knots, and of its generalization to invariant money, is based on the assumption that path-finding, exhibiting a sequence of moves between two equivalent objects, is hard. No proof of security from that assumption alone is known. The existing proofs add knowledge-of-path assumptions, which assert that any efficient algorithm producing two objects with the same invariant implicitly knows a path between them. No attack can refute such an assumption, and it is not known to follow from security.
We ask when path-finding is the right assumption. When each equivalence class is the orbit of an efficiently computable action of a group that can be superposed over, and every move acts as a group element, as for graphs, average-case hardness of path-finding is necessary for security. For knots no such group is known, and a path-finder only reduces forgery to an equally hard state-preparation problem.
With or without a path-finder, a forger must prepare a state that verification accepts, and we take the hardness of that task as the assumption. For schemes whose verification walk mixes in polynomial time, the preparation assumption states that no efficient algorithm, given the serial number of a freshly minted banknote and one object measured from it, prepares such a state. It is falsifiable, and it is equivalent to security against forgers that measure their banknote first. The transfer assumption, which security implies, states that measuring first costs a forger at most a polynomial factor. Together the two are equivalent to security, so every proof of security must establish the preparation assumption. If the preparation assumption holds, no fully black-box reduction that calls the forger only at the serial number it is given can derive the transfer assumption from the preparation assumption.

---


### 302. [CORD: Learning Reusable Degradation Representations Across Heterogeneous Physical Systems](https://arxiv.org/abs/2609.39784)

**<font color=#1a73e8>作者：</font>** Haibo Li, Zhiguo Zeng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can heterogeneous physical degradation systems benefit from joint pretraining and move beyond system-specific prognostics toward reusable cross-system representation learning? CORD combines type-specific observation interfaces with a shared degradation backbone. Its two self-supervised objectives learn at complementary scales: Intra-Observation Structure Modeling (ISM) captures structure within observations, while Inter-Observation Dynamics Modeling (IDM) captures latent degradation evolution across observation histories. We evaluate CORD under two transfer boundaries: Pretraining-Included System Types, where downstream datasets and held-out units are unseen but their system types are represented during source pretraining, and Pretraining-Excluded System Types, where the entire turbofan-engine type is absent from pretraining. Across bearings, batteries, and cutting tools, CORD (Multi-domain) consistently improves over CORD (Single-domain) under Frozen adaptation, provides further gains under Full FT in most settings, and remains competitive with representative external baselines. Source-pretrained initialization also improves low-label adaptation to the pretraining-excluded engine type. Frozen-representation analysis further shows improved cross-unit lifecycle consistency after multi-domain pretraining. Joint pretraining across heterogeneous physical systems thus produces degradation representations reusable across devices, datasets, and system types.

---


### 303. [Seeing as Humans Do: Learning from Motion to Segment Anything Without Supervision](https://arxiv.org/abs/2609.39785)

**<font color=#1a73e8>作者：</font>** Weijian Jian, Xiaoyue Zhang, Bin Xiao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The Segment Anything Model (SAM) relies heavily on massive manual annotations, creating a fundamental bottleneck for model scaling. While unsupervised methods attempt to learn object concepts from motion, they typically overfit to moving entities, lacking both multi-granularity understanding and the ability to generalize to static objects. To overcome this, we introduce Motion-Grounded Segment Anything (MoSA), a highly scalable unsupervised framework that learns a transferable objectness prior from unlabeled videos. MoSA operates in three progressive stages: (1) automatically generating multi-granularity motion pseudo-labels from large-scale video data; (2) training a Perceptual Grouping Model (PGM) via contrastive learning to internalize a generalized, appearance-driven concept of objects; and (3) transferring this learned prior into a prompt-guided architecture for segment-anything-style inference on images. Extensive zero-shot evaluations across seven challenging benchmarks (e.g., COCO and ADE20K) demonstrate that MoSA significantly outperforms existing unsupervised methods. Notably, despite using zero manual annotations, MoSA achieves segmentation performance comparable to the fully supervised SAM. Our findings reveal that harnessing large-scale unlabeled motion is a feasible and highly scalable alternative to annotation-driven segment-anything pipelines.

---


### 304. [Privacy Foundations for Multi-Institutional Scientific Artificial Intelligence](https://arxiv.org/abs/2609.39787)

**<font color=#1a73e8>作者：</font>** Olivera Kotevska, Sumit Jha, Aurélien Bellet 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Scientific artificial intelligence (AI), spanning foundation models (FMs) to federated data-analysis pipelines, is becoming shared infrastructure across national laboratories, universities, hospitals, and industrial partners. This collaboration creates privacy risks whose natural unit is often an institution's participation, research strategy, or technical capability rather than a single record. Differential privacy (DP), federated learning (FL), secure computation, trusted execution, and provenance each protect parts of the stack, but their guarantees rarely compose across mixed-trust institutions, access tiers, and autonomous agents. This perspective recasts privacy for scientific AI as an assurance problem defined by six elements: protected asset, observer, channel, permitted disclosure, guarantee, and evidence. We demonstrate the framing through a claim register for a composite cross-institutional scenario and use it to assess the model lifecycle. Two of the resulting gaps are specific to leadership-class facilities: scheduler, allocation, and telemetry metadata expose an institution's resource posture, and instrument-attached control loops leak research strategy through timing and contention on shared accelerators. We identify six research priorities: institution-level guarantees, agent-communication privacy, cross-tier information flow, privacy-compatible reproducibility, leadership-scale accounting, and instrument side channels. The contribution is a common form for stating, comparing, and auditing claims whose guarantees otherwise remain fragmented across the scientific AI stack.

---


### 305. [Safety of Latent Communication in Multi-Agent Systems](https://arxiv.org/abs/2609.39788)

**<font color=#1a73e8>作者：</font>** Muhammad Huzaifa, Sina Mavali, Thorsten Eisenhofer  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Latent communication enables multi-agent systems to exchange information directly in internal representation space, reducing the token, computation, and latency overhead of text-based communication. To this end, lightweight trainable links are introduced to map the sender's representations into the receiver's input space. In this work, we show that even benign link training can increase harmful compliance relative to text-based communication while the underlying safety-aligned agents remain unchanged. An attacker can amplify this effect by optimizing the links on harmful query--response pairs or poisoning otherwise benign training data. We further develop a reinforcement-learning attack that rewards harmful compliance alongside benign task performance without requiring harmful target responses. Across three communication topologies and four safety benchmarks, this attack raises the mean harmful-compliance score from 27.9 with benignly trained links to 76.9. Compared with direct supervised optimization, it also achieves higher average accuracy on two benign utility benchmarks. Adapting the rewards toward safer behavior also enables repair of compromised links, substantially reducing harmful compliance across all evaluated attacks without updating the agents. Overall, our results show that safety alignment requires considering the multi-agent system as a whole.

---


### 306. [Pseudo-Label-Triggered Retraining from Forecast Errors for Online Time Series Forecasting](https://arxiv.org/abs/2609.39789)

**<font color=#1a73e8>作者：</font>** Yeryeong Kwak, Yoo-Min Jung, Jonghun Park  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world time series forecasting systems operate under non-stationary data streams, where forecasting performance may degrade over time. Although retraining can recover the performance, it incurs non-trivial computational and operational costs. Under limited deployment resources, the key challenge is therefore not only how to retrain but also when to retrain. While existing retraining policies often rely on indirect indicators such as drift alarms or model staleness, we instead use realized forecast errors as direct deployment feedback. In this paper, we propose PILOT (Pseudo-label-Informed Learned Online Trigger), an online retraining framework that learns when to retrain from forecast-error dynamics. Since ground-truth retraining labels are unavailable, PILOT constructs a pseudo-label from future increases in forecast error and trains a lightweight scorer to predict it from observed error states. At deployment, PILOT uses only completed forecast errors and serves as a plug-in module for arbitrary forecasting backbones without architectural modification. We evaluate PILOT under standard multivariate forecasting settings across eight benchmarks with three representative backbones---DLinear, iTransformer, and TimesNet. Across all three backbones, PILOT achieves state-of-the-art average-rank performance among retraining policies while maintaining a favorable performance--efficiency trade-off.

---


### 307. [TopTimeNet: Topologically-assisted time-series classification model](https://arxiv.org/abs/2609.39792)

**<font color=#1a73e8>作者：</font>** Sharareh Sayyad, Sophia Bazzi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distinguishing periodic from chaotic dynamics in a time series is a fundamental challenge in both physics and engineering. Yet, end-to-end learned architectures must discover both a representation and a decision boundary from data, at substantial cost. We introduce TopTimeNet, which decouples these tasks: a fixed, non-learned stage extracts a $42$-dimensional geometric and topological descriptor from Takens delay embeddings and persistent homology, and a lightweight learnable stage performs classification. On a benchmark of $49$ nonlinear dynamical systems, a $1{,}638$-parameter configuration matches the mean accuracy of one with $33\times$ more trainable parameters. Additionally, this approach delivers mean accuracy comparable to convolutional neural networks and surpasses the average performance of converged Transformer models, while requiring three to four orders of magnitude fewer trainable parameters. Robustness also depends sharply on where noise is introduced: TopTimeNet degrades gracefully under perturbations to its precomputed features, but degrades sharply when noise is introduced into the raw signal and the full feature-extraction pipeline is recomputed, showing that robustness to perturbations of the precomputed features does not imply robustness of the complete raw-signal-to-prediction pipeline. These results show that decoupling fixed geometric and topological feature construction from a lightweight discriminative stage can achieve comparable classification accuracy with substantially fewer trainable parameters.

---


### 308. [Probabilistic Adversarial Training](https://arxiv.org/abs/2609.39798)

**<font color=#1a73e8>作者：</font>** Andi Zhang, Xingyu Zhao, Siddartha Khastgir  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Building on a probabilistic perspective in which adversarial examples arise from the overlap between a distance-based distribution $p_{\mathrm{dis}}$ and a victim-classifier-induced distribution $p_{\mathrm{vic}}$, we start from a simple intuition: adversarial examples become harder to generate when these two distributions are pushed apart, as their overlap becomes smaller, thereby increasing robustness. This intuition naturally motivates a KL-based robustness objective. We then prove that $\mathrm{KL}(p_{\mathrm{dis}}\|p_{\mathrm{vic}})-\log Z_{\mathrm{vic}}$ is a lower bound on probabilistic robustness (PR), where $Z_{\mathrm{vic}}$ denotes the normalizing constant of $p_{\mathrm{vic}}$. Since PR is generally intractable to compute directly, maximizing this KL-based lower bound provides a tractable surrogate objective for improving PR. We further show that this objective recovers a scaled form of adversarial training, offering a probabilistic interpretation of adversarial training and a principled route to robustness improvement. We call the resulting method probabilistic adversarial training. Experiments show that it consistently improves PR, and ablation studies demonstrate that the induced scaling factor can even enhance the PR of non-probabilistic adversarial training methods.

---


### 309. [Finite-Horizon Fisher Memory in Two-Sided Power-Bounded Recurrent Systems](https://arxiv.org/abs/2609.39800)

**<font color=#1a73e8>作者：</font>** Jeonghoon Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We analyse allocation, admission and post-write retention in finite-horizon linear-Gaussian noisy recurrent memories. At every horizon, the directional Fisher memory $M_n$ satisfies $\operatorname{tr}M_n=N$: non-normality redistributes information but cannot raise its spherical average, while normal carriers satisfy $M_n=I$. For bi-power-bounded carriers, we derive uniform $1/n$ lag bounds, identify the limit of $M_n$ with the inverse of the classical Cesàro asymptotic limit of $W^\top$, and give finite-horizon error bounds. A time-varying coupling defines an end-to-end store operator. The writer-optimal direction need not be store-optimal. After writing ends, an invertible hold preserves the full stored Fisher matrix. Additive contamination bounded by $\alpha$ times the closure covariance retains at least $1/(1+\alpha)$ of that matrix; a covariance-aware decoder attains the corresponding accuracy. With recurrent carriers held fixed, training input masks and linear readouts approached the task-specific optimum in 160 runs, with median normalized Rayleigh efficiency above $0.998$. Binary accuracy matched the Gaussian prediction to mean absolute error below $0.002$ over more than four orders of magnitude in $J$. In a separate pre-specified study of 320 runs, trained masks followed the designated input-time objective in both carrier types, in 16 of 16 draws. These studies used development-seen carriers and are pre-specified validations, not blind holdouts. The same fixed design reproduced the objective-specific result in 16 of 16 draws on carriers unused before run commitment. Exact isolation preserved information, while a decoder fixed at its training horizon fell to chance; inverse-adjoint transport restored its sampled decisions to numerical precision.

---


### 310. [Making Sense of Animal-to-Human Drug Development Evidence: Stakeholder Practices, Challenges, and Requirements for AI Tools](https://arxiv.org/abs/2609.39808)

**<font color=#1a73e8>作者：</font>** Rosni Vasu, Simona E. Doneva, Benjamin V. Ineichen  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Animal models are widely used to study human biology and health interventions, yet translating findings from animal studies to humans remains challenging. Evidence across preclinical and clinical research informs experimental and translational decisions. Artificial Intelligence (AI) tools are increasingly reshaping how this evidence is searched, synthesized, and used, but it remains unclear how they should support the diverse stakeholders involved in assessing animal-to-human evidence. We conducted semi-structured interviews with 13 stakeholders to examine their evidence practices, challenges, and expectations for AI support. We found that stakeholders approach the same incomplete evidence base with different goals, expertise, and heuristics. Participants valued AI particularly for locating, screening, and extracting evidence, but were more cautious about automated interpretation and quality judgments. They emphasized transparency, source traceability, uncertainty communication, and human oversight. Based on these findings, we derive design implications for role-sensitive AI tools that support more systematic and transparent reasoning about animal-to-human translation.

---


### 311. [A Comprehensive Benchmark of Source-Free Universal Domain Adaptation on Time Series Representations](https://arxiv.org/abs/2609.39810)

**<font color=#1a73e8>作者：</font>** Romain Mussard, Fannia Pacheco, Maxime Berar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Source-Free Universal Domain Adaptation (SF-UniDA) extends Universal Domain Adaptation by removing access to source data at adaptation time while still handling label-set mismatches between domains. Despite growing interest in this setting for image data, no benchmark exists for time series, which are more challenging. We present the first SF-UniDA benchmark on time series. In addition, we provide the first study of pretrained foundation models as feature extractors for time series domain adaptation. In this context, we identify a critical and previously underexplored limitation of all existing SF-UniDA methods: the inference threshold for unknown-sample rejection is highly sensitive. We address this by proposing a plug-in auto-thresholding module that can be integrated into any SF-UniDA method. Experiments on three well-known time series datasets confirm the suitability of this module. They also highlight that foundation models do not systematically outperform classical backbones and that SF-UniDA tailored for time series is yet to be developed.

---


### 312. [Backward-State Policy Is Part of the Learning Algorithm](https://arxiv.org/abs/2609.39813)

**<font color=#1a73e8>作者：</font>** Shuxiao Xie, Shuyang Xie, Dezhi Ran 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-precision training rounds tensors that the backward pass reads again, often for several gradients; each use can read the forward's rounded value, the original, or a new random rounding. This backward-state policy looks like a memory and precision detail, settled by copy accuracy and final loss. We argue that it is part of the learning algorithm, and that neither check shows whether it is right. Copy accuracy does not decide the outcome: in three pairs of 390M runs with an emulated FP8 backward, training fails when attention's backward reuses the forward's rounded output and succeeds with a new rounding from the same distribution. Even the most accurate copy, the original itself, can be wrong by our reference: the gradient of the forward pass as it actually ran, with gradients passed through rounding unchanged. For example, a normalization output stored in low precision feeds two gradients: the gain's gradient needs the original, but the next layer's weight gradient needs the rounded value that layer multiplied. Final loss, the other check, does not rule out the error of reading the original for both: it persists in models trained with such a store, while planned loss comparisons stay within a margin fixed in advance. We therefore derive from this reference which value each use must read, or which substitute gives the same gradient on average with the forward held fixed, and check these per-use requirements on single operators, without training. In three tests using PyTorch and Transformer Engine, the requirements predicted beforehand whether reuse changes what the backward computes on average relative to an independent copy, and every prediction held. Backward-state policy is thus part of the learning algorithm: it should be specified and checked use by use, not settled by copy accuracy and final loss.

---


### 313. [Should I stay or should I show? Learning to selectively disclose information](https://arxiv.org/abs/2609.39818)

**<font color=#1a73e8>作者：</font>** Carlotta Giacchetta, Alessando Bogani, Cesare Barbera 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In many high-stakes settings, human decision-makers can acquire support information before making a decision. However, acquiring information is costly, and disclosure may fail to improve human decisions or may even impair them. We tackle this problem by studying selective disclosure, i.e., the problem of learning when to reveal support information to a human decision-maker under a budget constraint. We first show that the optimal policy is a threshold rule on the Value of Information (VoI), i.e., the expected reduction in human decision risk induced by disclosure. Since VoI is unknown in practice, we estimate the regime-specific human risks and bound the possible degradation of the resulting plug-in policy relative to lack of disclosure, as well as its regret relative to the optimal policy. Experiments on benchmark datasets show that selective disclosure outperforms both no disclosure and full disclosure, regardless of whether the support information is beneficial or harmful. Two user studies show that human-AI team performance can improve when disclosure is led by our learned policy and not human-selected, although this advantage varies across tasks. A counterfactual benchmark, which replaces participants' predictions with a machine-learning prediction when disclosure occurs, suggests that these differences might depend on lower adherence to advice when the information is automatically provided rather than self-requested.

---


### 314. [P-SRM: Selective Recovery of Rejected Predictions in Visual Tracking](https://arxiv.org/abs/2609.39832)

**<font color=#1a73e8>作者：</font>** Youbin He, Siwei Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many visual tracking methods use rejection mechanisms to suppress unreliable predictions. However, these mechanisms can also reject correctly localized candidates, leaving useful information unused. We investigate how to identify and recover these candidates while preserving native accepted outputs and candidate coordinates. To this end, we propose P-SRM (Post-rejection Selective Recovery Method), which combines spatial responses, past accepted states, and native decision margins to reassess candidates and selectively restore reliable predictions. We evaluate P-SRM on six trackers and four datasets spanning category-specific, point, and generic object tracking. Across all nine configurations, P-SRM improves rejected-candidate ranking and overall tracking performance. These results show that post-rejection verification can identify and recover useful predictions discarded by native rejection, demonstrating the value of reusing rejected information. Project repository: this https URL.

---


### 315. [RainAtlas: A Multi-Continental Dataset for Precipitation Downscaling](https://arxiv.org/abs/2609.39833)

**<font color=#1a73e8>作者：</font>** Pierre-Louis Lemaire, Luca Schmidt, Wietze Suijker 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Extreme rainfall events are increasing in intensity and frequency as climate change accelerates. While kilometer-scale precipitation forecasts are critical for supporting local decision-making, the limited availability of high-resolution precipitation observations hinders their accuracy, especially in under-resourced regions. Machine learning models are widely used to downscale precipitation data to km-scale, but their application to unseen geographies presents challenges. First, processing raw high-resolution precipitation datasets across regions requires significant engineering and domain expertise. Second, generalization across regions remains difficult. To help overcome these barriers, we release RainAtlas, a large-scale, ML-ready and multi-continental dataset for precipitation downscaling. Covering three continents, RainAtlas harmonizes heterogeneous hourly km-scale observations to a common 2-km grid. Each regional partition contains around 210,000 aligned low- and high-resolution precipitation pairs, respectively from ERA5 reanalysis and direct observations. We benchmark state-of-the-art ML-based downscaling models across RainAtlas using a wide range of metrics. Our evaluation reveals substantial variance in out-of-domain generalization depending on the training regions. This underscores the need for cross-regional, multi-source km-scale evaluation, establishing RainAtlas as a well-positioned benchmark for precipitation downscaling research.

---


### 316. [Fast Regularized Policy Mirror Descent with One-Step TD Updates](https://arxiv.org/abs/2609.39837)

**<font color=#1a73e8>作者：</font>** Qipei Chen, Wenye Li, Yule Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Policy mirror descent (PMD) enjoys fast convergence in regularized Markov decision processes (MDPs), but existing guarantees often rely on exact or increasingly accurate policy evaluation. We analyze PMD coupled with a persistent critic advanced by one temporal-difference (TD) update. For finite discounted MDPs, we establish global linear convergence in value for exact coordinate-wise Bellman updates, with any positive constant actor stepsize and arbitrary finite critic initialization. The proof combines a resolvent-based auxiliary distribution with a decaying Bellman-violation correction and a potential weighted by inverse coordinate weights. We then study stochastic TD-PMD with general strongly convex mirror maps under a single off-policy Markov trajectory. With suitably chosen constant stepsizes and a finite-batch TD update, the method achieves an expected value gap of $\epsilon$ after $\widetilde{O}(1/((1-\gamma)^5 \widetilde{\sigma}_b \epsilon))$ transitions. The stochastic analysis relies on the trajectory-wise Lipschitz continuity of the regularizer, derived from uniform bounds on vertex Bregman divergences, together with a visitation-weighted resolvent estimate for signed critic-error propagation that yields an inverse-linear dependence on behavior coverage $\widetilde{\sigma}_b$. In contrast to many prior guarantees for regularized policy optimization, our sample-complexity guarantee holds without trajectory resets, generative-model access, or nested policy-evaluation loops. Numerical results are consistent with the theoretical convergence analysis.

---


### 317. [Dynamic LoRA-Experts and Prototype-Ensemble Matching for Class-Incremental Learning](https://arxiv.org/abs/2609.39839)

**<font color=#1a73e8>作者：</font>** Hongwei Zhao, Rui Liu, Yansong Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Class-Incremental Learning (CIL) aims to continuously learn new classes without forgetting previously acquired knowledge. Parameter-efficient fine-tuning with pre-trained models reduces parameter overhead but can suffer from cumulative interference and suboptimal alignment between inference samples and specialized modules. We propose Dynamic LoRA-Experts and Prototype-Ensemble Matching (DLEPEM), a two-stage rehearsal-free framework. DLEPEM allocates a task-specific LoRA-Expert for each incremental task to reduce cross-task interference, then combines frozen pre-trained-model prototypes with task-adaptive LoRA-Expert prototypes for reliable task-level discrimination. Experiments on standard CIL and Few-Shot CIL benchmarks demonstrate strong performance under the evaluated protocols.

---


### 318. [DyRAD: Radar Novel View Synthesis for Dynamic Driving Scenes](https://arxiv.org/abs/2609.39841)

**<font color=#1a73e8>作者：</font>** Merav Keidar, Tomer Borreda, Rajalakshmi Nandakumar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing dynamic driving scenes from recorded sensor data supports closed-loop evaluation of autonomous driving systems by synthesizing observations beyond the original trajectory. Unlike cameras and LiDAR, radar measures radial velocity directly through Doppler. Yet existing radar novel-view synthesis fails to exploit this capability: methods addressing dynamic scenes reconstruct only range-azimuth tensors, while methods that render Doppler assume static scenes. Moreover, because radar processing spreads each reflection across multiple bins, existing representations absorb this spread into scene geometry, causing it to render incorrectly when the viewpoint moves. We present DyRAD, which models dynamic driving scenes using static background reflectors and motion-tracked dynamic point reflectors to render complete range-azimuth-Doppler (RAD) tensors. Reflector velocities are derived from object tracks and projected onto the line of sight, making Doppler both a rendered output and supervision for those tracks. Crucially, we render reflectors through a fixed analytic point-spread function (PSF) derived from the radar's signal-processing chain, preventing sensor-induced spread from being baked into the scene representation. Beyond improving scene reconstruction, this separation also enables zero-shot sensor-configuration transfer, allowing the same reconstructed scene to be rendered under different radar specifications without refitting. We evaluate DyRAD on RADIal, Boreas, and a synthetic benchmark across both on-path poses and displaced viewpoints untested by prior work. On RADIal, DyRAD recovers radar detections in 90.7% of reference-detected objects, compared with 26.9% for the strongest baseline.

---


### 319. [Predicting Multi-View Rashomon Representation: Can We Learn Where Models Disagree?](https://arxiv.org/abs/2609.39848)

**<font color=#1a73e8>作者：</font>** Mingyue Ma, Zongbo Han, Changqing Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models are increasingly adopted across a wide range of applications, often serving as core blocks within AI systems. Yet different foundation models may encode the same input from multiple different views, leading to substantial representation disagreement, which we term Rashomon Representation. Such disagreement often signals inputs that a given model encodes in a way inconsistent with other models, offering a valuable yet underexplored signal for input reliability estimation. While prior work has largely focused on measuring disagreement across multiple models with a representation set, we instead focus on predicting disagreement from a single representation. We hypothesize that this disagreement follows some consistent, input-dependent patterns rather than occurring at random. To test this, we quantify disagreement by comparing each sample's nearest neighbors across different models' representation spaces, then train a lightweight predictor that estimates disagreement from a single model's representation. At inference time, given a new input, the predictor uses that input's representation to tell whether it aligns with or diverges from those of other models. Extensive experiments across diverse foundation models and datasets show that representational disagreement is indeed input-dependent, predictable, and generalizable, enabling efficient reliability estimation of foundation models.

---


### 320. [Dimension-Free Rank Lifting from Random Hyperplane Arrangements](https://arxiv.org/abs/2609.39855)

**<font color=#1a73e8>作者：</font>** Luca Becchetti, Matteo Russo, Ruben Skorupinski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the width required for a randomly initialized hidden layer of a neural network to achieve rank lifting. Namely, given a dataset $X \in \mathbb{R}^{m \times d}$ of $m$, $d$-dimensional input vectors separated by an angle of at least $\theta$, we consider the random feature matrix $\sigma(XR)$, where $R$ is standard Gaussian. For positively homogeneous nonpolynomial activations, which include sign, Heaviside, ReLU, and ReLU powers among others, we prove that $$n \gtrsim \frac{1}{\theta}\max\left\{m,\log\left(\frac{1}{\delta}\right)\right\}$$ neurons suffice for $\sigma(XR)$ to have full row rank $m$ with probability at least $1-\delta$. This dimension-free bound exponentially improves the previous general-dimensional guarantee for sign features (Drago et al., 2026) and is essentially tight. The proof shows that one random feature column escapes every proper subspace of $\mathbb{R}^m$ with probability $\Omega(\theta)$, using a coupling of nearby Gaussian directions and a local crossing of the induced hyperplane arrangement. We also study stable rank lifting, where the goal is to establish a quantitative analogue of exact rank lifting, i.e., a lower bound on the smallest eigenvalue of the empirical feature Gram matrix in high-probability.
Our analysis unifies and generalizes stable rank guarantees for all $q$-homogeneous non-polynomial activations following prior work in Panigrahi et al. (2020) and Song (2026). In particular, we combine a diagonally dominant Taylor tail of the population kernel with truncation and matrix concentration, to show that for positively homogeneous nonpolynomial activations, stable rank lifting is achieved at width $$n \gtrsim C^q \frac{m}{\theta^{2q+1}} \log^{2q+\frac{1}{2}}\left(\frac{m}{\theta}\right) \log\left(\frac{m}{\delta}\right),$$ where $q$ is the degree of the activation and $C > 0$ is some universal constant.

---


### 321. [Completion-Aware Cross-Fidelity Offline-to-Online Reinforcement Learning for Multi-Line Bus Holding](https://arxiv.org/abs/2609.39868)

**<font color=#1a73e8>作者：</font>** Yifan Zhang, Qifan Zhang, Liang Zheng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Exploratory reinforcement learning (RL) on an operating bus fleet is impractical,while policies trained only from historical data cannot acquire new experience. Hybrid Offline-and-Online (H2O) RL combines fixed target replay with simulator interaction, but the inexpensive online simulator can differ from the target in transition and event-duration dynamics. We study this cross-fidelity problem for multi-line bus holding and address a failure mode in which lower generalized passenger time coexists with incomplete passenger journeys.

---


### 322. [Hyperspectral Image Models: Technical Report](https://arxiv.org/abs/2609.39871)

**<font color=#1a73e8>作者：</font>** Tanishq Rachamalla, Aryan Das, Srishti Kaushik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral remote sensing has advanced across diverse deep learning paradigms, including spectral spatial CNNs, Vision Transformers, Mamba, graph neural networks, Kolmogorov Arnold networks, and self supervised masked autoencoding. Yet progress remains hindered by fragmented repositories, incompatible tensor conventions, and non standardized evaluation. Hyperspectral Image Models addresses these challenges through a modular framework unifying 55 representative models across six paradigms with a common registry, automatic 4D/5D tensor adaptation, and standardized constructors. It integrates 24 benchmark scenes from Airborne, Spaceborne, UAV, and Mars CRISM sensors, with caching, label remapping, PCA, explicit band selection or raw spectra, optional spatial max pooling, and arbitrary PxP patch extraction. To prevent inflated accuracy from overlapping windows, it supports class balanced random partitioning and spatially disjoint regional blocking with Chebyshev guard bands that eliminate train test pixel overlap. Experiments use a single this http URL with deterministic seeds and complete provenance, generating LaTeX benchmark tables and classification maps. Across 1,320 model scene evaluations and 6,600 seeded runs, scene difficulty dominates architecture, with mean accuracy ranging from 96.40% on Botswana to 56.70% on Houston 2018, versus a 15 point spread across paradigm means. No paradigm universally dominates, while sub 1 M parameter models can match architectures two orders of magnitude larger. Code is publicly available at this https URL.

---


### 323. [Algorithmic Recourse Under Competition](https://arxiv.org/abs/2609.39877)

**<font color=#1a73e8>作者：</font>** Shahin Jabbari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Algorithmic recourse provides individuals who have received undesirable outcomes from machine learning models with suggestions for minimum-cost improvements to achieve the desired outcome. A central assumption when computing recourse is that the decision rule remains fixed throughout the recourse implementation phase. We challenge this assumption in settings where individuals compete for limited resources. In such settings, widespread recourse implementation can change the acceptance threshold even when the scoring model that is used to evaluate individuals remains the same. This change in acceptance threshold can, in turn, invalidate the original recourse recommendations (i.e., following the recourse may not lead to the desired outcome). To address this problem, we introduce a framework called recourse under competition that jointly optimizes for recommendation recipients and the recommended score target they need to satisfy to balance the recourse cost and post-shift validity among initially rejected individuals. We develop an algorithm based on the Implicit Function Theorem and empirically analyze its performance. Experiments on synthetic and real datasets show that personalized score targets can achieve higher validity, albeit at a higher cost. In contrast, common score targets generally offer favorable cost-validity trade-offs for lower to medium validity values.

---


### 324. [Grounding with Confidence: Controllable Generative Video Temporal Grounding](https://arxiv.org/abs/2609.39883)

**<font color=#1a73e8>作者：</font>** Jinhao Chen, Benlei Cui, Ruijian Jia 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video temporal grounding supports applications such as video search, content review, and automated editing by localizing events described in natural language. Yet existing generative models typically output timestamps without explicit interval-level confidence scores to guide candidate selection. We separate candidate generation from acceptance by scoring individual intervals within the original decoding pass. A lightweight confidence head reads pooled decoder states, providing an explicit score trained for interval selection. Offline verifier scores supervise the head on fixed candidate sequences, and temporal-overlap labels adapt it to current rollouts during reinforcement learning. GT-anchored candidate-pool supervision and set-level optimization train the generator. The resulting scores support ranking, threshold-based selection, and rejection without invoking an external verifier at inference. On a fixed OMTG-Bench candidate pool, confidence raises query-macro Recall@0.5 from 9.95% to 14.42% over generation order at a 10% global return budget, and from 26.48% to 31.12% at a 25% budget. The continuous scores let downstream applications adjust return budgets or acceptance thresholds to match their precision-recall preferences, without regenerating candidate intervals.

---


### 325. [Markovian Dynamics Enforcer: Feasibility Preserving Correction on Learned Dynamics Manifolds](https://arxiv.org/abs/2609.39888)

**<font color=#1a73e8>作者：</font>** Kevin Yu, Tao Guo, Constantinos Antoniou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural trajectory predictors can reach low prediction error while violating dynamics, actuator limits, or state constraints, especially when controls are unobserved and dynamics are partially specified. We introduce the Markovian Dynamics Enforcer (MaDE), a time-invariant post-hoc operator mapping state-transition proposals onto a learned feasible dynamics manifold, trained on feasible states without ground-truth controls. For each transition it infers a control and recomputes the state through a completion model of known physics plus a learned residual. It then corrects that control by gradient-based inequality reduction, so inequality satisfaction is best-effort within an iteration budget. Since every correction iterate re-enters the completion model, the returned state is dynamically consistent by construction relative to that model and the supplied previous-state anchor. MaDE drives dynamics residuals to essentially zero on fully specified simulated systems, and on an underspecified system leaves a smaller true-dynamics residual than the baselines. Designed to attach to arbitrary predictors, the frozen operator is evaluated downstream of recurrent, structured state-space, and transformer predictors. On recorded vehicle trajectories the one-step residual against a kinematic bicycle model is 0.0071 to 0.0072 for MaDE and 0.1703 to 0.1714 for raw predictors. MaDE raises average displacement error by a factor of 1.57 to 1.83.

---


### 326. [Solving Multi-Agent Sokoban via LaCAM](https://arxiv.org/abs/2609.39889)

**<font color=#1a73e8>作者：</font>** Keisuke Okumura  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Sokoban, a puzzle game in which an agent pushes boxes onto unlabelled target locations in a grid world, is a long-standing benchmark planning problem. While it is easy to see the connection to practical applications such as warehouse logistics with autonomous forklifts, its multi-agent counterpart has remained underdeveloped. This is because Multi-Agent Sokoban is substantially more difficult due to factors specific to multi-agent planning, such as the rapidly growing branching factor as the number of agents grows and the need to handle integrated task assignment and collision-free pathfinding. In this paper, we show that a scalable planner for Multi-Agent Sokoban can be designed by leveraging recent advances in multi-agent pathfinding (MAPF). Specifically, our Sokoban-LaCAM efficiently solves instances involving tens of agents and boxes while preserving both completeness and eventual optimality guarantees. This provides evidence that MAPF can serve as a powerful primitive for solving broader collective automation problems.

---


### 327. [Shared Weights, Selected Computations: How Looped Transformers Route What Each Loop Does](https://arxiv.org/abs/2609.39892)

**<font color=#1a73e8>作者：</font>** Jiaju Wu, Yi Hu, Muhan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped Transformers repeatedly apply the same set of Transformer layers, giving them a recurrent architecture for latent computation. Their strong performance on iterative reasoning and length-generalization tasks suggests an appealing explanation: recurrence may provide an inductive bias that lets the model reuse a learned algorithm across loops. However, weight sharing alone does not imply that every loop performs the same operation. This raises a basic question: is each loop actually repeating the same computation, and if not, what routes the shared parameters to different operations?
We study this question using graph walks as a test case. In the model's native trajectories, decoded predictions can advance by different numbers of graph steps or remain at a reached target, showing that recurrent progress need not follow a fixed one-loop-one-step pattern. We then show that a frozen loop can be steered toward different transitions by modifying its entering hidden state: a learned linear layer $J$ selects the desired transition without changing the shared Transformer layers.
To test how this steering works, we use activation patching and find that attention patterns can recover its effects and switch the selected transition. Across five matched pairs of graph models, changing intermediate supervision during backbone training changes which transitions $J$ can induce. This suggests that $J$ selects computations learned by the backbone rather than creating new algorithms. Together, these results show that the hidden state can control shared computation, with attention routing as a causal pathway.

---


### 328. [Spatial-Temporal Multi-scale Network for Screen Content Video Quality Enhancement](https://arxiv.org/abs/2609.39894)

**<font color=#1a73e8>作者：</font>** Ziyin Huang, Sik-Ho Tsang, Xinyuan Qin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Different from natural videos, Screen Content Videos (SCVs) are characterized by abrupt motion, scene switches, and high-frequency details such as text and graphics. Conventional video enhancement methods, which rely heavily on temporal continuity, often suffer from performance degradation when processing SCVs due to the disruption of temporal correlations. To address these challenges, we propose the Spatial-Temporal Multi-scale Network (STM-Net), a novel framework specifically tailored for compressed SCV enhancement. Our approach integrates three complementary components: a Prior-Guided Spatio-Temporal Dispatcher (PG-STD) that routes input into three parallel streams to avoid feature contamination, a Bidirectional Temporal Feature Extraction (BTFE) module that adaptively handles abrupt transitions without explicit detection, and a Cascaded Multi-scale Feature Distillation (CMFD) module that preserves critical high-frequency details. Experimental results demonstrate that STM-Net outperforms state-of-the-art methods in both objective metrics and subjective visual quality, providing a robust solution for screen content artifacts. Code is available at this https URL.

---


### 329. [Do Better Goal Representations Improve Goal-Conditioned Reinforcement Learning?](https://arxiv.org/abs/2609.39901)

**<font color=#1a73e8>作者：</font>** Syed Nazmus Sakib, Abdul Monaf Chowdhury, Nafiul Haque 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Goal-conditioned reinforcement learning (GCRL) relies heavily on how target goals are represented to the policy. While recent methods encode goals via temporal distance, occupancy, or controllability, it remains unclear how much downstream performance actually depends on representation quality. We study this in offline GCRL by constructing an exact temporal-distance goal representation in deterministic mazes. We then systematically corrupt its geometric quality while keeping the downstream learner fixed. Across OGBench navigation tasks and two algorithms, large changes in goal-representation quality produce almost no change in performance. However, applying the same interventions to the agent's current state more than doubles success, revealing the state pathway as the true bottleneck. Building on this insight, we show that simple random Fourier positional encodings substantially improve performance on the hardest navigation tasks without map information or objective modifications. Overall, our findings suggest that in state-based offline navigation, improving how the agent's current state is represented matters far more than refining the goal representation. Code will be released soon.

---


### 330. [Understanding Parents' Complex Views of AI for Children's Pretend Play](https://arxiv.org/abs/2609.39906)

**<font color=#1a73e8>作者：</font>** Sungho Oh, Mohammad Namvarpour, Maxi Heitmayer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI could support children's pretend play, but it could also direct the play on behalf of children. Whether AI should have roles in children's lives is controversial because its influence on children remains uncertain. We conducted semi-structured interviews with 10 U.S. parents, each with at least one child aged 4-15. During the interview, we described the concept of AI-supported pretend play and provided participants with two boundary-case storyboards. We analyzed the interview data through codebook thematic analysis, using inductive coding and affinity diagramming organized around the research questions, and then used qualitative systems mapping to examine relationships within and across themes. We found that the same characteristics of AI, e.g., ability to assume characters, responsiveness, and adaptability, were seen by parents as potentially useful but also concerning. Parents imagined that AI could make role-based play accessible to all children or help parents participate in family play. However, they opposed the idea of AI for children's play without a clear understanding of how it works and its long-term influence on their children. Parents worried about children's loss of imagination and creativity, emotional attachment to AI, reduced human interaction, inappropriate behavior by AI and/or children, and their inability to manage children's AI use. Parents viewed AI not only as a play tool but also as a social actor and a possible perturbation in the existing family dynamics. The appropriateness of AI and child--AI interactions therefore emerged as a requirement for AI in children's pretend play, in addition to technical safeguards and parental control. We contribute an integrated account of parents' interdependent judgments and emphasize the need for longitudinal research with children and their diverse families.

---


### 331. [Patient-Centered Treatment Planning for Chronic Multimorbidity: A Hierarchical Reinforcement Learning Framework for Preference Modeling](https://arxiv.org/abs/2609.39911)

**<font color=#1a73e8>作者：</font>** Nafiseh Payani, Soham Das, G. Anthony Wilson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Patient preference, defined as a patient's demonstrated willingness and capacity to adhere to clinical recommendations, is a primary determinant of therapeutic effect yet remains structurally absent from existing computational treatment planning models. We address this gap by presenting patient-centered factored-action hierarchical option-critic (FAHOC), a hierarchical reinforcement learning (HRL) framework that jointly learns high-level options corresponding to therapeutic strategies and factored intra-option policies that decompose the joint action space into disease- and intervention-specific subcomponents, while imposing a cooperation-aware action masking mechanism. This enables structured exploration, improved credit assignment across hierarchy levels, and more interpretable decision pathways, while enforcing patients' preferences. Formal guarantees establish that cooperative patients achieve higher optimal expected health outcomes than non-cooperative patients, and that the factored Q-function approximation error is provably bounded. The framework is evaluated using longitudinal data collected from approximately 50,000 comorbid hypertension and type 2 diabetes mellitus patients from five hospitals in the Southeast U.S. FAHOC achieves a quality-adjusted life year expectancy equivalent improvement of 0.669 (vs -0.133 observed clinician practice), correctly identifies cooperative patients in 95.9% of cases and never violates a patient's preference in held-out test, demonstrating that HRL with explicit preference constraints can support preference-consistent, clinically safe decision-making in multimorbidity management.

---


### 332. [NavHarness: Adaptive Goals for Agentic Vision-Language Navigation](https://arxiv.org/abs/2609.39915)

**<font color=#1a73e8>作者：</font>** Haoxiang Shi, Zaijing Li, Muhe Ding 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Navigation (VLN) requires embodied agents to generate actions based on instructions and observations. General-purpose multimodal agents offer a promising basis for this task, but selecting plausible local actions does not ensure that execution remains consistent with the intended route, particularly in long-horizon tasks. Moreover, the accumulated interaction history increases the input required for subsequent decisions, resulting in a significant inference overhead. To this end, we introduce \method, an Agentic VLN framework that includes a Goal Agent that sets adaptive goals for local actions, a Verify Agent that dynamically verifies whether a goal has been completed, a Memory Agent for multimodal context compression, and a Visuomotor Agent to execute adaptive goals. Specifically, the Goal Agent formulates adaptive goals based on the instruction, current observation, and execution history. Then the Visuomotor Agent executes navigation actions to achieve each goal, while the Verify Agent uses a goal-specific verification question to dynamically assess whether the observed outcomes satisfy the intended completion condition. Verified goal completion then marks a boundary for the Memory Agent to compress the corresponding multimodal interaction history while preserving information needed for subsequent navigation. We evaluate navigation on R2R-CE and RxR-CE, examine framework variants across three model backbones, and study context evolution during execution. For Real-World evaluation, \method achieves 83.3\% success and 1.51\,m navigation error across eight challenging routes evaluated three times each.

---


### 333. [Super-Resolving Unseen Hyperspectral Sensors at Any Scale via Spatial Operators](https://arxiv.org/abs/2609.39926)

**<font color=#1a73e8>作者：</font>** Ji-Xuan He, Guohang Zhuang, Bo Junge 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Achieving cross-sensor generalization and arbitrary-scale reconstruction with a single model remains challenging in hyperspectral super-resolution (HSR). Although recent methods support arbitrary-scale reconstruction, applying them to new sensors or scales beyond the training range often requires additional data and computation to maintain reconstruction quality. To address these challenges, we propose OmniHSR, which predicts band-shared spatial operators rather than spectral values. Cross-Spectral Mapping (CSM) resamples inputs with any number of bands to fixed reference positions and predicts local operators with Gaussian supports. Continuous Operator-Field Reconstruction (COFR) composes these operators into a continuous field and applies them to all original bands for arbitrary-scale reconstruction. Experiments demonstrate that operator prediction outperforms direct spectral-value prediction on all seven datasets. Trained solely on ARAD with only 0.538M parameters, OmniHSR outperforms all directly transferred baselines on six unseen datasets without target-domain training data or adaptation. Across twelve upsampling factors from $\times2$ to $\times48$, it improves average PSNR on Pavia U and Chikusei by 0.55 dB over the strongest baseline. It also surpasses baselines trained from scratch or adapted on the target sensor and achieves up to $36\times$ faster inference. Our code will be publicly released soon.

---


### 334. [Reliability-Aware Checkpoint Selection for Domain Generalization](https://arxiv.org/abs/2609.39934)

**<font color=#1a73e8>作者：</font>** Jinshi Liu, Jiahao Li, Pan Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Checkpoint selection in domain generalization often relies on source-validation accuracy, yet the selected checkpoint need not provide reliable probabilities on unseen target domains. Source-target distribution shifts can alter accuracy rankings, while accuracy alone does not measure predictive probability quality. We identify an empirical selection opportunity within fixed training trajectories: reselecting among checkpoints with near-optimal source accuracy can improve mean target probability quality with small observed changes in mean target accuracy. We study accuracy-constrained reliability selection (AC), which retains checkpoints within a tolerance of the best source-validation accuracy and ranks them by source reliability. Our reference rule aggregates within-set normalized negative log-likelihood (NLL) and class-wise calibration error (CwECE) using $D_\infty$. AC uses no target data and requires neither additional training nor weight averaging. We evaluate five domain generalization training algorithms on three benchmarks, using PACS to develop the objectives and a 0.5-percentage-point tolerance. In exploratory aggregation comparisons on 360 OfficeHome and TerraIncognita runs, the reference rule reduces mean target soft-bin squared-gap ECE and CwECE by 0.240% and 0.182%, respectively, and NLL by 0.030 relative to Source-Acc. Mean target accuracy changes by +0.213 percentage points. These results identify opportunities for reliability-aware reselection, while the additional benefit of joint over single-objective ranking remains unresolved.

---


### 335. [Coverage Before Control: Route-Instruction Grounding and Steering for Controllable Retrosynthesis](https://arxiv.org/abs/2609.39955)

**<font color=#1a73e8>作者：</font>** Xuemin Chen, Xiaozhuang Song, Xinjian Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Single-step retrosynthesis models are commonly evaluated by their ability to recover recorded reactions. In practice, chemists may need to choose among several precursor sets for the same product, for example to preserve a particular motif. Recovering a recorded answer alone does not establish this ability to follow a preference. Satisfying such requests requires both coverage of relevant alternatives and control over which alternatives are favored. We introduce Route-Instruction Grounding and Steering (RIGS), a two-stage framework for instruction-conditioned retrosynthesis. Stage A trains a language projector, teaching it which alternatives an instruction favors or discourages. Stage B uses the projector learned in Stage A to steer a frozen generative model through lightweight residual adapters. We construct nested one-to-many training supports by pairing each product with increasing numbers of candidate precursor sets. Extensive experiments demonstrate that broader support helps the model generate a wider range of alternatives, and RIGS can learn to guide generation according to instructions. The relationship between coverage and control is consistent across model scales but non-monotone.

---


### 336. [Reconstructing the Dynamic World: A Representation-Centric View of 4D Scene Reconstruction](https://arxiv.org/abs/2609.39960)

**<font color=#1a73e8>作者：</font>** Ziren Gong, Guo Chen, Yongjia Li 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 4D scene reconstruction aims to recover the evolving geometry, appearance, and motion of dynamic environments from visual observations. Despite substantial progress in neural scene representations, reconstructing dynamic scenes remains challenging due to non-rigid motion, occlusions, temporal inconsistencies, and the trade-offs between reconstruction fidelity and computational efficiency. Recent advances in Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) have introduced diverse approaches to representing and reconstructing dynamic scenes, yet their relationships, underlying design choices, and evaluation protocols remain fragmented. In this paper, we present a unified perspective on 4D scene reconstruction, organizing existing methods around their scene representations, temporal modeling strategies, reconstruction pipelines, and optimization objectives. Through this framework, we examine how different design choices affect geometric fidelity, appearance consistency, motion representation, and computational efficiency. We further consolidate commonly used datasets and evaluation metrics, identify limitations in current experimental practices, and discuss open challenges in reconstructing complex, dynamic real-world environments. By connecting methodological developments with their underlying assumptions and evaluation evidence, this work provides a structured foundation for understanding existing approaches and identifying future research directions. An evolving collection of relevant papers and resources is available at this https URL.

---


### 337. [Diptych: Scoped, AI-Interpreted Comparison for Reference Listening in Music Production](https://arxiv.org/abs/2609.39963)

**<font color=#1a73e8>作者：</font>** Chongjun Zhong, Abhinaba Roy, Archishman Ghosh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Reference listening is a common strategy in music production, but current comparison tools often obscure a key human judgment: deciding what should be compared. We present Diptych, an AI-assisted system that lets users define comparison scope across whole tracks or independently selected segments, while inspecting structured audio features and scope-specific AI interpretations. We evaluated Diptych in a within-participants study with 12 musicians, complemented by source-blinded ratings from four expert listeners. Participants used the system to surface additional differences, nine of ten of which received at least partial expert support, and reported good usability and greater clarity about possible next steps. These findings suggest that AI support for creative comparison should prioritize user-defined scope, inspectable evidence, and actionable guidance, while avoiding authoritative judgments that exceed what the evidence can support.

---


### 338. [Overview of BioASQ 2026: The fourteenth BioASQ Challenge on Large-Scale Biomedical Semantic Indexing and Question Answering](https://arxiv.org/abs/2609.39975)

**<font color=#1a73e8>作者：</font>** Anastasios Nentidis, Georgios Katsimpras, Anastasia Krithara 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents an overview of the fourteenth edition of the BioASQ challenge, organized in the context of the Conference and Labs of the Evaluation Forum (CLEF) 2026. BioASQ is an international challenge series that supports progress in biomedical language processing tasks ranging from semantic indexing and information extraction to question answering and summarization. In 2026, BioASQ included six shared tasks: a) Task 14b on biomedical semantic question answering. b) Task Synergy14 on question answering for developing biomedical top- ics. c) Task MultiClinSum-2 on multilingual clinical summarization. d) Task BioNNE-R on extracting relations between nested named entities in Russian and English. e) Task ELCardioCC on clinical coding in cardiology. f) Task GutBrainIE on gut-brain interplay information extrac- tion. Across these six tasks, 87 distinct teams participated, submitting more than 1000 runs overall. As in previous editions, several submissions reached competitive performance, reflecting the continued progress of state-of-the-art methods across biomedical language processing tasks.

---


### 339. [Richard: Voice-First Mobile Interaction for Persistent Tasks](https://arxiv.org/abs/2609.39976)

**<font color=#1a73e8>作者：</font>** Xinyang Chen  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Mobile terminals need to provide application and network services while supporting users' control over their attention. We explore voice-first interaction organized around requests and delegated tasks, allowing users to leave a conversation and later inspect, revise, and retrieve the work. We present Richard, a system prototype that manages voice sessions, task execution, and result delivery separately, linking them through persistent request records. Conversation and task views provide visual feedback, while the backend coordinates immediate responses, dedicated service operations, and agent tasks. Request revisions, execution states, and notifications remain associated with the relevant task. We examine this design through Android functional records, controlled lifecycle verification, and execution records of a real programming request. Controlled verification reproduces revision, execution after confirmation, and result retention; deployed-service records show backend progress and failure feedback after client disconnection. These observations inform the design of task continuity, user control, and service integration in mobile voice interaction, providing an implementation basis for personal computing devices that accommodate intermittent user participation.

---


### 340. [Learning to Explain While Planning: Rule-Aligned Diffusion Planning for Autonomous Driving](https://arxiv.org/abs/2609.39995)

**<font color=#1a73e8>作者：</font>** Jiaxi Ye  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion planners exhibit strong capabilities in generating multimodal trajectories. However, existing methods primarily rely on expert demonstrations to fit trajectory distributions, learning statistical correlations among scenes, behaviors, and trajectories without explicitly modeling driving rules. In long-tail scenarios where expert data are scarce, the lack of behaviors to imitate may lead to trajectories that violate safety or compliance requirements. Moreover, their generation process lacks rule-level explanations, making it difficult to determine which rules drive trajectory adjustments, when they take effect, and how strongly they act, thereby limiting failure diagnosis, safety validation, and targeted improvement. To address these limitations, we propose the Rule-Aligned Diffusion Planner (RADP), which incorporates differentiable driving rules into the diffusion objective during training, turning rule knowledge into intrinsic behavioral principles beyond finite demonstrations. We further introduce Rule-Pressure Attribution (RPA), which constructs supervision signals from gradients of rule losses with respect to predicted trajectories and employs a lightweight attribution head to estimate the optimization pressure exerted by each rule online. To assess the closed-loop behavioral relevance of these attributions, we propose a temporal risk-alignment protocol that evaluates whether current rule pressures reflect corresponding risks during subsequent closed-loop execution. Experiments on nuPlan show that RADP improves closed-loop planning in challenging safety-critical scenarios, while RPA exhibits consistent temporal alignment with subsequent rule-specific risks, validating both intrinsic rule learning and rule-level interpretability.

---


### 341. [DashVMC: Real-Time Discrete World Model Control in Geometry Dash](https://arxiv.org/abs/2609.40003)

**<font color=#1a73e8>作者：</font>** Florent Tariolle, Florian Yger  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World-model agents are usually evaluated in simulators that can wait for the policy; live games impose the opposite constraint, requiring capture, prediction, and action before the next frame. We present DashVMC, which learns a compact, action-conditioned world model from approximately two hours of recorded Geometry Dash gameplay. To test whether the learned dynamics are actionable, a controller is initialized by behavioural cloning (BC) and refined with Proximal Policy Optimization (PPO) entirely in frozen-model rollouts, without further interaction with the live game. Across three controller seeds, the refined policies survive longer than their BC initializations on all three official levels and a held-out community layout. At deployment, the baseline skips visual generation and sustains a 60-Hz capture-to-action loop on a consumer GPU. Action-conditioned continuations and rollout diagnostics show that the model remains useful for control despite imperfect long-horizon fidelity.

---


### 342. [Can We Anticipate Violence? Multimodal Learning from Pre-Incident Behavioral Cues](https://arxiv.org/abs/2609.40014)

**<font color=#1a73e8>作者：</font>** Sindhuja Penchala, Mohammed Yusuf Mujawar, Noorbakhsh Amiri Golilarz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detecting violence after it begins is important from recognizing behavioral cues that appear immediately beforehand. This work studies short-horizon pre-incident risk recognition from multimodal video signals. We construct a binary Normal-versus-Risky setting from temporally annotated XD-Violence clips, using 443 samples with source-level separation across training, validation, and test sets. Each sample consists of a variable-length pre-incident clip, with its duration determined by the observable behavioral context preceding the incident. The inci- dent itself is excluded from all input clips. We evaluate three complementary information sources: facial-region appearance, temporally aligned audio, and body-motion features derived from tracked keypoints. Controlled ablations are performed with Swin-Tiny, ViT-Tiny, and DeiT-Tiny to measure the contribution of each modality under the same split. Results show that combining all modalities is more effective than using any other combination alone. The best configuration, Deit-Tiny with audio, facial appearance, and motion, achieves 91.21% accuracy, 88.96% balanced accuracy, 93.65% F1-score, and 96.38% ROC-AUC on the held-out test set. These results suggest that complementary appearance, acoustic, and kinematic cues provide useful evidence for recognizing elevated pre-incident risk.

---


### 343. [Fenchel Tilting: Weighted Correction for Efficient Finetuning of Generative Models](https://arxiv.org/abs/2609.40030)

**<font color=#1a73e8>作者：</font>** Maksim Bobrin, Maksim Zhdanov, Dmitry Dylov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adapting a pretrained generative model to an arbitrary preference expressed as a utility function underlies reward alignment, guided design, and constraint satisfaction, enabling diverse applications. Existing fine-tuning methods trade off generality against computational cost: they either restrict the family class of supported preferences to keep optimization simple or preserve generality at the expense of efficiency. We introduce Fenchel Tilt Flow Control (FTFC), which decouples utility optimization from generative-model fitting. FTFC first optimizes for a target distribution by jointly fitting an effective reward and density-ratio weights on pretrained samples. Method combines the utility's variational structure with Fenchel duality, supporting general $f$-divergence penalties that determine how rewards are transformed into an distribution-correction weights. These weights are then frozen and used to modify a diffusion or flow model in a single stage of importance-weighted denoising or flow matching, without differentiating through sampling trajectories. We establish exact duality for concave utilities under suitable conditions and show that weighted fitting reproduces the optimal target distribution for a given utility. Across image and molecule generation benchmarks, FTFC improves over baselines on diverse preference functions, while also being up to $20\times$ more efficient. roposed method enables adaptation beyond expected-reward maximization without complex optimization, while preserving robustness for more general class of the utility functions compared to baselines.

---


### 344. [WARP: A Unified Benchmark for Invisible Image Watermarking -- Robustness and Protection Against Attacks](https://arxiv.org/abs/2609.40031)

**<font color=#1a73e8>作者：</font>** Khaled Abud, Aleksey Yakushev, Aleksandr Akimenkov 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Digital image watermarking is increasingly critical in media contexts, as emerging regulations and industry practices require marking AI-generated content and ensuring traceable sources to prevent manipulation or misuse. Recent advances in invisible watermarking methods highlight the need to update existing benchmarking practices to reflect current techniques and evaluation criteria.
We address this by introducing WARP -- a unified framework and benchmark for evaluating the robustness of invisible watermarks. WARP incorporates 32 recent classical, deep, and generative watermarking methods, as well as 34 different erasing techniques, ranging from traditional distortions to more sophisticated adversarial, purification, and re-embedding attacks. It provides standardized, reproducible, and easily scalable protocols for evaluating perceptual quality, watermark readability, and attack resilience.
Using WARP, we extensively evaluate current invisible watermarking techniques, collecting the largest robustness benchmark in the field. Results identify the most robust approaches under both distortion and adversarial conditions, and reveal consistent relationships between watermarking methods and the attack strategies most effective against them. Our experiments also highlight that some of the watermarking methods considered are highly vulnerable to reembedding, even if they are robust to standard distortions. The code is made available at this https URL.

---


### 345. [Efficient Active Auditing of Multi-Group Fairness with Bias Probes](https://arxiv.org/abs/2609.40034)

**<font color=#1a73e8>作者：</font>** Ayoub Ajarra, Debabrota Basu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Over the past decade, Machine Learning (ML) has been trained under dual objectives: minimizing prediction error via Empirical Risk Minimization (ERM) while controlling unfairness bias. In practice, however, fairness-aware training often yields limited improvements over standard ERM, making reliable post hoc auditing essential. Existing auditing approaches for black-box models either rely on model reconstruction --exposing systems to extraction attacks-- or directly estimate fairness metrics, offering limited insight into which regions of the data distribution drive bias. More fundamentally, property-specific auditing --aimed at extracting only targeted fairness information without reconstructing the model-- remains poorly understood. In this work, we introduce the bias probe framework, which enables targeted and adaptive querying to reveal bias structure while preserving model confidentiality. Building on this framework, we propose ALeBi, an active auditor that learns such probes to efficiently estimate multi-group fairness metrics. We establish novel sample complexity guarantees governed by a property-specific complexity measure, resolving a previously posed open question, and extend our analysis to adversarial settings where the model owner may strategically obscure bias. Our results uncover a fundamental trade-off between model confidentiality and reliable auditing, and show that property-specific probing enables both accurate estimation and interpretable identification of high and low-bias regions. Extensive experiments support our theoretical findings and demonstrate the practical effectiveness of our approach.

---


### 346. [Enhancing Autoregressive Video Generation via Representation Adversarial Distillation](https://arxiv.org/abs/2609.40037)

**<font color=#1a73e8>作者：</font>** Fangyu Lin, Xingtong Ge, Lunjie Zhu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-step autoregressive video generation enables efficient streaming synthesis, but errors introduced in early temporal blocks are reused as context and can propagate through subsequent rollouts, leading to detail degradation, structural drift, and unstable motion. Existing distribution matching distillation (DMD) primarily aligns student and teacher distributions in diffusion latent space, but provides no direct supervision over the perceptual quality of decoded videos. We introduce Radian, a representation-space adversarial distillation framework that complements on-policy DMD with real-data adversarial supervision in the feature space defined by a frozen visual foundation model (VFM). During training, Radian sparsely decodes frames from autoregressive student rollouts, extracts multi-level visual representations, and applies lightweight discriminator heads to distinguish generated outputs from real video frames. The DMD objective anchors the student to the pretrained teacher, while the representation-space adversarial objective supplies complementary perceptual and semantic gradients that promote high-quality modes. These additional components are discarded after training, leaving the generator architecture and inference-time denoising budget unchanged. Experiments on Wan2.1-1.3B cover four-step chunk-wise, one-step frame-wise, and minute-long autoregressive generation. Our method achieves a VBench Total of 0.8444 and a VideoAlign Total of 0.8033 under four-step generation, and improves VBench-Long from 0.7805 to 0.8041 over Rolling Forcing while using fewer denoising steps. Controlled comparisons across image, video, and diffusion representations further indicate that the choice of representation spaces induces distinct adversarial signals, and external VFM gradients complement DMD more effectively than adversarial supervision derived from diffusion-internal features.

---


### 347. [MGhana-ST: A Low-Resource Speech Translation Dataset for Ghanaian Languages and an Analysis of Multilingual Training Trade-offs](https://arxiv.org/abs/2609.40041)

**<font color=#1a73e8>作者：</font>** Frank Lawrence Nii Adoquaye Acquaye, Eric George Parakal, Jesse Johnson 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present MGhana-ST, a speech translation dataset for four low-resource Ghanaian language varieties: Ga, Twi (Akuapem and Asante), Ewe, and Fante. MGhana-ST is an ongoing annotation effort; the experiments here use a fixed subset of about 16.1 hours of paired speech and English translations. The audio is curated from two existing Ghanaian speech resources. Unlike in those resources, the English translations are produced directly from audio by 37 native-speaker annotators and include verbal and non-verbal event annotations.
Using Whisper-small, we compare monolingual and multilingual training under severe data scarcity, reporting means over three seeds. Flat multilingual training benefits no variety in this regime. Ga and Twi are unchanged within seed variance (+0.51 and +0.06 BLEU against monolingual standard deviations of 1.63 and 2.20), while Ewe declines by 6.99 BLEU and Fante by 5.11. The degrading varieties are Ewe, which is linguistically distinct and drawn from a different source corpus, and Fante, the least-resourced. Comparing empirical cross-lingual transfer with typology-based similarity, we find that transfer BLEU identifies closely interacting language pairs better than URIEL similarity, though neither predicts which varieties benefit from joint training.
We also report a methodological finding. An earlier single-run analysis found positive transfer for three of four varieties; this did not survive replication across seeds. For Ga and Twi, monolingual baselines trained on 1.6 to 6.2 hours of audio have seed standard deviations roughly five and thirty times those of the multilingual models (0.35 and 0.07 BLEU). When the monolingual condition is noisier, a single-run comparison can show apparent transfer of this size from seed variation alone. We release MGhana-ST to support research on African language speech technology and low-resource speech translation.

---


### 348. [Gromov-Wasserstein Distillation for Inductive Multi-View Embedding](https://arxiv.org/abs/2609.40047)

**<font color=#1a73e8>作者：</font>** Rafael Pereira Eufrazio, Eduardo Fernandes Montesuma, Charles Casimiro Cavalcante  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gromov-Wasserstein multidimensional scaling (GW-MDS) learns low-dimensional representations from relational data but remains transductive, providing no explicit mapping for unseen samples. We introduce an inductive framework based on barycentric distillation. A GW-MDS teacher learns a latent support and an optimal transport plan from the training data, and barycentric projection converts the resulting coupling into sample-aligned targets. A neural student then learns an explicit out-of-sample mapping, avoiding additional relational-matrix construction and GW optimization at inference. We formulate the approach for single-view data and extend it to Mean-GWMDS and Multi-GWMDS teachers through consensus and selected-projection targets learned by a multi-view student with view-specific encoders. We also investigate a direct neural baseline trained solely with a GW objective. Experiments on synthetic and real-world data using Euclidean, geodesic, and cosine relations show that the distilled models preserve the teacher geometry on unseen samples and consistently outperform direct neural GW training in sample-indexed relational preservation. These results establish barycentric projection as an effective bridge between transductive GW embeddings and inductive neural mappings.

---


### 349. [From Tweets to Trades: Analyzing the Influence of Public Mood over Stock Market Performance in Turkiye](https://arxiv.org/abs/2609.40064)

**<font color=#1a73e8>作者：</font>** Ece Elif Adak, Bertaç Şakir Şahin, Şaziye Betül Özateş  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Purpose: This study examines whether domain-specific public mood is associated with stock-market dynamics and whether these relationships vary across communication domains and market conditions. It distinguishes public mood from investor sentiment and investigates whether heterogeneous sources of public communication exhibit different relationships with market behaviour.
Design: The study analyses 610,422 posts published by 176 curated X accounts between January 2022 and December 2023, covering Politics and Government, Economy and Finance, and Media and Society. Posts are classified using fine-tuned Turkish transformer models under three domain-specific and one pooled regime. Public mood measures are constructed at daily, weekly, and monthly frequencies and examined alongside BIST100 and BIST30 market measures using correlation, Granger causality, vector autoregression, and impulse response analyses across the full period and selected market conditions.
Findings: Public mood is not associated with the direction of stock-market returns but is associated with the magnitude of price movements, particularly for Media and Society and pooled communication. These relationships become stronger at longer aggregation frequencies. Predictive relationships are concentrated in Economy and Finance communication, while their magnitude and direction vary across market conditions, particularly during the 2023 election period. The pooled measure largely reflects the most active communication domain.
Originality: The study contributes to behavioral-finance research by incorporating communication - domain heterogeneity into the analysis of public mood and market dynamics. It also demonstrates how aggregating heterogeneous sources can obscure domain-specific relationships between public communication and financial markets.

---


### 350. [Accelerated Algorithm for Sparse Regularized Partial Optimal Transport](https://arxiv.org/abs/2609.40075)

**<font color=#1a73e8>作者：</font>** Khoa Nguyen, Dung T. Nguyen, Thong Huynh 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Partial Optimal Transport (POT) extends the classical optimal transport problem by relaxing the strict mass conservation constraint, enabling its use in a wide range of real-world applications. In many of these settings, sparse transport plans are preferred for their interpretability and computational benefits. While smooth and strongly convex regularizers - such as quadratic or elastic net - have been vastly used in various machine learning applications to induce sparsity and accelerate computation, they have received less algorithmic attention compared to entropic approaches for computational POT. In this paper, we propose a new optimization framework that leverages these regularizers through a penalty-based reformulation, enabling efficient gradient-based updates while preserving the structure of the original problem. Our method accommodates a broad class of regularizers that promote structured and sparse transport plans. Building on this formulation, we design an accelerated first-order algorithm that alternates between smooth updates and simple projection steps. Through empirical benchmarks on color transfer, domain adaptation, and point cloud registration, our approach consistently outperforms established baselines - achieving lower transport cost, higher sparsity, and faster convergence - making it a practical and scalable solution for modern transport problems.

---


> [!TIP]
> 当前位于：**301-350**（第 7/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-382](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
