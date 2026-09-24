# 📦 其他研究 | 2026年09月25日

> 本类共 **240** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-240](./part-05.md)

---

### 1. [AgroBench: A Reproducible Multimodal Benchmark for Weakly Supervised Crop Yield Learning from County Statistics and Pixel Observations](https://arxiv.org/abs/2609.26809)

**<font color=#1a73e8>作者：</font>** Udaiveer Singh, Rajiv Ranjan, Shashank Tamaskar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable agricultural yield statistics are typically reported at coarse administrative scales, whereas modern geospatial machine learning methods require spatially explicit, pixel level supervision. This mismatch has limited the development of large-scale benchmarks for crop yield learning using multimodal Earth observation data. A reproducible benchmark, AgroBench, is presented for transforming publicly available U.S. county level crop yield statistics into weakly supervised pixel-level crop time series. Each crop pixel time series is paired with a county-level yield value as a weak supervisory signal rather than a directly measured pixel-level yield label. Our geospatial data generation pipeline integrates USDA crop yield statistics with crop-specific land cover masks, Sentinel 2 multispectral imagery, Sentinel-1 synthetic aperture radar observations, climatic variables, and terrain information to produce temporally aligned multimodal sequences describing individual crop pixels throughout the growing season. The resulting benchmark contains over 13 million observations from 788,654 unique crop pixels spanning 5,107 county year combinations across eight growing seasons (2017 to 2024) for five major U.S. crops. To facilitate standardized evaluation, we establish a crop yield prediction benchmark using a Leave-One-Year-Out evaluation protocol and provide baseline results using representative machine learning models. By releasing the complete data generation pipeline, benchmark dataset, and evaluation protocol, AgroBench provides a reproducible foundation for future research in weakly supervised learning, multimodal remote sensing, spatiotemporal modeling, and geospatial foundation models for agriculture.

---


### 2. [The Drift Contract: Spectral Updates for Depth-Robust Local Learning](https://arxiv.org/abs/2609.26811)

**<font color=#1a73e8>作者：</font>** Fabien Polly  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Local learning trains each layer with its own auxiliary loss and no global backward pass, which makes layer updates structurally parallel. Two problems have kept it marginal: accuracy degrades as depth grows, and hyperparameters are fragile. We apply Muon-style spectral update geometry (momentum orthogonalization with spectral step scaling) to per-layer local updates, an intersection not previously studied. On CIFAR-10 MLP benchmarks with local linear heads, a single step-size setting is the best value in our tested grids from width 128 to 2048 and from depth 12 to 48, while local Adam requires re-tuning along both axes and still collapses at depth 48 (31.3 percent re-tuned per depth, 19 percent with its depth-12 setting transferred, vs 42.7 percent for the spectral update at its unchanged setting). At five seeds and width 512 the spectral update leads local Adam by a clear margin (48.9 +/- 0.5 vs 46.6 +/- 0.3). Prospectively specified controls attribute the transfer and most of the depth robustness to the spectral geometry itself rather than to any step-size rule on top of it. We additionally formulate the step size as a drift contract, lr = epsilon / RMS(input), which bounds each layer's weight-induced pre-activation change per step, conditioned on its current input. The contract yields a small gain over the best fixed learning rate where that baseline is measured, makes the step size interpretable, and provides a per-layer, input-conditioned drift bound that standard optimizers do not offer. We report one negative result: with RMSNorm and weight decay in the trunk, the stability benefit of spectral updates accrues to global rather than local training, so the local advantage concentrates precisely where normalization is absent.

---


### 3. [Signal2Symbol: Neuro-Symbolic Temporal Reasoning for Explainable Physiological Time-Series Anomaly Detection](https://arxiv.org/abs/2609.26820)

**<font color=#1a73e8>作者：</font>** Naser Mansour, Sidahmed Benabderrahmane, Ameer Rahwan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physiological time series such as electrocardiograms (ECG) and electroencephalograms (EEG) exhibit complex temporal structure, substantial acquisition variability, and a strong need for transparent decision-making. Although deep models can achieve high detection performance, they often provide limited insight into why a segment is anomalous, how local anomalies relate over time, and whether a detection belongs to a broader recurring pattern. We propose Signal2Symbol, a neuro-symbolic framework for explainable biosignal anomaly detection. The method first converts ECG/EEG signals into symbolic sequences using either a learned VQ-VAE (Vector Quantized Variational Autoencoder) codebook or a SAX (Symbolic Aggregate approXimation) baseline. It then constructs bigram enriched token-window transactions and scores anomalies through rare itemset evidence derived from minimal rare itemset mining. Detected anomalous windows are merged into intervals and related using Allen interval algebra, enabling composite temporal explanations such as escalation chains, artifact overlap, and cross-channel synchrony. Finally, we introduce a rare temporal concept lattice based on Formal Concept Analysis (FCA), which groups anomalous intervals by shared rare symbolic evidence, Allen temporal relations, channel context, and robustness attributes. The resulting Galois lattice compresses many local detections into interpretable families of temporal-symbolic anomalies. We evaluate on three public benchmarks: MIT-BIH Arrhythmia (beat-level ECG), PTB-XL (record-level ECG), and the Bonn EEG dataset (segment-level EEG). We stress-test robustness under additive noise and baseline-wander perturbations. The results highlight the value of neuro-symbolic tokenization for temporal anomaly analysis and show that Allen/FCA reasoning provides compact, interpretable summaries of local detections.

---


### 4. [HARN: Hierarchical Associative Resonance Network for Event-Driven Multi-Timeframe Forecasting](https://arxiv.org/abs/2609.26822)

**<font color=#1a73e8>作者：</font>** Nabeel Ahmad Saidd  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Financial time series evolve across multiple temporal resolutions, challenging forecasting systems to incorporate newly available information without repeatedly recomputing unchanged representations. We introduce HARN, a Hierarchical Associative Resonance Network for event-driven multi-timeframe forecasting. HARN maintains persistent representations across temporal levels and updates each level only when its corresponding completed bar becomes available. The architecture combines causal multi-scale temporal encoding, gated associative memory, cross-level resonance, and hierarchical evidence aggregation, with forecasting performed in basis-point space and reconstructed to the original price scale. We evaluate HARN on four assets spanning equity, foreign exchange, and commodity markets using multiple random seeds and component ablations. HARN achieves competitive reconstructed-price forecasting errors against single-timeframe PatchTST and TimeXer baselines, while ablations reveal the effects of removing individual components across assets and timeframes. A code-level audit further examines consistency between the implementation and the defined event-driven causal protocol. The results position HARN as a persistent multi-timeframe forecasting framework rather than evidence of universal predictive superiority.

---


### 5. [What Makes a Terminal-Bench Task Hard? Separating Genuine Hardness from Fake-Hardness on an Adjudicated Agentic Corpus](https://arxiv.org/abs/2609.26826)

**<font color=#1a73e8>作者：</font>** Edward Lue Chee Lip, Boden Moraski, Tim Knappe 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Frontier benchmarks need tasks that current models cannot solve. But a task that no model solves is not automatically a hard task. The same zero pass rate can come from a real capability gap, but it can also come from missing context, a broken reference solution, infrastructure failure, or a verifier that can be bypassed. In this paper, we study this issue using a frozen Terminal-Bench 3 / Frontier-Bench 0.1 production record with 1,081 pull requests, 639 scored tasks, 28,801 trials, and $105,933 in logged agent spend. We ask what an all-fail task actually certifies. For the 125 tasks with no honest pass, we combine task artifacts, reference-solution runs, empty-solution controls, adversarial trials, trajectories, telemetry, and review records, and apply an ordered validity screen. Only 78 of the 125 tasks survive as certified-unsolved candidates. The remaining tasks include 14 with broken oracles, 8 dominated by infrastructure failures, 4 that are only passable through verifier bypasses, and 21 whose solvability is not certified by the available evidence. Thus, lack of saturation and genuine difficulty are not the same thing. The certified-unsolved label is also narrow: it means that the authored route passed, infrastructure did not dominate, no strict bypass was observed, and all evaluated agents failed. It does not prove intrinsic hardness, verifier completeness, or failure at the intended capability. We further analyze rejected submissions and passing tasks to show that pass rate alone cannot explain why a task is difficult. Overall, our results suggest that frontier benchmarks should report the evidence behind their all-fail tasks before using them as capability claims.

---


### 6. [LWCal: Loss-Weighted Calibration for Tabular Classifiers with Noisy Calibration Labels](https://arxiv.org/abs/2609.26839)

