# 📦 其他研究 | 2026年08月26日

> 本类共 **361** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-361](./part-08.md)

---

### 101. [Multimodal Prompt Learning with Irregular EHRs for Robust Monitoring of Critical Care Patients](https://arxiv.org/abs/2608.21941)

**<font color=#1a73e8>作者：</font>** Yixin Yang, Yueyang Sun, Weichen Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate assessment of patients in intensive care units (ICUs) is essential for timely clinical intervention and improved patient outcomes. Multimodal electronic health records (EHRs), including structured physiological time series and longitudinal clinical notes, provide complementary information for critical care prediction. However, in real-world clinical settings, individual modalities may be partially observed or entirely unavailable, resulting in substantial performance degradation for existing multimodal models. To address this challenge, we propose a multimodal prompt-learning framework for robust clinical prediction under diverse missing-modality scenarios. The proposed framework introduces four complementary types of prompts: generative prompts, missing-signal prompts, missing-type prompts, and temporal prompts. Generative prompts construct surrogate latent representations for unavailable modalities, while missing-signal prompts distinguish observed representations from generated ones. Missing-type prompts condition the model on different modality-availability configurations, whereas temporal prompts perform condition-specific aggregation over temporally encoded clinical sequences. Together, these prompts enable the model to capture missingness-aware intramodal dependencies and cross-modal interactions within a unified architecture. Extensive experiments demonstrate that our method outperforms existing approaches across evaluation metrics on two missingness settings. Ablation and robustness analyses further verify the complementary contributions of the four prompt types and the effectiveness of the proposed framework for clinical prediction from incomplete multimodal EHR data.

---


### 102. [Bulbul: A Dataset for Dialectal Arabic Speech Recognition](https://arxiv.org/abs/2608.21950)

**<font color=#1a73e8>作者：</font>** Ahmed Ashraf, Aisha Alansari, Fadel Al Abbas 等 33 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Arabic automatic speech recognition (ASR) faces unique challenges due to diglossia, extensive regional dialect variation, and limited speech resources. Existing speech datasets often focus on single dialects or large-scale broadcast/web data, leading to trade-offs between linguistic diversity and annotation quality. We present BULBUL, a multi-dialect Arabic ASR dataset collected from 275 speakers in 11 Arab countries. BULBUL includes structured dialect and sub-dialect coverage, as well as recordings of classical Arabic and modern standard Arabic spoken by participants in their native dialectal accents to support accent-aware modeling. The quality of the recordings was ensured through a two-level human verification process. We further benchmark a range of recent ASR systems, establishing strong baselines for modern dialectal and accented Arabic ASR.

---


### 103. [SSDi8: Accurate and Efficient 8-bit Quantization for State Space Duality](https://arxiv.org/abs/2608.21952)

**<font color=#1a73e8>作者：</font>** Hyunwoo Kim, Byoungchan Ko, Minseok Kang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in sequence modeling have highlighted Mamba as a state space architecture offering efficient long-range dependency modeling and providing a viable alternative to Transformers. Building upon this, Mamba-2 introduces the Structured State Space Duality (SSD), which integrates recurrent and attention modes to achieve efficiency and scalability. However, this architectural expansion substantially increases memory and latency overhead, underscoring the need for efficient compression strategies tailored to SSD. In this work, we present SSDi8, the first post-training quantization framework specifically designed for SSD to maintain a persistent INT8 path. SSDi8 introduces a reformulation that decouples element-wise multiplications from matrix multiplications, enabling reuse of quantized activations across modules. Moreover, SSDi8 adaptively quantizes channel-varying activations at cost-effective points, further reducing latency. On the accuracy side, SSDi8 explicitly leverages the intrinsic dimensional decomposition of SSD, exploiting distinct outlier distributions across axes, and incorporates an error correction term based on per-channel error statistics. Comprehensive experiments demonstrate that SSDi8 achieves accuracy comparable to FP16 while delivering up to 1.4x speedup in W4A8 and W8A8 settings. We further validate its robustness in resource-constrained environments by deploying it on the Orin NX device.

---


### 104. [Trustworthy Visual Quality Inspection under Data Scarcity in Manufacturing](https://arxiv.org/abs/2608.21967)

**<font color=#1a73e8>作者：</font>** Panagiotis Sapoutzoglou, Jessy Ribaira, Martin Kanounnikoff 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated visual inspection in manufacturing aims to replace slow and inconsistent manual checks, but its economic value depends on whether its decisions can be trusted enough to automate routine inspection while reserving human expertise for ambiguous cases. In production-line settings, defective samples are scarce, since the process is optimized to produce good parts, which limits any learning-based inspector trained on real data alone. Compounding this, defect decisions emitted as hard labels with no confidence estimate carry an asymmetric cost: a false reject wastes a good product, while a false accept may increase the risk of undetected defects progressing through the production process. We address both problems by mitigating data scarcity through the generation of synthetic defective samples with a diffusion model, and meeting the need for confidence-aware decisions with a Bayesian classifier that defers ambiguous units to human review rather than misclassifying them. These components are embedded in a staged pipeline of successive, complementary checks. We evaluate how synthetic augmentation affects classification and localization on a test set of real defects, and examine the system's trustworthiness at three points: the decision, the synthetic data, and the pipeline structure. This work-in-progress reports preliminary results suggesting that diffusion-generated defects, combined with uncertainty-aware classification, can lower the cost of reaching a trustworthy, deployable inspection model under data scarcity.

---


### 105. [ToSCA: Leveraging Hierarchical Reinforcement Learning on Temporal and Strategic Abstractions of Conversational Agents](https://arxiv.org/abs/2608.21969)

**<font color=#1a73e8>作者：</font>** Xiaoyu Wang, Qingqing Gu, Yue Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Humans have multiple levels of temporal abstractions on daily interaction and thinking, such as concept perception and strategic planning. Inspired by this nature, we propose a two-level hierarchical reinforcement learning (RL) framework for conversational agents, bridging the gap between previous token-level or utterance-level RL methods. Developed on a two-level MDP, the token-level response decoding is conditioned on the utterance-level action, the explicit textual strategies. Based on theoretical derivation and efficiency consideration, we use DQN to solve the high-level critic and PPO to solve the low-level actor-critic. To further alleviate the reward sparsity and facilitate the convergence, we also design the dual-granularity reward mechanism, in which the utterance-level satisfaction score is integrated with token-level intrinsic motivation and K-L penalty. Experiments on both daily and emotional support conversations show that our method outperforms versatile baselines in strategy determination and response quality. Our implementation is available at this https URL.

---


### 106. [Improved denoising diffusion probabilistic models with efficient non-diagonal covariance modeling](https://arxiv.org/abs/2608.21972)

**<font color=#1a73e8>作者：</font>** Rui Xia, Ayan Das, Artem Artemev 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The sampling process of Denoising Diffusion Probabilistic Models (DDPMs) can be accelerated by leveraging second-order information in the form of approximations to the denoising posterior covariance -- allowing samples of acceptable quality to be produced in fewer but larger sampling steps. Previous attempts at using such information have used drastic (e.g.\ diagonal) simplifications of the covariance. These do not do justice to the peculiar statistical structure of natural images, which exhibit strong non-diagonal correlations between pixels and color channels, and a slow-decaying power-law frequency spectrum. Here, we develop a novel covariance model that captures these features. Our Kronecker-DCT (K-DCT) model uses a Kronecker-factored decomposition of inter-color covariances and spatial covariances modeled in the frequency domain using the Discrete Cosine Transform (DCT). The use of the DCT reduces the computational complexity from quadratic to log-linear, resulting in negligible computational and memory overhead in each denoising step. By learning K-DCT-structured amortizations of the denoising posterior covariance using pre-trained score models on CIFAR-10, Celeb-A, ImageNet and LSUN datasets, we show improved performance compared to previous SOTA denoising samplers, both in terms of FID and likelihoods, especially in the regime of few denoising steps.

---


### 107. [A Loss-Robust Disturbance Certificate for Minimal-Receiver Quantum Key Distribution](https://arxiv.org/abs/2608.21974)

