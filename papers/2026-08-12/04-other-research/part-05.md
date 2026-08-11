# 📦 其他研究 | 2026年08月12日

> 本类共 **445** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-445](./part-09.md)

---

### 201. [A QUBO-Inspired Computational Framework for Airport Landside Bottleneck Diagnosis and Dynamic Dispatch Optimization](https://arxiv.org/abs/2608.08632)

**<font color=#1a73e8>作者：</font>** Wuming Lei, Xiaobin Li, Mingyan Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Airport landside traffic centers connect terminal arrivals with taxis, ride-hailing vehicles, private cars, buses, metro services, parking facilities, and terminal-area roadways. Peak arrivals can create coupled congestion across passenger queues, vehicle queues, pickup berths, storage areas, and access roads. This study proposes a QUBO-inspired computational framework for bottleneck diagnosis and dynamic dispatch in this setting. Shanghai Pudong International Airport and Hangzhou Xiaoshan International Airport serve as case airports. A five-minute state model links passenger arrivals, vehicle supply, pickup berth service, vehicle storage, and road capacity. Bottleneck diagnosis uses service intensity, road demand saturation, bottleneck frequency, queue severity, shadow-price leverage, and a composite congestion severity index. Two dispatch schemes are tested under consistent demand inputs: finite-action model predictive control and quadratic-unconstrained-binary-optimization-inspired simulated annealing. In the strong-peak baseline scenario, the QUBO-inspired method reduces the final passenger queue from 3445 to 2477 passengers at Shanghai Pudong and from 2053 to 1482 passengers at Hangzhou Xiaoshan. Case results indicate different dominant bottlenecks. Shanghai Pudong is more affected by road saturation, whereas Hangzhou Xiaoshan is more affected by pickup berth service. Robustness tests under demand, supply, service, road-capacity, modal-share, and random-noise perturbations show retained queue-reduction benefits under the tested uncertainty levels.

---


### 202. [Smart Compaction: Predicting Compaction Utility from Lakehouse Table Metadata](https://arxiv.org/abs/2608.08639)

**<font color=#1a73e8>作者：</font>** Jannic Cutura, Subash Prakash  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Open lakehouse table formats accumulate small data files over time, which degrades query performance. Deciding when compaction is worthwhile remains threshold-driven, but which metadata features actually determine compaction utility is not well understood. We present an open simulation framework that generates 2,376 Apache Iceberg tables spanning three orders of magnitude in file size, extracts 17 metadata features from manifest files without reading data, and trains XGBoost to predict the continuous file-reduction ratio (R2 = 0.998, RMSE= 0.013). The binary compaction decision turns out to be trivially separable by a single partition-level threshold max_files_per_partition> 4, requiring no learned model. Cross-schema validation on 96 TPC-H tables confirms generalisation without retraining (R2 = 0.976). A query benchmark reveals that compaction benefits metadata-heavy queries but can slow full-scan aggregations by reducing task parallelism. All code and data are publicly available.

---


### 203. [Whose Refusal Is It? The Unmeasured Contribution of Black-Box Multimodal Guardrails](https://arxiv.org/abs/2608.08641)

**<font color=#1a73e8>作者：</font>** Haoyu Zhang, Xiao Luo, Haowen Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A black-box guardrail is evaluated as though the safety number it earns were its own. It is not. A defended pipeline holds two components that can refuse (the guardrail, and the target model out of its own alignment), and every reported metric is a sum over both. We show that the guardrail's actual share of the safety credited to it runs from none of it to essentially all of it, decided by two variables no evaluation records: which channel carries the payload, and what text the harness places in the defense's internal read.
The split is recoverable at no extra cost, because a guard block replaces the model's response and the two counts are therefore disjoint. On a text guard across two open-weight targets: with the payload rendered as pixels the guard blocks nothing and the model produces every refusal the system makes; reading the encoded prompt the attacker actually sent, the guard produces a minority of the refusals attributed to it; reading the unencoded request behind the attack, it blocks almost everything and the model falls silent. The blindness is not inaccuracy: the same guards block no benign image inputs either, so their image-channel decision is a constant.
Granting the unencoded request inflates measured benefit substantially for a guard gate, less for a caption-mediated re-check, and not at all for a majority-vote smoother; the ordering reproduces in an independent replicate. Isolating the grant within one defense shows it does not improve detection: the harm-verdict stage contributes nothing, while the stage that regenerates the answer carries the effect. Nor is the inflated setting careless; the reference implementation builds every stage from a single prompt field that cannot distinguish what the attacker sent from what the benchmark records, so faithful porting supplies it silently. Previously published figures of our own are among those revised.

---


### 204. [Exact Rank-Space KL Projection for Shared-Marginal Low-Rank Factors: Application to Doubly Stochastic Clustering](https://arxiv.org/abs/2608.08642)

**<font color=#1a73e8>作者：</font>** Enliang Hu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study exact Kullback--Leibler (KL) projection for low-rank factorizations whose two nonnegative factors have prescribed row marginals and a shared, learned column marginal. For arbitrary positive row marginals of equal total mass, the joint KL projection reduces exactly to a strictly convex gauge-fixed dual with only $r-1$ effective variables; its Hessian is a sum of categorical covariance terms and admits $O((n+m)r)$ matrix-free Hessian--vector products. The projection theorem is objective-independent. We then specialize this geometry to doubly stochastic (DS) graph learning through $W=U\operatorname{Diag}(g)^{-1}V^\top$, where row-simplex factors with a common column mass induce an exactly DS graph without materializing an $n\times n$ optimization variable. Combined with observed-edge sparse fitting, a stochastic anchor-reduced manifold regularizer, and Bregman backtracking, the resulting mirror-descent method preserves exact feasibility at every accepted step. Under a nonvanishing latent-mass condition, it satisfies sufficient decrease and an $O(1/N)$ mirror-stationarity bound, while strictly positive accumulation points are KKT stationary. Matched clustering experiments show competitive accuracy, feasibility residuals near numerical precision, and favorable anytime behavior without a dense learned graph.

---


### 205. [Path-dependent Discrete Amortized Inference](https://arxiv.org/abs/2608.08644)

**<font color=#1a73e8>作者：</font>** Tiago da Silva, Esmeralda S. Whitammer, Salem Lahlou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider the problem of sampling compositional and discrete objects from a given unnormalized posterior distribution. Notably, recent studies have shown that this problem can be efficiently solved by learning a deterministic Markov Decision Process (MDP) that progressively builds each object in proportion to the posterior. In this work, however, we demonstrate that the Markovian assumption can both hamper signal propagation during training and catastrophically reduce the learned sampler's expressivity due to state aliasing. To address these issues, we propose lifting the MDP with a learnable latent dynamical system that allows the underlying policy to depend on the entire past trajectory---and not only on the current state. In view of this, we refer to the resulting method as path-dependent discrete amortized inference. Importantly, we provably extend existing learning algorithms for discrete amortized samplers to our setting. In experiments on standard benchmark problems, we also show that our approach often leads to faster learning convergence and improved state space exploration relatively to prior techniques.

---


### 206. [HaloMark: A Spectral Threshold for Embedding-Vector Watermarking under C2PA](https://arxiv.org/abs/2608.08645)

**<font color=#1a73e8>作者：</font>** Tarun Sharma  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Foundation-model embeddings are now a primary data asset, but the content-provenance machinery built for images and audio does not transfer to them. C2PA binds to an asset with a stable bit-level or perceptual identity; embeddings have neither, since quantisation, projection, fine-tuning, and windowed averaging reshape them in normal use and break any fixed hash.
We present HaloMark, a watermark for embedding vectors cryptographically bound to a C2PA manifest. It composes four standard primitives -- a block-diagonal orthogonal rotation, public whitening, an input-dependent LSH commitment, and a per-vector nonce -- around one protocol change: the producer signs the LSH commitment c into the C2PA sidecar, and the verifier reads c from the manifest instead of recomputing it. Recomputing is fragile under whitening, which flips the commitment bucket on 62% of inputs at cos = 0.96; reading the signed c reduces the verifier's score to T = T_null + beta(A)*epsilon, so security turns on a single scalar beta, which we bound rigorously for linear and non-adaptive attackers and characterise empirically for the adaptive case.
We evaluate against an adversary holding polynomially many clean/watermarked pairs under one key with full sidecar visibility, across eight baselines and ten adaptive attackers including denoising-autoencoder removal. The eleven encoders separate at an empirical threshold eff_rank(Sigma)/d ~= 0.19: above it, detection AUROC stays at 0.98 or higher across every in-budget attack on the three encoders we sweep in full, and at 0.965 or higher under single-seed DAE removal on the rest; below it every variant we tested fails. Why the threshold is dimension-uniform is left open. Deployed as a Qdrant admission filter, the verifier runs at 284 us and 24 bytes of sidecar per vector, validated end-to-end against three C2PA reference-SDK bindings.

