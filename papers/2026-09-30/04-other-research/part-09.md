# 📦 其他研究 | 2026年09月30日

> 本类共 **908** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**401-450**（第 9/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-908](./part-19.md)

---

### 401. [Does Learning to Predict the World Help Agents Act? Auditing World-Model Post-Training](https://arxiv.org/abs/2609.33335)

**<font color=#1a73e8>作者：</font>** Xinyu Che, Hang Yan, Yanchen Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Predicting how an environment will change before acting is a natural route to better decision making for agents. Recent post-training methods therefore require agents to predict the next observation and turn that prediction into a reward or a direct supervision signal, which is called world model. Existing next-observation training methods help the agent to learn the environmental content. However, they additionally involve an optimization process, which may introduce several effects other than learning to predict the world. Consequently, where the performance gain comes from during the training process remains an open question. We answer this research question through replacing true next-observation targets with in-distribution mismatched observations during the training process. Across two interactive text environments, mismatched targets lower prediction accuracy by 15.3-61.6% relative to ground-truth targets, yet retain substantial task gains over the base model. Compared with the base model, trained models consider more candidate actions and exhibit less looping. We also introduce a setting that replaces prediction-based rewards with independent random signals. This training expands task coverage (pass@64) even when the reward carries no environment information. We also generalize this finding to VisualWebArena, where random-reward training raises pass@64 by 14.3% relative to the base model, without observation-matching rewards or an external multimodal teacher for reward construction.

---


### 402. [Beyond Conservatism: Recoverability-Conditioned Exploration for Model-Based Imitation Learning](https://arxiv.org/abs/2609.33336)

**<font color=#1a73e8>作者：</font>** Xuanlin Chen, Ziyue Wang, Xunlan Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model-based imitation learning (MBIL) improves real-environment interaction efficiency by optimizing policies on imagined rollouts from a learned world model. However, the gap between model-induced and real-environment occupancies makes policy learning sensitive to model error. Conservative MBIL mitigates model exploitation during policy optimization, but when real-environment interactions are collected by the same conservative policy, uncertain regions around the expert distribution remain insufficiently sampled. Generic uncertainty-driven exploration, on the other hand, may allocate interaction to novel but task-irrelevant dynamics. We propose REcoverability-CONditioned Exploration for Model-Based Imitation Learning (RECON). RECON separates conservative policy learning from active data collection by maintaining a main policy for task execution and an explorer for real-environment interaction. The explorer is optimized based on epistemic uncertainty conditioned on recoverability estimated from multi-step main-policy imagination, focusing data collection on unknown states from which the main policy can still return toward expert behavior. Experiments on locomotion, navigation and manipulation show consistent gains in interaction efficiency, imitation performance, and robustness, indicating that RECON directs real-environment interaction toward recovery regions around the expert distribution that are underexplored by prior methods, and thereby learns a world model better suited for imitation.

---


### 403. [Safe Score Matching: Diffusion Policies with Hamilton-Jacobi Reachability for Online Safe Reinforcement Learning](https://arxiv.org/abs/2609.33337)

**<font color=#1a73e8>作者：</font>** Boyang Li, Matthew Kim, Sylvia Lee Herbert  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online safe reinforcement learning (RL) seeks policies that maximize reward while satisfying safety constraints. A popular line of research in safe RL relaxes safety to a soft expected-cost constraint and solves the resulting Constrained Markov Decision Process via primal-dual Lagrangian updates that only enforce safety on average. To address this limitation, hard, state-wise constraints are introduced and often imposed through Hamilton-Jacobi (HJ) reachability. Yet such constraints require solving different objectives in the feasible and infeasible regions: reward maximization in the former, recovery toward the feasible regions in the latter. The resulting target action distributions are inherently multimodal, and this structure poses a fundamental challenge for the Gaussian or deterministic actors used in existing HJ-based safe RL, which often collapse onto suboptimal modes. Diffusion policies provide the expressiveness needed to represent such distributions, and recent work on Q-score matching offers a route to training them for online RL by score regression -- but has been applied only to reward maximization. We propose Safe Score Matching (SSM), an off-policy actor-critic method that adapts Q-score matching to hard-constrained safe RL by gating a two-branch score target with HJ reachability: inside the feasible set, the denoising process degenerates to Q-score matching on actions classified as viable by the HJ critic; outside, a recovery branch biases denoising toward regions with lower worst-case violation. On quadrotor and fixed-wing trajectory-tracking and stabilize-and-avoid benchmarks, SSM attains the best or near-best task performance with low false-safe rates, whereas the primal-dual baseline admits more unsafe behavior and reachability-based baselines tend to be more conservative; on Safety-Gymnasium velocity tasks, SSM attains the lowest cost with competitive reward.

---


### 404. [Naturalness-guided Manifold Flow Matching for Sign Language Production](https://arxiv.org/abs/2609.33339)

**<font color=#1a73e8>作者：</font>** Jiayi He, Shengeng Tang, Sisi You 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sign Language Production (SLP) aims to generate sign motions from text. Conditional Flow Matching methods have achieved strong performance in SLP by constructing conditional paths that transform a source distribution into a target distribution. However, existing methods construct these paths via linear interpolation, whereas the rotational geometry of human joints confines valid joint rotations to a manifold embedded in Euclidean space. Consequently, linear interpolation between two sign motions leaves this manifold and ignores the motion distribution on it. In this paper, we revisit SLP from the perspective of manifold transport and propose a Naturalness-guided Manifold Flow Matching framework, termed \textbf{SignNMFlow}, which constructs conditional paths directly on the motion manifold by jointly considering geometric efficiency and the motion distribution. Specifically, we exploit the intrinsic geometry of the manifold and introduce a motion naturalness measure to characterize the motion distribution. By minimizing the kinetic energy under this measure, we learn a naturalness-guided interpolation that couples a closed-form geodesic, which provides geometrically efficient transport, with a learnable deviation that incorporates the motion distribution, thereby significantly improving the fidelity of generated sign motions. Extensive qualitative and quantitative evaluations demonstrate the effectiveness of this work.

---


### 405. [RAEGL: Risk-Aware Evidence-Gated Learning for Selective Contextual Routing under Temporal Shift](https://arxiv.org/abs/2609.33340)

**<font color=#1a73e8>作者：</font>** Yifan Guo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contextual specialization can improve forecasting accuracy, but a correction selected on one historical interval may become unreliable under temporal distribution shift. To address this issue, we propose RAEGL, a Risk-Aware Evidence-Gated Learning framework for selective contextual forecasting. RAEGL retains a validated global predictor by default and activates a contextual residual only when pre-deployment evidence supports its use. The framework separates candidate selection from gate calibration and jointly evaluates randomization significance, practically meaningful gain, and temporal stability. Experiments on real-world audits and controlled panels show how RAEGL can prevent harmful contextual deployment while making conservative opportunity costs explicit. In a reconstructed Our World in Data audit, exact fallback avoids RMSE degradations of 0.0960 and 0.0239 caused by two validation-selected corrections. In a sealed World Development Indicators evaluation, a region-based correction passes the randomization test but is withheld because its gain is only 0.000092, its country-clustered 95% confidence interval crosses zero, and only 0.02% of bootstrap replicates reach the practical threshold. In controlled panels, the stability- and support-aware extension activates in 97.2% of strong, stable-context runs while rejecting all high-drift settings. These results support RAEGL as an auditable, evidence-based mechanism for managing contextual deployment risk and as a conservative alternative to validation-driven contextual selection.

---


### 406. [CalibHyper: Chance-Corrected Relational Hypergraphs for Few-Shot Molecular Property Prediction](https://arxiv.org/abs/2609.33342)

**<font color=#1a73e8>作者：</font>** Linyu Li, Zhi Jin, Yuanpeng He 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular property prediction is central to drug development and materials discovery, but experiments are costly and labeled data are scarce. Context-aware methods use auxiliary assay labels to support few-shot prediction, and recent work supervises property relations with label agreement. However, label agreement is sensitive to class marginals and does not directly capture dependence between properties. We propose CalibHyper, a chance-corrected relational hypergraph method based on the joint label distribution. CalibHyper subtracts an independence baseline from the ordered four-state label distribution and shrinks the residual according to the number of joint observations. A swap-equivariant relation head estimates these residuals, which choose the auxiliary properties for each molecule and set the sign and weight of their hyperedge messages. On thirteen datasets from five benchmarks, in both 1-shot and 10-shot settings, CalibHyper and its ablation settings achieve ROC-AUC competitive with the strongest reported results.

---


### 407. [CHI: A Composite Hallucination Index Unifying Entity, Relation, and Quantity Dimensions for Summarization Evaluation](https://arxiv.org/abs/2609.33343)