**<font color=#1a73e8>作者：</font>** Roberto Di Pietro  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Quantum Key Distribution (QKD) enjoys information-theoretic security, yet the most damaging attacks against deployed systems exploit the receiver, where the key bit is encoded in which one of a pair of never-identical detectors clicks. The minimal receiver, one rotatable polarizer and one threshold detector, removes that attack surface, and single-detector BB84 demonstrations already run sampled error estimation; the structure of its zero-probability error subensemble, however, has remained uncharacterized. We characterize exactly that structure, introducing a deterministic impossible-event certificate: a click behind a polarizer set orthogonal to the transmitted state has probability exactly zero on an ideal channel, so a single occurrence is a probability-one witness of disturbance; and, since loss deletes clicks and never creates them, the certificate is loss-robust. We prove it sound but incomplete over three polarization states, and show that the four BB84 states close the gap: a fixed-basis intercept-resend attack yields an ideal trip probability of $1/4$ per orthogonal round ($\eta/4$ observed at detection efficiency $\eta$), independent of the interception angle. An illustrative finite-size budget yields 256 retained bits from $\approx 62{,}000$ transmitted rounds at $\eta = 0.1$; under realistic detector noise ($q_0 = 10^{-6}$ per opened gate), each trip retains $\approx 12$ bits of evidence at a sub-percent honest false-abort probability per session. The core ideal trip-probability predictions are numerically verified on the Qiskit circuit simulator, via a released, seed-fixed implementation. Overall, by endowing the minimal-detector receiver of polarization QKD with a conclusive, loss-robust disturbance alarm, our solution lowers the hardware entry cost of security-monitored QKD, hence fostering its adoption at the cost-sensitive network edge.

---


### 108. [Machine learning and digital pragmatics: Which word category influences emoji use most?](https://arxiv.org/abs/2608.21975)

**<font color=#1a73e8>作者：</font>** Mohammed Q. Shormani, Yehia A. AlSohbani, Mohammed Q. Shormani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study examines the performance of the state-of-the-art MARBERT model in identifying the lexical/pragmatic category associated with emoji use on X within a digital pragmatics approach (DPA). A net corpus of 15856 Colloquial Arabic (CA) posts containing emojis was collected from X using Python. The texts were tokenized and normalized into 4 lexical categories, namely noun_norm, verb_norm, adj_norm, and adverb_norm, and 2 pragmatic/structural categories, question_norm and exclamation_norm. MARBERT was finetuned and optimized to identify which category scores standard metrics more, hence associated with emoji use, while binary logistic regression was used to examine which category is statistically associated with emoji occurrence. Findings unveil that nouns dominate the corpus in normalized frequency (M = 0.675, SD = 0.161), followed by verbs (M = 0.083, SD = 0.100). However, verbs have the strongest influence of emoji use indicated by verb density (\b{eta} = 0.821, p = .001, 95% CI [0.332, 1.309]). The study concludes that in digital pragmatics of CA on X, emoji use association with lexical/pragmatic category can be explained by a hybrid approach of computational, statistical, and pragmatic methods, reflecting the interaction among machine learning, linguistic/lexical features, contextual representation, and pragmatic communication.

---


### 109. [How Reliable Are NVD CWE Labels? A Large-Scale Semantic Audit with Seclometry](https://arxiv.org/abs/2608.21977)

**<font color=#1a73e8>作者：</font>** Yu Nong, Yao Du, Majid Behravan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> CWE labels in the National Vulnerability Database (NVD) are widely treated as ground truth for vulnerability search, scanner evaluation, benchmark construction, learning-based security tools, and vulnerability prioritization. Yet their reliability has not been systematically measured at scale, despite growing concerns about NVD's enrichment backlog and anecdotal reports of inaccurate, ambiguous, or missing labels. This paper presents a large-scale, code-semantics-grounded measurement of CWE labeling quality in NVD. We build CWEAgent, a validated auditing instrument based on seclometry, a structured representation of vulnerability semantics that captures the root cause, trigger condition, violated security property, exploit mechanism, and impact of vulnerable code. On a manually curated benchmark of 100 open-source CVEs, CWEAgent achieves 85% top-1 accuracy and 92% ambiguity-aware accuracy. Applying CWEAgent to 15,556 open-source CVEs disclosed from 2017-2026, we find that only 49.70% of NVD CWE labels exactly match the code-grounded label. Another 31.37% are defensible alternatives under taxonomy ambiguity, while 3.63% are evidence-inconsistent likely errors. Label reliability varies sharply by assigning organization and weakness type, and apparent project- or language-level differences are largely composition effects of those underlying weakness types. Evidence-inconsistent labels have also increased over time. Through manual review of 434 confirmed mislabels, we identify six recurring error patterns, showing that CWE noise is a structural problem in vulnerability metadata rather than isolated annotation mistakes.

---


### 110. [Beyond Similarity: Heterogeneous Graph Learning for Multi-Objective Food Substitution in Charitable Food Agencies](https://arxiv.org/abs/2608.21979)

**<font color=#1a73e8>作者：</font>** Naimur Rahman Chowdhury, Limon Bin Hossain  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Charitable food agencies play an important role in alleviating food insecurity by distributing donated food to people in need. However, they rely on ad hoc in-kind donations and often face shortages of specific foods, so they offer substitutes. A good food substitution requires matching household preferences, nutritional needs, and item similarity. Agencies have limited direct records of consumption behavior due to resource constraints, making it challenging to make an appropriate substitution decision that meets multiple criteria. In this study, we propose a heterogeneous graph neural network (HeteroGNN), a source-grounded recommendation framework for food substitution in charitable food agencies. We first build a unified relational graph from large-scale public data sources, combining household behavior on food consumption and food nutrient information in the United States (US) context. We treat the substitution recommendation as a multi-objective ranking problem with three targets, including behavior affinity, health suitability, and substitution similarity. We train and validate the proposed framework under standard graph relationship and adverse cold-start settings by removing relational edges from the graph. Our results show that the proposed framework leverages relational information beyond node features in predicting consumption behavior. Additionally, the proposed framework remains robust with sparsity when the model receives incomplete information about behavior and nutrient features. Finally, we show the weak correlation among different objectives, thereby justifying the multi-objective framing as a replacement for an aggregated decision. The proposed framework can help downstream charitable agency decision-makers make contextspecific substitution recommendations with limited information available.

---


### 111. [AI Grinding for Fun and Cryptanalysis](https://arxiv.org/abs/2608.21986)

**<font color=#1a73e8>作者：</font>** Lukasz Olejnik, Bartosz Naskrecki  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present an autonomous cryptanalysis workflow in which agents generate, test, and refine hypotheses before human review. The autonomous stage returns reproducible candidates with exact witnesses, controls, code, and run records. A researcher then decides whether the evidence establishes a break, defect, or coverage gap.
Two failure modes recur. First, a public algebraic map or input representation erases or exposes a relation that a construction must hide. Examples include multiplication by zero, boundary coefficients of a polynomial product, quotients, characters, Schur squares, and variable-length byte encodings without boundaries. Second, a simulator, error law, or parameter certification uses a distribution different from the one claimed. Several targets fail in both ways.
Every result has an exact witness and a discriminating control; every stated boundary has a proof. Three further targets yielded no attack but support narrower guarantees than a generic reading suggests.
Eight published constructions fail at stated parameters or claims. A Ring-LWR commitment opens to every message with probability one. One ciphertext reveals two middle-product encryption rows. A lattice e-voting protocol loses receipt-freeness. A permutation-recovery attack against updatable encryption extends by linear algebra to the old decryption key. An explicit normal basis splits a degree-63 instance into seven degree-nine instances. A signature hash outside the lattice setting maps two printable equal-length messages to the same digest. A rerandomisable scheme's accept bit is a threshold oracle on its decryption noise. Separately, a group-ring decision claim and a multivariate MinRank hardening fail at the assumption or accounting level rather than as complete construction breaks. Each failure occurs one level above its supporting assumption.

---


### 112. [Key Recovery from Residue-Confined Errors in Pradhan CRT-RLWE](https://arxiv.org/abs/2608.21989)

**<font color=#1a73e8>作者：</font>** Lukasz Olejnik, Bartosz Naskrecki  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We show that the CRT-FHE scheme of Pradhan et al.\ is insecure for laws within its assumed error distribution range. The secret key follows from the public key by a single ring inversion whenever the public multiplier is a unit. The plaintext is recovered from any ciphertext under such a law without the secret key, for every multiplier, giving chosen-plaintext advantage $1/2$. We further show that the transformation from ordinary Ring-LWE to CRT-RLWE does not preserve the error distribution, so it does not establish that CRT-RLWE is at least as hard as Ring-LWE.
One mechanism underlies both. The Chinese remainder theorem (CRT) function is reduced modulo $p_1p_2$ while its output is used modulo a coprime modulus $q$, so under every zero-preserving section an error in $p_2\R$ encodes to zero. The law $p_2B_1$ is so confined, meets the stated conditions, and decrypts correctly. Confinement is not a weakness of scale: scaling any baseline law by $p_2$ leaves its ordinary Ring-LWE problem exactly equivalent, while the reduced encoder destroys every error it produces. The reduction discrepancy is a multiple of $p_1p_2$ and not of $q$, so the small-error premise of the proof cannot remove it, and at the reported parameters a single error coefficient refutes the identity while satisfying that premise. The centered binomial $B_2$ separates the coefficient laws at total variation distance $3/8$, and at the reported dimension that distance between the induced polynomial laws is exponentially close to one.

---


