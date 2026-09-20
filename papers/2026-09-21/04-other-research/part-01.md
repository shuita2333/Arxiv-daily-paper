# 📦 其他研究 | 2026年09月21日

> 本类共 **247** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-247](./part-05.md)

---

### 1. [Modality Discrepancy Transformer for Ambivalence and Hesitancy Recognition](https://arxiv.org/abs/2609.19148)

**<font color=#1a73e8>作者：</font>** Shiyu Luo, Yu Wang, Jiawen Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Ambivalence and hesitancy (A/H) are affective states in which individuals express contradictory signals across facial, vocal, and linguistic channels. Automatically recognising A/H in clinical videos requires detecting cross-modal disagreement -- the signal that standard fusion methods suppress. Based on the conflict-aware multimodal fusion framework of Bekhouche et al., we present the Modality Discrepancy Transformer (MDT). MDT enriches the original 6-token design to a 9-token representation comprising three modality embeddings, three absolute-difference features, and three Hadamard-product discrepancy features learned through linear projections. These nine tokens undergo Transformer self-attention, with FiLM-based text-conditioned modulation and LoRA fine-tuning as core architectural components. A text-guided late fusion branch blends a text-only auxiliary head with the full multimodal output at inference. On the BAH dataset from the 3rd ABAW Challenge, MDT achieves 0.7408 Macro F1 on the labelled test split and 0.7368 on the private leaderboard, outperforming the strongest published baseline by over 10 points while training in under 20 minutes on a single GPU.

---


### 2. [Stop Removing Stopwords: How an Inherited Preprocessing Default Distorts Legal Text-as-Data](https://arxiv.org/abs/2609.19153)

**<font color=#1a73e8>作者：</font>** Gregory M. Dickinson  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Empirical legal scholarship increasingly treats judicial text as data, and much of it still runs on sparse, interpretable pipelines -- TF-IDF features and linear classifiers -- because the textual feature is often the object of study, not merely a means to a prediction. Yet these pipelines inherit a chain of preprocessing defaults from mid-century information retrieval that were never validated against classification accuracy, the most entrenched being stopword removal. This study introduces an exhaustive single-word ablation that measures a preprocessing step's effect directly against the downstream objective, and applies it to stopword removal as the hardest case to dislodge. Matching Supreme Court Database labels to Caselaw Access Project opinion texts, it examines two binary tasks that bracket F1 headroom, ideological direction (no-removal baseline F1 ~ 0.68) and constitutional versus non-constitutional law type (~ 0.92), across 7,668 and 7,001 opinions. For each task the analysis approximates the best stoplist any expert could build, removing each of roughly 18,500 candidate words and measuring the effect directly. Three findings follow: generic stoplists in common use fall below the no-removal baseline in every test; even optimized stoplists are statistically indistinguishable from removing nothing; and meta-models trained on word-level features cannot predict which removals help, so list curation has nothing to target. The method generalizes to any inherited preprocessing default, and the result is a caution specific to interpretable legal text-as-data: a step that silently reshapes which features a model sees can distort the very doctrinal and ideological signal such research exists to recover. Leaving stopwords in place is a question of measurement validity.

---


### 3. [Regularized Emphatic Temporal-Difference Learning: Stability under Constant Stepsizes](https://arxiv.org/abs/2609.19170)

**<font color=#1a73e8>作者：</font>** Xingguo Chen, Zhaohui Wu, Jinguo Ye 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Emphatic temporal-difference learning (ETD) stabilizes the expected off-policy TD update and changes its projection geometry, but neither property determines constant-stepsize sampled dynamics. We construct an ergodic two-state counterexample in which the ETD mean map contracts while the sampled product has a positive top Lyapunov exponent. Regenerative-cycle analysis separates this sign from the infinite variance of the follow-on trace. We introduce regularized emphatic TD (RETD), a normalized first-order post-shock repair that leaves the trace and importance ratios unchanged, stores the emphatic TD signal in a leaky scalar state, and releases a delayed correction. RETD's raw equilibrium is an affine shift of the ETD equilibrium; single- and two-regularization readouts recover the ETD fixed point exactly. We prove almost-sure convergence for harmonic diminishing stepsizes and a conditional constant-stepsize moment-contraction result from a Markovian random-product bound. RETD has certified negative exponents on the two-state construction and one Baird point, whereas the positive Baird ETD sign remains numerical. Paired 10,000-run experiments validate both separations, fixed-point recovery, a nonmonotone stability region, and task dependence. RETD changes post-shock dynamics; it does not reduce the shared follow-on-trace variance.

---


### 4. [CC-OPI: Online Distributed Task Allocation for UAV Swarms under Communication Constraints](https://arxiv.org/abs/2609.19208)

**<font color=#1a73e8>作者：</font>** Biao Liu, Tong Zhang  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In multi-robot missions such as post-disaster search and rescue, a short communication range fragments a swarm of Unmanned Aerial Vehicles (UAVs) into transient information islands. Under such intermittent connectivity, the prevailing "allocate-then-execute" paradigm--which requires global consensus before any physical movement--breaks down. This paper proposes the Communication-Constrained Online Performance Impact (CC-OPI) algorithm, an event-driven method that interleaves task negotiation with physical execution. CC-OPI replans only at discrete physical and topological events and integrates two further elements. The first is a pair of cost-evaluation metrics adapted to dynamic topologies--one with a spatial locality penalty that promotes regionalized operation, the other with a deadline-aware urgency term--complemented by a non-preemptive state lock that shields each UAV's ongoing action. The second is a decentralized fault-tolerance layer that pairs version-based state synchronization with a global-time-driven emergency pool. We establish that CC-OPI terminates in finite time, free of stale-completion deadlock and of unbounded reassignment within the mission horizon. In simulations at a 250 m communication radius, CC-OPI sustains a task completion rate of about 0.80: it leads a matched online execution of the unmodified Performance Impact (PI) and Consensus-Based Bundle Algorithm (CBBA) rules by about seven percentage points, exceeds the naively transferred static baselines by roughly 20 points, and remains within several points of PI and CBBA under full connectivity. Within the tested settings, CC-OPI degrades gracefully as connectivity weakens and absorbs packet loss, terrain occlusion, and runtime task arrival. The price is more messages and some redundant travel--a deliberate trade-off of efficiency for robustness.

---


### 5. [Generative Query Suggestion via Intent Coverage and Query-Level Credit Assignment](https://arxiv.org/abs/2609.19209)

**<font color=#1a73e8>作者：</font>** Xinpeng Liu, Lu Ma, Jiayi Qiao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative query suggestion aims to enhance user engagement by anticipating user intents and recommending relevant follow-up queries. A central challenge is to generate slates whose individual queries are useful while the slate covers distinct intents. We propose an Intent-Driven Query Suggestion Framework with dual-stage optimization. First, intent-aware diversity modeling constructs intent-aligned supervised fine-tuning (SFT) data and uses an Intent-Aware Diversity Reward to optimize intent coverage. Second, query-level credit assignment routes individual quality signals to the corresponding query tokens while sharing a slate-level diversity signal across the slate. Experiments on a large-scale production dataset, including online A/B testing and offline evaluation, show improvements in click-through rate, query quality, and intent coverage.

---


### 6. [What Do Current Systematic Generalization Tasks Miss? A Reasoning-Centered Analysis](https://arxiv.org/abs/2609.19212)

**<font color=#1a73e8>作者：</font>** Chengwen Qi, Deheng Ye, Yatao Bian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Systematic generalization, the ability to solve novel problems by recombining known atomic elements, is central to human intelligence but difficult to study rigorously under controlled settings. Existing studies therefore rely on simplifications such as approximately linear action composition, productivity-based tests, and action-explicit goals, which make systematic generalization easier to study but omit some essential aspects of this capability. To characterize what these simplifications miss, we adopt a reasoning-centered lens and introduce TranSGrid, a testbed that brings deductive, inductive, and abductive reasoning together within a unified task. Experiments with seven Transformers on 4,800 TranSGrid instances show that all models perform much worse on TranSGrid than on a held-out test set: the largest model solves 79.6% of the test set, but only 55.3% of TranSGrid and 15.8% of the hardest subset. The gap remains within the training length range, showing that productivity alone is not sufficient to evaluate systematic generalization. Additionally, we reintroduce the other two simplifications into TranSGrid: one variant makes actions compose almost linearly (reducing the inductive demand), the other makes goals action-explicit (reducing the abductive one). In both, solve rates return to roughly the test set level, showing that either simplification alone is enough to reduce TranSGrid to an ordinary held-out test set. Together, our results show that existing tasks reduce either or both of the inductive and abductive demands, and that comprehensively measuring systematic generalization requires a task that involves all three forms of reasoning.