**<font color=#1a73e8>作者：</font>** Praveenkumar Katwe, Rakesh Chandra Balabantaray, Kali Prasad Vittala  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Faithfulness evaluation of abstractive summaries remains an open challenge, with existing metrics addressing only isolated hallucination types: factual entity errors, relational inconsistencies, or numerical fabrications, without capturing their co-occurrence or interaction. We introduce CHI (Composite Hallucination Index), the first unified hallucination metric that decomposes faithfulness errors into three orthogonal dimensions: entity hallucination (EHI), relation hallucination (RHI*), and quantity hallucination (QHI). Each dimension employs a shared softmax-normalized architecture over Venn diagram-derived factors representing extractiveness, positive hallucination, over-focus, negative hallucination, and lost focus. The novel QHI component introduces tolerance-aware numerical matching with exact, epsilon, derived, and temporal comparison modes. We fuse the three dimensions via harmonic mean to produce a single composite score that penalizes weakness in any dimension. We validate CHI on 800 source articles spanning four domains (news, medical, legal, financial) with summaries from five generation systems. Empirical results demonstrate that: (i) the three dimensions are statistically orthogonal (mean rho = 0.148), confirming they capture distinct error types; (ii) CHI achieves the highest system-level correlation with human judgments (rho = 0.66, p = 0.006) on SummEval, outperforming ROUGE (rho = 0.53), EHI (rho = 0.58), and all individual components; and (iii) ablation studies confirm that all three dimensions contribute unique variance, with the full composite outperforming any individual component while providing decomposable error diagnostics unavailable from single-score baselines. CHI provides practitioners with a decomposable, interpretable, and efficient faithfulness metric suitable for both offline evaluation and online monitoring of summarization systems.

---


### 408. [ReLoc: Rethinking Scene Coordinate Regression Architecture for Robust Outdoor LiDAR-based Localization](https://arxiv.org/abs/2609.33344)

**<font color=#1a73e8>作者：</font>** Heejoon Moon, Yurim Cho, Je Hyeong Hong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scene Coordinate Regression (SCR) has recently emerged as a promising approach for LiDAR-based localization, achieving accurate localization without requiring an explicit 3D map. Despite their effectiveness, existing SCR methods rely on scene classification-based global embedding that struggles to provide fine-grained discrimination among nearby locations. Moreover, their reliance on uniform sampling of local features during training assigns equal importance to all points, thereby inadvertently propagating features from dynamic objects or unstable regions and potentially degrading training stability. In this paper, we present ReLoc, a revamped SCR architecture that can effectively address these limitations. First, we redesign the global embedding module by combining learnable context tokens with a feature aggregator to capture richer and more discriminative scene context. Second, we introduce an attention-based local feature enhancement module to mitigate the impact of noisy local features while encouraging context-consistent structures, yielding more robust local feature representations. Experimental results on two large-scale outdoor datasets demonstrate that our approach achieves state-of-the-art accuracy over previous SCR-based methods while maintaining real-time inference performance.

---


### 409. [Language Discrimination Improves Linguistic Learning in Multilingual Speech Models](https://arxiv.org/abs/2609.33345)

**<font color=#1a73e8>作者：</font>** Maureen de Seyssel, Jie Chi, Zakaria Aldeneh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual self-supervised speech models can benefit from sharing information across languages, but under a matched total pretraining data budget they still fall short of monolingual models. We show that strengthening the model's ability to discriminate languages during pretraining reduces and, on some measures, closes this multilingual gap on continuous phonetic and higher-level linguistic measures, while preserving substantial cross-language sharing. Using a controlled English/French HuBERT setting, we test two interventions which strengthen language discrimination: an auxiliary language classifier and per-language k-means targets. Across interventions, continuous-feature phone discrimination error (phone-ABX, lower is better) decreases from 11.6% in the bilingual baseline to 10.4% (monolingual: 10.8%), while lexical performance (sWUGGY, higher is better) increases from 52.1% to 56.7% (monolingual: 58.5%) and prosodic performance (ProsAudit, lexical subtask, higher is better) from 68.9% to 72.9% (monolingual: 72.6%). Across HuBERT training stages, the strongest gains on most linguistic measures occur when language discrimination is introduced in the first iteration, whereas later or repeated interventions yield smaller improvements and are accompanied by increased language-wise segregation. These results support a causal role for language discrimination in reducing the additional cost of multilingual learning.

---


### 410. [MultiEcho: An Experimental Science of Learned Worlds](https://arxiv.org/abs/2609.33347)

**<font color=#1a73e8>作者：</font>** Meng Zhu, Airui Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models can be studied as experimental systems with response laws of their own. We introduce MultiEcho, a framework for estimating these laws through controlled counterfactual interventions, delimiting their applicability, and separately testing their physical correspondence. Across nine simulated physical systems and seven frozen model configurations, three-reference estimators predict complete intervention responses and recover intervention parameters. Estimator selection uses discovery data only; frozen fits are evaluated on validation and confirmation contexts. The experiments distinguish response predictability, intervention readability and physical accuracy. Responses can be locally describable yet poorly match physical effects in the same target coordinates. Event-window, visibility and camera interventions reveal conditional applicability, and paired generator configurations show reduced readability under a scene prompt with stronger guidance. Magnitude sweeps expose small image errors alongside large relative effect errors. An exact-reset material experiment separates registered visible-response success from fixed-readout failure on material-dependent futures at matched positions and velocities. Exact finite-scale identities resolve odd and even response errors; first-order remainder bounds specify when refined calibration converges. MultiEcho provides an experimental basis for studying learned-world laws independently of, and in relation to, physical laws.

---


### 411. [KoopCell: Koopman-Based Generative Model for Learning Single-Cell Dynamics from Distribution Snapshots](https://arxiv.org/abs/2609.33350)

**<font color=#1a73e8>作者：</font>** Wanfeng Lu, Yutong Zhang, Keyi Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning population dynamics from temporally sparse, unpaired distribution snapshots is a fundamental challenge in developmental biology. Recent approaches based on neural differential equations and flow matching can interpolate between observed population snapshots, but may struggle to extrapolate beyond the training horizon and often lack an explicit mechanism for modeling developmental branching. We propose KoopCell, a unified generative framework based on Koopman-Mori-Zwanzig theory that jointly learns representations and predictive linear latent dynamics. Theoretically, using the weak continuity equation, we derive a closed-form least-squares estimator for the Koopman generator from distribution snapshots and establish convergence guarantees under suitable assumptions. To model branching dynamics, we further develop KoopCell-M, which incorporates non-Markovian memory into the latent Koopman dynamics through a Markovian embedding. Experiments on synthetic systems and three scRNA-seq datasets demonstrate the ability of our framework to recover Koopman spectra, model branching through memory, and scale to predicting high-dimensional gene expression distributions, achieving state-of-the-art performance among the evaluated methods.

---


### 412. [How Much Imprecision is Enough Imprecision in my Classifier? A Practical Elicitation Procedure](https://arxiv.org/abs/2609.33352)

**<font color=#1a73e8>作者：</font>** Victor F. Lopes de Souza, Sébastien Destercke, Abdelhak Imoussaten  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Set-valued classifiers, whether derived from precise probabilities and an adapted cost function, from convex sets with a robust inference mechanism, or from conformal methods, are routine options to obtain more robust, trustworthy predictions. However, there is a lack of operational tools to measure how robust or imprecise a given user is ready to be when receiving predictions, that is how much precision he/she is ready to let go in exchange of more accuracy. This is why we propose, in this paper, practical and operational elicitation procedures to measure the user proneness to set-valued predictions. The effectiveness of the iterative elicitation procedure in converging to the target parameter value is demonstrated on both tabular and image datasets drawn from standard machine learning benchmarks. The results show that the procedure also presents the user with a small number of instances, highlighting the practicality of the approach for real-world applications aimed at identifying the decision maker's optimal behavior when faced with imprecision.

---


### 413. [Focus and Supplement: Dual-Enhanced Vision Transformer for Multi-Class Anomaly Classification](https://arxiv.org/abs/2609.33353)