### 113. [Variance Driven Exploration: A Provable and Efficient Methodology for Pure Exploration in Highly Stochastic Environments](https://arxiv.org/abs/2608.21995)

**<font color=#1a73e8>作者：</font>** Khang Luong, Nam Nguyen, Hoang Ta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose Variance Driven Exploration (VarDE), a principled approach for pure exploration in highly stochastic environments, where the exploration process is dominated by stochastic variance. VarDE is built on a fundamental principle: sampling effort should be allocated to minimize the uncertainty of the final decision. We formalize the uncertainty of the final decision through a smooth decision function and derive allocation rules that explicitly capture how stochastic noise in individual components affects the reliability of the final output. We apply this methodology to three core problems of pure exploration -- Best Arm Identification (BAI), Monte Carlo Tree Search (MCTS), and Best-Policy Identification (BPI) -- with theoretical guarantees on variance decay and simple regret. Empirically, we demonstrate consistent and significant improvements of VarDE over existing methods, with especially strong gains in highly stochastic environments.

---


### 114. [DySCo: Dynamically consistent data-driven downscaling of extremes in climate projections](https://arxiv.org/abs/2608.21998)

**<font color=#1a73e8>作者：</font>** S. Stamatelopoulos, M. Wang, I. Lopez-Gomez 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Regional climate risk assessment is critical for applications such as infrastructure design, disaster forecasting, and insurance resource allocation. However, estimating regional (i.e., high-spatial-resolution) risk with global climate models (GCMs) remains computationally prohibitive, which has driven the development of downscaling methods for coarse GCM outputs. Downscaling is vital for rare events, since quantifying their extreme properties requires high spatial resolution and very long GCM simulations. These methods non-intrusively increase GCM resolution while correcting statistical biases from unresolved fine-scale processes, thereby improving the accuracy of extreme event statistics with long return periods. A key challenge is preserving dynamical consistency, as freely evolving GCM trajectories are not expected to track the observational dataset used for training the correction operator. This is critical for causal extreme event analyses, where storyline-based risk assessment, i.e., extreme event catalogs, is necessary for effective planning. We address this challenge by introducing Dynamically and Statistically Consistent downscaling (DySCo), a non-intrusive framework yielding high-resolution climate projections consistent with coarse GCM dynamics. DySCo relies on a data-driven reformulation of nudging to create dynamically paired training trajectories without intrusive GCM modifications. Using these paired trajectories, we train a dynamically and statistically consistent, two-stage operator. We evaluate the method by downscaling the Community Earth System Model v2 Large Ensemble (LENS2) in time and space towards historical reanalysis. Results show DySCo achieves superior dynamical consistency with the coarse GCM trajectories, essentially applying a minimal, causal correction to the GCM, preserving top statistical performance comparable to state-of-the-art unsupervised models.

---


### 115. [Close Shortcut Wins Long: Seeking Diverse and Stable Generators for Data-Free Knowledge Distillation](https://arxiv.org/abs/2608.22003)

**<font color=#1a73e8>作者：</font>** Kailin Lyu, Zherui Zhang, Junhao Dong 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Data-Free Knowledge Distillation (DFKD) preserves privacy by transferring knowledge without real data access. However, existing generator-based DFKD methods suffer from over-reliance on teacher preferences and pattern collapse, exhibiting "generative shortcut learning" in the frequency domain: dependent on specific frequency components and frequency positions, resulting in inconsistent synthetic image quality and class diversity. In this paper, we propose a CSWL framework aimed at introducing insights from the frequency domain perspective to improve generator diversity and training stability to Close the phenomenon of Shortcut learning to Win in the Longer term. To address the issue of generative shortcut learning, we introduce frequency-domain augmentation at the feature level, encouraging the generator to attend to the full frequency spectrum and thereby suppress shortcut learning behavior. To tackle training instability, we propose a Cross-Stage Frequency Reconstruction (CSFR) auxiliary task, which implicitly constructs an Exponential Moving Average (EMA) mechanism to promote long-term optimization and stability. Extensive experiments, including downstream tasks and various image recognition datasets at multiple resolutions, validate the effectiveness of CSWL in improving both diversity and stability from the frequency view.

---


### 116. [Spectral Pre-Filtering for Context-Adaptive Sensor Fusion: A Four-Role FFT-GDCB Integration for High-Stakes Decision Systems](https://arxiv.org/abs/2608.22023)

**<font color=#1a73e8>作者：</font>** Oleg Miroshnichenko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Context-adaptive Kalman filters calibrate their noise covariance matrices Q and R from innovation residuals via online regression. When the underlying sensor or signal carries periodic structure -- mechanical LiDAR rotation harmonics, engine vibration, ground multipath, weekly and annual demand cycles, dosing-interval rhythms, weekly media-buying cadence -- the regression input is contaminated and the fitted covariance models structural modes rather than genuine state uncertainty. We introduce a four-role FFT pre-filter that solves this problem at $O(N\log N)$ cost and serves three additional roles "for free": (i) it whitens coloured noise before the Kalman update, restoring the optimality assumption; (ii) it cleans innovations before covariance regression, preventing periodic contamination of $\hat{R}$ and $\hat{Q}$; (iii) it generates spectral context features that enrich the downstream bandit's regime-selection state; (iv) it deseasonalises the input feature vector before any supervised regression that produces a sensitivity coefficient (beta, dose offset, bid modifier). We position the algorithm inside the Gated Decoupled Compositional Bandits (GDCB) family, where it acts as a preprocessing layer for the supervised scaler. The single $O(N\log N)$ FFT call thereby serves four downstream consumers, fits in <0.1% of the sensor-fusion or pricing-pipeline compute budget, and is a drop-in addition with no changes to the Kalman filter, bandit, or runtime composition operator. We summarise empirical validation across six independent domains (rocket descent, autonomous-vehicle tracking, short-term rental pricing, clinical drug dosing, airline fare distribution, and ad-operations bid calibration), all returning a PROVES verdict under a pre-registered evaluation protocol.

---


### 117. [One-Step Evolution for Long-Time Extrapolation: An Error-Bound-Informed and Prior-Guided Neural Residual Framework for Autonomous PDEs](https://arxiv.org/abs/2608.22026)

**<font color=#1a73e8>作者：</font>** Maqun Zhang, Feng Gao, Wankun Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate simulation of the long-time evolution of systems governed by partial differential equations (PDEs) is central to scientific computing. Among existing deep learning?based approaches for solving PDEs, neural operators typically rely on extensive trajectory data, whereas physics-informed meth?ods often exhibit limited stability during long-time extrapolation. For a well-posed autonomous PDE, long-time trajectories can be generated by repeated composition of a fixed-step evolution operator; hence, long-time extrapolation depends on controlling the approximation error of this operator and the propagation of that error under recursive composition. Accordingly, we propose a numerical-prior-guided, physics-constrained method trained without ground-truth trajectory supervision: a low-cost numerical prior reduces the difficulty of approximating the one?step evolution operator, while a weak-form PDE residual provides a computable proxy for the one-step error term in the error?propagation bound. We validate the method on five benchmark cases spanning four PDE classes and compare it with ten physics?informed learning methods under a unified protocol that excludes ground-truth trajectories from training and model selection. The results indicate that, in all five cases, the proposed method reduces long-time extrapolation error relative to the numerical prior and outperforms the best competing baseline in each case, thereby improving long-time simulation accuracy across different PDEs without ground-truth trajectory supervision. The source code developed for this paper will be made publicly available upon acceptance of the manuscript.

---


### 118. [ARCHER: Amortized cross-specimen pose estimation for cryo-electron microscopy](https://arxiv.org/abs/2608.22029)

**<font color=#1a73e8>作者：</font>** Nhan D. Nguyen, Bao Pham  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Single-particle cryo-electron microscopy (cryo-EM) pose estimation is traditionally solved anew for each dataset, where iterative refinement is done from scratch while the estimator learns to store the molecule in its weights. In this work, we show that pose inference is a generalizable, specimen-agnostic operation when conditioned explicitly on a reference volume. We introduce ARCHER, an amortized contrastive classifier that models the pose posterior over a discrete rotation grid. Trained across a variety of protein structures, it operates zero-shot without retraining per structure. This transferability is grounded in Fourier-space information mechanics, where all specimen dependence is captured by the reference structure's power spectrum and spatial extent. ARCHER achieves a median angular error of 5.0° on 100 held-out test structures and 2.5° on experimental particles, matching dedicated estimators within 0.16 Å in 3D reconstruction. Crucially, downstream conformational signal is preserved. The leading conformational coordinate correlates at 0.97 with deposited benchmarks, faithfully reconstructing free-energy basins and mobile domains. These results overall demonstrate that cryo-EM pose estimation can be generalized across different structures.

---


### 119. [Align, Unify, Suppress, Route: A Coherentist View of Transformer Computation](https://arxiv.org/abs/2608.22034)

