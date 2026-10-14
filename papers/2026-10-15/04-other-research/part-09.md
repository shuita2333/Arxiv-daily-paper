# 📦 其他研究 | 2026年10月15日

> 本类共 **810** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**401-450**（第 9/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

---

### 401. [BAT3R: Robust Online 3D Reconstruction with Bayesian Adaptive State Updates](https://arxiv.org/abs/2610.16330)

**<font color=#1a73e8>作者：</font>** Lijian Li, Yuanpeng He, Yudian Zheng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward transformer models have driven remarkable progress in 3D vision,yet their quadratic complexity renders them impractical for long video sequences. Streaming 3D reconstruction addresses this bottleneck by processing frames sequen?tially with constant memory. However, existing recurrent architectures inevitably suffer from progressive degradation over long sequences, as they fail to account for the intrinsic reliability of observations and the accumulated confidence of the historical state, leading to severe error accumulation. To address these issues, we introduce BAT3R, a training-free Bayesian adaptation framework comprising two synergistic modules: State Innovation Gating (SIG) and Bayesian-guided Adaptive State Updating (BASU). SIG acts as a distributional regularizer that anchors state evolution to its geometric initialization, effectively arresting representational drift during long-term inference. Building on this, BASU reformulates state update as a recursive Bayesian inference process within a Kalman filtering framework. By jointly modeling the temporal reliability of observations via information-theoretic gain and spatial relevance via cross-attention maps, BASU achieves an asymmetric spatio-temporal state fusion: well-consolidated historical regions are protected from redundant updates, while genuinely novel scene content is aggressively incor?porated. Extensive experiments on standard benchmarks (7-Scenes, TUM, ScanNet, KITTI, etc.) demonstrate that BAT3R consistently outperforms state-of-the-art online 3D reconstruction methods, with the most significant gains observed on long sequences and complex scenes.

---


### 402. [Doctor Trigger: A Framework for Release-Bound Face Verification](https://arxiv.org/abs/2610.16336)

**<font color=#1a73e8>作者：</font>** Chia-Ming Lee, Chia-Yu Lin, Hung-Kai Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Face swapping and generative editing enable realistic facial manipulation, while online redistribution complicates publisher oversight of circulating face images. Existing approaches establish provenance, detect manipulation, recover embedded watermarks, verify image integrity, or disrupt unauthorized face manipulation. These capabilities do not necessarily establish consistency with a specific publisher-enrolled release, limiting the evidence available for verification and human review. To address this gap, we introduce Doctor Trigger, a framework for verifying circulating faces against private publisher-held release records. Before publication, the publisher embeds a weak keyed Fourier-phase signal in each face while preserving visual fidelity and stores its spectral reference. Afterward, verification compares the circulating face with that reference and uses key projection to measure retention of the release-specific signal. Therefore, relation and key evidence jointly help publishers identify suspicious copies for review, potentially reducing the circulation of manipulated images. Experimental results across FF++, DFDC, and Celeb-DF show that spectral agreement separates tested face swaps and generative manipulations from enrolled releases, while the keyed signal distinguishes published versions from their unreleased originals under the evaluated key-preserving benign transformations. Doctor Trigger complements provenance metadata with release-specific face verification and record-linked evidence for further assessment.

---


### 403. [WorldRoPE: Probabilistic World-Centric Rotary Embedding for Multi-View Attention](https://arxiv.org/abs/2610.16337)

**<font color=#1a73e8>作者：</font>** Mijeong Kim, Kyujin Lim, Bohyung Han  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rotary Positional Embedding (RoPE) is widely used to encode relative positions in Transformers. In multi-view settings, however, patch coordinates are defined independently in each image: the same 3D point can therefore have different coordinates across views, making them insufficient for establishing cross-view correspondences. We introduce WorldRoPE, a probabilistic world-centric RoPE for multi-view attention. At each layer, WorldRoPE back-projects each patch token into a set of volumetric Gaussian primitives in a shared world frame. These primitives represent multiple plausible 3D supports for a token, jointly capturing alternative depth hypotheses, depth uncertainty, and the finite spatial extent of its patch frustum. When a key token's support is projected into a query view, it induces a distribution over where that key may appear in the query image. WorldRoPE integrates the rotary operator over this distribution in closed form, combining rotations at the projected primitive centers according to their mixture weights with covariance-dependent attenuation. This makes attention less sensitive to uncertain key locations in the query view, without rasterizing or warping token features. The formulation reduces to deterministic RoPE when the support collapses to a point. Across layers, the predicted geometry guides cross-view attention, while the updated features refine the geometry used at the next layer. Experiments on novel view synthesis, depth estimation, and 3D geometry reconstruction demonstrate the effectiveness of WorldRoPE for multi-view Transformers.

---


### 404. [SyncReward: Human-Aligned Synchronization Reward for Audio-Visual Generation](https://arxiv.org/abs/2610.16338)

**<font color=#1a73e8>作者：</font>** Kaisi Guan, Ying Ba, Wenjing Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent years have witnessed rapid progress in joint audio--visual generation. However, audio--visual synchronization remains a challenge, as generated speech and sound often temporally misalign with visual events. A key bottleneck is the lack of human-annotated data, reliable evaluation benchmarks, and synchronization-aware evaluation models for generated audio--visual outputs. To address these limitations, we conduct a comprehensive study spanning data, benchmarking, and reward modeling. We first introduce SyncReward-Data-80K, a dataset containing 80K professional synchronization ratings for clips from eight audio--visual generators. A taxonomy-guided construction pipeline covers four sound-event families: Speech, Onset, Instrument, and Ambient. We further construct \textbf{SyncReward-Bench}, a held-out benchmark of 1K clips, each independently rated by multiple professionals. Using this benchmark, we systematically evaluate specialized synchronization metrics and omni-modal models, revealing their substantial misalignment with human judgments. Finally, we develop SyncReward, a reward model that combines semantic--temporal contrastive pretraining on real clips with human supervision on generated clips. As an evaluation metric, SyncReward achieves the strongest agreement with human ratings among the evaluated methods. As a reward, it improves synchronization through inference-time best-of-$N$ selection and reinforcement learning based post-training. We will release the data, benchmark, model, and code at this https URL.

---


### 405. [Rescuing Points Trapped Inside Incorrect Decision Regions: A target for Evaluating and Improving Forward-Forward Learning](https://arxiv.org/abs/2610.16347)

**<font color=#1a73e8>作者：</font>** Alireza Rahmansetayesh, Amirhossein Yousefiramandi, Maxwell Spiridonov 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Forward-Forward learning replaces end-to-end backpropagation with local, layer-wise training objectives. Its variants are evaluated primarily by classification accuracy, often measured with linear probes trained on their representations. We show that this evaluation can over-credit the learning method: a linear probe on the representations of an untrained convolutional neural network already reaches accuracy well above chance. Moreover, a single accuracy value does not reveal which datapoints become correctly classified after training and which remain misclassified. To examine what learning contributes beyond the random, untrained baseline, we present an analysis methodology built on the Boundary Proximity Index (BPI), a multiclass margin normalized by a class-centroid reference. We apply our analysis to seven Forward-Forward variants and related layer-local methods and find that initially misclassified points near the probe's decision boundary generally have higher rescue rates than those farther inside incorrect decision regions. Rescue rates vary substantially across methods, with some correcting a substantial fraction of these deeply embedded points. Together, these analyses offer a way to evaluate representation learning beyond accuracy and identify the rescue of points far inside incorrect decision regions as a target for improving local learning methods.

---


### 406. [DWI Connectome-based Sex Classification in Young using Supervised Variational Autoencoder](https://arxiv.org/abs/2610.16348)

**<font color=#1a73e8>作者：</font>** Aditya Kothapalli, Aaryan Gera, Sathvik Reddy V 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> During adolescence, significant changes in brain development are influenced by hormonal changes that impact both the body and the brain. This study presents sex classification in 787 young adults having age range of 15-25 years using Diffusion-weighted (DWI) structural connectome, focusing on 82 Desikan-Killiany atlas ROIs. A supervised variational autoencoder (SVAE) is used to extract latent space features from DWI connectome data. Although several studies explored differences in brain structure and function between sexes, the main contribution of this study lies in incorporating SVAE to learn a compact, regularized latent representation for the task of sex classification. Initial exploratory data analysis shows that these features can capture the differences in sex-specific latent space patterns. Subsequently, the learned latent space SVAE features are fed to different ML models for sex classification. Among the considered ML classifiers, the multi-layer perceptron yields the highest accuracy of 80% in classifying sex. This demonstrates the effectiveness of SVAE in learning compact, informative representations from DWI connectome for sex classification. The present work highlights the potential of using DWI brain connectomics and deep learning to differentiate sex, paving the way for future research on diverse populations that may include transgender individuals, to better understand sex-related variations in brain structure.

