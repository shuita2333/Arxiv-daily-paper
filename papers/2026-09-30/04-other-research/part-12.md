# 📦 其他研究 | 2026年09月30日

> 本类共 **908** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**551-600**（第 12/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | **551-600** | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-908](./part-19.md)

---

### 551. [PerceptFence: Content-Mediation Architecture and Deterministic Coverage for Screen-Share AI Assistants](https://arxiv.org/abs/2609.34027)

**<font color=#1a73e8>作者：</font>** Asmita Negi, Neeraj Kumar Singh Beshane  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Live screen-share AI assistants observe raw screen and speech streams, but users have little runtime control over what an assistant may observe, retain, or disclose. Prompt-level privacy settings are insufficient because sensitive content enters through the capture stream. We present PerceptFence, a content-layer mediation architecture between capture, memory, and model responses, with a deterministic synthetic-fixture scaffold; the artifact omits live capture, category inference, authenticated re-consent, cross-session state, and an external model adapter. On 9,600 protocol-documented adversarial strings scored by a separately implemented exposure oracle, PerceptFence neutralises 0.828 of digit-PII payloads on the 5 seeds both systems run, versus 0.183 for Microsoft Presidio; outside that family Presidio leads 0.238 to 0.154, so the overall 0.398 to 0.260 comparison is only indicative. We then evaluate the path a deployed assistant uses: 480 synthetic developer-support screens rendered by Chrome, degraded, and read by OCR, with rules frozen before testing and three screen types held out. PerceptFence neutralises 889 of 968 OCR-surviving secrets and PII values (0.918; Wilson 95% 0.899-0.934) against 0.581 for Presidio and 0.179 for gitleaks, and 0.974 on the held-out screen types, at a measured cost of 0.763 task-token retention on those types. The contribution is a documented mediation architecture and an evaluation method with explicit coverage boundaries, not a claim of live deployment, formal privacy, novel redaction primitives, or general model robustness.

---


### 552. [Posterior Regimes and Latent Deception: Variational Bayesian Inference in Hidden Markov Models for Sequential Fraud Detection in Financial Transactions](https://arxiv.org/abs/2609.34031)

**<font color=#1a73e8>作者：</font>** Joseph Uririoghene Obukofe, Anthony O'Hare, Chioma Sandra Dike  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a three-tier progression of Hidden Markov Models: maximum-likelihood (Baum-Welch), variational Bayesian (VBEM), and a neural variational extension (Neural VBEM), that model each customer's transaction history as a trajectory through a small number of latent behavioural regimes, one of which is empirically identified as fraud-associated. The Neural VBEM HMM replaces the fixed Gaussian-multinomial emission family with a learned encoder, compressing a 741-dimensional transaction representation into a 64-dimensional latent space in which the VBEM HMM's posterior operates; a UMAP projection of this space reveals that the discovered regimes are not discrete clusters but ordered segments of a single continuous behavioural manifold, with confirmed fraud concentrated at its extreme. We show that the model's natural output, that is, the posterior probability of regime membership, is routinely mistaken for a fraud probability, and quantify the resulting miscalibration (the regime-membership interpretation error, MRIE); a corrected posterior-predictive score, closes most of this gap. We further distinguish batch (smoothed) inference, which uses look-ahead unavailable at deployment time, from filtered (forward-only) inference, and report both. On IEEE-CIS transaction data, the neural tier achieves a 14.4$\times$ fraud enrichment in its identified regime; while its AUPRC trails a discriminative XGBoost baseline, we show this gap is structural and not incidental, and argue the model is best positioned as a calibrated triage and interpretability layer rather than a drop-in ranking replacement.

---


### 553. [Re:Cognize -- Open-Set Comic Character Re-Identification](https://arxiv.org/abs/2609.34032)

**<font color=#1a73e8>作者：</font>** Aaditya Baranwal, Madhav Kataria, Yogesh S Rawat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A manga reader meets a character on one page and knows them on sight a hundred pages later, without ever being handed a cast list. Re-identifying comic characters demands the same, open-set and sequential: pages arrive as a stream in reading order, new faces appear before anyone names them, and the cast is assembled as the story is read. $\textbf{Re:Cognize}$ evaluates recognition as the story is read, not against a cast handed over in advance: four protocols on one query stream, from closed-set retrieval to a cast the model must build and grow itself. The surprise is where models fail. Recognising is close to solved: one reference image per character already ranks as well as a gallery built in advance. Knowing what to believe is not: a model that adds its own matches makes its cast worse, while the same growth with correct labels would gain over twenty points of top-1 accuracy. The bottleneck is acceptance, not vision, and one comparison decides it: an addition pays exactly when it is right more often than the cast already was on the queries it takes over. The comparison has nothing to fit, and measured on half of a new corpus it calls the other half correctly. $\textbf{ReCast}$ puts it to work with nothing fitted on data: a cast sheet of one running average per character, grown only where the page itself vouches for a crop. It recovers a third to two thirds of what perfect labels would, depending on whether the cast starts from random examples or from first appearances. Re:Cognize measures whether a model can read along; ReCast is a cast that does. Our claims are on identity maintenance, recognising characters already met; the emergence of new ones is measured as a diagnostic under a fixed reference rule, and we propose no method for it.

---


### 554. [3D Point Tracking with State Space Models](https://arxiv.org/abs/2609.34035)

**<font color=#1a73e8>作者：</font>** Masahiro Ogawa, Qi An, Atsushi Yamashita  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tracking any point of a dynamic scene in metric 3D - in absolute meters, not up to an unknown scale - underpins 3D and 4D reconstruction, robot navigation, and autonomous driving, where decisions are made in meters, not pixels. Our objective is a 3D point tracker accurate in those absolute terms and operating within a single commodity GPU, pose-free, monocular budget. Our method rests on one observation: once a point's 2D image trajectory is fixed, the quantity that governs its metric accuracy is the depth along its pixel ray. Rather than learning tracking end-to-end, we therefore compose two frozen front-ends - dense optical flow for 2D correspondence and a monocular metric-depth network for the third dimension - and learn only the residual they cannot supply: that depth, refined by a compact state space model (Mamba-3) conditioned on appearance features (DINOv3). A state space model rather than the transformers the strongest 3D trackers adopt is what makes a single-GPU budget attainable: it summarises a track in a fixed-size recurrent state whose memory cost is constant in the number of frames, whereas attention requires a key-value cache that grows linearly with them. On the TAPVid-3D minival benchmark our best configuration attains the highest absolute metric accuracy among methods evaluated under identical conditions (mean metric Average Jaccard, 0.256), exceeding strong feed-forward trackers, while a companion analysis, reproduced with each competitor's own evaluator, explains why several published trackers lose most of their accuracy under this budget.

---


### 555. [ARCH-B: Architectural Representation, Comprehension and Hierarchy Benchmark](https://arxiv.org/abs/2609.34047)

**<font color=#1a73e8>作者：</font>** Kieran Sagar Parikh, Jose Luis Garcia del Castillo y Lopez  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal models increasingly interpret visual environments, but their ability to recognize the same building across photographs, floor plans, elevations, sections, and renderings remains poorly characterized. We introduce ARCH-B, a benchmark of 354 four-choice questions across 11 cross-representational archetypes, constructed from a building-linked corpus of 3.9 million architectural images using visually similar distractors, model-guided difficulty screening, and manual validation. We evaluate 25 multimodal models and collect 5,830 responses from non-expert human participants. Model accuracy ranges from 10.45% to 83.90%, compared with a human baseline of 35.35%. Models perform comparatively well on mixed-representation outlier detection and photograph matching, but remain weaker on floorplan-to-photograph correspondence. Human and model difficulty across archetypes is only weakly correlated (Spearman's (\rho=0.33)). Held-out evaluation confirms that the difficulty identified during screening generalizes beyond the curation models. ARCH-B provides a diagnostic evaluation of visual correspondence and representation transfer across architectural media.

---


### 556. [FLARE: Flow Matching with Local Axis-Angle Representations for Stochastic Micromagnetic Evolution](https://arxiv.org/abs/2609.34070)