---


### 7. [''Bless his heart... he thought all we did was push a button": Understanding Worker Challenges with U.S. Election Technology](https://arxiv.org/abs/2609.19233)

**<font color=#1a73e8>作者：</font>** Delaney Gomen, Josiah Hester, Naveena Karusala 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper explores how the technologies U.S. election officials depend on also challenge their work. Every election, misleading narratives stem from errors that occur while using election technology, threatening election official safety and eroding faith in elections. We seek to understand the impact of these challenges directly from worker perspectives. This paper presents a qualitative analysis using combined interview and survey data from a total of 50 election officials representing 20 states. Our findings present design as a substantial factor in mistakes when using election technology, but other obstacles, like lack of funding and technical support, also strain operations. We show how election technology design can lead to harms for election officials and connect those harms to their negative effects on democracy. Our work emphasizes the potential for researchers in human-centered computing to support U.S. election officials-and democracy-by working towards better usability across election technologies.

---


### 8. [RAUL: Reference-Assisted Ureteroscopy Localization for Skill Assessment](https://arxiv.org/abs/2609.19236)

**<font color=#1a73e8>作者：</font>** Fangjie Li, Mai Bui, Charan Mohan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Objective: Incomplete navigation of anatomy during ureteroscopic kidney stone surgeries can contribute to repeat interventions. While skilled surgeons have lower reintervention rates, there are no objective metrics to quantify scope-navigation performance to evaluate when a trainee becomes skilled. This work aims to recover ureteroscope trajectories from endoscopic video and derive navigation metrics to quantify differences in skill. Methods: We propose RAUL, a reference-assisted reconstruction framework for recovering ureteroscope trajectories from ureteroscope videos only in phantoms. For each phantom, we use a slow, high-quality reference exploration video to generate a reference reconstruction. We localize subsequent exploration videos against this reference. We evaluate localization accuracy against electromagnetically tracked scope pose. We compute navigation metrics from phantom exploration trajectories to compare surgical residents across experience levels. Results: The proposed reference-assisted framework achieves a mean translation root mean square error of $0.5 \pm 0.1$ mm across 9 phantoms. Compared to standard Structure-from-Motion (SfM), the proposed pipeline increases frame-wise localization coverage from $50.5 \pm 14.9\%$ to $86.1 \pm 7.2\%$ of all video frames. The reconstructed trajectories revealed significant differences between high- and low-experience trainees in established navigation metrics. Conclusion: RAUL enables substantially more complete recovery of ureteroscope trajectories from videos compared to standard SfM pipelines, enabling trajectory-based skill assessment without additional tracking equipment. Significance: To the best of our knowledge, this is the first use of video-only recovery of ureteroscope trajectories without external tracking sensors for skill assessment, supporting scalable automated assessment of ureteroscopy navigation skill.

---


### 9. [YNU-HPCC at SemEval-2025 Task 11: Bridging the Gap in Text-Based Emotion Using Multiple Prediction Headers](https://arxiv.org/abs/2609.19238)

**<font color=#1a73e8>作者：</font>** Hao Yang, Jin Wang, Xuejie Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper describes the participation of the YNU-HPCC team in subtask A of task 11, Bridging the Gap in Text-Based Emotion at SemEval-2025. Our best-performing system employs the RoBERTa (Robustly Optimized BERT Approach) model, an improved version of BERT that utilizes the Transformer encoder architecture. We enhanced the output head to allow the model to process one emotion simultaneously. We obtained the official ranking score (0.44), including results from all languages. The entire dataset was translated into English using Google Translate to facilitate subsequent processing. Through probabilistic and attention analyses, we found that (I) a single prediction head performs better than six heads predicting six emotions simultaneously, and (II) training on a uniformly translated English dataset yields better results than using the original dataset. The code is available at: this https URL.

---


### 10. [Randomized SVD Approximations for Spectral Co-Clustering of Word-Document Matrices](https://arxiv.org/abs/2609.19243)

**<font color=#1a73e8>作者：</font>** Fateme Mazdarani, Carlos Toxtli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spectral co-clustering is a useful tool for discovering latent structure in word-document matrices, but its reliance on singular value decomposition (SVD) can make standard formulations expensive on high-dimensional data. This paper presents two randomized approximations for normalized spectral co-clustering of bipartite text data when the numbers of document and word clusters may differ. The first method uses randomized SVD through random projection, while the second combines partial SVD with element-wise random sampling. Across real-world and synthetic datasets, both methods reduce runtime relative to the full-SVD baseline, but their behavior depends on matrix sparsity. The random projection method is the more reliable approximation across the tested settings, whereas the sampling-based method is most useful on denser matrices and provides limited benefit on already sparse text data. These results show that randomized approximations for spectral co-clustering should be selected according to the underlying structure of the data.

---


### 11. [Radio-Frequency Convolutional Neural Networks](https://arxiv.org/abs/2609.19279)

**<font color=#1a73e8>作者：</font>** Zhihui Gao, Shi-Yuan Ma, Yiran Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Running artificial intelligence (AI) models directly on edge devices such as smartphones, wearables, and drones offers low latency, pervasive scalability, and data privacy, but these devices rarely carry the computing capability that modern neural networks demand. Edge accelerators have been developed in response, yet each adds computing hardware to devices already constrained in size, weight, power, and cost (SWaP-C). An alternative lies in what these devices already carry: the frequency mixer in every wireless radio multiplies signals in time, natively performing convolution in the frequency domain. Here we introduce radio-frequency convolutional neural networks (RF-CNNs), which repurpose existing communication hardware for CNN inference. Multi-channel convolutions are mapped onto frequency tones for a passive mixer to execute in a single pass. We experimentally demonstrate that RF-CNN runs deep CNNs up to 26.4 million parameters and nine layers from classification of wireless signals and images to controllable image generation, close to full-precision performance. Because the weights arrive over the air and the analog hardware is shared with communication, the edge device spends energy only on data preparation and readout-down to 0.72 femtojoules per multiply-accumulate, two orders of magnitude less than it would cost on an added digital processor. These results suggest that deployed wireless infrastructure can bring efficient, state-of-the-art AI inference to the billions of devices it already connects.

---


### 12. [Learning-Induced Dynamical Transition in Recurrent Neural Networks](https://arxiv.org/abs/2609.19288)

**<font color=#1a73e8>作者：</font>** Varun Vaidya  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning in recurrent neural networks can fundamentally reshape their underlying dynamics, transforming initially chaotic activity into stable task-dependent behavior. We develop a non-equilibrium dynamical mean-field theory(DMFT) to describe this transition during learning. We show that a slow feedback-driven learning process generates an evolving effective feedback strength that drives the network through a transition from chaotic to stable dynamics defined by a bifurcation of the DMFT solution. By deriving the two-time correlation function throughout learning, we identify a critical feedback strength and a corresponding learning rate dependent critical time separating these regimes. The transition arises from the progressive deformation of an effective dynamical landscape by the growing learned feedback structure. Starting from the untrained state, the theory predicts the time evolution of the network output during training and shows quantitative agreement with numerical simulations.

---


### 13. [MuTable: Composable and Reusable Table Transformations for In-Situ Data Exploration](https://arxiv.org/abs/2609.19294)

**<font color=#1a73e8>作者：</font>** Fuling Sun, Devamardeep Hayatpur, Jane L. E 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Tables are central to data work to support precise lookup and full detail, but they can be limiting for overview and pattern-finding tasks. Visualizations are then created to gain richer perceptual support. In practice, moving between tables and charts often requires maintaining parallel representations, introducing context switching, and extra coordination work. Building on prior hybrid table-visualization systems, we present MuTable, a prototype that reifies transformations as persistent, composable, and reusable modifiers to support in-situ data exploration. Users can reshape the table while retaining and adapting intermediate forms as their questions evolve. An expert interview with eight data workers suggests that MuTable can support coordination between representations, rapid exploration, and greater user agency in constructing visualizations, as a low-commitment exploration space.

---


### 14. [Personalized Federated Hierarchical Gaussian Processes for Privacy-Preserving Modeling of Heterogeneous Distributed Systems](https://arxiv.org/abs/2609.19337)