**<font color=#1a73e8>作者：</font>** Zeming Liu, Hang Lyu, Jingtao Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-hoc probability calibration is usually evaluated under an optimistic assumption: the held-out calibration labels are clean. In many AI deployment settings, however, labels come from weak annotators, historical decisions, heuristics, or distant supervision, so the same label noise that corrupts training also corrupts calibration. We study this overlooked failure mode for tabular classifiers and propose LWCal, a CPU-only post-hoc calibrator that down-weights calibration examples whose noisy labels are contradicted by the base model's held-out probability. LWCal requires no clean validation labels, no noise-rate estimate, and no retraining of the base classifier. A second variant, Gated-LWCal, adds a conservative disagreement gate that backs off toward the raw score when the calibration split appears extremely inconsistent. On nine local binary tabular tasks, six random seeds, symmetric and asymmetric label corruption, and three tree-based base learners, LWCal obtains the lowest average calibration error while Gated-LWCal obtains the best average proper-score tradeoff. In the main random-forest study over 432 noisy cells, Gated-LWCal reduces expected calibration error from 0.188 to 0.122 and negative log likelihood from 0.438 to 0.396 relative to the raw classifier. Paired bootstrap intervals for Gated-LWCal versus raw, Platt, isotonic, and beta calibration exclude zero on ECE, Brier score, and NLL. The artifact contains all scripts, result tables, figures, and the compiled paper.

---


### 7. [A Leakage-Aware Multimodal Evaluation Framework for Early Intraoperative Acute Kidney Injury Prediction](https://arxiv.org/abs/2609.26848)

**<font color=#1a73e8>作者：</font>** Quang Minh Nguyen, Duc Minh Le, Ho Nhat Minh Nguyen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Postoperative acute kidney injury (AKI) after major non-cardiac surgery carries substantial morbidity, yet early intraoperative risk stratification remains difficult. In this retrospective cohort study, we propose SynerT, a waveform-only hybrid temporal backbone that combines a causal dilated TCN with a hierarchy of dilated recurrent layers to encode early intraoperative physiologic trajectories for AKI risk prediction. Building on SynerT, we further design two model variants that extend the backbone with structured clinical context: SynerT-MM, a late-fusion multimodal extension that integrates hemodynamic burden summaries and preoperative covariates, and SynerTStack, a leakage-safe stacked ensemble that combines cross-validated predictions from SynerT-MM with strong tabular baselines at the meta-learning stage. All models are evaluated under a strict leakage-aware framework on VitalDB, a high-fidelity perioperative database, with prediction restricted to information available within the first 60 intraoperative minutes. Among 2,413 waveform-usable cases (180 AKI-positive; 7.46% prevalence), SynerT fell well below strong structured-data baselines, demonstrating that waveform-only temporal modeling is insufficient under strict early constraints. SynerTMM recovered discrimination by incorporating hemodynamic burden summaries and preoperative covariates, and SynerT-Stack achieved the best overall performance across AUROC, AUPRC, and F1-max. Cross-fitted Platt recalibration substantially corrected calibration defects in both multimodal variants, and decision-curve analysis confirmed the recalibrated stacked model delivered the strongest net clinical benefit across low-to-intermediate thresholds.

---


### 8. [QUARTET: Quad-branch cross-Attention and Random-walk Traces for Enhancing Transformers on Relational Graphs](https://arxiv.org/abs/2609.26855)

**<font color=#1a73e8>作者：</font>** Kyaw Hpone Myint, Nan Jiang, Xiang Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Relational Deep Learning (RDL) models multi-table databases as heterogeneous temporal graphs, and graph transformers currently achieve state-of-the-art performance on benchmarks like RelBench. However, the current leading model, RelGT, suffers from two key limitations: its random local sampler yields loosely connected subgraphs that hinder message passing, and its global attention module relies on a single, seed-feature-based memory that ignores broader macro-level dynamics. To overcome these limitations, we introduce QUARTET, an expressive graph transformer architecture that applies full self-attention on local subgraphs while enriching global context through cross-attention branches. Specifically, QUARTET employs a Causal Random Walk (CRW) sampler based on recency-truncated Personalized PageRank (PPR) to extract compact, hub-robust, and densely connected local subgraphs without temporal leakage. Concurrently, a quad-branch cross-attention module integrates global context from four complementary perspectives: seed feature, seed topology, temporal dynamics, and collaborative dynamics. Across the RelBench v1 classification tasks, QUARTET consistently matches or outperforms the current state-of-the-art graph transformer baselines (HGT and RelGT). Ablation studies confirm that the CRW sampler significantly enriches local neighborhood quality, while the global branches provide essential, task-specific predictive gains.

---


### 9. [Comparative Evaluation of Static Embedding Models for HTTP Request Anomaly Detection](https://arxiv.org/abs/2609.26860)

**<font color=#1a73e8>作者：</font>** Amanda Riverol, Gustavo Betarte, Rodrigo Martínez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Web applications are increasingly targeted by cyberattacks that exploit HTTP requests to evade security mechanisms. Traditional web application firewalls (WAFs) rely on rule-based approaches that often exhibit high false positive rates and limited adaptability. Recent studies have explored machine learning techniques and word embedding models to improve anomaly detection in HTTP traffic. This paper presents a benchmark for static embedding models, specifically Word2Vec, FastText, and Doc2Vec, within a unified, single-class classification framework. We propose HEDA (HTTP Embedding-Based Detection Architecture), a modular detection pipeline that combines static embedding representations with single-class anomaly detection models to detect anomalies at the request level. The approach operates in an unsupervised environment, where both the embedding models and detectors are trained exclusively on benign HTTP traffic. The proposed methodology is evaluated on three datasets with heterogeneous characteristics, including both synthetic and real traffic. The experimental results show that the choice of embedding representation significantly affects detection performance, and that FastText-based embeds produce the most consistent results across all datasets, achieving high detection rates while keeping false positive rates under control.

---


### 10. [Safety Nudges: User-Facing Interventions for Real-Time AI Risk Awareness](https://arxiv.org/abs/2609.26865)

**<font color=#1a73e8>作者：</font>** Varshini Elangovan, James Wedgwood, Chhavi Yadav 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Conversational AI systems can pose safety risks to their users such as hallucination, sycophancy, overconfidence, and anthropomorphism, but these risks are difficult for users to detect during everyday use. We introduce Safety Nudges, a browser-based tool that provides lightweight, in situ flags when concerning behavior is detected in chatbot conversations. We evaluated Safety Nudges in a two-week field study with 45 frequent chatbot users, collecting interaction logs, surveys, and feedback on individual nudges. Participants found the tool useful, clear, and minimally disruptive, with nearly all users reporting an increased awareness of potential AI harms, though we found that this improved awareness alone did not necessarily lead to discernible behavioral changes. Our results suggest that user facing safety nudges can complement model-level safeguards by helping people critically evaluate AI responses in context, while highlighting the importance of relevance, calibration, and user control in nudge design for conversational AI safety.

---


### 11. [PR-Smoother: Simulator-Preserving Non-Gaussian Smoothing for Data Assimilation](https://arxiv.org/abs/2609.26890)

**<font color=#1a73e8>作者：</font>** Yuta Tarumi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many physical data assimilation (DA) workflows require smoothing methods that represent non-Gaussian posteriors over physical state variables, scale to high-dimensional simulators, train from observation windows alone, and remain compatible with calibration of the prescribed simulator. We introduce PR-Smoother, a simulator-preserving amortized smoother designed for this prescribed-simulator DA regime. Its key design principle is to keep the prescribed simulator explicit in both the evidence lower bound and the variational family: rather than learning replacement dynamics or a learned trajectory prior, PR-Smoother learns only future-conditioned corrections around the prescribed rollout. This yields an explicit non-Gaussian smoothing distribution over physical trajectories and supports joint state, parameter, and sensor-bias learning from observations alone. The variational family contains the exact smoother in deterministic and linear-Gaussian limits. Empirically, PR-Smoother captures multimodal posteriors in 4-dimensional Lorenz-96, remains accurate under ambiguous nonlinear observations and process noise in 40-dimensional Lorenz-96, and scales to joint state-parameter-bias inference in 16,384-dimensional Kolmogorov flow.

---


### 12. [CORE-STACK+: Meta-Learning for Deep Stacked Generalization](https://arxiv.org/abs/2609.26905)

