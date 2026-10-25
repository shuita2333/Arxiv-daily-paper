# 📦 其他研究 | 2026年10月26日

> 本类共 **211** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-211](./part-05.md)

---

### 151. [Beyond Watching and Searching: Benchmarking Agents for Video-centered Deep Research Reports](https://arxiv.org/abs/2610.31158)

**<font color=#1a73e8>作者：</font>** Jiahao Meng, Qize Yang, Yuxuan Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep research agents synthesize open-web evidence into long reports, but current benchmarks do not evaluate research centered on a source video. We introduce Video-Centered Deep Research Report Generation. Given a video and user request, an agent identifies research questions, retrieves external multimodal evidence, and produces an interactive report linked to relevant video moments. This task has direct practical value because it helps users locate relevant moments, verify claims, reproduce demonstrated procedures, and make informed decisions from video content. We present a skill-based workflow and OmniDR-Bench for this task. For evaluation, we propose Omni Atomic Rubric Trees (Omni-ARTs). Each tree contains three dimensions, 23 shared directions, and task-specific atomic binary criteria. The directions test audiovisual grounding, multimodal evidence use, and interactive presentation. Audited Rubric Construction (ARC) builds these trees through independent evidence collection, automated checks, behavioral calibration, and iterative human review. OmniDR-Bench contains 50 Chinese and English tasks across 19 realworld subcategories. It includes 6,414 criteria. Across 18 agent configurations, the best system scores 63.3 out of 100. Current agents still need broader content coverage, stronger causal and logical analysis across modalities, and more accurate citation support. We further analyze models, harnesses, skill configurations, video categories, and research trajectories. The code and data are released at this https URL.

---


### 152. [Towards Field-Deployable Wearable IMU Systems for Occupational Activity Recognition](https://arxiv.org/abs/2610.31160)

**<font color=#1a73e8>作者：</font>** Ihsan Ul Haq, James Brusey, Farnad Nasirzadeh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wearable inertial measurement unit (IMU) systems for construction worker human activity recognition (HAR) routinely report aggregate accuracies above 95 %, rarely under genuine subject-independent (leave-one-subject-out (LOSO)) evaluation, masking the per-individual variance that determines real-world deployment performance. Using the VTT-ConIoT benchmark, we conduct, to our knowledge, the first systematic configuration sensitivity analysis of this dataset: six classifiers across five sensor placements and three window sizes under a single LOSO protocol, a personalised-calibration pilot, and a validated comparison of tabular GAN-based and standard time-series augmentation. Per-subject LOSO accuracy for the main multi-sensor, 16-class configuration ranges from 61.9 % to 88.7 % (mean 77.5 %), a 27 pp spread, though all data are laboratory-collected. Multi-sensor fusion and longer windows both improve accuracy; standard augmentation gives small, consistent gains, while Conditional Tabular GAN (CTGAN) augmentation actively harms accuracy with a demonstrated distributional-fidelity mechanism; and personalised calibration recovers 16.8 pp for the weakest participants from just 30 % of their own data. These findings provide evidence-grounded configuration guidance for scaling occupational body sensor networks towards field deployment

---


### 153. [BelT Block Cipher](https://arxiv.org/abs/2610.31178)

**<font color=#1a73e8>作者：</font>** Sergey Agievich, Victor Galinskij, Nikolai Mikulich 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> BelT is a block cipher with a 128-bit block size and a 256-bit key, developed in Belarus and adopted as part of the Belarusian national standard STB 34.101.31 for encryption and integrity control. Its specification was issued as a preliminary standard in 2007, becoming a final standard in 2011. BelT employs an eight-round structure combining elements of a Feistel network and the Lai-Massey scheme. This paper presents a complete description of the cipher and explains the principles underlying its design. Software performance and possible optimizations of BelT are discussed in comparison with those of candidates in the Advanced Encryption Standard (AES) competition.

---


### 154. [RaSFNet: Ray-aligned and Scan-aware Fusion Network for LiDAR Semantic Segmentation](https://arxiv.org/abs/2610.31186)

**<font color=#1a73e8>作者：</font>** Chuang Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LiDAR point cloud semantic segmentation is a fundamental component of 3D perception for autonomous driving and robotics. Projection-based methods map 3D point clouds into 2D representations for feature extraction using 2D networks. However, aggregating multiple points during projection can obscure geometric differences within each frustum, while local feature extraction limits the modeling of spatial relationships across scanning regions. Moreover, proximity in the projected representation does not necessarily imply proximity in 3D space, and interactions between point and projected features may mix features from different ranges, reducing semantic discriminability. To address these challenges, we propose the Ray-aligned and Scan-aware Fusion Network (RaSFNet), which incorporates point cloud geometry and LiDAR scanning characteristics into projection-based semantic segmentation. Specifically, the Ray-Aligned Geometric Distribution Encoding (RAGDE) module characterizes point distributions within each frustum using a ray-aligned coordinate system. To model spatial context, a Scan-Topology-Aware Mamba (STAM) block organizes frustum features according to the LiDAR azimuth sampling pattern and captures long-range dependencies across scanning regions. In addition, a Range-Constrained Point-Frustum Fusion (RCPFF) mechanism uses shared range information to guide feature exchange between point and frustum representations while maintaining spatial correspondence. RaSFNet achieves mIoU scores of 70.2% and 77.7% on the SemanticKITTI and nuScenes validation sets, respectively, indicating competitive segmentation performance compared with the evaluated methods.

---


### 155. [Inside-JEPA: From Prediction to Relational Grounding in Latent World Models](https://arxiv.org/abs/2610.31194)

**<font color=#1a73e8>作者：</font>** Hossein Resani, Javen Qinfeng Shi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Joint-embedding predictive architectures (JEPAs) learn world models in latent space, enabling efficient planning but leaving their states opaque. We introduce Inside-JEPA, which places relational channels for ordered entity pairs inside the JEPA latent state and shows that an inverse-dynamics loss can ground these channels without relation labels when its head reads them, either alone or as part of the full state. On Something-Something V2, latent prediction alone performs no better than a random relation head, while inverse-dynamics supervision that recovers actions from channel changes improves relational AUROC by .065-.103 across ten settings with annotated boxes, by .081 on RH20T robot episodes with held-out tasks, and by .050-.061 across five relations using off-the-shelf detection and tracking. An inverse head on entity latents decodes actions more accurately but barely improves relational grounding; shuffled labels, two label-free objectives, and action labels on only 5% of the pairs also fail to ground the channels. Given an action, predicted relational changes approach the quality of observed future relations (AUROC .599 vs .621). For one-step relational goals, a supervised readout of the 16 channels ranks the correct action among the top five of 65 in 43% of cases, compared with 24% for prediction-only latents and 17% for a frequency prior.

---


### 156. [Structural cryptanalysis of classic McEliece: Assessment of claims, costs and evidence](https://arxiv.org/abs/2610.31196)

**<font color=#1a73e8>作者：</font>** Ramses Fernandez  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> For the last two years, classical structural attacks on McEliece with binary Goppa codes progressed further, at the parameters of Classic McEliece, than in the previous four decades: a subexponential and then a quasi-polynomial distinguisher, key recoveries for public challenges with brute-force labels up to $254$, and conditional key-recovery estimates of about $2^{89}$ to $2^{128}$ per run of a large sparse linear-algebra computation, depending on the parameter set and on whether and how memory access is charged. On September 2026 the German BSI advised against new deployments of the scheme. This paper gives a version-aware critical assessment of these results. It separates proved distinguishers, conditional cost estimates and actual recoveries; analyses in detail Saarinen's HOVER algorithm, his conditional cost analysis and his recovery of the TII-254 challenge, together with Weis's cost study of Holdout/Hermite key recovery; and compares the other key-recovery routes and the objections raised against them. Our own analysis finds that the cost model is now the main quantitative uncertainty, with about thirty bits between the cheapest and the most expensive model for the same computation; that for the four larger parameter sets every model considered leaves the conditional estimates far below the targeted levels, whereas for mceliece348864 the shortfall is of the order of the spread between models; that the structural estimates are lower than Grover-accelerated information-set decoding for the four larger sets in essentially every model and comparable for mceliece348864; and that none of this is a demonstrated attack, since the underlying heuristics have been tested only on instances tens of thousands to hundreds of thousands of times smaller than the target. We close with open questions.

---


### 157. [Moving Regions, Not Moving Objects: Segmenting What Actually Moves under Camera Motion](https://arxiv.org/abs/2610.31209)