**<font color=#1a73e8>作者：</font>** Xianjian Xie, Hao Yan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present Personalized Federated Hierarchical Gaussian Processes (pFedHGP) for probabilistic regression and classification when data are distributed across heterogeneous clients. Each client's latent function decomposes into (i) a shared global component, (ii) a client-specific deviation that shares the global kernel structure, and (iii) a flexible local residual. Sparse inducing-variable approximations and federated variational inference keep raw data local while the server synchronizes only low-dimensional statistics for the shared component. Full predictive distributions support uncertainty-aware decisions. In application studies, pFedHGP attains perfect fault classification in press tonnage monitoring using 13.77% of labeled cycles and recovers geographic zones in federated air-quality modeling without centralizing station-level time series. An Instantaneous Linear Mixing Model viewpoint links the hierarchy to multi-output Gaussian processes for correlated sensors.

---


### 15. [Scaling Zero Knowledge UNSAT Verification via Normalized Chaining](https://arxiv.org/abs/2609.19353)

**<font color=#1a73e8>作者：</font>** Ashwin Karthikeyan, Ethan Kharitonov, Kuldeep S. Meel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Proofs of UNSAT are a standard primitive in formal verification and software assurance. In many real-world settings, the proof itself encodes proprietary or security-sensitive information, making public disclosure undesirable. Zero-knowledge certification of UNSAT addresses this tension: it enables a prover to convince a verifier that no satisfying assignment exists, without revealing anything about the underlying proof beyond its validity. Luo et al. recently introduced ZkUnsat, a protocol that achieves this goal by proving the validity of a weakened resolution proof in zero knowledge. ZkUnsat demonstrates the feasibility of zero-knowledge certification; however, its scalability to larger, real-world instances is constrained by substantial prover memory overhead, limiting its real-world applicability. Motivated by advances in UNSAT proof formats such as LRAT, which enable efficient plain-text verification, we present a preprocessing technique that improves the efficiency of ZkUnsat without introducing additional leakage. Our approach normalizes the proof so that each derived clause is justified by a resolution chain of fixed public length k. This eliminates chain-length leakage and reduces prover memory usage. With k = 16, our method certifies roughly 62% more instances than baseline ZkUnsat on the SAT 2002 competition benchmarks. Furthermore, for an equivalent number of certified instances, the memory footprint drops to under 25% of that required by the baseline.

---


### 16. [Open-vocabulary 3D object detection with promptable segmentation](https://arxiv.org/abs/2609.19358)

**<font color=#1a73e8>作者：</font>** Ömer Faruk Deniz, Mustafa Taha Koçyiğit  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Three-dimensional object detection for autonomous driving is dominated by detectors trained on large corpora of human-annotated 3D boxes. Such a detector learns a fixed category list, and everything outside it is invisible. This paper asks whether the task can be solved training-free and open-vocabulary. A promptable segmentation model (SAM3), queried with class names as text prompts, supplies instance masks in the vehicle's six surround-view cameras, and the masks are turned into metric 3D boxes using the geometry of the scene. The core is a controlled three-stage comparison on nuScenes in which 2D detection is held fixed and only the source of 3D geometry changes. Geometry predicted from images alone reaches 0.183 mean average precision (mAP) under the official protocol; fitting boxes from raw LiDAR points inside the same masks with training-free rules reaches 0.298 mAP / 0.348 nuScenes detection score (NDS) at zero labeling cost; borrowing supervised box geometry at inference time lifts the same detections to 0.413 mAP / 0.555 NDS, which locates the pipeline's largest deficit in measurement precision rather than 2D detection, while class confusion and confidence calibration survive that substitution. Reversing the direction, a three-state camera-witness rule built from the same masks improves a supervised LiDAR-only detector from 0.596 to 0.630 mAP, roughly half the gain of fully supervised camera fusion, with no training. A coverage analysis shows that SAM3 finds 84% of in-range objects with a correctly named mask; the classes that fail in the official metric are misnamed or geometrically unforgiving, not unseen.

---


### 17. [Smart Insole Human Activity Recognition for Continuous Monitoring in Elderly Care](https://arxiv.org/abs/2609.19359)

**<font color=#1a73e8>作者：</font>** Edwin Rios, Antony Garcia, Fengpei Yuan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Falls in older adults are often preceded by changes in mobility, balance, and postural transitions. This paper presents a wireless smart insole platform and machine-learning workflow for recognizing sitting, standing, walking, and unstable walking from plantar-pressure and inertial signals. Each insole integrates 16 active pressure-sensing locations and a six-dimensional IMU stream consisting of tri-axial acceleration and angular velocity. Data were collected from 15 healthy adults at 80~Hz and segmented into overlapping windows. Window length and candidate model families were first screened with stratified 10-fold cross-validation; the primary performance estimate was then obtained with participant-independent 5-fold Stratified Group cross-validation, ensuring that all windows from a participant remained in a single fold. Under this protocol, Histogram-Based Gradient Boosting (HGB) achieved macro-F1 scores of 0.954 and 0.959 for the left and right feet, respectively, and 0.980 with bilateral sensing. A compact 1D-CNN evaluated with the same participant-independent folds did not significantly outperform HGB ($p=0.0625$). The results show that low-profile footwear sensing can infer activity state from pressure and IMU measurements for participants unseen during training, establishing a basis for activity monitoring and fall prevention in elderly care.

---


### 18. [Stiefel Attention: When the Geometry of Transformer Projection Matrices Dominates Optimizer Choice---and When It Does Not](https://arxiv.org/abs/2609.19363)

**<font color=#1a73e8>作者：</font>** Rubén Darío Guerrero  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The query and key projections $\WQ,\WK$ in attention are almost always trained by Euclidean optimizers with no constraint on their geometry. We constrain them to the Stiefel manifold and optimize them there with a Riemannian Adam that carries one scalar second moment per frame, caps its step by a trust region, and retracts polarly. Four propositions prove this update is steepest descent in the embedded metric, independent of gradient scale, well conditioned, and exactly $\mathrm{O}(d)$-equivariant, each certified numerically in \texttt{float64}. A fifth supplies the mechanism: weight decay has \emph{identically zero} Riemannian gradient on $\St(d,r)$, since $W = W I_r$ lies in the normal space, so the learned attention geometry survives the collapse cycles that decay drives through the rest of the model. On modular arithmetic grokking, a single run holds $97.0\%$ validation accuracy at epoch 20\,000 against the baseline's $61.1\%$---an unstable endpoint we report as evidence for the mechanism rather than as an effect size. On CIFAR-10 patches the same rule gains $\mathbf{+8.98}$\,pp over 12 paired starts ($t{=}60.6$, $12/12$), and the gap widens with data rather than eroding. The step rule earns this: a fixed-step Riemannian update is degree one in the gradient, so it moves $24$--$40\times$ less per step than an identically shaped AdamW matrix---its frames barely leave their initialization, and freezing them outright costs only $0.28$\,pp. An ablation credits the whole gain to making the step scale free, and nothing measurable to the projector or to equivariance. A negative result sharpens the account: gauge removal cannot motivate the method, because a direction along which the loss is invariant carries no gradient at all.

---


### 19. [Durably Reducing Belief in Women's Health Misinformation Through Culturally Adaptive AI Videos](https://arxiv.org/abs/2609.19364)

**<font color=#1a73e8>作者：</font>** Anku Rani, Kokil Jaidka, Shruti Sharma 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Health misinformation disproportionately harms women, yet interventions rarely address the community norms that sustain false beliefs. We test whether culturally adaptive AI-generated video in which the presenter looks like someone from her community reduces misinformation belief among low-literacy women in suburban India. In a field experiment (N=434), participants watched an AI-generated video featuring either an adaptive or neutral presenter. The culturally adaptive presenter reduced misinformation belief by 30%, nearly twice the reduction produced by the neutral presenter compared to the non-intervention control condition. Post-experiment interviews suggest women recalled the neutral condition as a generic video but recognized the adaptive presenter. Gains persisted for three weeks. The adaptive advantage was largest for beliefs reinforced by community, such as blaming women for infertility, and negligible for medical knowledge gaps, such as understanding vaccines. These findings demonstrate the potential of culturally adaptive AI interventions to counter socially embedded health misinformation.

---


### 20. [Machine-Learning Assessment of the Predictive Value of Inflammatory Biomarkers for Cognitive Impairment in an Older Hispanic Adult Cohort](https://arxiv.org/abs/2609.19374)