**<font color=#1a73e8>作者：</font>** Noor Islam S. Mohammad  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stacking heterogeneous vision backbones (CNNs, ViTs, and hybrids) is the de facto recipe for accuracy, calibration, and robustness, yet two coupled pathologies limit its returns. Prediction-space multicollinearity ill-conditions the meta-learner's Gram matrix, inflating weight variance and producing brittle solutions on a thin manifold. Calibration collapse compounds constituent miscalibration through naive linear stacking, so adding more models can hurt expected calibration error (ECE). Existing remedies, ridge regularization, greedy selection, model soups, and SWAG address at most one of these issues, and none jointly target conditioning and calibration in heterogeneous prediction pools. We introduce CORE-STACK+, a preconditioning pipeline with four components: (i) a kernelized redundancy filter that removes non-linear inter-model dependencies invisible to Pearson correlation, using Centered Kernel Alignment (CKA) [23]; (ii) a $<15$K-parameter differentiable meta-feature gate that learns per-sample attention over ensemble statistics; (iii) a spectrum-adaptive Ridge penalty $lambda^{star}=lmax(Chat)/SNR(Chat)$ derived from a Marchenko-Pastur signal-noise decomposition, eliminating nested cross-validation; and (iv) a Laplace-approximate Bayesian blender replacing inverse-RMSE heuristics. We prove a PAC-Bayes excess-risk bound that, for the first time, jointly accounts for prediction-space redundancy and meta-learner capacity. Across six benchmarks, CORE-STACK+ delivers $+1.8\%$ top-1 on ImageNet-1K, $-4.2$ mCE on ImageNet-C, $+0.9$ mIoU on ADE20K, and $+1.3$ AP on COCO, while reducing retained models by 35-57% and inference FLOPs by up to $41%$. ECE improves $2.1\times$ over deep ensembles without post hoc temperature scaling.

---


### 13. [On Preference Coverage Collapse from Hindsight Relabeling in Multi-Objective Reinforcement Learning](https://arxiv.org/abs/2609.26918)

**<font color=#1a73e8>作者：</font>** Baptiste Bonin, Caro Strickland, Audrey Durand  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hindsight relabeling which retroactively replacing a transition's goal with the outcome the agent actually achieved is an effective tool for improving sample-efficiency in Reinforcement Learning (RL). A natural extension to preference-conditioned multi-objective RL (MORL) relabels transitions with the preference direction the agent achieved rather than the one asked for. We show that this extension is frequently harmful: across four preference-conditioned off-policy algorithms spanning two critic backbones and two preference-sampling schemes on the continuous-control MO-Gymnasium suite, it degrades 19 of 36 algorithm-environment settings by as much as four standard deviations, improves only one, and leaves the rest unaffected.
The harm is not a symptom of noisy relabels; denoising the target recovers almost nothing, and neither prioritized sampling nor any buffer-structural choice reproduces it. Instead, repeated relabeling collapses the critic's coverage onto whatever narrow region of the preference space the agent happened to visit. We name this failure mode \emph{Preference Coverage Collapse}, and quantify it with abandoned preference mass (APM), a value-aware statistic that tracks the harm ($\rho = -0.73$) where a purely structural coverage count does not.
We then introduce \texttt{her\_mix}, a single-parameter convex combination pulling the achieved direction back towards the requested preference. At one fixed value across every algorithm and environment, it returns 16 of the 19 harmed settings to baseline, preserves and even improves the one setting in which relabeling helps, and cuts abandoned preference mass from $69\%$ to $6\%$. Protecting coverage over the preference simplex, not filtering noisy relabels, is what makes hindsight relabeling safe for MORL.

---


### 14. [Cross-Modal Contrastive Learning from Histopathology and CT for Automated Renal Cell Carcinoma Grading](https://arxiv.org/abs/2609.26920)

**<font color=#1a73e8>作者：</font>** Amit Das, Tanmay Shukla, Naofumi Tomita 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Background: Clear cell renal cell carcinoma (ccRCC) exhibits substantial clinical heterogeneity, and accurate grade assessment is essential for risk stratification and treatment planning. However, conventional grading requires invasive tissue sampling. We developed RCC-Align, a cross-modal contrastive learning framework that leverages paired histopathology and computed tomography (CT) data during training to improve noninvasive CT-based ccRCC grade prediction. Methods: RCC-Align aligns paired whole-slide histopathology images (WSIs) and CT scans through contrastive cross-modal objectives, transferring grade-discriminative information from microscopic tissue morphology to macroscopic radiologic representations. The framework was trained and evaluated on paired TCGA and CPTAC cohorts using patient-level five-fold cross-validation. Performance for low- versus high-grade ccRCC classification was compared against CT-only baselines (DINOv2-Base and DINOv2-Finetuned) and a WSI-based reference model (GigaPath-Finetuned). Cross-modal alignment was assessed using cosine similarity analysis. Results: RCC-Align achieved an AUC of 0.601 (95% CI, 0.524-0.673) and AUPRC of 0.599 (95% CI, 0.541-0.676), outperforming DINOv2-Finetuned (AUC 0.545; AUPRC 0.543) with significantly improved low-grade prediction (p = 0.004). RCC-Align also demonstrated stronger paired WSI-CT embedding alignment compared with baselines. The WSI-based GigaPath reference achieved an AUC of 0.719. Conclusion: Pathology-guided contrastive learning improves CT-based ccRCC grading while requiring only CT at inference. This approach may complement tissue diagnosis when biopsy is unsafe, infeasible, or limited by intratumoral heterogeneity. Validation in larger, multi-institutional cohorts with external testing is needed before clinical translation.

---


### 15. [A 3D Pose-Based Ensemble Framework for Cricket Shot Classification and Automated Biomechanical Analysis](https://arxiv.org/abs/2609.26923)

**<font color=#1a73e8>作者：</font>** Sourav Shome, M.D. Ashiquzzaman Rahad, Rameswar Debnath  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cricket is one of the most celebrated sports world-wide, and technological advancement has become deeply embedded in how the modern game is analyzed and coached. Cricket shot classification and automated performance analysis add a further dimension to this trend. Traditional approaches rely on RGB video features or static images, which are sensitive to environmental variations such as camera angle, lighting, and background clutter, and often fail to capture the underlying biomechanics of batting actions. In this paper, we propose a system to improve cricket coaching that takes raw video data, extracts batsmen from video frames using YOLO, and extracts 3D pose data from video frames using MeTRAbs. The system produces sequential skeletal pose data of 30 body points and captures the biomechanical features of a batsman. As part of the system, we also propose a deep learning ensemble for shot classification of four shots: flick, pull, defense, and drive. The ensemble performed well, compared to existing classification works, achieving 97.68% accuracy. In addition, we analyzed the misclassification rates to identify cases where shots were incorrectly classified and examined their possible causes. Our proposed system allows novice players to obtain useful feedback, such as important joint angles relative to expert batsmen, which can also be useful for injury prevention. The shot classifier also helps track class-wise shots over time for further analysis. In addition to novice players, coaches can use the system for player evaluation.

---


### 16. [Building Socio-Affective Artificial Intelligence for Interactive Multi-Agent Simulations](https://arxiv.org/abs/2609.26927)

**<font color=#1a73e8>作者：</font>** David Berga  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The objective of this article is to provide design principles and a software architecture for enabling interaction between humans and multiple agents in simulated dynamic worlds. This connects the current era of general artificial intelligence (AI/AGI) with the proliferation of transformer-based conversational agents and the increased computational capabilities. Given an overview of current and previous multi-agent theories of mind (socially and affectively-aware agents), the existence of an integrative design of agent interactions with themselves and with humans must be crucial for understanding how to create sustainable and governance in future human-agent reasoning systems. In this work is presented a software "AGIMUD" that integrates: A. socially-aware reasoning and emotion in agent behavior and interaction, B. a design of human multimodal scheme for human users, artificial agents and simulated worlds, and C. distributing the AI processing through the network to enable multiple autonomous agents. These integrations allow the dynamic world recreation as multi-user dungeons (MUDs) where both agents and humans can interact simultaneously in real time. Find the code online in this https URL.

---


### 17. [Which Objectives Need a Dial? Predicting Objective Conflict and Covering Trade-offs in Steerable Pluralistic Alignment](https://arxiv.org/abs/2609.26929)

**<font color=#1a73e8>作者：</font>** David Tsoi, Esra Dönmez  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> People hold diverse, sometimes conflicting values, so no single aligned model can satisfy everyone. Pluralistic alignment therefore calls for steerable models that can balance competing objectives differently. Multi-Objective Direct Preference Optimization (MODPO) does this by using an objective weight to span a continuum of trade-offs. We study two questions: when can one model improve two objectives simultaneously, and how can many trade-offs be covered without training a separate model for each? Across seven objective pairs from HelpSteer and UltraFeedback, two pre-training measurements predict whether objectives align or conflict for human-annotated data, but not for AI-annotated data, where response length and repetition confound reward-model scores. For broader trade-off coverage, selecting the nearest trained model and merging model parameters both help, but neither consistently matches direct training. These findings yield practical guidance for building steerable models that serve diverse preferences.

---


### 18. [When Post-Processing Fairness Constraints Help and When They Harm: Evidence from Eight Cross-Domain Evaluations](https://arxiv.org/abs/2609.26955)