**<font color=#1a73e8>作者：</font>** Pengyu Li, Renjie Tong, Xuanlue Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon micromagnetic simulation remains expensive because conventional and learned solvers typically propagate Landau--Lifshitz--Gilbert (LLG) dynamics step by step. Existing learned approaches generally retain stepwise integration or model deterministic evolution, leaving full-field, direct-horizon stochastic prediction largely unexplored. We propose FLARE, a flow-matching framework that recasts stochastic finite-time magnetization prediction as conditional transport over anchor-relative local axis-angle rotations. This rotation-space formulation respects the intrinsic geometry of magnetization dynamics and preserves pointwise unit norm by construction. By explicitly conditioning on the physical prediction horizon, FLARE directly generates full-field stochastic endpoints across multiple target times without stepwise integration. Against the strongest single-checkpoint external baseline on each metric, FLARE achieves 29.9% lower angular energy distance ($15.30^\circ$), and a 37.3% lower fair energy score (0.393). On a representative composed 5-ns two-segment protocol, FLARE achieves a $3{,}062\times$ best-batch speedup over the widely used GPU micromagnetic solver MuMax$^3$ on a single GPU.

---


### 557. [SNaP: One-Step Posterior Sampling for Noisy Inverse Problems](https://arxiv.org/abs/2609.34071)

**<font color=#1a73e8>作者：</font>** Shirin Shoushtari, Edward P. Chandler, Xiao Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion and flow-matching models can produce high-quality posterior samples for inverse problems, but typically require tens to thousands of network evaluations per draw. MeanFlow enables one-step generation, yet applying it to inverse problems leaves no intermediate steps at which to enforce measurement consistency. We introduce SNaP, a one-step MeanFlow posterior sampler for linear inverse problems with Gaussian noise. Its central innovation is a measurement-adapted source: a Gaussian distribution whose mean and anisotropic covariance are determined by the measurement operator, observation, and noise level. The source anchors well-measured directions while preserving variation where the measurements are weak or uninformative. We show that the exact conditional flow transports this source to the true posterior. Across natural-image restoration and multi-coil MRI, SNaP produces diverse, high-quality samples with one network evaluation per draw, 30 to 2250 $\times$ faster than iterative samplers.

---


### 558. [WhiteCon: Semi-Supervised Domain Adaptation Regression Through Whitening Transform and Dual Consistency](https://arxiv.org/abs/2609.34078)

**<font color=#1a73e8>作者：</font>** Se Jin Sim, Seoung Bum Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Domain adaptation is crucial for addressing distributional shifts that degrade model performance across domains. While most existing research has centered on classification, semi-supervised domain adaptation regression (SSDAR) for continuous-output tasks remains largely unexplored, particularly in practical scenarios with limited labeled target data. To address this gap, we propose semi-supervised domain adaptation regression through whitening transform and dual consistency (WhiteCon), which combines domain-specific whitening transform (DWT) and dual consistency regularization to enhance training stability and domain adaptation. DWT reduces the variance of the model parameters by transforming the feature covariance matrix into an identity matrix, thus stabilizing training under ordinary least squares assumptions. In addition, variance consistency regularization, as part of dual consistency regularization, aligns the variances of weak, strong, and mixup-augmented features to improve resilience against augmentation-induced perturbations. Empirical evaluations on various benchmark datasets under SSDAR settings demonstrate that the proposed WhiteCon achieves state-of-the-art performance compared to existing methods, effectively addressing domain shifts in regression tasks. The code for WhiteCon is available at this https URL.

---


### 559. [Beyond One Epoch: Uncertainty-Weighted Sensitivity Regularization for Recommendation Models](https://arxiv.org/abs/2609.34083)

**<font color=#1a73e8>作者：</font>** Richard Lettich, Shagun Gupta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recommendation models with sparse embeddings and a shared consumer often exhibit the one-epoch phenomenon: a second epoch lowers training loss while sharply degrading generalization. We present a view based on the violation of the prequential principle. On the first epoch, an example's label has not affected the embedding rows used to score it. On later epochs, those rows contain a displacement induced by the labels earlier update. This creates an incentive for the shared consumer to exploit this displacement in subsequent epochs, which fails to generalize. We call this self-influence asymmetry. Using an exact scalar model and local influence analysis, we connect this mismatch to the uncertainty in the embeddings and the consumers incentive to exploit it in subsequent epochs. We verify this hypothesis using an embedding-consumer-update interventions in deep recommendation models and propose uncertainty-weighted sensitivity regularization (UWSR) which counteracts this mismatch by augmenting the loss function to penalize the consumer for relying on uncertain embeddings. Unlike existing remedies, UWSR preserves the learned embeddings and across three benchmarks, four-epoch UWSR reduces test cross-entropy by 1.38%-6.78% and improves AUC by 0.0058-0.0231 relative to one-epoch training.

---


### 560. [Evaluating Machine Unlearning in ASR](https://arxiv.org/abs/2609.34092)

**<font color=#1a73e8>作者：</font>** Diogo Dinis, Francisco Teixeira, Bhiksha Raj 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Machine unlearning (MU) offers a path to compliance with "right to be forgotten" regulations. While MU has received increasing attention for speech tasks, it remains largely unexplored for Automatic Speech Recognition (ASR). In this work, we investigate whether existing MU algorithms and evaluation tools are suitable for ASR. We apply several MU techniques to an ASR model, evaluating privacy-utility trade-offs for single-subject unlearning, then assess the best algorithm under sequential and simultaneous unlearning. Results show that gradient ascent-based algorithms achieve strong utility-privacy trade-offs, whereas more complex approaches over-unlearn samples, making them easier to identify as unlearned. This suggests standard privacy evaluations based on simple Membership Inference attacks are insufficient to reliably assess unlearning success, motivating improved evaluation methods for MU in ASR. Finally, we show that both sequential and simultaneous unlearning yield worse privacy and utility than single-subject unlearning, underscoring the need for unlearning constructions better suited to these settings.

---


### 561. [Beyond Correctness: Evaluating Semantic Knowledge in Cross-Table Transfer](https://arxiv.org/abs/2609.34098)

**<font color=#1a73e8>作者：</font>** Seokyong Sheem, Hochang Lee, Suyeong Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Semantic knowledge is increasingly used to bridge heterogeneous schemas in tabular learning, but how much does that knowledge actually improve prediction? Studies in tabular learning commonly answer this question through semantic ablations that modify or suppress the supplied semantic knowledge. We show that these ablations can lead to misleading conclusions about predictive benefit: poor performance under altered semantics may be taken as evidence that the intended knowledge is beneficial. Across real and controlled experiments, altering semantic content can produce large performance differences even when the model gains little predictive benefit from having that semantic knowledge in the first place. To separate these effects, we distinguish two quantities: content sensitivity and predictive utility. Content sensitivity measures the change in performance when semantic content is altered, whereas predictive utility measures the benefit of the intended semantic knowledge relative to a suitable reference without that knowledge. This distinction motivates an evaluation framework in which the control is chosen according to the question being asked: altered controls assess sensitivity to semantic content, whereas claims that semantic knowledge improves prediction require a suitable reference. Even then, predictive utility is not fixed; it varies across suitable references and decreases when the reference can more easily recover the tested knowledge from other inputs or labeled examples. In a bounded audit of 25 semantic-ablation comparisons across nine studies, only one of 18 explicit predictive-utility claims is paired with a control that clearly isolates the tested semantic contribution. Together, these findings motivate a simple evaluation principle: semantic-ablation controls should be chosen and interpreted according to the question they are intended to answer.

---


### 562. [A Differentiable Optimization Framework for Registering Sequential Bounding Boxes with Point Cloud Stream](https://arxiv.org/abs/2609.34103)

**<font color=#1a73e8>作者：</font>** Xuesong Li, Jinguang Tong, Jie Hong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Refining a sequence of coarse 3D bounding boxes against a LiDAR point-cloud stream demands tracks that are geometrically accurate (high IoU) and temporally coherent (low roughness), preferably without training data. The usual recipe keeps the two concerns apart: register each frame independently, then smooth the trajectory afterwards with a Kalman~RTS or Savitzky--Golay filter. Smoothing displaces boxes from a geometric optimum and never re-optimises, so it trades accuracy for smoothness. We instead fold the temporal smoothness constraint into a training-free registration objective and solve for all poses jointly with L-BFGS. The payoff depends on how well the object is seen. On well-observed tracks it is large: within the low-roughness budget, the joint objective beats both post-hoc smoothers on paired multi-seed statistics and cuts roughness several-fold relative to frame-wise registration at matched accuracy. Treating visibility as an experimental variable exposes the limit. The advantage decays monotonically as views become one-sided, until it is indistinguishable from zero for near-edge-on objects and slightly negative under a ray-cast simulator with range-dependent density and ego motion, where the decoupled pipeline is in fact ahead at tight roughness budgets. We locate that boundary and trace it to one term: orientation alignment ties yaw to the estimated velocity and fails once that estimate is noisy. A ground-truth-free rule can choose the temporal scale and keep every track inside the roughness budget.