**<font color=#1a73e8>作者：</font>** Wenhua Jin, Tiancheng Chen, Sheng Tang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Moving object segmentation is conventionally formulated at the sequence and object level, marking an entire instance as moving once it moves anywhere in a video. Recent instantaneous formulations distinguish moving from stationary intervals, but still generate masks at the object level through frozen segmentation foundation models. Because the mask is derived from an instance-level proposal, motion is typically attributed to the entire instance rather than localized to the regions that actually move. Moreover, such instance-level predictions can produce masks even when no part of the instance is actually moving, revealing a more fundamental issue: motion is not an intrinsic property of an instance; it can only be determined by comparing at least two frames. Building on this premise, we introduce MoRSe, which jointly interprets two frames to predict a moving-region mask, distinguishing actual scene motion from apparent motion induced by the camera. A single RGB encoder replaces multi-stage foundation stacks, so no optical flow, point tracks, or separate mask generator is needed at inference. We release MoRSe-5K, a benchmark of 42 sequences with Static, Dynamic-Static, and Dynamic settings designed to evaluate the model's ability to distinguish and localize moving and stationary regions under different camera and scene motion conditions. MoRSe outperforms both specialized moving object segmentation methods and dense 4D reconstruction methods with motion-thresholded predictions, while producing the fewest false positives on sequences where nothing moves.

---


### 158. [Evolving Federated Density Peak Clustering with Shuffler-Based Anonymization](https://arxiv.org/abs/2610.31211)

**<font color=#1a73e8>作者：</font>** Miha Ožbot, Seiichi Ozawa, Igor Škrjanc  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we present a novel one-shot federated clustering approach based on evolving fuzzy clustering and shuffler-based anonymization. In federated clustering, each round reveals additional model information to the server and can increase the opportunity to infer properties of local datasets, even when raw samples are never shared. Consequently, fewer client-server exchanges and unlinkability are important, so transmitted information cannot be attributed to any single client. Data-stream clustering algorithms, which learn in a single pass over the data, align well with the one-shot federated learning paradigm, where a single communication round can be sufficient. The proposed Evolving Federated Density Peak Clustering (eFDPC) method combines evolving fuzzy data-stream clustering and density peak clustering in a federated setting. Each client independently evolves micro-clusters from private data mini-batches through cluster addition and merging. To limit communication, density peak clustering is applied to the learned micro-clusters and only the selected peaks are transmitted, rather than the full local models. A shuffler-based layer is introduced between the clients and the server to anonymize contributions prior to reconstruction and global peak selection. We consider a peak-only variant, eFDPC-P, as well as eFDPC-G with server-side label propagation. Experiments on synthetic and real-world benchmark datasets show that eFDPC outperforms recent federated clustering baselines in one-shot settings and scales to higher-dimensional, non-IID data.

---


### 159. [Local Discrimination of Binary Classifiers via Localized AUC Functional](https://arxiv.org/abs/2610.31216)

**<font color=#1a73e8>作者：</font>** Wenye Ren, Anna Győrffy-Kerekes, Tancredi Dorsi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Risk prediction models are frequently evaluated with AUC, which means that during evaluation we are blind to performance heterogeneity, which could lead to bad decision-making in clinics. In this work, we aim to change that by identifying patient cohorts for whom the risk prediction model might not be an accurate predictor. To separate these cohorts, we use a version of the weighted AUC, which we call Localized AUC or LAUC. Using this metric, we build a method that we coin LOCATOR. This method is able to identify cohorts of patients for whom the risk prediction model is inaccurate. We test this method both in real-world data and in simulations. We also build a statistical background for the use of Localized AUC for our purposes.

---


### 160. [GLOW-FM: Efficient Generative Low-Light Image Enhancement with One-Step Latent Flow Matching](https://arxiv.org/abs/2610.31222)

**<font color=#1a73e8>作者：</font>** Ariel Lapid, Yuval Haitman, Reuven Peretz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-light image enhancement (LLIE) aims to recover well-exposed and perceptually faithful images from severely degraded observations. Recent diffusion-based generative methods achieve strong perceptual quality by leveraging powerful image priors, but their iterative sampling incurs substantial computational cost, limiting practical deployment. Despite recent efficiency gains in generative LLIE, high-quality enhancement with a single function evaluation and low overall computation remains challenging, particularly under diverse real-world low-light conditions. We introduce GLOW-FM, a one-step latent flow-matching framework for efficient generative LLIE. GLOW-FM performs conditional transport in the latent space of a frozen Tiny-VAE and leverages Terminal Velocity Matching (TVM) to enable enhancement with a single function evaluation. Matched comparisons with alternative one-step objectives support TVM as an effective design choice, and, to the best of our knowledge, this is its first adaptation to image restoration and specifically to LLIE. Extensive experiments on challenging real-world benchmarks demonstrate that GLOW-FM achieves competitive image quality and state-of-the-art cross-dataset generalization while requiring only a single function evaluation and 34 GFLOPs for the small variant. These findings highlight the potential of GLOW-FM to bring generative LLIE closer to practical deployment through single-step inference and compact latent modeling. Code will be made publicly available upon publication.

---


### 161. [Lightweight Frame Compensation for Real-Time Polyp Segmentation under Frame Skipping](https://arxiv.org/abs/2610.31228)

**<font color=#1a73e8>作者：</font>** Weihao Gao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time polyp segmentation in computer-assisted colonoscopy is hampered by the difficulty of deploying high-accuracy models under strict latency budgets. Frame skipping, which performs inference every K frames and reuses or interpolates the rest, improves throughput but introduces motion blur and lesion misalignment that degrade temporal consistency. To close this gap, we propose the Lightweight Frame Compensator (LFC), a 77K-parameter plug-and-play module inserted before a frozen segmentation backbone. Operating on a three-frame window, LFC fuses consecutive frames via spatio-temporal attention into a single compensated frame, and is trained only on pseudo-labels generated by a differently seeded model, without any expert annotation. Experiments on three polyp video benchmarks show that LFC recovers most of the accuracy degraded by direct frame skipping and, in several settings, reaches the accuracy of frame-by-frame inference, while retaining a 2.05X--2.55X throughput gain. We further evaluate the temporal stability of three backbones spanning CNN, pyramid Transformer, and global-attention Transformer architectures, revealing a spectrum of sensitivity to frame skipping that arises from how locally or globally each architecture aggregates misaligned input. The compensation gain of LFC follows this spectrum: it is largest for high-capacity Transformer backbones, which achieve the best static accuracy but suffer the most under skip-frame inference. LFC thus offers a lightweight, pluggable, and deployment-friendly route to real-time polyp segmentation.

---


### 162. [Reward-Weighted Preference Optimization for Selective Combinatorial Optimization Problems](https://arxiv.org/abs/2610.31239)

**<font color=#1a73e8>作者：</font>** Haohui Zhang, Xinyu Hu, Wouter van Heeswijk 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has emerged as an effective approach for combinatorial optimization, but most existing methods focus on problems such as the Travelling Salesperson Problem (TSP) in which all elements must be served. Selective combinatorial optimization problems (SCOPs), including the Orienteering Problem (OP), Prize-Collecting TSP (PCTSP), Stochastic PCTSP and Knapsack Problem (KP), additionally require selecting which elements to include. This selection creates sampled solutions with substantially different objective values, yet standard preference optimization reduces such comparisons to binary rankings and discards the magnitude of these differences.
We introduce Reward-Weighted Preference Optimization (RWPO), a pairwise training objective that incorporates reward-gap information into preference learning. For candidate trajectories sampled from the same instance, RWPO weights each preference loss according to the normalized difference in their rewards, assigning greater training emphasis to comparisons that represent larger improvements in solution quality. We further combine RWPO with scale-specific fine-tuning and reward- and likelihood-weighted tilted sampling to adapt trained policies to larger and shifted instance distributions without relying on local-search post-processing.
Experiments on the OP, PCTSP, Stochastic PCTSP, and KP show that RWPO consistently improves over unweighted preference optimization and policy-gradient baselines across a wide range of instance sizes. On the OP, the resulting solver exceeds the mean reward of the Compass metaheuristic at scales from 100 to 2,000 nodes. The results demonstrate that preserving reward-gap information can substantially improve preference-based learning for selective combinatorial optimization and support generalization to large-scale instances.

---


### 163. [Weaponizing the Exit: Input Privacy Leakage via Exit Routing Manipulation in Multi-Exit Networks](https://arxiv.org/abs/2610.31246)