**<font color=#1a73e8>作者：</font>** Nithin Raghava Ramachandra Narla  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fairness audits in production ML typically occur once, at deployment, on a single domain. Both fail in practice: fairness can shift after retraining or a changing user base, and interventions validated on one dataset are rarely tested across the heterogeneous domains an organization deploys. We present FAPE (Fairness Auditing for Production Environments), a four-stage framework evaluating a single post-processing intervention, Fairlearn's ThresholdOptimizer, across eight domain evaluations: criminal justice, income prediction, legal admissions, credit lending, agricultural lending, a multi-domain benchmark corpus, healthcare, and education. Each is scored on demographic parity and equalized odds difference, plus disparate impact ratio and accuracy cost where computable. Intervention effectiveness tracks baseline disparity magnitude: across model-domain pairs the constraint improved disparity in 9 of 14 high-disparity cases and worsened it in 3 of 4 near-fair ones. Each of the five high-disparity exceptions reverses under one of two measurement checks, a minimum group size or thresholds fit on held-out data. A CUSUM monitor started at deployment, tested on a simulated shift, separates constrained models that never met a 0.1 parity convention from those that met it and later regressed. A single deployment-time audit is therefore an unreliable guide, which argues for baseline-disparity screening and continuous monitoring

---


### 19. [Transfer Learning with Conformalized Quantile Regression for Solar PV Forecasting Under Load-Shedding-Driven Data Scarcity](https://arxiv.org/abs/2609.26959)

**<font color=#1a73e8>作者：</font>** Rakib Abdullah, K. M. Tahlil Mahfuz Faruk  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Solar photovoltaic (PV) forecasting in regions affected by load shedding is challenging because reliable historical observations are scarce. This study proposes a transfer learning framework combined with Conformalized Quantile Regression (CQR) to improve PV power forecasting and provide reliable uncertainty estimates under severe data scarcity. A source-domain PV dataset from Alice Springs, Australia, is used to pretrain a temporal forecasting model, which is then adapted to simulated Bangladesh PV data representing different levels of historical availability. Experimental results show that transfer learning reduces RMSE by up to 23.7% when only one month of target-domain data is available and by 13.7% with three months of data. The proposed Transfer Learning plus CQR framework achieves 94.3% empirical coverage with three months of target data while producing prediction intervals that are 14% narrower than those obtained without transfer learning. These results demonstrate that combining transfer learning with conformal uncertainty quantification can improve both point forecasting accuracy and uncertainty reliability when target-domain PV data are severely limited.

---


### 20. [CRISP: Scalable Importance-Stratified Coresets for Imbalanced Tabular Learning](https://arxiv.org/abs/2609.26962)

**<font color=#1a73e8>作者：</font>** Hardhik Mohanty, Indrayana Rustandi, Mohamadreza Sheibani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large imbalanced tabular datasets make repeated gradient-boosted tree training expensive. Existing coreset methods often lose accuracy when most majority examples are removed. We present CRISP (Coreset Reduction via Importance-Stratified Pruning), a linear-time method that allocates a negative-class budget across quantile strata of a proxy-model score. Sample weights account for unequal inclusion probabilities. At 95% negative-class reduction on a production fraud dataset, CRISP trains on approximately 1.70M of 25M rows and retains 99.7% of full-data Average Precision. This is a 93.2% reduction in total training rows. On public CriteoPrivateAds, CRISP has the highest mean Average Precision at each tested rate from 90% to 99.4% majority reduction. Sparkov results are mixed at lower rates, but CRISP has the highest mean at 99.2% and 99.4%. Ablations identify budget allocation and inverse-propensity weighting as the main sources of the production-dataset gain.

---


### 21. [How Constraints and Preferences Shape Travel Planning: Implications for AI Planning Support](https://arxiv.org/abs/2609.26968)

**<font color=#1a73e8>作者：</font>** Fuling Sun, Yining Cao, Peiling Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Planning is a common yet complex activity shaped by constraints to satisfy and preferences to balance. Travel planning, as both an everyday activity and a frequent benchmark for evaluating intelligent systems, offers a rich context for examining how constraints and preferences emerge and evolve. While recent AI systems have achieved impressive results in generating personalized itineraries, they often assume that users can articulate stable goals upfront. To understand how real-world planning unfolds, we conducted a two-part interview study: one with eight travelers reflecting on their planning experiences, and one with nine travel agents sharing professional practices. We trace the dynamics of constraints and preferences as they are surfaced, refined, and coordinated throughout the planning process, and identified 11 actions revolving around constraints and preferences, which shaped the planning process. We offer design heuristics for planning tools that better support human-AI collaborative actions to support the fluid, contingent nature of planning.

---


### 22. [TinyUDE: Solver-Free Universal Differential Equations on Microcontrollers via Lie-Taylor Jet Matching](https://arxiv.org/abs/2609.26972)

**<font color=#1a73e8>作者：</font>** Pranavanath Balamurali, Hrishi Kamireddy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training Universal Differential Equations (UDEs) traditionally relies on backpropagating through numerical ODE solvers, creating memory footprints far exceeding the capabilities of edge microcontrollers. We present Lie-Taylor jet matching, a solver-free training framework that fits a hybrid vector field directly to the first and second time-derivatives of observed system states. These derivatives, the truncated Lie-Taylor jet, are estimated online via Savitzky-Golay filtering, yielding fully analytic gradients without automatic differentiation software. We evaluate whether eliminating the solver compromises accuracy against a conventional baseline (fixed-step RK4 integration, multiple shooting, exact discrete adjoints, Adam) sharing identical dynamics, noise models, network architectures, and metrics. While naive derivative matching degrades under sensor noise, our noise-adaptive mechanisms close and reverse this gap: full-rate phase-shifted sampling, a reservoir buffer, cosine-annealed optimization with weight averaging, on-device noise estimation, and polynomial-misfit quality gating. On a damped pendulum and chaotic double pendulum, our method matches or exceeds baseline accuracy at matched data windows and recovers unmodeled damping coefficients. Across noise levels from 0% to 5%, it attains a geometric-mean relative field error of 0.65x that of the baseline within 108 kB of static memory, compared with megabytes of solver tape. On an ESP32 microcontroller, the on-device run reaches a field error of 0.0020 and recovers the damping coefficient to c = 0.400 (true 0.400) within 61.3 kB of static memory and 7.24 ms per update (18.1% duty cycle at 25 Hz), confirming real-time on-device training is feasible without a numerical solver.

---


### 23. [Resource-Efficient Distributed Recursive Gaussian Processes](https://arxiv.org/abs/2609.26979)

**<font color=#1a73e8>作者：</font>** Josephine King, Ali Emre Balci, Raj Thilak Rajan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gaussian processes (GPs) provide a flexible framework for learning unknown functions from noisy measurements while quantifying predictive uncertainty, making them well suited for estimation in multi-agent systems. However, when measurements are collected by multiple agents, maintaining a unified GP model without centralized processing requires efficient distributed algorithms that can operate using local measurements and communication with neighboring agents. In this work, we develop two distributed recursive GP (RGP) algorithms for multi-output GP regression: ADMM-RGP and PDMM-RGP. We analyze the stability and convergence of both algorithms and develop parameter selection strategies to accelerate convergence, thus reducing the communication burden. The proposed methods are validated on a real-world multi-output wind dataset, and their convergence behavior is examined across communication graphs with varying connectivity. Numerical experiments demonstrate that ADMM-RGP and PDMM-RGP can significantly reduce communication relative to the state of the art, while maintaining comparable estimation accuracy and network-wide consensus.

---


### 24. [Lessons learned from deploying imaging AI with the open PACS-AI platform](https://arxiv.org/abs/2609.26981)

**<font color=#1a73e8>作者：</font>** Samuel Kadoury, Julie G. Hussin, Pascal Thériault-Lauzier 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We describe deploying imaging AI at six hospitals through PACS-AI, an open self-hosted platform. The binding constraint is not model accuracy but infrastructure to route studies, display results, capture feedback, and audit what runs. At one center, angiography models completed 515 of 607 jobs (84.8%); failures reflected absent diagnostic views, and 78.1% of 638 clinician ratings were positive. Publishing honest readiness levels for every model is itself a governance practice.

---


### 25. [Topological Signatures of Cyber-Attack Classes in Natural Visibility Graph Representations of Network Traffic](https://arxiv.org/abs/2609.26990)