---


### 563. [The Devil is in the Spectrum Bias: Spectrum-Balanced Feature Matching for Robust Representation Distillation](https://arxiv.org/abs/2609.34106)

**<font color=#1a73e8>作者：</font>** Kuniaki Saito, Yoshitaka Ushiku  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large visual foundation models have demonstrated remarkable transferability across a wide range of downstream tasks. To deploy such models efficiently, feature matching has become a popular knowledge distillation approach that transfers teacher representations to smaller student models without requiring labeled data. However, we show that the conventional feature matching objective with L2-distance is inherently biased toward reconstructing dominant spectral directions of the teacher representation, while under-optimizing low-variance directions that often contain task-relevant information. To address this, we propose Spectrum-Balanced Feature Matching, SpecMatch, a simple objective that adaptively emphasizes under-optimized spectral directions while preserving the relative importance of dominant directions. SpecMatch is easy to implement and introduces negligible computational overhead. Extensive experiments on image recognition demonstrate that SpecMatch consistently improves downstream adaptation across diverse tasks, including image classification, anomaly detection, medical image analysis, and domain generalization. In particular, SpecMatch outperforms conventional feature matching in 40 of 42 teacher--student and training-setting combinations, while consistently improving over the original student model in all settings. We further demonstrate that the proposed objective generalizes beyond vision, improving downstream performance across six protein understanding tasks.

---


### 564. [SpecRegMatch: Robust Semi-Supervised Regression for Vehicle Interior Noise Prediction](https://arxiv.org/abs/2609.34111)

**<font color=#1a73e8>作者：</font>** Sejin Sim, Jinsoo Bae, Seoung Bum Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of artificial intelligence has observed increased application in predicting vehicle interior noise levels within the automotive industry. However, the collection of labeled data for training models in this context involves significant costs. Previous studies in semi-supervised regression (SSR) have effectively mitigated the reliance on labeled data by incorporating unlabeled data. Nonetheless, these approaches often introduce a high computational cost due to the training of multiple models and data sampling. This study introduces SpecRegMatch, a novel SSR method aimed at addressing the computational cost associated with training by leveraging a single model, thus eliminating the need for multiple data samplings. SpecRegMatch integrates consistency regularization and information maximization to robustly train the model, achieved through various augmentations applied to both the embedding vectors and predicted values. Experimental results demonstrate that SpecRegMatch achieves state-of-the-art performance across various scenarios, even when using a single model. It attains a remarkable performance, as indicated by an R^2 score of 0.434. This is especially noteworthy in scenarios where labeled data is scarce. You can access the code for our proposed method at this https URL.

---


### 565. [GUITAR: Structured Failure Diagnosis of GUI Agents via State Transitions](https://arxiv.org/abs/2609.34113)

**<font color=#1a73e8>作者：</font>** Shaoqing Zhang, Kehai Chen, Xuefeng Bai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding where and why Graphical User Interface (GUI) agents fail is essential for building more reliable systems, yet current evaluation relies on step accuracy, a metric that treats each screen independently and overlooks the underlying structure of GUI environments. This leads to two critical blind spots: (1) functionally equivalent screens are evaluated in isolation, obscuring systematic failure patterns across shared screens; and (2) the long-tailed GUI distribution renders failures on rare but critical screens invisible under standard metrics. To address these issues, we propose \textbf{GUITAR}, a state-centric diagnostic framework that performs structured failure analysis over both states and transitions, using a State Transition Graph (STG) by mapping visually diverse screens to shared functional states. Across 8 agents and 6 tasks from AndroidControl and Mind2Web, GUITAR reveals that 60.4\% of failures occur in 20\% of states, localizing errors to a small set of bottlenecks. Bottleneck-targeted guidance improves SR by 2.8\% and retains a 1.88\% average gain across 7 agents under three-fold trajectory-held-out evaluation with fully automatic STGs. These findings demonstrate the diagnostic and actionable value of structure-aware evaluation within the evaluated mobile and web tasks. Code is available at this https URL

---


### 566. [Evolution of fairness in multi-objective reinforcement learning framework](https://arxiv.org/abs/2609.34114)

**<font color=#1a73e8>作者：</font>** Jingyi Zhang, Xin Ou, Guozhong Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fairness, as a fundamental social norm, continues to pose a longstanding puzzle regarding its emergence. Traditional game-theoretic models largely rely on the assumption of \emph{Homo economicus}, wherein individuals are purely rational and self-interested, acting solely to maximize material payoffs. Such accounts, however, overlook the multidimensional nature of human decision-making, which is often shaped also by other considerations beyond economic incentives. To address this gap, we propose a multi-objective reinforcement learning framework that models the evolution of fairness as a dynamic trade-off between material payoff maximization and fairness-driven moral behavior, regulated by a fairness pressure coefficient. Using simulations of a two-objective Q-learning ultimatum game, we find that increased fairness pressure promotes fair outcomes, as expected. Strikingly, however, under moderate pressure, responder behavior reverses: responders become ``forgiving" by accepting low offers -- a pattern in line with our daily experience. Microscopic analyses reveal that this strategy reversal stems from competition between payoff-maximizing and fairness-oriented preferences. We further extend our framework to an asymmetric setting, where proposers and responders assign different weights to the two objectives. Overall, our work expands the reinforcement learning paradigm from a single-objective to a multi-objective formulation, offering a versatile tool for elucidating a broader range of human social behaviors.

---


### 567. [Probabilistic electrical power demand forecasting with uncertainty quantification](https://arxiv.org/abs/2609.34120)

**<font color=#1a73e8>作者：</font>** Mahesh Neupane, Pragya Dhungana, Pradip Khatri 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The majority of research on electricity consumption forecasting has focused on deterministic approaches, which generate a single point estimate for each time step in the forecasting horizon. However, the increasing penetration of renewable energy sources and the growing complexity of modern smart grids have introduced greater variability and uncertainty into power-system demand and operation. Consequently, probabilistic forecasting, which quantifies the uncertainty and variability associated with future electricity demand, is becoming increasingly important for reliable power-system planning and operation. This study presents an empirical comparison of four contemporary probabilistic forecasting models for electricity consumption, highlighting their respective strengths and limitations. We have performed comparision on real-world power systems related datasets. Across all power-consumption zones, NGBoost demonstrates superior probabilistic forecasting performance, achieving the lowest MAE and RMSE while providing well-calibrated uncertainty estimates with high prediction-interval coverage and reasonably narrow intervals. These results indicate that NGBoost offers a more accurate and reliable forecasting framework than Bayesian, Monte Carlo (MC) Dropout, and Gaussian Process Regression (GPR) models for the considered electricity consumption data.

---


### 568. [What Does a Stream Model Buy You in Flow Matching?](https://arxiv.org/abs/2609.34123)

**<font color=#1a73e8>作者：</font>** Jian Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stream-level flow matching replaces the linear interpolant of conditional flow matching (CFM) by a Gaussian-process (GP) stream connecting each source--target pair, and reports lower sample error than \icfm{} on 2-Gaussian, MNIST and CIFAR-10 benchmarks. We ask what such a stream model actually contributes. Three results answer the question. (i)~\emph{Reduction.} The stream-level CFM objective depends on the stream law only through the per-time joint law of $(s_t,\sdot_t)$, so the conditional paths a Gaussian stream can reach are exactly the Gaussian conditional paths CFM already parametrises; in the coordinate-wise, shared-scalar-kernel construction gpcfm actually uses, the entire design space collapses to two scalar curves $(m_t,v_t)$, and cross-time covariance affects only estimator variance. (ii)~\emph{The GP is a constrained chart of that space.} One kernel sets both $m_t$ and $v_t$, so the paper's own recipe for widening coverage-shrinking the SE length-scale---destroys the interpolant (the midpoint mean weight falls from $1.03$ to $0.00$). On the 2-Gaussian benchmark this makes the GP chart diverge on $15/200$ runs at high coverage against $0/200$ for a decoupled $(m_t,v_t)$ chart ($p=6.6\times10^{-5}$), and crossing the two curves shows the divergence tracks the mean, not the variance. On MNIST the same sweep does not diverge and the ordering reverses, so whether the coupling is harmful is benchmark-dependent; what holds on both is that the recipe buys nothing---no coverage level beats the paper's own, and past $\max_t\sqrt{v_t}\approx0.6$ both charts degrade. (iii)~\emph{Audit.} The released code does not implement the mechanism it describes: state and velocity are drawn independently ($\mathrm{corr}=0.00\pm0.01$ against an intended $\pm0.83$--$0.99$).