---


### 207. [Multi-Relational Knowledge Graph Enhanced Embedding for Trajectory-User Linking](https://arxiv.org/abs/2608.08646)

**<font color=#1a73e8>作者：</font>** Zhifeng Chu, Bin Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Trajectory-User Linking (TUL) aims to identify the owner of an anonymous trajectory from a set of candidate users, providing a basis for user mobility analysis and personalized location-aware services. Existing methods often learn Point of Interest (POI), temporal, and semantic features independently, make limited use of structural knowledge shared across trajectories, and compress structural and sequential information before classification. To address these issues, we propose Multi-Relational Knowledge Graph Enhanced Embedding for Trajectory-User Linking (MakeTUL), which, to the best of our knowledge, is the first attempt to introduce knowledge graph representation learning into TUL. MakeTUL organizes visit-time, POI-category, and transfer-speed information as typed relations in a multi-relational mobility knowledge graph, allowing heterogeneous mobility semantics to jointly constrain the learned embeddings. The resulting POI representations are further enriched with high-order co-occurrence patterns extracted from the trajectory collection, providing structural prior knowledge for sparse and overlapping trajectories. By integrating these prior-enhanced representations with temporal, category, and transfer information, the trajectory sequence learning module captures ordered mobility patterns, while a dual-branch classification layer preserves and combines global structural evidence and sequential evidence at the decision level.

---


### 208. [Charting Public Health: A Taxonomic Study of Visualization Practices in the Public Health Field](https://arxiv.org/abs/2608.08657)

**<font color=#1a73e8>作者：</font>** Mia Hines, Alvitta Ottley  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Public health organizations regularly produce and publish data visualizations to raise awareness of critical issues, influence decision-making processes, and promote overall well-being. However, the design practices shaping these visualizations in real-world settings remain largely unexamined, limiting the research community's ability to evaluate their effectiveness, accessibility, and alignment with communication goals. To address this gap, we construct and analyze a large-scale corpus of over 4,000 real-world data visualizations drawn from more than two dozen websites associated with U.S. and international public health organizations. We evaluate salient design characteristics like chart type, visualization accessibility, use of embellishments like iconography, and design flaws. This work contributes to understanding real-world decisions in designing data visualizations and supports public health officials in improving data visualization-related communications. Visualizations in our finalized corpus and the labeled dataset can be found at this https URL.

---


### 209. [JSGS: JPEG State-Guided Supervision for 3D Gaussian Splatting from Mixed-Quality Views](https://arxiv.org/abs/2608.08659)

**<font color=#1a73e8>作者：</font>** Jinhua Cui, Anhong Wang, Kai Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Standard 3D Gaussian Splatting (3DGS) assumes that every input image faithfully samples scene radiance. However, mixed-quality JPEG images violate this assumption because compression-induced blocking and ringing artifacts can corrupt updates to Gaussians shared across views. To address this problem, we propose JPEG State-Guided Supervision for 3D Gaussian Splatting from Mixed-Quality Views (JSGS). JSGS uses luminance and chrominance quantization tables stored in each JPEG file to construct a view-specific JPEG observation operator. This operator encodes and decodes each rendered view for domain-matched comparison with the corresponding decoded input image. The luminance quantization table supplies continuous weights within a fixed middle frequency band. A loss in the low frequency band anchors coarse structure, while the weighted middle frequency loss redistributes supervision among the selected DCT coordinates. The resulting block disagreement also guides the Gaussian Controller to regularize small primitives with high opacity in disagreement regions. Across seven scenes and three mixed-quality schedules, JSGS achieves the lowest mean LPIPS and the highest mean SSIM under every schedule while rendering at approximately 150 FPS. Code: this https URL.

---


### 210. [Degradation-Guided Underwater Image Restoration with Task-Oriented Latent Control](https://arxiv.org/abs/2608.08661)

**<font color=#1a73e8>作者：</font>** Xu Zhang, Xuhui Cao, Kangzhe Yuan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Degradation information in underwater images plays a dual role: its spatial and spectral cues can guide adaptive restoration, while degradation-entangled features may be propagated without explicit regulation during decoding. Existing methods largely overlook this dual role, either underexploiting degradation cues or directly forwarding encoder features through skip connections. To address this issue, we propose PROTEUS, which couples degradation-guided feature adaptation with task?oriented latent control. PROTEUS tackles this problem from two complementary perspectives. At the feature level, the Guided Dynamic Feature Modulation Block exploits spatially varying degradation cues to adapt feature processing across network stages. At the representation level, the task-oriented latent controller learns a structured control code under discriminative regularisation and uses it for channel-wise modulation of skip features, without requiring the code to form a metrically cleaner embedding. Extensive experiments on five paired and four non-reference underwater benchmarks demonstrate that PROTEUS achieves highly competitive restoration performance, with a favourable balance between restoration quality and computational cost.

---


### 211. [FiRe: Fixed-Noise Refinement for Visual Counterfactual Explanations](https://arxiv.org/abs/2608.08664)

**<font color=#1a73e8>作者：</font>** Yan Zeng, Changlu Guo, Oskar Kristoffersen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual counterfactual explanations aim to change classifier decisions through realistic and localized edits while preserving decision-irrelevant content. Existing DDPM-based methods typically perform classifier-guided editing along a long reverse denoising trajectory. The changing noise levels make semantic editability and spatial control difficult to balance, and the editable state is noisy, whereas the target classifier is trained on clean images. As a result, these methods require either costly recursive denoising or low-quality one-step estimates to obtain classifier-facing clean images. We propose FiRe, a Fixed-noise Refinement framework for visual counterfactual explanations. Rather than following a reverse denoising trajectory, FiRe maps the input to a fixed noise level and iteratively refines the noisy state at that level. To provide clean images for classifier guidance, FiRe first adapts Pixel Mean Flow to visual counterfactual explanation, enabling direct clean-image prediction from noisy states. To make fixed-noise refinement produce minimal and localized counterfactual edits, FiRe introduces three FiRe-specific controls: a dynamic dual-mask strategy, adaptive guidance, and early stopping, which determine where edits accumulate, which changes become visible, and when refinement stops. Experiments on five tasks across three datasets show that, compared with the strongest recent baseline, FiRe achieves about 3$\times$ faster online inference and 8$\times$ fewer FLOPs while obtaining comparable or state-of-the-art counterfactual quality.

---


### 212. [FOX: Visual Exploration of Data Fact Outliers](https://arxiv.org/abs/2608.08671)

**<font color=#1a73e8>作者：</font>** Yikai Li, Yong Wang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Exploratory Data Analysis (EDA) systems extract and present data facts to summarize meaningful patterns such as trends and correlations for efficient dataset exploration. However, existing approaches rarely consider outlier detection at the level of data facts,and heterogeneous facts from different analytical scopes are often aggregated in a single view, making it difficult to define meaningful metrics and effectively analyze data fact outliers. To fill this gap, we present FOX, a novel visual analytics system for interactive data Fact Outlier eXploration. FOX organizes data facts into groups with consistent analytical scopes and computes a unified outlier score that combines distribution-based and pattern-based components. Its interface comprises an Upload Panel for data preparation and two coordinated exploration panels: the Overview Panel employs a matrix-based visualization to enable an intuitive overview of all data facts, and the Main Panel provides four linked views for cluster-level and fact-level analysis. We evaluated the usability and effectiveness of the system through two usage scenarios on public datasets and in-depth interviews with 12 participants. The results show that FOX enables meaningful detection, analysis, and explanation of data fact outliers.

---


### 213. [Catastrophic Forgetting in Continual Reinforcement Learning](https://arxiv.org/abs/2608.08673)

**<font color=#1a73e8>作者：</font>** Emma Graham  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work explores the relationship between task similarity and catastrophic forgetting in reinforcement learning. Catastrophic forgetting, the phenomenon in machine learning of losing the ability to effectively perform on previous tasks, is a significant impediment to continual learning. This study aims to understand the extent to which the similarity of a new task influences the performance on the previous task. Interpretable reinforcement learning, specifically Q-learning, is employed on graph-based tasks with the objective of minimising the number of steps to reach a goal. The study investigates the performance on a previously learned task after training on a new task, for tasks of varying relative levels of complexity. The experimental results reveal a complex dynamic between task similarity and forgetting, with significant fluctuations in forgetting severity observed across degrees of task similarities and task complexities, and are suggestive of an interdependence of forgetting on the similarity and complexity of tasks. The observations were accompanied by observations of high degrees of variability in forgetting and an uneven distribution of task similarity measures. The relationship between these variables remains unclear and no evidence of statistical significance that task similarity has an effect, independently, on forgetting is found in continual reinforcement learning. Further research is warranted to gain a comprehensive understanding of the potential interplay between task similarity and catastrophic forgetting.