**<font color=#1a73e8>作者：</font>** Antony Garcia, Gabrielle Britton, Alcibiades Villarreal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Small clinical tabular datasets require interpretable machine learning because deep learning is often impractical and ensemble models can be difficult to inspect. A key pitfall is that statistical significance does not necessarily imply predictive utility. Using data from the Panama Aging Research Initiative--Health Disparities (PARI-HD) cohort (n=165), we implemented a leakage-safe threshold-likelihood Bernoulli/Categorical Naive Bayes (BNB/CNB) classifier. Within every training fold, each continuous predictor was reduced to a supervised chi-square-derived state, while income entered the model through a categorical likelihood. All data-dependent steps were performed within repeated stratified 10-fold cross-validation with 30 repeats. The demographic baseline achieved a ROC-AUC of 0.630 +/- 0.017. I-309 (CCL1) was the dominant incremental feature, increasing AUC by 0.110, with paired DeLong tests yielding p<0.05 in 100% of repeats. In the pre-specified primary analysis, I-309 produced a fixed-partition DeLong p=0.0018, with robustness assessed across 200 random partitions, where the median p-value was 0.0011. Within the exploratory family of 18 candidate markers, I-309 achieved a Benjamini-Hochberg-adjusted q=0.032 on the frozen partition and satisfied q<0.05 in 85% of random partitions, whereas no other marker demonstrated reliable incremental predictive value. Because the fitted model is an inspectable table of thresholds and class-conditional probabilities, these results identify I-309/CCL1 as an interpretable candidate feature for tabular prediction of cognitive impairment, pending external validation.

---


### 21. [LinePilot Digitizer: Line-Plot Recovery with Manual and Automatic Calibration](https://arxiv.org/abs/2609.19377)

**<font color=#1a73e8>作者：</font>** Fengbo Ma, Rayan Akhtar, Aakash H. Joshi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering numerical series from line plots requires accurate axis calibration and reliable curve extraction. We present LinePilot Digitizer (LinePilot), which combines continuous color-based curve recovery with three calibration modes: LinePilot (standard), LinePilot (enhanced), and LinePilot (OCR). We also introduce DigitizerBench, the first dedicated benchmark for systematically evaluating digitizer performance, using an orthogonal design spanning signal, rendering, and plot-structure factors with complementary automatic and human-guided evaluations. We evaluate performance using failure-penalized capped normalized root-mean-square error (FPC-NRMSE), which assigns unit loss to missing, unusable, or catastrophically inaccurate outputs. On DigitizerBench-Full, LinePilot (OCR) achieves the lowest mean FPC-NRMSE (0.672) and highest trusted usability (38.2%) among the tested automatic pipelines. On DigitizerBench-Lite, LinePilot (enhanced) achieves the lowest mean FPC-NRMSE (0.081), 100% output success, and highest trusted usability (93.3%). The orthogonal benchmark design further enables factor analysis to identify the factors that most significantly affect digitizer performance. Together, the three calibration modes provide a practical trade-off between automation, user control, and accuracy within a shared curve-recovery workflow.

---


### 22. [FCx: An algorithm for finding Feasible Counterfactual Explanations](https://arxiv.org/abs/2609.19383)

**<font color=#1a73e8>作者：</font>** Kleopatra Markou, Vana Kalogeraki, Dimitrios Gunopulos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Counterfactual (CF) explanations identify changes that alter an input's classification. While existing methods produce realistic and low-cost CFs, they often fail to ensure feasibility, by suggesting non-constructive modifications or incompatible with future changes (e.g., changing an individual's race to secure a job offer). We introduce a refinement of CF explanations that explicitly enforces feasibility. Our approach is the first to efficiently generate CFs that are realistic, low-cost and feasible. We accommodate both hard feasible constraints, specified by domain knowledge users, and soft feasible constraints, inferred automatically via causal inference from the dataset. Our method, Feasible Counterfactual Explanations (FCx), is based on a modified Variational Autoencoder (VAE) optimized with a multi-factor loss function. We measure the cost of a change based on the absolute change in values (proximity) as well as the number of features changed (sparsity) while realism is measured based on the LOF for density estimation, guaranteeing that CFs reside in densely populated regions. Extensive experiments on four public datasets show that our approach matches state-of-the-art performance across multiple metrics while guaranteeing feasibility.

---


### 23. [Riemannian--Lorentz Fusion of Vision Transformers and State-Space Models](https://arxiv.org/abs/2609.19384)

**<font color=#1a73e8>作者：</font>** Badri N. Patro, Vijay S. Agneeswaran  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scaling deep learning faces critical bottlenecks: data exhaustion, exponential training costs, and resource concentration. Model merging combines pre-trained checkpoints without gradient descent, offering orders-of-magnitude savings versus retraining. Combining independently trained vision models is difficult when their architectures and parameter shapes differ. Existing weight-space merging methods generally assume aligned, shape-compatible checkpoints, whereas a Vision Transformer (ViT) and a state-space model (SSM) implement token mixing with different operators. We study a hybrid Heterogeneous merging setting that retains both architectures while aligning parameter groups by semantic role. Our proposed Riemannian--Lorentz Parameter Fusion (RLPF) method projects aligned groups to common coordinates, lifts selected coordinates to the Lorentz hyperboloid model of hyperbolic space, computes a regularized geodesic barycenter, and decodes the result into the two branches. A learned gate then combines branch logits for each input. Component groups use fixed curvature values, with normalization parameters treated as Euclidean. In the results available in this manuscript, the fine-tuned system obtains 82.37\% on CIFAR-10, 75.04\% on Oxford-IIIT Pet, and 78.58\% top-1 accuracy on ImageNet-1K; the corresponding best-parent accuracies are 76.54\%, 71.42\%, and 76.42\%. On ImageNet-1K, the reported pre-fine-tuning initialization reaches 77.80\%. These results support further study of geometry-aware heterogeneous fusion, but not a training-free single-checkpoint merge: RLPF is a two-branch hybrid whose gate and reported final models are trained.

---


### 24. [Do AI Agents Understand Computer Architecture?](https://arxiv.org/abs/2609.19387)

**<font color=#1a73e8>作者：</font>** Ambika Sharan, Grigory Chirkov, Soheil Abbasloo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agents are increasingly asked to design hardware, and increasingly reported to succeed. Such reports establish that a design improved; they cannot establish why. An agent that improves an accelerator may be reasoning about the machine, or may be searching competently over knobs whose meaning it never recovers -- and only the first transfers to the next architecture. Existing evaluations cannot tell the two apart, because they vary the agent while holding the framing of the problem fixed. We do the opposite. AutoTuring hands the same agent the same 15-dimensional accelerator space twice: once as named architectural knobs with simulator counters, once as anonymous variables on [0,1], with the evaluator, the legal space and the reachable optima held identical, so that the only thing that varies is whether the problem means anything. The gap between the two is the measurement. On a nine-kernel FP16 GEMM basket, meaning pays: the architect beats a modeled H200 by 5.4% and its blind counterpart by 12.3% on average, with 70.1% fewer simulator calls. It does not pay uniquely: a critic loop recovers most of that gap for the blind agent and buys the architect nothing, so architectural knowledge and structured critique behave as substitutes rather than as complements. We report these as preliminary findings -- five to six runs per condition on a single modeled accelerator -- and take the comparison itself, not the accelerator, to be the contribution.

---


### 25. [WZPlanner: Safe End-to-End Path Planning for Autonomous Driving in Work Zones](https://arxiv.org/abs/2609.19393)

**<font color=#1a73e8>作者：</font>** Nishad Sahu, Changzhong Qian, Guangzhou Cai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Work zones alter lane geometry through temporary traffic controls and closures that may be absent from on-board maps, challenging autonomous vehicle (AV) perception and planning. Generalization is also limited by scarce public datasets with structured geometric supervision. We present WorkZonePlan, a dataset comprising 149K+ synthetic and 5K+ real-world multimodal samples with 3D annotations for lane boundaries, work zone boundaries, and driving trajectory options. It also provides 76 closed-loop CARLA scenarios replayed under three weather conditions, yielding 228 Bench2Drive-format evaluation routes. We introduce WAVE (Work-zone-focused AV data generation in Virtual and rEal Environments), a semi-automated pipeline for creating the dataset, and BoundaryFormer (BF), a transformer-based model that jointly predicts lane and work zone boundary polynomials and driving trajectories. BF uses slot attention for boundary prediction. Ablations show that a separate trajectory decoder using boundary slot features substantially improves trajectory prediction over a slot-attention-only approach. Building on this finding, BF++ offers Camera and Camera+LiDAR variants with metric ground-plane encoding, typed boundary/trajectory queries, long-range point anchors, image-space curve refinement, and conservative gated LiDAR fusion. On the 211 routes common to all four models at the evaluation freeze, BF++-Camera and BF++-Camera+LiDAR achieve Driving Scores of 63.0 and 64.4, respectively, compared with 59.3 for SimLingo and 26.1 for TransFuser++ (TF++). BF++ is 40 times smaller than SimLingo and more than 10 times smaller than TF++, while achieving higher Driving Scores. These results support jointly predicting lane boundaries, work zone boundaries, and driving trajectories as a promising direction toward safer AV operation in work zones. Code and dataset: this https URL.

