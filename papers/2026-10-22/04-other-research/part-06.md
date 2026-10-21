# 📦 其他研究 | 2026年10月22日

> 本类共 **288** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-288**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-288**

---

### 251. [CNN-based classifier for subject-independent MBTI Extraversion/Introversion preference classification from short-time EEG signals](https://arxiv.org/abs/2610.28442)

**<font color=#1a73e8>作者：</font>** Filip Postepski, Grzegorz M. Wojcik  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study examines whether short, minimally preprocessed EEG segments contain sufficient information to distinguish between individuals classified as extraverted or introverted according to the Myers--Briggs Type Indicator (MBTI). EEG recordings from 50 participants were divided into 4-s segments and analyzed using a subject-independent nested 5-fold cross-validation procedure to compare EEGNet, EEGProgress, and a newly proposed compact convolutional architecture, SSCNet. SSCNet achieved the highest mean accuracy (0.6481), AUC (0.7063), and F1-score (0.6276). The proposed architecture also showed the lowest variability across folds. SSCNet demonstrated the best computational efficiency, with the shortest median training epoch time and the highest training throughput despite having a similar number of trainable parameters to EEGProgress. The results suggest that MBTI Extraversion--Introversion preferences may be moderately predictable from short time-domain EEG segments without manual spectral feature extraction, while highlighting the importance of subject-independent validation and computationally efficient model design.

---


### 252. [Toolflation: Seller Agents Distort Tool Markets Through Spontaneous Generative Engine Optimization](https://arxiv.org/abs/2610.28454)

**<font color=#1a73e8>作者：</font>** Zhenwei Tang, Di Bai, Jintao Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agents are starting to sell to other agents. Seller agents write the listings of tools, services and products, and buyer agents read these listings when they choose what to use. We show that seller agents told only to be selected more often practice generative engine optimization on their own, and that this distorts the market for sellers and for buyers. We build tool markets from real data tools on Amazon and Instagram and run every tool on every question, so we know which tools can answer each question. Under all five production models we test, sellers rewrite their descriptions to claim more and more fields, including fields that their tools return for fewer than half of the targets. We call this process toolflation. Nothing in the market limits it, and how far it goes depends on the model, as the number of claims that contradict the sellers' own evidence differs by an order of magnitude between models. Toolflation shifts the buyers' choices between sellers, and the most capable tool loses share in seven of the ten combinations of seller model and platform. Under four models, the choices stay with capable tools and buyer agents keep their task success. Under the fifth, sellers copy one another until the descriptions no longer tell the tools apart. Buyer agents then pick tools by their position in the list, tools that answer almost nothing win a quarter to two fifths of the choices, and task success falls from 89% to about 30% on Amazon, close to random choice, and from 77% to 40% on Instagram. The sellers did only what their vendors asked, and the cost fell on buyers they never dealt with. We therefore argue that honesty toward third parties under competition is part of safety alignment, and that models should be tested as sellers before they are deployed as sellers.

---


### 253. [LocaLeJEPA: Maximum Entropy Representations under Geometric Priors](https://arxiv.org/abs/2610.28458)

**<font color=#1a73e8>作者：</font>** Kartik Tandon, Alessio Borgi, Pavel Snopov 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Joint-Embedding Predictive Architectures (JEPA) offer an appealing approach to self-supervised learning, but are typically prone to representation collapse. LeJEPA resolves this by introducing a theoretically grounded distribution-matching objective that drives the embedding towards an isotropic Gaussian. However, this approach is fundamentally tied to Euclidean assumptions, and its global target does not reflect domain-specific geometric priors, such as the use of non-Euclidean embedding geometries, e.g., equivariant CNNs or hyperbolic ViTs. We thus introduce LocaLeJEPA, a framework motivated by a manifold-theoretic reformulation of LeJEPA's entropy-maximization property. The accompanying LocaLeReg, a novel locally Euclidean distribution-matching regularizer, enables a stable and scalable implementation of the LocaLeJEPA framework. We then perform extensive experiments in the vision setting on models trained on ImageNet-1K. LocaLeJEPA significantly outperforms LeJEPA when paired with hyperbolic ViT-S/8 and equivariant ResNet-50 backbones, and also with ordinary Euclidean ViT-S/8 and ViT-L/14 backbones. This holds both in terms of linear and k-NN classification performance on ImageNet and on a series of downstream tasks tested. We view the LocaLeJEPA formalism as a principled approach to the JEPA paradigm that better respects intrinsic data geometry while also accommodating generalizations to exotic embedding geometries. Code available at this https URL.

---


### 254. [Beyond Trajectory Statistics: Community-Consistent Human Mobility Generation via Evolving User-Location Graphs](https://arxiv.org/abs/2610.28467)

**<font color=#1a73e8>作者：</font>** Bo Liu, Tong Li, Jiapeng Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human mobility data are fundamental to Web-based location services and broader urban applications, and mobility generation provides synthetic trajectories when real data are costly or inaccessible. Although recent mobility generators have incorporated collective mobility patterns, they primarily focus on individual trajectories and aggregate population dynamics, leaving evolving community structures formed by user-location interactions insufficiently modeled. In this paper, we study community-consistent human mobility generation. To this end, we formulate mobility generation as the generation of dynamic user-location graphs to model community structures and propose MOTION, a Multi-agent framework for cOmmuniTy-consIstent human mObility geNeration. MOTION consists of user agents, location agents, and a global manager agent. MOTION first detects coherent communities from historical mobility using the Leiden algorithm and extracts community-conditioned interaction priors to guide the generation process. Guided by these priors, the user agents plan mobility, search destination candidates, and infer user movements from the individual view. In parallel, selectively activated location agents infer likely user arrivals from the community view. The manager coordinates both views, diagnoses interactions causing deviations, and attributes targeted reflection signals to revise user decisions, location attraction, and source-user selection. Experiments on two real-world datasets show that MOTION outperforms baselines by at least 4.05% across reported metrics of individual trajectories, population and flow distributions, and community and graph structures. Further analyses confirm its robustness, privacy preservation, and downstream utility. The code is available at this https URL.

---


### 255. [Answering in the User's Variety: Calibrated Accommodation Pairs for Post-Training](https://arxiv.org/abs/2610.28474)