**<font color=#1a73e8>作者：</font>** Ali Melih Kanca, Ilker Turker  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Natural Visibility Graph (NVG)-based representations provide a promising approach for capturing structural patterns in sequential network traffic. However, whether different cyber-attack classes exhibit distinctive topological signatures in such representations remains insufficiently understood. This study investigates the discriminative and structural characteristics of NVG-based network traffic representations using the CSE-CIC-IDS2018 dataset. Seventy-six numerical traffic features were independently transformed into NVGs within overlapping frames of 40 observations, and ten graph-theoretic metrics were extracted from each graph, resulting in 760 topological descriptors per frame. The discriminative capability of these representations was evaluated using a multi-branch convolutional neural network (CNN) with stratified five-fold cross-validation. The model achieved an average accuracy of 96.20% and a Matthews correlation coefficient (MCC) of 0.9566. To characterize class-specific topological differences, Kruskal-Wallis and Mann-Whitney U tests were combined with Benjamini-Hochberg false discovery rate correction and effect-size measures. Of the 10,640 attack-versus-benign comparisons, 7,777 (73.1%) remained statistically significant after FDR correction, with 4,844 exhibiting large Cliff's delta effects. The strongest global differences were predominantly associated with backward-traffic and packet-length-related features combined with connectivity, clustering, and centrality measures. These findings indicate that NVG-derived representations can provide strong discriminative capability while revealing class-dependent topological patterns associated with different cyber-attack classes.

---


### 26. [HYDRO: Towards Non-Reversible Face De-Identification Using a High-Fidelity Hybrid Diffusion and Target-Oriented Approach](https://arxiv.org/abs/2609.27011)

**<font color=#1a73e8>作者：</font>** Felix Rosberg, Vitomir Štruc, Cristofer Englund 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Target-oriented face de-identification models aim to anonymize the identity of a target individual across different images or video frames, such that the target can no longer be reliably recognized, while maintaining key characteristics of the visual data. Such models commonly leverage generative encoder-decoder architectures to manipulate facial appearances, enabling them to produce realistic high-fidelity de-identification results, while ensuring considerable attribute-retention capabilities. However, target-oriented models also carry the risk of inadvertently preserving subtle identity cues, making them (potentially) reversible and susceptible to reconstruction attacks. To address this problem, we introduce in this paper a novel (robust) face de-identification approach, called HYDRO, that combines target-oriented models with a dedicated diffusion process specifically designed to destroy any imperceptible information that may allow learning to reverse the de-identification procedure. HYDRO first de-identifies the given face image, injects noise into the de-identification result to impede reconstruction, and then applies a diffusion-based recovery step to improve fidelity and minimize the impact of the noising process on the data characteristics. To further improve image fidelity and better retain gaze directions, a novel Eye Similarity Discriminator (ESD) is also introduced and incorporated it into the training of HYDRO. Extensive quantitative and qualitative experiments on three diverse datasets demonstrate that HYDRO exhibits state-of-the-art (SOTA) fidelity and attribute-retention capabilities, while being the only target-oriented method resilient against reconstruction attacks. In comparison to multiple SOTA competitors, HYDRO reduces the success of reconstruction attacks by 85.7% on average.

---


### 27. [Anatomy-Aware Synthesis of Post-Contrast Breast MRI from Pre-Contrast Images](https://arxiv.org/abs/2609.27015)

**<font color=#1a73e8>作者：</font>** Zhengbo Zhou, Dooman Arefan, Lin Gu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We developed an anatomy-aware deep learning framework to synthesize post-contrast breast MRI from pre-contrast images, emphasizing tumor and background parenchymal enhancement (BPE) regions. This retrospective study included 649 patients with 6,251 paired pre-contrast and post-contrast images. The framework integrates breast mask consistency, lesion-region supervision, and BPE-region supervision into an image-to-image translation model. Evaluation included quantitative image quality metrics, a reader study with two breast radiologists, and downstream Ki-67 classification. The proposed method outperformed Pix2Pix, Pix2PixHD, diffusion-based synthesis, and mask-supervised baselines in whole-image and regional evaluations. Ki-67 classification showed no statistically significant performance differences across real- and synthetic-image training and testing settings, although this does not establish equivalence. These findings suggest that anatomy-aware supervision improves synthesis fidelity and support further investigation of synthetic post-contrast MRI for contrast-free imaging workflows.

---


### 28. [GeoRVQ: Decoder-aware geometry for residual-token prediction in physiological signals](https://arxiv.org/abs/2609.27018)

**<font color=#1a73e8>作者：</font>** Bo Cui, Yaowen Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Residual vector quantization (RVQ) turns physiological waveforms into compact token sequences, but conventional masked modeling treats every incorrect token as equally costly. We propose GeoRVQ, a coarse-to-fine masked token model whose objective reflects the local response of a frozen waveform decoder. Decoder-induced costs define geometry-aware soft targets and expected distortion, while quantizer-causal prediction follows residual dependencies from coarse to fine levels. In a descriptive aggregate over MIMIC-IV Waveform, VitalDB, and CODE-15\%, GeoRVQ increases exact token accuracy from $.133\pm.004$ to $.143\pm.003$, reduces decoded distance from $.606\pm.006$ to $.393\pm.007$, and increases R-peak F1 from $.784\pm.004$ to $.837\pm.008$ under matched model and training conditions. Across 45 held-out code substitutions, decoder-induced cost has a Spearman correlation of $.85$ with realized decoded cost, compared with $.54$ for Euclidean codeword distance. These results indicate that decoder-aware objectives can improve waveform and event preservation without requiring a large increase in exact token accuracy.

---


### 29. [Adversarial Attacks and Identity Leakage in De-Identification Systems: An Empirical Study](https://arxiv.org/abs/2609.27022)

**<font color=#1a73e8>作者：</font>** Felix Rosberg, Cristofer Englund, Eren Erdal Aksoy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we investigate the impact of adversarial attacks on identity encoders within a realistic de-identification framework. Our experiments show that the transferability of attacks transfers from an external surrogate model to the system model (e.g., CosFace to ArcFace) allows the adversary to cause identity information to leak in a sufficiently sensitive face recognition system. We present experimental evidence and propose strategies to mitigate this vulnerability. Specifically, we show how fine-tuning on adversarial examples helps to mitigate this effect for distortion-based attacks (i.e., snow, fog, etc.), while a simple low-pass filter can attenuate the effect of adversarial noise without affecting the de-identified images. Our mitigation results in a de-identification system that preserves its functionality while being significantly more robust to adversarial noise.

---


### 30. [LexLattice: Multilingual Extractive Summarization via Neural Cellular Automata on Document Hierarchies](https://arxiv.org/abs/2609.27032)

**<font color=#1a73e8>作者：</font>** Sujay Uday Rittikar, Sheela Ramanna  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Faithfulness is a central concern in legal text summarization, which motivates extractive approaches that select verbatim content traceable to its source. Such methods typically rank paragraphs or other structural units in isolation, yet give little attention to consolidating evidence that is distributed across, and shares salience between, distant parts of a document. We introduce LexLattice, an extractive summarizer that reifies a legal act's hierarchy as a two-dimensional semantic lattice and consolidates over it with a masked 2D neural cellular automata before selection. LexLattice attains state-of-the-art ROUGE across all 24 languages of EUR-Lex-Sum in both multilingual and cross-lingual settings, surpassing instruction-tuned baselines with billions of parameters, despite concentrating all trainable capacity in a 1.8M parameter consolidator over a frozen multilingual encoder. A consolidator trained only on high-resource languages further transfers to unseen languages with near-lossless retention (0.99), indicating that the model operates on language-agnostic semantic geometry rather than surface form. Our results position explicit consolidation over document structure as a compact and traceable alternative to scale for multilingual legal summarization.

---


### 31. [WTF?! Simulation-Free Reinforcement Learning with Wasserstein-Tilted Flow Maps](https://arxiv.org/abs/2609.27033)

**<font color=#1a73e8>作者：</font>** Abbas Mammadov, Jerry Y. Huang, Justin Lin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reward fine-tuning aims to update a pre-trained flow-based generative model to improve the downstream reward of its generated samples. Existing methods typically formulate this problem as sampling from a reward-tilted distribution, the solution to a KL-regularized reward-maximization problem. Here, we introduce an optimal transport regularizer built directly from the pre-trained drift. Unlike KL reward tilting, the resulting objective transports individual samples toward higher reward rather than reweighting the base distribution. We show that the resulting problem is equivalent to a deterministic optimal control problem on the flow. Given a pre-trained flow map, this equivalence yields a simulation-free reinforcement learning algorithm for fine-tuning generative flows. We call the resulting framework Wasserstein-Tilted Flow Maps (WTF), the first end-to-end fine-tuning recipe native to flow maps. The output is a fine-tuned flow map that retains strong reward-aligned performance at few-step inference budgets without post-hoc distillation. Experiments on ImageNet-256 and text-to-image show that WTF achieves higher reward with comparable or higher diversity than baselines, while requiring up to $280\times$ less training compute. More broadly, we argue that accelerated samplers such as flow maps are essential infrastructure for efficient post-training, and that the dominant KL-regularized formulation is only one of many choices worth revisiting.

---


### 32. [Training Intelligent Voice Assistant Wakeup with Controllable Synthetic Conversations](https://arxiv.org/abs/2609.27037)