---


### 407. [VideoSlate: Stateful Commit Control for Temporally Grounded Agentic Video Reasoning](https://arxiv.org/abs/2610.16357)

**<font color=#1a73e8>作者：</font>** Shuo Zheng, Yuanjie Dang, Peng Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Agentic video reasoning systems gather and assess video evidence across stages, selecting relevant spans as visual evidence for answering questions. New candidates and observations prompt reassessment of the current span, but revisions can correct localization errors or discard useful evidence already present in the adopted span. Systems therefore need to connect evidence organization across stages with temporal state control, allowing accumulated information to jointly inform revision assessment while explicit adoption decisions govern how assessment outcomes affect downstream visual evidence. We introduce VideoSlate, a stateful commit-control framework built around shared evidence. A typed evidence blackboard links candidate spans, provenance, construction, and verifier observations, enabling an incumbent-relative certifier to assess revision support from the candidate, current span, and related proposals. Based on certification, the controller authorizes a revision or retains the current span, separating evidence accumulation from state updates and recording each decision and its evidence on the blackboard. Extensive evaluations across video grounding and grounded question-answering benchmarks show that VideoSlate can improve temporal localization through selective revision.

---


### 408. [World Models Need a Physical Registry: Learning Internal Predictive States for Physically Plausible World Models](https://arxiv.org/abs/2610.16365)

**<font color=#1a73e8>作者：</font>** Shinseong Kim, Jaeseok Jeong, Jianlong Fu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Video world models must generate physically plausible futures, not just realistic frames. Existing approaches typically use semantic, physical, or predictive information to guide the visual generation stream, leaving a fundamental question: where inside the generator should predictions of scene evolution live? Standard video tokens jointly encode appearance and dynamics, but provide no distinct state for learning and reading predictive dynamics. We answer this question with the Physical Registry: temporally grounded registry slots inside a video DiT that are initialized from an observation-conditioned forecast, co-evolve with video tokens, and receive future-representation supervision, making predictive dynamics an explicit, readable state of the generator. In a controlled comparison of predictive-state interfaces on Physics-IQ Verified, Physical Registry improves vanilla fine-tuning by 9.9/8.7 points on I2V/V2V, the largest gain among the interfaces we compare. Across all Cosmos and WAN backbones, Physical Registry improves Physics-IQ Verified scores. With only 0.45% additional parameters, it enables Cosmos 3 Nano 16B to surpass the published I2V score of Cosmos 3 Super 64B (43.56 vs. 42.7). On WorldModelBench, it also improves physical adherence and the total score for all four evaluated backbones. Because the registry becomes candidate-specific while remaining readable, the Physical Registry Selector (PRS) ranks emerging futures by how far their intermediate registry readouts depart from the shared forecast before full denoising is complete. Across four backbones, this selection improves I2V scores by 5.6-15.9% without completed-video external scoring. Together, these results support a broader principle: dynamics prediction should live as an explicit model state that co-evolves with the video representation. Project page: this https URL

---


### 409. [Resource-constrained Remote Attestation of Smart Meters Using Merkle Trees in a Trusted Execution Environment](https://arxiv.org/abs/2610.16373)

**<font color=#1a73e8>作者：</font>** Amirhossein Shakiba, Hamid Reza Ghaeini, Sadegh Dorri Nogoorani  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Smart meters are pivotal to the functioning of smart grids, as they measure and transmit energy consumption data that includes sensitive information about household energy usage patterns. While this data offers significant financial benefits, it can also reveal detailed insights into residents' daily routines, making the security of smart meters a critical concern. This paper introduces a novel remote attestation method for smart meters that ensures the integrity and privacy of data exchanged between smart meters and central servers while detecting unauthorized tampering. Our approach structures the communication data into a Merkle Tree-a hash data structure that facilitates efficient data integrity and authenticity verification. All operations involved in constructing the Merkle root and hashing critical data are executed in the secure environment of a Trusted Execution Environment (TEE) using OP-TEE, thereby maintaining the integrity and security of the smart meter's data. Comparing our experimental results with the related works highlights the superiority of our method in terms of resource efficiency, security robustness, and the feasibility of implementation on smart meters and resource-constrained devices, thereby enhancing the overall security and reliability of smart grid systems.

---


### 410. [Throwing4: Phase-Aware Pose Modeling for Throw-Distance Prediction in Elite Athletics](https://arxiv.org/abs/2610.16383)

**<font color=#1a73e8>作者：</font>** Bikash Kumar Badatya, Kartike Tiwari, Jyotirmoy Amin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Elite athletics throwing provides a structured biomechanical action sequence together with an objective continuous outcome, namely throw distance, making it a suitable setting for performance-oriented sports analytics. In this work, we investigate whether explicit phase alignment of pose dynamics improves throw-distance prediction under realistic broadcast conditions. To support this study, we curate Throwing4, a dataset of 500 elite throwing clips spanning javelin, discus, hammer, and shot put, with corresponding two-dimensional pose sequences, frame-level phase annotations, and official distance labels. We formulate throw-distance prediction from broadcast-derived pose as a regression problem and compare full-sequence modeling against a phase-conditioned approach that partitions each attempt into four technique stages and fuses phase-specific motion representations. Experiments across multiple graph-based pose encoders show a consistent reduction in prediction error when phase structure is incorporated, indicating that phase-aligned modeling provides a more stable representation than treating the entire motion as an unstructured sequence. These findings suggest that explicit biomechanical phase information is a useful inductive prior for pose-based performance modeling in elite athletics throwing. Beyond score prediction, the dataset and protocol provide a basis for future work on fine-grained technique analysis, interpretable sports analytics, and robust modeling from broadcast video.

---


### 411. [Risk-aware Road-network Trajectory Synthesis under Local Differential Privacy](https://arxiv.org/abs/2610.16384)

**<font color=#1a73e8>作者：</font>** Hongzhen Xiang, Chenxu Wang, Yumeng Song 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Road-network trajectory synthesis under local differential privacy (LDP) enables mobility data analysis without uploading raw trajectories to an untrusted server. Existing locally private trajectory synthesis methods mainly model whole trajectories, point sequences, or grid-level mobility patterns. However, they cannot handle non-uniform privacy risks caused by local road-network and trajectory contexts, such as endpoints, long-stay-associated regions, and low-out-degree branches. They also do not directly protect conditional next-hop choices on road networks, where a user's selected successor may reveal sensitive local movement intentions. To address these challenges, we propose TrajRACE, a locally private synthesis framework for road-network trajectories. TrajRACE uses start, segment-count, and transition reports to represent trajectories. For each transition, it keeps the current road segment as a public aggregation context and perturbs the true successor among legal successors on the client side. It then assigns risk-aware protection strengths to transitions according to local road-network and trajectory contexts. Finally, the server recovers population-level start, segment-count, and conditional transition statistics from heterogeneous privatized reports, and generates synthetic trajectories that follow the public road-network topology. Experiments on three road-network trajectory datasets demonstrate the effectiveness of TrajRACE in improving synthetic-data utility across distributional, query-based, and pattern-level metrics, while providing stronger protection for high-risk local transitions.

---


### 412. [Sampling from Neural Operator Priors to Solve Partial Differential Equations](https://arxiv.org/abs/2610.16396)

**<font color=#1a73e8>作者：</font>** Andrew Millard, Joshua Murphy, Zheng Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Guided sampling with sparse observations and PDE residuals has recently been combined with neural operator priors to solve partial differential equations in function space, their natural setting. We pair such a prior with pseudo-bootstrap sequential Monte Carlo (pBS SMC), a guided sampling framework that accommodates proposals without tractable densities, and introduce a new proposal by adapting the DPM++ algorithm to the guidance setting. Across five benchmark PDE systems this proposal attains the best error--time trade-off at every step count tested, and wrapping it in pBS gives the lowest error on most inverse-problem settings, with the largest gains when few sampling steps are used.