**<font color=#1a73e8>作者：</font>** Zhizhuo Kou, Heming Li, Jian Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> People adapt how they talk to the person in front of them. However, chat models tend to respond in Standard English regardless of the dialect used by the user. A uniform answer can hide whether training treats these users alike, and output audits cannot tell as well. We trace how each post-training stage, from supervised fine-tuning (SFT) to preference optimization (DPO) and reinforcement learning, changes a model's tendency to match the user, and read what each update prefers from two content-matched replies, one matching the user and one not. Across 10 open model lineages, post-training standardizes replies to every informal cue, yet after adjusting for how likely each reply already was, the DPO update still favours matching British and Australian spelling over AAE and Singlish on 10 lineages, and models still produce AAE features when asked. We then introduce calibrated accommodation pairs (CAP), preference data that reward matching users' dialect density while preserving Standard English for Standard-English users. On a fully open model, CAP raises convergence on features it was not trained on without a detectable increase in dialect for Standard-English users or a cost in instruction following. In contrast, one-sided pairs reach a similar gain only by overshooting the user and imposing dialect. Our findings show that uniform replies can hide selective updates and audits should read the update as well as the output. Code: this https URL.

---


### 256. [Exploring Temporal Context-Aware Physical Grounding in Latent World Models](https://arxiv.org/abs/2610.28483)

**<font color=#1a73e8>作者：</font>** Yilei Man, Yang Chen, Jingcai Guo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learning latent dynamics is fundamental to building action-conditioned world models for planning. Among existing families, Joint Embedding Predictive Architectures (JEPAs) offer a natural framework by modeling transitions directly in latent space rather than at the pixel level. However, two issues remain in JEPA-based world models: (i) physical grounding lacks explicit aggregation of temporal context and (ii) action planning always overly relies on generic sampling distributions. To this end, we propose $\mathcal{G}$-JEPA, which incorporates temporal context into physical grounding for latent world models and couples the learned models with prior-guided action planning. Specifically, during learning, we incorporate a shared causal temporal module that aggregates temporal context within observation and prediction sequences under physical state supervision, grounding both in task-relevant physical states. When planning, we further introduce action inference through stepwise conditioning of a generative action distribution on the current and goal latent representations together with their evolving discrepancy, yielding anchored proposals that guide model-based online refinement. Together, physical state supervision guides temporal representation learning, while the action prior guides search through the learned world model. Experiments demonstrate improved planning performance on manipulation tasks, including tasks with increasing temporal separation between initial and goal observations. Code is publicly available at this https URL.

---


### 257. [Proof-Carrying Contracts: Commitments AI Agents Cannot Break](https://arxiv.org/abs/2610.28484)

**<font color=#1a73e8>作者：</font>** Carlo Ciliberto, Alessandro Rudi, Enrico Tassi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents increasingly act on behalf of people or other agents, purchasing services, exchanging information and delegating work. What an agent must respect is written in instructions, policies or agreements, but text alone cannot make it comply. It may make mistakes, be redirected by what it reads, or pursue different interests. For an economy of such agents to function, parties need agreements they can rely on without inspecting or trusting one another's agents. We introduce Proof-Carrying Contracts (PC2), a framework for making agreed constraints enforceable throughout an agent's interactions with a system. Before a requested operation can run, the agent must supply a machine-checkable proof that it preserves the agreed constraints in every case allowed by its model. An execution system called the Airlock checks the proof and controls access to the operation. The parties specify the conditions to preserve, while the agent supplies the reasoning needed to justify its decisions and remains free to adapt its strategy. This avoids having to design a separate permission policy and prove that every decision it permits is safe. We prove that the constraints hold at every instant during execution, even for an adversarial agent, and identify when this implies safety in the world. Reusable capability modules provide tools and guarantees from which contracts can be constructed. PC2 provides a foundation for an agent economy whose agreements protect both those delegating work and those carrying it out.

---


### 258. [Geometry-Agnostic Data-Driven Discovery of Extreme Scenarios](https://arxiv.org/abs/2610.28487)

**<font color=#1a73e8>作者：</font>** Angeline Hu, Ava K. Tse, Kaitlyn S. Yasumura 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce a two-stage data-driven neural framework for discovering dynamically admissible extreme scenarios. Rather than assuming prior knowledge of the governing equations, the first stage infers the effective dynamical constraints directly from observational data. When the underlying physical system possesses suitable symmetries, the learned dynamics can be represented in a geometry-agnostic form, independent of any fixed grid, coordinate system, dimensionality, and intrinsic curvature. In the second stage, a physics-informed neural-search uses this learned dynamics to uncover rare, high-impact coherent structures that may not have appeared in the original observations. We demonstrate this framework through representative examples of increasing dimensionality and geometric complexity. Starting from a traditionally learned Duffing dynamics, we find a homoclinic pulse as a plausible localized extreme scenario. Next, since the same equation also appears in the stationary nonlinear Schrodinger system, with the coordinate interpreted as space instead of time, this pulse becomes a standing soliton. We then retrain the first stage using a geometry-agnostic neural representation, enabling the learned dynamics to be lifted to higher-dimensional space to obtain higher-dimensional solitary profile, known as Townes soliton. Finally, with a Liouville system, we demonstrate that dynamics learned from data on a (1+1)-dimensional Lorentzian quasi-manifold can be transferred to a (2+0)-dimensional Euclidean manifold to identify an instanton. Our approach can be applied to other coherent spatiotemporal structures, including kinks, rogue waves, compactons, peakons, and potentially even singularities, with applications in risk analysis, nonlinear forecasting, and anomaly detection.

---


### 259. [Learning from Automatic 3D Gaussian Splatting Edits for Online Bayesian Scene Change Detection](https://arxiv.org/abs/2610.28490)

**<font color=#1a73e8>作者：</font>** Changrui Zhu, Simon Julier  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online scene change detection requires integrating incoming observations to determine which regions have changed relative to a reference scene. We update change beliefs as new images arrive using generalised Bayesian evidence fusion. However, the prior probability of change and evidence models are unknown beforehand, and numerical Bayesian inference can be costly. We address these challenges by learning offline from automatic edits to a reference 3D Gaussian Splatting (3DGS) model. These edits generate labelled training views without manual annotations. Together with unchanged reference observations, they provide supervision for learning scene-specific evidence models and estimating the effective pixel prior and response statistics. Online prediction combines current evidence with historical support, while closed-form local Bayes factors, parameterized by the learned response statistics, update an accumulated 3D Gaussian field. Object-guided refinement produces the final change masks. Our method achieves state-of-the-art accuracy on PASLCD and CCS3D, with $67.64\%$ and $75.82\%$ mIoU, respectively. On PASLCD, the complete pipeline runs at $17.2$\,FPS over complete query sequences, the fastest among the evaluated online methods.

---


### 260. [Model- and Layer-Level Closed-Loop Forecasting with SSM-Based Spiking Neural Networks](https://arxiv.org/abs/2610.28495)