**<font color=#1a73e8>作者：</font>** Nura Aljaafari, Andre Freitas  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mechanistic interpretability has identified transformer circuits, but lacks a shared vocabulary for describing how their functions compose across tasks and architectures. We introduce Coherentist Probabilistic Compositionalism (CPC), an interpretive framework that grounds transformer computation in coherentist theories of interpretation and describes it through four operator roles. Alignment identifies candidate relations, unification integrates supporting information, suppression reduces incompatible alternatives, and routing carries selected information to the output. Across 15 models from five architecture families, the suppression, unification, and routing weight-space signatures correlate with held-out activation-level role measures above random baselines. Suppression is more stable across tasks than unification. Ablating alignment heads reduces downstream suppressive activity beyond a random-head control in 10 models, but similar effects on no-conflict prompts indicate a general upstream dependency, not contradiction-specific coupling. Explicit contradictions significantly shift a layerwise coherence proxy in 14 models; after removing shared residual covariance, the gap has the predicted direction in every model. Base and instruction-tuned variants preserve induction-head score structure ($r{\geq}0.98$) without a consistent shift of operator signatures towards later layers. These results support CPC as a shared vocabulary for comparing transformer mechanisms while showing that their depth and geometric expression remain architecture-specific.

---


### 120. [ORBIT++: Benchmarking SfM in the Wild with 360° Video](https://arxiv.org/abs/2608.22039)

**<font color=#1a73e8>作者：</font>** Sara Sabour, Linyi Jin, Richard Tucker 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Structure-from-Motion (SfM) is a cornerstone of 3D perception, yet current methods often fail when applied to complex videos involving challenging camera motions or dynamic scenes. Compounding the problem, the field lacks reliable ground-truth benchmarks for such difficult scenarios, making it hard to gauge real-world progress or to pinpoint where improvements are most needed. To address this gap, we introduce a new benchmark for evaluating camera pose estimation. Our key insight is to leverage online panoramic 360° video as a source of data from which to construct challenging clips, while still enabling robust ground-truth trajectory recovery. The panoramic nature of these videos provides richer visual context for tracking camera motion, even when parts of the view are affected by blur, motion, or dynamic objects. After tracking camera motion across full 360° videos, we crop and reproject selected portions to generate perspective-view clips that serve as our benchmark, called ORBIT. Experiments show that COLMAP, as well as recent optimization-based and feed-forward SfM methods struggle to accurately estimate camera poses on our benchmark. Hence, ORBIT provides a valuable testbed where researchers can meaningfully measure progress on truly challenging, real-world SfM problems.

---


### 121. [ReMAP: Self-supervised learning to unveil brain representations and vulnerability](https://arxiv.org/abs/2608.22042)

**<font color=#1a73e8>作者：</font>** Jade Perdereau, Virginie Loison, Kanssa El Ayeb 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> General anesthesia offers a rare opportunity to observe the human brain under a standardized, controlled perturbation. Yet intraoperative electroencephalography (EEG) is almost always reduced to a single proprietary depth index, collapsing a rich trajectory into one number and discarding how a brain moves between states. Here we ask whether the geometry of that trajectory, not merely the depth it reaches, carries clinically meaningful information. Using similarity-based self-supervised learning on raw, two-electrode frontal EEG, with no labels, we place each recording within a low-dimensional space in which anesthetic depth becomes one readable axis while the shape of a patient's path encodes additional structure. We validate the representation across two cohorts and two acquisition systems totaling more than 1,000 patients. Depth of anesthesia is predicted accurately (BIS mean absolute error = 3.2, R2 = 0.82), and in the sparse-montage setting our compact ( 68k parameter) model remains competitive with EEG foundation models orders of magnitude larger (4M-157M parameters), indicating that matching the representation to the recording dominates raw scale. The learned space organizes age along its own gradient, independent from depth, without supervision. The same space also aligns with interpretable anesthetic signatures like frontal alpha, slow-delta, and burst suppression, linking this data-driven representation to established neurophysiology. On an independent cohort with longitudinal follow-up, the geometry of the early trajectory separates 30- month cognitive and mortality outcomes complementary to age (AUROC 0.86). These results suggest that the path a brain traces through anesthesia is a label-efficient correlate of latent vulnerability, motivating prospective validation.

---


### 122. [Multi-Agent Discovery and Resource-Aware Autonomous Exploration of Scientific Datasets](https://arxiv.org/abs/2608.22045)

**<font color=#1a73e8>作者：</font>** Aashish Panta, Hugo Lee, Giorgio Scorzelli 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Modern scientific facilities and instruments generate datasets at scales that are difficult for individual researchers to discover, access, and explore. Although many datasets are publicly available, using them often requires familiarity with repository organization, data formats, multiresolution structures, and visualization parameters. We present WebVisus, a constrained and resource-aware multi-agent system for discovering and autonomously exploring remote, multiresolution scientific datasets. Given a natural-language research question, WebVisus identifies the user's intent and launches an autonomous exploration agent that examines slices, volumes, and timesteps while adapting data resolution and retrieval quality to available client memory and computational resources. This design supports progressive exploration without complete dataset downloads or manual configuration of low-level visualization parameters using natural languages. We report the system architecture, constrained agent protocol, resource-aware access mechanism, and case studies evaluating autonomous visual exploration and resource-aware agentic access across scientific datasets.

---


### 123. [Robust Global Structure-from-Motion via View Graph Pruning](https://arxiv.org/abs/2608.22054)

**<font color=#1a73e8>作者：</font>** Jiamin Xu, Lixing Yao, Weichen Dai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Structure-from-Motion (SfM) aims to estimate camera poses and reconstruct 3D structures from a collection of unordered images. Compared with incremental SfM, global SfM achieves better scalability by jointly estimating camera poses based on a view graph constructed from pairwise correspondences. However, its performance is highly sensitive to erroneous edges caused by visually ambiguous matches, which may lead to incorrect camera registration and reconstruction artifacts. In this work, we propose a subgraph-guided view graph pruning framework for robust global SfM. Our key idea is to exploit the internal consistency of reliable subgraphs to identify and remove unreliable connections. Specifically, we first partition the view graph into locally consistent subgraphs and perform global SfM within each subgraph to obtain reliable camera poses. We then apply RANSAC-based edge pruning across subgraphs to remove inconsistent edges, and finally perform global SfM on the refined view graph. Extensive experiments on ambiguous, sequential, and unordered image datasets demonstrate that our method improves the robustness of global SfM under challenging conditions. Further evaluation with neural rendering shows that the improved camera estimation leads to higher-quality novel view synthesis results.

---


### 124. [Personalized and Aspiration-Oriented Career Path Recommendation](https://arxiv.org/abs/2608.22056)

**<font color=#1a73e8>作者：</font>** Kuleshwar Sahu, Girish Keshav Palshikar, Rajiv Srivastava  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fulfilling career aspirations is important for growth of employee and organization. We propose a data driven methodology to recommend personalized career path for a given aspirant's career path and aspirations. The pro-posed method uses the career path similarity (CPS) between aspirant's career and candidate career path, and 'aspirational similarity' (AS) between aspiration and candidate career paths to find suitable career path. CPS ensures personalized recommendation while AS ensures aspiration fulfillment. We defined two methods to compute the CPS between career paths which are (a) domain knowledge driven (DKD) and, (b) unsupervised representation learning and alignment (URLA) based, along with different AS measures. The DKD based similarity is defined in the terms of features extracted and summarized over career paths. In the URLA, we use the sequence of event names present in the career paths of the employees to learn the embedding for each event name. In URLA we use learned embedding vector of the career path event names and as-sociated event attributes (skill cluster and domain) to find the best alignment between two career paths. We hypothesized that relative position of event names in the sequence represents semantics of event name and that can be learned. We use LSTM neural network to learn the embedding vector of each career event name. We also define the matching method to compute the AS be-tween aspiration and career path in both proposed methods. We combine CPS and AS to rank available 'candidate career paths' of employees to find the suitable one. We get better DCG value in URLA as compare to DKD. We also showed that ranking are coherent using both the methods. URLA method is better since it does not require domain knowledge to model the similarity and includes temporal aspect by optimal Levenshtein alignment using weighted cosine distance.

---


### 125. [Competitive Memory Readout for Robust Video Object Segmentation: 2nd Place Technical Report for the MOSEv2 Track of the 8th LSVOS Challenge](https://arxiv.org/abs/2608.22064)