**<font color=#1a73e8>作者：</font>** Marcin Sowański, Kacper Leszczyński, Kacper Krzywicki 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Wake word detection is a critical component of virtual assistants, serving as the gateway to seamless user interactions. This paper introduces a novel wake-up system that extends traditional direct keyword detection with contextual trigger detection. After an initial wake word activation, the system uses reasoning to distinguish between user commands and unrelated speech, ensuring efficient and context-aware engagement. We present a data generation architecture that produces a 62.3-hour corpus of controllable multi-speaker conversations containing direct invocations, contextual follow-ups, and non-addressed speech. Experimental results demonstrate the effectiveness of the proposed approach across diverse synthetic conversational scenarios. We release the code, dataset and trained models to promote reproducibility and further advancements in intelligent assistant technologies.

---


### 33. [Improving Service Availability in KubeEdge-Based Architectures Using Lightweight Intrusion Detection](https://arxiv.org/abs/2609.27052)

**<font color=#1a73e8>作者：</font>** Harrol Ndjeudji Kuibou, Mostafa Anouar Ghorab, Mohamed Aymen Saied  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The increasing adoption of the Internet of Things (IoT) and cloud computing has accelerated the evolution of edge computing paradigms [1]. Industry forecasts estimate that the number of connected IoT devices will reach approximately 50 billion by 2030, following an estimated 38 billion connections by 2025 [34], resulting in an unprecedented growth in data generation. This trend necessitates efficient, scalable, and secure data processing mechanisms at the network edge. Consequently, ensuring the reliable management and protection of IoT applications and devices has become a critical challenge. In this context, KubeEdge extends cloud-native capabilities to edge environments, enabling distributed orchestration while introducing new security concerns. This paper investigates the security of container images in IoT-driven and distributed edge architectures. Specifically, we analyze the impact of major security threats, including Denial of Service (DoS) attacks and malicious container deployments, on the availability and operational stability of KubeEdge-based systems. To address these challenges, we propose a lightweight Recommended Intrusion Detection Rule Set (RIDRS) tailored for resource-constrained edge environments. The proposed approach improves system resilience by enabling timely detection and mitigation of security threats. We define system stability as the ability to maintain consistent operational behavior and to recover autonomously under adversarial conditions. Experimental results demonstrate that RIDRS significantly reduces system downtime and enhances service availability, particularly in scenarios involving code injection and malicious pod deployment attacks.

---


### 34. [The Illinois Social Attitudes Aggregate Corpus (ISAAC): An Open Tool and Reproducible Pipeline for Analyzing Social Group Discourse at Scale](https://arxiv.org/abs/2609.27059)

**<font color=#1a73e8>作者：</font>** Babak Hemmatian, Sarah Hadjarab, Jessica Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce the Illinois Social Attitudes Aggregate Corpus (ISAAC), an open, modular, and accessible corpus of 527 million+ English-language Reddit posts selected for relevance to six key social group distinctions based on race, sexuality, age, ability, body weight, and skin tone, covering the 17-year period from 2007 to 2023. A multi-step, human-audited filtering pipeline was used to keep irrelevant content in the curated dataset below 10%, both overall and for each social group distinction. Each post was then algorithmically annotated with the user's estimated home region, along with a suite of validated off-the-shelf and custom semantic labels including moralization, sentiment, emotion, and linguistic generalization. We confirm the validity of the resulting corpus through convergent evidence linking ISAAC to macro-level societal trends, such as online search behavior, temporal spikes during major societal events (both nationally and regionally), and long-term shifts in public attitudes. By offering a unified, public infrastructure, ISAAC eliminates research fragmentation and enables seamless replication while supporting diverse empirical workflows at scale. Specifically, ISAAC allows investigators to perform cross-category comparisons, conduct high-precision tracking of long-term temporal shifts in social group discourse, and map spatial variation onto localized public opinion and policy outcomes. ISAAC's fully public, modular pipeline facilitates easy extension of the corpus to new platforms, languages, and social categories. To accommodate various research needs, ISAAC is accessible both without coding through a point-and-click website and labeler web-apps, and programmatically via an SQL playground, a Python package, and HuggingFace.

---


### 35. [Pro-Bench: Prompt-Robust Open-Vocabulary Visual Grounding Across Real-World Heterogeneous Environments](https://arxiv.org/abs/2609.27076)

**<font color=#1a73e8>作者：</font>** Linus Nwankwo, Muslim Alaran, Christian Rauch 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary visual grounding enables robots to localise task-relevant entities from natural-language queries without dependence on predefined perceptual taxonomies. However, existing benchmarks largely rely on short category labels and web-scraped imagery, leaving it unclear whether open-vocabulary models can robustly ground diverse queries and visual conditions under real deployments. We introduce \textbf{Pro-Bench}, a prompt-conditioned benchmark for open-vocabulary visual grounding in heterogeneous, real-world environments. Pro-Bench includes $13k+$ RGB frames from independent robotic domains (subterranean, industrial, indoor, outdoor, urban), with $74.5k$ manual instance annotations and $515$ target queries covering categorical, attributive, relational, affordance, state, part-whole, negative, and compositional semantics. We benchmarked $16$ open-vocabulary model configurations in strict zero-shot inference, measuring localisation accuracy across IoU thresholds, end-to-end inference latency, prompt-induced performance variation, and target recovery consistency. Our results show that prompt-robustness is strongly architecture-dependent. Most model configurations ($10/16$) perform best with short category labels, whereas free-form queries yield the highest accuracy for only one. Moreover, similar aggregate mAP can conceal substantial differences in consistent target recovery across reformulations. Pro-Bench enables systematic evaluation of these gaps and supports prompt-robust visual grounding. Pro-Bench: this https URL.

---


### 36. [NADI 2026: The Second Multidialectal Arabic Speech Processing Shared Task](https://arxiv.org/abs/2609.27086)

**<font color=#1a73e8>作者：</font>** Peter Sullivan, Bashar Talafha, Ahmed Ashraf 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> NADI 2026 is the seventh edition of the Nuanced Arabic Dialect Identification (NADI) shared task series and the second dedicated to multidialectal Arabic speech processing. This edition comprises five tasks and eight subtasks spanning Automatic Speech Recognition (ASR), Spoken Dialect Identification (SDID), Text-to-Speech (TTS), Spoken Language Translation (SLT), and Spoken Language Understanding (SLU). NADI 2026 emphasizes realistic evaluation through low-bandwidth, mixed-dialect, code-switched, out-of-domain, and zero-shot settings, while introducing TTS, SLT, and SLU to the series for the first time. The shared task attracted 21 participating teams from at least 13 countries, with 48 test-phase submissions and 14 submitted system-description papers. Results show that out-of-domain generalization remains a major bottleneck and highlight the effectiveness of recent Arabic-specialized speech models, multimodal dialect identification approaches, and ensemble methods. Overall, NADI 2026 provides a broader and more challenging benchmark for robust Arabic dialect speech processing.

---


### 37. [Local Evidence and Geometric Readout Repair in Trained GNNs](https://arxiv.org/abs/2609.27092)

**<font color=#1a73e8>作者：</font>** Nadi Tomeh, Hugo Attali  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many node-classification GNNs apply a linear classifier to a nonnegative mixture of local messages. An error can reflect either poor mixture weights or a reachable logit set poorly positioned for the classifier. We separate these causes with an exact-mass linear program and two learned post-hoc repairs. Every reweighted prediction has an equivalent centered logit translation, but only translations in a message-induced displacement set are realizable by reweighting. Across eight datasets, eight GNN backbones, and ten splits, mean accuracy rises from 62.6% for the frozen models to 63.8% with reweighting and 65.3% with set-conditioned translation. A parameter-matched node-only translator reaches 64.6%, showing that translation explains most of the gain while the message set supplies a smaller additional benefit. Although oracle reweighting can correct many errors, label-free reweighting captures little of this potential: local evidence is often present but hard to select, and relaxing the evidence constraint is more effective than learning within it.

---


### 38. [Cryptographic Security Is Not Enough: Privacy Gaps in the Renegade Decentralized Dark Pool](https://arxiv.org/abs/2609.27100)