**<font color=#1a73e8>作者：</font>** Xurui Li, Enjie Xu, Chenzhou Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-class anomaly classification in industrial vision remains challenging due to noisy/incomplete anomaly representations and the unknown number of anomaly classes. To overcome this, we propose MACO, a novel multi-class anomaly classification framework that learns comprehensive representations and dynamically estimates class number without prior knowledge. First, a soft-focus attention uses anomaly maps to concentrate on relevant abnormal regions, while suppressing background noise. Second, auxiliary classification ([A-CLS]) tokens complement the [CLS] token. They collectively attend to diverse anomaly sub-regions, yielding more holistic and discriminative features. These [A-CLS] tokens are also effective across more tasks and domains. To infer the class number, we propose Correlation-based Number Estimation strategy. It computes the average correlation among labeled classes and transfers its separability cue to the unlabeled set. Experiments on MVTec AD and MTD datasets demonstrate our superiority. Under known class number, MACO improves ARI by 6.5% and $\textbf{16.3%}$ on both datasets, respectively. In the more challenging unknown number scenario, it achieves an $\textbf{11.2%}$ NMI gain on MTD and outperforms existing number estimation strategies by $\textbf{24.1%}$ UPS on MVTec AD. Code will be released at this https URL.

---


### 414. [DISCERN: Can AI Agents Work Like Scientists and Guide Discovery?](https://arxiv.org/abs/2609.33357)

**<font color=#1a73e8>作者：</font>** Nan Huang, Mario Tapia-Pacheco, Kun Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reliable automated research requires agents to vet data, verify analyses, and generate hypotheses grounded in trustworthy evidence, potentially reducing routine scientific workload while allowing scientists to focus on interpretation and discovery. Existing benchmarks often only assess analytical task completion or hypothesis generation separately rather than testing whether reliable evidence supports valid and novel claims. We introduce DISCERN (Data Integrity and Scientific Capability: Evidence, Reasoning, and Novelty), a controlled benchmark on real, publicly available datasets that evaluates three key levels of an automated research workflow. The first two levels test data integrity and analysis verification under confounds and tool traps, while the third tests hypothesis generation and revision under adversarial review, including counterfactual cases in which evidence consistent with real data and documented scientific phenomena conflicts with established expectations, motivating alternative explanations and testable hypotheses. Across 203 tasks, eight life-science tracks, and eight models, DISCERN shows that strong aggregate performance can mask level-specific weaknesses. Agents earn perfect scores in only 60.8% of Level 1, 34.2% of Level 2, and 0.6% of Level 3 evaluations, with penalties attributed to rejection of sound data, failure to carry recognized limitations into conclusions, and wide variation in hypothesis production. Cross-track rankings by token and code use are substantially more stable than rankings by evidence judgment, suggesting greater consistency in computational effort than in evidence-based reasoning. These profiles identify opportunities for supervised scientific assistance, but current agents do not yet demonstrate reliable autonomous analysis or discovery. Code and data: this https URL

---


### 415. [When Does Geometric View Synthesis Help Wine Label Retrieval? A Public One-Shot Benchmark Across Self-Supervised and Vision-Language Backbones](https://arxiv.org/abs/2609.33359)

**<font color=#1a73e8>作者：</font>** Yueh-Cheng Huang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geometric view synthesis can expand a single wine-label photograph into a training set, but its value with pretrained image encoders is unclear. We study this on a public WineSensed-derived benchmark of 1,000 classes, one enrollment photograph per class, and 4,295 real queries. With the earlier DINO vision transformer (ViT-S/16) recipe, geometric views raise top-1 accuracy from 34.1% to 62.6-63.7%, about three times the gain from two-dimensional (2D) augmentation. Frozen SigLIP 2-B already reaches 94.7%. A linear head over its frozen features gains 1.2-1.3 percentage points with the two geometric pipelines localized by the Segment Anything Model (SAM), while the other pipelines gain an inconclusive 0.3-0.6 points. Low-rank adaptation (LoRA) and validation-selected full fine-tuning show no clear gain within the reported confidence intervals; fixed-budget full fine-tuning loses 9-24 points. SAM localization supplies all six views for 99% of sources, compared with 43% for the edge-based front end. Recognition differences between the two cylinder constructions depend on the training recipe and are confounded by their crop and canvas conventions. Rendered-cylinder tests show different responses to source tilt, but an uncalibrated rim-ratio proxy establishes no corresponding trend in recognition on real photographs. An author-confirmed audit of 50 residual errors identifies 21 query-enrollment appearance mismatches, without establishing an irreducible error rate. These results support geometric synthesis for the tested self-supervised recipe and a smaller benefit through frozen-feature adaptation of the text-supervised encoder.

---


### 416. [DrafTS: Time-Aware Decomposition with Residual Correction for Time Series Modeling](https://arxiv.org/abs/2609.33368)

**<font color=#1a73e8>作者：</font>** Yiqiu Liu, Siru Zhong, Zhiguang Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-world time series contain evolving underlying dynamics with irregular variations that lack stable temporal patterns and are often referred to as noise. Existing methods address this mixture by filtering frequencies or suppressing noisy observations. They either miss temporal evolution or risk suppressing useful dynamics. We propose DrafTS, a model-agnostic framework that aims to reduce noise while preserving evolving dynamics through time-aware Decomposition with ResiduAl correction For Time Series. DrafTS uses features derived from instantaneous amplitude and frequency to guide decomposition into a primary component intended to capture underlying dynamics. A task-specific backbone models the primary component, while a lightweight correction module uses residual information to correct the backbone output. Across four time series modeling tasks, DrafTS improves six diverse backbones, demonstrating its effectiveness. Code is at this https URL

---


### 417. [The Selection Rule Decides the Winner: A Pre-Registered Audit of Open-Set Graph Anomaly Detection](https://arxiv.org/abs/2609.33370)

**<font color=#1a73e8>作者：</font>** Farhan Shahriyar Hossain, Taufikur Rahman Fuad, Md Abrar Jahin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Open-set graph anomaly detection trains on a few labeled anomalies from one class and must also find anomaly classes that were never labeled. Published results share three conventions: the test score is read at the best epoch on the test set, baseline numbers are copied from earlier papers, and most anomalies are minority classes relabeled as anomalous. We ask how much of the reported ranking these conventions decide. We re-run two recent methods, DEMO and NSReg, together with OUTPOST, a small first-order detector built for this study. All three use one protocol with identical seeds and splits on eight graphs (seven for the baselines, which cannot run on ogbn-mag), ten seeds each, and every run is scored under both the best-epoch rule and a deployable validation rule. Before the runs that test them, we registered 40 predictions. Three findings hold. First, the rule changes the leader: under the best-epoch rule, OUTPOST and NSReg each lead three of seven graphs, while under the validation rule, NSReg leads five. Second, the best-epoch bonus depends on how the benchmark was built: 0.045--0.080 AUC-ROC on the three small relabeled-class graphs and 0.002--0.014 on the three real fraud graphs. Third, pseudo-labeling in OUTPOST is worth 0.038--0.065 AUC-ROC on the same three graphs but gives no benefit on any real fraud graph. We also show that a 0.002 tie band for hyperparameter selection lies below the paired standard error on all six graphs tested, even at ten seeds. Twelve of our 40 predictions were falsified, and we report them. We close with a short reporting checklist.

---


### 418. [TNF based Spectral Embedding for Effective Application of Supervised Machine Learning Techniques in Automobile Insurance Fraud Detection](https://arxiv.org/abs/2609.33376)

**<font color=#1a73e8>作者：</font>** Rohan Yashraj Gupta, Lalith Srikanth Chintalapati, Satya Sai Mudigonda 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fraud detection is an important area of research in the insurance business due to its financial implications. The primary aim of a fraud detection model is to identify fraud and non-fraud cases with high accuracy along with other important metrics such as Sensitivity, Specificity, Precision, F1-score, False Positive Rate, False Discovery Rate, AUC etc. To achieve this, we need to explore a suitable classification model to identify fraud and non-fraud cases. In this work, we have used auto insurance data set and explored classification models such as Decision Tree (DT), Random Forest (RF), XGBoost, LightGBM and Gradient Boosting Machine (GBM). To overcome the problem of data imbalance, we have employed MWMOTE and TGAN techniques. We have used Topological Node Feature(TNF) based spectral embedding for low dimensional data representation along with some popular embedding methods like MDS, Isomaps and t-SNE. After studying all the 65 possible combinations of these models, we have proposed an innovative method for effective automobile insurance fraud detection. For the given dataset, our results show that using a combination of MWMOTE as a data imbalance handling technique (Phase I), TNFSE2 as data embedding (Phase II) and Random Forest as classification (Phase III) provides the best result in comparison to all other combinations. This work also highlights the efficacy of TNF based spectral embedding in automobile insurance dataset

---


### 419. [Optimal Transport Dropout for Structured Predictive Uncertainty](https://arxiv.org/abs/2609.33377)