---


### 214. [Backward Compatibility in Tree-Based Explanations and Enhanced CART Algorithm](https://arxiv.org/abs/2608.08674)

**<font color=#1a73e8>作者：</font>** Hirofumi Suzuki  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the operation of machine learning models, model update is a fundamental process that requires careful consideration of its impact on downstream decision-making. Particularly when operating explainable models, changes in explanations resulting from model updates can lead to detrimental outcomes for users. Decision trees, due to their high transparency, are frequently employed in risk-sensitive decision-making and serve as a prominent example in which the aforementioned issue is evident. However, existing research addressing similar issues has focused on explanations based on feature contributions, and thus cannot handle explanations derived from tree structures. Therefore, this paper proposes the Backward Compatibility Loss in Tree-based eXplanations (BCLTX), a loss metric that suppresses changes in decision tree explanations before and after updates. Furthermore, we design CART with Backward Compatibility in Tree-based eXplanations (CART-BCTX), a lightweight algorithm that improves upon CART for the decision tree update problem under BCLTX. Experimental results using 10 real-world datasets, including both classification and regression tasks, show that CART-BCTX achieves favorable trade-offs between prediction performances and BCLTX values, with comparable computation times to CART, regardless of the task.

---


### 215. [UniSpace: Unified Visual Representation and Scalable Multimodal Modeling](https://arxiv.org/abs/2608.08676)

**<font color=#1a73e8>作者：</font>** Jinbo Yan, Limeng Qiao, Jie Qin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic vision encoders have become a central visual interface for multimodal understanding and semantic conditioning in image generation. However, their final tokens discard fine-grained visual details, leading to poor pixel reconstruction and limiting their use in reconstruction-sensitive tasks such as image generation and editing. In this work, we ask whether understanding, generation, and editing can be modeled in a single visual representation space built from a pretrained semantic ViT. We show that the frozen Transformer blocks of a semantic ViT are not intrinsically unable to preserve visual details. Instead, the original patch parameterization drives the representation toward semantic abstraction, making fine-grained information difficult to recover from the final tokens. Based on this observation, we introduce \emph{Patch Reparameterization}, which preserves the original semantic pathway while adding a reconstruction-aware patch embedding that provides fine-grained visual information to the same frozen ViT blocks. The resulting unified representation preserves multimodal understanding while enabling high-fidelity image reconstruction and a favorable reconstruction--generation trade-off. We further scale this representation into \emph{UniSpace}, an 8B Mixture-of-Transformer-Experts model that performs understanding, generation, and editing in the same visual space without a separate VAE pathway. System-level evaluations demonstrate practical text-to-image generation and instruction-based image editing, showing that a reparameterized pretrained ViT can serve as a unified visual interface for scalable multimodal modeling.

---


### 216. [Semi-Dense Matching Uncertainty Is Not Just Local Confidence](https://arxiv.org/abs/2608.08685)

**<font color=#1a73e8>作者：</font>** Khoa Hoang, Hoang-Tuan Nguyen, Huong Ninh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable semi-dense matching is essential for modern geometric vision systems. Designed under a coarse-to-fine paradigm, it achieves an optimal balance between performance and computational cost. However, existing methods often struggle to provide well-quantified uncertainties, where catastrophic coarse-assignment failures are ignored, leading to truncated error distributions and severely misjudged geometric estimations. In this paper, we propose a lightweight, post-hoc overall uncertainty estimation framework that introduces a two-component calibrated Laplace mixture model with only 9 learnable parameters. The objective is to explicitly capture both the sharp local refinement noise and the broader tail of coarse-assignment failures. We introduce the Coarse-success posterior Refit (CoRe) method, a geometric refitting module that utilizes the posterior probability of coarse-assignment success as soft correspondence weights. Extensive experiments show that our method consistently improves downstream geometric accuracy across various pretrained-only matchers and robust estimators with minimal computational overhead. Our code is available at this https URL.

---


### 217. [A Structural Dynamics Graph World Model: Unified Modeling, Constrained Rollout, and Interpretable Calibration](https://arxiv.org/abs/2608.08689)

**<font color=#1a73e8>作者：</font>** Wei Wang, Yaosen Chen, Han Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The state evolution of a complex system arises jointly from object laws, relational propagation, domain conservation, and unmodeled error. Forcing all sources into one black box makes mechanism attribution and constraint preservation unauditable; forcing every mechanism into one equation family discards mature domain solvers. We propose SD-GWM, a Structural Dynamics Graph World Model as an executable structural contract: nodes declare self-dynamics S, edges declare neighbor graph-coupled dynamics N---both fixed-form mechanism assets (rules, ODEs, solvers) calibrating only authorized parameters. An optional bounded residual R concentrates learnability, while a global projection maps states to feasibility, enforcing constraints without guaranteeing accuracy gains. On eight pre-registered research questions, SD-GWM delivers (i) heterogeneous integration: rules and solvers plug in natively; (ii) semantic fidelity: disabling R preserves source semantics bit-for-bit, with four theory properties under explicit proof/empirical boundaries; (iii) auditable governance: stepwise traces enable counterfactual fault localization (top-1 = 1.0) without post-hoc approximations. On a semi-synthetic flood testbed and USGS streamflow, SD-GWM reduces constraint violations to floating-point tolerance in analytical tests and to zero in semi-synthetic and real-data cases. Persistence matches SD-GWM in calm periods, but during a 254-day extreme-flood shift persistence and all neural baselines collapse (90-min RMSE 892-3007 cfs) while SD-GWM holds at 108 cfs (8-28x gain). The bounded residual cuts RMSE ~50% only under backbone bias. We position SD-GWM not as a universally superior forecaster, but as a verifiable substrate for auditable, constraint-safe spatiotemporal mining.

---


### 218. [CUPA-T2*: Covariance-Aware Uncertainty Propagation and Alignment for T2* Mapping in Accelerated MRI](https://arxiv.org/abs/2608.08693)

**<font color=#1a73e8>作者：</font>** Gideon N. L. Rouwendaal, Natascha Niessen, Hannah Eichhorn 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Quantitative T2* maps have strong potential for biomarker discovery but are limited by long scan times, rendering them impractical in clinical settings. Significant acceleration can be achieved through undersampling in k-space combined with learning-based reconstruction. However, reconstruction artifacts and noise can propagate into downstream T2* fitting, degrading its accuracy. We introduce CUPA-T2*, a framework that explicitly propagates voxel-wise inter-echo uncertainty from stochastic Monte Carlo dropout reconstructions to downstream T2* fitting via covariance-aware sampling. T2* fitting is performed with a heteroscedastic MLP and a correlation-based regularizer that encourages alignment between predicted variance and reconstruction uncertainty. Experiments on accelerated brain MRI data show tissue-dependent behavior: CUPA-T2* achieves competitive overall T2* fitting performance and improves white-matter performance at higher accelerations. Compared with a heteroscedastic baseline, the proposed framework substantially increases alignment between reconstruction uncertainty and predicted T2* variance, while also revealing a trade-off with calibration (ECE) and selective prediction performance (AURC). CUPA-T2* enables reconstruction uncertainty-aware T2* fitting and delivers voxel-wise uncertainty maps to support the interpretation of quantitative T2* estimates.

---


### 219. [OccAnyScene: Towards Unified Indoor-Outdoor 3D Occupancy Predictio](https://arxiv.org/abs/2608.08696)

**<font color=#1a73e8>作者：</font>** Junjie Liu, Wanshui Gan, Zitong Dai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D occupancy prediction is fundamental to scene understanding, yet existing 3D semantic occupancy methods are typically specialized to fixed scene types and occupancy protocols. We introduce Cross-Scene 3D Semantic Occupancy Prediction, a new task setting which requires a single model to handle heterogeneous indoor and outdoor scenes with varying cameras, spatial ranges, voxel specifications, and semantic taxonomies. This setting poses a fundamental challenge: achieving metric-consistent yet scene-adaptive image-to-3D lifting across varying camera configurations and scene scales. To address this challenge, we propose OccAnyScene, a pixel-frustum-centered Gaussian framework built upon a pretrained depth foundation model. Specifically, the framework employs Pixel-Aligned Frustum Feature Aggregation to construct a camera-aware frustum query for each feature pixel, and Frustum-Parameterized Gaussian Construction to decode each query into multiple Gaussians whose positions and sizes are constrained by the predicted pixel depth and corresponding frustum geometry. OccAnyScene sets new state-of-the-art results, achieving 59.92% mIoU on the indoor Occ-ScanNet and 23.06% mIoU on the outdoor SurroundOcc-nuScenes.