**<font color=#1a73e8>作者：</font>** Yulong Tian, Lei Wang, Jincan Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multi-exit networks improve inference efficiency by allowing inputs to terminate early at intermediate exits. We identify a privacy vulnerability in cloud deployments of these networks: a malicious Cloud Service Provider (CSP) can infer sensitive properties of individual user inputs solely from inference latency, without accessing inputs, intermediate states, or model outputs. The attack exploits the CSP's control over the model supply chain. Prior to deployment, the CSP supplies a specially crafted multi-exit network manipulated so that inputs carrying a target sensitive property are routed to a designated exit with high probability, while other inputs exit elsewhere. At serving time, the CSP infers the exit index from per-query latency, thereby determining whether each input possesses the target property without accessing inputs, outputs, or internal model states. We propose a training framework combining selective label smoothing and entropy-covariance optimization to control confidence distributions across exits and reduce premature termination. We conduct experiments on four datasets across ten target properties. The results demonstrate strong attack effectiveness and stealthiness. The attack achieves an average F1 score of 0.73, compared to 0.25 for the strongest baseline, while main task accuracy drops by less than 1.3\% and inference speedup degradation remains below 0.1 in most settings. Our code is available at this https URL.

---


### 164. [Reducing Multi-Horizon Photovoltaic Forecast Error through Tree-Anchored Expert Combination](https://arxiv.org/abs/2610.31248)

**<font color=#1a73e8>作者：</font>** Sun Ze, Zhou Liguo, Xu Yuqing 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A strong direct tree model may remain the best standalone photovoltaic forecaster, yet a weighted combination can reduce its residual errors. We examine whether complementary temporal predictors can lower the tree's mean absolute error (MAE) over 15--240 minutes without weaker ensemble members degrading performance. The candidate bank contains LightGBM and seven neural implementations with different temporal representations. A combiner fitted to MAE has nonnegative weights that sum to one. Unhelpful candidates can receive zero weight, while the tree anchors the combination and provides a development-stage fallback. The main design shares weights across horizons; horizon-specific weights and alternative losses test whether further complexity is needed. On 56,078 windows from two co-located public PVDAQ systems, the historical shared-MAE policy reduces scaled MAE by 3.21\% relative to the tree.
The latest bounded neural correction does not reduce MAE further than this static combination. The results support selective combination of complementary predictions in this bank rather than equal averaging or indiscriminate addition of modules. Both analyses reuse a previously inspected evaluation period. They do not establish independent replication, weather-specific causation or universal gains from eight experts.

---


### 165. [QuaNAS: Uncertainty-Aware Reuse of Earlier Searches for Query-Efficient Neural Architecture Search](https://arxiv.org/abs/2610.31251)

**<font color=#1a73e8>作者：</font>** Brama Seta Putra Satria, Dwi Sunaryono, Misbakhul Munir Irfan Subakti 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural architecture search (NAS) on a new dataset often affords only tens of short training runs, so what the search knows before its first evaluation decides its efficiency. Yet most NAS methods start from scratch, guided at best by zero-cost proxies that are unreliable across tasks. QuaNAS treats a library of earlier searches in the same search space as explicit knowledge of uncertain reliability. Main effects of design decisions learned from this library and, secondarily, zero-cost proxies become priors over candidate architectures without any label of the new dataset. A Gaussian process starts at the prior optimum and re-estimates after every evaluation how far each prior is trusted. Under a protocol frozen before any confirmation data were seen, QuaNAS was evaluated once on 12 new image, time-series, text and tabular datasets. It lowered anytime regret on the short-training objective 2.7- to 3.9-fold relative to five pre-specified NAS baselines that start from scratch (Holm-adjusted p = 0.0012 each). Its final models matched (non-inferiority margin 0.5 pp) or exceeded matched-recipe reference models on nine datasets, as did the prior optimum, selected without a single evaluation. Post-hoc comparisons with established transfer methods given the same library trace the gain to the library: without it, the same Gaussian process had over twice the regret. They also show where each transfer mechanism works best: the pooled main effects of QuaNAS for weakly transferable tabular tasks, per-task surrogates for image, time-series and text tasks and for small or mismatched libraries. Finally, the main effects make the transferred knowledge inspectable.

---


### 166. [Reinforcing intra-operative tumour localisation with weak supervision from pre-operative appearances](https://arxiv.org/abs/2610.31253)

**<font color=#1a73e8>作者：</font>** Sidhart Sami, Ali Sharjeel, Sri Atluri 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Limited tumour visibility on intra-operative images complicates surgical navigation, including liver hepatocellular carcinoma (HCC) targeting on computed tomography (CT) imaging. This makes labelled datasets difficult to curate for deep learning, and transferring pre-operative delineations through registration remains challenging due to intra-operative deformation and lack of paired pre- and intra-operative data. We propose to transfer tumour appearances learned from pre-operative magnetic resonance (MR) images to guide localisation on intra-operative CT through weak supervision. A classifier is trained to classify tumour presence on pre-operative images. This is applied to windows on intra-operative images, and despite the domain gap, it assigns higher tumour-presence probabilities on average to tumour-containing windows. These weak cross-domain signals guide a reinforcement learning agent to localise tumours on intra-operative images. We compare direct transfer, few-shot adaptation and synthetic transfer (trained using unpaired MR and CT), which translates CT into synthetic MR before localisation. On an external HCC cohort, synthetic transfer outperformed other tested methods and CT-only baselines. Our framework enables cross-modality tumour localisation without paired MR-CT training images.

---


### 167. [Deep ReLU Networks Can Fail the Best Approximation Property for Continuous Target Functions](https://arxiv.org/abs/2610.31264)

**<font color=#1a73e8>作者：</font>** Sebastian Kassing  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We construct a continuous function on $[-1,1]^2$ for which the infimum of the $L^2$-approximation error over the class of ReLU networks with two hidden layers and architecture $(2,2,1,1)$ is not attained. This counterexample shows that deep ReLU networks do not satisfy the best approximation property in general, even for continuous target functions. Our findings contrast with existing results for shallow neural networks, where ReLU is one of the few activation functions that guarantee the existence of global minima in typical regression tasks. The proof is based on the fact that the breaklines for neurons in the second hidden layer can bend, which breaks the symmetry arguments used in the one-hidden-layer case.

---


### 168. [DISC: Domain-Integrated Similarity Cost for Time-Series Dataset](https://arxiv.org/abs/2610.31288)

**<font color=#1a73e8>作者：</font>** Yen-Ku Liu, Hongjie Chen, Franck Dernoncourt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The growth of time-series datasets and foundation models has made dataset comparison a central part of time-series workflows. Assessing source-target transfer before model adaptation requires similarity estimates that can summarize transfer-related dataset relationships without exhaustive source-target evaluation over every candidate pair. Many metrics have been proposed for measuring similarity between time-series datasets, but they capture different dataset relationships and vary in how well they align with downstream utility across tasks. We evaluate this gap by measuring the correlation between source-target similarity scores and downstream forecasting errors in out-of-distribution and transfer-learning settings. We propose Domain-Integrated Similarity Cost (DISC), a learnable aggregation framework that uses calibration transfer observations to select, weight, and combine similarity metrics for different downstream tasks. By integrating complementary metric values, DISC better distinguishes source-target dataset differences that matter for downstream behavior. After calibration, DISC scores source-target pairs using only their similarity-metric values and yields higher alignment than single-metric references on the reported split. These results show that time-series dataset similarity is task-dependent, and that learned metric integration provides a stronger proxy for downstream transfer behavior than manually selecting one similarity metric.

---


### 169. [RecallGS: Geometry-Grounded Recall for Online Semantic Gaussian Splatting](https://arxiv.org/abs/2610.31293)

**<font color=#1a73e8>作者：</font>** Thanh-Khoi Nguyen, Thien-Phuc Tran, Minh-Triet Tran  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online semantic 3D Gaussian Splatting (3DGS) enables open-vocabulary scene understanding from streaming observations. However, existing methods recover geometric context missing from image-derived semantic features using an additionally learned 3D network, incurring extra training and runtime overhead. We observe that such geometric-semantic evidence may already exist in the agent's observation history and can be retrieved rather than learned. Based on this insight, we introduce RecallGS (Geometry-Grounded Recall for Online Semantic Gaussian Splatting), a lightweight, training-free mechanism that treats past observations as a non-parametric geometric-semantic prior. RecallGS follows a recall-ground-fuse pipeline: CLIP retrieves relevant observations, alpha-compositing weights identify geometrically supported views, and aggregate their semantic features over each Gaussian's rendered footprint. On ScanNet and ScanNet++, RecallGS achieves strong semantic segmentation performance at 2.48 FPS, demonstrating that geometric-semantic context can be effectively recovered from observation history without an additional learned 3D branch.