**<font color=#1a73e8>作者：</font>** Giacomo Lorenzon, Francesco Regazzoni  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deterministic neural networks and neural operators provide point predictions with no intrinsic measure of reliability. Yet, predictive uncertainty may stem from irreducible outcome variability, finite data, or limitations of the chosen model class. Monte Carlo dropout offers a computationally convenient way to construct a predictive distribution through stochastic feature masking, without training multiple independent networks or explicitly inferring a posterior over model parameters. However, its perturbation law is largely prescribed a priori and typically factorised across latent coordinates. We introduce Optimal Transport Dropout (OTD), which instead learns the predictive mapping and the law of its latent perturbations jointly. Starting from a simple independent reference distribution, OTD transports latent perturbations through a learnable flow and propagates them through the predictive neural network, thereby inducing a structured predictive law. Training uses the strictly proper Energy Score, while a kinetic-action term geometrically regularises the transport. Synthetic benchmarks show that OTD captures multimodal predictive distributions, generates meaningful dispersion when the model is misspecified, and exhibits contracting dispersion as more training data or greater model capacity are provided. For a field-valued partial differential equation surrogate, predictive dispersion strongly aligns with the spatial pattern of prediction errors. On this task, compared with Monte Carlo dropout, OTD yields more accurate predictions and better-calibrated, substantially narrower intervals. On real-world regression benchmarks, it further shows competitive accuracy and better probabilistic predictions compared to established baselines. OTD therefore offers a way to learn structured predictive uncertainty without explicit posterior inference or ensembles of independently trained predictors.

---


### 420. [PulseQuant: Propagation-Guided Subspace Correction for 4-Bit Video Diffusion Transformers](https://arxiv.org/abs/2609.33384)

**<font color=#1a73e8>作者：</font>** Yutong Wang, Xingtong Ge, Enhuai Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Quantization errors in video diffusion transformers can be amplified or attenuated by subsequent denoising updates, making local reconstruction error an incomplete predictor of final impact. We introduce PulseQuant, a 4-bit post-training quantization method that combines trajectory sensitivity with activation geometry to guide offline calibration. Isolated block--step interventions estimate propagation risk, which prioritizes sensitive trajectory states during row-radius selection. With these radii fixed, response-subspace correction uses neighboring-code edits to reduce residual components along dominant activation directions. Both stages preserve the original 4-bit weight representation. Controlled interventions show that short-horizon propagated error predicts final latent error more reliably than immediate block-output error, supporting calibration beyond local reconstruction objectives. Evaluations on Wan models, Self Forcing, and MiniMax-H3 demonstrate improvements in key consistency and dense-reference metrics while remaining competitive on other attributes across model scales and generation paradigms.

---


### 421. [From Grey-Box to Green-Box: When can Physics-Informed Machine Learning Reduce Carbon Footprints in Structural Health Monitoring?](https://arxiv.org/abs/2609.33387)

**<font color=#1a73e8>作者：</font>** Daisy R. Bradley, Nathan A. Hinchliffe, Daniel J. Pitchforth 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning plays an increasingly vital role in engineering, but the corresponding increase in compute time is not without environmental cost. Physics-informed machine learning or "grey-box" models have been developed to overcome some of the limitations of traditional black-box learners, utilising the physical insight that an engineer would have about the structure they are modelling and have shown promising results in the structural engineering field among many others. This work explores whether an additional advantage could be a reduced environmental impact, considering the relationship between training data quantity and training time, linking this duration to carbon emissions from computing.
In a structural health monitoring context, four physics-informed machine learning approaches - spanning Gaussian processes and neural networks - are evaluated: residual modelling, input augmentation, hybrid modelling, and constrained learning. The emissions for training each of the models to reach a given error threshold is compared, and in most examples, shown to be lower for the physics-informed models (with input augmented models being an exception). This reduction in training emissions further compounds the environmental savings achieved by collecting and storing less data. Although promising results, we cannot expect a silver bullet and the case studies demonstrate that a trade-off is needed between the increased complexity that comes from introducing physics into a machine learner, against the gain from reduced training data requirements.

---


### 422. [AutoHGNN: Robust and Efficient Neural Architecture Search for Hypergraph Neural Networks](https://arxiv.org/abs/2609.33392)

**<font color=#1a73e8>作者：</font>** Sirui Li, Pietro Liò b, Xinsheng Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hypergraph neural networks have achieved significant success in recent years. However, manual architecture crafting is labor-intensive and often fails to capture complex, higher-order relations, making the automation of hypergraph neural network structure design crucial. To improve the automation and adaptability of hypergraph learning, this paper proposes AutoHGNN, a neural architecture search framework tailored for hypergraph neural networks. First, we introduce a Hyper-Interaction Module (HIM) into the search space to address the mismatch between conventional graph neural network designs and hypergraph data. Second, we propose Hypergraph Stable Topological Distance (HyperSTD) as a structural selection criterion to identify architectures that best preserve the intrinsic structural affinities of the original hypergraph during differentiable search. Extensive experiments on various benchmark datasets demonstrate that AutoHGNN consistently outperforms manually designed and automatically searched baselines in classification accuracy and time efficiency, proving that the discovered architectures are significantly more effective.

---


### 423. [Cross-modal Translation via Conditional Latent Denoising for Video Deepfake Detection](https://arxiv.org/abs/2609.33394)

**<font color=#1a73e8>作者：</font>** Xinzhe Li, Youzhi Tu, Kong Aik Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The growing threat of video deepfakes necessitates multimodal detection. Beyond serving as independent indicators of authenticity, audio and visual signals have intrinsic dependencies that also provide an essential criterion for detection. Previous methods often overlook the cross-modal correspondences, hindering information transfer between domains and leaving crucial detection cues unexplored. To address this challenge, we propose a framework called Cross-modal Translation via Conditional Latent Denoising (CTCLD) for video deepfake detection. It connects the distinct distributions of heterogeneous modalities in latent spaces, enabling smooth cross-domain information transfer to improve detection performance. We first establish a Bayesian foundation by decomposing the audio-visual joint distribution. Subsequently, CTCLD translates both modalities via bidirectional latent denoising conditioned on each other, effectively capturing subtle inconsistencies in the manipulated signals. Experimental results demonstrate that the proposed CTCLD enables comprehensive domain alignment, resulting in a robust video deepfake detection approach with competitive performance.

---


### 424. [SciGen-Verifier: A Multimodal Reasoner for Explainable Verification in Scientific Image Generation](https://arxiv.org/abs/2609.33399)

**<font color=#1a73e8>作者：</font>** Jiali Chen, Zhengteng Lin, Zuqi Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In realistic education, a solution is often expressed not only in words but in a drawing--a circuit, a geometric construction, a function plot--and a teacher must grade the drawing as carefully as the text. Recent advances in unified multimodal models have enabled scientific image generation, yet verifying the correctness of these specialized visual outputs remains a critical bottleneck: errors often arise from intricate domain knowledge, structural reasoning, and multi-step instruction rather than surface-level artifacts. Existing verifiers mainly target natural images and compress judgement into scalar scores, leaving scientific coverage and explainable feedback for error correction underexplored. To bridge this gap, we make three main contributions. (1) We construct SciGen-Verify, a benchmark dedicated to explainable verification of scientific image generation, spanning instruction following, multidisciplinary reasoning, and world knowledge domains. It contains a three-tier hierarchical protocol over the binary judgement, supporting explanation, and corrective editing instruction. (2) We develop SciGen-Verifier, a reasoning-driven multimodal verifier trained via cold-start supervised fine-tuning followed by a curriculum-based two-stage reinforcement learning pipeline. The rubric-guided process rewards first strengthen scientific reasoning exploration and outcome rewards subsequently align output with ground-truth annotation. (3) On SciGen-Verify, SciGen-Verifier achieves competitive performance against much larger proprietary models. It further serves as a practical online critic for iterative image rectification.

---


### 425. [Groupwise Selective State-Space Filtering for Accurate and Streaming Action Boundary Detection](https://arxiv.org/abs/2609.33400)

**<font color=#1a73e8>作者：</font>** Mustafa Bora Çelik  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Action boundary detection partitions untrimmed video into intervals without assigning action classes. We present a boundary-detection adapter operating on pre-extracted video features, learning temporal representations via groupwise selective scans. Learned group fusion and temporal modeling convert these into transition scores, which are decoded into boundary timestamps. Trained with boundary-time supervision, the class-agnostic model is evaluated on Breakfast, GTEA, and 50Salads using temporal tolerances and bipartite matching, achieving boundary $F_1$ scores of 0.457, 0.622, and 0.611. A stateful variant enables feature-streaming inference with zero neural look-ahead, one-sample peak confirmation, and bounded memory. Downstream systems can subsequently assign s

---


### 426. [VaME: Exploring Variational Latent Reasoning for Multimodal Embeddings](https://arxiv.org/abs/2609.33402)