---


### 220. [Loss-Resilient Wireless Video Token Communication over Block Fading Channels](https://arxiv.org/abs/2608.08698)

**<font color=#1a73e8>作者：</font>** Bingyan Xie, Yongjeong Oh, Zihan Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Video token communication represents video content as discrete tokens that differ in their importance to reconstruction and exhibit temporal dependencies. When these tokens are packetized for wireless transmission, block fading can cause multiple important or correlated tokens to be lost together, severely degrading video reconstruction. To address this issue, we propose a loss-resilient wireless video token communication (WVTC) framework. WVTC evaluates token importance from the intrinsic predictive structure of video tokens, assigning high priority to structural I-tokens and measuring P-token importance by temporal neighborhood novelty. A shuffled mixed I/P-token packetization scheme disperses structural anchors and correlated temporal regions across packets. Using only current block channel state information, an online scheduler jointly considers packet importance density, MCS-dependent decoding reliability, block capacity, and importance concentration when allocating packets to fading blocks. At the receiver, a fine-tuned detokenizer reconstructs missing content from surviving tokens without retransmission. Numerical results demonstrate improved perceptual quality and more graceful degradation under increasing packet error rates.

---


### 221. [SRE-FER: Regional residual evidence learning for mitigating local evidence dilution in fine-grained facial expression recognition](https://arxiv.org/abs/2608.08702)

**<font color=#1a73e8>作者：</font>** Jiaye Song, Ruochen Zhang, Yuliang Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained facial expression recognition (FER) hinges on capturing subtle muscular cues that distinguish adjacent emotions. Yet capturing these cues presents a dilemma. Detector-based methods depend on fragile landmark pipelines, whereas we find that directly transferring foundation models such as DINOv3 under conventional global readouts can cause local evidence dilution: early global aggregation washes out sparse muscular signals and leaves persistent confusion between categories such as fear/surprise and sad/neutral. To recover this evidence, we propose SRE-FER, a readout-level regional residual evidence learning framework. Its core module, RERA, adds zero-initialized residual logits that refine class boundaries while preserving the backbone's global prediction. Training-time action unit (AU) guidance steers regional features toward expression-relevant areas using Facial Action Coding System (FACS)-based anatomical priors, without requiring an external facial pipeline at inference. An optional Full setting further routes sample-specific non-redundant tokens. On three benchmarks, SRE-FER attains 92.76% on RAF-DB, 91.32% on FERPlus, and 67.78% on AffectNet-7, demonstrating highly competitive performance compared to existing FER methods.

---


### 222. [AI Evaluation Should Measure Verification Cost, Not Correctness Alone](https://arxiv.org/abs/2608.08709)

**<font color=#1a73e8>作者：</font>** Viviana Crescitelli, Generoso Immediato, Fabio Persia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The reliability of AI generative models is typically measured by output correctness, yet in practice it depends on the effort required to verify those outputs. We argue that current evaluation metrics overlook a critical failure mode: Verification-Cost Errors (VCEs), defined as incorrect input-output pairs that a declared fraction of the verifier population fails to identify within the verification budget available in a given deployment context. Unlike standard notions of "hallucination", VCEs are defined operationally, by the failure of correct identification within budget rather than by any property of the output itself. Plausibility and authoritative presentation are hypothesised contributors to that failure, not defining conditions. To capture this asymmetry, we introduce the notion of verification cost relative to a deployment budget as an operational dimension that current evaluation does not routinely capture. The quantity is presented as a conceptual instrument rather than a finalized metric. Evidence from code generation and multi-modal document understanding shows that high benchmark accuracy can mask significant verification effort in practice. We therefore take the position that correctness alone is insufficient as a measure of reliability. AI evaluation should explicitly account for verification cost, reflecting whether errors can be detected under realistic resource constraints.

---


### 223. [High-Quality Exposure Correction with Diffusion-Based Image Generation Priors](https://arxiv.org/abs/2608.08720)

**<font color=#1a73e8>作者：</font>** Ziwen Li, Meng Cao, Jinpu Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although most existing exposure correction methods achieve high fidelity, they often place excessive focus on overall pixel-wise accuracy, making it challenging to effectively model extreme exposure regions, which results in suboptimal perceptual quality. Recently, diffusion models have received significant attention due to their remarkable performance in the realm of image generation. However, their successful application to exposure correction remains a challenging and open question. The key challenge lies in generating accurate image structures and maintaining high image fidelity during stochastic diffusion processes. In this paper, we propose DPEC (Diffusion Prior-based Exposure Correction), a novel framework for image exposure correction that utilizes diffusion-based image generation priors encapsulated in pre-trained large-scale diffusion models. Specifically, we first propose an efficient fine-tuning strategy to derive an exposure corrector from pre-trained models, enabling the generation of enhanced images in a single-step denoising process. Moreover, we seamlessly combine the strengths of diffusion models and regression models, and design a joint cross-attention module to integrate multi-scale diffusion prior features, thereby effectively preserving high-frequency details and minimizing random artifacts. The diffusion model focuses on dealing with low-frequency content rather than all the intricate texture details. The experimental results demonstrate that the proposed DPEC method consistently outperforms existing state-of-the-art methods on multiple exposure correction datasets, whether in terms of fidelity, perceptual quality, or visual effects.

---


### 224. [From Scaffolding to Internalization: Enhancing CPR Training with In-Situ Visualization and Kinesthetic Feedback](https://arxiv.org/abs/2608.08729)

**<font color=#1a73e8>作者：</font>** Jiahe Dong, Shuhao Zhang, Yutao Ming 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> CPR training requires learners to not only understand explicit procedural targets, such as compression depth and rate, but also to internalize these targets as stable psychomotor skills. However, existing CPR training systems often rely on feedback presented outside the action space, which divides learners' attention between performing compressions and monitoring external guidance. This separation weakens the coupling between action and bodily sensation and may lead to an over-reliance on external feedback, compromising skill retention once support is removed. To address this challenge, we conducted a formative study with novice trainees and certified BLS instructors, from which we derived three design goals: embedding feedback within the task space, providing active kinesthetic guidance, and gradually fading assistance based on learning phases. Informed by these insights, we designed Kinesthetic-CPR, a stage-adaptive multimodal mixed reality CPR training system, and evaluated it in a controlled user study across two sub-studies (N = 60). This work offers design implications for CPR training systems that aim to better support skill retention.

---


### 225. [IDATA: Scalable Invertible Diffusion for Unrestricted Adversarial Transfer Attack](https://arxiv.org/abs/2608.08734)

**<font color=#1a73e8>作者：</font>** Yi Pan, Jun-Jie Huang, Tianrui Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unrestricted adversarial transfer attacks are important for evaluating the black-box robustness of deep visual models. Diffusion-based attacks have shown promising transferability and visual imperceptibility by optimizing adversarial perturbations along denoising trajectories in latent space. However, existing methods are limited by two challenges: memory-intensive multistep backpropagation and frequency-agnostic perturbation over intermediate latents. To address these issues, we propose IDATA, a memory-efficient diffusion framework for unrestricted adversarial transfer attack. IDATA consists of two key components: an Invertible Diffusion Module (IDM) and a Low-Frequency Constraint Module (LFCM). Specifically, IDM reformulates adversarial optimization over diffusion trajectories as an invertible process, enabling constant-memory backpropagation through on-demand reconstruction of intermediate states instead of storing the full denoising chain. Moreover, LFCM leverages Discrete Wavelet Transform (DWT) to decompose latent variables into low- and high-frequency components, restricting perturbations to semantically stable low-frequency subspaces, thereby improving transferability while preserving visual imperceptibility. Extensive experiments on multiple benchmarks and diverse model architectures demonstrate that IDATA consistently outperforms state-of-the-art baselines in attack success rate, memory efficiency, and visual imperceptibility. These results suggest that IDATA is a promising tool for black-box robustness evaluation of deep visual models. Code is available at this https URL.

---


### 226. [Memory-Efficient Activation Checkpointing with Sliding Window and Hirschberg's Algorithm for 0/1 Knapsack Solving in PyTorch](https://arxiv.org/abs/2608.08740)

**<font color=#1a73e8>作者：</font>** Jędrzej Maczan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation checkpointing minimizes the runtime of neural networks under a given memory budget, by selecting which intermediate tensors to store and which to recompute. PyTorch solves this as a 0/1 knapsack problem, where operations from a joint forward-backward computation graph are items with a memory cost (weight) and a runtime saving (value). The default solver, dp_knapsack, allocates a full dynamic programming (DP) table of shape $(n+1) \times (W+1)$, where $n$ is the number of operations and $W$ is the quantized memory budget. This method is resource-hungry and crashes at $n = 100$ items on a machine with 64 GB RAM.
In this paper, we introduce dp_knapsack_sliding_hirschberg, which combines the sliding window trick and Hirschberg's algorithm to reduce peak memory from $O(nW)$ to $O(W)$ while preserving the exact optimal solution. Our experiments show successful knapsack execution at $n = 2000$, where dp_knapsack fails at $n = 100$, a 20$\times$ increase in computable problem size. In addition, our benchmarks show a consistent 25-28\% runtime speedup over dp_knapsack.
The implementation is merged into PyTorch and released in version 2.10.