---


### 26. [Improving Offline Goal-Conditioned Reinforcement Learning via Selective Reward Stimulation](https://arxiv.org/abs/2609.19414)

**<font color=#1a73e8>作者：</font>** Jing Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Goal-conditioned reinforcement learning aims to learn policies that reach specified goals, but remains challenging in offline settings with sparse rewards and long-horizon dependencies. In such settings, goal-completion information can be temporally distant from the early decisions that enable success, while offline value estimation introduces additional error. We study this issue from a reward-propagation perspective and show, in a stylized delayed-goal setting, how goal-directed value separation can become small relative to local estimation error. Motivated by this analysis, we propose Reward Stimulation Implicit Q-Learning (RSIQL), a simple non-hierarchical method that introduces additional reward signals at progress-making intermediate states in offline trajectories. RSIQL uses an auxiliary goal-conditioned value function to identify intermediate states estimated to make progress toward the goal and applies reward stimulation to provide less-delayed training supervision. Unlike hierarchical methods, RSIQL does not learn a separate high-level subgoal policy. Experiments on D4RL goal-reaching benchmarks and OGBench show that RSIQL improves over goal-conditioned IQL on average and achieves performance competitive with hierarchical offline goal-conditioned methods, while retaining a simple flat policy structure.

---


### 27. [RGS: Reflection-aware Gaussian Splatting via Learning Geometry Continuity for Reflective Objects](https://arxiv.org/abs/2609.19421)

**<font color=#1a73e8>作者：</font>** Xiaobiao Du, Yida Wang, Cheng Bi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gaussian Splatting has significantly improved the quality of novel view synthesis with explicit Gaussian representation. However, we observed that existing 3D Gaussian Splatting methods (3DGS) often suffer from surface collapse issues on reflective regions, and thus produce inferior geometry and low-quality specular. In this work, we propose a physically-based deferred rendering framework, named Reflection-aware Gaussian Splatting (RGS), that can accurately model specular regions and improve novel view synthesis performance. Specifically, we found that a powerful 3D foundation model can provide a strong 3D geometric prior to foster correct geometric modeling. Based on this, we propose a cross-view shape consistency regularization to regularize the geometry surface with the large model prior and cross-view constraints. In this manner, our RGS can produce smoother geometric surfaces on reflective regions while reducing geometric hollows. To further improve rendering results on reflective regions, we present a reflection-aware densification strategy that is designed to capture specular variations across various views. With this strategy, our RGS is able to render novel views of objects in higher quality. Extensive experiments demonstrate our method consistently renders high-quality reflective objects, achieving state-of-the-art performance.

---


### 28. [Seeing Abnormal from Normal: Glomerular Abnormality in Representations of Normal Renal Morphology](https://arxiv.org/abs/2609.19444)

**<font color=#1a73e8>作者：</font>** Greta Hasko, Rachit Saluja, Tianyu Shi 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained evaluation of glomerular pathology must distinguish normal glomeruli from abnormalities such as global and segmental glomerulosclerosis, obsolescent, ischemic, solidified, disappearing, and atubular glomeruli. Supervised classification requires labeled examples of every category, which is impractical when subtypes are rare or absent from the training cohort. One-class anomaly detection offers an alternative by modeling normal data and scoring deviations, allowing previously unseen abnormalities to be detected. We use the frozen residual U-Net backbone of Omni-Seg, pretrained to segment structurally normal renal primitives without abnormal-subtype labels. We propose NoRDeC (Normal-Reference Detection and Characterization), a framework combining Mahalanobis normal-reference scoring with layer-wise representation analysis to determine whether and where glomerular pathology is encoded, how spatial aggregation affects detection, and whether abnormalities alter inter-layer relationships differently. Using glomerular images from two institutions, we evaluate backbone layers and aggregation strategies, compare NoRDeC with PaDiM and PatchCore, and analyze representations using centered kernel alignment (CKA). Layer 4 with Center-70 aggregation achieved a pooled AUROC of $0.926\pm0.013$. NoRDeC achieved the highest AUROC in six of seven abnormality categories and in the pooled analysis, while CKA suggested subtype-dependent changes in inter-layer relationships not captured by anomaly scores alone. The normal-reference model is fitted using only normal glomeruli; abnormality labels are used for configuration selection, evaluation, and grouping in the representation analysis. These results show that a frozen renal feature extractor can support both detection and representation-level characterization of glomerular abnormalities without using abnormal examples to fit the detector.

---


### 29. [The syntax and semantics of goals](https://arxiv.org/abs/2609.19448)

**<font color=#1a73e8>作者：</font>** David M. Abel, Mark K. Ho  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In both cognitive science and computer science, goals are conceptualized as cognitive states that flexibly combine with world knowledge to organize and specify purposeful behavior. In this way, goals are compositional representations whose content relates to rational behavior. We here draw attention to goals as representations and their content because it highlights a parallel with other areas in cognitive science - in particular, the syntax-semantics interface in linguistics and logic - while also foregrounding foundational questions about the expressivity, design, and efficiency of different goal representations. For example, goals are typically taken as fixed and imposing constraints on desirable behaviors, but we can also identify constraints on goal representations themselves, such as whether a particular goal language is sufficiently expressive to capture behaviors of interest, or whether different goal representations capture the same behavior. Here, we synthesize work that aims to characterize the properties of different goal representations and suggest these are points of a broader design space. We close by discussing how distinguishing the form and meaning of goals can elucidate the implicit assumptions we make about goals, inform the study of interactions between higher-level cognition and motivation, and isolate axes of variation for different conceptions of goals.

---


### 30. [Efficient Unified Multimodal Understanding (EUMU): Winning Solution for the MUMU Track at the 8th LSVOS Challenge](https://arxiv.org/abs/2609.19451)

**<font color=#1a73e8>作者：</font>** Dayoung Kil, Seong-heum Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The Mobile Unified Multimodal Understanding (MUMU) Challenge requires a single efficient model to jointly perform multi-concept image tagging, open-vocabulary object detection, and image captioning. We present Efficient Unified Multimodal Understanding (EUMU), the winning solution for the MUMU Track of the 8th LSVOS Challenge. EUMU builds on a shared pretrained multimodal model, using its prompt-based capabilities for detection and captioning and training lightweight heads on shared visual features to predict quality, scene, and event tags. Rather than treating the three tasks independently, EUMU applies task-aware inference refinement by reusing task outputs as cross-task cues. For detection, caption cues help recover objects missed by the initial detection. For captioning, detection cues help refine the caption to better reflect the detected objects. For tagging, image statistics refine quality predictions, while caption and detection cues refine scene and event predictions. This design unifies all three tasks within a single model while satisfying the challenge's resource constraints. EUMU contains 239.169M parameters, requires 23.947 GFLOPs, uses 4.5 GB of peak inference memory, and achieves a final challenge score of 17.3409. Code and models are available at this https URL.

---


### 31. [Sharpness-Aware Minimization (SAM) Improves Classification Accuracy of Bacterial Raman Spectral Data Enabling Portable Diagnostics](https://arxiv.org/abs/2609.19453)

**<font color=#1a73e8>作者：</font>** Kaitlin Zareno, Jarett Dewbury, Siamak K. Sorooshyari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Antimicrobial resistance is expected to claim 10 million lives per year by 2050, and resource-limited regions are most affected. Raman spectroscopy is a novel pathogen diagnostic approach promising rapid and portable antibiotic resistance testing within a few hours, compared to days when using gold standard methods. However, current algorithms for Raman spectra analysis 1) are unable to generalize well on limited datasets across diverse patient populations and 2) require increased complexity due to the necessity of non-trivial pre-processing steps, such as feature extraction, which are essential to mitigate the low-quality nature of Raman spectral data. In this work, we address these limitations using Sharpness-Aware Minimization (SAM) to enhance model generalization across a diverse array of hyperparameters in clinical bacterial isolate classification tasks. We demonstrate that SAM achieves accuracy improvements of up to 10.5% on a single split, and an increase in average accuracy of 2.7% across all splits in spectral classification tasks over the traditional optimizer, Adam. These results display the capability of SAM to advance the clinical application of AI-powered Raman spectroscopy tools.