---


### 413. [Recursive Environment Scaling for General Long-Horizon Agents](https://arxiv.org/abs/2610.16397)

**<font color=#1a73e8>作者：</font>** Lingxiao Jing, Zhengbo Jiao, Yichen Xiang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study environment scaling as a way to increase agent-benchmark difficulty while holding core task objectives fixed. Our framework, Recursive Environment Scaling (RES), transforms existing benchmark environments while preserving their objectives and completion requirements. A proposer changes information access, resource relations, and execution dependencies; execution-grounded checks validate the resulting candidate, and accepted changes are inherited across rounds. This produces related environments for paired evaluation and training-trajectory collection. Experiments on 294 initial tasks from three benchmarks show lower task success for all six evaluation models, with decreases of 57.14--77.14 percentage points on Claw-Eval-Live. With equal trajectory counts and identical optimization settings, fine-tuning on RES trajectories outperforms original-trajectory SFT in all nine model--benchmark comparisons by 7.00--14.61 percentage points. Ablations identify recursive inheritance and dependency composition as important contributors to increased difficulty. Together, these results support environment scaling for both agent evaluation and training.

---


### 414. [Recovering from Pose-Selection Failures in Repeated Visual Localization](https://arxiv.org/abs/2610.16409)

**<font color=#1a73e8>作者：</font>** Jaehyun Kim, Wonseok Kang, Tae-Wan Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Repetitive structures can give an incorrect pose candidate more inlier support than an accurate one, causing visual localization to select it. History-Guided Pose Reselection (HPR) uses coarse position forecasts from up to five past localization outputs to distinguish well-separated current-query candidates. The best-fitting forecast proposes an alternative; HPR accepts it only if every well-fitting forecast is much closer to it than to the localizer's pose. HPR needs no odometry and returns the selected candidate unchanged, using prediction for selection rather than pose refinement. With one development-set threshold, HPR improves recall within 5 meters and 10 degrees in all 12 main configurations of Hierarchical Localization (HLoc), MASt3R-based pose generation, and JIST-based retrieval, losing successes on fewer than 0.4 percent of queries. On NAVER Gangnam B1, HPR corrects 97 HLoc failures and loses six successes; gains persist within 0.25 meters and 2 degrees on all three HLoc test sets. Median HPR runtime on HLoc candidates is below one millisecond, excluding pose generation. Recovery weakens under less frequent localization.

---


### 415. [What UI Design Can Do For "Good" Oversight Work: A Three-Month Action Research Study](https://arxiv.org/abs/2610.16410)

**<font color=#1a73e8>作者：</font>** Cedric Faas, Lisa Dargasz, Julius Gabelmann 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> With AI automating consequential tasks, human oversight is required for ethical, legal, and practical reasons. Yet these oversight tasks can be demanding and often make for poor work. Empirical evidence on overseers' lived work experiences remains underexplored, yet critical for designing ``good'' oversight. We provide longitudinal, in-the-wild insights through action research accompanying (N=8) tutors who oversaw an AI-supported learning assistant over three months. Our thematic analysis combines insights from twelve weekly meetings and two workshop iterations and was enriched by four repeated questionnaires. We identified stimulation, mastery, and relatedness as key challenges, stemming from the task's repetitiveness, unclear impact of interventions, and limited connections with students and peers. Informed by our initial findings, we deployed targeted UI modifications with mixed success. This paper documents the long-term evolution of the work characteristics of a real-world oversight task and discusses which oversight work characteristics can and cannot be supported by interface design.

---


### 416. [Chain Dimension Scaling: Communication-Efficient Loop-Style Scaling for Industrial Short-Video Ranking](https://arxiv.org/abs/2610.16415)

**<font color=#1a73e8>作者：</font>** Zhimeng Jiang, Yuening Li, Ruixiao Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Industrial recommendation rankers keep scaling in width and depth to billions of parameters, but this increasingly incurs costs in parameter growth, distributed communication overhead, and training inefficiency. We introduce \underline{C}hain \underline{D}imension \underline{S}caling (CDS), a scaling strategy orthogonal to width and depth. CDS repeatedly applies a single feature-interaction block with parameters shared across iterations, so the number of iterations (the chain length) becomes a new scaling dimension that adds no parameters. A lightweight intra-chain residual connection stabilizes optimization and improves quality. CDS enables two regimes. In the \emph{compression regime}, shallow blocks with a longer chain match deeper baselines with fewer parameters and faster training; in the \emph{quality-scaling regime}, increasing chain length under a fixed parameter budget yields consistent offline and online gains, suggesting the chain dimension adds modeling capacity beyond parameter reuse. We evaluate CDS in a large-scale multi-task short-video ranking system in production. In the compression regime, CDS stays within $0.03\%$ of baseline offline quality while reducing trainable parameters by 26.6\% and improving training throughput by 6.4\%, with neutral-to-positive online participation. In the quality-scaling regime, quality improves monotonically with chain length. Wall-clock analysis shows the efficiency gain comes mainly not from reduced FLOPs but from lower cross-device synchronization overhead and reduced optimizer update cost. These results position parameter-shared iterative computation as a practical, communication-efficient scaling axis for industrial ranking systems.

---


### 417. [Not All Challenges Are Equal: Evaluating Interactive Liveness Detection Against Real-Time Face Swaps](https://arxiv.org/abs/2610.16417)

**<font color=#1a73e8>作者：</font>** Anton Firc, David Drtil, Martin Perešíni 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote identity verification assumes that a camera stream shows a live person, yet public real-time face-swap tools can replace that person before the stream reaches the verifier. Passive deepfake detectors generalize poorly to new generators, while interactive challenges are often selected without evidence of which gestures expose current attacks. We evaluate randomized gesture challenges in 108 live sessions with six subjects, 24 impersonated identities, and two face-swap tools, DeepFaceLive and FaceFusion, injected through a virtual camera. The static calibration segment reaches a session-level AUC of 0.878 with a frozen UCF spatial detector, while the mean across the active-gesture windows reaches 0.988. Pose and combined gestures have the highest point estimates, whereas expressions show no clear improvement. Hand occlusion against FaceFusion, configured with an occlusion mask, scores below the static baseline. The end-to-end time required to satisfy the validator also distinguishes attacks from genuine sessions, achieving a session-level AUC of 0.732, although this signal includes synthesis and transport delays. These results show that challenge sets should be tested against current attack configurations and that response time can provide an additional, deployment-specific signal.

---


### 418. [Learning $ω$-Powered Conditional Distributions with Importance-Weighted Flow Matching](https://arxiv.org/abs/2610.16419)

**<font color=#1a73e8>作者：</font>** Maciej Falkiewicz, Frantzeska Lavda, Jason Ramapuram 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classifier-Free Guidance (CFG) with guidance scale $\gamma$ is commonly motivated by the $\omega$-powered conditional distribution obtained by setting $\omega=\gamma$, but CFG does not, in general, sample from this distribution exactly. We study whether the powered target can instead be learned explicitly. We introduce Importance-Weighted Conditional Flow Matching (IW-CFM), which reweights conditional flow-matching examples using density ratios obtained from frozen conditional and unconditional flow models. With exact normalized weights, the resulting objective has the same gradient as flow matching on the powered target; in practice, we use self-normalized estimation and a regularized empirical approximation for high-dimensional data. On synthetic distributions, IW-CFM recovers analytical powered targets for which numerically matched CFG, $\gamma=\omega$, exhibits a visible mismatch. On ImageNet, an amortized lightweight corrector achieves better alignment than fixed- and matched-guidance CFG with the corresponding weighted and filtered reference distributions. We additionally present an exploratory CLIP analysis of powered-density rankings on real ImageNet data. Aggregate shifts across selected prompt-specific contrasts coexist with heterogeneous classwise responses, including nonmonotonic trajectories. These results provide a practical route for studying and approximating model-defined powered conditional distributions.

---


### 419. [CultureBot: A Framework for Retrieval-Augmented Exploration of Cultural Heritage Data](https://arxiv.org/abs/2610.16435)