**<font color=#1a73e8>作者：</font>** Prerna Arote, Adrian Saiz, Oriol Saguillo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Dark pools are designed to provide pre-trade privacy, liveness, and post-trade confidentiality - concealing order flow before execution and limiting information leakage after. Decentralized dark pools, such as Renegade, aim to replicate these properties without custodial risk, using secure multi-party computation (MPC) and zero-knowledge proofs for private order matching and verifiable settlement.
We show that Renegade's cryptographic guarantees do not deliver these dark pool properties in practice. MPC-with-abort ensures correctness but not fairness: a party may learn the match result and abort without penalty, breaking pre-trade privacy. We demonstrate that the protocol's discovery layer further leaks trading intent before MPC even begins, and that sustained probing via selective abort can probabilistically reconstruct counterparty order history, threatening post-trade confidentiality. We also show that the absence of input-consistency checks prior to MPC execution enables a griefing attack using invalid state commitments requiring no real token holdings that continuously locks honest users' wallets and wastes compute, breaking liveness under sustained conditions.
We further analyze over 700,000 Renegade transactions on Base and probe the P2P layer, finding that the network is effectively centralized: 88% of traffic routes through a handful of relayers, with only four nodes sustaining the P2P layer. Since relayers hold their users' wallet state in plaintext, this concentration means the system operates as a centralized orderbook in practice - reproducing off-chain the information asymmetry that dark pools are designed to eliminate.
Together, our results show that cryptographic privacy does not imply dark pool security: pre-trade privacy, liveness, and post-trade confidentiality each require additional protocol-level guarantees beyond MPC correctness.

---


### 39. [Damnatio Memoriae: Adversarially and Selectively Forgetting Identities in the Embedding Space of Face Recognition Models](https://arxiv.org/abs/2609.27115)

**<font color=#1a73e8>作者：</font>** Ünsal Öztürk, Vedrana Krivokuća Hahn, Sushil Bhattacharjee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A face recognition model links two images of a person recorded on separate occasions when their embedding similarity exceeds an operating threshold. We consider making chosen identities unlinkable across separate occasions while the model remains in service for the rest of the population. Deleting their images and retraining does not achieve this, since the model recognises identities never observed in training. Therefore, the embedding space must be altered against these identities, the process of which we call open-set adversarial forgetting. We propose three loss functions, one that disperses an identity's embeddings from their centroid, and two that map each image onto its own near-orthogonal target, learnt with the classifier head or fixed in advance as an almost-orthonormal frame. Each is fine-tuned alongside the classification objective on a subset of each identity's images. We evaluate them against four methods from prior work in verification and identification, at two forget scales and three backbones. Every loss acting on the embedding geometry makes the forget identities nearly unidentifiable. The orthonormal frame alone achieves strong forgetting, which holds wherever an image of that subset enters the comparison and leaves distinct forget identities unlinkable. It also surpasses a concurrent unsupervised method at a higher retain rate.

---


### 40. [From greenhouse climate to individual leaves: an organ-resolved model of lettuce growth](https://arxiv.org/abs/2609.27118)

**<font color=#1a73e8>作者：</font>** Md Hasibur Rahman, Faraz Ahmed, Hafiz Muhammad Bilal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Greenhouse climate management aims to improve crop production while limiting energy use. This requires knowing how a crop will respond before conditions are changed. A crop digital twin can support this decision only if it represents how plant physiology and structure develop together. A unified framework was developed to simulate lettuce growth from the physiology of individual leaves. Each leaf received the conditions at its position in the canopy and contributed carbon through photosynthesis. Part of this carbon was used for maintenance and the remainder supported growth, distributed among leaves by their age, size and local environment. The predicted leaf mass, area and age generated an evolving three-dimensional plant in NVIDIA Isaac Sim. Ray tracing calculated the radiation intercepted by each leaf and returned it to photosynthesis, so structure and growth influenced each other over time. Against greenhouse measurements, the relative root mean square error was 9.5% for total dry weight and 9.2%, 12.7% and 13.1% for leaf number, canopy diameter and largest-leaf area, respectively. A 30% decrease in incident radiation reduced final dry weight by 10.4%, while the same increase raised it by 6.9%, and adding 200 ppm carbon dioxide raised it by 46.1%. Within a simulated 40-plant block, interior plants accumulated 8.6% less dry weight than border plants with identical initial states, and the leaf-specific tipburn index rose in the enclosed leaves over the period in which tipburn appeared on the greenhouse plants. Resolving individual leaves therefore explains how local exposure changes plant growth within the greenhouse. The framework provides the forward plant model needed for a bidirectional digital twin, where observations of the physical plant can update predictions and support greenhouse climate decisions.

---


### 41. [PEARL: A Lightweight Prompt-based Feature Interpreter Framework for Real-Time, Anonymous, and Heterogeneous Collaborative Perception](https://arxiv.org/abs/2609.27123)

**<font color=#1a73e8>作者：</font>** Armin Maleki, Hayder Radha  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Heterogeneity across Collaborative Perception (CP) agents is a major challenge for emerging CP frameworks due to domain gaps from differing sensors, architectures, and training data. Prior works mitigate this challenge by aligning features in a unified space via model retraining or per-agent-type interpreters. These strategies (a) require access to neighbor configurations, (b) do not fully address real-time CP deployment, and (c) generalize poorly to unseen agents joining at run time. To overcome these challenges, we present PEARL, a Prompt-Embedding framework for Anonymous and Real-time Lightweight heterogeneous CP. PEARL supports multiple CP interpreters and selects one for a new-joining agent in real time using two lightweight, multi-scale interpreters trained in parallel: a sparse-detection (LWSD) interpreter that aligns salient regions for cooperative detection, and a dense, domain-invariant (LWDDI) interpreter that produces agent-invariant features for fast interpreter selection. Both interpreters use low-rank visual prompts to reduce computation, storage, and model complexity. Extensive experiments on simulated (OPV2V, V2XSet) and real (DAIR-V2X) datasets show that PEARL generalizes across simulated and real-world cooperative driving scenarios. Its real-time model-selection strategy yields an 8.2% Average Precision (AP) gain over a random-selection baseline while running in 1.67 ms on average. Although primarily designed for real-time CP, PEARL also outperforms state-of-the-art heterogeneous CP frameworks under traditional offline training by 5.6% AP on average while reducing communication cost by up to 34.7 times. Equally important, PEARL does not require sharing agents' configurations or model settings, thereby protecting information that may be proprietary or private. These results establish PEARL as a scalable and practical framework for heterogeneous collaborative perception.

---


### 42. [When Clients Are Orchestrated: Strategic Gradient Manipulation to Defeat Federated Learning Servers with Efficient Defense](https://arxiv.org/abs/2609.27124)

**<font color=#1a73e8>作者：</font>** Mohamed Shaaban, Ahmed Abdelnaby, Mohamed Elmahallawy  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated Learning enables decentralized model training by exchanging model updates--rather than raw data--with a central parameter server (PS). While most of the existing defenses primarily assume static or independently acting adversaries, we reveal a new class of dynamically adaptive attacks that systematically bypass such protections. We propose Fed-ADR, a holistic attack framework in which a malicious orchestrator server (OS) dynamically coordinates a heterogeneous set of adversarial clients, including both targeted and untargeted attackers. Through real-time coordination by the OS, malicious clients strategically adapt their gradient updates to evade defenses deployed by the PS, while either severely degrading global model performance or steering training toward adversarial this http URL mitigate this threat, we offer a detection mechanism that estimates each client's true gradient from historical updates, enabling real-time detection of coordinated malicious behavior without additional overhead. We further introduce an in-situ recovery mechanism that restores global model performance without restarting training, preserving convergence and minimizing recovery time. Comprehensive experiments on MNIST, Fashion-MNIST, and CIFAR-10 benchmark datasets demonstrate that Fed-ADR's attack scheme can reduce global accuracy from over 90% to below 10%, bypassing several state-of-the-art defenses. When our detection and recovery modules are employed, they identify malicious clients and restore accuracy to over 90% within a few rounds, at a substantially lower cost than retraining from scratch--achieving a reduction of at least 20x in computational overhead.

---


### 43. [Super-Resolution of Solar Magnetograms via Adaptive Stratified Ensemble Learning with Uncertainty Estimation](https://arxiv.org/abs/2609.27131)

**<font color=#1a73e8>作者：</font>** Sina Norouzi Kandalan, Haodi Jiang, Jason T. L. Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-image super-resolution of Sun's photospheric magnetograms enables consistent analysis across heterogeneous space-based instruments and supports long-term studies of solar magnetic field evolution. We address the super-resolution task from SOHO/MDI (low-resolution) to SDO/HMI (high-resolution) line-of-sight (LOS) magnetograms using a modified RRDBNet architecture initialized by ESRGAN pretrained weights. Through systematic per-image diagnostic analysis, we identify image complexity as the dominant predictor of reconstruction errors. To exploit this finding, we introduce an adaptive stratified specialist ensemble (SSE) of three specialist networks with uncertainty estimation, where each specialist network is trained by images from three different complexity strata using a weighted random sampling strategy. During inference, a lightweight router based on input image statistics assigns each test image to the appropriate specialist network. Our experimental results demonstrate the good performance of the proposed ensemble and its superiority over closely related methods.

---


### 44. [MINER: Multi-crop INference-time Enhancement for Rare-Object Retrieval with Frozen Dual Encoders](https://arxiv.org/abs/2609.27142)