---


### 227. [Parcel2Progression: An Anatomy-aware Longitudinal Framework for Alzheimer's Disease Diagnosis](https://arxiv.org/abs/2608.08753)

**<font color=#1a73e8>作者：</font>** Madhumitha Venkatesh, Shanawaj S Madarkar, Konda Reddy Mopuri  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Alzheimer's disease (AD) progression is a longitudinal process with subtle pathological cues in the early stages. Yet, computational constraints have limited most neuroimaging models to either compromise spatial information or limit the number of longitudinal scans. We aim to overcome this bottleneck and fully leverage high-resolution, variable-length T1w structural MRI (4D sMRI) scan sequences. We introduce Parcel2Progression (P2P), a Longitudinal Transformer Framework which tackles this challenge using an Atlas-guided Parcel Encoder that tokenizes 3D scans into a set of richer anatomically grounded representations. A Longitudinal Transformer then integrates irregular, arbitrary-length longitudinal visits with patient age. This synergy delivers two key advantages: (1) parcel-specific interpretability, and (2) computational tractability for long-term analysis, which scales linearly with the number of scans compared to a naive quadratic 4D ViT cost. P2P outperforms prior works and baselines in both MCI (Mild Cognitive Impairment) to AD conversion prediction and AD vs. CN (Cognitively Normal) classification tasks across ADNI, AIBL, and MIRIAD datasets. Leveraging longitudinal scans boosts performance over single-scan baselines by up to 5% and 7% in balanced accuracy for AD classification and MCI conversion prediction tasks, respectively. Interpretability analysis using parcel saliencies and attention rollouts reveals clinically consistent atrophy patterns in AD and MCI subjects. We also demonstrate the frameworks' reliability in anomaly detection using a synthetic dataset, and test the model's generalizability for other neurodegenerative diseases like Frontotemporal Dementia.

---


### 228. [UPolarSQ: Polar Representation Learning for Optic Disc and Peripapillary Atrophy Segmentation and Quantification in Fundus Photographs](https://arxiv.org/abs/2608.08771)

**<font color=#1a73e8>作者：</font>** Mengxian He, Yunyun sun, Ziyue Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Myopia-induced posterior-pole remodeling is frequently accompanied by Optic Disc (OD) deformation and Peripapillary Atrophy (PPA), both of which provide clinically relevant structural biomarkers. In Cartesian fundus images, however, PPA often appears as an irregular and partially visible crescent adjacent to the OD, leading to fragmented segmentation and post-processing-dependent quantification. We propose UPolarSQ, a unified polar-domain framework for OD/PPA segmentation and biomarker quantification in myopic fundus images. UPolarSQ first maps an OD-centered region of interest into polar coordinates, where OD and PPA boundaries can be represented as radial profiles. It then employs UPolarSeg, a U-Net-based segmentation network enhanced with a Radial-Angular-Decoupled Module and boundary-aware auxiliary supervision to model anisotropic polar features and radial boundary transitions. Clinical biomarkers, including disc shape and PPA-width-related measurements, are deterministically extracted from the predicted polar masks, aligning segmentation and quantification within a shared geometric representation. Experiments on internal and external cohorts demonstrate that UPolarSQ improves OD/PPA segmentation and supports reliable polar-native biomarker estimation for myopic analysis.

---


### 229. [OmnilingualGAIA2: Evaluating the Multilingual Gap in Frontier AI Agents](https://arxiv.org/abs/2608.08775)

**<font color=#1a73e8>作者：</font>** Andrea Caciolai, Pere-Lluís Huguet Cabot, Chierh Cheng 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agentic benchmarks aim to measure how well AI agents plan, search, execute, and recover within realistic multi-tool environments, but they are almost exclusively in English. As AI agents are globally deployed to a linguistically diverse user base, whether agentic competence measured in English transfers to other languages remains an open question. We introduce OmnilingualGAIA2, a machine-translated expansion (with partial human- expert validation) of the GAIA2 agentic benchmark, covering ten target languages spanning five writing systems, paired with a localised and human-calibrated multilingual verifier. Evaluating seven frontier and open-weight agents, we find a universal cross-lingual gap of 8.8-18.4 pass@3 points that is agent-asymmetric in magnitude, concentrates on tool-orchestration rather than quantitative reasoning, and does not close with model scale. A stratified error attribution decomposes the gap as predominantly model-driven (55%), with a bounded translation-contamination floor of only 6.4% of scenario-language pairs. Human-expert linguistic analysis further identifies morphological cue loss and amplified ambiguity as the primary failure mechanisms in non-Latin-script languages. Our results argue that multilingual agentic evaluation must become a standard part of the reporting protocol for globally deployed agents.

---


### 230. [Quantum-Classical Physics-Informed Kolmogorov-Arnold Networks for Solving Fuzzy Differential Equations](https://arxiv.org/abs/2608.08782)

**<font color=#1a73e8>作者：</font>** Xiang Rao, Yuxuan Shen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this study, we propose a quantum-classical physics-informed Kolmogorov-Arnold network (QCPIKAN) dedicated to the solution of fuzzy differential equations. The network takes the spatiotemporal coordinates and membership level as joint inputs and employs ChebyKAN modules and a parameterized quantum circuit to construct a hybrid function approximator. It simultaneously approximates the lower and upper endpoint functions associated with the {\alpha}-cuts and incorporates the governing equations, initial-boundary conditions, and fuzzy-structural constraints into the training objective. Theoretically, a unified error-analysis framework is established for QCPIKAN and PIKAN, in which the endpoint-solution error is decomposed into approximation, sampling, optimization, and fuzzy-structure constraint errors. Under the assumptions of well-posedness and residual stability, it is proved that QCPIKAN has a smaller a priori error bound when the representational gain introduced by quantum entanglement features exceeds the additional computational error. Numerical experiments are conducted for elliptic, parabolic, and hyperbolic equations in an ideal quantum-simulation environment. The results show that QCPIKAN captures the overall contraction of the solution interval as increases. At most tested membership levels, the mean relative L2 error of PIKAN is approximately 1.1-2.7 times that of QCPIKAN. In the fuzzy convection example, the mean wavefront-position error of PIKAN is approximately 1.77 times that of QCPIKAN. Nevertheless, both models still exhibit local fuzzy-structure violations near boundaries, in high-gradient regions, and around the wavefront. These results indicate that QCPIKAN provides a quantum-classical hybrid physics-informed computational framework with comparatively high predictive accuracy for solving fuzzy partial differential equations represented by {\alpha}-cuts.

---


### 231. [Three Generations of Healthcare IT: From the Digital Record to the Computable Care Process](https://arxiv.org/abs/2608.08806)

**<font color=#1a73e8>作者：</font>** Alexander Apartsin, Yehudit Aperstein  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Objective. Healthcare IT is usually organized by the technologies it adopts. We instead organize it by the unit of information a system makes computable, and describe a computational layer whose object is patient-specific clinical intent. Approach. We give criteria for a computational layer, derive three (record, clinical state, and a proposed layer of intent), and formalize the Actionable Clinical Record (ACR) as the atomic object of the third layer. Discussion. The framework distinguishes prescribed, observed, and intended process; existing standards represent intent once it is structured but do not recover it from natural communication, the capability we localize. The ACR is complementary to FHIR workflow resources, guidelines, and process mining; a companion feasibility study illustrates tractability for one narrow subproblem. Conclusion. Computable clinical intent is a coherent research direction; the ACR, its readiness ladder, and an executable-correctness evaluation framework are reusable constructs for subsequent work to extend, evaluate, or falsify.

---


### 232. [Tevatron-Elastic: A Unified Abstraction for Training Elastic Retrievers and Rerankers](https://arxiv.org/abs/2608.08809)