---


### 170. [Practical Auditing of Differentially Private Graph Release Mechanisms: Methodology, Toolkit, and Case Study](https://arxiv.org/abs/2610.31294)

**<font color=#1a73e8>作者：</font>** Nicholas D'Silva, Surya Nepal, Salil S. Kanhere  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Differential Privacy (DP) has become a prominent approach for protecting graph data releases, yet empirical auditing methodologies have largely been developed for tabular datasets and machine learning pipelines rather than graph-structured outputs. We present a methodology for empirically auditing DP graph release mechanisms, identifying two graph-specific audit design problems: canary construction and witness statistic selection. We combine these components with an established statistically certified testing procedure and implement the resulting methodology as an open-source Python toolkit. To demonstrate the approach, we audit a published state-of-the-art Node-DP graph release mechanism. Across a series of synthetic and real-world canary pairs, we obtain certified lower bounds on the privacy parameter {\varepsilon} that exceed the claimed value, yielding counterexamples sufficient to falsify the claimed guarantee for the audited implementation. The violations persist under progressively stronger restrictions on the input domain, including non-empty and connected graphs. We also show that witness selection can materially affect whether a violation is detected, highlighting the importance of evaluating a diverse battery of statistics when auditing DP graph release mechanisms.

---


### 171. [PiHand: Latent Hand-Object Interaction Priors for Physics-Based Policy Learning](https://arxiv.org/abs/2610.31299)

**<font color=#1a73e8>作者：</font>** Niklas Berndt, Xianghui Xie, Enes Duran 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthesizing physically grounded dexterous hand-object interactions is important for VR/AR, gaming, and robotics, yet remains challenging because subtle contact dynamics, diverse object geometries, and target trajectories must be jointly respected while maintaining natural grasps. Existing methods either track mocap trajectories with limited transfer to novel objects, or rely on hand-only generative priors that fail to capture coupled hand-object motion, sacrificing contact fidelity and sample efficiency. To tackle these challenges, we introduce PiHand, a Physically grounded Interaction-aware Hand motion synthesis framework. PiHand first trains expert policies that track mocap demonstrations in simulation, distills them into a unified hand-object interaction prior using a goal-conditioned VAE, and finally solve diverse dexterous manipulation tasks through bounded residual exploration in its latent space. With only a single reward and no complex curriculum training, this yields general tabletop manipulation policies that generalize to unseen objects and trajectories on GRAB and DexYCB. The same prior transfers to object catching and bimanual handover, two tasks that are rarely seen in its training data. Across all tasks, PiHand consistently outperforms baselines in all metrics. We will release the processed data and model checkpoints.

---


### 172. [Subgoal-aware Memory Graph for GUI Agent](https://arxiv.org/abs/2610.31307)

**<font color=#1a73e8>作者：</font>** Dezhao Luo, Daniel Beechey, Derek Yuen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> GUI agents aim to automate complex user tasks by interacting with mobile interfaces, but ef- fective decision-making in long-horizon set- tings requires reusing prior experience rather than relying solely on the environment ob- servations. Existing memory-based methods typically store experience either at the single- action level or as entire trajectories. Single- step actions are often too fine-grained to carry meaningful semantics, since the success of an individual action does not necessarily imply progress towards the overall goal. In contrast, whole trajectories are often too coarse-grained and difficult to reuse across different tasks. We propose a subgoal-aware memory graph that distils past trajectories into structured, reusable evidence at the level of subgoals. We define a subgoal as consecutive actions shar- ing a single intent, the granularity at which progress toward the task becomes meaning- ful. To reduce redundancy and support cross- task reuse, we organise subgoal experiences as nodes in a graph, where related memories can be merged, extended, and retrieved based on the environment observation. On SPA-Bench, our method improves success rate by 11.11% over the baseline.

---


### 173. [The Bayesian Learning Rule Beyond KL Geometry](https://arxiv.org/abs/2610.31308)

**<font color=#1a73e8>作者：</font>** Sophia Sklaviadis, Wu Lin, Andre Martins 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Bayesian learning rule (BLR) exploits the relation between Bayesian updating and the Kullback-Leibler divergence (KLD) to derive efficient additive updates for exponential family variational posteriors. The KL geometry is powerful but restrictive: combined with posterior families with parameter-dependent support it can lead to undefined objectives. We ask which non-KL geometries preserve the additive BLR computation. Previous works that use $f$-divergences suggest that this is only possible with the KLD. Here, we show that this is not true. We show that additive information-geometric optimization algorithms can be derived for the class of mixed-space Bregman or Fenchel-Young discrepancies. These discrepancies induce generalized maximum-entropy families, dual coordinates, and generalized-BLR canonical gradient updates, recovering the classical BLR. The generalized BLR leads to new algorithms that \textit{cannot} be derived from the KL-based BLR. For the Tsallis negentropy with quadratic statistics, the generalized BLR yields bounded-support and heavy-tailed $q$-Gaussian posteriors and an easy Newton-like implementation. Experiments up to CIFAR-100 illustrate controllable support and tail behavior and competitive performance.

---


### 174. [Identifiability from Stationary Covariance in Linear SDEs with Reciprocal Interactions and Latent Variables](https://arxiv.org/abs/2610.31310)

**<font color=#1a73e8>作者：</font>** Ana Leticia Garcez Vicente, Saber Salehkaleybar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous-time stochastic differential equations (SDEs) provide a natural framework for modeling interacting dynamical systems. A central causal question is whether causal effects among observed variables can be identified from observational data drawn from the stationary distribution, given the underlying causal graph. For linear SDEs, existing identifiability results are largely restricted to fully observed systems whose causal graphs contain no directed 2-cycles. We first establish new graphical conditions for the generic identifiability of causal effects in systems that may contain directed 2-cycles, thereby allowing for reciprocal interactions. Next, we address the previously unexplored setting of latent variables by developing an instrumental-variable framework for identifying a target direct causal effect under partial observability.

---


### 175. [Bridging the Data Gap: Source-Informed Task-Space Transport for Few-Shot Diffusion](https://arxiv.org/abs/2610.31323)

**<font color=#1a73e8>作者：</font>** Jinjian Jiang, Jing Peng, Rehan Deen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many deployments require a model to move rapidly from a data-rich source to a related target observed only sparsely. This is especially consequential where target data are difficult to collect, as in healthcare settings with persistent population or acquisition imbalances. Retraining or fine-tuning a high-capacity generator for every target is costly and can be statistically unreliable when target data are scarce. We introduce Meta-Diff, which instead learns a recurring source--target relation once in a compact task space. A shared encoder maps each distribution to a low-dimensional coordinate; a learned relation transports a new source coordinate to its predicted target, and a shared diffusion backbone generates from that prediction without target-specific retraining. Controlled Gaussian-mixture experiments identify when this works: task identity must survive the representation, the relation must generalise across tasks, and the source--target shift must leave useful headroom for transport. On held-out CIFAR-100 validation tasks, correct source $+$ transport achieves 13.9% lower mean SW than transport from the wrong source. With validation-selected adaptation settings in the final-test one-target comparison, its mean SW is 14.7% lower than target-only modelling and 32.7% lower than full fine-tuning; the main route itself uses no target image and assumes the applicable relation is known. On matched CIFAR test episodes, generating from the clean-source coordinate and then applying the known corruption yields lower SW than task-space transport. Office-Home exposes a complementary boundary: transport can align target-domain statistics without reliable object identity. Together, these results recast extreme-few-shot adaptation as reusable transport in task space, while making the conditions for its success and failure directly measurable.

---


### 176. [Muffin - A Shared Memory Buffer for Asynchronous AI Agents](https://arxiv.org/abs/2610.31355)

**<font color=#1a73e8>作者：</font>** Ping-Lin Kuo, Suman Navaratnarajah, Christian Frey 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rise of Agentic AI systems has changed the landscape of artificial intelligence by enabling strong reasoning capabilities through specialized multi-agent interaction with structured self-reflection. However, in target-driven reasoning tasks, single- and multi-agent systems are often on par in terms of performance gains. A major challenge is that failures often arise from an ineffective exchange of critical information during inter-agent interaction and coordination. Different from existing multi-agent debate paradigms that rely on synchronous turn-taking and sharing information across different agents, we propose an inter-agent protocol based on shared Memory bUFFer INference - referred to as MUFFIN - in an asynchronous agentic framework. In the first step, an orchestrator routes queries based on their reasoning demands and delegates demanding ones to a multi-agent setting, where a shared memory buffer provides asynchronous exchange of intermediate findings while an agent's private reasoning remains local. Our experiments show that our framework Muffin outperforms established competitors, achieving the best accuracy in 17 out of 20 of our benchmark settings, and provides a better quality-cost trade-off than multi-agent debate: Muffin improves accuracy by 19.2 accuracy points while using 77.4% fewer tokens, without requiring full-trace sharing.

