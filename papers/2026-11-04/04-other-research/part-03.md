# 📦 其他研究 | 2026年11月04日

> 本类共 **633** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-633](./part-13.md)

---

### 101. [Swap, Replicate, Read the Mass: A Protocol for Auditing Demographic Bias in System One Decision Models](https://arxiv.org/abs/2611.00496)

**<font color=#1a73e8>作者：</font>** Alejandro Mozo Quesada, Sergio Gálvez Rojas, Francisco López Valverde  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> System One decision models replace text generation with typed, probability-scored answers and are entering production. Answers execute without a person in the loop, and no multi-model audit exists on established bias benchmarks. We provide that audit: three benchmarks: BBQ (all eleven categories), CrowS-Pairs, and SilverSpoon, adapted to the typed interface, twelve models plus a no-thinking ablation, and 1,638,000 decisions. Every order-sensitive item runs twice with options swapped; native typed models also swap labels; ten configurations repeat under extra seeds and batch 16. We find widespread stereotype alignment, order-dependent answers, and confidence that tracks instability rather than bias. In BBQ, 97 of 143 model-by-category scores are significant and 94 aligned, while the commercial reference abstains on 99.5% of ambiguous items, hiding aligned probability mass. Option swaps flip 0.0% to 72.6% of choices; typed scoring stays below 10% except Laya (22-33%), and untuned letter prompting reaches 73%. CrowS-Pairs preference spans 0.496 to 0.816, and boolean answers can be decided by position (1.00 versus 0.005). SilverSpoon judgments shift toward lower-SES labels in five of eight decision models, inherited from the 9B backbone or induced by tuning. Audits must permute options and reverse questions by default; order-invariant scoring should become a procurement requirement.

---


### 102. [Where Does EEG Help Wearable Freezing of Gait Detection?](https://arxiv.org/abs/2611.00497)

**<font color=#1a73e8>作者：</font>** Chuntian Chi, Lifang He, Huajie Shao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Freezing of gait (FoG) detectors built on inertial measurement units (IMUs) are accurate while the legs move, but they become unreliable when the legs are nearly still, which is exactly when akinetic freezing, voluntary stopping, and standing must be told apart. Electroencephalography (EEG) captures motor-planning activity that leg sensors cannot, but EEG is impractical for daily use. We ask where EEG helps: as an input at inference time, or only during pretraining, so that the deployed detector still needs only IMUs. We assemble a pretraining corpus of synchronized EEG and IMU recordings (5 datasets, 184 people, 94 hours) and compare six settings that differ only in the modalities used for pretraining and as model input, each with tuned hyperparameters and five independent pretraining runs. On the BXHC FoG dataset (leave-one-patient-out, 10 patients with FoG), adding EEG as input raises FoG F1 from 0.663 to 0.740 (9 of 10 patients improve), and the gain in ranking performance is confined to the quartile of windows with the least leg movement (AUROC +0.063). Pretraining the IMU encoder jointly with EEG improves an IMU-only detector both within the cohort (FoG F1 0.663 to 0.705) and when it is trained on a small cohort and tested on another (FoG F1 +0.083, all 10 test patients improve). Repeating the study with PD-only and healthy-only pretraining corpora, each with its own hyperparameter search, shows that IMU-based detection is robust to the corpus, whereas the benefit of aligning EEG with IMU requires both. Cross-cohort analysis further shows that detectors trained without annotated voluntary stops classify nearly all stops as freezing. Finally, on PD versus non-PD classification in three external datasets, joint EEG+IMU pretraining improves PD detection from walking EEG over EEG-only pretraining (AUROC 0.750 vs. 0.683), while IMU-based detection does not depend on the pretraining.

---


### 103. [Beyond Blackwell: Constrained Data Processing Inequalities](https://arxiv.org/abs/2611.00510)

**<font color=#1a73e8>作者：</font>** Brendan van Rooyen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the comparison of statistical experiments from a decision-theoretic standpoint, working with Markov transitions as basis-free linear maps on dual spaces. Our starting observation is that the data-processing inequality, that adding noise to an experiment cannot lower its Bayes risk, is the functoriality of fibrewise minimisation over a presheaf of decision rules: the rules available after an experiment form a presheaf, garbling acts on it by precomposition, and a risk functional is a natural transformation from it to the ordered reals. The argument refers to neither probabilities nor expected values, and it survives replacing the decision presheaf by a sub-presheaf of admissible rules. Any constraint imposed on the strategy that a rule induces fairness, unbiasedness, is automatically of this form, and so yields a data-processing inequality with no counterpart in the unconstrained Blackwell theory.
Our main result is their quantitative companion. For constraints closed under post-processing we define a constrained deficiency and prove a constrained randomization theorem: one experiment dominates another on every admissible decision problem exactly when the constrained deficiency is small. The classical theorem is the case of no constraint, where the identity is itself an admissible rule; in general it is not, and the constrained deficiency is an optimisation over the coarsenings of an experiment that render it compliant. Specialising to equalized odds, we exhibit a pair of experiments that unconstrained Bayes risk identifies at a given loss and prior but that the constrained risk separates, giving a one-line certificate of Blackwell-incomparability. We work throughout with finite sets.

---


### 104. [Efficient and Scalable Multi-View Masked Autoencoder for Heterogeneous Graph Self-Supervised Learning](https://arxiv.org/abs/2611.00511)

**<font color=#1a73e8>作者：</font>** Hao Geng, Deqing Wang, Lihao Ge 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent years have witnessed the flourishing of self-supervised learning on heterogeneous graphs, e.g., masked autoencoder-based methods. However, existing methods suffer from three issues, including the prohibitive computational cost of constructing meta-path-induced subgraphs, the limitations of uniform random masking, and the suboptimal objective of reconstructing potentially noisy or uninformative original node features. To address these issues, we propose the Multi-View Masked Auto Encoder (MVMAE), a novel, efficient, and scalable framework for heterogeneous graph self-supervised learning. First, MVMAE introduces a novel multi-view mask-then-reconstruct strategy. Instead of masking individual nodes or features, MVMAE randomly masks entire meta-path views and guides the model to reconstruct their representations from remaining visible views. This approach shifts the learning objective to a high-level and semantic task, providing a more robust and informative supervisory signal that is effective even when initial node features are absent or flawed. Then, to handle the computational demands, MVMAE employs an efficient offline aggregation mechanism that pre-computes and reuses representations for each meta-path view, completely avoiding the costly construction of meta-path-induced subgraphs. Next, to fuse the representations of each view, MVMAE uses a Transformer-based multi-view fusion encoder to capture the complex correlations between views, and a deliberately simple MLP decoder to compel the encoder to learn highly expressive and robust node representations. Extensive experiments on six real-world datasets, including three large-scale graphs, demonstrate that MVMAE consistently outperforms state-of-the-art self-supervised and even semi-supervised baselines, confirming its superior effectiveness and scalability. Our source code is released at this https URL.

---


### 105. [Practical Preimages for 19- and 20-Step SHA-256 with Standard Padding](https://arxiv.org/abs/2611.00512)

**<font color=#1a73e8>作者：</font>** Sebastian R. Wain  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present practical preimage attacks on 19- and 20-step SHA-256 that respect the standard IV, Davies-Meyer feed-forward, and full FIPS 180-4 padding, for arbitrary prescribed 256-bit targets. Building on Basra's algebraic selector saturation and backward padding absorption, we introduce three techniques: an exact $O(1)$ inversion of the low padding byte $(W_{13} \bmod 256) = \mathtt{0x80}$ that leaves $(a_5, a_6)$ free for exact context shaping; a causal bit-slice equivalence theorem that prunes $99.74\%$ of right-hand candidate nodes across seven stages; and a closed-form $\mathbf{F}_2$ upper-half inverse paired with compact $Q_0^{-1}$ lookup tables. One CPU core solves arbitrary 19-step padded targets in $1.2$--$86.4$ s (median $19.5$ s) after an $18$ s table build. A 20-step padded preimage costs $2^{46.6}$ CPU-reference evaluations: $191$ node-hours on one 10-core Apple M4 CPU node (16 threads), or $9.0$--$22.2$ GPU-hours on one NVIDIA L4. A companion Zero-$a_3$ bridge inverts the unpadded 20-step compression function in $2^{38.1}$ evaluations. We provide 46 self-verifying witnesses, including 55-byte preimages of SHA-256("abc") and $0^{256}$. These attacks cover 19--20 of 64 steps and do not threaten full SHA-256.

---


### 106. [SASFormer: Stage-Aware Selective Attention Transformer for All-in-One Blind Image Restoration](https://arxiv.org/abs/2611.00523)