**<font color=#1a73e8>作者：</font>** Vasileios Karampinis, Angelos Vlachos, Giorgos Filandrianos 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Digital cultural heritage collections encode rich relations among objects, places, periods, providers, images, and source institutions, yet users typically access them through keyword search and faceted browsing. We present CULTUREBOT, an interactive framework for natural-language exploration of cultural heritage collections that combines knowledge-graph-guided retrieval, lexical-semantic retrieval, and source-linked generation. CULTUREBOT maps user queries to structured catalogue relations, enriches retrieved records with textual evidence, and generates answers that link back to the underlying repository records. We instantiate the framework on 81,852 SearchCulture records and release an online demonstration. In an expert evaluation involving six cultural-heritage specialists, 55 persona-grounded queries, and 250 evaluations, the graph-guided system was rated significantly higher than two general-purpose assistants and a non-graph ablation, with the largest gains in evidence grounding, diversity, reasoning, and completeness. These results support graph-guided retrieval as a practical way to expose the relational structure of cultural collections through conversational access while preserving links to catalogue evidence.

---


### 420. [RAP-WAM: Learning World-Action Models through Predictive Rehearsal and Action Perturbations](https://arxiv.org/abs/2610.16443)

**<font color=#1a73e8>作者：</font>** Yuanpeng He, Ceyao Zhang, Fangjing Li 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent world action models draw on video generation priors to jointly predict future observations and robot actions. Adapting these priors to control requires determining how future predictions should guide policy learning. RAP-WAM combines predictive Rehearsal and Action Perturbations (RAP) with future-supervised queries and Coupled Action Projection for policy learning. Predictive rehearsal trains on model-generated inputs while retaining recorded targets, and accumulates recurring errors into a spatial prior. We perturb actions and measure changes in video predictions. Action-response-based spatiotemporal credit assignment combines these responses, prediction error, and the rehearsal prior to allocate visual supervision; spatially aggregating the responses determines supervision intensity across future action steps. No separate scoring network or deployment-time probe is required. The base learns from a video-pretrained backbone without intermediate pretraining on external embodied data. We evaluate the fixed base and its agent-refined, task-conditioned system. On 42 RoboDojo tasks, their average success rates are 12.85% and 15.62%, with Scores of 17.86 and 20.59. Across 15 real-robot tasks, the complete system achieves 89.00% task-macro-average success, exceeding the strongest of five baselines by 37.67 percentage points. Across 315 fixed-output simulation windows, 45.21% of response-top20 positions fall outside error-top20, revealing information beyond prediction error.

---


### 421. [Tikhonov-Stabilized Bezier Representation Forecasting for Training-free Diffusion Acceleration](https://arxiv.org/abs/2610.16448)

**<font color=#1a73e8>作者：</font>** Lei Zhu, Mujie Lin, Ruochong Zheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models, particularly Diffusion Transformers, achieve strong image and video generation quality but remain expensive at inference time due to repeated denoiser evaluations. Feature caching offers a deployment-friendly acceleration strategy by reusing or predicting intermediate representations without retraining the generator or modifying the sampler. However, existing cache-then-forecast methods often rely on Taylor-style finite-difference extrapolation, which can become unstable over longer cache intervals, and typically predict local module outputs whose errors may accumulate through subsequent denoiser blocks. We propose \textbf{BeziCast}, a training-free diffusion acceleration framework that forecasts output-proximal denoising representations using low-order B'ezier trajectories. BeziCast estimates B'ezier control points via Tikhonov-stabilized fitting, providing a smooth, capacity-controlled temporal parameterization that avoids explicit high-order derivative estimation and decouples trajectory capacity from cache-query density. To moderate aggressive extrapolation, we further derive equivalent forecasting weights and introduce a convex-hull-inspired guardrail that detects high-risk predictions and softly pulls them toward a conservative simplex-projected estimate. Extensive evaluations across advanced image and video diffusion models demonstrate the effectiveness of BeziCast. In particular, BeziCast accelerates FLUX.1 by up to (4.79\times) and HunyuanVideo by up to (4.11\times), while preserving substantially better generation quality than competing acceleration baselines.

---


### 422. [CryptoFlowBench: Benchmarking Multi-Hop Reasoning on Blockchains for Cryptocurrency Fund Tracing](https://arxiv.org/abs/2610.16449)

**<font color=#1a73e8>作者：</font>** Runang He, Tongya Zheng, Jing Cao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Pseudonymous accounts and complex smart-contract ecosystems substantially hinder the tracing of illicit cryptocurrency fund flows. Existing Graph Neural Networks (GNNs) have achieved promising performance in blockchain fraud detection, yet their static node- or edge-level predictions do not naturally generalize to multi-hop fund tracing. Meanwhile, existing tracing methods mainly rely on predefined heuristics to capture multi-hop relationships, limiting their adaptive reasoning capabilities. To bridge this gap, we introduce CryptoFlowBench, a benchmark constructed from authoritative reports on cryptocurrency-related illicit incidents, with four tasks spanning local to multi-hop fund tracing. These tasks pose substantial challenges to existing learning- and heuristic-based methods, particularly in complex multi-hop scenarios. We therefore propose ChainSleuth, a graph-tool-augmented agent that iteratively reasons, invokes graph tools, and updates its tracing trajectory, enabling adaptive information acquisition and recovery from erroneous paths. Experiments show that no baseline consistently dominates all four tasks, revealing substantial gaps between local fraud detection and multi-hop fund tracing. ChainSleuth achieves notable improvements on multi-hop tasks, demonstrating the potential of agentic graph reasoning for cryptocurrency fund investigation.

---


### 423. [Not Every Cue Is Evidence: Cue Supportability for Forensic Distillation in Face Forgery Detection](https://arxiv.org/abs/2610.16452)

**<font color=#1a73e8>作者：</font>** Binjia Zhou, Dawei Luo, Shuai Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Explainable face forgery detection requires not only correct judgments but also forensic evidence supported by the input image. However, training cues are typically derived from the forgery generation pipeline. Since images available to the model are of limited quality and resolution, it is difficult to observe the fine-grained traces these cues refer to. Training methods that further supply such cues as privileged supervision exacerbate the problem, as the student is taught to articulate evidence it cannot perceive. The student consequently resorts to templated or over-generalized expressions, giving rise to the correct-answer, wrong-evidence (CAWE) failure. We propose a dual supportability audit that filters privileged cues before distillation. Each candidate cue must be predictable from the remaining privileged context and causally tied to high-attribution visual regions in the current image. Only cues satisfying both conditions receive substantial distillation weight, preventing unsupported details from leaking into the student. Experiments across eight benchmarks show that our method maintains or improves detection accuracy while significantly raising explanation faithfulness compared to existing paradigms.

---


### 424. [GHOST: Geometry-Constrained Hybrid Diffusion for Open-Vocabulary 3D Scene Graph Generation](https://arxiv.org/abs/2610.16455)

**<font color=#1a73e8>作者：</font>** Changqun Feng, Wangxiandi Yin, Xin Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D scene graph generation requires understanding both object semantics and metric spatial relations. However, existing open-vocabulary methods often struggle with spatial predicates because language similarity reflects semantic co-occurrence rather than explicit geometry. We propose GHOST, a Geometry-constrained Hybrid diffusion framework for Open-vocabulary 3D Scene graph generaTion. GHOST jointly models continuous node geometry and discrete edge predicates, following a geometry-to-constraint-to-predicate denoising process to ensure geometrically consistent relation prediction. It introduces language-grounded constraint induction, which maps predicate embeddings to differentiable geometric constraints that guide both layout refinement and predicate reweighting. A Geometry-Topology Collaborative Denoiser further couples node and edge reasoning through noise-adaptive interaction and orientation-aware modeling. Experiments on 3DSSG demonstrate state-of-the-art performance in both closed-set and open-vocabulary settings, including over 17-point gains over RelationField on spatial predicates.

---


### 425. [Foresee: Making Procedural Futures Tangible through Generative Previews](https://arxiv.org/abs/2610.16469)