---


### 569. [PrefLUT: Reusable and Refinable Personalized Color Editing from Pairwise Preferences](https://arxiv.org/abs/2609.34133)

**<font color=#1a73e8>作者：</font>** Chuanzhi Xu, Langyi Chen, Chengkun Yue 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Photographic color editing is inherently personal: the same image can appear too warm, too muted, or already satisfactory to different users. Most lookup table (LUT) and reference-guided methods target a specified appearance rather than model persistent preferences from repeated user choices. To address this gap, we introduce PrefLUT, a reusable and refinable user-preference modeling framework for deployable 3D LUTs, encoding ordered preferred/non-preferred image pairs into a lightweight Reusable User Profile that is reused across queries and refined using additional user preference pairs, without per-user optimization. A Query-Conditioned LUT Predictor combines this profile with each image to predict a LUT latent vector and edit strength. An Identity-Residual LUT Decoder and Edit-Strength Controller then produce an exportable 3D LUT. Experiments on three datasets demonstrate effective personalized editing and general-purpose enhancement. Each quantized profile requires only 260 bytes, and editing takes 1.365 ms/image on an RTX 5090 GPU. We also introduce the Preference-Conditioning Verification Protocol (PCVP), an evaluation protocol to verify whether personalized image edits depend on user preferences and the query image through controlled changes to user profiles, preference orders, pair correspondences, and query images.

---


### 570. [You Can't Have It Both Ways: Concept Entanglement Limits Diffusion Model Unlearning](https://arxiv.org/abs/2609.34137)

**<font color=#1a73e8>作者：</font>** Yian Wang, Ali Ebrahimpour-Boroojeny, Hari Sundaram 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Concept unlearning in text-to-image diffusion models aims to suppress a target concept (e.g., \texttt{horse}) while preserving related but distinct content (e.g., \texttt{donkey}), yet existing methods either leak under indirect prompts or visibly degrade other concepts. We show that these failure modes stem from the geometry of concept representations rather than from any particular algorithm. Formalizing concepts as activation-space regions, we prove that the overlap between a target and other concepts lower-bounds the damage any robust erasure must inflict on them, with the trade-off scaling linearly in the degree of overlap. Across thirteen unlearning methods, including methods designed to preserve non-target concepts, no method achieves both strong erasure and strong neighbor preservation: STEREO nearly eliminates indirect leakage but cuts neighbor generation by more than 75\%, while sparse inference-time methods preserve neighbors but leak. Damage increases with our overlap measure, monotonically so for STEREO; the $\kappa$-scaling reproduces on SDXL, and neighbor-selective damage recurs on FLUX. Perfect unlearning is the wrong target for entangled concepts; methods should be evaluated on the Pareto frontier our theorem establishes.

---


### 571. [Word Similarity Datasets for Indian Languages: Annotation and Baseline Systems](https://arxiv.org/abs/2609.34138)

**<font color=#1a73e8>作者：</font>** Syed S. Akhtar, Arihant Gupta, Avijit Vajpayee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With the advent of word representations, word similarity tasks are becoming increasing popular as an evaluation metric for the quality of the representations. In this paper, we present manually annotated monolingual word similarity datasets of six Indian languages - Urdu, Telugu, Marathi, Punjabi, Tamil and Gujarati. These languages are most spoken Indian languages worldwide after Hindi and Bengali. For the construction of these datasets, our approach relies on translation and re-annotation of word similarity datasets of English. We also present baseline scores for word representation models using state-of-the-art techniques for Urdu, Telugu and Marathi by evaluating them on newly created word similarity datasets.

---


### 572. [Long-Term Operational Planning Using Scenario-Based System Load Forecasting](https://arxiv.org/abs/2609.34140)

**<font color=#1a73e8>作者：</font>** Akash Debnath, Shiuli Subhra Ghosh, Jaime De La Ree 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid expansion of hyperscale data centers is significantly increasing electricity demand in Northern Virginia. Dominion Energy, the region's primary electric utility, must reinforce its transmission network to support this growth. These projects require planned outages that must be evaluated months in advance to support construction planning and outage coordination while meeting NERC and PJM N-1 reliability requirements. Long-term outage studies are commonly performed day by day using monthly or seasonal peak-load assumptions. Although this approach simplifies analysis, it can be overly conservative because it does not capture granular load variability. Consequently, short-duration outages that may be feasible under realistic loading conditions are often postponed or denied, delaying critical transmission expansion and grid modernization projects. This paper evaluates the operational value of incorporating realistic multigranular load forecasts into long-term, contingency-based outage assessments and compares the results with conventional peak-based methods. Daily, weekly, and monthly forecasts are developed using statistical and machine-learning models, including SARIMA, Prophet, Gradient Boosting, and Random Forest, followed by bottom-up temporal reconciliation to maintain consistency across forecast horizons. Results show that granular load forecasts reduce unnecessary conservatism and improve outage accommodation, particularly for short-duration requests, without changing existing reliability criteria. The proposed approach can strengthen long-term outage coordination and support timely transmission reinforcement and grid modernization.

---


### 573. [Analytical and Convolutional Neural Network-Based Motion-Vector Propagation for Efficient Video Object Detection](https://arxiv.org/abs/2609.34142)

**<font color=#1a73e8>作者：</font>** Ashiyana Abdul Majeed, Mahmoud Meribout, Neethu Joseph  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continuous video analytics requires accurate localization at low latency within embedded power budgets. This paper presents a hardware-software design methodology that reuses codec motion vectors (MVs) between detector invocations. Two alternative models support translation and scale changes: analytical motion-vector propagation (Analytical-MV) and learned propagation using a convolutional neural network (CNN) (CNN-MV). The learned model uses convolutional operations and independent object updates suited to parallel execution on an edge graphics processing unit (GPU). Analytical-MV combines a harmonic-mean precision-recall score (F1) of 0.909 with a mean end-to-end latency of 9.03 ms and an energy consumption of 0.177 J per frame, yielding the lowest latency and energy among the evaluated configurations. Relative to detection on every frame, it reduces mean latency by 25.9% and energy per frame by 36.4%. CNN-MV offers a different trade-off: its fastest configuration raises recall from 0.871 for Analytical-MV to 0.890 and lowers mean power from 19.64 to 17.32 W, while achieving a latency of 18.42 ms and an energy consumption of 0.319 J per frame. It is therefore useful when recall or operating power is more important than minimum latency and energy. Execution on a deep learning accelerator (DLA) further reduces time-averaged GPU utilization relative to GPU execution. Host-processing optimization substantially improves both latency and energy, demonstrating the value of jointly designing temporal models and their execution pipelines.

---


### 574. [Beyond Geometry: Benchmarking and Consistency Reasoning for 3D Logical Anomaly Detection](https://arxiv.org/abs/2609.34143)

**<font color=#1a73e8>作者：</font>** Zhiqiang Qin, He Xie, Junfei Yi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing 3D industrial anomaly detection mainly targets local geometric deviations. In contrast, many industrial anomalies violate object-level design or assembly rules, which we define as 3D logical anomalies. To address these challenges, we introduce the Industrial Logical Anomaly Detection Dataset (ILGAD), the first scalable benchmark dedicated to logical anomalies in industrial point clouds. ILGAD contains 2,774 samples from 15 categories with point-level annotations and covers existence, specification, pose, and assembly-state errors. To detect such 3D logical anomalies, we propose a consistency reasoning framework that assesses whether local geometry, structure coverage, and spatial relations conform to the normal design. The framework detects geometric changes, unsupported expected structures, and abnormal local arrangements. Experiments on ILGAD, Anomaly-ShapeNet, and IEC3D demonstrate superior object-level detection and point-level localization, showing that the framework effectively detects logical anomalies and generalizes to conventional geometric defects.

---


### 575. [CAST: Reconstruction-Coupled Acceleration of Interactive World Models](https://arxiv.org/abs/2609.34144)