**<font color=#1a73e8>作者：</font>** Xiangpeng Tian, Mingyang Li, Fajing Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> All-in-one image restoration aims to recover high-quality images from multiple degradation types using a single unified model. Recent methods improve unified restoration with hybrid attention, prompt learning, or routing mechanisms, but generally focus on enhancing degradation adaptivity while employing similar feature modeling strategies across network stages. Consequently, the distinct representation requirements of encoding and decoding under diverse degradations remain insufficiently explored. In this paper, we propose SASFormer, a Stage-Aware Selective Attention Transformer for all-in-one blind image restoration. SASFormer follows a stage-aware design principle: the encoder uses established hybrid channel-spatial attention to build robust content-preserving and degradation-aware representations, while the decoder employs adaptive selective attention for restoration-oriented reconstruction. To address the stage-specific requirements of decoder reconstruction, we develop Adaptive Selective Channel Self-Attention (ASCSA) and Adaptive Selective Spatial Self-Attention (ASSSA), enabling the decoder to dynamically identify restoration-relevant channel responses and spatial contexts. Specifically, ASCSA performs adaptive query-channel selection and attention masking, while ASSSA adaptively integrates spatial attention across multiple window sizes. Compact implicit prompts further modulate the selection process without requiring explicit degradation labels. Extensive experiments on 3-, 5-, and 11-degradation settings demonstrate that SASFormer achieves strong restoration performance with favorable parameter efficiency. Moreover, stage-wise representation analysis and ablation studies provide empirical support for the proposed stage-aware design and the effectiveness of decoder-side adaptive selection.

---


### 107. [3D Neural Rendering for Automated Ultrasonic Laser Scans](https://arxiv.org/abs/2611.00527)

**<font color=#1a73e8>作者：</font>** Thomas Pierson, Matthew Mitchell, Kira Perna 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Laser doppler vibrometer (LDV) scans can be used to detect defects and cracks in manufactured parts before they are deployed. This work presents a method for reconstructing the steady-state surface wavefield of a three-dimensional part by combining automated robotic manipulation with neural rendering. A six-degree-of-freedom (6-DOF) robotic manipulator (UFactory xArm6) with an embedded piezoelectric transducer presented an acoustically excited test article to a stationary LDV at a sequence of known orientations, yielding a set of complex-valued 2D scans with poses derived analytically from the arm kinematics rather than from image-based pose estimation. These scans were used to train a novel complex-nerfacto model, a modified Neural Radiance Field (NeRF) pipeline that replaces the standard three-channel RGB output head with a two-channel output. Complex-nerfacto represents the real and imaginary velocity components of a wavefield, preserving the complex measurement without quantization. Reconstructions of a welded aluminum cylinder and a welded T-bracket were evaluated against measured scans using Z-normalized cross-correlation (ZNCC). The complex-valued pipeline achieved a mean ZNCC of 0.60 at held-out viewing angles, compared with 0.28 for a baseline RGB nerfacto model trained on rendered images of the same data. The resulting surface wavefield reconstructions supported defect detection and characterization on complex components. We identify geometry reconstruction from sparse LDV scans as the remaining obstacle to practical deployment.

---


### 108. [When Does Spatial Cooperation Help? Contamination Regimes in Decentralized Online Spectrum Anomaly Learning](https://arxiv.org/abs/2611.00532)

**<font color=#1a73e8>作者：</font>** Alp Berke Ardic, Erdem Koyuncu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning-based spectrum monitors adapt online to benign propagation changes, but persistent rogue transmissions can gradually become incorporated into the learned background. Spatially distributed receivers provide additional evidence for detecting such anomalies, while decentralized model mixing can also spread contamination to receivers with clean measurements. We study this tradeoff using a decentralized online learner with sample gating and model sharing. We show that, without defenses, contamination propagation is governed by the occupancy rate and is independent of cross-receiver correlation. In contrast, the benefit of spatial fusion depends strongly on correlation and the detector operating point, so cooperation can either improve or degrade detection. We also show that fragmented transmissions can evade gating based on temporally smoothed statistics. Combining smoothed and per-sample gating substantially improves robustness to such intermittent contamination.

---


### 109. [Governing Equations of Human Sleep Macro-Structure:Symbolic Discovery from 1,106 Nights](https://arxiv.org/abs/2611.00550)

**<font color=#1a73e8>作者：</font>** Junhui Gao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human sleep is organized into a small number of cycles per night: deep sleep dominates early cycles, REM lengthens toward morning, and light sleep clusters at cycle boundaries. These regularities have long been described qualitatively but never distilled into closed-form laws from large-scale data. A total of 1,106 nights (Sleep-EDF 153 + SHHS 953) are segmented into REM-anchored cycles, and four cycle-indexed statistics follow simple closed-form equations: cycle length declines nearly linearly (R^2=0.996), REM duration follows an inverted U (R^2=0.873), deep-sleep (N3) run length decays exponentially (R^2=0.987) with a time constant of 2.94 cycles, consistent with the homeostatic Process S of the two-process model, and light-sleep (N1) run length follows a U shape (R^2=0.956), confirming a "long-short-long" pattern across the night. The laws are reproduced by per-night differentiable fitting (142/142 and 773/773 nights converge), by unconstrained symbolic regression (PySR), and by a 500-night generative synthesizer built from them. Their robustness is established against the two main methodological threats: bootstrap CIs computed by resampling whole nights (1,000 replications) exclude zero for every shape term, and a five-level scan of the REM-merge segmentation threshold preserves every qualitative form. These appear to be the first closed-form laws governing the macro-structure of sleep, distilled and tested across an age-mixed sample (healthy young adults and community-based older adults).

---


### 110. [RATR: Training-Free Material Rebinding via Role Assignment and Temporal Routing](https://arxiv.org/abs/2611.00551)

**<font color=#1a73e8>作者：</font>** Jiehui Tang, Yunlong Yu, Zhao Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Material rebinding aims to transfer the material appearance from a reference image while preserving the target object's geometry and identity. Existing methods typically struggle to balance material fidelity with structural preservation due to the coupled influence of structural and appearance cues in their visual conditions. We identify role entanglement in the target and reference conditions as a contributing factor the target condition carries both geometry and its original appearance while the reference condition contains material cues alongside object-specific structure. To address this issue, we propose RATR, a training-free material rebinding method built on a diffusion-based image editor that assigns complementary roles to the two conditions and coordinates their influence during denoising. To make the target condition primarily convey structure, we introduce an albedo-resolved surface release mechanism, which suppresses the target's original surface appearance while retaining geometric cues, yielding a structure-oriented condition for material transfer. On the reference side, the designed material evidence isolation mechanism emphasizes material cues while reducing interference from object-specific structure, yielding a complementary material-oriented condition.

---


### 111. [Spatial-Spectral Interactive POCS Network for Large-Gap Seismic Data Interpolation](https://arxiv.org/abs/2611.00556)

**<font color=#1a73e8>作者：</font>** Baisong Jiang, Chunxia Zhang, Anxiang Di 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large gaps in seismic acquisition disrupt reflection events and hinder spectral recovery. Existing seismic interpolation deep unfolding networks primarily rely on localized spatial priors, limiting their ability to aggregate the global context necessary for reconstructing these extensive missing regions. We propose a spatial-spectral interactive projection-onto-convex-sets network (SSI-POCS) to tackle this severely ill-posed problem. By unfolding the classical iterative solver, our network integrates physical consistency with dual-domain deep priors via learned transforms, soft thresholding, and exact data reinsertion. Within the learned prior, a spatial Restormer branch captures local waveform structures, while a fast Fourier convolution (FFC) branch extracts global context, effectively suppressing incoherent components and enhancing spectral energy concentration in the $f-k$ domain. A dual-domain fusion module exchanges these complementary features via bidirectional channel attention and gated modulation, yielding substantial interpolation improvements. To overcome the severe loss of lateral continuity caused by large gaps, we introduce structural similarity (SSIM) supervision, complemented by focal frequency loss (FFL) and transform consistency constraints to suppress incoherent high-frequency components and regularize training. Experiments on a synthetic salt dome and a North Sea field dataset under 50% random and consecutive trace removal demonstrate the effectiveness of SSI-POCS. It significantly enhances event continuity across large gaps and mitigates artifacts, achieving a 3.285~dB SNR improvement over the best competing method while reducing parameters by 75.66%.

---


### 112. [Structured Channel Network Pruning with Bi-Sparse Matrix Factorization](https://arxiv.org/abs/2611.00566)

**<font color=#1a73e8>作者：</font>** Jingjing Liu, Ziyang Wang, Xianchao Xiu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Structured channel pruning for convolutional neural networks (CNNs) plays an important role in pattern recognition and deep learning. Nevertheless, existing methods usually calculate channel importance scores based on the magnitudes of individual filters, making it difficult to distinguish shared redundancy from individual channel contributions. To tackle this limitation, we propose a novel structured channel pruning method termed bi-sparse matrix factorization (BSMF). Specifically, BSMF characterizes the convolutional weight matrix as output-channel coefficients over a shared basis with row-wise $\ell_{2,p}$-norm and column-wise $\ell_{2,q}$-norm regularization terms, respectively. Note that $p,q\in[0,1)$, which, to our best knowledge, has not been explored in the literature. To solve the resulting non-convex optimization problem, we develop an efficient update scheme built upon the alternating direction method of multipliers (ADMM), in which all subproblems admit closed-form solutions. After that, a compact CNN is obtained by reconstructing the convolutional filters from the learned factors and discarding the redundant channels. Extensive experiments on the CIFAR-10 and ImageNet-1K datasets demonstrate that our proposed BSMF achieves significant network compression while maintaining high reconstruction accuracy. The source code is publicly available at this https URL