**<font color=#1a73e8>作者：</font>** Mingqi Gao, Sijie Li, Jungong Han  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present our solution for the MOSEv2 track of the 8th Large-scale Video Object Segmentation (LSVOS) Challenge at ECCV 2026. The challenge evaluates robust video object segmentation under complex temporal dynamics, including long-term occlusion, disappearance and reappearance, large appearance changes, and strong interference from visually similar objects. Our method builds on SAM~3 and focuses on its memory readout. Standard target-only memory retrieval can confuse the annotated target with same-class non-target objects because such distractors are represented only implicitly as background. Our method introduces Competitive Memory Readout, which explicitly incorporates same-class competitor evidence when retrieving target information from memory. To prevent excessive suppression of weak or reappearing targets, we further apply a lightweight adaptive restoration rule after competition. The resulting system retains the original SAM~3 tracking pipeline while improving target identity preservation in challenging videos. Our submission achieves 66.20 on the primary challenge score and ranks 2nd in the MOSEv2 track.

---


### 126. [Spiking Neural Networks for Energy-Efficient Object Detection in Forward-Looking Sonar Imagery](https://arxiv.org/abs/2608.22072)

**<font color=#1a73e8>作者：</font>** Gwenevere Frank, Gert Cauwenberghs  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous underwater vehicles (AUVs) are increasingly important tools in industries ranging from research, to energy, to defense. AUVs are power-constrained platforms operating in remote environments with fixed battery capacities, where propulsion competes with compute and sensors for power over lengthy mission durations. AUVs frequently operate in dark or turbid waters where optical sensing is of limited value, and rely on sonar as their primary sensing modality. Convolutional neural networks (CNNs) are the state-of-the-art solution for object detection in forward-looking sonar imagery, but are energy expensive (e.g. YOLOv8m: 322 mJ/inference). Spiking neural networks (SNNs) rely on binary spike activations and thus sparse accumulate-only operations, allowing them to be remarkably energy efficient, particularly when paired with dedicated neuromorphic hardware. The sparse, high-contrast structure of forward-looking sonar (FLS) returns is structurally matched to spike coding in a way that optical imagery is not. No prior work has assessed the suitability of SNNs for object detection in FLS imagery. SpikeYOLO, a fully spiking network trained with surrogate gradients, was benchmarked against state-of-the-art CNN baselines on three FLS object detection datasets. Key results: SpikeYOLO T=2 achieves 3.3$\times$ lower theoretical compute energy on UATD (97 vs 322 mJ) at competitive accuracy (0.529 mAP@0.5:0.95 vs. YOLOv8m's 0.575); SpikeYOLO matches YOLOv8m on mAP@0.5 and outperforms YOLO-SONAR and Fast R-CNN baselines on the sparse Marine-Debris-FLS dataset at 4.4$\times$ lower energy; SpikeYOLO demonstrates superior robustness to multiplicative speckle noise (3.0% degradation at $\sigma{=}0.4$ vs. 8.9% for YOLOv8m), outperforming YOLOv8m outright at $\sigma{=}0.6$, directly relevant to real-world FLS deployment.

---


### 127. [Autonomous Cyber Defense: Real-Time Attack Detection and Mitigation in Software-Defined Networks Using Machine Learning](https://arxiv.org/abs/2608.22075)

**<font color=#1a73e8>作者：</font>** Alexandre Amaral, Fernando Moro, Ana Malheiro  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Adversaries now move faster than manual response processes can absorb. The average eCrime breakout time, that is, the interval between initial access and the first lateral movement to another host, fell to 29 minutes in 2025, a 65\% increase in speed over the previous year; the fastest observed breakout took 27 seconds, and in one intrusion data exfiltration began within four minutes of initial access. This work presents a machine learning based system that monitors network traffic in real time, diagnoses attacks, and automatically applies countermeasures in software-defined networks, so that detection and response no longer depend on human intervention. The system comprises two modules: \textit{Network Dataset Creation} (NDC), which collects IP flows, preprocesses and aggregates them to build the training dataset, and \textit{Intrusion Prevention System} (IPS), which automates the modeling, training, and evaluation of different algorithms and triggers blocking actions on the SDN controller. A case study with a \textit{SYN flooding} denial of service attack, shows the attack being detected and blocked in 21 seconds without human intervention, a response time compatible with the window imposed by current breakout times.

---


### 128. [Improving Energy Efficiency of Oil Platforms Through Optimal Loading of Diesel Generators Using Machine Learning and Search Algorithms](https://arxiv.org/abs/2608.22076)

**<font color=#1a73e8>作者：</font>** Khivishta Boodhoo, Josh Plumbly, Nicholas Watson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rising energy demand, fossil fuel depletion and climate change highlight the need for more efficient energy production and consumption. Offshore oil and gas platforms face challenges related to inefficient energy use, system failures, accessibility and environmental impact. Machine learning (ML) offers opportunities to improve the safety, sustainability and efficiency of these systems; however, previous research has largely focused on increasing oil production rather than reducing energy consumption on platforms. This study investigates the use of ML and search algorithms to improve diesel efficiency on an offshore oil platform. Data collected over 18 months from a platform in Scotland were analysed, focusing on four diesel generators as the primary diesel-consuming equipment. Following exploratory data analysis and outlier detection, regression models were developed to predict daily diesel consumption for different generator power loads. Multiple Linear Regression and Artificial Neural Networks achieved the best predictive performance compared with Extra Trees Regression, Extreme Gradient Boosting and Random Forest. Search algorithms were then used to identify combinations of generator power loads that minimised daily diesel consumption. The results showed an average diesel saving of 27% per day compared with the worst daily power-load combinations, equivalent to approximately 24,000 litres/day. These findings demonstrate significant opportunities for improving energy efficiency on offshore oil platforms using ML-based optimisation.

---


### 129. [When More References Hurt: Contamination-Aware DINOv2 Memory Banks for Few-Shot Steel Defect Detection](https://arxiv.org/abs/2608.22082)

**<font color=#1a73e8>作者：</font>** Hannaneh Kalantari, Javad Khoramdel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Patch-memory anomaly detectors assume that their reference bank is normal, an assumption that is difficult to guarantee when additional industrial images are unverified. We study whether a few trusted normal images can safely recover useful normal patches from such references without defect masks. Starting from the DINOv2 patch-memory formulation used by AnomalyDINO, we score candidate patches by distance to a clean seed bank, discard the most suspicious 20%, merge the retained patches with the seed, and enforce a fixed budget by greedy coreset selection. On Severstal, naive additional references contain 9.46% anomalous patches; the proposed trim rejects 78.1\% of them and reduces residual contamination to 2.59%. At an equal 51,200-patch development budget, the proposed bank reaches 0.1084 AUPRC versus 0.0950 for naive expansion, 0.0952 for random removal, and 0.1030 for eight clean images. Injecting only 0.5\% anomalous patches into a clean bank reduces AUPRC from 0.1030 to 0.0759. On all five completed held-out pairs, the proposed bank improves over naive expansion, with a mean gain of 0.0142 AUPRC. Reference purity is therefore a first-order design variable, and unverified images are useful only when their contribution is filtered explicitly.

---


### 130. [Counterfactual Quotient Models: Learning What Actions Change, Not What the World Does](https://arxiv.org/abs/2608.22092)

**<font color=#1a73e8>作者：</font>** Junlin Chen, Ruijie Wang, Jianxin Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement-learning models commonly predict complete future states, observations, or feature occupancies, even though action selection depends only on differences between the consequences of candidate actions. As a result, these models may devote substantial statistical and representational capacity to high-dimensional phenomena that evolve independently of the agent's current choice. We introduce the Counterfactual Quotient Model, which treats action-conditioned futures as equivalent when they differ only by a component shared across actions. Its canonical centered representation removes this common component while preserving every pairwise action comparison expressible by the modeled reward family. The implemented model learns these action-dependent effects directly from synchronized counterfactual rollouts, so shared stochastic dynamics cancel before function approximation rather than after complete futures have been predicted. We establish the decision sufficiency, identifiability, common-mode invariance, approximation behavior, and regret properties of the resulting representation. Controlled experiments in physics-based environments provide initial evidence for these properties: direct effect learning suppresses action-independent variation, supports previously unseen reward queries, and improves action ranking relative to models trained to predict absolute futures.

---


### 131. [Three-Phase Scribble-Adaptive Curriculum Learning for autoPETV Grand Challenge](https://arxiv.org/abs/2608.22096)

**<font color=#1a73e8>作者：</font>** Libo Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This report describes Libo Zhang's algorithmic solution to autoPETV Grand Challenge on interactive lesion segmentation in whole-body PET/CT. Interaction is encoded as two additional input channels that rasterize the accumulated foreground and background scribbles, and a residual-encoder U-Net of about 140 million parameters is trained with a three-phase curriculum over 4000 epochs: the network first learns fully automatic segmentation with silent interaction channels, then observes ground-truth-derived scribbles under randomly sampled visibility modes, and finally adapts to its own mistakes through online simulation of up to five error-driven correction steps. Training draws on 1811 autoPET and DeepPSMA studies, and the submission ensembles the best and final checkpoints of five folds by logit averaging. In interactive five-fold cross-validation with six interaction steps, the final checkpoints reach a mean AUC-Dice of 3.836 and a mean AUC-DMM of 3.869, improving monotonically in every fold, with roughly half of the total gain delivered by the first corrective scribble. Our code and trained model checkpoints are available on this https URL.