---


### 32. [Beyond Private Training: The New Landscape of AI Privacy](https://arxiv.org/abs/2609.19456)

**<font color=#1a73e8>作者：</font>** Sean Culatana, Kang Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented systems increasingly rely on vector indexes that may retain deleted items in their search graph. Existing deletion interfaces can prevent deleted identifiers from appearing in returned results while still computing distances to their embeddings during graph traversal. We formalize this distinction as output safety versus traversal safety, and introduce TSD-AUDIT, a framework for auditing and enforcing traversal-safe deletion in graph-based approximate nearest-neighbor retrieval. On Faiss IndexHNSWFlat, native filtering leaves the number of distance computations unchanged relative to unfiltered search; at a 70% deletion rate, trace-faithful replay detects deleted-vector scoring in all 100 audited queries. Code inspection of hnswlib's mark_deleted path reveals the same scoring-before-liveness pattern. TSD-AUDIT enforces an alive-before-scoring invariant, repairs connectivity using only live candidates, and emits per-query scored-trace certificates that an independent verifier can check against the deletion snapshot. Under region-targeted deletion, TSD-AUDIT improves Recall@10 over native filtering by 4.3--42.2 percentage points across deletion fractions from 0.5 to 0.9, while remaining comparable under random deletion. These results show that output-only deletion audits can miss process-level exposure: auditing deletion in vector retrieval requires accounting for the vectors scored during search, not only the identifiers returned.

---


### 33. [ParticleSplat: Self-supervised Object-centric Latent Particle Splatting](https://arxiv.org/abs/2609.19463)

**<font color=#1a73e8>作者：</font>** Lyuxing He, Daniel Guo, Elizabeth Terveen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present ParticleSplat, a self-supervised object-centric learning method that decomposes scenes into a set of latent ''particles'' representing semantic entities through feedforward 3D Gaussian Splatting. Building on the Deep Latent Particles (DLP) framework, which represents images as a set of particles with attributes such as position, scale, and visual appearance, we address a key limitation of DLP: its inherently 2D nature, which prevents explicit 3D spatial and geometric reasoning that are critical for downstream tasks such as robotic manipulation. Leveraging the structural similarity between latent particles and 3D Gaussian primitives, we introduce a 3D latent particle space trained with a novel view synthesis objective. Our model jointly encodes multiple views with camera poses into a shared 3D object-centric latent space, then transforms particles into particle-aligned 3D Gaussians whose composition reconstructs the full scene. On simulated and real-world datasets, we show that this formulation inherently learns object masks without supervision and supports controllable 3D scene editing, such as moving objects by modifying particles in the latent space. We further establish that the learned 3D representation improves downstream performance on robotic manipulation tasks.

---


### 34. [Enhanced Agriculture-informed Neural Network by Domain Knowledge](https://arxiv.org/abs/2609.19466)

**<font color=#1a73e8>作者：</font>** Ci Lin, Futong Li, Rose Chong-Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate prediction of nitrous oxide (N2O) emissions from agriculture is important for assessing environmental impacts and supporting sustainable farming. However, prediction remains difficult because N2O emissions result from complex interactions among soil properties, climate, biochemical processes, and management practices, while high-quality observations are limited. Deep learning models can capture nonlinear relationships but often lack physical interpretability and may generalize poorly across environmental conditions. We propose the Knowledge-enhanced Agriculture-informed Neural Network (KAINN), a hybrid neural-mechanistic framework that extends the Agriculture-informed Neural Network by incorporating domain knowledge about fertilizer diffusion, soil respiration, and water-filled porosity. We evaluate KAINN using CNN, LSTM, and Transformer architectures across multiple growing seasons and input-feature configurations. The results show that KAINN generally provides lower root mean square error and mean absolute error and higher R-squared values than purely data-driven models and the original AINN. Analysis of the learned interfaces also shows smoother and more physically consistent parameter trajectories with reduced uncertainty. These findings demonstrate that incorporating environmental knowledge into neural networks can improve the reliability, interpretability, and generalization of agricultural N2O-emission predictions.

---


### 35. [Search at the Cost of Sampling: Nearly-Instant Latent Space Bayesian Optimization](https://arxiv.org/abs/2609.19476)

**<font color=#1a73e8>作者：</font>** Donney Fan, Colin Doumont, Aleksandra Kalisz 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models are increasingly central to many de novo discovery pipelines, in which designs are generated at scale and filtered through virtual screens to determine a set of candidates to experimentally validate. While Bayesian optimization (BO) is a natural fit for this setting, as it uses past evaluations to guide future proposals, the computational overhead required for its sequential decision-making becomes a bottleneck when virtual screens are relatively cheap. We make BO practical in this regime by exploiting the unique combination of a linear model constrained to a spherical domain where high-dimensional latents concentrate. We build off recent work justifying the use of linear surrogates, while deriving nearly closed-form solutions to the surrogate modelling and acquisition problems that exploit spherical symmetry. The result is at least a 100x speedup over state-of-the art baselines, with matching or improved performance across molecular and image generation benchmarks. Altogether, our method makes BO a practical drop-in for de novo pipelines where it was previously too slow to consider.

---


### 36. [Reputation as Community Memory for the Agentic Web](https://arxiv.org/abs/2609.19502)

**<font color=#1a73e8>作者：</font>** Ryan Chard, Gus Ellerm, Alexander Brace 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Agents can now externalize experience into memory, consolidating historical traces into semantic knowledge and procedural shortcuts that persist between sessions. Such memory is typically private to a single agent. We argue that agentic memory benefits from being collective, because trustworthy knowledge of the shared environment---the data sources, services, and tools agents depend on---cannot be established by any single agent, only corroborated across many independent observers. We present Cairn, a community reputation platform that captures collective knowledge, allowing agents to query the community's opinion of a resource before use and to submit evidence-backed ratings afterward. Cairn aggregates observations via a time-decayed Beta model with confidence shrinkage and supports semantic discovery over reviewer rationales. We evaluate Cairn's reputation engine under adversarial simulation (e.g., lying, collusion, camouflage), benchmark its retrieval performance, and report a case study of rating heterogeneous agents in production.

---


### 37. [FenceXR: AR Movement Replay for Error-Detection Training and Spatially Grounded Feedback](https://arxiv.org/abs/2609.19505)

**<font color=#1a73e8>作者：</font>** Avinash Ajit Nargund, Amelia Haruka Harrison, Timothy Robinson 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recognizing technical errors in movement is a perceptual skill important to motor learning, but it is challenging for beginners in fast, complex sports like fencing to develop it. A coach's attention is scarce, live demonstrations vary from repetition to repetition, and video review is limited to whatever camera angle was used to record it. Coaches and advanced fencers reviewing a recording face a related problem. They can see an error, but have no way to anchor their feedback to the movement itself, and are left describing it in words the learner must map back onto their own body. We present FenceXR, an augmented reality system that reconstructs 3D movement replays from monocular smartphone video to address both problems. A Trainee module trains novices to detect common lunge errors while a Reviewer module lets coaches and advanced fencers attach text or voice annotations to a specific joint and moment in a replay, which can be shared asynchronously with a trainee. In a study with 18 novice fencers, unaided error-detection accuracy rose from near-chance (37.5%) before training to 64.1% after a single session, with interviews showing a shift from broad visual scanning toward targeted inspection of specific joints and their timing. In a video-based study with four fencing experts, all four viewed the Reviewer module as a valuable complement to their existing coaching tools, particularly for feedback that is difficult to convey through standard video. We end with a discussion of implications for designing AR systems that ground movement-based training and feedback in the movement itself.

---


### 38. [AMB3R-SLAM: Kilometer-scale SLAM with Hierarchical Backend](https://arxiv.org/abs/2609.19518)