**<font color=#1a73e8>作者：</font>** Yusi Sun, Ying Jiang, Jiayin Lu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Procedural guidance can show users how to act without explaining what an action enables later. We present Foresee, an interface combining next-step guidance with consequence previews, method comparisons, and cross-step access. A hybrid pipeline combines structured rendering, image editing, and video generation. A literature-informed framework and six-participant formative study shaped its design. A 24-participant study compared AR guidance, AR with generated video, and Foresee across digital painting, gameplay, and cocktail making. Exploratory painting comparisons showed higher correct completion without a recorded error than AR and higher post-task quiz accuracy than generated-video guidance under task-wise correction. Interviews revealed that users could overlook valued explanations, match visible outcomes without understanding later possibilities, or wait for concrete demonstrations when symbolic cues were unclear. These findings inform generative previews that explain what actions enable or constrain while supporting ongoing execution.

---


### 426. [Auditing Observation-Quality Shortcuts in the Evaluation of Person-Centered Motion for Video Anomaly Detection](https://arxiv.org/abs/2610.16471)

**<font color=#1a73e8>作者：</font>** Chaehyun Kim, Changwon Lim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video anomaly detection (VAD) identifies deviations from normal patterns, but such deviations do not necessarily correspond to safety-critical events. We focus on human-centered emergencies and violence and investigate whether motion-based anomaly discrimination reflects task-relevant motion information or observation-quality differences arising from person detection, pose estimation, and tracking. We introduce an observation-quality-aware evaluation framework that combines quality diagnostics, quality balancing, motion orthogonalization, and robustness analyses. On human-centered categories of UCF-Crime, quality-only features match or exceed the discrimination of multi-cue motion in the original cohort, revealing a strong observation-quality shortcut. After cardinality matching brings all 11 measured quality variables below a prespecified marginal balance threshold, multi-cue motion consistently outperforms quality-only features across Logistic Regression, Random Forest, and RBF-SVM, yielding ROC-AUC gains of 0.046-0.141. Because nonlinear quality-only prediction remains above chance after matching, we interpret this result as additional discrimination beyond measured marginal quality rather than as evidence of quality-free or causal motion understanding. These findings show that high VAD performance should not be interpreted as evidence of abnormal-motion modeling without auditing the reliability of the person-observation pipeline. Our study provides a systematic protocol for evaluating observation-quality shortcuts and for assessing whether motion-based discrimination survives explicit control of detection, pose-estimation, and tracking reliability.

---


### 427. [Ontology-Based Post-Coordinated Expression Assembly: from Clinical Narrative to Queryable Knowledge Graphs](https://arxiv.org/abs/2610.16474)

**<font color=#1a73e8>作者：</font>** Johann Pignat, Christophe Gaudet-Blavignac, Julien Ehrsam 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical oncology documentation records decisive information in free text, where it remains readable but not retrievable at scale, leaving cohort identification dependent on incomplete diagnostic codes or manual review. The current standard, coding individual terms, captures what a document mentions, not what it asserts: meaning lies in how those terms relate to one another. We present a method for deriving queryable knowledge graphs from clinical narratives, conforming to the Extended Grammar of SNOMED CT across multiple ontologies. The method specifies how entities should be annotated and related. It defines five relation classes, each bound to a construction rule that assembles the entities and relations into post-coordinated expressions. A deterministic implementation, UNIGRAPHE, applies those rules to construct knowledge graphs from annotated text. Applied to expert-annotated real-world oncology documentation, UNIGRAPHE reconstructed 5,299 annotations into 2,196 post-coordinated expressions and shows that relation structure is the missing piece to make clinical narrative formally queryable.

---


### 428. [XAI-Guided Fourier Domain Generalisation for Pure-Simulation Sim-to-Real Deep Reinforcement Learning](https://arxiv.org/abs/2610.16478)

**<font color=#1a73e8>作者：</font>** Wei Yao, Chuyao Wang, Ziwei Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep reinforcement learning has shown strong potential for vision-based autonomous driving, but policies trained in simulation often suffer severe performance degradation when deployed in the real world. Existing sim-to-real methods commonly address this gap through image-transfer-based domain adaptation or policy-agnostic domain randomisation. However, the former requires laborious acquisition of target-domain data and is often limited to the deployment domain, whereas the latter introduces unguided perturbations that may not reflect the underlying sim-to-real discrepancy, leading to suboptimal transfer performance. To overcome these limitations, we propose XFD, an explainable artificial intelligence (XAI)-guided Fourier domain generalisation framework for pure-simulation sim-to-real reinforcement learning. The proposed framework extracts explainability attribution maps from simulated observations, and converts these attributions into policy-conditioned Fourier-domain interventions. By perturbing appearance-sensitive spectral components while preserving task-defining spatial structures, XFD constructs robustness-enhancing visual domains entirely within simulation. Subsequently, the proposed robust policy optimisation guides the policy towards attending to task-critical features while suppressing sensitivity to irrelevant visual information. Extensive experiments in simulation and zero-shot real-world deployment demonstrate that XFD consistently improves traveled distance and reward over standard policy and randomly domain-randomised baseline, especially on unseen maps with cluttered backgrounds. Attribution-based analysis further proves that the proposed policy preserves more consistent task-relevant visual evidence across simulation and real-world observations.

---


### 429. [PXRD-Bench: How Close Are We to Determining Crystal Structures from Powder Diffraction?](https://arxiv.org/abs/2610.16480)

**<font color=#1a73e8>作者：</font>** Dongyeop Woo, Nofit Segal, Nayoung Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Determining crystal structures from powder X-ray diffraction (PXRD) would enable routine characterization of newly synthesized materials, including those absent from reference databases. Generative models offer a promising approach, but existing evaluations remain fragmented and largely assume single-phase samples with known composition. To fill this gap, we introduce PXRD-Bench, a unified benchmark that extends evaluation to unknown per-element atom counts and recovery of both structures in two-phase mixtures. It provides approximately 4.1 million training structures with simulated PXRD, tests generalization to unseen compositions and structural prototypes, and evaluates recovery from experimental PXRD after excluding structurally matching training entries. To provide a strong reference baseline, we also introduce Bragglite, a PXRD-to-structure model developed through a systematic study of PXRD modeling choices. It achieves a 44.2\% Top-1 match rate on experimental RRUFF patterns with known composition, 24.6\% above the strongest prior baseline. Further analysis yields several key findings: some models fail to benefit from experimental PXRD, while generalization to unseen structural prototypes and recovery from two-phase mixtures remain challenging. Together, our benchmark, systematic studies, and Bragglite clarify the capabilities and limitations of current PXRD-to-structure models.

---


### 430. [Drafting Agents, Not Just Tokens: Speculative Recursive Self-Improvement for Agentic Systems](https://arxiv.org/abs/2610.16491)

**<font color=#1a73e8>作者：</font>** Xin Xu, Ke Cheng, Hao Wang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Improving an agent through successive revisions requires balancing exploration and evaluation under a limited budget. A narrow search can miss useful sequences of edits, while fully evaluating every intermediate version can exhaust the budget before those sequences yield a verified improvement. We introduce Speculative Recursive Self-Improvement (SpecRSI), which drafts executable successor agents before their predecessors are fully evaluated, while requiring complete verification before adoption. Verification-Aware Tree Search (VATS) allocates the budget between further edits and outstanding checks using the predicted verified return of a continuation. Group Verification Optimization (GVO) learns the improver from completed searches while keeping the real evaluator fixed. In the main scientific comparison, terminal gains exceed Janus by 33.3%--40.0%. Additional evaluations show that SpecRSI outperforms Janus in all 50 scientific backbone--task pairs and exceeds MetaRSI-v1 by 1.85%--2.38% in macro-average system score across twenty backbones. Coding-validation success reaches 69.4% versus HGM's 64.3% at a 20.8% lower target-cost index.

---


### 431. [Self-Verifier Capture in Unified Visual Generators: Diagnosing and Repairing Closed-Loop Self-Reward](https://arxiv.org/abs/2610.16500)