---


### 177. [RIDAR: Safeguarding Research Integrity in Autonomous Research Agents via Automated Detection and Runtime Intervention](https://arxiv.org/abs/2610.31372)

**<font color=#1a73e8>作者：</font>** Jiening Siow, Amy Xin, Junjie Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous research agents are increasingly used to automate large portions of scientific research, yet they are prone to research integrity violations (RIVs): behaviors that compromise the validity, reproducibility, or faithfulness of the research process. We present RIDAR, a framework for automated RIV detection and runtime intervention. First, we introduce RIVT, a comprehensive taxonomy of 14 RIV types spanning the full research lifecycle. Building on RIVT, we present RIDAR-post-hoc, a framework to detect RIVs within agent trajectories. RIDAR-post-hoc achieves 85.2% F1 performance on RIV-Gold, a benchmark for RIV detection with 60 expert-annotated trajectories. Applying RIDAR-post-hoc to RIV-Wild, a dataset of 300 agent trajectories across 50 distinct research tasks, we detect 3,964 RIV instances in 99.7% of trajectories, revealing the prevalence of RIVs in current agents. Finally, we present RIDAR-runtime, a framework for dynamically detecting and correcting RIVs during agent runtime. RIDAR-runtime effectively reduces agent RIVs remaining at task completion by 36.8%. We will release our code and data to facilitate future research.

---


### 178. [A Task-Centric Survey of Long-Document Visual Question Answering: Taxonomy, Evolution, and Future Directions](https://arxiv.org/abs/2610.31385)

**<font color=#1a73e8>作者：</font>** Yufei Tong, Guanjie Cheng, Tianle Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual document understanding is essential for acquiring knowledge from visually rich documents and is attracting growing research interest. Existing surveys emphasize architectures or technical approaches, with limited attention to how task bottlenecks shape technical choices and research priorities. We present a task-centric survey that decomposes long-document visual question answering (VQA) into four components: document parsing, evidence organization and retrieval, generator organization and learning, and evaluation. For each, we develop a fine-grained taxonomy and trace motivations, technical responses, and cross-component connections. We focus on explicit retrieval while covering direct reading. Our temporal analysis traces expanding priorities from multimodal content understanding to sufficient, high-fidelity evidence acquisition and sustained evidence management. We outline future directions in evidence sufficiency, verifiable and correctable understanding, and budget-aware coordination, with an outlook on continual document understanding.

---


### 179. [Post-Hoc Feature Selection Layer for Neural Networks Interpretability](https://arxiv.org/abs/2610.31420)

**<font color=#1a73e8>作者：</font>** João Kenji Suwa, João Pedro Silveira e Silva, Bruno Iochins Grisci  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The interpretability of complex neural networks remains a critical challenge, especially for models already deployed in high-stakes domains. To address this, we adapted the Feature Selection Layer (FSL) to optimize feature weights post-training, a variant we term post-hoc FSL. Our approach reframes the FSL as a lightweight, trainable module that integrates with already frozen pre-trained models on tabular datasets to highlight the features the original model considers most important. This post-hoc FSL learns feature relevance by fine-tuning its weights based on the original model's learned outputs. Crucially, this process is non-invasive, operating without altering the original model's architecture or its learned parameters. We conducted our experiments using both statistical and visual metrics, including accuracy, F1 score, recall, precision, weighted t-SNE and silhouette score, and also analyzed the stability of the post-hoc FSL on high-dimensional synthetic and real-world tabular datasets. We compared the post-hoc FSL feature weighting method using these metrics against the original embedded FSL and other post-hoc interpretability methods, such as Integrated Gradients, Noise Tunnel, DeepLIFT, Gradient SHAP, and Feature Ablation. Experimental results demonstrate that the post-hoc FSL feature weighting method successfully identified relevant features across the different datasets, maintaining the predictive power of the original neural network while enhancing its interpretability.

---


### 180. [How Well Do Decision Models Transfer to Vietnamese? An Empirical Study of Text Classification](https://arxiv.org/abs/2610.31422)

**<font color=#1a73e8>作者：</font>** Phat Huu Ha, Nguyen Xuan Phuc, Nong Nhut Quy 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in specialized decision models have expanded the possibilities for zero-shot classification, yet their effectiveness on Vietnamese remains underexplored. This study evaluates four specialized decision models across 13 classification settings spanning six task groups, examining zero-shot performance, sensitivity to label-description language, and robustness to Vietnamese linguistic variations. The evaluation considers English, Vietnamese, and bilingual label descriptions, alongside common linguistic perturbations involving teencode, typographical errors, and diacritic removal. Under English label descriptions, JEV achieves the strongest overall performance, ranking first in 11 classification settings. The effects of label-description language vary across models and datasets, with bilingual descriptions providing no consistent improvement. Robustness experiments reveal that diacritic removal causes the most substantial performance degradation, reducing mean macro-$F_1$ by 9.51--15.47 points across model configurations, considerably more than teencode or typographical errors. These findings highlight the importance of label-description choices and Vietnamese orthographic variation when evaluating specialized decision models for zero-shot text classification.

---


### 181. [Conservative Meta-Agent Search: Architecture Adaptation under Non-Stationarity](https://arxiv.org/abs/2610.31436)

**<font color=#1a73e8>作者：</font>** Ali Atiah Alzahrani  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated agentic-system design is typically evaluated on static task suites with immediate scalar rewards. Deployed systems face persistent shift, delayed dependent feedback, correlated component failures, and costly architecture changes. We formalize meta-agent architecture search as sequential incumbent replacement with switching costs and hard risk constraints and introduce Conservative Meta-Agent Search (CMAS). CMAS retrieves archived architectures and proposes typed graph edits, then scores each against the incumbent by paired shadow replay under common random numbers, with interventional component credit. Promotion requires an empirically calibrated, variance-penalized simultaneous score above a pre-specified margin, and is followed by a simulated canary stage and pre-specified rollback. Since backtests cannot certify meta-level skill, we introduce MetaInvest-Bench, a regime-switching simulator whose specified worker competence makes a surrogate-optimal architecture computable, with leakage-controlled replay, adversarial governance tracks, and five negative controls. Financial streams serve as a risk-sensitive testbed for meta-level generalization; we claim no alpha. Across 96 streams, CMAS cuts normalized mean surrogate dynamic-oracle regret from 0.116 to 0.104 and raises held-out utility from 0.44 to 0.48 over the strongest adaptive baseline; when extra workers add no value, it contracts to near-single-agent teams. Its deployment inference cost is ~6% lower, though its search-inclusive token cost is the highest of the methods compared. The observed per-update false-promotion rate is 3.4% against a nominal 5% target, and 4.8% in a sealed rerun. The calibration is empirical: it concerns an update-level replay statistic on an author-designed benchmark, and guarantees neither full-utility improvement, nor absence of simulated canary-stage harm, nor sequence-level error control.

---


### 182. [When Is a Memory Safe Enough to Act On? Action-Conditioned Verification for Long-Lived Agents](https://arxiv.org/abs/2610.31446)

**<font color=#1a73e8>作者：</font>** Yiqi Wang, Yifei Wang, Jiaqi Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Long-lived agents act on memory carried across sessions, and many of their actions are irreversible, so a stale memory can turn directly into harm. Existing work improves the memory itself --- retrieving, refreshing, or reconciling entries --- yet whether an entry must be re-checked before acting is not a property of the entry: the same remembered address can be used unchecked for a routine shipment but should be re-confirmed before a valuable one. We therefore study \emph{action-conditioned memory verification}: given a candidate action, decide which of its memory premises to re-verify and when to proceed or abstain, balancing execution risk, abstention, and verification cost. We formulate this as a sequential stopping problem, in which a verification is worth its cost only if it can change what the agent does next; under suitable verifier reliability and cost conditions, increasing action consequence can move the same memory through proceed, verify, and direct-abstention regimes. Building on this formulation, \textsc{AMV-Guard} is a practical verification gate that extracts the premises a candidate action rests on, calibrates beliefs about whether they are wrong, and selects checks by bounded value of information (VOI). On ToolSandbox, relative to a static policy given the same inputs, it lowers mean verification cost by 33.9\% while keeping 100\% safe-proceed recall and 0\% Gate harmful, and raises Proceed coverage from 38.83\% to 44.17\%; in a gate-core transfer to AppWorld, which carries over the stopping/VOI core but not the full structured pipeline, it lowers verification cost by 21.3\% at a small cost in safe-proceed recall and task success. These results suggest that verification effort should be set by what an agent is about to do, not only by how reliable a memory appears.