---


### 113. [The First-Order Value of Free Covariates in Budgeted Risk Monitoring](https://arxiv.org/abs/2611.00576)

**<font color=#1a73e8>作者：</font>** Yanze Cao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A deployed model sees its inputs for free, but checking whether its risk has risen requires costly labels. We study how to spend a label budget so that a risk increase is detected quickly while false alarms stay controlled, including under input shifts that keep the risk below a safety threshold $\tau$. Let $A$ be the false-alarm control scale and $h(r)=\mathrm{kl}(r,\tau)$ the Bernoulli KL divergence between the changed risk $r$ and $\tau$. At label rate $b=c/\log A$, we prove that every rule that chooses requests from its own label history has worst-case (Lorden) delay at least $(1/h(r)+1/c)\log A$ to first order: besides collecting evidence, it must wait for its next label. The bound needs only a label budget on one finite stretch of safe source data and false-alarm control over an initial window; a bound on the average time to false alarm does not suffice. When a harmful change also shifts the inputs, a rule that lets the inputs trigger labeling attains delay $\log A/h(r)$ to first order on a fixed Gaussian model, so free covariates save at least $1/b$ rounds. A hybrid rule adds a label-history fallback for risk changes that leave the inputs unchanged. Synthetic experiments and two ACS tasks, with strengthened label-only baselines, show the predicted pattern. The covariate trigger has a cost: because its budget is calibrated on the source, a benign input shift can make it request nearly every label.

---


### 114. [From Apparent Search Gains to Selection Failures: Auditing Test-Time Inference in Structured Workflow Planning](https://arxiv.org/abs/2611.00579)

**<font color=#1a73e8>作者：</font>** Zhitong Chen, Weifeng Zhang, Kai Yin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Test-time search can improve structured planning, but when methods differ in prompts, post-processing, and selection, it is unclear what an observed gain should be attributed to. We study this question on DisasterBench, where models compose typed multi-tool workflows, by decomposing inference into three observable stages: whether a correct workflow is discovered, whether it survives structural validation, and whether it is finally selected. Comparing independent sampling, a nominal tree-search configuration, and multi-operator search under controlled inference budgets on two model families, we find that (i) the nominal tree-search configuration realizes non-adaptive complete-workflow sampling, and independent sampling with its expansion prompt reproduces its candidate discovery without constructing a tree; (ii) structural validation never removes the last correct workflow in our evaluated candidate pools, whereas majority voting leaves a discovered correct workflow unselected on 10-19% of tasks per pool, with an audit confirming substantive tool-choice or information-flow errors in 57 of 60 examined cases; and (iii) a tool-specification-aware verifier recovers some of these losses but overturns more correct decisions than it fixes. Our results motivate auditing realized rather than nominal inference pipelines, and reporting discovery, validity, and selection separately.

---


### 115. [Evolving Scientific Intelligence: From Fragmented Evidence to Distributed Experimental Loops](https://arxiv.org/abs/2611.00580)

**<font color=#1a73e8>作者：</font>** Yuheng Ding  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific discovery advances when evidence from different investigations is brought into contact. Yet paper-centric communication leaves experimental results fragmented, delayed, or unreported, creating a "scientific memory wall" between growing computational capabilities and the evidence accessible to AI systems. We envision a different dynamic: in a network of intelligent laboratories, a failed or overlooked experiment in one domain could trigger a hypothesis in another, whose testing generates evidence that stimulates further investigations. Such chains of information collision and empirical validation could transform isolated discovery loops into a cumulative scientific process. We propose Evolving Scientific Intelligence (ESI), an architectural blueprint for enabling these evidence-driven chain reactions. ESI preserves experimental records in shared, computable scientific memory, where evidence from different domains can be recombined into testable hypotheses. It jointly selects candidates and evaluation methods according to scientific value, reliability, and cost, then coordinates physical tests across distributed experimental nodes. Their feedback revises hypotheses and evaluators, while slower meta-control reassesses research objectives and decision criteria to guard against self-reinforcing errors and misguided optimization. We call for an Information Manhattan Project to build the infrastructure for scientific intelligence that evolves through experimentally grounded chains of discovery.

---


### 116. [Price is Only the Symptom: Understanding and Analyzing Economic-State Manipulation Vulnerabilities in DeFi](https://arxiv.org/abs/2611.00587)

**<font color=#1a73e8>作者：</font>** Hao Wu, Haijun Wang, Xiapu Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Economic-state manipulation has emerged as a significant security threat to decentralized finance (DeFi), causing substantial financial losses. Existing studies predominantly characterize these attacks as price manipulation, focusing on observable price distortions while overlooking underlying violations of economic-state integrity. We conduct a comprehensive empirical study of Economic-State Manipulation (ESM) vulnerabilities in DeFi. We first curate a diverse dataset comprising 276 real-world attacks and 91 Code4rena audit findings. Based on these cases, we develop a cause-oriented taxonomy comprising four primary categories and eleven subcategories. Our analysis reveals that ESM vulnerabilities extend beyond conventional price manipulation, frequently involving violations of protocol-internal accounting, AMM state consistency, and execution-time constraints. We further investigate the evaluation datasets of six existing studies and find that, although they cover 6-10 vulnerability subcategories, their distributions remain dominated by limited manipulation mechanisms. Furthermore, we systematically evaluate seven representative detection approaches on our dataset. Our results reveal limited coverage, with the best-performing approach identifying only 50.4% of real-world attacks. Through an analysis of false negatives and false positives, we identify fundamental limitations arising from reliance on predefined attack patterns, insufficient reasoning about economic-state semantics, and incomplete exploitability validation. These findings provide empirical insights for developing more generalizable ESM vulnerability detection techniques.

---


### 117. [Guarded Compression of Adam Optimizer State with Shared-Gradient Bounds](https://arxiv.org/abs/2611.00589)

**<font color=#1a73e8>作者：</font>** Annan Zhang, Shengjie Song, Wenshuai Yao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adam keeps two FP32 moments per parameter, twice the bytes of the FP32 weights, yet compressing them is risky: the update divides by the square root of the second moment, so small reconstruction errors can change the restored computation substantially. We study guarded moment compression, in which a coordinate's decoded moments are accepted only if they reproduce the native FP32 Adam update to within a tolerance $\tau$, in units of the learning rate, for every gradient in a clipped domain; all other coordinates are stored exactly. The natural certificate, which ranges each update separately over gradient intervals, fails: on one million trained OPT-125M coordinates it escapes 98.9% of coordinates and the payload grows to 126.6% of raw FP32. Our key observation is that both updates consume the same gradient and parameter. Bounding their difference directly, with FP32 rounding-error allowances and a fixed mixed linear-logarithmic gradient partition, cuts escapes to 0.53% and the payload to 28.3% at $\tau=0.01$. Across 120 complete-checkpoint restores of OPT-125M and ResNet-18, with four trained seeds and three training fractions per model, guarded 8-bit log codes shrink moment payloads by 69.5% and 71.9% relative to FP32, 40.8% and 45.4% relative to equally guarded BF16, and 29.3% and 37.6% relative to equally guarded blockwise 8-bit, and every restored first update stays within tolerance. Encoding and restoration together take 2.3-2.6$\times$ as long as guarded BF16 but less time than guarded blockwise 8-bit. Searching both moment codes jointly saves under 0.001% more bytes at 6% more codec time, so per-moment rounding suffices. The guarantee covers the first restored update under a pinned Torch operation model; we measure subsequent training empirically.

---


### 118. [State-Aware Activation Recomputation with Replay Contracts and Selective Preservation](https://arxiv.org/abs/2611.00590)

**<font color=#1a73e8>作者：</font>** Annan Zhang, Shengjie Song, Wenshuai Yao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Activation recomputation saves accelerator memory by replaying forward segments during the backward pass, but replay is only correct if it sees the state the original forward pass saw. Mutable buffers, aliased bytes and random-generator state can change in between, so re-executing unchanged code can differentiate a different computation. We make this state explicit. A versioned replay contract specifies what replay must restore, and a joint planner chooses, per segment, between activation retention, whole-buffer snapshots and selective-region preservation, charging each option its measured memory and recovery cost. Independent derivative and byte-level checks validate the contract, and a Torch/JAX cohort retains all 5,900 execution records, including matches, rejections and divergences. On frozen sparse-write H100 workloads, each measured over fifty fresh processes, joint planning reduces paired step time by 18.16% against a correctly costed eager/whole planner at a 44 GiB budget (approximate 97.5% ratio interval $[.8172,.8195]$). At 32 GiB, where the eager/whole planner has no feasible static policy, joint planning is 4.98% faster than fixed regions at 29.94 rather than 26.20 GiB. A complete CIFAR-100 dense-queue application runs seven methods for 100 encoder and 25 probe epochs at six training seeds, with byte-identical test scores within each seed. There, joint planning uses 22.41% more allocated memory than whole snapshots, with a process-time geometric-mean ratio of 1.0080 (seed range $[.9845,1.0191]$). Together, the results map where selective preservation pays off: sparse writes with large activations benefit, while in the dense-queue workload whole snapshots use less allocated memory.

---