**<font color=#1a73e8>作者：</font>** Erik Stolt, Sanja Karilanova, Ayca Ozcelikkale  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep State-Space Models (Deep SSMs) have shown promising performance and computational benefits in processing of time-series data with complex temporal dependencies. Spiking neural networks (SNNs) constitute a biologically inspired class of deep SSMs, where computing blocks communicate through spikes, discrete single-bit events rather than continuous activation functions. A particularly important task in time-series processing is forecasting, i.e. predicting future values of a sequence from past observations alone. However, how to best perform forecasting with SNNs is an open question, where the standard autoregressive nature of the data processing with SNNs requires values that are not available during the forecasting phase. In this article, we address this challenge. We explore two closed-loop forecasting strategies, in which the network's own generated values are fed back into the network as if they were observed past values: (i) model-level and (ii) layer-level closed-loop forecasting. We evaluate these approaches on the ETT-small datasets, a standard benchmark for time-series forecasting, under both spike-based and continuous activation functions. We compare the proposed closed-loop approaches against state-of-the-art methods such as SpaceTime, as well as the zero-masking baseline in S4. Both of the proposed approaches perform comparably to or better than zero-masking with S4, and in most cases match SpaceTime. These findings highlight the trade-off between continuous and low-bit quantized activations, and demonstrate that the proposed Deep SSM architectures provide a competitive framework for forecasting.

---


### 261. [ECG for laboratory values:A comprehensive physiological and technical analysis](https://arxiv.org/abs/2610.28507)

**<font color=#1a73e8>作者：</font>** Walentin Palanchuk  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Laboratory measurements are essential for clinical decision making but typically require invasive blood sampling. Recent research suggests that ECG recordings may contain information beyond cardiac rhythm and provide information related to laboratory values. This thesis investigates NT-proBNP prediction from ECG recordings and patient metadata using a multimodal deep learning framework, while considering the physiological plausibility of ECG-based prediction. It also compares a 1-lead configuration using lead II with the corresponding 12-lead configuration. Additional experiments on glucose, hemoglobin, and potassium are presented in the appendix.
Regression, binary classification, and three-class classification experiments were conducted using MIMIC-IV, with the three-class task based on clinically established thresholds. The 12-lead configuration consistently achieved better performance. Regression reached a mean absolute error of 534.98 pg/mL for 1-lead and 514.27 pg/mL for 12-lead. Binary classification achieved AUROCs of 0.849 and 0.876, respectively, while three-class classification achieved macro-averaged AUROCs of 0.738 and 0.752.
The results indicate that precise NT-proBNP regression remains challenging, whereas broader concentration ranges can be classified more effectively. The findings are consistent with the physiological hypothesis that ECG characteristics and NT-proBNP concentrations reflect shared cardiovascular processes. ECG-based NT-proBNP prediction may therefore provide complementary information, particularly for classifying broader concentration ranges. However, laboratory measurements remain necessary, and validation on independent datasets is required.

---


### 262. [Deep Learning-Based Road Lane Quality Assessment from Egocentric Dashcam Video](https://arxiv.org/abs/2610.28508)

**<font color=#1a73e8>作者：</font>** Shaif Chowdhury, Akhila Yeruvasu, Moshiur Rahman Tonmoy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable lane markings are important for both human drivers and automated driving systems, but their condition is still commonly assessed through manual inspection. Existing autonomous-driving datasets primarily support lane detection and scene understanding and usually lack maintenance-oriented labels for lane-marking visibility, continuity, or degradation. In this study, we present a geo-referenced smartphone dashcam dataset and baseline framework for lane-marking quality assessment. The dataset contains 63,839 road-facing frames collected across South Texas using a GPS-enabled dashcam application. A subset of 3,339 frames is matched with OpenStreetMap-derived lane-count labels, which are used as weak supervision for lane-count regression and map-consistency evaluation. We propose three lane-quality measures: Contrast Stability Index (CSI), which captures lane-background contrast using Laplacian responses; Line Continuity Ratio (LCR), which estimates structural continuity using edge and Hough-line evidence; and Regression Lane Confidence Score (RLCS), which measures agreement between predicted and map-derived lane counts on matched frames. The baseline prediction models attained strong performance, with CSI (MAE $0.039$, $R^2=0.97$) and LCR (MAE $0.093$, $R^2=0.84$). Notably, CSI and LCR are no-reference, segmentation-derived quality metrics that can be computed without dense human labels. In a pilot validation using 50 human-ranked images, these proposed lane-specific metrics show stronger rank agreement with human lane-quality ordering (e.g., Spearman's $\rho=0.7316$ and Kendall's $\tau=0.5472$ for LCR) than general image-quality measures such as PSNR, SSIM, BRISQUE, NIQE, and LPIPS. We believe the dataset, metrics, and baseline provide an initial step toward scalable, low-cost, location-aware lane-marking quality assessment. Data and code: this https URL

---


### 263. [GraphCast-Mamba: Learning Non-Markovian Corrections for Weather Forecasting](https://arxiv.org/abs/2610.28512)

**<font color=#1a73e8>作者：</font>** Ilya Vilkoviskiy, Liang-Hong Mo, Suozhi Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unresolved atmospheric processes can introduce history dependence beyond the short input windows used by many weather forecasting models. We introduce GraphCast--Mamba, which augments a frozen, pretrained $1^\circ$ GraphCast backbone with a trainable Mamba correction branch combining graph message passing and Mamba layers. The branch retains a temporal memory state across successive six-hour forecast steps, learning corrections informed by temporal context beyond GraphCast's two-frame input. Training is confined to the correction branch, using ERA5 data from 2015--2021. After 2,500 optimizer updates, including warm-up, the selected model achieves substantial improvements relative to the uncorrected GraphCast backbone. It reduces the GraphCast loss (normalized weighted mean-squared error; MSE) by 14.42% when aggregated over the full ten-day forecast and by 21.66% at day 10 (240 h after forecast initialization). At this final forecast lead time, root-mean-square error (RMSE) decreases by 7.09--14.60% across all 11 evaluated variable groups, spanning temperature, wind, pressure, geopotential, specific humidity, and precipitation. These results demonstrate broad improvements in ten-day weather forecasts through a short correction-training schedule while retaining the pretrained backbone.

---


### 264. [Touch-JEPA: Tactile Representation Learning from Hand-Object Video with Limited Tactile Supervision](https://arxiv.org/abs/2610.28519)