---


### 183. [MixPT: Point Transformer with Interleaved Window and Global Attention](https://arxiv.org/abs/2610.31455)

**<font color=#1a73e8>作者：</font>** Minkyun Seo, Hyungtae Lim, Jaesik Park  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Point cloud transformers aim to capture detailed local geometry and relationships across a scene at a manageable computational cost. Two common approaches are window attention and global attention. They differ in how they enable scene-wide interaction, which refers to information exchange among tokens across a scene. Window attention reduces computational cost by restricting self-attention to groups of tokens called windows; in serialized designs, each window contains a fixed number of consecutive tokens from a spatially ordered sequence. Because each block only directly connects tokens within the same window, information exchange across windows relies on changes in window membership across blocks and hierarchical pooling. Global attention, in contrast, directly connects all tokens within a scene, but computing attention over all token pairs can be costly when the number of tokens is large. To balance computational cost and scene-wide interaction, we introduce MixPT, a point transformer that uses a mix of window and global attention blocks in an interleaved schedule, while retaining a single fixed serialization pattern for its window blocks. For scenes with a large number of tokens, MixPT applies global attention to spatially pooled tokens and returns residual updates to the original-resolution stream. Across indoor and outdoor benchmarks, MixPT achieves competitive accuracy with lower latency than representative window and global attention baselines. We further demonstrate the feasibility of scaling the attention stage in depth by repeating the interleaved pattern of window and global attention blocks.

---


### 184. [How Different, or Different How? Stance Granularity in Viewpoint Selection for Dialog Systems that Engage Users with Alternative Views](https://arxiv.org/abs/2610.31459)

**<font color=#1a73e8>作者：</font>** Morita Tarvirdians, Reeve Lorena, Catharine Oertel  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Systems that aim to help a user engage with viewpoints other than their own have to decide how different those viewpoints should be. Viewpoints are mainly represented on a scalar scale, too coarse to distinguish viewpoints that disagree with the user about different things. We introduce a selection policy in which a bandit sets how far viewpoints may sit from the user, and the policy selects the most novel viewpoint within that bound. We vary only its stance encoder, comparing a scalar score with Perspectivized Stance Vectors, which break a position into separate stances on concepts. We integrate it inside a dialog system and run a between-subjects study (N=63). Concept-level stance produces more varied exposure sequences and broader coverage of the topic's positions, but does not change how deeply users justify viewpoints or how accurately they reconstruct them. Finally, we analyze user--viewpoint relations at the concept level, showing that users reconstruct a viewpoint least accurately on concepts that one side took no position on, rather than on concepts where the two disagreed. Our findings open up opportunities for dialog systems that support engagement with alternative viewpoints by acting on which concepts a user and a viewpoint disagree on, rather than on distance alone.

---


### 185. [RheOPT: Few-Shot Non-Newtonian Flow Prediction via Newtonian Pretraining of RheOFormer](https://arxiv.org/abs/2610.31465)

**<font color=#1a73e8>作者：</font>** Maedeh Saberi, Amir Barati Farimani, Safa Jamali  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite advances in numerical methods, non-Newtonian flow simulations remain computationally expensive because velocity and stress must be advanced together through rate- and history-dependent constitutive dynamics. Neural-operator surrogates reduce inference cost after training, but their training data require the same expensive simulations they aim to replace, making data-efficient learning essential when only a few non-Newtonian simulations can be afforded. Here, we introduce the Rheological Operator Pretrained Transformer (RheOPT), which pretrains a transformer-based neural operator on inexpensive Newtonian simulations and fine-tunes it on a small number of non-Newtonian samples. Rather than transferring the Newtonian constitutive response itself, RheOPT reuses geometry-conditioned transport structure that remains useful after the stress model changes. We evaluate RheOPT in two geometry-matched settings: a $4{:}1$ contraction channel for Giesekus, Oldroyd-B, and Bingham fluids, and the oscillatory wake behind a triangular obstacle for Oldroyd-B flow. In the contraction, Newtonian pretraining substantially improves few-shot prediction, and a model fine-tuned on four target samples can match or exceed a from-scratch model trained on four times as many. This benefit is reliable under reversible instance normalization (RevIN) but dataset dependent under Global normalization, a difference we trace to the dynamic range of each fluid's velocity and stress fields. In the wake, where relative $L_2$ error alone cannot verify that vortex shedding is recovered, phase-insensitive diagnostics show that pretraining recovers the shedding frequency and wake fluctuation amplitude that are suppressed by the from-scratch model in the few-shot regime. Overall, RheOPT establishes Newtonian simulation as a physically grounded pretraining source for data-efficient non-Newtonian operator learning.

---


### 186. [Supporting or Replacing Students' Reasoning? Cognitive Offloading in AI-Assisted Proof Learning](https://arxiv.org/abs/2610.31481)

**<font color=#1a73e8>作者：</font>** Eason Chen, Sophia Judicke, Kayla Beigh 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We studied 153 students in an undergraduate proof-based mathematics course with staggered-access to an AI support system. Students were randomly assigned to receive an AI chatbot and a homework-feedback interface earlier or later in the course. During the period when only the early-access group had access, their homework scores were 2.56 points higher, but exam performance did not differ significantly between groups, suggesting that improved AI-supported homework performance did not translate into detectable gains on a subsequent exam. After all students received access, every additional 100 messages sent to the AI chatbot was associated with a 3.02-point lower score on the subsequent exam. A mediation analysis showed a significant indirect association linking lower baseline self-efficacy to greater chatbot use and, in turn, lower exam scores: a one-point decrease in self-efficacy corresponded to 0.62 fewer exam points through chatbot use. These findings raise concerns that students may use the chatbot to offload their cognitive reasoning. Use of the homework-feedback interface, which required students to submit their proof attempts before receiving feedback, was not negatively associated with exam performance. We recommend against using a chatbot for AI tutoring and suggest exploring a tutor embedded in the course activities.

---


### 187. [SABLE: Scalable Affine Bayesian Latent-space Exploration](https://arxiv.org/abs/2610.31495)

**<font color=#1a73e8>作者：</font>** Erik Bodin, Lisa Maria Kreusser, Donney Fan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Complex objects such as engineering designs and proteins are often difficult to optimise because their design spaces exhibit high-dimensional structure and objective evaluations are expensive. Generative models provide continuous latent representations, but their latent spaces can have thousands to tens of thousands of dimensions, creating a regime where the latent dimension $D$ greatly exceeds the evaluation budget. We introduce SABLE, a Bayesian optimisation method for high-dimensional latent spaces with an isotropic distribution and limited budget. SABLE uses a Bayesian affine surrogate for prediction and acquisition, treating higher-order structure as surrogate discrepancy. After $N$ observations, the slope update has dimension at most $N-1$, yielding a decomposition of each query into an in-span component optimised by expected improvement (EI) in at most $N$ dimensions and an off-span component governed by a scalar norm. We show that the off-span norm implicitly selected by affine EI can lead to underexploration, and SABLE instead prescribes it using a finite-horizon schedule, without restricting search to a learned subspace. A recompression scheme reduces information to $\mathcal O(M)$ pseudo-observations, bounding refitting cost by $\mathcal O(M^2D+M^3)$ while keeping parameter inference, prediction, and acquisition decisions to tens of milliseconds. Across synthetic benchmarks and latent-space optimisation tasks, SABLE achieves high sample efficiency and reduces decision time by several orders of magnitude at large budgets.

---


### 188. [Evaluation of Uncertainty-Aware Multi-Software Ensembles for Hippocampal Segmentation](https://arxiv.org/abs/2610.31505)