### 119. [Beyond Sensitive APIs: Detecting Access Control Flaws at Sensitive Callsites in Android Firmware](https://arxiv.org/abs/2611.00594)

**<font color=#1a73e8>作者：</font>** Haotian Deng, Meng Hao, Hanxiao Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Existing studies of vulnerable pre-installed Android apps identify dangerous behavior by checking whether an app invokes an API from a predefined set of security-sensitive APIs. These sets usually exclude generic APIs to avoid false positives; unfortunately, this misses a class of vulnerabilities in which a generic API, such as a database read, appears benign in general but becomes security-sensitive when operating on protected data, yet is left without sufficient access control. While this class of vulnerabilities appears addressable via access control analysis, existing studies focus only on the presence of checks, not on whether those checks enforce sufficient protection for the operation at a given callsite. In this work, we propose Callix, which first assesses callsite sensitivity by jointly analyzing the invoked API functionality and the data involved in the operation, then recovers each security check on the execution path as an explicit security property, and finally introduces the notion of restriction context to decide whether these checks are sufficient for the identified sensitive operation. We evaluated Callix on 1,750 distinct pre-installed apps from the 10 top-tier Android vendors as of 2025. In total, Callix discovered 819 vulnerable paths across these vendors, 42.1% of which allow reading or modifying private user data through generic database operations. Manual validation of a random 60% sample shows a precision of 95.1%. Many of our findings have been confirmed and rewarded through vendor bug bounty programs.

---


### 120. [X-World 1.6: Building Controllable Virtual Cities with World Models](https://arxiv.org/abs/2611.00596)

**<font color=#1a73e8>作者：</font>** XPeng, Boyang Wang, Boyi Sun 等 35 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deploying generative world models for end-to-end closed-loop evaluation and policy learning requires precise scenario control, consistent observations, and sustained generation quality during extended interactions. This report presents \emph{X-World~1.6}, advancing X-World~1.0 toward a more reliable and versatile driving simulator. The upgraded base model offers finer-grained control over traffic semantics, including traffic lights and road markings, together with improved spatial consistency across cameras. Virtual City capabilities broaden scenario construction through a family of models conditioned on diverse 2D and 3D references, including support for generating multi-camera future videos from a single image. An enhanced post-training framework enables efficient causal, few-step generation with stronger temporal coherence, better quality retention over longer rollouts, and improved alignment with human preferences. We also introduce a dedicated evaluation suite to support systematic assessment and guide model iteration. Together, these upgrades expand the scenarios X-World can simulate and improve the efficiency and reliability of its generated observations, supporting broader use in autonomous-driving development.

---


### 121. [Editing the Goal: Per-Token SAE Steering and Its Depth Limits in $π_{0.5}$](https://arxiv.org/abs/2611.00602)

**<font color=#1a73e8>作者：</font>** Rocio Perales Valdes, Animesh Garg  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) have recovered interpretable, causally relevant features in robot foundation models (RFMs) such as $\pi_{0.5}$ (arXiv:2603.19183, arXiv:2603.19233). SAE features on individual instruction tokens are less interpretable than timestep-pooled ones (arXiv:2603.19183), and whether they can redirect a robot's goal remains untested. We show that replacing the SAE features of a single goal word with those of an alternative goal word, leaving the instruction text unchanged, steers $\pi_{0.5}$-LIBERO into completing the alternative task. At layer 0, BatchTopK feature swaps redirect behavior in up to 20/20 rollouts in a scene where random-feature swaps redirect none, with success varying across six scenes in two LIBERO suites and across layers. The effect depends on SAE architecture: word-selected Matryoshka edits largely do not outperform random ones. SAEs are also not required. Adding a fixed difference-in-means vector at twice its natural magnitude redirects 8-10/10 rollouts. Layer-wise activation patching shows that goal-word edits remain effective up to layer 6 for object location and layer 2 for object identity, and up to layer 13 in both cases when patching also covers camera tokens. These results are proof of existence in an RFM in simulation and an initial map of how deep goal-redirecting edits remain effective. Visit this https URL for video rollouts.

---


### 122. [Sparse Autoencoder Attribution Graphs Are Decided at the Margin](https://arxiv.org/abs/2611.00606)

**<font color=#1a73e8>作者：</font>** Karl Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Attribution graphs over the features of sparse autoencoders (SAEs) are used to predict what an ablation does and are compared across training seeds. A TopK SAE keeps the largest preactivations at each token, and a feature's margin is its preactivation's distance to the cutoff. On five public TopK SAE pairs from three Pythia models, zeroing one feature moves a next layer feature across the cutoff in 0.74 of cases or more, and the crossings carry most of the response's energy. Over writes that scale a feature's code by three factors, the graph built on the features active beforehand has a median relative error of 0.247 or more. The margin graph adds the first order change to every preactivation and reranks, at the same cost, and errs by at most 0.033. At the median, the crossing features' decoded change is 1.24 times the model's own change in norm or more. Between seeds of one testbed, sparse maps between features explain 0.85 of a graph's energy on its active features, and 0.47 once the other seed's graph keeps only its own. The largest model studied is pythia-160m.

---


### 123. [ECG2Gene: Deep Learning-Based Germline Tumor Susceptibility Gene Risk Assessment Using Electrocardiograms](https://arxiv.org/abs/2611.00614)

**<font color=#1a73e8>作者：</font>** Shanwei Zhang, Qinghao Zhao, Yize Zhao 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electrocardiograms (ECGs) may contain physiological information related to hereditary cancer susceptibility, but its relationship with future cancer risk remains unclear. Here, we present ECG2Gene, a two-stage deep-learning framework that derives digital phenotypes related to germline tumor susceptibility from routine 12-lead ECGs and predicts future cancer risk. In Stage 1, carrier status for pathogenic or likely pathogenic variants in ATM, BRIP1, CHEK2, PALB2, BRCA1, and BRCA2 supervises a multitask model that generates six continuous ECG-derived gene scores. In Stage 2, XGBoost integrates these scores with clinical variables to predict subsequent breast and ovarian cancer in women and prostate cancer in men. We also introduce ECG-Wide Association Analysis (EWAS) to characterize associations between ECG-derived gene scores and ECG waveforms. Across the clinical feature combinations evaluated in UK Biobank, the best-performing sex-specific models achieve AUROCs of 0.683, 0.633, and 0.660 for breast, ovarian, and prostate cancer, respectively. In external evaluations, models combining ECG-derived gene scores with age achieve prostate cancer AUROCs of 0.709 and 0.579 among men in the overall China Kadoorie Biobank and MIMIC-IV-ECG cohorts, respectively. ECG2Gene links genetically supervised ECG phenotyping and waveform association analysis to future cancer outcomes, demonstrating the potential of routine ECGs combined with clinical information for non-invasive, opportunistic cancer risk assessment.

---


### 124. [LM6-CastBench: A Geometry-Aware Simulation Dataset for Transient Thermal Prediction in LM6 Sand Casting](https://arxiv.org/abs/2611.00619)

**<font color=#1a73e8>作者：</font>** Suhani Kolhatkar, Anand Khandekar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Transient thermal fields during solidification connect casting process conditions and cooling behaviour to the formation of defect-prone regions in aluminum cast ings. Repeatedly solving this thermal problem across geometries and process conditions is computationally expensive, motivating data-driven surrogate models. However, existing machine-learning studies on casting thermal behaviour rely on study-specific simulation databases that do not support reproducible geometry-level benchmarking. We introduce LM6-CastBench, an open simulation dataset for geometry-aware learning of transient thermal fields in LM6 aluminum sand casting, combining three geometry families, ten variants per family, five pouring tempera tures, and three mould temperatures (450 geometry-process cases in total). Each case retains CAD geometry, unstructured mesh connectivity, spatial descriptors, process metadata, and time-resolved nodal temperatures. We benchmark a point wise MLP against a spatially structured U-Net under geometry-level data splits; the U-Net reduces temperature-field errors by a large margin, with the biggest gains on geometries with localized features and abrupt section changes. LM6-CastBench gives researchers a reproducible dataset and benchmark for geometry-aware surro gate modelling of casting thermal behaviour.

---


### 125. [XLA from the Trenches: Correctness on TPU Workloads at Scale](https://arxiv.org/abs/2611.00624)

**<font color=#1a73e8>作者：</font>** Ignacio Cano, Amir Saadat, Rishipal Singh Bhatia 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accelerating modern foundational models has pushed domain-specific compilers toward increasingly complex, multi-tiered optimization pipelines. However, this heavy optimization focus introduces delicate tradeoffs between peak execution performance and correctness. Subtle codegen defects can trigger numerical degradation and memory or buffer corruption, invalidating multi-million-dollar training runs and degrading live serving quality without raising obvious compiler errors. In this paper, we present a battle-tested methodology for verifying and triaging Google's XLA:TPU compiler at hyperscale. We leverage fuzzing techniques, combining synthetic program generation with real production traces, while orchestrating AI agent swarms to autonomously generate stress tests, reproduce failures, and draft fixes. To pinpoint root causes in full workloads, we pair this with a hierarchical differential pipeline that bisects large graphs down to individual failing operations inside fused kernels. Deployed in production, our framework has already driven the resolution of over 142 compiler bugs (with 103 additional findings under review), from which we distill pragmatic lessons learned.