---


### 132. [Beyond Fresh Starts: Stateful Inference for Streaming ASR in Conversational Voice Agents](https://arxiv.org/abs/2608.22101)

**<font color=#1a73e8>作者：</font>** Sameep Chattopadhyay, Alexander Erdmann, Mari Ostendorf  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern voice-agent systems rely on streaming speech recognition models that operate under stringent latency constraints. This study shows that, due to the limited memory constraints of real-time processing, these systems are adversely impacted by conversational phenomena such as long silences and backchannels. While many agentic pipelines mitigate this by resetting state at each turn, this approach discards vital context and impairs performance at turn onsets. We propose two state-management strategies that preserve cross-utterance context to reduce onset errors. In experiments with two state-of-the-art streaming models on two spoken dialogue benchmarks, our best method yields an average of 15-21% relative WER reduction at utterance onsets.

---


### 133. [Learning Implicit Constitutive Laws for Dynamic 3D Gaussian Splatting from Monocular Videos](https://arxiv.org/abs/2608.22102)

**<font color=#1a73e8>作者：</font>** Xiaoyang Liu, Kai Han  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present GCA (Gaussian Constitutive Alignment), a framework for learning implicit constitutive laws from monocular dynamic video of deformable objects represented by 3D Gaussians. Given a static multi-view scan for geometric initialization, our method learns intrinsic physical dynamics solely from a single fixed-viewpoint video of the moving object. Existing implicit methods often suffer from local minima under noisy supervision and lack physical interpretability, while explicit approaches rely on predefined constitutive equations, limiting generalizability and becoming unstable in monocular settings. To address these challenges, our framework unifies LoRA-based adaptation with two key alignment modules. First, we propose Rank-based Depth-Geometric Anchors (RDGA) to establish robust geometric constraints from monocular dynamic observations via scale-invariant rank-based depth alignment, reducing the reliance on unreliable pixel-level color supervision. Second, a Constitutive Prior Regularizer (CPR) integrates classical constitutive models as soft differentiable priors, regularizing the optimization while preserving the flexibility of implicit modeling---even when the actual material is absent from the hypotheses. Extensive experiments on synthetic, real-to-sim, and real-world datasets demonstrate that GCA outperforms existing methods, achieving 48% lower Chamfer Distance than the strongest baseline on synthetic benchmarks while remaining robust under monocular supervision.

---


### 134. [Opinion-Guided Layered Strategies for Decentralized Coordination](https://arxiv.org/abs/2608.22104)

**<font color=#1a73e8>作者：</font>** Shuhao Qi, Zhiyong Sun, Siep Weiland 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Autonomous agents increasingly interact with other independent agents, and such interactions typically admit multiple joint behaviors. When two agents prefer different ones, their independent strategies may be mutually incompatible and fail to reach a coordinated outcome; when they are identical, neither can differentiate its role when needed. Ideally, an agent should coordinate with any agent it encounters, regardless of which admissible joint behavior that agent aims to realize. We therefore propose a new form of strategy, the opinion-guided strategy, which keeps all the admissible joint behaviors available and postpones the selection to execution time, when the other agent's behavior reveals which one to realize. To realize this, nonlinear opinion dynamics are leveraged in a layered realization to guide the agent to a common admissible joint behavior in response to the other agent's evolving behavior, even without communication. We formally establish the conditions under which the strategy remains robust to every preference the other agent may hold. This robustness has an important implication: two agents running identical strategies can break symmetry when needed, a capability that conventional strategies lack. Three case studies across different applications show that the opinion-guided strategy coordinates with every randomly encountered agent, as long as it is willing to realize one of the admissible joint behaviors. One of them corresponds to a general-sum game: unlike conventional approaches devoted to finding a unique Nash equilibrium in advance, the opinion-guided strategy keeps every equilibrium open and guarantees the agents reach one, decided by their runtime interaction.

---


### 135. [Symbolic Neural ODEs: Learning interpretable models from time-series data](https://arxiv.org/abs/2608.22112)

**<font color=#1a73e8>作者：</font>** Nibodh Boddupalli, Jeff Moehlis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a machine learning framework for identifying sparse, interpretable models of dynamical systems directly from time-series data. Our approach parameterizes the underlying vector field using a neural architecture and trains it by minimizing a multi-step prediction loss over a finite horizon. To ensure numerical tractability, we optimize a mean absolute error objective averaged across prediction steps, and progressively increase the horizon during training. A key feature of this formulation is that it enforces consistency under repeated composition of the learned dynamics. As a result, the identified models exhibit significantly improved stability compared with approaches based on one-step regression of the vector field. When combined with sparsity-promoting regularization, this leads to parsimonious models that generalize beyond the training data. We demonstrate accurate recovery of systems exhibiting a wide range of behaviors, including stable and unstable fixed points, periodic orbits, and chaotic attractors. For chaotic systems, while long-term trajectory prediction is inherently limited by sensitivity to initial conditions, we show that multi-step training yields models with accurate short-term dynamics and strong agreement in long-time statistical properties, including mean, variance, and Lyapunov exponents. Moreover, we establish theoretical bounds linking trajectory error to statistical accuracy, providing a step toward a principled explanation for this behavior.

---


### 136. [CST: Collaborative Selective Transmission for Communication-Efficient Multimodal Edge Inference](https://arxiv.org/abs/2608.22115)

**<font color=#1a73e8>作者：</font>** Hai Chi, Junrui Zhang, Rui Ning 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Collaborative multimodal inference improves edge perception by combining observations from distributed sensing devices, but transmitting high-dimensional helper representations incurs substantial communication overhead and can lead to high end-to-end latency. Existing communication-efficient methods reduce payloads through compression, semantic coding, or feature selection, yet typically optimize compactness or task relevance without explicitly accounting for information already represented at the main device. Consequently, task-relevant but redundant helper features may still consume bandwidth. We present Collaborative Selective Transmission (CST), a main-directed query--response framework that retrieves only helper information complementary to the current main representation. Inspired by Partial Information Decomposition and the Multiview Redundancy Assumption, CST learns sample-adaptive, helper-specific sparse retrieval supports while discouraging retrieval of semantics already covered by the main device or duplicated across helpers. During inference, the main device transmits only support indices, and each helper returns the corresponding latent values, avoiding dense helper-feature exchange. Across three real-world multimodal sensing benchmarks, CST transmits no more than 14.18% of helper feature values while achieving best or near-best task performance among the evaluated methods. Experiments on a five-node NVIDIA Jetson Orin Nano testbed across 5--100 Mbps demonstrate up to a $4.27\times$ speedup over Transmit-All in end-to-end inference, confirming practical end-to-end latency reductions.

---


### 137. [Vehicle speed dataset for the major European road network derived from Sentinel-2 imagery, 2022-2026](https://arxiv.org/abs/2608.22116)

**<font color=#1a73e8>作者：</font>** Maciej Adamiak, Sascha Fendrich, Julian Psotta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The dataset provides individual vehicle speed observations on European E-roads: motorways, trunk roads, primary and secondary roads, as tagged in OpenStreetMap as e-road, for the years 2022-2026. Speeds are derived from Copernicus Sentinel-2 Level-2A satellite optical imagery using a processing pipeline that exploits the short, well-characterized acquisition delays between the blue (B02_10m), green (B03_10m), and red bands (B04_10m) of the Sentinel-2 push-broom instrument. A moving vehicle appears at slightly displaced positions in the three bands, forming a moving echo. The detected displaced intensity peaks are linked into per-vehicle trajectories through a prediction-and-matching procedure. The resulting displacements are converted into ground speeds using publicly accessible inter-band time delays. Each record contains the trajectory geometry, per-channel displacements and headings, internal quality indicators, the estimated speed, the acquisition timestamp, and the source Sentinel-2 product identifier. The dataset is distributed as GeoPackage files, with one record per detected vehicle, and can support studies of traffic patterns, speed behavior, transport modeling, and the calibration of road network attributes at a continental scale.

---


### 138. [TANGO: Token-Aggregated Nonlinear Gating Operators for Natural and Formal Language Modeling](https://arxiv.org/abs/2608.22117)