**<font color=#1a73e8>作者：</font>** Peixi Wu, Mingzhou Jiang, Feipeng Ma 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Universal multimodal retrieval requires compact embeddings that preserve task-relevant semantic information across diverse modalities. Prior works have incorporated latent reasoning into multimodal embedding learning to refine this information before embedding extraction. However, most existing approaches remain confined to deterministic latent paths, without exploring alternative trajectories to discover better embeddings. Thus, we propose VaME (Variational Multimodal Embeddings), a framework that models latent reasoning as a learnable distribution over trajectories. Specifically, we first introduce Variational Latent Reasoning (VLR) to enable autoregressive exploration in latent space, guided by answer reconstruction through a lightweight decoder. Meanwhile, we augment the original embedding-token readout with a latent-fused embedding to facilitate exploration during subsequent reinforcement learning. Finally, we optimize latent reasoning over stochastic variational trajectories through reinforcement learning, using Semantic Decoding Reward (SDR) to favor semantically meaningful trajectories with interpretable decoded outcomes. On the 78-task MMEB-V2 benchmark, spanning image, video, and visual-document retrieval, VaME outperforms most explicit CoT-based models and all latent-reasoning baselines. VaME also demonstrates robust performance on reasoning-intensive benchmarks such as MRMR, with substantial gains after reinforcement learning. Importantly, VaME achieves these gains with at least a 4.25x inference speedup over the deterministic latent autoregressive baselines. The code will be made publicly available.

---


### 427. [StarBOA: Real-Time Mamba State-Space Unrolling for Sparse Radar Micro-Doppler in ISAC Networks](https://arxiv.org/abs/2609.33408)

**<font color=#1a73e8>作者：</font>** Mustafa Bora Çelik, Ceren Çelik, Orhan Gazi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In Integrated Sensing and Communications (ISAC), radar sensing must operate under chirp subsampling with up to 90\% missing data. An attention-based baseline, limited to a 52~ms buffer, collapses toward maximum uniform entropy ($H=2.584$ bits) as sparsity increases, failing to capture long-range gait-cycle context. We propose StarBOA, which replaces attention with a causal Mamba state-space model that updates incrementally on a per-window basis without re-scanning past reconstructions. By maintaining a persistent state, StarBOA integrates over $100\times$ more temporal history at no additional per-step computational cost. StarBOA outperforms the baseline's published results across all sparsity levels, with SSIM gains increasing from $+0.0379$ at 50\% missing data to $+0.2472$ at 90\%. Each window is processed in 1.53~ms with zero lookahead, demonstrating efficient causal reconstruction under extreme chirp subsampling.

---


### 428. [Weird Machine Compositors: Exploiting AI Orchestration at the Expression Layer](https://arxiv.org/abs/2609.33413)

**<font color=#1a73e8>作者：</font>** Eilon Cohen, Ariel Fogel  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Orchestration platforms secure user-provided expressions through enumerate and block sandboxing: AST rewriting, runtime property blocklists, template sandbox environments. We demonstrate that these sandboxes are weird machines whose instruction set is the underlying language specification, and that the enumerate and block approach is unfixable, following the same trajectory that led to the deprecation of past sandboxing technologies such as Java's SecurityManager and vm2.
We validate this claim through three rounds of escalating bypasses against n8n's expression sandbox (three CVEs, two CVSS 9.4, one unauthenticated), and frame these findings within a broader pattern of sandbox failures across the orchestration products category. We identify a trust laundering pattern where orchestration pipelines and applications move attacker controlled input from untrusted to fully credentialed through transformations that strip taint at each level. AI-assisted enumeration accelerates the discovery of these coverage gaps, compressing the timeline between a sandbox's deployment and its compromise.
We provide an AST coverage analysis methodology, an accompanying open-source tool, and a defensive playbook that includes policy inversion (allowlist over blocklist) as a structural mitigation.

---


### 429. [Investigating the Effect of k-NN Preprocessing on Developing Graph Neural Networks: A Fairness-Based Perspective](https://arxiv.org/abs/2609.33416)

**<font color=#1a73e8>作者：</font>** Nikolaos Zafeiropoulos, Emmanouil Mavrikos, George E. Tsekouras  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, a methodology to design fair graph convolutional neural networks (GCNs) is developed and tested over several application data sets. The graphs that are used as inputs to the network are constructed by a k-nearest neighbor-based preprocessing procedure, while fairness issues are considered in terms of the equalized odds criterion. To effectively incorporate the above heterogenous information, the equalized odds criterion is directly embedded into the model's optimization objective through an additional fairness-driven loss functional term. The proposed methodology investigates how varying the neighborhood size in the k-NN algorithm during graph construction influences both the classification performance and the fairness of the resulting models. Extensive experimentation is conducted on three real-world tabular datasets with known biases, evaluating the interplay between graph structure and fairness enforcement. The results demonstrate that the choice of the value of the parameter k critically impacts the performance trends, either steadily improving or peaking at intermediate values depending on dataset characteristics, while the application of fairness constraints significantly mitigates disparities in false positive and false negative rates across groups defined by the protected variable at hand, without incurring major sacrifices in overall accuracy. This study highlights the importance of jointly optimizing the graph construction process and fairness objectives in GCN-based learning, providing a systematic approach toward building more equitable and effective graph-based models.

---


### 430. [Grounding Memory Summarization in Utility Intent](https://arxiv.org/abs/2609.33417)

**<font color=#1a73e8>作者：</font>** Zhenyu Lei, Mingjia Shi, Xingbo Fu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing summarizers for memory systems are typically optimized for human-facing criteria such as faithfulness, which misaligns with their true objective: preserving the evidence needed to support future queries. We show that conditioning summarization on query-answer pairs substantially improves answer quality, and that this utility-aware behavior is transferable across queries. Motivated by these findings, we propose MemSuit, a self-distillation framework in which a teacher summarizer, conditioned on observed query-answer pairs, produces utility-aware memory entries that a student learns to reproduce from the raw conversation alone. To prevent collateral erasure where conditioning on a single query-answer pair discards evidence relevant to other plausible queries, the teacher decomposes each block into multiple self-contained entries that preserve distinct query-relevant facets as independently retrievable units. To align the retriever with the compact, fact-dense style of teacher entries, we further fine-tune the embedding model with a contrastive objective supervised by teacher entries. Across a diverse suite of conversational query types, MemSuit consistently outperforms state-of-the-art baselines, confirming the value of grounding memory in downstream utility.

---


### 431. [TT-VidT: Decoupling the Temporal Axis for Efficient Motion-Centric Video Pretraining](https://arxiv.org/abs/2609.33419)

**<font color=#1a73e8>作者：</font>** Shih-Ying Yeh, Daniel Z. Kaplan, Xuehai Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Comparisons in video self-supervised learning often evaluate complete training recipes rather than isolating the method itself: architecture, objective, data exposure, schedule, scale, and decoder capacity can all vary at once. This makes it hard to identify which choices yield motion-prioritized representations, whose gains concentrate on frame-to-frame change while retaining useful appearance. We address this with a matched $4 \times 6 = 24$ architecture-objective study at roughly 170M ~ 190M encoder scale on $\sim$1.7M OpenVid and Moments-in-Time v2 clips for 8 epochs, and propose TT-VidT. TT-VidT combines a DINOv3-initialized ViT-B/16 per-frame spatial path with a compact Temporal Transfer Layer, trained by Diff Compression to reconstruct target frames from a first-frame appearance anchor and frame-specific motion tokens. The sweep shows that TT3D with Diff Compression, not either component alone, enters the strongest motion-sensitive regime, and decoder ablations favor a compact video-pretrained decoder. In final comparison, TT-VidT leads Jester, Something-Something V2, ARID, and Diving48 fine-tuning simultaneously, improving over the strongest non-TT row by 54% ~ 121%, while using 48% fewer encoder FLOPs than DisMo and 55% fewer than VideoMAE or V-JEPA2. HMDB51, IARD, and EPIC-Kitchens bound the claim.

---


### 432. [A Light Bilevel Refinement Aligns Self-Supervised Representations for Stronger Task-Specific Learning](https://arxiv.org/abs/2609.33424)

**<font color=#1a73e8>作者：</font>** Gustav Wagner Zakarias, Zheng-Hua Tan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-supervised pretraining learns representations that are broadly transferable across downstream tasks, yet direct fine-tuning can be suboptimal due to misalignment between self-supervised and downstream task objectives, potentially degrading pretrained features beneficial to the downstream task. The BiSSL framework addressed this by introducing a transitional training stage formulated as a bilevel optimization problem, in which the downstream task objective guides the self-supervised learning process in refining pretrained representations to better facilitate subsequent fine-tuning. However, BiSSL relies on conventional bilevel optimization solving techniques whose costly implicit hypergradient approximations render the method increasingly impractical for contemporary model architectures. To make it efficient and scalable, we introduce BiSSLight, which combines M-FAC-based implicit gradient approximation with parameter-efficient fine-tuning via LoRA, enabling efficient application at larger scales that were previously impractical. Evaluation across multiple downstream tasks and contemporary model architectures shows that BiSSLight consistently improves downstream performance, with gains becoming more pronounced as model size increases despite stronger baselines. The method is highly computationally efficient, reducing computation time by more than a factor of ten compared to its predecessor on a ViT-H backbone.