---


### 126. [Autonomous Analysis of Thermoelectric Materials Big Data by Multi-Agentic AI and Construction of a Knowledge Base and Specialized AI](https://arxiv.org/abs/2611.00627)

**<font color=#1a73e8>作者：</font>** Yusuke Hashimoto, Takaaki Tomai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Extracting knowledge from large databases of experimental materials data requires repeated analyses and reusable records of their choices and results. We developed Multi-Agentic AI (MAA), a multi-agent system in which AI agents with distinct roles analyze experimental thermoelectric data under predefined instructions and quality checks, saving analysis records traceable to their sources. In four experiments varying theme and cycle counts, we measured what accumulated in these records. In the largest experiment (100 analyses across 10 themes and 10 cycles), concept co-occurrences were concentrated within themes, vocabulary was shared across themes and some relation descriptions were first detected in later cycles. A specialized AI that searches this experiment's knowledge bases and reads their analysis records answered materials questions with cited sources. Retrospective checks, including tracing an answer generated with a preliminary corpus back to the source data, exposed errors: traceability makes errors findable but not absent.

---


### 127. [Structural Dual Adaptation for Safe Reinforcement Learning](https://arxiv.org/abs/2611.00636)

**<font color=#1a73e8>作者：</font>** Runsheng Yu, Zhuoyang Song, Zengde Deng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Primal-dual methods enforce safety constraints in reinforcement learning through Lagrangian relaxation. For a fixed policy, the exact bounded multiplier response exhibits bang-bang switching at the constraint boundary. Practical gradient updates can oscillate through coupling with policy optimization. We propose Structural DuaL Adaptation (SDLA), which replaces this bang-bang response with a unique continuous response through current-cost centering, trajectory weighting, and quadratic regularization. We characterize activation thresholds and response sensitivity. Ternary search computes multipliers without a dual gradient stepsize. For entropy-regularized tabular policies, we bound equilibrium constraint violations alongside reward gaps. We establish convergence of delayed updates under mild assumptions. Neural PPO/SAC experiments on OmniSafe and HASARD demonstrate competitive rewards with improved constraint tracking. On HASARD, PPO-SDLA achieves higher reported mean reward than the human baseline in six of eighteen settings while meeting the respective mean-cost budgets, including four with lower mean cost. To the best of our knowledge, this is the first report of higher mean reward at lower mean cost than the human baseline across multiple HASARD settings.

---


### 128. [FastAgent: A Physics-Aware FastFluent-to-Fluent Workflow for Rapid CFD Screening and Industrial Steam Dewaxing Design](https://arxiv.org/abs/2611.00645)

**<font color=#1a73e8>作者：</font>** Chen YanKai, Yu QiuHeng, Yuan Man 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Industrial computational fluid dynamics (CFD) becomes costly when complex geometries, long transients and coupled physics must be evaluated across large design spaces. We introduce FastAgent, a physics-aware campaign controller built around FastFluent, a lightweight numerical engine for rapid physical screening. FastFluent supplies stage-specific fields and diagnostics; FastAgent allocates physical models, numerical resolution and simulation horizons by the active quantities of interest (QoIs), while returned Fluent discrepancies update subsequent decisions. Across six public CFD benchmark campaigns, the framework reduces normalised worst-QoI error by 5.68-99.14% and accelerates decision-relevant computation by factors of 1.53-15.36 relative to a matched Generic Agent control. Applied to high-pressure steam dewaxing in investment casting, FastAgent identifies nonuniform condensation heating as the dominant startup mechanism and separates rapid risk-window localisation from high-fidelity melt-completion confirmation. The rapid route requires 81.39% fewer cell-time updates than a fine-grid, small-time-step reference. Structural analysis localises fracture at the observed blade edge. Screening 131,072 outlet layouts and selectively evaluating candidates with Fluent and Abaqus identifies Sparse-6, which reduces simulated crack opening by 96.0% and connected crack extent by 66.7% relative to the Original design. These results demonstrate how rapid numerical evidence and adaptive fidelity control connect large CFD search spaces to mechanism-guided industrial design.

---


### 129. [Regularized Wasserstein Distance for Discrete Generative Modeling and Clustering Analysis](https://arxiv.org/abs/2611.00653)

**<font color=#1a73e8>作者：</font>** Senmao Ye, Fei Liu, Dawei Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we formulate clustering analysis as discrete generative modeling. Specifically, when the generator is restricted to a finite candidate space, the generated samples naturally emerge as the most representative prototypes of the underlying data distribution. To model such a discrete candidate space, we employ a Discrete Distribution Network (DDN). However, DDN suffers from unstable training due to its hard nearest-neighbor selection. To stabilize training and encourage geometric consistency, we replace DDN's l2 loss between images with regularized Wasserstein distance between the empirical distributions of real and generated images. The resulting framework, termed Discrete Generative Clustering (DGC), offers four notable advantages: 1) the learned cluster centers are directly interpretable, as they are realistic synthetic samples; 2) the inference cost scales logarithmically with the number of clusters, i.e., O(log K), making the method scalable to extremely large K; 3) the regularized Wasserstein distance provides a smooth and well-behaved optimization objective that facilitates stable convergence, whereas DDN's l2 loss tends to converge to poor local optima; and 4) DGC replaces DDN's nearest-neighbor selection with random-neighbor selection, which avoids the density shift problem during multi-step forward. Extensive experiments on several benchmarks demonstrate the effectiveness and desirable properties of DGC. The code is publicly available at GitHub.

---


### 130. [SE-Mem: Semantic-Episodic Memory for Scene-Consistent Generative View Synthesis](https://arxiv.org/abs/2611.00658)

**<font color=#1a73e8>作者：</font>** Changsong Lei, Yihan Li, Yu-Hui Wen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative view synthesis aims to synthesize novel-view videos from reference observations along user-defined camera trajectories. Maintaining global scene consistency throughout this process remains challenging for camera-conditioned interactive video generators. Existing approaches typically select reference frames based solely on camera poses, overlooking whether the content remains semantically relevant or even visible. To address these limitations, we draw inspiration from semantic and episodic memory in human cognition, in which semantic memory captures generalized knowledge across experiences, whereas episodic memory preserves information tied to specific past events and contexts. Motivated by the complementary roles of semantic and episodic memory, we introduce SE-Mem, a Semantic-Episodic Memory framework that organizes historical observations in a structured 3D representation and augments its elements with semantic importance scores. A two-stage memory retrieval strategy is designed to identify the most informative frames to provide contextual guidance. Taking into account both semantic significance and geometric visibility, SE-Mem preserves semantic coherence and fine-grained visual details during novel view synthesis. Extensive evaluations show that our approach improves visual quality and achieves competitive geometric consistency across multiple benchmarks.

---


### 131. [From White Canes to Edge AI: A Survey of Assistive Navigation Technologies for Blind and Low-Vision Individuals](https://arxiv.org/abs/2611.00671)

**<font color=#1a73e8>作者：</font>** Abtin Zandi, Arian Ashrafi, Sarvin Nami 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Independent mobility is a foundational requirement for the autonomy of blind and low-vision (BLV) individuals, yet the assistive technologies that support it have historically evolved slowly. This survey systematically reviews 108 peer-reviewed studies published between 2008 and 2026, organizing the field into four technological eras: (i) a foundational era of passive mechanical aids, namely the white cane and the guide dog; (ii) a hardware era of electronic travel aids built on ultrasonic, infrared, and satellite positioning sensors that alert users to proximity but lack semantic understanding; (iii) a deep learning era in which convolutional and transformer-based detectors introduced context-aware scene understanding, initially tethered to cloud infrastructure; and (iv) a contemporary edge-native era defined by model compression, quantization, hardware acceleration, and multi-sensor fusion that relocate intelligence onto resource-constrained wearable and mobile devices. For each era we analyze representative systems, sensing modalities, computational architectures, and reported performance, and we consolidate the field's model-optimization techniques into a single technical reference spanning four detector families and twelve compression strategies. Across the corpus, we find a persistent mismatch between rapid algorithmic progress and slow real-world adoption, driven by cognitive overload in user interfaces, fragmented evaluation protocols, and the scarcity of studies involving BLV participants. We conclude with open challenges, including seamless indoor-outdoor transition, standardized benchmarks, privacy-preserving perception, and the emerging role of multimodal foundation models, and outline a roadmap for socially acceptable, user-centered assistive navigation.

---


### 132. [Smooth bounding box for object detection](https://arxiv.org/abs/2611.00676)