**<font color=#1a73e8>作者：</font>** Leyang Chen, Junyi Wu, Fanqing Kong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive world models must respond quickly to controls while preserving scene consistency. Existing acceleration methods can miss heterogeneous control responses and spatial transport when recovering skipped features. We observe that interaction-induced feature changes correlate with approximation error, while low-frequency interpolation errors are phase-sensitive and show more predictable phase progression. These findings motivate CAST, a reconstruction-coupled inference framework. CAST selects anchors by interaction sensitivity and cross-layer coverage, reconstructs skipped residuals with frequency- and confidence-aware Phase-Aware Reconstruction (PAR), and coordinates historical KV routing according to downstream reconstruction responsibility. On Matrix-Game 3.0 and HY-World 1.5, CAST achieves 2.15x and 3.48x speedups, respectively, while maintaining visual quality close to Native (Figure 1). It also attains the highest VBench scores among compared methods and leads non-native baselines on seven and six of thirteen WorldMark dimensions, demonstrating a balance of generation speed, visual quality, and interactive responsiveness under real-time control. Code is available at this https URL.

---


### 576. [ExpertoRhythm: Morphology-Aware Learning for Waveform Reconstruction and Cuffless Blood Pressure Estimation from Single-Channel PPG](https://arxiv.org/abs/2609.34146)

**<font color=#1a73e8>作者：</font>** Amir Arjomand, Kenneth B. Kent, Georgiy Krylov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous cuffless blood pressure (BP) monitoring from photoplethysmography (PPG) has strong potential for wearable health and telemonitoring, but accurate estimation remains difficult because PPG-to-BP mapping must preserve subtle waveform morphology and pressure-range-dependent dynamics. We introduce ExpertoRhythm, an attention-enhanced 1D U-Net that reconstructs the arterial blood pressure (ABP) waveform from a single-channel PPG signal and derives systolic and diastolic BP directly from the reconstructed waveform. The central contribution is a composite morphology-aware learning objective that integrates range-weighted SmoothL1 reconstruction with a window-range regularizer to emphasize high-dynamic BP segments and reduce amplitude under/over-shoot. On the UCI cuff-less BP dataset with 942 subjects, ExpertoRhythm achieves 2.46/1.46 mmHg MAE for systolic/diastolic BP (SBP/DBP), while obtaining a 30.4% average relative error reduction over pure MSE across waveform reconstruction and BP estimation metrics. Clinical-style evaluation further demonstrates low bias and strong agreement across the BP range, including high-pressure windows up to 200 mmHg, satisfying AAMI criteria and achieving BHS Grade A. These results suggest that morphology-aware waveform reconstruction from a single PPG channel can provide an accurate and practical pathway toward continuous cuffless BP monitoring in wearable and remote-care settings.

---


### 577. [Functional Hand Type Prior for 3D Hand Pose Estimation and Action Recognition from Egocentric View Monocular Videos](https://arxiv.org/abs/2609.34149)

**<font color=#1a73e8>作者：</font>** Wonseok Roh, Seung Hyun Lee, Won Jeong Ryoo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current methods for egocentric view action recognition often face challenges in perceiving dynamic hand movements relying solely on geometrical or physical information. In this work, we effectively address this problem by gaining insights into the correlation between functional hand configurations and objects, which improves the detailed interpretation of real-world scenarios. To this end, we introduce a practical taxonomy of hand types based on the functioning perspective and utilize it for per-frame hand type labeling on existing datasets. We also propose a novel hand action recognition framework considering semantic details of the hand type as prior. This approach boosts the network's understanding of the continuous hand interaction throughout the action sequence. Our whole pipeline consists of three main modules: (1) Feature Extraction, (2) Egocentric Knowledge Module, which estimates 3D hand pose, object category, and hand type leveraging short-term cues, and (2) Egocentric Action Module, which aggregates per-frame knowledge, including text embeddings of hand type, over a longer time. In our extensive experiments with large-scale benchmarks, FPHA and H2O, our model outperforms current state-of-the-art methods, demonstrating its superior performance.

---


### 578. [Self-Evolving Agents via Likelihood-Guided Tool-Space Optimization](https://arxiv.org/abs/2609.34151)

**<font color=#1a73e8>作者：</font>** Xuanqi Zhang, Ruinan Jin, Running Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-evolving agents can continually improve their behavior, while tools define the executable action space through which they interact with the environment. However, exposing the full tool library to model introduces substantial irrelevant context and can impair tool-use decisions. We study tool-space self-evolution, where each recurring task type maintains a persistent tool space which is constructed from accumulated output experience. We identify three limitations of existing methods: (1) output-unaware selection: they rely primarily on tool descriptions or model priors rather than observed tool outputs; (2) statelessness across request: they select tools independently for each request without consolidating prior output experience into persistent task-specific state; (3) inference cost: they repeatedly search, rank, or reason over candidate tools for subsequent requests of the same task. We address these limitations through output-aware tool scoring, persistent task-specific tool spaces, amortized tool selection, and reusable configurations across models. We introduce LOTS (Likelihood-Only Tool Scoring), which evolves an agent's tool space from accumulated output experience while keeping model parameters fixed. After each request, LOTS holds the model's generated answer and estimates each tool's contribution by measuring how much the answer likelihood changes when its observed output is removed. These contributions are aggregated within each recurring task to rank tools and update its persistent space. Across three benchmarks, LOTS improves task performance while substantially reducing tool context. More importantly, sequential experiments demonstrate that task-specific spaces persist and continue to improve over time, while cross-model experiments show that learned configurations transfer across different models.

---


### 579. [SPINET: Sheaf Protein Inverse Folding Network](https://arxiv.org/abs/2609.34153)

**<font color=#1a73e8>作者：</font>** Jens Lundsgaard, Colin Mikulski, Zhixuan Yan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Proteins change shape as they function, yet most inverse folding models predict amino acid sequences from a single, fixed backbone. A central challenge in protein engineering is to design proteins that undergo specific motions, which requires accounting for how their structures change over time. This motivates inverse protein folding conditioned on protein motion. We introduce SPINET, which predicts sequences from molecular dynamics trajectories. It uses cellular sheaves to represent residue interactions within each frame and recurrent units to integrate information across frames, then predicts all amino acids in a single pass. We evaluate SPINET on mdCATH and ATLAS, where it outperforms all evaluated static and ensemble baselines in sequence recovery. On mdCATH, it achieves 56.7% top-1 recovery, compared with 44.5% for the strongest static baseline and 40.7% for the strongest ensemble baseline. We also evaluate whether the predicted sequences are compatible with conformations sampled along the target trajectory. On mdCATH, they achieve a median TM-score of 0.760, and structural recovery favors target conformations over unrelated decoys for 99.5% of test domains.

---


### 580. [Transfer Calibrated Prediction Powered Inference](https://arxiv.org/abs/2609.34156)

**<font color=#1a73e8>作者：</font>** Aditya T. Vadlamani, Jae Ho Chang, Srinivasan Parthasarathy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prediction-powered inference (PPI) and its power-tuned extension (PPI++) improve confidence intervals by combining a small gold-standard labeled sample with a large AI model's predictions. Its efficiency gain relies on low residual variance, which may not hold if the predictor is pre-trained on a different source domain. We propose Transfer Calibrated Prediction-Powered Inference (TC-PPI), adapting the source-domain predictor to the target domain using gold-standard samples through cross-fitting. This approach supports various adaptation methods, such as sparse linear calibration, LoRA, and fine-tuning. Our jointly tuned cross-fit estimator, Joint-TC-Cross-PPI++, maintains unbiasedness and is simultaneously at least as efficient as classical inference, PPI, and PPI++, thereby protecting against negative transfer. We provide high-dimensional MSE bounds for calibration and show empirical improvements over baseline methods across various real-world applications.

---


### 581. [Hidden Activations are not Enough I: Knowledge Matrices as Higher Representations](https://arxiv.org/abs/2609.34166)

**<font color=#1a73e8>作者：</font>** Marco Armenta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the knowledge matrix of a trained feedforward network as a higher representation of its inputs. A network is a pair $(W,f)$, a thin representation $W$ of its quiver and an activation $f$; its function factorizes through the space of quiver representations, each input $x$ inducing a representation, and the knowledge matrix $M(x)\in\mathbb{R}^{C\times(d+1)}$ is the contraction of that representation to one matrix whose rows sum exactly to the logits. At one trained network we ask what determines it, what it is invariant to, what it determines, and what its geometry measures. Under (LCS), a locally constant slope diagonal, as for ReLU, the matrix at a regular input is a function of the realized germ; its stabilizer among encodings regular there is exactly the germ stabilizer at inputs with no vanishing coordinate, neuron permutation a special case; and it recovers the germ, whereas hidden activations, gauge-covariant and germ-incomplete, are not enough. Under (LCS) it equals per-class gradient$\times$input plus an exact aggregate bias attribution, grounding it in attribution theory and computing it by $C$ vector-Jacobian products instead of probing. The fixed shape gives an alignment-free per-sample distance between ResNet-152, DenseNet-121 and GoogLeNet; the row-sum identity gives an exact visible/invisible displacement decomposition whose unit-free coherence $A=(d_\Psi/d_M)^2$ puts adversarial germ motion at median $A\le 0.23$, with an attack-family ordering concordant across six architectures (Kendall $W=0.921$; $0.97$ on the three networks at full scale). Two honest negatives: on AlexNet/CIFAR-10 penultimate features win 5 of 6 detectors and all 16 attacks, and a matrix-direction counterfactual fails 0/54.