**<font color=#1a73e8>作者：</font>** Joshua Nunley  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A standard Transformer block separates cross-token interaction in self-attention from a nonlinear feed-forward network applied independently at each position. We introduce the TANGO model (Token-Aggregated Nonlinear Gating Operators), which replaces these two sublayers with one cross-token gated residual update. Each source token produces a SwiGLU gate vector. Query-key similarities determine a weighted average of source gates for each destination, and the resulting gate rescales projected destination features. TANGO assigns a separate weight to every causally visible source and is quadratic in sequence length. The WANGO model (Windowed Aggregation of Nonlinear Gating Operators) retains the same unnormalized scores within a recent window and uses positive feature-map prefix statistics for older sources, giving linear sequence-length complexity for fixed window and feature dimensions.
We compare TANGO and WANGO with Recurrent and Untied Transformer++, full-attention GAU, and FLASH. All models have approximately 44.3M nonembedding parameters and are trained in three matched runs. TANGO, WANGO, and Recurrent Transformer++ apply one shared block four times; the other architectures use four independent blocks. TANGO obtains the lowest mean validation negative log-likelihood on FineWeb-Edu, Lean, and DeepMind Mathematics, although it has the largest analytical forward-pass operation count. WANGO obtains the lowest mean FineWeb-Edu NLL among the architectures with computation linear in sequence length and outperforms Recurrent Transformer++ at nearly the same analytical forward-pass multiply-accumulate count.

---


### 139. [The Price of Decentralization in Top-$K$ Arm Identification](https://arxiv.org/abs/2608.22120)

**<font color=#1a73e8>作者：</font>** Larissa Xu, Jasmine Nguyen, William Chang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cooperative teams often need to agree on the best few options rather than simply accumulate reward, and they must do so while each member sees only a fragment of the team's collective experience. We study this as top-$K$ joint-arm identification in multi-agent multi-armed bandits: at every round $M$ agents simultaneously choose individual actions that compose a joint arm, and the team must ultimately return the $K$ joint arms of highest mean reward. The difficulty is that an agent may not observe the actions of others, their rewards, or either. We treat three observability regimes---(A) shared rewards with hidden actions, (B) observed actions with private rewards, and (C) full asymmetry---and design communication-free elimination algorithms (UCB-Intervals) that reconstruct implicit coordination from whatever signal each regime leaves intact: a shared arm ordering in (A), observable deviations in (B), and enlarged confidence radii under (C). We give matching analyses in both the fixed-budget and fixed-confidence objectives, then fold all three regimes into a single meta-guarantee indexed by a multiplicity $c$ and a consensus factor $\rho$. Our central result is quantitative rather than merely algorithmic: change-of-measure lower bounds show that shared-reward identification is optimal up to one universal logarithmic factor, and that the entire statistical price of removing communication is a multiplicative $\rho^2$ in sample complexity---a fixed $4\times$ penalty under full asymmetry. The resulting stopping time scales as $O\!\left(\sum_{\mathbf{a}} \frac{\log(A^M/\delta)}{\Delta_{\mathbf{a}}^2}\right)$ and the fixed-budget error as $\exp(-\Theta(T/H_1))$, with the dependence on the joint-action count $A^M$ shown to be unavoidable.

---


### 140. [A Lightweight and Post-Quantum Secure Framework for IEC 61869-9 Sampled Value Communication](https://arxiv.org/abs/2608.22123)

**<font color=#1a73e8>作者：</font>** S.M. Suhail Hussain, Arman Ahmad, Mohammad Tayyab 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Securing IEC 61869-9 Sampled Values (SV) is challenging because process-bus communication must satisfy stringent real-time constraints while supporting standardized high-rate publication profiles. This paper presents an experimentally validated security framework that combines lightweight per-frame authentication for operational SV traffic with post-quantum-capable key establishment protocol. For message integrity, the proposed method applies field-selective authentication employing optimized Chaskey-12 to reduce per-packet computational overhead. For trust establishment, the paper introduces an ML-KEM-based pairwise authentication and key-establishment procedure. The pairwise protocol is analyzed in the Quantum Random Oracle Model and is also verified with AVISPA tool under the Dolev-Yao adversarial model. A C-based publisher/subscriber prototype is implemented on a two-node process-bus testbed. Performance is evaluated across the eight IEC 61869-9 SV packet profiles using HMAC-256, AES-GMAC-128, Blake-2s, Chaskey-12, and a compiler-optimized Chaskey-12 implementations. These results indicate that optimized Chaskey-12 achieves ~90% lower latency than HMAC on SV packets. The proposed security framework is a practical and scalable candidate for protecting IEC 61869-9 SV traffic on resource-constrained digital-substation devices.

---


### 141. [Blockwise Stabilized Adaptive Cubic Regularization with Subsolvers via Recurrence](https://arxiv.org/abs/2608.22129)

**<font color=#1a73e8>作者：</font>** Rodion Podorozhny  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cubic-regularized Newton methods have the optimal $\mathcal{O}(\varepsilon^{-3/2})$ global rate and an automatic saddle-escape mechanism, but their subproblem is most often solved by a full eigendecomposition, limiting feasible model size. We introduce a blockwise optimizer that partitions parameters by tensor, minimizes an independent cubic model with an adaptive cubic constant $M_b$ per block, and accepts or rejects each block step against a monotone guard on the full loss. The subproblem solver is chosen by block size: small blocks use lazy exact cubic steps from explicitly formed per-block Hessians; arbitrarily large tensors use a matrix-free Chebyshev-bounded Krylov subspace built by the Lanczos process. The cubic shift bounds the required polynomial degree whenever the gradient-driven shift dominates negative curvature, renders the shifted operator positive semidefinite before any polynomial is applied, and preserves the $\mathcal{O}(\varepsilon^{-3/2})$ rate under inexact subproblem solves. We prove these claims, and the blockwise scheme carries a monotone per-block descent guarantee. Experiments cover FINER INRs (about 199k parameters) and a 91.4M-parameter ViSIR INR, where the blockwise cubic step remains exact in the cubic-model sense on every block, including the 88.5M-parameter decoder tensor (97\% of the model). Run to full convergence on FINER, the ARC-$\varphi_1$ optimizer reaches 133.5 dB PSNR while tuned Adam plateaus at 78.2 dB at the same extended budget; in the roughly 70 minutes Adam takes to reach its peak, ARC-$\varphi_1$ reaches 95.6 dB. A companion report isolates the loss-landscape features responsible for Adam's behavior.

---


### 142. [TRACE: Artifact-Robust Statistical Shape Modeling from Imperfect Surface Scans - A Case Study in Craniosynostosis 3D Photography](https://arxiv.org/abs/2608.22131)

**<font color=#1a73e8>作者：</font>** Sanjay Bhandari, Nawazish Khan, Alzbeta Novotna 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Craniosynostosis severity analysis increasingly relies on statistical shape models (SSMs) to quantify cranial morphology, but most existing workflows depend on computed tomography or heavily curated three-dimensional (3D) photographs. Raw clinical 3D photographs provide a radiation-free and repeatable alternative, yet often contain shoulders, hands, hair, clothing, scanner noise, and incomplete boundaries that corrupt correspondences. We introduce the Template-constrained Robust Artifact-aware Correspondence Estimation (TRACE) framework, an unsupervised method for constructing SSMs directly from artifact-contaminated clinical 3D head photographs. TRACE predicts sparse anatomically corresponding head-surface control points from the raw point cloud, refines them through a coarse-to-fine Surface-Aware Deformation cascade, and uses thin-plate spline warping to deform a clean template mesh into a subject-specific head reconstruction. This template-constrained formulation keeps dense correspondences on clinically relevant head anatomy while suppressing non-head artifacts. The correspondence module is decoupled from the point-cloud encoder, enabling the same deformation pipeline to be paired with different backbones, including PointNet, DGCNN, and Point Transformer V3. Across all backbones, TRACE substantially improves surface sampling, topology preservation, and shape-model quality over prior SSM methods, providing a scalable foundation for photograph-based craniosynostosis shape analysis and a framework that may extend to other artifact-contaminated surface scans when an appropriate clean template is available.

---


### 143. [SSE-Bio: A Structured Self-Evolving Agent with Agentic Retrieval Policy for Multi-Hop Biomedical Reasoning](https://arxiv.org/abs/2608.22132)

**<font color=#1a73e8>作者：</font>** Zhaohan Meng, Zaiqiao Meng, Siwei Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Biomedical multi-hop question answering (QA) requires models to connect evidence across intermediate entities such as diseases, drugs, proteins, and phenotypes. Existing agents typically rely on static retrieval workflows or coarse-grained prompt rewriting, which can lead to instruction drift when reasoning procedures need to be updated. We propose SSE-Bio, a structured self-evolving agent with an agentic retrieval policy for multi-hop biomedical reasoning. Instead of globally rewriting agent instructions, SSE-Bio maintains a structured state, selectively retrieves knowledge triplets and prior templates through a trainable proxy policy, and improves its reasoning memory through fine-grained template editing. To optimise retrieval decisions, we introduce a proxy-training strategy based on group relative policy optimization, where the proxy is improved through decision-contrastive groups over alternative retrieval choices. Experiments on three biomedical multi-hop QA benchmarks show that SSE-Bio consistently outperforms existing baselines, achieving an improvement of 6.56 absolute points over the strongest self-evolving baseline on BioHopR.