**<font color=#1a73e8>作者：</font>** Minseong Kweon, Qiao Feng, Yiming Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding contact and tactile magnitude in hand-object interaction is a key step toward physically intelligent systems, yet learning such representations is limited by the cost and restricted coverage of tactile measurements. We present Touch-JEPA, a framework for learning tactile representations from hand-object videos with limited tactile supervision. We first introduce a self-supervised pretraining objective that learns from video alone without tactile supervision. Using video-derived hand geometry, Touch-JEPA predicts masked visual features at corresponding hand-surface locations from spatial and temporal context, encouraging the representation to capture latent contact dynamics. We then extend this formulation to joint representation learning, where masked prediction is applied to all videos while tactile supervision is available only for a labeled subset, grounding the shared representation in measured contact and magnitude. With self-supervised pretraining alone, simple supervised readouts on frozen Touch-JEPA features outperform supervised baselines in contact discrimination and tactile magnitude estimation across three human-hand benchmarks, and transfer to robotic hands without robot tactile training data. Joint learning with limited tactile supervision further improves contact and magnitude estimation on the human-hand benchmarks. Together, these results show that hand-object video can provide scalable self-supervision for tactile representation learning, while limited tactile measurements provide complementary physical grounding.

---


### 265. [Latent Bridge: From Video Latents to 3D Geometry via Feature Alignment](https://arxiv.org/abs/2610.28521)

**<font color=#1a73e8>作者：</font>** Shuai Zhang, Zhanpeng Ouyang, Zhengqing Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation and feed-forward 3D reconstruction typically use separate representations, requiring RGB decoding and visual re-encoding to recover geometry from generated latents. We propose Latent Bridge, which connects video generative latent spaces with geometric feature spaces to directly predict 3D geometry from video latents. We develop representation-specific bridges for Wan2.1 and V-RAE, enabling feed-forward prediction of cameras, depth, and 3D point clouds without the intermediate RGB pathway. Each bridge is trained on RGB videos through feature distillation, while the video encoder and geometry model remain frozen. Training requires neither ground-truth geometry nor execution of the downstream geometric aggregator or prediction heads. At inference, the same video latents support both RGB decoding and geometry prediction. The same trained bridge can be reused for image-to-video and text-to-video generation within the same video latent space, without bridge retraining. Experiments on Co3Dv2 and WildRGB-D demonstrate competitive geometric reconstruction quality, efficient end-to-end generation and reconstruction, and faster latent-to-geometry decoding, highlighting latent alignment as a practical and reusable interface between video generation and 3D reconstruction. Our code is available at: this https URL.

---


### 266. [Copyright Leakage Detection in AI Generated Videos](https://arxiv.org/abs/2610.28524)

**<font color=#1a73e8>作者：</font>** Shaif Chowdhury, Moshiur Rahman Tonmoy  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation models can create realistic-looking video footage from images and text prompts. Some of the recent advances have raised concerns about the reproduction of copyrighted visual content. However, copyright leakage detection in generated videos remains largely unexplored.
In this paper, we introduce a new benchmark data set for copyright leakage detection, comprising 50 copyrighted concepts, each with 5 images. For each concept, we have 5 videos created using the image+prompt video generation model and the prompt-only video generation model. Following that, we develop an AI toolset based on a contrastive retrieval framework that formulates copyright leakage detection as a video-to-image retrieval problem by matching aggregated video frame embeddings against a database of copyrighted image embeddings. Our method uses a single similarity threshold and retrieves the most similar copyrighted reference as supporting evidence.
We conducted experiments showing strong retrieval and detection performance, achieving 99.6\% detection accuracy with only a single false negative. These results show the effectiveness of the retrieval-based method for scalable and explainable copyright leakage detection in AI-generated videos. Data can be accessed publicly from this https URL and the source code for this project is publicly available at this https URL.

---


### 267. [CoGaussian: Open-Vocabulary Gaussian-based Collaborative 3D Scene Understanding](https://arxiv.org/abs/2610.28530)

**<font color=#1a73e8>作者：</font>** Om Shivam Verma, Shaya Farahmand, Lingjun Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Collaborative perception enables agents to retrieve the scene semantics and geometry beyond the field of view of any individual agent. This broader scene understanding enhances transportation safety and improves efficiency in multi-robot systems. However, existing collaborative semantic occupancy methods rely on dense 3D voxel annotations and are limited to recognizing objects within a predefined set of semantic classes. To overcome these limitations, we present CoGaussian, an open-vocabulary Gaussian-based collaborative semantic occupancy prediction framework. CoGaussian represents a scene as a set of foundation model-aligned sparse 3D Gaussians, which serve as a compact representation for communicating and fusing geometric and semantic information across multiple agents. On the Semantic-OPV2V benchmark, our method outperforms existing open-vocabulary single-agent approaches, highlighting the effectiveness of open-vocabulary collaborative scene understanding.

---


### 268. [TracePrism: Extending Semantic Trace Topics to Iterative, Encoding-Aware Trace Partitioning](https://arxiv.org/abs/2610.28532)

**<font color=#1a73e8>作者：</font>** Gennady Andrienko, Natalia Andrienko, Manuel Resinas 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Process mining typically explains an event log with a single model, clustering, or classifier fitted to all cases, although real logs often mix cases that follow different sub-processes. Trace clustering separates sub-populations, but it fixes one notion of trace similarity for the whole analysis. We propose TracePrism, which treats process discovery as iterative partitioning with three characteristics. The trace encoding is adaptive: it is chosen for each working set of remaining traces from a library of encodings, with suggestions scored for that set. The partitioning is iterative: the analyst forms a candidate group based on a rule, a dominant topic, a cluster over topic weights, or a region of an embedding, accepts it if it is coherent in both process structure and outcome, and continues with the remaining traces. Decisions are revisable and recorded: a group can be reopened under a different working set or encoding, and the findings repository keeps both the earlier decision and its revision. We implement TracePrism as an open-source prototype and demonstrate it in usage scenarios on three real-world event logs. The scenarios also revealed behavior that we had not anticipated, such as process drift.

---


### 269. [Binary Discrete Diffusion: Candidate-Set Diffusion for Logic and Planning Tasks](https://arxiv.org/abs/2610.28543)

**<font color=#1a73e8>作者：</font>** Rodrigo Casado Noguerales, Dimitri von Rütte, Bernhard Schölkopf 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion models iteratively denoise a noisy sequence of categorical data such as text, enabling any-order generation with self-correction and in-filling capabilities. This makes them promising candidates for reasoning, planning, and constrained-generation tasks like coding and math. Yet masked and uniform diffusion erase a token's identity in a single corruption event, so their noisy states cannot explicitly represent partially resolved uncertainty in which several alternatives remain plausible. We close this gap with Binary Discrete Diffusion, a family of continuous-time discrete-diffusion processes whose noisy state is a set of candidate tokens per position, represented as a binary membership vector. Binary diffusion changes candidate sets through additions and removals, allowing information to be lost and recovered gradually while the diffusion state itself represents partial uncertainty. On Sudoku-Extreme, Boxoban, and graph coloring, the symmetric formulation of binary diffusion consistently outperforms strong, well-tuned masked and uniform baselines under matched architectures and controlled training, sampling, and tuning budgets, with its largest gains on the hardest instances, while remaining competitive on language modeling (Text8, TinyStories, OpenWebText). These results support candidate sets as an effective intermediate representation for iterative reasoning and show that the corruption kernel can materially change the computation learned by the reverse model.