**<font color=#1a73e8>作者：</font>** Abdulmalik Alquwayfili, Faisal AlMeshal, Jumanah Almajnouni 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image retrieval with frozen dual encoders degrades when the query names a small, visually subordinate object in a cluttered scene: a single global image embedding underrepresents the localized visual evidence. We present MINER, a training-free inference framework that augments a frozen dual encoder's global image embedding with a small bank of region-level embeddings and a hubness-correcting similarity rescoring, recovering visual evidence that global pooling underweights. To evaluate this setting, we introduce ROCS, a benchmark built from high-clutter subsets of Flickr30K and MS COCO whose images are re-captioned to name a single low-salience object. Experiments on CLIP, SigLIP, and SigLIP 2 show that MINER improves retrieval on every backbone, on ROCS and on the standard splits. Analyses show that these gains come primarily from broader spatial coverage rather than precise crop placement, revealing a simple and general way to recover localized evidence from frozen representations. Code: this https URL. Dataset: this https URL.

---


### 45. [A Systematic Evaluation of Infrastructure-Based Radar System for Highway Traffic Monitoring](https://arxiv.org/abs/2609.27143)

**<font color=#1a73e8>作者：</font>** Tianheng Zhu, Woei-chyi Chang, Alamss Riaz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrastructure-based radar systems offer robust and long-range solutions for traffic monitoring, yet their detection and tracking performance under real-world conditions remains insufficiently evaluated. This study introduces DRaT (Drone and Radar Trajectories), a dual-modality dataset of naturalistic vehicle trajectories collected at a highway merging segment in Fort Worth, Texas, to systematically assess radar sensing performance against drone-derived ground truth. The performance is evaluated at three levels: individual vehicle detection, trajectory tracking, and macroscopic traffic parameter estimation. For individual vehicle detection, the radar achieves an overall precision of 78% and a recall of 57%, with degraded performance under congested traffic conditions and at longer distances. At the trajectory level, the radar demonstrates reasonably strong tracking performance (IDF1 = 0.699), maintaining reliable vehicle identities when tracks are successfully established. For macroscopic traffic flow metrics, the radar accurately estimates space-mean speed (MAPE < 4%) but underestimates density and volume by approximately 23% due to missed detections. The paper also discusses practical deployment considerations and potential downstream applications of roadside radar sensing systems. To support reproducible research on infrastructure-based sensing systems, we have open-sourced the DRaT dataset on Zenodo: this https URL.

---


### 46. [Learning Risk Scores Robust to Unobserved Confounders](https://arxiv.org/abs/2609.27144)

**<font color=#1a73e8>作者：</font>** Ryan Edmonds, Yingxiao Ye, Sina Aghaei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider the problem of learning risk scores to prioritize individuals for scarce resources or interventions, from historical observational data affected by unobserved confounding. Decisions about who receives scarce resources are often guided by risk scores based on recorded characteristics, such as responses to a survey. These risk scores are increasingly being learned directly from observational data: historical records of individuals' characteristics, allocation decisions, and outcomes. Standard methods such as inverse propensity weighting (IPW), which corrects for the bias introduced by the historical allocation policy, can be used to learn accurate risk scores if the historical decision process is fully explained by the recorded characteristics. In practice, however, historical decisions often depend on unrecorded information, causing learned risk scores to systematically under-prioritize exactly the individuals whose unrecorded circumstances drove past prioritization. We propose a method for learning risk scores that are robust to this kind of unobserved confounding, building on IPW. Since propensity weights cannot be reliably estimated under unobserved confounding, we instead treat them as belonging to an uncertainty set determined by the observable data and domain-informed estimates of the degree of confounding, combining sensitivity analysis from causal inference with Wasserstein distributionally robust optimization. The resulting robust risk score learning problem admits a sample-based approximation that we reformulate as an exponential cone program compatible with off-the-shelf solvers. We demonstrate the effectiveness of our approach on semi-synthetic data derived from datasets in the UCI Machine Learning Repository. Our method improves calibration by up to 29.2% over traditional benchmarks and up to 11.1% over the state of the art, without compromising other metrics.

---


### 47. [Temporally Ordered Region-Token Mamba with Logit-Space Diffusion for Remote Sensing Change Detection](https://arxiv.org/abs/2609.27149)

**<font color=#1a73e8>作者：</font>** Anuvab Sen, Maneet Chatterjee, Aparup Ghosh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing change detection requires both global reasoning across bitemporal images and precise localization of changed regions. However, dense attention is computationally expensive for high-resolution imagery, while conventional feature fusion and coarse decoding may inadequately separate genuine changes from appearance variations or preserve object boundaries. We present Bitemporal Mamba-Diffusion for Change Detection (BMD-CD), which combines temporally structured state-space modeling with logit-space diffusion refinement. BMD-CD converts deep bitemporal features into region tokens and arranges them in explicit temporal partitions before bidirectional state-space propagation. Its Bitemporal Ordered Mamba Operator enables long-range cross-temporal interaction with linear sequence complexity, while Orthogonal Feature Disentanglement forms a change-oriented output and a complementary rotated output using learned pairwise rotations and unchanged-region consistency. Multiscale decoding then produces coarse change logits, which are refined through a five-step Conditional Diffusion Decoder operating directly in logit space. Experiments on LEVIR-CD, WHU-CD, DSIFN-CD, CDD, and S2Looking demonstrate strong performance across diverse change-detection settings. BMD-CD achieves F1 scores of 93.7%, 96.0%, 97.8%, and 99.0% on the four standard benchmarks and improves 3-pixel Boundary-F1 to 87.7% and 91.4% on LEVIR-CD and WHU-CD, respectively. The full model requires 32.09 GFLOPs and 47 ms per 256 x 256 image pair, while also showing zero-shot transfer to ValaisCD and B-FLAIR-test. Our code is available at this https URL

---


### 48. [The Linear Representation Hypothesis Needs a Group Action](https://arxiv.org/abs/2609.27158)

**<font color=#1a73e8>作者：</font>** Louie Hong Yao, Yuhao Li, Shengchao Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To make claims about representations that generalize beyond a particular trained model, we need to specify when two representations should count as equivalent. The Linear Representation Hypothesis is often discussed without making this equivalence explicit. Different notions of equivalence preserve different structures, so metrics, probes, and interventions that appear to study the same representation may in fact correspond to different hypotheses. We therefore argue that the Linear Representation Hypothesis is not one hypothesis but a family of claims distinguished by representation equivalence. We formalize this idea using group actions, specifying the representation object, the procedure that produces it, and the property ultimately asserted, while accounting for equivalences imposed by the model architecture. This framework clarifies how assumptions can change across metrics, reading points, and analysis stages, and we use it to audit common representation quantities and recent interpretability analyses.

---


### 49. [Beyond Overlap: Estimating the Causal Effect of Benchmark Exposure](https://arxiv.org/abs/2609.27176)

**<font color=#1a73e8>作者：</font>** Divyansh Singh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evidence that evaluation material entered training does not reveal how much it affected evaluation. This distinction leaves a contaminated benchmark score difficult to interpret: provenance can establish contact, but only a counterfactual can quantify the performance attributable to that contact. We present LeakScale, an interventional framework for estimating this missing quantity. LeakScale creates fresh executable tasks that require private, family-specific information absent from and non-derivable from the public task, controls access to that information, and estimates the resulting control-adjusted change in executable accuracy. Across 2,048 unique families, two model families, two executable domains, and 262,144 generations, exposure improves accuracy in every model-by-domain combination, with gains ranging from +7.17 to +27.31 percentage points. These findings separate two empirical questions that are often conflated: whether benchmark contact occurred and how strongly a reported score depends on it. LeakScale makes the latter directly measurable.

---


### 50. [Data-driven discrete-time deep recurrent neural network-based modeling for dissipative systems](https://arxiv.org/abs/2609.27186)

**<font color=#1a73e8>作者：</font>** Tuan Luong, Hyungpil Moon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physical AI has gained increasing attention for its role in developing AI systems that better understand, predict, and control real-world dynamics. Achieving this requires AI models that not only achieve high prediction accuracy but also preserve fundamental physical properties of dynamical systems. In this paper, we propose a deep discrete-time dissipative recurrent neural network (DissipNet) that explicitly enforces dissipativity, a key property related to stability and energy dissipation, through structural weight constraints and a dedicated training algorithm. By construction, the proposed network is capable of learning dissipative dynamics while preserving their inherent stability, which is formally analyzed using Lyapunov theory. In contrast to Physics-Informed Neural Networks (PINNs), which incorporate governing equations into the training loss but do not guarantee preservation of internal analytical properties such as dissipativity or passivity, our approach provides explicit guarantees on stability at the model level. We demonstrate the effectiveness of the proposed method through several modeling applications, and compare its performance with a naive recurrent neural network (RNN) and a PINN-based model.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-240](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