---


### 582. [Natural Image Autoencoder-Based fMRI Representations for Trait and State Prediction](https://arxiv.org/abs/2609.34167)

**<font color=#1a73e8>作者：</font>** Juhyeon Park, Yeonwoo Kim, Peter Yongho Kim 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models pre-trained on large-scale fMRI datasets have shown strong downstream performance, but at substantial data and computation cost. To investigate how much fMRI-specific pre-training is actually needed for such performance, we introduce FReD, which derives fMRI representations from a frozen Deep Compression AutoEncoder (DCAE) pre-trained exclusively on natural images and pairs them with a task specific readout. For trait prediction, FReD summarizes frame-wise representations by their temporal mean and log-standard deviation and applies linear probing, with late fusion across two normalization schemes. For state prediction, it represents each frame as a single token and models temporal dependencies with a shallow Transformer. Across four resting-state datasets spanning six trait-prediction targets, linear probes on frozen DCAE features generally outperform those on fMRI foundation model representations and remain competitive with fully fine-tuned fMRI foundation models. On three task-fMRI state-prediction tasks, a temporal readout on DCAE features performs comparably to the strongest foundation models evaluated. A Gaussian injection analysis further shows that localized signal changes are recovered more accurately from the frozen DCAE features than from the evaluated foundation-model representations. Together, these results show that strong performance on current fMRI benchmarks is possible without fMRI-specific representation pre-training, making frozen natural-image features as a useful baseline for assessing its added value.

---


### 583. [GPARA: Graph-Posterior-Aligned Refinement and Active Acquisition for Grounding Diffusion Priors](https://arxiv.org/abs/2609.34172)

**<font color=#1a73e8>作者：</font>** Wangqian Chen, Hao Wang, Yumeng Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Active grounding of a frozen diffusion prior requires jointly determining where new measurements should be taken and how they should be used to refine the current reconstruction. Posterior-ensemble-based methods can estimate acquisition utility from generated samples, but require repeated ensemble generation as observations accumulate and capture posterior geometry only through empirical statistics. This paper proposes GPARA, which learns a context-dependent graph surrogate over diffusion prediction residuals, inducing an explicitly reusable posterior response operator that propagates measurement innovations to unobserved variables and evaluates candidate measurements through weighted posterior-risk reduction. Under the matched surrogate, we show that the same response operator also determines expected one-step acquisition benefit and yields an analytic ranking consistent with expected reconstruction improvement. A bounded learned residual calibrates the analytic utility to account for surrogate mismatch, while a small prior ensemble is generated once and reconditioned to update risk weights without repeated diffusion posterior sampling during acquisition. Experiments on two reconstruction tasks spanning physical field and computer vision show consistent improvements in refinement and active acquisition over the evaluated baselines. Ablations further support the complementary roles of step-wise graph refinement, adaptive risk weighting, and analytically anchored calibration.

---


### 584. [GradLev: Token-Parallel Test-Time Training Via Costate Prediction](https://arxiv.org/abs/2609.34174)

**<font color=#1a73e8>作者：</font>** Bo Liu, Qiang Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time training (TTT) allows a model to improve its predictions at inference time by updating weights after every observed token. However, sequential gra- dient writes make parallel training difficult. We observe that, given layer inputs and activation gradients (costates), online gradient descent admits exact parallel scans for both forward evaluation and reverse backpropagation. GradLev lever- ages this duality: a causal auxiliary network predicts costates across all tokens in parallel; associative scans compute the adapted weights and forward activations and propagate gradients backward; and the resulting gradient targets supervise the predictor via a consistency loss. Exact consistency guarantees exact recovery of the sequential online learner. At deployment, the auxiliary predictor is discarded, and the model updates natively via token-by-token forward and backward passes.

---


### 585. [AGILE-GS: Anchor-Guided Fast Next-Best-View Selection for Active 3D Gaussian Splatting](https://arxiv.org/abs/2609.34176)

**<font color=#1a73e8>作者：</font>** Amirhossein Mollaei Khass, Nader Motee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiance fields need hundreds of views, and their placement matters as much as their number. Next-best-view (NBV) selection for 3D Gaussian Splatting (3DGS) usually scores every candidate in the pool and keeps one. Searching for information and choosing a camera, however, are separable problems. We present AGILE-GS, an anchor-guided NBV method that separates the two. A virtual anchor pose is optimized on SE(3) by Riemannian gradient ascent on expected information gain. It need not be reachable or in the pool; it marks where the model is most uncertain. Candidates are scored against the anchor's viewing geometry, and a greedy ridge-leverage step distills the pool into a small, non-redundant shortlist without rendering any candidate. The shortlist can be used in two ways. AGILE-GS takes the first view on it as the next view, so no Fisher information is computed for any candidate. AGILE-GS+ computes the Fisher information gain of each shortlisted view and picks the best, so the expensive evaluation runs on a handful of views rather than the whole pool. On standard benchmarks and in closed-loop embodied acquisition, both match or exceed existing baselines while cutting selection latency by one to two orders of magnitude.

---


### 586. [Enhanced Video Text Editing with Trajectory-Aligned Glyph Rendering](https://arxiv.org/abs/2609.34178)

**<font color=#1a73e8>作者：</font>** Shulian Zhang, Xiangyu Shu, Wenbo Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video text editing aims to replace or add text in a video while keeping the rest of the video unchanged, which requires the edited text to be correct in every frame and to move coherently with the scene. Despite the remarkable progress of video diffusion models, they struggle to reproduce exact stroke structures and often produce garbled or wrong characters, especially for characters with complex strokes. To address this, we propose a trajectory-aligned glyph rendering reference that provides explicit per-frame glyph guidance following the position and perspective of the text, and a depth-normalized recognizer feature supervision that supervises the generated text on multi-depth features of a frozen text recognizer with per-depth normalized errors, targeting stroke errors overlooked by the diffusion loss. We further build VTEdit, a benchmark of 288 real-scene clips with 440 annotated text trajectories covering text replacement and text addition, which will be publicly released to facilitate future research. Experiments on VTEdit show that our method outperforms image text editing methods, video editing methods, and commercial models in text accuracy and background preservation, achieving a sentence accuracy of 0.9408, and receives the highest preference in a user study.

---


### 587. [EntroPack: Fast and Accurate Entropy-Coded Weight Compression at Arbitrary Bitrates](https://arxiv.org/abs/2609.34185)

**<font color=#1a73e8>作者：</font>** Hong Zhang, Zhongjie Duan, Yingda Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weight compression helps large neural networks fit deployment memory budgets, but common fixed-width formats offer only coarse storage choices. Entropy coding supports finer rates, yet the achieved size depends on the quantized weight distribution and coding overhead. Exploiting this flexibility requires accurate rate selection and efficient weight reconstruction for inference. We present EntroPack, an entropy-coded weight compressor that supports arbitrary target bitrates without activation calibration or fine-tuning. It combines row-normalized $E_8$ lattice quantization with a conditional probability model of lattice coordinates. Sampled storage estimates select the quantization resolution without repeated full-stream encoding. The final coordinates are entropy-coded in independently decodable tiles, enabling fast, fused symbol decoding and numerical weight reconstruction on the GPU. EntroPack supports floating-point and integer weight containers, such as BF16, FP16, FP8, and INT8, with storage bitrate controlled independently of numerical precision. Online decoding adds latency that grows with weight count, making the method well suited to compute-intensive workloads such as diffusion denoising and Transformer prefill. Experiments demonstrate fast encoding and modest inference overhead in these settings. When compressing the linear-layer weights of the image generator Z-Image-Turbo, EntroPack achieves substantially lower weight and denoiser output errors than fixed-width formats at comparable storage rates, with modest denoising-step overhead. Targeting 4 bits per parameter, it achieves lower weight and denoiser output errors than NF4, including about 24% lower relative $L_2$ weight error, with less storage. Source code is available at this https URL.

---


### 588. [MotionSpaceFlow: Representation-Aware Flow Matching in Direct Motion Space](https://arxiv.org/abs/2609.34190)