**<font color=#1a73e8>作者：</font>** Hengyi Wang, Lourdes Agapito  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present AMB3R-SLAM, a real-time monocular SLAM system capable of reconstructing kilometer-scale trajectories over 10k frames on a single consumer-grade GPU. Our model couples a lightweight front-end for low-latency online tracking with a hierarchical backend that progressively enforces local, mid-level, and global consistency. By avoiding bundle adjustment that relies on the static world assumption, our system naturally handles complex dynamic scenes out of the box. Furthermore, we demonstrate that our method can be extended to leverage stereo, RGB-D, and LiDAR as additional inputs. AMB3R-SLAM achieves strong camera tracking performance across 9 datasets, reducing the absolute trajectory error (ATE) of previous state-of-the-art methods on VBR and Oxford Spires by over 70%. With additional LiDAR input, our model further reduces ATE to sub-meter level on KITTI and VBR datasets.

---


### 39. [LSTM-UT and Recurrent-Depth Transformers on Cellular Automata](https://arxiv.org/abs/2609.19521)

**<font color=#1a73e8>作者：</font>** Aras Kavuncu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recurrent-depth Transformers apply shared computation repeatedly, but differ in how they retain information across steps. We compare a Block Universal Transformer (BUT), which carries only its current hidden state; CoTFormer, which also retains an expanding attention cache; and a new LSTM Universal Transformer (LSTM-UT) with bounded gated memory. On Rule 30 cellular automata, BUT extrapolates to unseen recurrent depths more reliably than CoTFormer, although its accuracy eventually degrades. State and cache interventions show that CoTFormer's failure depends on their interaction: correcting the current state can temporarily restore accuracy, while retained history can undermine that correction. In a delayed-recall task, BUT also outperforms CoTFormer despite lacking direct access to past states; CoTFormer does not reliably select the requested cached representation. LSTM-UT improves both depth extrapolation and delayed recall over these baselines. The results support bounded gated memory as an effective inductive bias for repeated computation and later retrieval in these tasks.

---


### 40. [EconSkills: Studying Skill Transfer and Retrieval for Web Agents on Live Economic Data](https://arxiv.org/abs/2609.19523)

**<font color=#1a73e8>作者：</font>** Yinzhu Quan, Zefang Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Web agents often revisit the same sites, yet most evaluations discard the procedures learned in earlier successful interactions. We introduce EconSkills, a skill library and evaluation framework that distills verified EconWebArena trajectories into parameterized standard operating procedures for retrieving live economic data. Each skill records its scope, navigation procedure, site-specific guidance, verification checks, and recovery steps while replacing source-instance values with placeholders. EconSkills separates two questions: whether a known relevant procedure transfers to a held-out task, and whether an agent can retain that benefit when selecting from a library. In controlled transfer, matched skills improve success over no-skill prompting and require fewer steps on paired successes, while abstraction is substantially more effective than replaying raw trajectories. At library scale, retrieval is competitive with the no-skill baseline overall and performs best on directly covered tasks; coverage-stratified outcomes show that approximate matches on uncovered tasks offset these gains. Browser trajectories further identify when procedural guidance shortens portal-specific navigation and when semantic verification remains necessary. These results establish that reusable economic web procedures can transfer across task instances and provide a concrete design target for coverage-aware selection and context delivery.

---


### 41. [Compressed Active Subspaces for Scalable Bayesian Inference](https://arxiv.org/abs/2609.19539)

**<font color=#1a73e8>作者：</font>** Thomas Flynn, Sanket Jantre, Byung-Jun Yoon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Active subspace methods provide a framework for quantifying predictive uncertainty in high-dimensional models by identifying and performing inference along parameter directions that have the greatest influence on the model output. However, the construction of active subspaces requires storing many full-dimensional model gradients, which becomes prohibitive as model size increases. We address this limitation by proposing Compressed Active Subspaces (CAS), a scalable approach that first maps the model parameters to a compressed space using a structured isometric embedding and then constructs the active subspace within this reduced parameterization. Our approach substantially reduces the memory required for active subspace construction and enables Bayesian inference for large models where standard active subspace methods become impractical. We demonstrate the scalability of CAS on neural networks of increasing size while maintaining predictive performance and robust uncertainty estimates.

---


### 42. [PerSeM: Persistent Semantic Memory for Long-Horizon Open-Vocabulary UAV Mapping](https://arxiv.org/abs/2609.19542)

**<font color=#1a73e8>作者：</font>** Saurbh Singh Jamwal, Ganesh Ramakrishnan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary segmentation enables rich semantic perception for UAVs, but frame-wise predictions can remain temporally inconsistent across repeated observations and changing viewpoints. We present PerSeM, a training-free persistent semantic memory framework for long-horizon open-vocabulary UAV mapping. PerSeM associates frame-wise semantic observations with persistent world-space voxels and constructs a majority-based semantic memory, which is conservatively refined through history-preserving spatial refinement, trust-aware replay, and context-guided verification. Experiments on the Forest and UAVScenes benchmarks show that persistent 3D memory provides substantial gains in semantic correctness and temporal stability over frame-wise predictions. Beyond this strong persistent-memory baseline, PerSeM provides consistent additional improvements, improving both semantic accuracy and temporal stability across all five evaluated UAVScenes sequences. Analysis using regions identified independently of the final PerSeM predictions further shows that these gains are concentrated in semantically difficult and temporally unstable regions, where majority-based memory is most likely to remain uncertain. These results demonstrate that persistent 3D aggregation provides a strong foundation for long-horizon semantic mapping, while conservative refinement of uncertain memory states can provide additional improvements without retraining or additional neural-network inference.

---


### 43. [Continual Enterprise World Model Discovery in Dynamic Systems](https://arxiv.org/abs/2609.19551)

**<font color=#1a73e8>作者：</font>** Shambhavi Mishra, David Vazquez, Perouz Taslakian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In an enterprise system, updating one field can set another, create a record, or start an approval. These effects are produced by business rules that are not built into the platform but written by each organization and revised over time. An agent working in such a system cannot predict the result of its own actions without knowing these rules. We study continual enterprise world model discovery, where an agent starts without knowledge of these business rules and discovers them by interacting with records and observing the outcomes. From those observations it builds a world model, which it revises as the rules change. To evaluate this, we introduce EnterpriseWorldShift, built on a live ServiceNow environment with nine tables, 25 hidden rules and 600 evaluation actions. It presents four versions of the same enterprise world, with the tables and records held fixed while a rule is modified, then added, then removed, so that discovery, revision, extension and retirement are each tested in turn. Our Continual Discovery Agent (CDA) builds such a model and carries it from one world to the next. It predicts the effects of the hidden rules more accurately than looking them up for each question, the approach taken by prior work, by up to 8.98 IoU points, and it answers from its own model without querying the running system.

---


### 44. [A Multi-Modal Generative Model for Tomato Disease Leaves Understanding](https://arxiv.org/abs/2609.19555)

**<font color=#1a73e8>作者：</font>** Khang Nguyen Quoc, Minh-Phuoc Tran, Gia-Han Truong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence for plant disease analysis has advanced from task-specific classifiers to multi-modal models capable of jointly interpreting visual and textual information. However, practical deployment in precision agriculture remains limited because most existing approaches treat disease understanding as isolated prediction tasks, failing to capture the complementary relationships among symptom recognition, severity assessment, and question-driven diagnostic reasoning. In tomato pathology, accurate interpretation of diseased leaves requires more than label prediction; it demands integrating visual symptoms with semantic context to support a comprehensive and explainable understanding. Here, we present SOLAR, a multimodal generative model that understands tomato disease spanning six question-answering tasks. SOLAR learns to align visual features with task-aware language representations by Fusion Expert module based on mixture-of-expert, enabling it to generate contextually relevant answers across diverse diagnostic tasks. By formulating tomato disease analysis as a generative Visual Question Answering (VQA) task, SOLAR provides a flexible framework that supports multi-task inference within a single model while improving performance and cross-task knowledge sharing. We evaluate SOLAR on $41,677$ images, including $216,209$ Question-Answering (QA) pairs to understand tomato leaf disease under both closed and open-ended QA settings. Experimental results show that SOLAR consistently outperforms state-of-the-art vision-only, vision-language, and task-specific models across all tasks, demonstrating superior accuracy, robustness, and multimodal reasoning. These findings highlight the potential of generative multimodal modeling as an effective direction for understanding of plant disease. The code for this study is available at this https URL.

---


### 45. [Cyber Exodus: Burnout Symptoms, Exit Intention, and Peer Response in Online Cybersecurity Communities](https://arxiv.org/abs/2609.19556)