---


### 433. [TeacherGRPO: Closing the Capacity Gap in Reasoning Distillation via Teacher Alignment](https://arxiv.org/abs/2609.33426)

**<font color=#1a73e8>作者：</font>** Zhenyu Lei, Zihan Chen, Yaochen Zhu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning distillation from powerful teacher models to smaller students faces the Gap Curse: as teachers grow more sophisticated, their complex distributions increasingly diverge from what students can approximate, causing performance degradation. Existing mitigation strategies either filter out challenging examples through data selection or introduce weaker intermediate assistant models, inherently compromising supervision coverage or quality. We propose Teacher Alignment, which directly adapts the teacher toward the student's distribution without discarding data or degrading reasoning quality. However, naive alignment through standard knowledge distillation triggers catastrophic collapse of the teacher's reasoning capabilities. To address this, we reformulate teacher alignment as reinforcement learning and introduce TeacherGRPO, built on Group Relative Policy Optimization with two key innovations: (i) Curriculum Selective Alignment applies dual token- and distribution-level curricula to focus rewards on high-signal reasoning gaps while filtering noise from trivial tokens and uncertain tail distributions, and (ii) Importance-Adaptive Length Regularization selectively penalizes verbose redundancy while preserving pedagogically critical reasoning steps. The aligned teacher then distills knowledge to students via standard pipelines. Extensive experiments show TeacherGRPO significantly outperforms baselines across diverse reasoning benchmarks and distillation methods. Our code is available at this https URL.

---


### 434. [Temporal Graph Learning of Wearable Actigraphy and Sleep Traces for Modelling Adolescent Crystallized Intelligence](https://arxiv.org/abs/2609.33428)

**<font color=#1a73e8>作者：</font>** Md. Tanvir Rahman, Nabil Anan Orka, Asaduzzaman Khan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Wearable actigraphy offers a scalable, ecologically valid alternative to episodic clinical assessment. However, predicting continuous adolescent crystallized intelligence ($G_c$) from such traces remains challenging due to irregular device adherence and complex behavioral-environmental interactions. We address this using daily summary data derived from 21-day Fitbit records of 6,091 adolescents in the Adolescent Brain Cognitive Development Study (Release 5.1). We propose SATURN, a Sleep-Activity Temporal Unified Regression Network. It represents participants as 21-node temporal graphs encoding daily behaviors and temporal adjacency. To prevent imputation artifacts, invalid-day edges are dynamically pruned during forward passes. Node embeddings are refined via residual GATv2 layers, aggregated through masked attention pooling, and fused with sociodemographic covariates. Under family-controlled, age-sex-BMI-stratified cross-validation, SATURN achieves $R^2 = 0.2783 \pm 0.0127$, consistently improving upon flattened machine learning (Gradient Boosting, $R^2 = 0.2372$) and sequential deep learning (BiLSTM, $R^2 = 0.2688$) baselines. Explainability analyses identify light activity, metabolic equivalents, and sleep duration as dominant predictors, while Monte Carlo dropout and subgroup analyses confirm equitable performance across sociodemographic strata. Ultimately, SATURN establishes a rigorous computational framework for digital cognitive phenotyping, offering a scalable pathway to complement traditional assessments by highlighting macro-level behavioral anomalies.

---


### 435. [TC-ADA: One-Shot Active Domain Adaptation for Semantic Segmentation](https://arxiv.org/abs/2609.33432)

**<font color=#1a73e8>作者：</font>** Weihao Yan, Yeqiang Qian, Yueyuan Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Manual dense annotation remains a major obstacle to deploying semantic segmentation models in new driving environments. Active domain adaptation (ADA) seeks label-efficient transfer by annotating only a selected portion of the target domain. Existing ADA methods commonly implement this process through multiple rounds of acquisition, annotation, and retraining. We study a practical one-shot image-level setting that selects and densely annotates a fixed target subset in a single round, followed by uninterrupted adaptation. Within this setting, we develop Target-Calibrated Active Domain Adaptation (TC-ADA) as a joint design of complete-image acquisition and target-calibrated adaptation. Stage~1 uses visual representations from a vision foundation model (VFM) together with semantic predictions from a fixed unsupervised domain adaptation model to select representative and informative target images without target annotations. Stage~2 jointly uses labeled source data, labeled target data, and the remaining unlabeled target data, while calibrating source and target supervision under limited target labels. Extensive experiments across five synthetic-to-real and real-to-real driving transfers show consistent improvements over representative ADA baselines. With only 23 to 46 labeled target images on four transfers and 140 on Mapillary, TC-ADA stays within 1.9 mean intersection over union (mIoU) points of target-only full supervision. Code will be available at this https URL.

---


### 436. [SMAT: Simple and Efficient Merge-Aware Training](https://arxiv.org/abs/2609.33437)

**<font color=#1a73e8>作者：</font>** Yanggan Gu, Yuanyi Wang, Zhen Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model merging integrates the capabilities of multiple experts without joint retraining, but standard expert training optimizes task loss alone and does not guarantee good performance after merging. Merge-aware training (MAT) aims to improve merged performance, but existing methods do not fully account for common merging operations and add training cost. We observe that, from an expert's perspective, common merging methods can be described by three operations: Scale reweights its own update, Mask removes selected coordinates, and Perturb adds updates from other experts. Based on this view, we introduce SMAT (Simple MAT), which jointly optimizes expert loss and expected loss at simulated merged parameters generated by sampling scaling coefficients, masks, and additive noise. We further introduce periodic scheduling, kernel fusion, and parameter storage switching to make SMAT efficient, with one forward and one backward pass per step. Across four language and vision-language backbones, SMAT improves the mean score across five merging methods by 1.07-2.16 points over the strongest baseline for each backbone, with less than 2% training-time overhead over standard fine-tuning.

---


### 437. [MAC-Net: A Multi-Task Deep Learning Framework for Modeling Cognitive Function From Task-Based fMRI](https://arxiv.org/abs/2609.33440)

**<font color=#1a73e8>作者：</font>** Md. Tanvir Rahman, Nabil Anan Orka, Asaduzzaman Khan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Objective cognitive assessment from neural signals supports neurorehabilitation, but individual-level prediction from task-based fMRI (tfMRI) remains difficult because neural features coexist with substantial demographic and scanner-related variation. We present the Multi-task Activation and Contrast Network (MAC-Net), a covariate-aware deep learning framework for modeling individual cognitive function from regional tfMRI. By isolating tfMRI features into a dedicated neural pathway and restricting participant variables to a terminal late-fusion pathway, MAC-Net prevents dominant covariates from suppressing high-dimensional clinical representations during feature learning. Evaluating baseline data from 6,500 Adolescent Brain Cognitive Development Study participants under family-aware cross-validation, MAC-Net was benchmarked against linear models, random forests, and alternative deep architectures. The N-back plus Monetary Incentive Delay configuration achieved $R^{2}$ values of 0.174, 0.238, and 0.277 for fluid, crystallized, and total cognition, outperforming covariate-only baselines (0.178) and alternative deep models (0.217). N-back was the most informative paradigm, whereas incorporating the Stop Signal Task marginally degraded performance. Feature attributions via Integrated Gradients, DeepLIFT, and Input Gradient were highly concordant, localizing working-memory-related frontal, parietal, and cingulate regions. These findings demonstrate that covariate-aware multi-task modeling yields reproducible cognitive-function estimations, establishing a robust neural engineering framework for clinical translation.

---


### 438. [Elucidating the Design Space of Regression-based Diffusion Reinforcement Learning](https://arxiv.org/abs/2609.33444)

**<font color=#1a73e8>作者：</font>** Toyota Li, David Zhao, Alan Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A nascent family of methods that forgoes the policy gradient and reweights a supervised regression instead has garnered momentum in reinforcement learning for diffusion and flow models. DiffusionNFT, FlowAWR, and RAM are representative regimes with contrasting motivations. It is yet opaque what, if anything, they share. We substantiate that each is the solution of one divergence-constrained reward-maximization problem, and they are differentiated only by the convex generator that defines the constraint. Under the unified modeling framework, we unravel the relaxations that prior art made during building the advantage-embedded regression target: approximating the KKT condition and posterior normalizer for the linear and exponential tilt shapes DiffusionNFT and FlowAWR respectively, while preserving the exact sparsemax projection onto the probability simplex for linear tilt leads to another superior model type in this work. Beyond the theoretical underpinnings, we further empirically investigate the design space and shed light on the training recipe for regression-style diffusion RL. Retaining the merits discovered during our exploration gives rise to DiffusionRFT, our paradigm that converges faster, trains more stably, and attains the top performance.