**<font color=#1a73e8>作者：</font>** Qing Yu, Kent Fujiwara  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in diffusion and flow models have substantially improved text-driven human motion generation. Yet most methods generate in low-dimensional, temporally downsampled latent spaces learned primarily for reconstruction, a bottleneck that can limit generation quality and preclude direct manipulation of individual frames and joints. We introduce MotionSpaceFlow (MSFlow), a representation-aware flow-matching framework that predicts clean motion directly in continuous motion space without a learned encoder or decoder. To account for the anisotropic structure of direct motion representations, we propose representation-aware noise scaling and show how the initial Gaussian source scale governs the covariance of intermediate probability-path marginals. We further introduce a Representation-Aware Multimodal Diffusion Transformer (RA-MMDiT), which jointly updates token-level language and full-resolution motion features through joint attention while adapting temporal information flow to the motion representation: causal attention for incremental features defined by frame-to-frame changes, and bidirectional attention for global features such as absolute joint coordinates. Across different datasets and motion representations, MSFlow achieves state-of-the-art text-to-motion performance. Its global representation variant additionally enables zero-shot, inference-time control over any joint or frame through projection sampling without control-conditioned training, delivering leading motion quality with exact constraint satisfaction.

---


### 589. [Cardinality-Stratified Interaction Decomposition for Interpretable Pairwise and Higher-Order Structure in Transactional Basket Data](https://arxiv.org/abs/2609.34191)

**<font color=#1a73e8>作者：</font>** Hidetoshi Kawase, Toshihiro Ota  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transactional basket data can reveal associations among items, but observed co-occurrence conflates item-specific relations with basket-size structure and unmodeled higher-order dependence. We introduce Cardinality-Stratified Interaction Decomposition (CSID), an interpretable framework that decomposes log-odds contrasts stratified by the number of remaining items into item-set-specific and cardinality-common components, without fitting a global joint distribution. CSID uses an information-weighted, gauge-constrained ridge projection to estimate pair and triple components and to diagnose higher-order contributions to pairwise structure. CSID is designed primarily for interpretable decomposition of association structure rather than for full-distribution prediction. In a simulation with zero pair effects, increasingly strong small-basket cardinality potentials drive ordinary Ising couplings spuriously negative, whereas CSID pair estimates remain centered near zero. Detection power rises with the magnitude of planted triple effects, and local deprojection reduces pair-coefficient RMSE from 0.244 to 0.073. Across three grocery datasets, high-information triple components are reproducible over time. In the matched cross-period partial-transfer evaluation, transferred CSID triple components show closer agreement with later-period stratified contrasts than the nodewise-symmetrized cardinality-aware higher-order pseudolikelihood comparator, with gains in weighted Lin's concordance correlation of 0.038--0.122. These results support CSID as an exploratory and interpretable decomposition framework for pairwise and higher-order association structure in transactional data.

---


### 590. [WorldWeave: Growing Persistent Geometric Worlds for Video Generation](https://arxiv.org/abs/2609.34221)

**<font color=#1a73e8>作者：</font>** Yifan Huang, Lifan Jiang, Qingyue Hao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite rapid progress, world models still lack explicit, persistent structural memory, making it difficult to preserve consistent world structure during continual scene expansion and cross-view revisits. To address this limitation, we present WorldWeave, a world generation framework that decouples world-state maintenance from visual rendering. Specifically, WorldWeave combines continual elevation-map generation with agent-guided scene organization and stitching to build an expandable explicit 3D world that incrementally extends structural memory while preserving existing structure. First, its terrain module uses diffusion-based image outpainting to generate continuous metric elevation maps under neighborhood conditioning and boundary constraints. Next, an agent integrates user intent, terrain evidence, and cross-region connectivity constraints to construct scenes through hierarchical semantic planning, deterministic geometry compilation, and local revision. Finally, during visual generation, planned camera trajectories query world geometry through a read-only interface, producing depth sequences that guide video synthesis without writing the generated results back into the world state. As a result, structural memory remains independent of short-window video generation, enabling continual expansion without predefined map boundaries and providing a consistent geometric basis for observations across trajectories and repeated visits.

---


### 591. [ReGDiff: Guided Diffusion in Regulated Latent Space for Exploring Metamaterial Voxel Geometry](https://arxiv.org/abs/2609.34231)

**<font color=#1a73e8>作者：</font>** Wangzhi Zhan, Jianpeng Chen, Dongqi Fu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Metamaterials are artificially engineered structures whose mechanical and physical behaviors are strongly shaped by geometry rather than composition. Voxel representation provides a unified format for metamaterial geometry generation, as it can express diverse classes such as truss, shell, and porous structures within a single cubic discretization. However, voxel-based generation faces a plausibility-novelty trade-off: staying close to known geometries helps preserve geometric regularities, while moving away from them is necessary for novelty but may produce degenerate geometries. To address this challenge, we propose REGDIFF, a generative framework that couples voxel representation with latent space regulation and guided diffusion. REGDIFF introduces a repel-and-sink (RAS) mechanism to smooth the latent distribution of plausible geometries, and short-range repulsion (SRR) guidance to discourage generation overly close to known samples while maintaining geometric plausibility. We further contribute a voxel-based benchmark covering truss- and shell-type metamaterial geometries, together with an evaluation module for geometric plausibility, novelty, and diversity. Experiments show that REGDIFF outperforms voxel-based generative baselines, achieving +8.9% in geometric plausibility, +46.4% in novelty, and +128.6% in diversity on average across two datasets. These results suggest that REGDIFF is a strong geometry candidate generator for downstream evaluation. Our code is provided at this https URL.

---


### 592. [Trustworthy synthetic visual media: Evidence across the media lifecycle](https://arxiv.org/abs/2609.34232)

**<font color=#1a73e8>作者：</font>** Zexi Jia, Zhiqiang Yuan, Jie Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Images and videos have long helped people understand what happened and how a work came into being. Generative systems complicate that role. Realistic media can now be produced and revised without leaving a stable history, so appearance no longer reveals whether a scene was captured, synthesized, or altered along the way. Trust must instead come from evidence that explains the path an asset has taken and the circumstances in which it was used. Some of this evidence can be recovered from the media, while some must be recorded during production and preserved as the asset circulates. This review brings those approaches together and asks when their claims remain meaningful after ordinary processing or deliberate manipulation. We argue that trustworthy media do not depend on one universal marker of authenticity. The evidence must suit the question at hand, reach the person making the judgment, and remain open to correction when better information emerges. The larger goal is to keep the history of media intelligible even as the media itself continues to change.

---


### 593. [DecFlowEdit: Self-Localized Flow-based Image Editing via Guidance Decoupling](https://arxiv.org/abs/2609.34237)

**<font color=#1a73e8>作者：</font>** Zheyuan Zhan, Can Wang, Jiawei Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flow-based image editing (FlowEdit) enables inversion-free semantic changes through the difference between source and target velocities. In this paper, we observe that FlowEdit's default classifier-free guidance (CFG) configuration, with asymmetric source and target scales, causes substantial background leakage. Matching these guidance scales, for example by removing CFG, improves edit-relevant localization but severely degrades editability. To get the best of both worlds, we propose DecFlowEdit, which decouples the optimal guidance scales for localization and for editing in flow-based generative models. In particular, DecFlowEdit first extracts an edit-relevant prior by temporally aggregating velocity differences evaluated without CFG, and then uses this prior to reweight the original updates under default CFG. Our method remains training-free and inversion-free, requiring neither external spatial masks nor attention manipulation. Experiments on PIE-Bench across FLUX, SD3, and SD3.5 show that DecFlowEdit improves background preservation, reducing structure distance by approximately 61 to 73 percent and background LPIPS by 68 to 80 percent relative to FlowEdit at comparable editing fidelity.

---


### 594. [CasEm: A Cascade Architecture for Long-Horizon Neural Emulation](https://arxiv.org/abs/2609.34246)

**<font color=#1a73e8>作者：</font>** Zhaoyi Li, Jingtao Ding, Shihua Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoregressive neural emulators can drift or diverge over long rollouts despite accurate short-term predictions. We introduce Cascaded Emulation (CasEm), a one-way rollout architecture that augments an existing full-state backbone with an independently evolving model of physically specified aggregates. Its forecasts guide corrections to full-state predictions, without feedback from the backbone to the aggregate model. Effective guidance requires aggregates that cover substantial backbone error, remain accurately predictable, and support useful full-state corrections. We derive a finite-horizon error bound that clarifies these three factors and use empirical diagnostics to guide subsystem selection. Across four ODE/PDE benchmarks, CasEm reduces long-horizon rollout errors across diverse backbones and suppresses the trend toward error divergence in both diffusion tasks using Fourier neural operator backbones. In global climate emulation, CasEm with a regional total-water subsystem reduces 10-year full-state time-mean error by 66.6% and 46.3% for frozen ACE and Spherical DYffusion backbones, respectively, while adding less than 3% to inference time.