**<font color=#1a73e8>作者：</font>** Yu Wang, Shengyao Zhuang, Xueguang Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A single model scale challenges the flexibility of a production retrieval system: some settings need it faster, others need a smaller index, and the right trade-off changes with the workload. In the context of information retrieval (IR), a transformer-based model can be made smaller in three ways---using fewer layers, passing fewer tokens through the upper layers, or producing a shorter embedding---and each way saves a different compute resource. These options have been studied one at a time, each as its own method with its own code and training setup, which makes them hard to combine or adapt to a new model. We present~\ours to bring all three under one simple abstraction: a single object names any size the model can run at, and a short schedule lists the sizes to train. Training then produces one checkpoint that serves all of those sizes, and at deployment the user picks any of them. The same abstraction covers both retrievers and rerankers and both encoder and decoder models, as it works through interfaces that Hugging Face transformers already expose; a new backbone is a configuration change, not new modeling code. Prior methods---Matryoshka embeddings, early exit, 2D~Matryoshka (e.g., Starbucks), and layerwise token compression---become special cases of our unified abstraction. The same interface also enables Matryoshka~LTC (MLTC), which jointly trains several token-compression ratios in one retriever checkpoint. To validate our framework, we train 20 checkpoints across three backbones and two tasks: the quality curves are smooth, one checkpoint costs little over a model trained for a single size, and a controlled study confirms the wallclock speedups. We release the framework and all checkpoints as a resource for building elastic retrieval systems.

---


### 233. [MRI super-resolution in ten sampling steps using a diffusion bridge model](https://arxiv.org/abs/2608.08819)

**<font color=#1a73e8>作者：</font>** Mojtaba Safari, Hang Yu, Zach Eidex 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Objective. MRI provides excellent soft-tissue contrast, but long acquisition times can cause patient discomfort and lead to motion artifacts, forcing a trade-off between spatial resolution and scan time. Diffusion-based super-resolution (SR) reconstructs high-resolution (HR) images from low-resolution (LR) inputs, but typically needs many sampling steps and initializes from a Gaussian prior ill-suited to image restoration. We developed an efficient diffusion framework that reconstructs HR MRI directly from LR data. Approach. We propose super-resolution diffusion bridge model (SR-DBM), a super-resolution diffusion bridge model that casts SR as a stochastic transport between the LR and HR image distributions. Through a Doob's h-transform of a mean-reverting stochastic differential equation, SR-DBM pins the process to the paired HR and LR images at its endpoints, initializing reconstruction from the measured anatomy rather than from Gaussian noise. The HR image is recovered by a deterministic reverse trajectory in which a network predicts the clean image at each of only ten sampling steps. We evaluated SR-DBM on ultra-high-field 7T brain T1 MP2RAGE maps and pelvic T2-weighted prostate images against nine comparison methods using PSNR, SSIM, GMSD, and LPIPS. Main results. SR-DBM attained the highest PSNR and SSIM and the lowest GMSD on both datasets (brain: 27.66+-1.52 dB, 0.96+-0.02, 7.96+-1.86$; prostate: 27.87+-2.29 dB, 0.80+-0.05, 8.38+- 1.44), with statistically significant gains over every comparison method (two-sided Wilcoxon signed-rank test with Holm correction, p<0.05). The strongest baseline, SR-EMamba, ranked second. Qualitatively, SR-DBM produced the smallest residual errors and best preserved fine structures and lesions.

---


### 234. [LogiShot: Logically Coherent Cross-Shot Video Generation](https://arxiv.org/abs/2608.08820)

**<font color=#1a73e8>作者：</font>** Shuai Guo, Yuhang Yang, Zeyu Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating cross-shot videos that are logically connected is essential for content creation. Currently, most cross-shot video-generation workflows, such as short-drama production, still rely on isolated textual scripts or explicit reference images to specify the generated content. Consequently, when user instructions are underspecified or ambiguous, a generated clip may appear visually plausible on its own but fail to align with the overall narrative, leading to disjointed content. We argue that achieving cross-shot logical coherence in video generation requires establishing logical connections across shots and maintaining visual consistency. To this end, we propose LogiShot, which incorporates information through two complementary paths: 1) LogiShot jointly encodes the context video and other conditioning signals, yielding dense multimodal cues that provide visual-semantic evidence for cross-shot generation; 2) the model maintains a visual memory of the context video throughout generation to preserve visual consistency across shots. Additionally, we construct a dataset with 110K samples and a dedicated benchmark for evaluating cross-shot logical coherence. Experiments demonstrate that LogiShot consistently outperforms existing baselines in terms of logical coherence across multiple shots. Model and data will be made publicly available.

---


### 235. [The Cost of Adaptivity: Matching Lower Bounds Across Learning Problems](https://arxiv.org/abs/2608.08826)

**<font color=#1a73e8>作者：</font>** Ibne Farabi Shihab, Adria Binte Habib  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptive procedures must work without nuisance information an oracle may use, such as a gradient scale or smoothness index, and robust procedures may have to answer queries whose coordinate and inspection time are chosen only after the data are seen. Such comparisons are meaningful only when the oracle advantage and validity contract are stated explicitly. We formalize nuisance adaptation via a slice-normalized minimax ratio retaining the worst-case instance within each nuisance slice, and separately define the robustness cost of expanding from one preannounced Gaussian query to arbitrary post-hoc inspection. Our main result is a finite-horizon composition law for Gaussian certification: from M independent coordinates, a familywise certifier protecting every coordinate and time up to T pays optimal normalized squared half-width of order log(eM) + log log(e^eT), within the sample-mean-centered rectangular class. Epoch stitching gives the upper bound; independent Gaussian block increments across coordinates and geometric time scales give a matching lower bound, already holding on a geometric checkpoint grid, forcing quantiles of the realized maximum width so selection and stopping taxes add. Two benchmark regimes complete the picture: unknown gradient scale in online convex optimization has constant cost, while pointwise adaptation over nested Holder classes costs order (log n / log log n)^(s1/(2s1+1)). Cast as model monitoring, the law lets an analyst inspect any of M slice metrics at any data-dependent time: the naive fixed-query band's selected coverage degrades sharply, to 0.30 at M=1 and to zero for M>=10, while the epoch-stitched certifier holds familywise coverage at an additive iterated-logarithm width cost. Experiments put both sharp predictions at risk of refutation; both survive.

---


### 236. [Treating Statewide CORS Networks as Spatially Distributed Sensors for GNSS Integrity Monitoring under Unintentional and Deliberate Threats](https://arxiv.org/abs/2608.08831)

**<font color=#1a73e8>作者：</font>** Minhaj Uddin Ahmad, Sagar Dasgupta, Muhammad Sami Irfan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> State departments of transportation (DOTs) in the United States increasingly rely on statewide continuously operating reference station (CORS) networks to support high-precision Global Navigation Satellite System (GNSS)-based positioning and timing for intelligent transportation systems. These networks also provide continuous observations that can support regional GNSS integrity monitoring. This study develops and demonstrates a framework that treats a statewide CORS network as a spatially distributed sensor system for identifying unintentional (environmental) and intentional (cyber) interference when GNSS measurements deviate from expected spatial patterns. We develop a graph-based Network Consistency Framework (NCF) that evaluates each station against its spatial neighborhood using four metrics: neighborhood residual, spatial gradient, residual, and graph smoothness. These metrics are combined into a Network Consistency Index (NCI). The framework is demonstrated using two consecutive days of four-constellation observations from 50 stations in the Alabama DOT-maintained CORS network, using changes in vertical total electron content ({\Delta}VTEC) and the Rate of TEC Index (ROTI) as spatially coherent observables. The framework quantified network-wide spatial consistency and identified localized anomalies. Detected anomalies indicate stations whose observations deviated from the surrounding regional network, signaling potential integrity issues. Determining whether anomalies result from receiver faults, localized interference, spoofing, or other causes requires further investigation. This study introduces statewide CORS networks as regional GNSS integrity observatories and presents the NCF and NCI for graph-based spatial integrity monitoring. Transportation agencies can implement the framework using existing CORS observations to monitor network integrity and identify localized anomalies.

---


### 237. [Visual Token Codec: Unleashing Spatial Redundancy for ViT Feature Coding](https://arxiv.org/abs/2608.08832)

**<font color=#1a73e8>作者：</font>** Donghui Feng, Fengxi Zhang, Changsheng Gao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Distributed deployment of large vision foundation models often partitions a ViT backbone and exchanges intermediate token features between computing nodes, making efficient feature compression critical under bandwidth and computation constraints. Existing ViT feature codecs typically flatten heterogeneous global and patch tokens into an L x C pseudo image, causing entropy models to mainly capture sequence-axis dependencies while overlooking the native two-dimensional patch-grid structure. In this paper, we show that ViT patch tokens retain strong local spatial correlations on the original grid. To exploit this structural prior, we propose the Visual Token Codec (VTC), a dual-path learned codec that separates global and patch tokens into dedicated coding paths. Global tokens are compressed with a lightweight factorized prior, whereas patch tokens are encoded on the patch-token grid using a spatial-channel context entropy model. To support intermediate-layer compression and practical rate adaptation, VTC further incorporates feature-matching supervision after subsequent ViT blocks and variable-rate modules within a single codec. Experiments on DINOv2 and SAM3 show that VTC consistently outperforms representative ViT feature coding baselines on classification, segmentation, and detection tasks. At 90% of uncompressed-feature performance, VTC reduces bitrate by 15.7x-37.4x across these tasks. We further provide intermediate-layer rate-utility analyses for practical transmission- and storage-oriented deployment scenarios.