---


### 439. [Concept Score Relearning: A Unified Cross-Architecture Attack on Concept Erasure](https://arxiv.org/abs/2609.33445)

**<font color=#1a73e8>作者：</font>** Hong Xi Tae, Jiaming Zhang, Wenwen He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Concept erasure aims to suppress undesirable knowledge in text-to-image generative models. However, existing robustness evaluations typically rely on relearning attacks tailored to specific model architectures. We study concept reactivation across two substantially different generative paradigms: noise-prediction U-Nets and flow-matching Transformers. We introduce \textbf{Concept Score Relearning (CSR)}, a unified parameter-level framework that reactivates erased concepts by optimizing each model within its native prediction space. CSR requires no external target-concept image dataset and applies the same concept-directed objective to both U-Net-based Stable Diffusion and Transformer-based FLUX. Experiments across diverse concepts and multiple erasure methods demonstrate consistent concept reactivation across both architectures, highlighting the cross-architecture applicability of CSR and the persistent recoverability of apparently erased concepts. For strict nudity, CSR reaches average ASRs of 50.47\% on FLUX and 40.29\% on Stable Diffusion, consistently ranking first across all evaluated safety settings.

---


### 440. [A Free Knob: Decoupling Calibration and Predictive Skill in Threshold-Based Evaluation](https://arxiv.org/abs/2609.33457)

**<font color=#1a73e8>作者：</font>** Md Tanveer Hossain Munim, Bijoy Ahmed Saiem, Al-Amin Sany 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many dense-prediction benchmarks evaluate rare events by pooling prediction and target over spatial blocks, thresholding each, and scoring the contingency table. At a fixed rare operating point, the max-pooled Critical Success Index (CSI) confounds spatial discrimination with amplitude calibration: sharp observations promote many blocks above threshold, while attenuated predictions from squared-error regression leave the same blocks below it. We repurpose classical monotone calibration as a symmetric audit: a post-hoc transform fitted on held-out data and applied separately to each system. The transform cannot reverse pixel ordering, so any contrast it reproduces cannot establish improved spatial ranking. On SEVIR, two released checkpoints of one architecture differ by -29.5% in extreme-threshold CSI before the control and by +5.3% after it. Across 450 pairwise contrasts among 6 systems, the difference in pooled frequency-bias deviation is associated with how far the CSI contrast moves under the control (r = +0.796), and 51 contrasts reverse sign. At CasCast's published extreme-event operating point, the cascade-over-backbone CSI gap falls from 0.1601 to 0.0339, a 78.8% reduction; the remaining gap stays positive. The effect persists when the transform is fitted on a window before the test period, and calibration also reveals advantages hidden by a better-calibrated baseline. On geostationary infrared imagery the relative gain grows as events become rarer, crowd counting reproduces the bias-gain relationship under patch-sum pooling, and semantic segmentation, where frequency bias is already near one, shows little average change. The confound therefore requires both a fixed operating point and a training regime that leaves the output miscalibrated there. We recommend reporting pooled frequency bias and a symmetric held-out FreeKnob Audit alongside rare-event pool-and-threshold scores.

---


### 441. [Geometric Identification in Predict-Then-Optimize Learning](https://arxiv.org/abs/2609.33472)

**<font color=#1a73e8>作者：</font>** Jiaxiao Xu, Changhong Mou, Keji Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decision-focused surrogates can recover downstream decisions without identifying the quotient report. We characterize the equality set of the convex Smart Predict-then-Optimize surrogate (SPO+) population risk. Under central symmetry, the centered mean class is the unique Bayes minimizer exactly when every nonzero effective displacement makes the old optimizer leave the shifted optimal face with positive probability. This condition separates face crossing from selected-oracle disagreement and gives quantitative local coercivity. Without symmetry, strict crossing alone need not identify the mean; selection balance with reflected crossing restores quotient-report identification, and conditional versions extend the result to measurable predictors. These are population statements, without finite-sample report-recovery or generic transfer-regret guarantees. Closed-form mechanisms reproduce the analytic identities and rates. Portfolio, complete-matrix KuaiRec, and Energy/Storage studies measure predictive fidelity, shifted regret, and fitted-report geometry. A known data-generating process (DGP) companion retains their application geometries while isolating conditional-mean recovery and crossing, without testing the original observational assumptions.

---


### 442. [Predicting Block-Coordinate Performance via Cross-Curvature](https://arxiv.org/abs/2609.33489)

**<font color=#1a73e8>作者：</font>** Shengkun Zhu, Jinshan Zeng, Zhiqiang Kou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Simultaneous and sequential block updates are two basic optimization strategies used across machine learning, such as neural-network training, federated learning, and low-rank adaptation. Choosing between them is difficult because their relative advantage depends on both the objective geometry and the number of iterations. We develop a unified theory for comparing Jacobi (JC), Gauss--Seidel (GS), and partially sequential deterministic block-gradient updates. Our analysis expresses the one-step loss difference through cross-block curvature, with an $O(\eta^3)$ remainder, where $\eta$ is the learning rate. We derive a signed loss comparison after $K$ iterations with $O(K\eta^3)$ error under regularity conditions and $\eta K\le T$ for fixed $T$, identifying the better method when the predicted difference exceeds this error. We evaluate these formulas along observed training trajectories across different machine learning settings. Over 500 iterations, our theory correctly identifies the lower-loss method in 98.0\% of iterations for the neural network, 83.4\% for federated learning, and 97.6\% for LoRA. Applying the loss recursion at each step using the measured parameter difference raises these rates to 100.0\%, 93.2\%, and 99.6\%, respectively.

---


### 443. [Federated Multi-Modal Human Activity Recognition using Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2609.33492)

**<font color=#1a73e8>作者：</font>** Debasmita Dey, Tanmay Sen, Himel Mallick  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human Activity Recognition (HAR) from heterogeneous wearable sensors is fundamental to the Internet of Health Things (IoHT), supporting rehabilitation, elderly care, and smart healthcare. Existing multimodal fusion methods often assign fixed equal weights to sensor streams, overlooking differences in modality importance, acquisition cost, and sensor quality, which can vary due to movement, incorrect placement, or temporary blockage. We propose an adaptive and cost-aware multimodal HAR framework based on multi-agent reinforcement learning for centralized HAR and extend it to federated learning as FedMHAR. In the centralized setting, multimodal fusion is formulated as a cooperative Multi-Agent Reinforcement Learning (MARL) problem, where each sensing modality is assigned a PPO-based agent that learns per-sample fusion weights, enabling the model to emphasize informative modalities while down-weighting costly sensors when cheaper alternatives provide sufficient information. In the federated setting, we introduce BiFL-PPO, a bidirectional federated optimization strategy in which a server-side PPO policy learns client-specific trust weights and feeds them back to adapt local learning rates and proximal regularization. Unlike round-level optimization, BiFL-PPO uses dense batch-level rewards for more frequent feedback and stable training under heterogeneous client data. Evaluation on the MEx Rehabilitation and UTD Multimodal Human Action datasets shows that the centralized framework achieves 87.30% and 94.98% accuracy, respectively, outperforming conventional fusion methods and state-of-the-art HAR models. FedMHAR achieves 79.74% and 77.49% in the federated setting, consistently surpassing FedAvg, FedProx, FedBN, FedNova, and AdaFedProx, while providing more stable performance and reducing sensor acquisition cost.

---


### 444. [Chameleon: Dynamic Format Adapter for Efficient Diffusion](https://arxiv.org/abs/2609.33496)

**<font color=#1a73e8>作者：</font>** Arnab Sanyal, Sandeep Chinchali  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) is the standard way to run modern diffusion models on memory-constrained accelerators, yet every existing diffusion PTQ scheme fixes the $\mathit{number\ format}$ in advance and only tunes the scale, zero point, or per-layer bit-width. At a fixed bit-width the best format depends on the distribution being encoded, and that distribution differs across weight channels, across layers, and along the diffusion timestep, where activation distributions slide from heavy-tailed and noise-dominated to tightly clustered and structured. We propose Chameleon, a PTQ framework that holds the bit-width fixed and treats the format itself as a discrete variable, chosen per weight channel and per (layer, timestep bucket) activation tensor. Activation formats come from {INT8, FP8 E4M3, FP8 E5M2, MXFP8, MXINT8}, selected ahead of time from two cheap statistics (empirical kurtosis and the closed-form diffusion SNR) and stored in a lookup table; weight formats come from {INT8, MXINT8} at 8 bits or {INT4, NF4, FP4 E2M1, MXINT4, MXFP4} at 4 bits, selected offline by reconstruction error. An architectural fork adapts the same selection layer to multi-step UNets, single-step distilled models, and Diffusion Transformers. Across SDXL, SDXL-Turbo, and PixArt-$\alpha$ on COCO-2014, Chameleon achieves the best FID in all six backbone $\times$ bit-width settings, with CLIP within 0.24 of the FP16 reference and the best of all quantized methods at $W_{4}A_{8}$.