---


### 595. [Rotated Manifold Optimization for Low-Rank Adaptation](https://arxiv.org/abs/2609.34264)

**<font color=#1a73e8>作者：</font>** Yuhui Ding, Javier Zazo, James Hensman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a novel optimizer for low-rank adaptation (LoRA) that explicitly incorporates the gauge symmetry of low-rank factorization. Our optimizer extends recent matrix optimizers for full-parameter training to the manifold of fixed-rank matrices by interpreting them as normalization under a rotated basis. We show how rotation and normalization can be integrated with the fixed-rank manifold efficiently. Our optimizer converges faster to lower held-out loss and achieves better or comparable downstream performance on both supervised finetuning and reinforcement learning tasks.

---


### 596. [ZeroCode: On-demand Error-Correcting Code Construction from the Zero Matrix via Reinforcement Learning](https://arxiv.org/abs/2609.34265)

**<font color=#1a73e8>作者：</font>** Ju-Hyeong Lee, Yongjune Kim, Sang-Hyo Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Error-correcting codes (ECCs) are essential across diverse applications, from wireless communications and storage to quantum computing, yet each application imposes distinct design requirements on the parity-check matrix (PCM). To address these on-demand requirements in a unified framework, we propose ZeroCode, a reinforcement learning (RL)-based approach that constructs PCMs sequentially from the all-zero matrix. ZeroCode formulates construction as a discrete sequential decision-making problem and uses proximal policy optimization with action masking to select valid edges. ZeroCode achieves a gain of approximately 1 dB over the prior RL-based construction method at a bit error rate (BER) of $10^{-4}$ for the (32,16) code and outperforms existing genetic, differentiable, and classical code-design methods in our experiments. Beyond optimizing decoding performance, the masking mechanism allows on-demand structural constraints, such as a maximum degree, 4-cycle-free structure, and quasi-cyclic structure, to be flexibly incorporated. Moreover, a single policy rollout yields a library of PCMs with varying edge counts, offering trade-offs between decoding performance and complexity without retraining. Overall, ZeroCode addresses diverse code-design requirements within a unified framework, providing solutions with optimized decoding performance under given constraints.

---


### 597. [Scaling Versatile 3D Assets Editing with a Million-Scale Dataset](https://arxiv.org/abs/2609.34271)

**<font color=#1a73e8>作者：</font>** Badi Li, Tianxin Huang, Yu Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although recent 3D generative models produce increasingly realistic assets, controllable 3D asset editing remains challenging. Existing methods are limited by scarce training data, insufficient source-aware modeling, and a lack of practical evaluation protocols. To address these limitations, we present Alchemy3D, a unified framework for training and evaluating versatile 3D asset editors that covers data construction, model architecture, and benchmark evaluation. Specifically, we curate Alchemy3D-1M, a large-scale 3D editing dataset containing 1.25M assets and 1.38M editing pairs across seven editing types. On this data, we train a family of generative flow models for general-purpose 3D asset editing. The model family supports image- and text-conditioned editing, few-step inference, and transfer to multi-view 3D part segmentation. We further introduce GEdit3D-Bench, a large-scale, open-world benchmark with a multi-dimensional evaluation protocol. Across existing and newly introduced benchmarks, our method outperforms prior methods on most metrics of editing fidelity, source preservation, and visual quality.

---


### 598. [Broken Symmetry in BF16 Attention: Why FlashAttention Gradients Blow Up Late in Training](https://arxiv.org/abs/2609.34272)

**<font color=#1a73e8>作者：</font>** Junlin Chen, Daize Dong, Huanwei Di 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> BF16 is now standard in large-scale pretraining, including in fused attention kernels such as FlashAttention, and these kernels are widely trusted. When we used FlashAttention-3 to pretrain a 450M-parameter transformer on 50B tokens, however, we ran into a problem: training was healthy for 25B tokens, then the gradient norm grew a thousandfold and the loss ended 0.2 nats above FP32 attention, without a single NaN. Recomputing the attention backward of just two layers in FP32 removes almost all of the excess gradient. Part of the cause is known: a fused multiply-add in the forward softmax, so far treated as an extreme-input NaN case and never fixed in FlashAttention-3. Repairing it stops the blow-up, but the query gradient is still wrong by more than its own size, and training still drives attention logits to thousands of times their size under accurate gradients. The remaining error comes from a broken conservation law. The softmax score gradient sums to zero along every row, which makes the query gradient blind to where the keys sit as a group; rounding it to BF16 leaves a small nonzero sum that leaks the mean key into the gradient, and the leak grows exactly as late training makes keys large and attention sharp. We introduce GProj (gauge projection), which restores the zero sum after the cast with two rank-one corrections per row. It cuts the remaining median query/key gradient errors from 219%/13% to 0.34%/0.37%, on par with FP32 attention, for 4.7% more time per training step. In matched from-scratch runs it trains to the same loss as FP32 attention, while FlashAttention-3 and key smoothing both destabilize.

---


### 599. [MoSPR: Histology-to-Gene Expression Prediction with Morpho-Spatial Macrostates and Low-Rank Molecular Programs](https://arxiv.org/abs/2609.34280)

**<font color=#1a73e8>作者：</font>** Dongmyung Shin, Geongyu Lee, Yesung Cho 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Predicting molecular profiles from histopathology remains challenging because whole-slide images contain spatially organized, heterogeneous tissue patterns, while gene expression comprises thousands of correlated targets. We introduce MoSPR (Morpho-Spatial Program Regression), a linear framework that couples an adjacency-informed histology representation with a low-rank molecular basis. MoSPR clusters frozen patch embeddings into morphology microstates, aggregates their spatial adjacencies across the training cohort, and groups microstates with similar adjacency patterns into shared macrostates. Each slide is then represented by global morphology and macrostate-specific deviations, which are linearly mapped to coefficients of a training-derived low-rank gene-expression basis. Across three cancer cohorts from The Cancer Genome Atlas, MoSPR achieves the highest mean gene-expression prediction scores among all evaluated methods. Without pathway-level supervision, pathway scores derived from its predicted expression profiles rank first in eight of nine comparisons across three pathway collections. Ablation studies on the breast cancer cohort show complementary gains from adjacency-derived macrostate representation and low-rank molecular prediction. Moreover, with half of the training data on this cohort, MoSPR exceeds the full-data gene-prediction score of the strongest competing baseline. Finally, its linear formulation enables exact decomposition of each predicted expression profile into global and macrostate-specific molecular contributions, providing an interpretable link between spatially coherent macrostate regions and their associated molecular programs. Our code is available at this https URL.

---


### 600. [Epistemic Learning from Imprecise Annotation](https://arxiv.org/abs/2609.34285)

**<font color=#1a73e8>作者：</font>** Kaizheng Wang, Siu Lun Chau  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Imprecise annotations may support several plausible labelling distributions, yet learning methods often resolve this ambiguity into a single predictive distribution. This can obscure what the annotation evidence leaves unresolved. We introduce epistemic learning from credal supervision, a framework that uses convex sets of plausible labelling distributions, called credal sets, as supervision and learns sets of predictive distributions. We instantiate the framework with the pessimistic--optimistic credal classifier (POCC), which combines a shared backbone with two classification heads trained to minimise worst-case and best-case losses over the supervision sets. Their outputs define a predictive credal set whose spread provides an uncertainty score. We also show how credal labels can be obtained through a simple relaxation of existing probabilistic labels, reducing commitment to their precise probability assignments. This construction admits closed-form inner optimisation under cross-entropy loss, enabling efficient training. Assuming the supervision sets contain the true conditional label distributions, and other regularity assumptions, we establish a finite-sample generalisation bound for the averaged predictor with an explicit penalty for supervision imprecision. We evaluate POCC using human annotator disagreement and teacher predictions, alongside label smoothing as a controlled proxy for annotation imprecision. Across these settings, POCC achieves a favourable balance of predictive accuracy, calibration, and uncertainty-based selective classification versus competitive baselines.

---


> [!TIP]
> 当前位于：**551-600**（第 12/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | **551-600** | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-908](./part-19.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