---


### 270. [Discount Yourself: Self-inclusive Freshness-weighted Gossip for Decentralised Learning under Client Outages](https://arxiv.org/abs/2610.28545)

**<font color=#1a73e8>作者：</font>** Qiyuan Wang, Ke Xiao, Christos Anagnostopoulos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decentralised federated learning (DFL) trains personalised models on devices that average with their neighbours rather than with a central server. Real devices, however, are often offline for hours or days, and a client returning from an outage can recover only by aggregating the models its neighbourhood holds. We observe that the stalest of these models is usually the client's own, a case that existing staleness-aware rules, which discount only the models a client receives, do not address. We formalise aggregation after an outage as estimating the state of a fully available network and derive three principles. First, the receiver must be discounted like any neighbour. Every rule that weights it at least as much as each neighbour has an error that grows without bound with the outage, whereas discounting all candidates by relative staleness keeps the error bounded. Second, staleness must be measured as inherited lag rather than age, since local training resets a model's age but not the lag it absorbed from stale neighbours. We introduce the effective lag, which tracks this quantity at the cost of one scalar per message. Third, the discount must be steep, because absorbed lag persists in every later round. These principles define Self-inclusive Freshness-weighted Gossip (SFG), a family of drop-in aggregation rules with the communication and computation of decentralised federated averaging, whose guarantees hold for the stale receiver itself. On three image benchmarks and eight outage processes, including real smartphone availability traces, the lag-based members SFG-L and SFG-Cut consistently outperform decentralised federated averaging and recent age-of-information rules, and ablations show that each principle is necessary. The analysis also explains why tuned limited merging from gossip learning is effective.

---


### 271. [OverSeer: Multi-Agent World Models Beyond What Agents See](https://arxiv.org/abs/2610.28554)

**<font color=#1a73e8>作者：</font>** Runjia Li, Kam Woh Ng, Minghao Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the success of video world models, extending them to multiple agents is difficult because it requires generating several agent-specific video streams that are consistent in time and between agents. To address this gap, we introduce OverSeer, a multi-agent world model that augments egocentric agent views with auxiliary camera views. We suggest that, by fixing the auxiliary views in space, they act as a proxy for a world-centric representation: Unlike the agents' views, which can change entirely due to a simple change in agent position, changes in the auxiliary views directly map to localized changes in the world state. We show that these fixed views substantially help the model to maintain consistency. We also show that, due to their redundant and semi-static nature, the auxiliary views can be efficiently compressed with a delta-VAE that encodes only the changes relative to a static reference image, reducing the number of tokens required to process them. Experiments in Minecraft and Doom demonstrate improved world and agent consistency, with qualitative results on real-world multi-camera captures indicating that the approach is not tied to game engines. Our compression analysis further shows that delta-VAE substantially reduces the computational overhead of auxiliary-view generation. We conclude that these fixed views provide a simple and efficient way to improve multi-agent world models.

---


### 272. [Learning Computational Structure for Sample-Efficient Prediction](https://arxiv.org/abs/2610.28555)

**<font color=#1a73e8>作者：</font>** Hangyu Zhou, Constantine Dovrolis, Stephen Mussmann  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Statistical learning in high dimensions suffers from the curse of dimensionality. Fortunately, many functions of practical interest are compositionally sparse, meaning they admit a composition of local functions, each depending on only a few variables, allowing sample complexity to depend on local arity rather than ambient dimension. Yet realizing this benefit requires exploiting hidden compositional structure, which theory does not establish for practical gradient-based training. We study this gap with CSFRBench, a controlled benchmark that hides the target's compositional computation during training but retains it for diagnosis, and find that dense networks and sparsity-based baselines leave much of that benefit unrealized. Inspired by the spatial organization of biological neural circuits, we introduce Learned Wiring (LeWi): each neuron has a learned low-dimensional embedding, only nearby neurons connect, and embeddings and weights are trained jointly. LeWi improves sample efficiency on targets with hierarchical structure, intermediate reuse, or independent modules. Across 32 additional targets generated by independently sampled computation graphs, LeWi is the most sample-efficient method not given the target graph, with 27% lower mean learning-curve area than dense networks. Dense networks perform better on targets with a single high-arity function. LeWi's representations and connectivity align with the target computation. On 17 world-model prediction tasks spanning control, navigation, and manipulation, LeWi beats the dense baseline on 16 and wins 99/119 baseline comparisons. These results show that jointly learning connectivity and weights can exploit computational structure to improve sample efficiency.

---


### 273. [Convergence of stochastic gradient descent for learning linear neural networks](https://arxiv.org/abs/2610.28561)

**<font color=#1a73e8>作者：</font>** Gabin Maxime Nguegnang, Bubacarr Bah, Holger Rauhut 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stochastic gradient descent (SGD) is the cornerstone of modern deep learning, yet its theoretical convergence properties remain poorly understood in non-convex settings. To address this gap, we study SGD dynamics in deep linear neural networks - simplified models that retain key non-convex characteristics while remaining analytically tractable. Building on recent results for gradient descent, we extend convergence guarantees to SGD under regularized squared loss. We establish almost sure boundedness of SGD iterates. Using the framework of asymptotic pseudotrajectories from stochastic approximation theory, our analysis establishes then, for both deterministic and adaptive step-size choices, convergence of SGD to the set of critical points under mild conditions (without relying on Lipschitz properties or whitened data). To our knowledge, this is the first work providing almost sure convergence guarantees for SGD in deep linear networks, bridging the gap between theoretical optimization and practical stochastic training.

---


### 274. [Asymmetric Bidirectional Predictive Dynamics in Google Search and COVID-19 Time Series: A Multi-Horizon Forecast-Error Analysis](https://arxiv.org/abs/2610.28563)