**<font color=#1a73e8>作者：</font>** Gabriel Oliveira-Stahl, Anna Schroder, James Moggridge 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate hippocampal segmentation can be a useful tool for diagnosing and monitoring neurological conditions such as Alzheimer's disease and epilepsy. While numerous automated segmentation methods exist, their clinical adoption remains limited. Reliable uncertainty assessment can enhance trust and facilitate clinical translation. This study evaluates ensembles of five heterogeneous hippocampal segmentation methods - InnerEye, ASHS, FastSurfer, HippoSeg, and FreeSurfer - across two dementia datasets and one epilepsy dataset. The sub-ensemble containing InnerEye, FastSurfer, and HippoSeg emerged as both accurate and efficient, highlighting the feasibility of balancing computational cost and performance. Additionally, ensemble-derived uncertainty quantification with sample variance, mutual information, and predictive entropy is shown to reduce inaccurate segmentations by flagging low-confidence cases, potentially providing a mechanism for automatically escalating ambiguous cases for expert assessment. Lastly, this study explores the downstream clinical utility of ensemble-derived uncertainty, finding a significant correlation with motion artefact severity and a modest contribution to Alzheimer's disease classification.

---


### 189. [FairFRESH: A Neuro-Symbolic Framework for Fair and Explainable Household Food Recommendation](https://arxiv.org/abs/2610.31506)

**<font color=#1a73e8>作者：</font>** Kodur Sai Vinay Sathvik, Kakoli Bora, Tejaswini R. M  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recommender systems typically serve one user at a time. However, in households, members share a finite pantry and follow different dietary rules, making independent recommendations prone to resource conflicts and dietary violations. We formulate household food recommendation as constrained fair division and present FairFRESH, a neuro-symbolic framework that learns per-member utilities, allocates foods under explicit welfare objectives, enforces dietary rules through a deterministic filter, and explains recommendations using Shapley and Banzhaf attributions. Theoretically, we show that no finite penalty guarantees compliance near a dietary-rule threshold, establish approximation guarantees for greedy allocation under utilitarian and smoothed Nash objectives in the stock-free model before filtering, and characterize the scale invariance of Nash welfare. We also use the minimax theorem to analyze rotating shared meals. On NHANES-derived data, the learned utility model achieves Recall@20 of 0.293, outperforming five learned recommenders (at most 0.244) but not a previous-day repetition heuristic (0.321). On held-out four-person households, Nash allocation reduces Gini disparity by 42% relative to conflict resolution while improving Recall@20 from 0.180 to 0.197. It comes within 2% of an upper bound on the smoothed Nash optimum, and rescaling one member's utilities changes at most 1.5% of assignments. All recommendations satisfy the encoded dietary rules, while attribution scores correlate with utility loss upon component removal (r = 0.76). In simulation, shared meals reduce pantry use by about one-third, and weekly rotation increases the worst-off member's utility by 38% over the best fixed meal.

---


### 190. [Piano2Pop: Expanding Piano Demos into Pop Productions Without Aligned Supervision](https://arxiv.org/abs/2610.31510)

**<font color=#1a73e8>作者：</font>** Yun-Chen Cheng, Chih-Pin Tan, Tzu-Hung Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Piano2Pop, a music-expansion task that transforms piano MIDI into instrumental pop productions. Enabled by recent advances in music generation and polyphonic music transcription, our pseudo-supervised approach conditions a pretrained flow-matching model on piano rolls without aligned piano-pop supervision. We train on synthetic piano-instrumental pairs derived from pop recordings, comparing pair-free transcription, including function-selective (FST) and register-density (RDA) augmentations, with a pair-supervised piano-cover generator as pseudo-demo sources. On 476 testing real-world piano-cover/pop pairs, the pair-supervised approach achieves the best Frechet Audio Distance, Accompaniment Prompt Adherence, and spectral shape on real-piano inputs, while FST mitigates piano-heavy outputs in pair-free training and remains a promising alternative. All fine-tuned systems significantly outperform the zero-shot baselines, which suggests a role for task-specific modeling.

---


### 191. [Beyond Causal Masks: Auditing and Localizing Hidden Future-Token Leakage in Adaptive Sequence Models](https://arxiv.org/abs/2610.31522)

**<font color=#1a73e8>作者：</font>** Huiting Liu, Jinsong Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hidden future-token leakage can create false architectural gains: an autoregressive model may appear substantially better under teacher-forced evaluation while its free-running generation deteriorates. We investigate this failure in an adaptive residual-routing decoder whose sequence-level routing summary exposes prefix positions to future tokens despite a correct causal attention mask. An anomalous 24-layer checkpoint reduces validation loss from the baseline's 3.5958 to 1.4259, yet it fails a prefix-invariance audit and has substantially higher reference-model perplexity during generation. Layer-wise diagnostics and implementation inspection trace the violation to a full-sequence summary broadcast through the dynamic routing-query path. Two independently trained 12-layer causal repairs eliminate detectable leakage and return validation loss and reference perplexity to the control scale, removing the large apparent advantage. As diagnostic tools, we use the established prefix-invariance contract, maximum prefix-output discrepancy (LeakScore), complementary behavioral metrics, and layer-wise profiles. Supporting experiments cover six synthetic implementation pairs spanning five module families, clean pretrained controls, controlled fault injection, and cache consistency across numerical precisions. These results illustrate how hidden future-token access can produce misleading claims of architectural progress and why lower teacher-forced loss should be interpreted together with whole-model causal checks and free-running evaluation.

---


### 192. [Diffusion-Based Synthesis of Complete 3D Biparametric Prostate MRI](https://arxiv.org/abs/2610.31523)

**<font color=#1a73e8>作者：</font>** Claudia Giardina, Montse Pardàs, Verónica Vilaplana  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic biparametric MRI (bpMRI) may help alleviate the limited availability of large and representative prostate MRI datasets for deep learning applications. In this work, we present a conditional 3D diffusion framework for anatomy-conditioned synthesis of complete prostate bpMRI from anatomical masks. The framework supports sequential synthesis, in which T2w and diffusion modalities are generated by separately trained models, and joint synthesis, in which all bpMRI modalities are generated simultaneously within a single model. Five configurations were trained using PI-CAI, FastMRI Prostate, and PROSTATEx datasets to investigate different conditioning schemes, target modalities, and synthesis strategies. Evaluation using distribution-based metrics, paired-image similarity, and qualitative assessment demonstrated the feasibility of both synthesis pathways. Joint synthesis achieved competitive distributional fidelity while generating complete bpMRI, whereas direct synthesis of ADC and computed high-b-value DWI outperformed their derivation from synthetic diffusion-weighted images.

---


### 193. [LACToS: Local Anomaly Detection via Conditional Typicality of Superpixels](https://arxiv.org/abs/2610.31538)

**<font color=#1a73e8>作者：</font>** Jihoon Hong, Alireza Kheirandish, Rohan Sanda 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Local anomaly detection is the task of identifying spatially confined anomalous or out-of-distribution (OOD) regions within an otherwise in-distribution (ID) image. Most existing methods are designed for a specific context, with a strong focus on industrial defect detection, where they achieve excellent performance on well-established benchmarks. However, we observe that these methods can exhibit significant performance drops in other contexts, especially when the inlier distribution is multimodal. To account for this inlier complexity, we propose LACToS, a principled local OOD detection method based on statistical typicality and made tractable through two innovations: (i) grouping pixels into superpixels and (ii) using a computationally efficient proxy to estimate typicality. We evaluate LACToS across three diverse applications spanning medical imaging, human faces, and X-ray security screening. LACToS performs more robustly than prior methods across these benchmarks. The code is released here: this https URL.

---


### 194. [PYTHIA, a transferable machine learning framework for simultaneous defect and adsorption site optimization](https://arxiv.org/abs/2610.31539)

**<font color=#1a73e8>作者：</font>** Ioannis Kouroudis, Zhaosu Gu, Poonam 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning has permeated material optimization, providing high value. Nevertheless, its re- liance on a high number of samples limits its applicability to relatively explored material families. In this paper we extend the applicability of machine learning to novel and understudied materials through the PYTHIA (Probabilistic Yet Transferable Hierarchical Interaction Architecture) framework. Pythia utilizes two of the most powerful machine learning concepts, foundational models and transfer learning. We employ a complex foundational model trained on a large dataset of chemically similar molecules, on a target that is physically close to our prediction target. Then, we freeze the weights and perform subspace alignment with the use of a transformer layer and add uncertainty quantification with gaussian processes. These two layers can be trained on a limited dataset yet allow us to leverage the gained knowl- edge and the studied materials and complex architectures. The resulting model is used as a surrogate for a Bayesian Optimization scheme. To showcase the robustness of the framework, we applied it to the investigation of adsorption and defect optimization of two distinct systems. Not only were we able to correctly and efficiently identify the optimal adsorption sites of even complex a