**<font color=#1a73e8>作者：</font>** Binyan Chen, Tong Pan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image-space reward requires decoding and a separate judge; unified visual generators can instead reuse their understanding pathway for decode-free, self-supplied reward. Optimizing against this verifier closes the self-reward loop; shared trainable weights let one update move generation and scoring even with the reward gradient stopped. We call the resulting failure self-verifier capture: self-reward rises while independently measured quality falls. Matched semantic/denoising by shared/frozen cells on Scale-RAE isolate two routes: the policy exploits on-manifold blind spots of a frozen semantic judge, while shared updates additionally rewrite the judge. A frozen judge also becomes stale, and repeated self-refresh yields progressively weaker recoveries. The diagnosis yields a two-part repair: locking the warmed reward read blocks rewriting, while sparse, parameter-disjoint external anchors counter residual exploitation. Unanchored rollouts retain semantic reward across multiple latent noise levels, providing dense latent reward that terminal image-space judging cannot supply, while a drift-triggered controller allocates anchors to high-drift rollouts and propagates their calibration within each group. At matched budgets, the controller improves on fixed-dose anchoring, increasingly so as coverage tightens. Both the unanchored failure and the repair transfer to the higher-performing, architecturally distinct Show-o2. Across both bases, the complete method significantly outperforms a construct-matched every-rollout judge on GenEval and DPG-Bench while externally scoring only 1/16 of rollouts. At 1/32 coverage, it scores higher in all four comparisons and remains jointly non-inferior.

---


### 432. [pi-Net: Empirical Latent Representations for Differentiable Physics Heads in Data-Scarce Systems](https://arxiv.org/abs/2610.16504)

**<font color=#1a73e8>作者：</font>** Akshay Dhalpe, Arnab Chattopadhyay, Shahriar Bakrani Balani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Developing reliable predictive models for multi-physics systems often forces a compromise between computationally demanding physical simulators and data-hungry, opaque machine learning (ML) algorithms. While incorporating dimensional analysis into directed computation graphs offers a structurally sound alternative to explicitly solving partial differential equations (PDEs), such formulations typically yield underdetermined systems that act as imperfect simulators. We introduce pi-Net, a physics-informed latent variable model that resolves these imperfect simulators. The hybrid pi-Net architecture consists of an encoder that maps inputs into physically normalized latent space, which are then decoded into final predictions by a differentiable physics head. Evaluated on a real-world, data-scarce Gas Metal Arc Welding (GMAW) case study, the framework achieves an R2 of 0.864 with only 60 experimental samples. The results demonstrate that pi-Net significantly outperforms purely data-driven baselines in data-scarce regimes while providing causal, process-level explainability.

---


### 433. [Boosting the Learning for Ranking Patterns](https://arxiv.org/abs/2610.16511)

**<font color=#1a73e8>作者：</font>** Nassim Belmecheri, Noureddine Aribi, Nadjib Lazaar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pattern mining is a valuable tool for exploratory data analysis, but identifying relevant patterns for a specific user is challenging. Various interestingness mea- sures have been developed to evaluate patterns, but they may not efficiently estimate user-specific functions. Learning user-specific functions by ranking patterns has been proposed, but this requires significant time and training samples. In this paper, we present a solution that formulates the problem of learning pattern ranking functions as a multicriteria decision making problem. Our approach uses Analytic Hierarchy Process (AHP) to elicit weights for different interestingness measures based on user preference. We also propose an active learning mode with a sensitivity-based heuristic to minimize user ranking queries while still providing high-quality results. Experiments show that our approach significantly reduces running time and returns precise pattern ranking while being robust to user error, compared to state-of-the-art approaches.

---


### 434. [Asymptotic Risk of Learning-Rate Schedules for Least-Squares Regression with Discretely Distributed Features](https://arxiv.org/abs/2610.16518)

**<font color=#1a73e8>作者：</font>** Noé Colomban, Francis Bach, Fabian Schaipp  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the last iterate of stochastic gradient descent (SGD) on streaming least squares with discretely distributed features (Slock's model), which decouples the dynamics across eigendirections. Under power-law source and capacity conditions, we derive the exact finite-time risk and asymptotic equivalents of constant and Warmup-Stable-Decay (WSD) schedules. With a tuned base learning-rate, the resulting scaling law decays as $\Theta(T^{-q})$, where $T$ is the horizon, and $q$ is independent of the cooldown length $c \in (0,1]$ but is strictly smaller for the constant schedule: any cooldown of fixed relative length $c > 0$, however short, improves the risk by a polynomial factor, while its length only affects the constant, which is minimized by linear decay ($c = 1$). Finally, we show that the optimal risk depends on the batch size $b$ and horizon $T$ only through $bT$, up to a critical batch size.

---


### 435. [Reinforcement Learning with Hawkes-Structured Networks for Market Making](https://arxiv.org/abs/2610.16524)

**<font color=#1a73e8>作者：</font>** Fernando Acero, Philipp Plank, Yufei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Market making under realistic order-flow dynamics is challenging due to the clustered, self-exciting nature of order arrivals, which are naturally modeled by non-Markovian Hawkes processes. We propose a model-free reinforcement learning (RL) framework for market making with general Hawkes order-flow dynamics. We first establish non-asymptotic performance bounds that quantify the loss incurred by approximating the infinite-dimensional Hawkes state using a finite collection of exponentially weighted features. Guided by this analysis, we introduce the Hawkes-Structured Network (HSN), a novel neural architecture that encodes historical order flow through a learnable mixture-of-exponentials filter. HSN is trained end-to-end using model-free RL, jointly optimizing the feature representation and quoting policy directly from reward feedback. Experiments on single- and multi-asset market-making problems with mixture-of-exponentials, power-law, and regime-switching kernels demonstrate that HSN outperforms general-purpose neural architectures, achieving higher trading rewards while implicitly recovering the underlying order-flow intensities.

---


### 436. [Deep Learning-based Mechanical Characterization of Synthetically Generated Plant Fibers under Transverse Compression](https://arxiv.org/abs/2610.16529)

**<font color=#1a73e8>作者：</font>** Nikolaos Kegkeroglou, Bilal Sabillah, Myrto Inglezou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Plant fibers are increasingly used as sustainable reinforcements in composites, but the intrinsic variability of their microstructure causes substantial scatter in transverse mechanical behavior, complicating composite design. Characterizing this behavior relies on finite element (FE) simulations requiring several minutes of high-performance computing per fiber, making high-throughput characterization across realistic fiber populations impractical. In this study, we propose a deep learning framework replacing this FE bottleneck with a fast pipeline. It includes two coupled recursive U-Nets predicting the step-by-step evolution of fiber deformation and internal stress fields under transverse compression, followed by a regression CNN estimating the transverse Young's modulus from the final stress field. Unlike prior approaches predicting stress fields for fixed configurations or idealized geometries, our framework recursively resolves the full temporal stress evolution for synthetic fibers derived from real hemp cross-sections, with or without a lumen. Trained on 1,000 synthetic fiber geometries with FE ground truth, it reproduces the stress field sequence with a Structural Similarity Index Measure (SSIM) of $0.9574 \pm 0.0074$ and a Root Mean Squared Error (RMSE) of $0.0345 \pm 0.0079$. It estimates transverse Young's modulus with an $R^2$ of $0.938 \pm 0.024$, a Mean Absolute Error (MAE) of $24.31 \pm 1.23$ MPa, and a Mean Absolute Percentage Error (MAPE) of $5.25 \pm 0.91\%$. Inference requires under one second per fiber versus five minutes per FE simulation, drastically reducing computational cost. This offers a fast, reliable tool for mechanical characterization of synthetic plant fibers, with promising applications in designing natural fiber-reinforced composites.

---


### 437. [Does the Explanation Drift Before the Guarantee? Label-Free Early Warning on Evolving Graphs](https://arxiv.org/abs/2610.16534)

**<font color=#1a73e8>作者：</font>** Tomasz Szandała, Damian Raczkowski  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deployed models can fail silently as the world they describe evolves. Attribution drift has served as an early warning in tabular data; we ask whether, in graph streams, a model's own explanations can forewarn the loss of nominal conformal coverage. Doing so requires repairing the naive drift statistic twice. A vanishing edge loses mask mass regardless of whether the model relied on it, so we condition the importance on edge presence. Evolving graphs also break edge identity: a relabelling that changes nothing shifts the identity-based statistic by 0.69 on synthetic graphs and 0.83 on real ego-networks, whereas aggregating over structural roles brings both to 0.0 and stays well-defined when the support changes. We test six pre-registered regimes on thirty seeds each. A two-channel monitor, tracking conditional mask mass and its distribution over roles, precedes coverage collapse by 8 to 14.5 steps across four gradual regimes (node addition, removal, replacement, and edge thinning), all surviving Holm correction. A sudden knockout yields the expected zero lead, and a harmless change triggers no alarm. Leads track the length of the transitional phase (Spearman 0.79 over 150 runs). On real transaction ego-networks, the untuned mass channel forewarns staged drift by 27 steps and is the only channel, attributional or structural, that never alarms on a stationary stream. The main limitation is that the mass channel is blind to covariate drift, which breaks the guarantee in every run; the distributional channel detects it and also rescues the rewiring regime, so we report the two channels separately rather than as a union.