---


### 144. [MEMONDEMAND: A Memory Management System for Large-Scale Enterprise Data](https://arxiv.org/abs/2608.22141)

**<font color=#1a73e8>作者：</font>** Xinyuan Song, Bowen Zhu, Hasibul Haque 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise repositories are large, heteroge- neous, and continuously updated, making re- trieval difficult when efficient access, source- faithful evidence, and cross-query adaptation must be supported together. Enterprise mem- ory extends retrieval beyond the model con- text, but existing systems do not jointly address collection-specific hierarchy construction, low- cost routing, detailed evidence loading, and workload-aware memory updates at this scale. We introduce MEMONDEMAND, short for On- Demand Memory, a memory management sys- tem with three coordinated mechanisms: a dy- namic multi-level hierarchy that determines the abstraction structure and depth for each col- lection, dual memory at every hierarchy level that separates distilled routing from detailed evidence, and on-demand memory promotion that updates node priority under a bounded active-state budget. On EnterpriseRAG-Bench, MEMONDEMAND outperforms the strongest published LB#1 result at every evaluated scale from 10M tokens through the complete 618M- token collection, with gains of 12.23% at 10M and 4.66% at 618M. Results on FinanceBench, HotpotQA, and FRAMES further show strong performance across financial, multi-hop, and fact-retrieval settings. Together, these results establish MEMONDEMAND as an accurate, ef- ficient, and scalable memory solution for very large enterprise repositories across data scales, domains, and evidence requirements. Our code is available at this https URL xfab-xinyuansong/MemOnDemand.git.

---


### 145. [Learning Reduced-Order Dynamics with Singularity via Latent-Augmented Neural Ordinary Differential Equations](https://arxiv.org/abs/2608.22142)

**<font color=#1a73e8>作者：</font>** Xiaorui Wang, Yu Zhou, Wenjie Mei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper addresses the issue of self-intersecting trajectories (in phase space) in industrial reduced-order modeling and proposes the Latent-Augmented Neural Ordinary Differential Equations (LA-NODEs) framework. From the perspective of artificial intelligence, the proposed method augments conventional neural ordinary differential equations to enhance model expressiveness, enabling the representation of conflicting vector fields that may arise in reduced-order systems, thereby improving learning accuracy. Through theoretical analysis, the underlying mechanism of the framework is established, and a condition for determining the minimum required augmentation dimension is derived. From the perspective of engineering applications, the effectiveness of the proposed method is validated on the reduced-order system of two representative industrial models, namely an interior permanent magnet synchronous motor (IPMSM) drive and a distributed energy system (DES). Experimental results demonstrate that the proposed method can recover system features that are difficult to capture using conventional approaches and achieve superior performance in terms of prediction accuracy and modeling fidelity, thereby providing an effective approach for high-precision data-driven modeling of complex industrial systems.

---


### 146. [Loss Landscape Features That Make Adam Stall: Definitions, Estimators, and the Preconditioned Hessian View](https://arxiv.org/abs/2608.22145)

**<font color=#1a73e8>作者：</font>** Rodion Podorozhny  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Across implicit-neural-representation (INR) architectures and analytic benchmarks we observe that a thoroughly tuned Adam (especially its learning rate (lr), e.g. in a hyperparameter sweep from $lr = 0.05$ to $10^{-8}$) can potentially reach a very low loss even on ill-conditioned loss landscape or converge at a plateau far above the loss attained by second-order methods. This report defines the measured metrics that help determine if Adam can mitigate the ill-conditioning on a given loss landscape. We provide the indicators by which each outcome is determined, that are: the condition number of the Hessian and of the Adam-preconditioned Hessian $D^{-1/2}HD^{-1/2}$ (with the derivation from Adam's update rule), the diagonal mass $\rho$ that distinguishes axis-aligned from cross-coupled ill-conditioning, the negative spectral mass estimated by stochastic Lanczos quadrature, and the gradient energy fractions over curvature bands, including the flat fraction that indicates the Adam stall. A worked out $2\times 2$ example and an illustration show the reasons why a diagonal preconditioning by Adam can remove axis-aligned ill-conditioning by rescaling and why it cannot do the same if the ill-conditioning is cross coupled. In addition, we present a case study of FINER image fitting architecture that goes over the whole loss landscape analysis framework: the fitting architecture description, reasons due to which its landscape stalls Adam at saddles, the measured PSNR values through our tuned baselines to the $120$--$134$\,dB results of the blockwise second order methods, the error maps behind those numbers, and description of the benefits such image fitting accuracy gives in practice.

---


### 147. [More accurate behavioral predictions with hybrid Bayesian-connectionist models](https://arxiv.org/abs/2608.22154)

**<font color=#1a73e8>作者：</font>** Brenden M. Lake, Akshay K. Jagadish, Guangyuan Jiang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Researchers must often choose between Bayesian or neural network models of behavior, two paradigms with complementary strengths and weaknesses. An ideal paradigm would facilitate testing many kinds of representations and inductive biases; Bayesian models make this easy, while neural networks do not. Similarly, an ideal paradigm would avoid over-simplifications; neural networks make this easy, while Bayesian models do not. Here, we introduce Bayesian distillation with Behavioral Tuning (BBT) as an approach to getting the best of both traditions. BBT offers a simple recipe for model building: first, a neural network is trained to mimic a Bayesian model through synthetic data, and second, the network is fine-tuned on human behavior to capture additional structure and nuance. Across four case studies in human concept learning, we find that BBT outperforms traditional approaches at predicting human behavior while also revealing psychological insights, resulting in models that can both mimic Bayesian priors and capture heuristics and biases that violate simple modeling assumptions.

---


### 148. [Why Does Robustness Reduce Superposition?](https://arxiv.org/abs/2608.22155)

**<font color=#1a73e8>作者：</font>** Adam Elimadi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The study of adversarial examples and their origins remains an open area of research. Mechanistic interpretability, and superposition in particular, offers new avenues for approaching this problem. Gorton & Lewis (2025) demonstrate that adversarial examples arise from superposition and show empirically that adversarial training reduces superposition, yet provide no mechanistic account of why this occurs. We present an empirical explanation inspired by the feature taxonomy of Ilyas et al. (2019), tracing the following chain of causalities: adversarial training abandons non-robust features, leading to fewer total features to represent, resulting in less superposition.

---


### 149. [Aggregation-Aware Synthetic Text Generation Against Authorship Re-Identification](https://arxiv.org/abs/2608.22161)

**<font color=#1a73e8>作者：</font>** Qian Ma, Anna Squicciarini, Sarah Rajtmajer  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Online users often release multiple texts under the same identity, giving attackers an author profile that can reveal more than any single text. Existing authorship obfuscation methods optimize privacy independently for each document, leaving them blind to cross-document correlations that make aggregation dangerous. We propose Aggregation-Aware Synthetic Text Generation (AAST), a framework that addresses this gap by jointly selecting synthetic texts at the bundle level rather than optimizing each text in isolation. AAST targets attribution and verification attacks, including cross-genre settings where attacker references come from a genre not observed during generation or selection. Experiments across same-genre, cross-genre, neural, and independent non-neural stylometric attacks show that AAST lowers account-level linkability as bundle size grows, while preserving semantic quality, linguistic acceptability, and sentiment alignment.

---


### 150. [MARL-Based Sequential RIS Auctions: A Physical-Layer Security Analysis](https://arxiv.org/abs/2608.22169)

**<font color=#1a73e8>作者：</font>** Yuanyu Zhang, Yu Zhang, Jialu He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Reconfigurable intelligent surfaces (RISs) hold great potential to enhance coverage, spectral efficiency, and communication security by intelligently configuring their reflecting elements. When owned by a neutral RIS operator, these elements can be offered as resources for which legitimate receivers and eavesdroppers compete. This paper investigates such competition and evaluates its impact on the physical-layer security performance of legitimate receivers. To model the competition, we develop a sequential RIS auction (SRA) framework, in which a bundle of RIS elements is auctioned in each round through a first-price sealed-bid mechanism, with each bidder submitting its bid based on the achievable rate gain and remaining budget. We then formulate the sequential bidding process as a Markov game by specifying its states, actions, rewards, and state transitions. To solve the game, we propose a multi-bidder deep deterministic policy gradient (MADDPG)-based multi-bidder reinforcement learning (MARL) approach under centralized training and decentralized execution (CTDE), enabling legitimate receivers and eavesdroppers to learn bidding strategies that maximize their long-term economic surplus. Numerical results show that, under the considered eavesdropper bidding strategies, the RL-based strategy enables legitimate receivers to achieve the highest secrecy rate per unit cost, outperforming random and fixed strategies and approaching the ideal physical-layer upper bound.

---


> [!TIP]
> 当前位于：**101-150**（第 3/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-361](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