**<font color=#1a73e8>作者：</font>** Chao Zhou, Shenghua He, Fengchuang Xing 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning-based object detection models are highly dependent on the quality of annotated training data. However, large-scale datasets often contain inevitable label noise, with bounding box localization errors being a prevalent and impactful form in object detection. While label noise handling techniques are well-studied for image classification, their adaptation to the more complex problem of bounding box errors remains underexplored. To address this, we propose a novel Smooth Bounding Box (SBB) strategy to mitigate the adverse effects of bounding box annotation inaccuracies. Our key insight is that annotation errors are often linked to annotator factors rather than specific image content, allowing for a statistical correction approach. Based on object size distribution within datasets, we implement the SBB strategy through two methods: 1) Global Scaling Correction (GSC), which applies a uniform scaling factor to estimate and correct a global average error; and 2) Interval Scaling Correction (ISC), which categorizes objects by size into intervals and estimates a dedicated correction factor for each, enabling more precise, fine-grained calibration. For efficient optimization of multiple parameters in ISC, we design a tailored model fine-tuning strategy. Furthermore, we introduce a Normalized Residual Fluctuation (NRF) metric to quantitatively assess the smoothing effect and training stability. Extensive experiments on multiple benchmarks demonstrate that our method consistently enhances detection accuracy across various model architectures. Both GSC and ISC achieve significant performance improvements over strong baselines, including the latest YOLOv11n, without adding inference overhead. The codes are available at this https URL.

---


### 133. [ROD-Dataset: A Pedestrian-Perspective Benchmark of Urban Obstacle Classes for YOLO-Based Detection](https://arxiv.org/abs/2611.00681)

**<font color=#1a73e8>作者：</font>** Abtin Zandi, Ariyan Azami, Bardia Sabagh Kermani 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Two groups of pedestrians face avoidable risk on the city sidewalk: people living with visual impairment, who reach an obstacle before anything warns them, and people walking with divided attention, who register a hazard late or not at all. A vision system can warn them only about obstacles it has learned to recognize, so its training data limits the protection it offers. No suitable training set exists: public benchmarks are recorded from vehicles, aerial platforms, or fixed rigs, general-purpose detectors omit the street furniture that causes trips, and pedestrian-focused collections are confined to single regions with incompatible class schemes. This paper introduces the Real-time Obstacle Detection (ROD) dataset: more than 24,000 images and 40,000 annotated obstacles across 25 classes, from vehicles and people to the stairs, manholes, traffic cones, and benches that general-purpose detectors overlook. Because street furniture differs between cities, ROD unifies twenty-nine public collections onto one taxonomy and adds eye-level imagery from two contrasting cities on two continents, Tehran and Toronto. Every label is human-verified, and each capture campaign is admitted only after a compact detector shows it can learn the class. Six lightweight YOLO detectors (nano and tiny variants) benchmarked on ROD all exceed 0.86 recall; YOLO12n attains the highest recall (0.889), YOLO26n the highest precision (0.925), and YOLOv9t the best mAP@0.50 (0.882) with the fewest parameters. Because the recall and mAP rankings disagree, selecting a model by mAP does not minimize missed obstacles, so per-class recall is reported for all 25 classes.

---


### 134. [Content-Preserving Principal Feature Blending for Training-Free Style Personalization](https://arxiv.org/abs/2611.00683)

**<font color=#1a73e8>作者：</font>** Le-Hoang Bui, Hoang-Nguyen Cao, Trung-Nghia Le 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reference-based style personalization should reproduce the appearance of a style reference while preserving the subject specified by a content prompt. In visual autoregressive models, dominant reference features can also carry object and spatial information, causing content leakage. We propose Content-Preserving Principal Feature Blending (CoPFB), a training-free method that estimates a low-rank content basis from a clean generation branch and removes the content-aligned component of the style residual. CoPFB applies rank-one blending at the first two autoregressive scales, followed by weaker content-projected refinement at the next three scales. On 1,900 combinations of Parti content prompts and FineStyle reference images, CoPFB improves text alignment from 0.293 to 0.297 and the harmonic score from 0.391 to 0.393 over PFB+SAC, while style similarity decreases from 0.590 to 0.577. CoPFB requires no fine-tuning or learnable parameters. Project page: this https URL.

---


### 135. [Generative Forecasting from Coarse-Grained Observations: When Does Cascading Help?](https://arxiv.org/abs/2611.00686)

**<font color=#1a73e8>作者：</font>** Alexandra Spitzer, Giovanni Abati, Lorenzo Baldassari 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study probabilistic forecasting of dynamical systems such as fluids and waves from coarse observations. Since the unseen fine scales influence the dynamics, the same coarse initial state can evolve into a whole distribution of futures. Generative forecasters may produce visually plausible samples, but it is hard to tell whether they sample the right conditional distribution, since trajectory data contain a single future for each initial state. We address this problem by generating reference data in a hierarchical way: for each coarse initial state, we generate many different fine-scale components and numerically evolve the full states. Using these conditional ensembles, we show that standard diffusion models and stochastic interpolants make substantial distributional errors. We then show that cascading shorter forecasts greatly reduces these errors for the turbulent flows and waves we study, but we also find and characterize cases in which it hurts. Since the coarse process is not Markov, cascading discards information about the unresolved fine scales even with exact transitions. To understand this, we propose a solvable analytic model which shows that the optimal cascade depth decreases as the coupling between the unresolved and observed scales gets stronger, and increases as the dependence of the forecast on the observation becomes more oscillatory. Consistent with our experiments, cascading is detrimental when the direct forecast is ``easy'' to learn, for example Gaussian as in the passive scalar case. We release our datasets as a first benchmark for probabilistic forecasting with ground-truth conditional ensembles.

---


### 136. [Shaped by What's Missing: Topological Invariance Simplification Discovers Behavioral Transitions](https://arxiv.org/abs/2611.00688)

**<font color=#1a73e8>作者：</font>** Kaiwen Bian, Eric J. Leonardis, Yuanjia Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding how animals move between behaviors is a central question in neuroethology, yet most segmentation methods first partition time into discrete states, leaving transitions as the unmodeled residue between them. We take the opposite view: in a suitable feature space, sustained behaviors are dense regions of the trajectory's density landscape, and transitions are the sparse corridors and loops that connect them. Because this structure is a property of the landscape's shape rather than of any particular coordinates, it can be read off directly with topology and should persist across feature spaces. We build this landscape from frame-by-frame trajectories, extract its discrete-Morse graph, and keep two kinds of structure: paths, the corridors a trajectory follows between dense behavioral regions, and cycles, closed routes whose entry and exit take different ways. Clustering these structures yields transitions directly, with no upstream state partition. On a rat behavior dataset across three feature spaces, including the latent space of a neural-network controller that imitates the animal in a physics simulator, the approach recovers transitions at coverage comparable to state-space and topological-clustering baselines, while carrying substantially more information about the transition identity, forming clusters at least as tight as the baselines', and matching annotated transitions with less reliance on time-warping. More broadly, the results show that behavioral transitions are a topological feature of a representation: recoverable from the shape of its trajectories, and consistent across distinct feature spaces.

---


### 137. [LoD-Loc v4: Towards Generalized Aerial Visual Localization via Panoptic LoD 3D Map Registration](https://arxiv.org/abs/2611.00704)

**<font color=#1a73e8>作者：</font>** Shuaibang Peng, Chengming Zhang, Juelin Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aerial visual localization over Level-of-Detail (LoD) 3D Maps has recently gained significant traction due to its global scalability, storage efficiency, and privacy-preserving nature. However, existing methods rely almost exclusively on building elements, which leads to catastrophic localization failures in rural or undeveloped areas where buildings are sparse or non-existent. To address this, we construct a unified Panoptic LoD 3D Map by fusing OpenStreetMap (OSM), Digital Elevation Models (DEM), and LoD assets, reformulating the problem as a panoptic registration task. By parsing the query image into discrete building `thing' instances and continuous `stuff' regions comprising road, vegetation, and water, we establish a holistic alignment with this map to robustly optimize the camera pose. To enable reliable panoptic perception, we develop a new automated pipeline that constructs AirPan - the largest aerial panoptic segmentation dataset to date, comprising 85k images with pixel-accurate annotations. This empowers our panoptic segmentation model to exhibit remarkable zero-shot generalization capabilities. Extensive experiments demonstrate that LoD-Loc v4 consistently outperforms state-of-the-art (SOTA) baselines by a significant margin. Most notably, it successfully maintains reliable localization in building-less scenarios, completely overcoming the catastrophic failures of prior building-centric paradigms.

---


### 138. [Personalized Rollout Allocation for Federated LQR Policy Optimization under Heterogeneous Process Noise](https://arxiv.org/abs/2611.00712)

**<font color=#1a73e8>作者：</font>** Mohammadreza Rostami, Shahriar Talebi, Solmaz S. Kia  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We study federated model-free learning of a common linear quadratic regulator (LQR) gain under a limited uplink communication budget, with clients that share dynamics and costs but experience different process-noise levels. Conventionally, clients transmit gradient matrices whose dimension equals the number of controller parameters. Exploiting the structure of two-point zeroth-order estimates, we consider an implementation in which clients transmit only one scalar cost-difference coefficient per rollout pair, while the server regenerates the associated perturbation directions from shared seeds. Communication thus scales with the number of rollout pairs rather than the controller dimension, turning the uplink budget into a rollout budget. Because noise heterogeneity produces gradient estimates of widely differing variance and every client carries equal weight in the fleet objective, uniform rollout allocation allows noisy clients to dominate the aggregated update and increases the probability of destabilizing updates. We propose a rollout-allocation scheme that assigns rollout pairs in proportion to the standard deviation of each client's estimates and show that it minimizes the variance of the aggregated update. The scheme is implemented exactly through a greedy integer allocation rule whose weights are estimated from the communicated scalars. We further prove that a single allocation factor quantifies its improvement over uniform allocation in a one-round instability bound, the certified step size, and the error floor of a joint stability and convergence guarantee. Simulations show that, under the same communication budget, personalized allocation reduces the one-step instability rate from $37\%$ to $0.3\%$.