**<font color=#1a73e8>作者：</font>** Andrei Velichko, Imen Mahmoud  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online search activity is widely used as a digital trace of information seeking during epidemics, but its predictive value is often reduced to correlation, a selected lag, or a single forecast-error score. We examine eight pre-specified Google Trends-COVID-19 pairs in both directions using matched LightGBM forecasts over rolling 400-day windows and horizons of 1-14 days. Log-RMSE gain is combined with forecast-error distribution entropy (FEDE), which captures horizon-dependent changes in the signed error distribution. The resulting directional predictive signature comprises response class, RMSE effect, FEDE endpoint and early-slope responses, persistence across rolling regimes, and horizon profile. For screening candidate directions, we also introduce a relative persistence-weighted directional predictive response strength (DPRS) on a within-study 0-100 scale; 100 denotes the strongest observed response in the comparison set, not an absolute coupling maximum. The pairs show concordant, RMSE-only, FEDE-only, and mixed responses. "loss of smell" -> reported cases is accuracy-dominant, with mean log-RMSE gain 0.104 (about 9.9% equivalent RMSE reduction) and DPRS 100, whereas the reverse direction is FEDE-dominant (D_FEDE=0.048; DPRS=42). "covid test" -> positive rate is FEDE-dominant (D_FEDE=0.039; positive in 72% of windows; DPRS=98) despite negative RMSE gain, while "lockdown" -> stringency is the clearest concordant case (DPRS=78). World-level symptom/case pairs are less persistent. Thus, forecast accuracy and error-distribution dynamics are complementary, predictive effects can be direction- and metric-dependent, and forecast horizon is part of the relationship. Aggregated regime-level patterns should not be extrapolated to individual time points or interpreted as evidence of causality.

---


### 275. [The Dynamics of Collapse and Recovery in Clustered Federated Learning](https://arxiv.org/abs/2610.28565)

**<font color=#1a73e8>作者：</font>** Priyanka Sinha, Snigdhansu Chatterjee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clustered federated learning (CFL) can suffer from cluster collapse. In particular, under unfavorable initialization, early client assignments concentrate heterogeneous groups on one cluster model, which is then trained toward a pooled compromise, while another model receives no updates. Since the current models determine client routing and routing determines subsequent model updates, we formulate clustered federated learning as control of an unknown dynamical system, with cluster models as the evolving state, client routing patterns as the control input, and routing interventions as state dependent controllers. In a two group linear model, we identify an initialization region in which greedy routing makes collapse self reinforcing. We then derive finite horizon error dynamics showing how routing interventions can reverse collapse by repeatedly training the starved model, primarily with updates from its compatible group. Motivated by this condition, each client uses blocked EXP3 to choose between greedy routing and interventions that redirect updates toward unused models. Experiments show that with simpler predictors and faster specialist formation, autonomous controller selection recovers usable specialists from unfavorable starts that trap standard CFL baselines. In transformed FEMNIST, the synchronized-entry configuration with persistent commitment recovers usable specialists in settings where the autonomous controller configuration often does not. Code and scripts for reproducing the experiments and figures are available at this https URL.

---


### 276. [Continual Concept Personalization in Diffusion Models via Residual-Space Adaptation](https://arxiv.org/abs/2610.28567)

**<font color=#1a73e8>作者：</font>** Yuzhi Liu, Enis Simsar, Giulia Lanzillotta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image personalization aims to equip pretrained diffusion models with the ability to learn user-specific concepts from only a few reference images. Existing methods, however, typically train each concept independently or assume that all concepts are available simultaneously. In practical applications, concepts often arrive sequentially, requiring models to continually learn new subjects, objects, or styles while minimizing interference with previously acquired concepts. We address this continual concept personalization setting by extending residual-space adaptation to the stochastic adaptation process of pretrained diffusion models. Our work achieves the highest concept fidelity among competing continual personalization methods while maintaining near-zero forgetting. Beyond these empirical gains, the learned residual-space dynamics reveal where adaptation capacity is concentrated within the diffusion model. Restricting adaptation to the identified layers by our method preserves nearly the same performance while reducing the number of trainable parameters by up to 72\%, demonstrating that residual-space dynamics can identify the layers that contribute most to continual concept personalization and directly guide more parameter-efficient adaptation.

---


### 277. [Can a Display Be Used for Rapid LiDAR-Camera Extrinsic Calibration?](https://arxiv.org/abs/2610.28571)

**<font color=#1a73e8>作者：</font>** Zuhao Zou, Xiangcheng Hu, Jianhao Jiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> ScreenCalib enables light detection and ranging (LiDAR)--camera extrinsic calibration using an ordinary programmable display, providing known visual markers and controlled geometry while reducing dedicated target preparation. The camera observes displayed AprilTags, whereas the LiDAR measures the physical screen surface and boundary, requiring indirect cross-modal association. Display geometry introduces association ambiguities, while indoor clutter complicates extraction. ScreenCalib addresses these challenges through tag-guided display extraction, geometric hypothesis generation and refinement, and surrounding scene edges for ambiguity resolution. The single-pose mode requires only one static placement. The joint multi-pose mode combines independent static observations through cross-pose consensus and jointly refines the shared extrinsics and tag scale, reducing sensitivity to tag-size measurement errors without requiring continuous motion or inter-pose trajectory estimation. Experiments in simulation and on three different sensor platforms cover mechanical and nonrepetitive LiDARs in clean and cluttered environments. Benchmark results show that ScreenCalib outperforms competitive calibration-board-based methods in translation accuracy. Joint multi-pose refinement further reduces mean rotation and translation errors across the three platforms and improves rendered-map alignment. Evaluation across readily available displays, including cell phones, tablets, laptops, computer monitors, and televisions, further examines ScreenCalib's versatility as a practical alternative to dedicated calibration targets. The source code is available at this https URL.

---


### 278. [Continuous-Time Policy Gradient from Discrete Data: Convergence Analysis and Model-Free Algorithms](https://arxiv.org/abs/2610.28580)

**<font color=#1a73e8>作者：</font>** Martin Hernandez, Xinyan Qing, Mo Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous-time reinforcement learning seeks an optimal policy under unknown dynamics driven by stochastic differential equations using observations collected at discrete times. We develop a policy gradient framework that combines rigorous convergence analysis with learning from discrete data. We first establish a performance difference lemma and derive policy gradient formulas for randomized and parametrized policies. We then prove exponential convergence of an entropy-regularized policy flow to the regularized optimum. For discrete parametrized updates, we derive a convergence bound that explicitly separates the contributions of critic error, policy-regression error, and the learning step size. To enable learning under unknown dynamics, we integrate this framework with PhiBE, which constructs a continuous-time surrogate generator from discrete transition data. The resulting on-policy and off-policy model-free actor-critic algorithms preserve the continuous-time structure of the control problem. Numerical experiments on an entropy-regularized linear-quadratic regulator and a nonlinear wheeled robot demonstrate the performance and stability of the proposed methods with both known and data-driven dynamics.

---