---


### 238. [SLAP: Selective Local Vision-Language Alignment for Fish Re-Identification via Partial Optimal Transport](https://arxiv.org/abs/2608.08840)

**<font color=#1a73e8>作者：</font>** Cigdem Beyan, Tonje Knutsen Sordalen, Kim Tallaksen Halvorsen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Individual fish re-identification (ReID) is a fine-grained recognition problem in which identity-discriminative cues are often localized to specific body regions rather than distributed uniformly across the animal. Nevertheless, recent CLIP-based ReID methods rely predominantly on global image-text alignment, allowing background and weakly discriminative regions to contribute to cross-modal supervision. We propose a selective local vision-language alignment framework that establishes localized correspondences between visual patch embeddings and multiple identity-aware prompt embeddings through Partial Optimal Transport (POT). Rather than enforcing exhaustive correspondence, POT enables selective matching between visual patches and prompt embeddings, allowing the model to emphasize the strongest cross-modal correspondences while avoiding forced alignment of weakly matching regions, thereby yielding more discriminative visual representations for retrieval. The framework is trained end-to-end, while only the adapted visual encoder is retained during inference. Experiments on the longitudinal Symphodus melops dataset demonstrate consistent improvements over recent CLIP-based ReID methods under both closed-set and open-set evaluation protocols. Additional evaluations on other datasets further demonstrate the generalization capability of the proposed method across diverse marine ReID benchmarks.

---


### 239. [Explicit Boundary Markers for Subword Vocabularies](https://arxiv.org/abs/2608.08847)

**<font color=#1a73e8>作者：</font>** Sander Land, Clara Meister  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Subword tokenizers represent many common words twice in space-using writing systems, once with a leading space and once without. The two entries have separate embeddings in models, so occurrences of one word are divided across rows that are trained independently, and the two forms need not even segment the string the same way: " together" may be a single entry while the same word without a preceding space is tokenized as "to|gether". Capitalization divides a word further, into as many as six forms. We introduce an alternative to standard whitespace conventions using an explicit word boundary marker, which prevents such duplication. Words are delimited by the boundary markers, and spaces between words are represented as pairs of such markers. Two shift codes do the same for title case and upper case, allowing one internal representation of a word to be re-used across different settings. Switching to this convention mitigates the duplicate-entry issue, but does not improve tokenization compression: for both vocabulary-learning algorithms, the best marker scheme stays within one percent of the baseline in characters per token, averaged across six languages. It does result in better language modeling performance. Every marker scheme tested downstream reaches lower bits per byte than the baseline, suggesting that duplication carries a cost that compression does not capture.

---


### 240. [Wearing Trust: How Older Adults Calibrate Reliance on Health Wearables Through Bodily Experience and Everyday Use](https://arxiv.org/abs/2608.08856)

**<font color=#1a73e8>作者：</font>** Yibo Meng, Bingyi Liu, ZhiMing Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Older adults increasingly use health wearables, yet often cannot inspect the properties that matter for reliance. Through 31 semi-structured interviews in China, we examined how participants judged whether wearable outputs were reliable enough for everyday use. Participants relied on brand and price, visible interface activity, lived interaction experience, and comparison with bodily sensation. These cues supported conditional trust, but did not reveal sensor validity, data continuity, or failure conditions. We describe this mismatch as an observability gap and outline design directions for showing signal quality, reliability by context, human-system fit, and alert provenance.

---


### 241. [Agentic Anomaly Detection with ORCA-Style Dynamic Inductive Bias Adaptation in Multimodal Wearable Time Series Data](https://arxiv.org/abs/2608.08859)

**<font color=#1a73e8>作者：</font>** Anushka Roy, Jyotirmoy Singh, Shreea Bose 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wireless Body Area Networks (WBANs) generate multivariate physiological time series that are highly nonstationary and must often be processed under strict computational and memory constraints. A critical yet underexplored challenge in this setting is selecting an appropriate temporal receptive field, which serves as a strong inductive bias for anomaly detection models. Existing approaches typically rely on fixed temporal contexts, which can perform inconsistently across heterogeneous signal regimes and require dataset-specific tuning. We propose ORCA, an agentically controlled anomaly detection framework that dynamically adapts the temporal receptive field at inference time based on lightweight signal statistics. Rather than introducing additional trainable parameters or learned policies, ORCA employs a supervisory controller that autonomously selects among discrete temporal contexts, enabling state-dependent inductive bias adaptation without retraining. Across a custom WBAN dataset, ORCA achieves performance comparable to the strongest fixed-context baselines (AUROC = 0.99) while eliminating the need to tune temporal horizons in advance. We further evaluate ORCA on MIMIC-IV as a challenging out-of-distribution benchmark, observing conservative generalization behavior without performance collapse under heterogeneous clinical conditions. These results highlight adaptive temporal inductive bias control as a practical and robust design principle for anomaly detection in resource-constrained, nonstationary physiological time series.

---


### 242. [Beyond Best Response: Quantal Stackelberg Deception as Insurance Against Attacker Misspecification](https://arxiv.org/abs/2608.08865)

**<font color=#1a73e8>作者：</font>** Asif Rahman, Md. Abu Sayed, Ahmed Ann Noor Ryen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Stackelberg Security Games (SSG) assume that an attacker observes the defender's strategy and chooses the target that maximizes their expected utility perfectly. In most realistic applications this is not plausible, and in the case of cyber deception (e.g., using decoys) the purpose of the game is to induce uncertainty and mistakes. Quantal response is a common way to represent noise and mistakes in decision-making; here it replaces perfect best-response with a logit choice with rationality parameter $\lambda$ and results in a generalized Quantal Stackelberg Equilibrium (QSE), which recovers the classical solution exactly as $\lambda \rightarrow \infty$. We conduct a deeper analysis of how QSE can function as a generalized form of insurance against a variety of forms of model specification error/uncertainty; our analysis shows that QSE provides a practical way to address the important role of tie-breaking rules and model uncertainty in SSG from both a theoretical and practical perspective. We conduct an empirical evaluation in a cybersecurity case study with two networks and real vulnerabilities drawn from CVE and scored using the Common Vulnerability Scoring System (CVSS). QSE beats Stackelberg in realized defender utility spanning 144 scenarios with specification errors and 25 parameter configurations, with gains of 46\% to 175\% showing a substantial advantage in a wide variety of realistic cases.

---


### 243. [Approximation Rates for Metaplectic Neural Networks](https://arxiv.org/abs/2608.08872)

**<font color=#1a73e8>作者：</font>** Ahmed Abdeljawad, Marcello Carioni, Elena Cordero  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper we develop quantitative approximation results for shallow neural networks constructed using a dictionary based on metaplectic operators. First, we extend the concept of Barron spaces by considering a symplectically motivated extension of the Fourier transform, known as the metaplectic transform. Then, after establishing embedding between metaplectic Barron spaces and Sobolev spaces we consider a neural metaplectic dictionary and we prove Monte-Carlo approximation bounds for metaplectic Barron functions using finite linear combinations of atoms of the dictionary. Finally, we validate the introduction of the neural metaplectic dictionary by devising a deep neural network architecture that uses as building blocks the atoms of the dictionary. We test it to approximate solutions of time-dependent Schrödinger equations, demonstrating better performance compared to classical phyisics informed neural networks architectures.

---


### 244. [Sparse Attention to Emotion: Efficient Facial Emotion Recognition via Token Reduction](https://arxiv.org/abs/2608.08873)

**<font color=#1a73e8>作者：</font>** Aya Manel Zitouni, Aicha Zenakhri, Karim Haroun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Facial Emotion Recognition (FER) is an important task that has significant implications across various fields such as biometrics, health, and human-computer interaction. Current Vision Transformer-based approaches display quadratic complexity $\mathcal{O}(N^2)$, with N being the input sequence length, making them cumbersome to deploy at the edge. In this paper, we hypothesize that the FER task does not necessarily require all facial information to correctly interpret emotional states, as specific regions such as the eyes, the mouth, and parts of the cheeks carry discriminative information that can be sufficient to recognize emotions. Based on this, we propose Sparse Attention to Emotion (SAE), a model that discards image tokens that have no added value to the emotional context, while preserving good accuracy and achieving a significant gain in computational cost. Surprisingly, even after suppressing 90\% of the image tokens, our model achieves competitive accuracy to state of the art methods at much lower cost, providing a lightweight Facial Emotion Recognition approach. Experimental results demonstrate that SAE achieves new state of the art results on the RAF-DB dataset while reducing the computational complexity by up to 90\%.