---


### 139. [Adversarial Robustness Is Not Zero-Day Generalization: A Controlled Evaluation of Flow-Based Intrusion Detectors on Corrected CIC-IDS2017](https://arxiv.org/abs/2611.00713)

**<font color=#1a73e8>作者：</font>** Abdulhamid Zaro  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Synthetic variants of known attacks, including feature-space adversarial perturbations, are sometimes used as stand-ins for unseen ("zero-day") attacks when evaluating machine-learning network intrusion detection systems (NIDS). We test whether this proxy holds. On the corrected CIC-IDS2017 release we train Random Forest, XGBoost, a 1D-CNN and an FT-Transformer and compare, at a fixed 1% false-positive rate over five seeds, detection under constrained perturbations of known attacks (gradient-based and black-box attacks on 42 attacker-controllable features) with leave-one-attack-family-out (LOAO) detection, where an entire family is absent from training. Detection under the strongest perturbation we tested, with budgets of at most 0.2, stays between 90.9% and 99.7%, yet mean detection of held-out families falls to 76.2% (RF), 40.2% (XGBoost), 25.8% (1D-CNN) and 22.8% (FT-Transformer). Robustness exceeds LOAO detection for every model (gaps of 24 to 72 percentage points, 23 to 66 when robustness is also averaged over families; Holm-adjusted p $\le$ 0.00096), and the two measures agree at most on a coarse ranking of the models. An exact mixed-integer evasion search confirms the tree ensembles' scores. Benign-only anomaly detectors and a simple multi-class open-set baseline do not close the gap. A temporal split on 5 seeds (3 of the 4 models) leaves the gap in place. On CSE-CIC-IDS2018 the gap recurs for every model (16 to 68 points). On these benchmarks and under this threat model, a robustness score should not be read as a zero-day score, and the two should be reported separately. Code and per-seed results are publicly available.

---


### 140. [Adversarial robustness does not entail human-aligned categorization](https://arxiv.org/abs/2611.00715)

**<font color=#1a73e8>作者：</font>** Itay Reznik, Raz Lapid, Moshe Sipper 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adversarial training can improve some forms of correspondence between artificial and biological vision, but whether robust classifiers acquire human-aligned classification behavior remains unclear. We generated 1,008 controversial stimuli by optimizing latent inputs to a pretrained GAN to elicit high-confidence disagreements between pairs of robust ImageNet classifiers. We compared four adversarially robust ImageNet classifiers - ResNet-101, ViT-B, ConvNeXt-L, and Swin-L - with two-alternative category judgments from 60 participants. We first evaluated each classifier on stimuli optimized to elicit disagreement with another model. Across classifiers, accuracy in predicting individual participants' single-trial category choices was near chance (48.6-51.3%), whereas majority judgments from other participants predicted responses with 85.0-86.8% accuracy. An analysis incorporating model prediction strength and participants' reported confidence found weak positive model-human correspondence for the two convolutional models. On stimuli optimized for disagreement between other model pairs, all four robust classifiers predicted human responses above chance but less accurately than predictions based on other participants' majority judgments; the same pattern held for 17 additional RobustBench models not used in stimulus generation. Across these 17 models, mean model-participant agreement was 67.3%, versus 81.3% mean participant-participant agreement on the same images. These results identify model-specific failures of human alignment and a model-human mismatch that persists across robust classifiers and substantially exceeds disagreement among human observers. Our findings show that adversarial robustness alone does not guarantee human-aligned categorization and suggest that robustness and human alignment should be evaluated as distinct properties of visual recognition systems.

---


### 141. [Uncertainty Aware Quality-Diversity Optimization For Offline Biological Sequence Design](https://arxiv.org/abs/2611.00716)

**<font color=#1a73e8>作者：</font>** Alona Rimon, Hannah Janmohamed, Maxime Allard 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Designing sequences such as nucleic acids and proteins with desired properties is a fundamental challenge in biology. Due to the vast, discrete nature of sequence spaces and the high cost of experimental evaluation, offline computational sequence design plays a crucial role in proposing novel sequences before costly wet-lab validation. In practice, it is also essential that proposed designs are diverse to increase the likelihood of downstream experimental success. This motivates methods that balance performance, novelty, and diversity, whilst mitigating against uncertainty inherent to offline optimization. Quality-Diversity optimization (QD) can discover diverse, high-performing solutions, making it well suited to this problem, but its elitist nature makes reliable exploration under uncertainty challenging. To address this, we introduce Prior-guided Offline MAP-Elites (POME), an uncertainty-aware QD framework explicitly adapted to the offline regime. Our method leverages foundation models as priors to guide search toward biologically plausible regions and enable robust exploration under uncertainty. Across three sequence design tasks, POME consistently improves both performance and diversity over prior offline QD methods, and achieves the most reliable balance compared to offline MBO baselines, obtaining the best performance on two tasks and the second-best on the third, while maintaining high diversity and novelty.

---


### 142. [SAVIER: Source-Anchored Visual Inspection and Evidence-Guided Repair for Vietnamese Cultural Text-to-Image Generation](https://arxiv.org/abs/2611.00722)

**<font color=#1a73e8>作者：</font>** Gia-Huy Thai, Duc-Tien Khong, Trung-Nghia Le  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present SAVIER, a training-free, one-pass framework that repairs the depiction of a named Vietnamese cultural entity in a generated image while preserving the scene details requested by the user. The problem is hard because a plausible scene can miss the cues that identify the entity, and prompt-level refinement never inspects the image it produces. SAVIER starts from a Culture-TRIP expanded prompt; a Curator separates source-linked cultural cues from prompt-preservation requirements, a prompt-blind Observer describes the first image, and a Refiner turns the discrepancies into at most three positive instructions before one regeneration with the same seed and a fixed bank of reference photographs. On the 50 bilingual prompts of ViCuP, evaluated with SDXL and FLUX.1-dev against a frozen, human-verified visual contract, SAVIER raises contract fulfillment from 55.6 to 69.6 and from 59.1 to 67.3 over Culture-TRIP and raises CAIRE cultural relevance on FLUX.1-dev. A reference-only ablation that removes the agent repair shows that SAVIER's photographs account for most of the contract gain; the agent roles add country-level relevance on FLUX.1-dev without lowering adherence to the original prompt under the official VQAScore. Project page: this https URL

---


### 143. [Cross-Evidence Authorization State Learning for Runtime Detection of Broken Object-Level Authorization in Black-Box Web Applications](https://arxiv.org/abs/2611.00738)

**<font color=#1a73e8>作者：</font>** Siqi Lin, Qianheng Cheng, Yiping Mao  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Broken object-level authorization (BOLA) remains difficult to detect in black-box Web applications because external runtime monitors generally lack access to source code, authorization policies, and object-ownership records. This paper proposes a cross-evidence authorization-state learning method that reconstructs subject--resource--object--action relations from request--response transactions. The method represents authorization relations with confidence-aware states, aggregates positive and negative evidence while accounting for provenance independence, and applies contamination-gated promotion, evidence quarantine and rollback, expiration, and revocation. A Python prototype is evaluated using a deterministic synthetic benchmark comprising 64,400 requests across five independent random seeds. In this benchmark, the proposed method achieves 100.00% recall, an F1-score of 56.63%, and a false-positive rate of 33.65%, while the measured unauthorized-relation pollution rate is 0.00%. Ablation experiments show that removing provenance independence or evidence quarantine increases the pollution rate to 100.00%. The experiments provide an initial evaluation under controlled synthetic conditions.

---


### 144. [Learning hidden-state dynamics from unpaired snapshots with lift-project SDEs](https://arxiv.org/abs/2611.00742)

**<font color=#1a73e8>作者：</font>** Qi Wang, Uduak George, Gustaaf Jacobs  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many systems are observed only through unpaired snapshots, with population samples available at each time point but no correspondence between samples at different times. These snapshots determine the one-time distributions but leave the temporal coupling unspecified, requiring a modeling prior to connect successive times. We propose the lift-project stochastic differential equation (SDE), an autonomous SDE on the observed coordinate and a few hidden coordinates, trained only to match the snapshots. Most existing methods, including time-dependent SDEs, Schrödinger bridges and optimal transport, evolve the observed coordinate alone. For a scalar observation, the classical comparison theorem implies that all such models have non-negative lagged covariance, so on data whose lagged covariance turns negative, their error has a computable floor. The lift-project SDE is not bound by this floor. On two representative partially observed systems, the Duffing and pendulum oscillators, at comparable fit to the snapshots, the proposed method reduces the lagged-covariance error by factors of 2.4 and 6.6 relative to the strongest baseline and is the only model below the error floor; one hidden coordinate is already enough for such improvement. Furthermore, if a second experiment changes only the initial state of the hidden coordinate, no single model that evolves the observed coordinate alone can fit both experiments, whereas a single lift-project SDE can.