---


### 438. [Learning Graded Sparse Mechanisms: A Representation Theorem and Certified Generalization](https://arxiv.org/abs/2610.16537)

**<font color=#1a73e8>作者：</font>** Mark Kozdoba, Shie Mannor  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In a variety of multi-agent and physical environments, an element's update depends strongly on a few other elements and weakly on many, and both the identity and the number of the elements that matter change with the state of the system. Such graded sparse mechanisms are common, for instance, in flocks, crowds, learned particle simulators and the neighborhood aggregation of graph networks, yet they have received little systematic study as a class of functions with the grading given. In this paper we study the supervised learning of the mechanism when the grading is provided by the environment, as a weight on every element. First, we define the class by axioms, where each element's influence is capped by its weight, the dependence on the weights is regular, and no element is distinguished, and prove a representation theorem: the class is exactly the Lipschitz ball of a transport metric on weighted multisets, and the metric is forced by the axioms. Next, the geometry of the representation gives generalization bounds that depend on the data in two ways. One is via the sparsity profile of the data -- the law of how many elements matter and by how much -- which bounds the rate over all designs with that profile, with an exponent from the profile and no dependence on the number of elements. In a number of natural cases we also show matching lower bounds, up to constants in the exponent. The other is empirical: due to the representation result, classical empirical discrepancy bounds apply to the class as they stand, and the resulting bound is the transport distance between the two halves of the sample in the class's own metric, computed exactly by a matching, with an additional concentration term. Finally, we study a simulated Vicsek flock under four interaction rules at two noise levels, and show that the certificate is non-vacuous, a small fraction of the trivial value on every rule.

---


### 439. [PatTransBench: an ipc-stratified, multi-dimensional benchmark for patent machine translation evaluation](https://arxiv.org/abs/2610.16538)

**<font color=#1a73e8>作者：</font>** Xiaowei Su, Xusen Cheng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present PatTransBench, a 12,000-item Chinese-English/Japanese/Korean patent machine translation (PatMT) benchmark with a four-dimensional evaluation protocol. The benchmark comprises 6,000 short-text (sentence/claim) and 6,000 long-text (paragraph) pairs, evenly split across three language pairs and both translation directions, built via IPC-section-stratified sampling and dualthreshold quality gating from upstream patent-family parallel corpora. The evaluation protocol spans literal n-gram overlap (BLEU, ROUGE-L, chrF), cross-lingual semantic textual similarity (CLSTS), 38-probe-language consistency testing, and serving performance under concurrency. A case study on PatMT2-7B and its fp8/AWQ4/AutoRound-4bit variants reveals direction-dependent quantization effects masked by aggregate scores and non-monotonic language-failure patterns across quantization schemes that are invisible to single-metric evaluation. We plan to release the benchmark, protocol, and case-study results upon publication to support reproducible PatMT evaluation.

---


### 440. [Overtaught, Underlearned: Learner-Centered Distillation from Multi-Agent Discussion](https://arxiv.org/abs/2610.16543)

**<font color=#1a73e8>作者：</font>** Mengtao Zhou, Jianxiao Wang, Xiupeng Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent discussion produces reasoning collaboratively, while deployment still relies on a smaller student that must answer alone. Full-graph distillation transfers such discussions by treating each correct solution as a separate training target, but what teachers provide need not match what the student learns. This mismatch appears in two ways: several correct solutions may amount to the same lesson in the student's representation (over-teaching), while some training questions remain missed after learning (under-learning). We quantify both with rates that are high on discussion graphs. To address them, we introduce FAR (Fold--Attempt--Revisit), a learner-centered distillation procedure that organizes supervision around the student's own state. Before training, FAR folds solutions within each discussion state into representative lessons. After training, the student's own attempts identify missed questions, while poorly represented clusters indicate where folding may have lost useful variation; FAR then writes targeted lessons from retained discussion contexts. Across two students and four reasoning tasks, FAR outperforms full-graph distillation with far fewer training targets and lower under-learning. Further analyses examine the behavior of FAR and the sources of its gains. Overall, the results show that organizing discussion supervision around the student can make distillation both more effective and more efficient.

---


### 441. [Heuristics are Not Enough: Calibrated and Corrected Caching for Video Diffusion Acceleration](https://arxiv.org/abs/2610.16545)

**<font color=#1a73e8>作者：</font>** Jiyue Jiang, Zhiyu Huo, Yuhan Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feature caching has become a mainstream training-free strategy for accelerating video diffusion models by reusing intermediate outputs across denoising steps. However, existing adaptive methods rely on heuristic difference measures misaligned with actual generation quality, employ a single global threshold that ignores heterogeneous phase dynamics, and never validate their budget estimates against true approximation error, allowing systematic bias to propagate uncorrected. We propose \textbf{AlignCache}, a closed-loop caching framework that directly aligns scheduling decisions with their true influence on the final generated video through three tightly coupled components: (1) phase-adaptive budget routing that partitions the denoising trajectory into structurally distinct phases, each governed by an independent threshold and a staleness-aware guard; (2) closed-loop threshold calibration that exploits counterfactual error measurement at the classifier-free guided output level to adjust decision boundaries online via an EMA feedback loop; and (3) momentum-augmented draft synthesis combining direction-magnitude gated residual extrapolation with anchor-guided unconditional correction. By transforming scheduling from a static risk accumulator into a feedback-driven, self-correcting controller, AlignCache consistently achieves superior acceleration-quality trade-offs across state-of-the-art video generation models. Our code is available at this https URL.

---


### 442. [DeepFlow: Two Convergent Differentiable Approaches for Pairwise Conditional Random Fields](https://arxiv.org/abs/2610.16546)

**<font color=#1a73e8>作者：</font>** John S. H. Baxter  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Basic probabilistic models form the basis of modern deep learning largely by defining the final activation layer of a network and allowing the networks outputs to be interpreted through a probabilistic lens. By increasing the complexity of these final activation layers to include features such as spatial regularisation, allow for these models to improve in performance without requiring significantly more data. The challenge however is to ensure that these more complex probabilistic graphical models adapt well to being used in tandem with deep learning, that is, ensuring they converge and have meaningful derivatives. The goal of this paper is to show two algorithms with provable convergence properties to allow this type of regularisation for image and signal classification models. Through both rigorous mathematical analysis and in silico experiments, we can show the differing performance between these solution types.

---


### 443. [Know Yourself and Know Your Neighbour: A Syntactically Informed Self-Supervised Compositional Sentence Representation Learning Framework using a Recursive Hypernetwork](https://arxiv.org/abs/2610.16547)

**<font color=#1a73e8>作者：</font>** Vasudevan Nedumpozhimana, John Kelleher  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sentence representation learning is still an open challenge in Natural Language Processing. In this work, we propose a new self-supervised framework for learning sentence representations, using a special type of neural network called a recursive hypernetwork. Our proposed model composes the representation of a sentence from representations of words by applying a recursive composition through the parse tree. We maintain a separate syntactic and semantic representation, and the semantic composition is guided by the information from the syntactic representation. To train this model, we introduce a novel set of six self-supervised tasks. By analysing the performance on 7 probing tasks, we validate that the generated sentence representation encodes richer linguistic information than both averaging baselines and state-of-the-art alternatives. Furthermore, we assess the impact of the six proposed self-supervised training tasks through ablation studies. We also demonstrate that the representations generated by our model are stable for sentences of varying length and that the semantic composition operators adapt to different syntactic categories\footnote{Code available: this https URL}.

---


### 444. [NoduleFlow: Automatic 3D Lung Nodule Detection and Segmentation](https://arxiv.org/abs/2610.16548)