---


### 245. [AeroReformer2: Spoken-Query Referring Segmentation for Aerial Images](https://arxiv.org/abs/2608.08874)

**<font color=#1a73e8>作者：</font>** Rui Li, Chenxi Duan, Haoyang Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spoken language offers a natural, hands-free interface for specifying an arbitrary target in dense remote-sensing imagery, yet existing referring remote-sensing image segmentation benchmarks accept only written expressions. To bridge this gap, we introduce \dataset, a spoken-query benchmark derived from RISBench that adds accent- and voice-diverse speech while preserving the original image, mask, and data splits. Its hard evaluation sets combine rotor, wind, and mixed interference with three signal-to-noise levels. We also propose \model, an efficient bilateral network that combines a boundary-preserving visual path with token-preserving speech encoding, kernel linear cross-modal attention, and a resolution refinement head. The design conditions visual features at two scales without materializing a dense speech--visual affinity matrix, then restores fine boundaries using high-resolution visual features. On the clean test split, \model with Swin-Base achieves 62.09\% mean intersection over union (mIoU) and 68.22\% overall intersection over union (oIoU), outperforming the strongest audio-adapted remote-sensing baseline by 5.38 and 2.08 percentage points, respectively. It retains the best hard-set mIoU at 54.09\%. To the best of our knowledge, this is the first benchmark and model study of full-sentence spoken-query referring segmentation for remote-sensing imagery. The code will be made publicly available.

---


### 246. [Inductive Graph Layout with Implicit Neural Fields](https://arxiv.org/abs/2608.08876)

**<font color=#1a73e8>作者：</font>** Berfin Inal, Daniel Probst  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> A graph layout is normally a table of $N$ free coordinates. We optimise a function with a fixed number of parameters instead. This gives a drawing a sample complexity and an extensible domain. Force-directed algorithms remain the standard tools for graph drawing. The most accurate among them minimise stress in the Kamada-Kawai formulation by directly optimising the node coordinates, at a full objective cost of $O(N^2)$ in time and space. Here, we propose Fling (Field Layout via Implicit Neural Geometry), a small neural network mapping the distances of each node to a set of landmarks, positioning it in the plane by training on the layout energy. The full spring system then becomes tractable without its distance matrix, as rest lengths follow from a landmark bound in constant time per pair while a second network learns the majorisation sums from exact anchor rows, at $O(|\mathcal{A}|N)$ per step for $|\mathcal{A}|\ll N$ anchors. Unlike neural drawers that read the graph by message passing, we represent the drawing as a function of node features. An unseen node costs one forward pass, where sparse and low-rank majorisation remain transductive. As the unknowns are weights rather than coordinates, the energy only requires a small fraction of the nodes, and a field fitted that way outperforms PivotMDS, landmark MDS, and a kernel ridge trained on the same energy and features, when the task is fitting the energy of a graph from a sample of its nodes. In addition, the same parameterisation enables a stochastic pivot stress variant, an aesthetics-optimised variant carrying a neighbour-embedding energy with node-edge clearance and crossing terms on the same field, and conditioning on the weight between two energies gives a whole layout family from one run.

---


### 247. [Epistemic Transfer in AI-Assisted Verification: A Framework and Evaluation Protocol](https://arxiv.org/abs/2608.08882)

**<font color=#1a73e8>作者：</font>** Christoph Trattner  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI tools that help people judge online claims are usually evaluated while the tool is present. This paper asks a different question: after using such a tool, what can the user still do on their own? I call this epistemic transfer. It refers to the effect of prior AI-assisted verification on later unassisted performance on new claims. In this paper, I make three contributions. First, I distinguish epistemic transfer from nearby outcomes such as correction effects, trust, reliance, and human--AI team performance. Second, I introduce two simple quantities for studying it: the Epistemic Transfer Effect (ETE), which compares delayed unassisted performance across conditions, and Tool-Removal Cost (TRC), which measures the immediate drop in performance when the tool is taken away. Third, I turn these ideas into a practical evaluation protocol that can be used in online experiments or field studies. The protocol combines answer-first and evidence-first AI conditions with active-practice and no-practice controls, delayed tests on held-out claims, behavioral measures, and participant- and item-level analyses. Putting ETE and TRC together yields a diagnostic space that separates capability building, capability plus tool advantage, epistemic inertness or de-skilling, and verification on loan. The point is not that every AI tool must teach. The point is that when independent judgment matters, we should test not only whether a tool helps now, but also what it leaves behind.

---


### 248. [City Sentinel: A Unified AI-Based Smart Surveillance Framework for Real-Time Multi-Threat Detection Using Deep Learning](https://arxiv.org/abs/2608.08887)

**<font color=#1a73e8>作者：</font>** Hanan Syed Shabir, Noor Fatima, Safia Baloch 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rapid urbanization has increased the need for surveillance systems that can monitor multiple public safety risks at the same time. Traditional systems often use separate solutions for facial recognition, vehicle identification, fire detection, and behavioral analysis, resulting in fragmented infrastructure and multiple interfaces for operators to manage. This paper presents City Sentinel, a unified AI-based surveillance framework that integrates six detection capabilities into one scalable platform: facial recognition, automatic number plate recognition (ANPR), fire and smoke detection, weapon and knife detection, violence detection, and road accident detection. The system combines a this http URL operator dashboard, FastAPI backend, cloud-based PostgreSQL event storage, InsightFace and YOLOv8 vision models, and EasyOCR for plate recognition. Camera streams are processed through dedicated inference workers using RTSP. On a workstation equipped with an NVIDIA RTX 3060 GPU, the system achieves a median end-to-end latency of 743 ms and supports four concurrent RTSP streams within a two-second latency limit. It achieves a 91.2% face-match rate, 85.7% plate-reading accuracy, and mAP@0.5 scores of 0.846 to 0.889 across the fire, knife, and weapon detection modules. In user-acceptance testing, operators could enroll a new identity in under one minute and identify a flagged person from live footage in an average of 12 seconds. The results demonstrate that a modular, open-source, multi-model architecture can provide broad surveillance coverage, cloud-based auditability, and flexibility for adding new detection capabilities while maintaining practical real-time performance.

---


### 249. [From Manuals to Maintenance: Fine-Tuning MedGemma for Multi-Modal Imaging System Support in Low-Resource Settings](https://arxiv.org/abs/2608.08896)

**<font color=#1a73e8>作者：</font>** Bernes Lorier Atabonfack, Zion Kongbi Nfo, Ahmed Tahiru Issah 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Imaging device downtime is a major barrier to healthcare delivery in low- and middle-income countries (LMICs), often driven by limited access to specialized biomedical engineering support. We present a multi-modality medical equipment maintenance question-answering (QA) framework and demonstrate the fine-tuning of a medical foundation model for specialized technical troubleshooting tasks. Guided by a multi-country survey across nine LMICs, we curated technical manuals from MRI and ultrasound systems to generate the INGENZI_DatasetV1, containing 10,294 high-quality, filtered QA-context pairs. Using QLoRA-based parameter-efficient fine-tuning, we adapted the MedGemma-4b-it model to interpret system error logs and generate step-by-step equipment repair instructions. Compared to the baseline model, the fine-tuned system achieved substantial improvements across metrics, including F1 score (0.22 to 0.38), ROUGE-2 (0.18 to 0.41), and BERTScore F1 (0.86 to 0.91). These metric gains demonstrate that the model generates significantly more precise and procedurally accurate technical responses to new troubleshooting queries. This work establishes a reliable foundation for AI-assisted diagnostic and maintenance tools in resource-constrained settings.

---


### 250. [Federated Attention Autoencoders with a Stochastic Aggregation Scheme for Anomaly Detection](https://arxiv.org/abs/2608.08906)

**<font color=#1a73e8>作者：</font>** Mihailo Ilić, Miloš Savić, Vladimir Kurbalija 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Outlier detection in decentralized data environments is a challenging task for many machine learning implementations, particularly in settings where data cannot be shared. Recently, there have been advances in federated outlier detection, some of which are based on the use of autoencoder networks. The introduction of attention mechanisms to autoencoders boosts their efficiency. However, the application of attention-based models in federated learning remains underdeveloped due to the absence of proper aggregation functions for these types of networks. In our work, we propose two novel aggregation functions tailored for attention-based autoencoders, which better preserve the learned information stored within the memory modules of these networks. We evaluated our approach on the KDDCUP10 dataset, and we showed that the proposed methods achieve up to 2.9\% and 5.1\% better results for F1 score and AUC ROC respectively when compared to traditional autoencoders.

---


> [!TIP]
> 当前位于：**201-250**（第 5/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-445](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