**<font color=#1a73e8>作者：</font>** Nadia Mehjabin, Ji Hyun Kim, Laura Barnes 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Security practitioners burn out at high rates, and the resulting attrition is itself a security problem. This workforce is hard to study: security operations centers are closed to outside researchers, studies that reach practitioners recruit through employers, and those who have disengaged most may have the least reason to answer an employer's survey. The same practitioners discuss their working conditions openly in online communities. We adapt the Burnout Assessment Tool, a validated clinical instrument, into a text annotation scheme and apply it to 354,861 posts and 296,442 replies from five online communities of cybersecurity practitioners. Checked against two trained coders on 100 posts, the annotation reaches a macro F1 of 0.75 across the four symptoms and 0.98 for detecting any burnout signal. We find that the four symptoms point to different problems at work, not to the same problem at different levels of severity. Exhaustion appears in almost any complaint about staffing or workload. Mental distance, a loss of belief that the work is worthwhile, is the only symptom unrelated to operational problems, and among posts with a single symptom it is accompanied by a stated intention to leave roughly twice as often as any other. Peer responses show the opposite pattern. When a poster says they are considering leaving, the mix of replies shifts toward career advice, but this shift is smallest for mental distance. The symptom most strongly associated with leaving is thus the one peers adjust to least, and a single burnout score obscures both patterns.

---


### 46. [FedFIbOS: Fisher Importance based Optimal Submodelling for Heterogeneous Federated Learning](https://arxiv.org/abs/2609.19559)

**<font color=#1a73e8>作者：</font>** Yasmeen Afzal, Jeremiah D. Deng, Haibo Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Heterogeneous federated learning requires clients with diverse computational capacities to collaboratively train a global model, where each client trains a capacity-constrained submodel. Existing methods select submodel parameters using heuristic importance measures---most prominently parameter magnitude---without theoretical justification for why these measures support convergence. We identify a fundamental gap: existing parameter selection criteria lack theoretical grounding in the convergence framework, partial client participation introduces additional estimation effects in the Fisher scores. We propose \textbf{FedFIbOS}: Fisher Importance-based Optimal Submodelling for heterogeneous federated learning, using Fisher Information in a principled criterion derived from minimizing submodel masking error. %We formally establish when magnitude selection is equivalent to Fisher selection fail under non-IID heterogeneous federated learning. We theoretically formulate submodel selection through a Fisher-weighted quadratic masking surrogate and show that the raw Fisher top-$k$ rule implemented by FedFIbOS solves this surrogate under a Fisher-dominant ranking condition. The resulting method retains the convergence structure of the underlying masked federated optimization bound. Fisher scores are efficiently estimated from empirical diagonal Fisher information using squared gradients, enabling stable and adaptive parameter selection without additional optimization overhead. Experiments on CIFAR-10, CIFAR-100, and AGNews under pathological and Dirichlet non-IID settings show FedFIbOS achieves ${\approx}10\%$ higher accuracy than the state of the art, with improvements becoming more pronounced under stronger heterogeneity.

---


### 47. [Value Faces: Surfacing How Self-Presentation Shifts Across Relationships](https://arxiv.org/abs/2609.19581)

**<font color=#1a73e8>作者：</font>** Gabriel Koo, Rayhan Rashed, Farnaz Jahanbakhsh  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> People present different aspects of themselves across relationships. Computational work has captured such variation in communication style. But this variation also extends to which principles people foreground or background in a particular relationship--i.e., in the values they express and how they balance them. We conceptualize these relationship-specific expressions of values as demonstrated values. To make demonstrated values visible, we introduce Value Faces, a system that analyzes a person's existing chat histories from their everyday messaging platforms using Schwartz's ten basic human values and produces separate value profiles for their different relationships. In a mixed-methods study(N=18), we find that the resulting value profiles distinguished participants' relational contexts with twice the odds of guessing, while system-inferred differences across relationships aligned with participants' perceptions of those differences. Participants used these profiles to articulate previously implicit differences in how they presented themselves, connect them to roles and changes over time, and reconsider their self-assessments.

---


### 48. [Selective Cotton Boll Localization for Robotic Harvesting: Evaluation of Deep Learning Vision Models Under Field Conditions](https://arxiv.org/abs/2609.19592)

**<font color=#1a73e8>作者：</font>** Thevathayarajh Thayananthan, Xin Zhang, Isuru Laddusinghe Badu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This study developed and evaluated a deep-learning-based perception framework for selective robotic cotton picking. The dataset contained 1,008 annotated field images collected using three cameras under varying natural lighting and weather conditions. Object-detection models from the YOLOv8 through YOLOv13 families were evaluated using their default configurations, while segmentation performance was assessed using YOLOv8-seg, YOLOv11-seg, YOLOv12-seg, the Segment Anything Model (SAM), SAMv2.1, FastSAM, and Grounded-SAM with the Recognize Anything Model (RAM). Among the detection models, GELAN-s achieved the most favorable balance between mean average precision (mAP) and inference speed, obtaining an mAP of 86.1%, precision of 81.6%, recall of 76.6%, and an F1-score of 79.0%, with an average inference time of 42.3 ms per image. Among the direct segmentation models, YOLOv12-m-seg provided the most favorable balance between AP@0.5 and FPS, achieving a segmentation AP@0.5 of 83.7% with an inference time of 20.4 ms per image. In the detection-prompted segmentation approach, bounding-box prompts generated by GELAN-s improved the localization of cotton bolls for SAM and SAMv2.1, while SAMv2.1 Tiny consistently outperformed FastSAM and Grounded-SAM with RAM. In the area-based evaluation against manually annotated segmentation masks, YOLOv12-m-seg achieved an $R^2$ value of 0.966, compared with 0.860 for GELAN-s + SAMv2.1 Tiny. Field experiments conducted using a UR5e robotic manipulator, a custom end-effector, and a ZED2i stereo camera further validated the effectiveness of the YOLOv12-m-seg model for real-time cotton boll detection, segmentation, and selective picking under varying confidence levels. These results demonstrate that YOLOv12-m-seg provides an efficient perception model for robotic cotton harvesting and has strong potential for field deployment.

---


### 49. [Full-Duplex Speech Models Take the Floor When Asked, Not When Needed](https://arxiv.org/abs/2609.19596)

**<font color=#1a73e8>作者：</font>** Linkai Peng, Baorian Nuchged, Kaiqi Fu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Full-duplex speech models listen and speak at once, promising always-on assistants. Yet they must also decide when they should speak. Human listeners speak when addressed or when the speaker stops, but also self-select to correct a false claim, supply a missing word, or warn of danger. We ask whether full-duplex models do the same. To separate the reason to speak from the opportunity, we construct context-matched English monologues in which only the trigger utterance varies within a topic, define 10 conditions from turn-allocation rules, and compress inter-word pauses to limit opportunities created by silence. Across five model families, being addressed and silence are far more reliable triggers than false facts or hazards. Frame-level text-token probabilities in Moshi and PersonaPlex are lower for false facts than for Neutral when averaged over the first 2\,s after trigger end. Pauses or permission to interrupt do not close this gap either. Given the floor, Moshi and PersonaPlex answer most direct questions, yet the proportion of non-empty false-fact replies that challenge the claim is only .14--.15, and the proportion of hazard replies that warn of danger is .04--.07. This paper thus identifies a gap in both speech initiation and response content. Closing it requires genuine content understanding and intervention decisions grounded in it.

---


### 50. [SIMLIFE: Pattern Understanding for Long-Horizon Human-Agent Partnership](https://arxiv.org/abs/2609.19610)

**<font color=#1a73e8>作者：</font>** Run Peng, Zinnia Nie, Jing Ding 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding humans over long horizons requires agents to infer not only what people need in the moment, but also how routines form, why they repeat, and when they change. We introduce SimLife, a scalable platform for simulating long-term household life with rich visual observations, ground-truth action logs, and synthetic dialogues with audio. Built on SimLife, SimLife-BP evaluates long-context pattern understanding: the ability to infer latent behavioral rules from weeks or months of everyday observations. The benchmark contains 106 episodes averaging 15.49 hours and 38.57 in-game days, and 1,439 question-answer pairs. Each task probes direct, counterfactual, noisy, and inverse reasoning under different levels of rule hints. Evaluating frontier models and architectures, we find that current models often achieve surface-level prediction without comprehensive rule understanding, rely on frequency-based heuristics rather than if-then reasoning over evidence, and struggle to adapt when behavioral patterns change. These findings suggest that long-context pattern understanding remains a major bottleneck for future embodied agents, while SimLife opens a broader space for studying memory, personalization, adaptation, and long-horizon planning in everyday human-AI interaction.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-247](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