### 279. [WildMAE: Structure-Aware Masked Autoencoding for Wildlife Image Reconstruction](https://arxiv.org/abs/2610.28590)

**<font color=#1a73e8>作者：</font>** Yicheng Zhang, Yujie Jin, Ke Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera-trap imagery presents substantial variation in animal appearance, illumination, background clutter, and visual degradation. Masked autoencoders (MAEs) offer a label-free framework for modeling such data through reconstruction of randomly hidden image patches. We present WildMAE, a decoder-side extension of MAE that combines local structure-aware refinement with masked-to-visible cross-attention. A zero-gated convolutional residual path introduces a two-dimensional neighborhood prior, while gated cross-attention allows masked positions to retrieve contextual information from visible-position features without replacing the original Transformer decoder. The associated training recipe progressively introduces normalized-pixel, Sobel-edge, and perceptual objectives. In the original Snapshot Serengeti study, covering 4,744 test images at 75% masking, the reported reconstruction scores were 27.90 versus 24.33 dB PSNR, 0.840 versus 0.780 SSIM, and 0.160 versus 0.320 LPIPS for WildMAE and vanilla MAE, respectively. Additional historical records document favorable average differences under four synthetic degradation conditions and describe component variants. We present the method, experimental observations, and their scope together: the retained metrics are historical protocol-dependent results, rather than a newly reproduced, harmonized comparison or a validation of restoration from genuinely unavailable pixels. WildMAE provides a practical architectural case study for combining global token mixing with spatial and targeted contextual refinement in wildlife masked-image modeling.

---


### 280. [PaPi: Parallel Picard-Duhamel Integration for Fast Neuro-Spectral Architectures](https://arxiv.org/abs/2610.28591)

**<font color=#1a73e8>作者：</font>** Arthur Bizzi, Márcio Marques, Kleyton Da Costa 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neuro-spectral architectures (NeuSA) are a class of physics-informed neural networks (PINNs) that have proven effective for solving time-dependent PDEs in the frequency domain. However, training and inference often rely on costly numerical integration of the learned vector field, typically using sequential Runge-Kutta time stepping, which limits temporal parallelism. We introduce PaPi, an integration scheme inspired by weakly nonlinear flows that enables time-Parallel inference through exponential integration and a Duhamel-Picard scheme. We show that the Duhamel-Picard iteration converges exponentially for all flows, and provide explicit error bounds that depend on how close the flow is to linear. Experiments show that PaPi accelerates training and inference by up to two orders of magnitude, achieving training times of under one second for low-dimensional PDE learning problems, while maintaining competitive predictive accuracy.

---


### 281. [Learning the 4D World through Point Trajectory Forecasting](https://arxiv.org/abs/2610.28594)

**<font color=#1a73e8>作者：</font>** Byungwoo Jeon, Sunghwan Hong, Dohyeon Kim 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable multi-view forecasting requires videos from different cameras to describe the same evolving 3D scene. To this end, we introduce Video-Point Model (VPM), a world model that conditions on multi-view video histories and a language instruction to jointly forecast future videos from arbitrary viewpoints and the 3D trajectories of persistent scene points. We extend a pretrained world model with camera-conditioned multi-view processing that integrates complementary observations across cameras, and add a trajectory head that predicts how physical points move through time. Each trajectory tracks a single point across all views, and supervising these trajectories alongside video generation therefore anchors appearance changes in every camera to a shared description of 3D motion. To support training and evaluation, we build VPM-Data, a simulation corpus pairing synchronized multi-view videos with persistent point trajectories, and VP-WorldBench, a forecasting benchmark spanning simulated and real environments. We further extend VPM to robot control by adding robot actions as a token modality in the generator. Action tokens share the point-supervised backbone and are denoised jointly with future videos, thereby grounding the policy in the same 3D-aware representation. On VP-WorldBench and existing 4D generation benchmarks, point supervision improves both video fidelity and 3D motion accuracy over a video-only counterpart, and in simulated and real-robot experiments, it also raises the manipulation success of the action-enabled model.

---


### 282. [What Do RTL Repair Benchmarks Actually Measure?](https://arxiv.org/abs/2610.28595)

**<font color=#1a73e8>作者：</font>** Yeyin Eva Zhu, Rishabh Ranawat  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> RTL repair benchmarks should measure whether a model can fix broken RTL given a specification. To this end, we construct and hash-bind RTLRepairDataset, 5,784 (broken, fixed) training pairs; RTLRepairBench, 459 held-out cases with 374 syntactic and 85 behavioral mutations; and an evaluation harness supporting simulation and formal equivalence. We then use this infrastructure to identify two measurement confounds. First, simulation and formal scoring give opposite signs for the apparent effect of providing a specification in one evaluated cohort; reset-aware rescoring attributes almost all of the simulation-formal disagreement to reset and first-cycle comparison semantics. Second, on 274 mined model failures, the specification-only minus specification-conditioned recovery point estimate ranges from -8.5 to +18.3 percentage points across six models. Thus, a conventional repair score need not isolate whether the model used the faulty RTL. We translate these findings into evaluation controls: report initialization, reset, first-cycle, and unknown-value semantics; disclose oracle coverage and undecided cases; and include a specification-only baseline. Together, the resources and audit provide both a benchmark for behavioral repair and a protocol for diagnosing what contributes to its measured score. We release the benchmark, the training set, construction code, sanitized aggregate evidence, and reproduction materials at this https URL.

---


### 283. [Neural Implicit Energy Optimization for LiDAR Mapping](https://arxiv.org/abs/2610.28598)

**<font color=#1a73e8>作者：</font>** Hrishikesh Viswanath, Md Ashiqur Rahman, Chi Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neural implicit representations provide memory-efficient signed distance field (SDF) parameterizations for large-scale LiDAR scenes, but the geometry recovered from sparse and often noisy inputs carries jitter and artifacts. Classical geometric optimization techniques resolve such artifacts with surface energy functionals, whose minimizers correspond to smooth surfaces. Motivated by this principle, we formulate neural LiDAR mapping as the optimization of energy functionals over the parameter space of neural implicit representations. Specifically, we regularize the signed distance field with an energy functional defined on the shape operator of its level set, which represents the curvature of the surface, thus encouraging smoothness along the surface. This adapts classical geometric priors to the scale of million-point LiDAR maps. Experiments on large-scale datasets show reconstructions with improved smoothness at preserved geometric fidelity, and no additional inference-time cost. The code is publicly available at \href{this https URL}{this https URL}

---


### 284. [KoalaGS: Complexity-Aware Continuous Level of Detail for Gaussian Splatting](https://arxiv.org/abs/2610.28615)