**<font color=#1a73e8>作者：</font>** Giulia Romoli, Filippo Ruffini, Francesco Di Feola 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low dose Computed Tomography (CT) is the standard imaging modality for lung cancer screening. On CT scans, lung cancer typically manifests as pulmonary nodules, whose manual identification is time-consuming and prone to observer variability, image quality limitations, and suboptimal reading conditions. Moreover, subtle temporal changes are often difficult to quantify reliably in CT scans from the same patient across follow-up examinations. Deep learning-based approaches for the automatic detection and segmentation of lung nodules have demonstrated improved accuracy and efficiency. However, most existing approaches provide only coarse region-of-interest localisation, rely on prior lesion annotations or human supervision, or treat detection and segmentation as separate tasks. In this work, we present NoduleFlow, a framework for lung nodule detection, classification, and segmentation directly from series of CT volumes. Our proposal consists of four interconnected modules and operates in an automated manner at inference time, without requiring prior lesion annotations, manual initialisation, or region-of-interest pre-selection. We further investigate whether nodule localization benefits from the propagation of candidate regions across follow-up scans through inter-scan registration fields, as opposed to conventional independent per-scan analysis. The generalisability of the framework is systematically evaluated across four independent datasets. The results underscore the potential of automated pipelines for lung nodule analysis in screening and diagnostic settings.

---


### 445. [Making Language the Low-Rate Code of Vision: Successive Refinement from Words to Pixels](https://arxiv.org/abs/2610.16552)

**<font color=#1a73e8>作者：</font>** Ruilin Gong, Hao Gong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An ordered visual code lets a short prefix stand in for an image, and the training loss decides what that prefix contains. Under pixel reconstruction the first bits go to the directions of highest variance, and we prove that a caption can then be independent of the entire first half of a code that is rate-optimal for pixels at every length. In the rate-distortion sense a caption is therefore not the low-rate code of its image, unless the code is built to make it one. We study that construction and what it costs. We cast captioning and text-to-image generation as successive refinement under a distortion measure that changes along the code, from caption log-loss in the early stages to pixel distortion in the last, so that each stage is compared with its own optimum. Putting words first then costs nothing among the caption stages exactly when the captions form a summarization chain, and it costs the pixels at most the caption uncertainty left in a pixel-optimal reconstruction, which is large for short prefixes and small at full length. We build RUNG, an ordered code whose prefixes are supervised by a summarization ladder of captions and whose full length reconstructs the image; generation extends the code past the prompt and captioning truncates it. With data and capacity held fixed, ordering by language instead of reconstruction raises prefix-caption information 2.9 times and GenEval from 0.76 to 0.83, at a measured cost of 2.8 dB PSNR at a quarter of the code and 0.1 dB at full length. RUNG-XL (3.4B) reaches 0.88 GenEval and 87.6 DPG-Bench in 32 network evaluations and 0.91 GenEval when errors are redrawn at the rung where they appear; its coarse and fine captions agree 94.1% of the time, and it edits images without inversion.

---


### 446. [AI Discovery in Combinatorics: From Problems to Solutions and Back to Bigger Problems](https://arxiv.org/abs/2610.16555)

**<font color=#1a73e8>作者：</font>** Eugenio Cainelli, Lorenzo Luccioli, Alessandro Iraci 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce $qt$Bench, a benchmark of 29 open problems in algebraic combinatorics. These problems ask for a simple combinatorial algorithm that explains given polynomial coefficients or identities. To help AI agents search for such algorithms, we provide a scaffold for playing with combinatorial objects, countering cheating attempts, and testing candidate solutions. To explore how far frontier AI systems can go on these problems, we collaborated with OpenAI, whose researchers obtained proposed solutions to several of them. This highlights bigger meta-problems: is AI discovery at scale ethical? How should these results be released? How should proof digestion be organized? We discuss these questions and give our views.

---


### 447. [G$^2$WAM: World Action Models for Efficient and Geometry Grounded Image-Goal Navigation](https://arxiv.org/abs/2610.16558)

**<font color=#1a73e8>作者：</font>** Ke Gui, Chenghao Shi, Ziyue Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models capture environment dynamics and support counterfactual reasoning for planning. In image-goal navigation, where the target often lies beyond the current field of view, the agent must not only model environmental dynamics but also maintain a persistent spatial memory of the scene. Existing approaches either introduce spatial context by fine-tuning pretrained models on the target task, which underexploits their spatial priors, or rely on external 3D reconstruction, which is computationally expensive for real-world deployment. In this paper, we propose the Geometry Grounded World Action Model (G$^2$WAM) for image-goal navigation. G$^2$WAM encodes spatial cues through a learned scene-coordinate localization module that anchors the current, goal, and history frames in a common reference frame, yielding a stable and consistent spatial context that enables efficient navigation without explicit 3D reconstruction. Following the world-action-model paradigm, G$^2$WAM jointly predicts future states and actions, eliminating the need for costly cross-entropy method (CEM) style planning. In addition, G$^2$WAM operates entirely in latent space, avoiding the computational burden of pixel-level reconstruction and substantially reducing inference cost. Across four trajectory prediction benchmarks, G$^2$WAM reduces average ATE and RPE by 40.1% and 35.2%, respectively. In closed-loop navigation experiments, it improves the success rate from 54.0% to 63.0% and the success weighted by path length (SPL) from 36.4% to 59.2%, while maintaining high efficiency.

---


### 448. [Optimal Transport PAC-Bayes Bounds](https://arxiv.org/abs/2610.16560)

**<font color=#1a73e8>作者：</font>** Armin Beck, Peter Ochs, Jalal Fadili  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> PAC-Bayesian generalization bounds are among the strongest distribution-dependent guarantees in statistical learning and are typically expressed in terms of the Kullback-Leibler (KL) divergence between a prior and posterior distribution. While analytically convenient, the KL divergence requires the posterior to be absolutely continuous w.r.t. the prior, imposing support constraints that can substantially restrict the choice of posterior. Moreover, the KL divergence does not account for the underlying geometry of the probability space. In this work, we derive new PAC-Bayesian bounds replacing the KL divergence with general optimal transport (OT) distances, including the total variation and Wasserstein-$p$ distances.

---


### 449. [The Language of Looking: Motion Tokens Reveal Domain-Dependent Local Structure in Gaze Sequences](https://arxiv.org/abs/2610.16565)

**<font color=#1a73e8>作者：</font>** Virmarie Maquiling, Enkelejda Kasneci  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Human gaze is the primary high-bandwidth interface through which we parse the semantics of our environment. While often modeled as a sequence, the degree to which gaze exhibits transferable local structure across domains remains underexplored. Using motion tokenization as a diagnostic lens across four diverse datasets, we investigate the transferability of local sequence structure. We demonstrate that while gaze can share a reusable motion-token vocabulary, identical motion tokens are organized into different local transition patterns depending on the dataset and task context. Our results show the limitations of naive data-pooling under low-semantic motion-token representations and provide a framework for evaluating behavioral sequences through information-theoretic diagnostics.

---


### 450. [Dense Endoluminal Mapping and Localisation from Monocular Bronchoscopy](https://arxiv.org/abs/2610.16570)

**<font color=#1a73e8>作者：</font>** Salvatore Esposito, Matias Mattamala, Daniel Rebain 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bronchoscopy inserts a camera through the airways to diagnose endoluminal disease. Locating the camera along the airway usually requires additional equipment, such as an electromagnetic tracker and a preoperative CT scan. In this paper, we investigate the use of the monocular camera stream to localise the bronchoscope without requiring additional sensing. We introduce a monocular SLAM system that localises the tip of a bronchoscope and reconstructs the airway surface around it from RGB video alone. A Depth Anything 3 backbone, fine-tuned on over a million photorealistic airway renderings, returns metric per-pixel depth and is the system's only source of scale. DINOv3 features routed through a custom cross-attention matcher supply sub-pixel correspondences on mucosa where classical descriptors fail. Both enter a factor graph alongside a dense constraint from projective iterative closest point (ICP) registration against the system's own running reconstruction, so surface evidence stabilises the directions the visual factors leave weakly observable. On six airways rendered from patient CT scans, the system reaches 26.1 mm mean absolute trajectory error and 77.5% mean surface F-score. Its mean surface accuracy exceeds that of five recent monocular SLAM and feed-forward baselines. MASt3R-SLAM, which fits a free scale to the ground truth, has a lower mean trajectory error (22.0 mm). ORB-SLAM3 completes only two of the six airways, whereas our system completes all six and also reconstructs two ex vivo specimens.

---


> [!TIP]
> 当前位于：**401-450**（第 9/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