---


### 145. [PeptSol: A Translational Benchmark for Protected-Peptide Solubility in Drug Manufacturing](https://arxiv.org/abs/2611.00749)

**<font color=#1a73e8>作者：</font>** Alexander Arjun Lobo, Marc Saouda, Urvi Awasthi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Liquid-phase peptide synthesis (LPPS) offers a scalable route to peptide manufacturing, but route development still depends on empirical solvent screens because each protected intermediate must be soluble for reaction and recoverable for purification. The protecting groups, terminal modifications, and noncanonical residues that govern this behaviour are poorly represented in existing peptide property benchmarks, limiting the ability to develop and rigorously evaluate molecular representation models for LPPS-relevant prediction tasks. We introduce PeptSol, an open benchmark of 1388 hand-curated protected-peptide solubility measurements with chemistry-aware splits. The measurements span only 84 parent sequences and 101 protected structures, and 92.5% come from a single historical programme. Across seven frozen molecular encoders, the best macro-F1 is 0.843 on binary solubility for the historical subset under a peptide-held-out split; the harder three-class ordinal task reaches 0.614 in that cell. No foundation model consistently outperforms a baseline combining chemical fingerprints with explicit molecular descriptors, and model rankings vary across prediction tasks and data splits. The dataset, evaluation protocol, and baselines establish a standard for measuring progress on molecular representations for synthesis-aware peptide developability.

---


### 146. [DuSE-Bench: Benchmarking Joint Reasoning over Evolving Dialogue and Documents](https://arxiv.org/abs/2611.00755)

**<font color=#1a73e8>作者：</font>** Guanjie Cheng, Jianfeng Gao, Yufei Tong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Persistent Web information assistants must combine evolving document facts with user requirements established and revised across sessions. Yet systematic evaluation of how changes in both sources affect response requirements and evidence attribution remains limited. To address this gap, we introduce Dual-Source Evolution Benchmark (DuSE-Bench), a benchmark comprising 1,000 tasks across five scenarios, including 700 whose required premises originate in both dialogue and documents. An evolving Support Graph guides task construction and preserves links from updated facts and reused conclusions to original turns and passages. Task annotations distinguish grounding source from state dependence and enable separate evaluation of response content, response type, and source attribution. Experiments across 11 baseline configurations reveal persistent challenges in joint reasoning over evolving dialogue and documents, with content accuracy on jointly grounded tasks reaching at most 56.7%. Moreover, improvements in content accuracy can coincide with poorer response choice, while content-correct responses frequently lack complete attribution to original evidence. Matched evidence substitutions further show that the effect of replacing one source's evidence depends on support from the other. These findings motivate coordinating dialogue memory and document retrieval to apply current user requirements and document facts together while preserving their original support. The data are available at this https URL.

---


### 147. [Old Is Not False: Valid-Time Memory for Interactive Video World Models](https://arxiv.org/abs/2611.00758)

**<font color=#1a73e8>作者：</font>** Ziming Wang, Chuyue Gong, Hongliang Cao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive video world models draw each frame from a memory bank of earlier frames stamped with their capture times. With frames, weights and noise fixed, reversing the timestamps of two views flips the state that generators of two families draw: they take the newest timestamp as the truth. That reading is right as long as states never return. After an agent undoes an action, the newest view of a region is outdated and the only view of the present is older; memories for changing worlds delete that older view, and memories that keep it hand the generator the past. Temporal databases separate when a record is stored from when its content holds, its valid time. ReDate keeps every frame and dates each retrieved token by its valid time, read from the agent's action log. The frozen generator then reads a reverted region as one that has just reached a new state, so ReDate needs no training. We prove that trusting the newest timestamp is right exactly when every current view is dated after every outdated one, that without a view taken after the return only the action log tells a reverted region from an up-to-date one, and that a generator able to draw from its own prediction gains more from re-dating than from deletion when the moved tokens keep little weight. After an undo, ReDate raises the share of FAR's steps showing the current state from 0.36 to 0.62 and HY-WorldPlay's from 0.003 to 0.19. We also propose a calibrated state metric to test any memory after undos.

---


### 148. [HiPaper: A Human-AI Collaborative System for Academic Literature Triage and Scholarly Sensemaking](https://arxiv.org/abs/2611.00762)

**<font color=#1a73e8>作者：</font>** Ye Jia, Pangjing Wu, Hayley Y.W. Gu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Scholarly sensemaking requires researchers to iteratively retrieve, collect, and synthesize literature as their understanding evolves. However, existing scholarly tools provide only partial support for this process. Recent artificial intelligence (AI)-based systems generally rely on opaque submit-and-wait pipelines that it users' ability to inspect, revise, and validate intermediate outputs. In this study, we present HiPaper, a human-AI collaborative literature review system informed by a formative study with academic experts. HiPaper organizes scholarly sensemaking as a three-stage interactive workflow spanning Retrieval, Collection, andSynthesis, centralized on the human-in-the-loop paradigm that exposes intermediate AI-generated content for user inspection and intervention through a persistent workspace called Knowledge Pocket. Through this workflow, users can iteratively refine search intent, curate and organize papers with AI-enriched metadata and clustering, and conduct evidence-traceable synthesis over selected literature. Our user study with 14 Ph.D. students showed that HiPaper efficiently supports scholarly sensemaking by enabling human-AI collaboration in both familiar and unfamiliar domains. Furthermore, the findings highlight how staged interactions with intermediate AI-generated content successfully scaffold user interactions throughout the sensemaking process.

---


### 149. [DADKC: Distribution-Aware Adaptive Differentiated Knowledge Consolidation for Cloth-Hybrid Lifelong Person Re-identification](https://arxiv.org/abs/2611.00768)

**<font color=#1a73e8>作者：</font>** Yan Zhang, Minghao Long, Meiqi Wan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lifelong Person Re-identification (LReID) aims to match the same person using sequentially collected data. In practical long-term deployments, however, the model must handle both domain shifts across cameras and scenes, and irregular clothing changes of the same identity. This gives rise to the Cloth-Hybrid Lifelong Person Re-identification (CH-LReID) task, which demands balancing cloth-relevant and cloth-irrelevant knowledge in streaming data. While existing LReID methods have explored replay-based or distillation-based anti-forgetting strategies, they typically fail to sufficiently model stage-aware domain distributions and cross-stage feature continuity under exemplar-free training. To address this problem, we propose a Distribution-Aware Adaptive Differentiated Knowledge Consolidation (DADKC) framework. The core idea is to enhance the existing Differentiated Knowledge Consolidation (DKC) paradigm with adaptive distribution modeling. To this end, three lightweight modules are designed: (1) an Anchor Pool Adapter (APA) to retrieve learnable anchor cues for refining identity features; (2) a Phase Path Mixer (PPM) to perform stage-aware expert routing for integrating domain-specific distribution paths; and (3) a Stage Bridge Alignment (SBA) module to regularize the continuity of base, anchor, and path representations between adjacent stages. Extensive experiments on the CH-LReID and LReID benchmarks show that DADKC gains 4.1%/4.5% mAP/R1 on Order-1 and 3.6%/3.4% mAP/R1 on Order-2 over the DKC baseline, and lowers weighted forgetting from 2.4%/1.7% to 1.8%/1.4%, while storing neither historical images nor per-image features. The code is available at this https URL.

---


### 150. [Now You See Them, Now You Dont FusionGhost Gait for Occlusion-Robust Gait Recognition with ArabGait dataset](https://arxiv.org/abs/2611.00780)

**<font color=#1a73e8>作者：</font>** Seba Al Mokdad, Tamer Shanableh, Reham Mohamed Aburas  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Skeleton-based gait recognition is generally more robust to appearance changes than pixel-based methods, but this robustness depends on stable pose extraction. Clothing variation in gait recognition includes changes in garments, silhouette, and carried items; under Gulf clothing (Kandoora/Abaya), the dominant failure mode shifts from appearance change to lower-limb pose degradation caused by severe occlusion. To study this regime, we introduce ArabGait, a 45-subject indoor multi-view dataset with four walking conditions across three viewpoints, and show that Gulf clothing lowers mean lower-limb confidence from 0.811 to 0.683 and raises lower-limb failure rate from 7.98% to 17.82%, with ankles most affected. We propose FusionGhost-Gait, a fused spatiotemporal architecture that integrates spatial graph blocks and temporal modeling in one residual unit, removes redundant channel projections, and uses compact temporal Ghost kernels as a lightweight regularization mechanism for pose-noisy trajectories while preserving efficient temporal downsampling. On ArabGait cross-clothing evaluation, including Protocol A and Protocol B, FusionGhost-Gait reaches up to 67.91% Rank-1 while remaining compact (108,970- 133,674 parameters and 0.035-0.052 billion floating-point operations (GFLOPs)), achieving more than 65% fewer parameters and 75% lower FLOPs than existing baselines. These results indicate that the proposed model generalizes effectively to challenging Gulf-clothing conditions while remaining lightweight and deployable for surveillance and access-control biometric systems.

---


> [!TIP]
> 当前位于：**101-150**（第 3/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-633](./part-13.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