---


### 445. [Hamiltonian JEPA: Action-Conditioned World Models with an Inherited Control State](https://arxiv.org/abs/2609.33497)

**<font color=#1a73e8>作者：</font>** Tamim Zoabi, Ameen Ali, Lior Wolf  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Planning from pixels needs more than a latent space that is stable and predictable. The state the planner scores must also be organized by how actions move the system. Joint-embedding predictive architectures (JEPAs) avoid pixel reconstruction by predicting future representations, but existing action-conditioned JEPAs ask one embedding to serve both perception and control. We introduce H-JEPA, which separates the two. A wide perceptual code is regularized toward a well-scaled isotropic geometry with a Bures-Wasserstein prior, and a fixed orthonormal slice of that code is the control state, which inherits the code's covariance without any objective of its own. The state evolves under phase-conditioned dissipative port-Hamiltonian dynamics whose input port has orthonormal columns. Port-inverse consistency (PIC) reads the executed action back through the transpose of that port. We show that this readout is exactly the rollout error projected onto the port directions, so PIC is a parameter-free reweighting of prediction error and not an auxiliary action decoder. Untying the readout from the port breaks this identity and loses half of the gain. H-JEPA matches or exceeds reconstruction-free baselines, including the action-decoding Delta-JEPA, on four pixel-based control benchmarks after at most $10$ training epochs, and its largest gain is on OGB-Cube ($91.9$ against $79.3$ percent). Ablations on PushT and OGB-Cube separate the contributions of the structured predictor, PIC, the prediction horizon, the state rank, and the anti-collapse prior.

---


### 446. [The cost of useful natural gradient updates](https://arxiv.org/abs/2609.33499)

**<font color=#1a73e8>作者：</font>** Subhransu S. Bhattacharjee, Dylan Campbell, Rahul Shome  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> What information is needed to turn a natural-gradient direction into a useful finite update? Under a population Kullback-Leibler (KL) budget, we call a step useful if it is feasible and loses at most a fraction $\varepsilon$ of the best feasible gain along the direction. We construct a four-state exponential family whose laws share their initial gradient, scalar Fisher information and natural gradient, yet two laws have disjoint useful-step sets. With these quantities supplied exactly and the law otherwise known only through draws, the family's worst-case sample complexity is $\Theta(\log(1/\delta)/(p\varepsilon^2))$ for small $\varepsilon$, where $p$ scales rare-state probabilities and $\delta$ is the failure probability. The budget is fixed and the optimal gain stays bounded away from zero, so the step length, not the direction, carries this cost. For succinctly described event-tilt models, returning a useful step is NP-hard even with the exact natural gradient and efficient exact sampling. Recovering the unit natural gradient to constant error is also NP-hard even in a two-parameter logistic family with Fisher condition number at most 3. We also give matching sample bounds for event tilts, sample bounds for damped Fisher solves and a population-KL certificate for affine classifiers. In frozen-feature classifier heads, stopping at a sampled KL boundary succeeds in about half of the trials, and a 10% KL margin raises joint success above 93% at a KL budget of 0.01. Thus, knowing where to move is not enough: how far to move can carry an update's entire cost.

---


### 447. [Pulseflow: PPG Counterfactual Generation Via Latent Transport](https://arxiv.org/abs/2609.33501)

**<font color=#1a73e8>作者：</font>** Hung Manh Pham, Dong Ma, Bin Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Photoplethysmography (PPG) has become an important modality for continuous cardiovascular monitoring, including atrial fibrillation (AF) detection. However, labeled AF recordings remain limited in many clinical settings, making model adaptation difficult when only limited target data are available. Generative modeling offers a natural way to alleviate this scarcity by synthesizing additional AF signals. Existing approaches, however, mainly generate samples that match the target condition without explicitly modeling how an observed source recording should be transformed, making it difficult to leverage abundant source recordings from a specific population or cohort for targeted augmentation. We introduce PulseFlow, a source-conditioned counterfactual generation framework that combines conditional representation learning with invertible latent transport to edit cardiac rhythm while retaining information from the source. Experiments across two clinical cohorts demonstrate effective rhythm transformation, measurable source correspondence, and improved AF classification under limited labels.

---


### 448. [When Evidence Changes the Subject: Subject-Typed Claim Licensing for Learned Routing](https://arxiv.org/abs/2609.33505)

**<font color=#1a73e8>作者：</font>** Jian Chen, Zixuan Yuan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern learned systems increasingly combine learned components with search, repair, or external solvers. Benchmarks often measure the resulting end-to-end system, while scientific claims may concern only one component, creating an attribution problem: evidence can fail to support the requested component-level claim while still supporting a positive conclusion about the larger system. Existing evidence-to-claim methods primarily calibrate claim strength. We argue that composite systems require a second dimension: scientific subject. We address this problem with subject-typed claim licensing, which separates weaker conclusions about the requested subject from positive but non-substitutive credit about another subject. We instantiate this idea in SCOPE-Routing for preference-conditioned multigraph routing. Non-authors reproducibly apply the declared semantics; held-out review yields fewer reference-relative upward deviations than unstructured review, while the difference from a strong evidence checklist remains unresolved; and a controlled routing study shows that score-optimal and claim-eligible methods can differ while valid hybrid-system credit is preserved. These results motivate treating claim strength and scientific subject as distinct dimensions of evidence-based evaluation.

---


### 449. [What Happens During Autonomous Deep Research After the User Steps Away?](https://arxiv.org/abs/2609.33509)

**<font color=#1a73e8>作者：</font>** Yimin Liu, Yijia Zhang, Yanmin Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In autonomous deep research, a user provides a task and relevant background, then leaves the agent to conduct an extended investigation without further human intervention. We study how this initial user information is reflected in intermediate actions and how these actions relate to final recommendations. We introduce DRaligned, a counterfactual behavioral evaluation framework built on PDR-Bench. By varying one task-relevant user factor while keeping the remaining context fixed, we compare acquisition requests, working drafts, and final reports. Source-grounded extraction, blinded local judgments, and deterministic aggregation yield coarse directional measurements while leaving ambiguous cases unresolved. Our experiments show that strong user-specific delivery can emerge from a largely shared research process: agents investigate similar broad questions but allocate requests differently, and final recommendations distinguish user conditions more clearly than explicit requests do. Reports can also integrate user factors that were not jointly visible during acquisition. In readable draft-to-report comparisons, recommendations often retain their coarse user-specific direction despite substantial rewriting. Final directional differences recur across tested agent models, execution harnesses, and evaluator models, even as execution paths vary. These findings describe how initial user information shapes autonomous research and clarify the relationship between the process an agent follows and the recommendations it delivers.

---


### 450. [Source Anchoring for Physical Consistency in Flow Matching Models](https://arxiv.org/abs/2609.33510)

**<font color=#1a73e8>作者：</font>** Giulia Romoli, Filippo Ruffini, Paolo Soda  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep generative models are used to solve partial differential equations and model distributions of physical system states, but ensuring that the generated samples satisfy the governing laws remains challenging. Projection-based flow-matching methods enforce physics by correcting the flow from an unconstrained noise distribution. These corrections shift the generated samples away from the distribution of target solutions, especially in high noise regions. To address this limitation, we propose Source Anchoring for Physical Consistency (SAPC), a Functional Flow Matching method that encodes the physical constraints into the source noise before generation begins. We evaluate SAPC on five systems governed by partial differential equations, covering six tasks with linear and non-linear dynamics, and compare results against five baselines and the unconstrained backbone. Anchoring the source reduces the need for large corrections that drive samples onto admissible but off-distribution states, and SAPC reproduces the target distributions most accurately on every evaluated task, while matching the constraint precision of the best projection-based baselines. Ablation experiments show that this gain arises from pairing source projection with a matched training objective that regresses toward the projected source. These results identify the source distribution as a key design choice for physically consistent generative modelling.

---


> [!TIP]
> 当前位于：**401-450**（第 9/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-908](./part-19.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