---


### 195. [Shift-aware score transport for privacy auditing without retraining](https://arxiv.org/abs/2610.31549)

**<font color=#1a73e8>作者：</font>** Yaohong Yang, Gauri Pradhan, Qi Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Privacy auditing empirically assesses privacy leakage by using membership inference attacks to establish lower bounds on privacy loss. We consider an observational auditing setting in which the auditor cannot insert canaries, control data inclusion, or retrain the target model, and must instead rely on fixed sets of known members and non-members. This setting is relevant for large deployed models or when retraining is restricted by computational or access constraints. In this case, non-members available for auditing may differ in distribution from the training data, causing membership-inference scores to be skewed due to the distribution shift. We address this problem by estimating the counterfactual in-distribution non-member score distribution using the available out-of-distribution (OOD) non-members. Our proposed method learns the relationship between data representations and membership-inference scores from OOD non-members and transports it to the target covariate distribution. Because this transport may become unreliable under extrapolation or imperfect conditional invariance, we further introduce a conservative correction calibrated directly to the nominal transported privacy level. We construct controlled calibration tasks from the available non-member data to estimate how representation-space displacement inflates the audit, and use this estimate to correct the transport-induced audit error. Across multiple datasets with distribution shifts, our method yields substantially more stable privacy estimates while retaining tighter lower bounds than baselines.

---


### 196. [Fine-Grained Analysis of Catastrophic Forgetting in Continual Learning via Algorithmic Stability](https://arxiv.org/abs/2610.31551)

**<font color=#1a73e8>作者：</font>** Guodong Zheng, Yan Sun, Peng Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding catastrophic forgetting, in which learning new tasks degrades performance on previously learned tasks, remains a fundamental challenge in continual learning (CL). Existing theoretical analyses often rely on specific model or task structures and offer limited insight into how iterative optimization affects forgetting. To address this gap, we develop an algorithmic stability framework for expected population forgetting under SGD without prescribing a particular model architecture. Specifically, we decompose forgetting into intra-task and cross-task generalization gaps and empirical forgetting. To bound the generalization gaps, we track how a sample perturbation affects updates within a task and propagates through subsequent tasks. We consider constant, intra-task decaying, and continuously decaying learning-rate schedules. Comparing the two decaying schedules allows us to characterize how restarting learning-rate decay at task boundaries affects the propagation of historical sample perturbations. For empirical forgetting, we derive bounds for all three schedules by retaining cumulative gradient alignment along the optimization trajectory, without requiring convexity. Combining these results yields upper bounds on expected forgetting that capture the effects of training set size, the number of updates per task, the total number of tasks, learning-rate schedules, and cumulative gradient alignment. Finally, we conduct experiments on Split CIFAR-100 and Split MiniImageNet to examine the empirical implications of our theoretical findings.

---


### 197. [Squaring-the-Sphere: Distortion-Free and Seamless Panorama Generation via CubeAtlas](https://arxiv.org/abs/2610.31565)

**<font color=#1a73e8>作者：</font>** Xuhui Zuo, Chenjie Cao, Tengfei Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating 360-degree panoramas requires both local perspective fidelity and global spherical continuity. Existing representations face a trade-off: equirectangular projection (ERP) enables seamless panorama modeling but suffers from severe distortion and a domain gap to pre-trained image generators, whereas cubemaps preserve perspective geometry but often produce inconsistent faces and visible seams. We present Squaring-the-Sphere, a panoramic image generation framework built on a novel representation CubeAtlas, which unfolds all cubemap faces into a single compact canvas. By arranging orientation-aligned, rotated polar regions alongside the equatorial faces, this representation preserves the perspective geometry of cubemaps while organizing the cross-face relationships required for seamless panorama assembly. It further enables a pretrained diffusion transformer to model the complete panorama jointly in a single pass, without altering the backbone architecture or positional encoding. While CubeAtlas has a token count comparable to ERP, its structured layout makes many dense attention interactions unnecessary. We therefore introduce a layout-aware sparse attention mask that preserves the interactions required for panorama continuity while removing geometrically irrelevant token pairs. As a result, CubeAtlas achieves better quality than ERP modeling with lower attention computation. Furthermore, we introduce a training-free super-resolution technique and a fusion scheme that enhance fine details in distortion-free perspective space before achieving the final ERP panorama. Experiments on various benchmarks demonstrate that our method improves geometric fidelity, cross-view consistency, and high-resolution visual quality over previous methods.

---


### 198. [Action Learning for Scientific Simulations](https://arxiv.org/abs/2610.31585)

**<font color=#1a73e8>作者：</font>** Sarah Liaw, Yuanqi Du, Yilun Du  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding and controlling how systems evolve is central to science and engineering, where many problems require reasoning about complete trajectories. Existing approaches typically learn local dynamics or generate trajectories, but objectives constructed from individual transitions can miss dependencies across time, while generative models do not necessarily provide a tractable objective for evaluating and optimizing arbitrary paths. We study $\textit{action learning}$, the problem of recovering a stochastic action from trajectory observations, yielding a common objective for reasoning about dynamical systems. We introduce $\textbf{LEAP}$ ($\textbf{L}$earned $\textbf{E}$nergy on $\textbf{A}$ction $\textbf{P}$aths), which anchors the unknown action to a tractable reference process and learns the remaining correction by comparing observed trajectories with reference trajectories. This construction yields a differentiable objective on path space that can capture both local dynamical structure and nonadditive dependencies across time. Once learned, the same action can be flexibly reused for path ranking and inference, mechanism steering, constrained optimization and sampling. Across stochastic physical systems, many-body orbital dynamics and molecular simulations, LEAP recovers underlying dynamics, captures dependencies across time and enables transfer across inference objectives and physical conditions. We show that $\textit{action learning}$ is a promising framework for turning trajectory observations into reusable objectives for scientific inference and control.

---


### 199. [Beyond Best-of-$k$: Prior-Consistent DAPS for Ambiguous Nonlinear Inverse Problems](https://arxiv.org/abs/2610.31592)

**<font color=#1a73e8>作者：</font>** Merve Kocabas, Benjamin A. Burns, Andreas Geiger 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have become strong priors for solving inverse problems. However, nonlinear inverse problems such as phase retrieval remain challenging when multiple measurement-consistent solutions are distinguishable only by the prior; we call such measurements ambiguous. Existing diffusion-based samplers rely on local approximations during reconstruction. For an ambiguous measurement, these approximations can allow measurement guidance to favor a measurement-consistent mode that is close to a prior-supported mode but is itself not supported by the prior. Evaluation often masks this type of failure by reporting the best-of-$k$ runs, where the best is selected by comparison to the ground truth. We introduce Prior-Consistent DAPS (PC-DAPS), a variant of Decoupled Annealing Posterior Sampling (DAPS) designed to address this failure case by maintaining multiple candidate solutions within a single sampling run. As annealing noise decreases, PC-DAPS prunes and replaces weaker candidates according to their prior consistency, without any ground-truth access. PC-DAPS reduces the incidence of prior-inconsistent samples and improves sample quality on nonlinear inverse problems while preserving sample quality and diversity on linear inverse problems.

---


### 200. [CRANE: Post-Hoc Counterfactual Retrieval for Multimodal Classifiers](https://arxiv.org/abs/2610.31594)

**<font color=#1a73e8>作者：</font>** Franco Rugolon, Ioanna Miliou, Panagiotis Papapetrou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Counterfactual explanation methods have been introduced for unimodal settings, with dedicated frameworks for tabular, timeseries, text, and image data, yet no post-hoc method has been designed for classifiers that learn from multimodal inputs. Existing explainability methods for multimodal classifiers apply modality-specific attribution independently to each input, which fails to yield coherent explanations and does not transfer to arbitrary pre-trained multimodal architectures. To address these shortcomings, we present CRANE (Counterfactual Retrieval via Agnostic Nearest-neighbour Explanations), the first post-hoc, model-agnostic framework for nearest-neighbour multimodal counterfactual generation that retrieves real training examples from the target class as candidate explanations, ensuring plausibility by construction. Across four heterogeneous datasets and three fusion strategies, we show that Multimodal Consensus Retrieval (MC-R), which intersects per-modality neighbour sets to identify instances jointly close to the query in every modality, emerges as the strongest multimodal strategy, achieving the best or joint-best outcome on three of four datasets while grounding every explanation in the joint training distribution. Unimodal strategies remain competitive when a single modality dominates the decision boundary.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-211](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