**<font color=#1a73e8>作者：</font>** Radu Beche, Raoul de Charette  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deploying a trained 3D Gaussian Splatting scene under shrinking compute budgets requires one primitive set to remain effective when rendered at smaller prefixes. In this continuous level of detail (LoD) setting, the challenge is to decide which Gaussians should retain capacity as the budget decreases. A pilot study on 3DGS-MCMC reconstructions shows that image complexity, computed from the input views before optimization, predicts where reconstruction error concentrates in image and 3D space. It also reveals that simple regions contain too many Gaussians and degrade as much as complex ones at lower budgets, despite being inherently cheaper to represent. Subsequently, in KoalaGS, during training we use this complexity prior to bias relocation toward poorly reconstructed areas while ensuring smooth degradation across LoDs. A primitive importance score then enables inference at low-capacity, while preserving the scene structure. Tested across three datasets, KoalaGS maintains competitive full-capacity quality while significantly improving quality across the budget spectrum, yielding smoother transitions across LoDs, and enabling faster progressive streaming.

---


### 285. [Efficient Edge-aware Attention Network for Graph Generation](https://arxiv.org/abs/2610.28618)

**<font color=#1a73e8>作者：</font>** Vincent Jung, Alba Carballo-Castro, Yiming Qin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph generative models commonly use graph-specific Transformer architectures to jointly update node and edge features. However, these architectures do not directly benefit from recent hardware-aware attention implementations, limiting their scalability. The adaptation is, however, non-trivial: edge and graph-level features must be injected into pairwise attention scores, graph masks must be respected, and dynamic edge updates remain a major source of quadratic memory usage. We propose an edge-aware attention layer for graph generation that incorporates structural information through head-wise score modulation, while updating edge representations with a lightweight residual mechanism that retains attention-score dependent edge updates. This layer can be effectively implemented using PyTorch's FlexAttention. We achieve similar generation quality to our baseline while reducing peak GPU memory by around 65% and substantially improving training and sampling throughput. These results suggest that the proposed architecture is a practical step toward scalable graph foundation models.

---


### 286. [MindView: Benchmarking Generative Multi-View Spatial Intelligence](https://arxiv.org/abs/2610.28622)

**<font color=#1a73e8>作者：</font>** Yanbo Wang, Siqi Luo, Siyu Zhang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial intelligence has recently been assessed through generative tasks such as spatially grounded image editing, yet language-guided generation of spatially consistent views from partial multi-view observations remains underexplored. We introduce MindView, a benchmark for generative multi-view spatial intelligence with 1,500 samples from 513 scenes across three indoor datasets. Its seven tasks form two families: geometry-dominant tasks specify changes in camera position and orientation, while semantics-dominant tasks require inferring target viewpoints by grounding referred objects and interpreting spatial relations and reference-frame cues. Evaluation of eleven generators reveals substantial room for improvement on MindView. A paired context analysis further shows that all eleven generators obtain lower overall scores under the expanded context setting. These findings motivate us to investigate whether task-specific supervision can improve target-view generation and whether models can use additional multi-view evidence effectively. We therefore fine-tune BAGEL on the MindView training dataset, improving its overall score by 24.3 points and yielding gains across all seven MindView tasks. Beyond these generation gains, the fine-tuned model also yields higher scores on three spatial-understanding benchmarks without training on their annotations, suggesting that learning to generate spatially grounded views may benefit spatial understanding. To improve evidence utilization under expanded context, we propose MindCue, a training-free spatial evidence selector guided by a target-view hypothesis. MindCue reverses the drop in overall score under expanded context and outperforms the standard-context baseline. Overall, MindView provides a concrete testbed for generative multi-view spatial intelligence.

---


### 287. [AEON: Unifying Video and 3D World Models](https://arxiv.org/abs/2610.28631)

**<font color=#1a73e8>作者：</font>** Weiqi Zhang, Wenyuan Zhang, Yu-Shen Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current world models for explicit world simulation typically follow two distinct pathways: (1) video generative models (e.g., Sora), which simulate realistic appearances but fail to preserve 3D consistency; and (2) 3D generative models (e.g., Marble), which generate geometrically consistent scenes but often yield static, less realistic observations. We present AEON, a unified framework that bridges video-based and 3D-based world models and combines the benefits of both. The key insight of AEON lies in a generative model that operates within the text- or image-conditioned video latent space while producing renderable 4D graphics primitives---specifically, 4D Gaussian Splatting (4DGS)---as the explicit world representation. We train a 4D reconstruction model to predict both 4DGS and camera poses from monocular videos, serving as our initialized 4D decoder. Furthermore, we design a domain adapter that translates generative video latents into reconstructive 4D latents through a distillation process on the video VAE. AEON naturally supports video-based world modeling by rendering 4DGS at predicted camera trajectories, and constructs a persistent 4D environment with scene dynamics for realistic world simulation. Consequently, AEON empowers a diverse range of world modeling applications and achieves state-of-the-art performance on standard benchmarks. Project Page: this https URL

---


### 288. [Joints, Camera, Action! Co-Generating 3D Motion and Video for Arbitrary Rigs](https://arxiv.org/abs/2610.28632)

**<font color=#1a73e8>作者：</font>** Noam Rotstein, Yoad Tewel, Chen Tessler 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation models can now depict remarkably realistic motion. Yet it is unclear how to use this motion beyond pixels: to animate a specific 3D asset and replay the animation in its 3D scene. For instance, a video model can show a monkey jumping over a crossbar, but it cannot return that jump as replayable 3D motion placed in the 3D scene. Here we present a model that directly co-generates the video and 3D motion for any supplied rig, along with a camera that registers this motion to the scene. Prior video-motion models either handle only human skeletons, often adding billions of parameters, or triangulate 3D motion from generated 2D pose maps. We instead keep 3D motion in a separate model that supports arbitrary skeletons, and connect it to a pretrained video model through a small set of cross-attention layers. This separation lets the motion model first learn how skeletons move from motion-only data, which is easier to obtain and augment than paired video. Additionally, our model learns to locate each joint in the video frames, which lets us recover the camera and place the 3D motion in the scene. To train across many skeletons, we use a generative video editor to place animated 3D assets in scenes suited to their actions, curating the edits so their known motion remains valid. Together with human and robot video, this yields nearly 200K training pairs. Our evaluations demonstrate that our model animates diverse rigs from text more faithfully than video-first pipelines, and its motion responds to the surrounding scene. It also turns video into rig motion, rig motion into video, and enables keyframe-based control of the 3D motion. Videos and additional results are available on our project page: this https URL.

---


> [!TIP]
> 当前位于：**251-288**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-288**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
