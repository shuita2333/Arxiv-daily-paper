# 📦 其他研究 | 2026年10月16日

> 本类共 **264** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-264**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-264**

---

### 251. [Generative Representation Learning for Scalable Latent Tokenization](https://arxiv.org/abs/2610.20533)

**<font color=#1a73e8>作者：</font>** Alan Baade, Kyle Sargent, Vincent Sitzmann 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce an approach for self-supervised representation learning designed to be used as a tokenizer for generative modeling. Our objective supervises a representation loss by factorizing the pointwise mutual information of the data, which we estimate by taking information differences between conditional predictions from a learned generative model. We justify our algorithm theoretically and empirically, demonstrating that our generative approach to representation learning avoids dimensional collapse and feature suppression in cases where commonly used methods like DINO and LeJEPA fail. Moreover, we show our representation learning technique is scalable; expending more compute leads to predictably better latent tokenization. For the first time, we perform a careful analysis of the combined flop efficiency of tokenizer and generative model and demonstrate that our approach is a compute-optimal improvement over direct diffusion for pixel-space generation, obtaining an FID-50K of 2.18 with JiT-L. Applied to ImageNet and the text-to-image dataset GPIC, we show tokenizer encoder scaling laws for diffusability, where extrapolating our approach achieves representations in 7x fewer FLOPs than DINOv2 on ImageNet and 8x fewer FLOPs than WebSSL on GPIC.

---


### 252. [Revisiting Simple Baselines for Relational Deep Learning](https://arxiv.org/abs/2610.20534)

**<font color=#1a73e8>作者：</font>** Viet The Nguyen, Vijay Prakash Dwivedi, Gunther Gust  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Relational deep learning has emerged as a powerful paradigm for learning end-to-end predictive models over relational databases by representing them as temporal heterogeneous graphs. Recent advances based on graph neural networks and Transformers have achieved strong performance across diverse domains. However, the effectiveness of simpler relational baselines remains underexplored, making it difficult to assess how much architectural complexity is needed to achieve strong predictive performance. Motivated by the observation that predictive signals arise from target attributes, relational attributes, and historical labels, we revisit how effectively these signals can be exploited using simple propagation methods. We adapt fixed low-pass feature propagation to relational entity graphs and train an MLP for prediction. The resulting predictions are further refined using Correct-and-Smooth, a graph-based label propagation algorithm that incorporates historical labels over task-specific meta-graphs connecting target entities. Across classification and regression tasks on RelBench, an MLP trained on neighborhood-filtered features outperforms one using only target-entity features on most tasks and recovers a substantial portion of the performance of heterogeneous GNNs. Correct-and-Smooth provides further gains from historical labels, although applying it requires a separately constructed meta-graph because connections among target entities are not directly specified by the relational entity graph. Together, our studies revisit the effectiveness of established propagation methods as simple RDL baselines while identifying canonical meta-graph construction as a key challenge for effective label propagation.

---


### 253. [PrismaCoder: Pushing the Boundaries of Open Multimodal Code Intelligence through Decomposed Rubric Synthesis](https://arxiv.org/abs/2610.20538)

**<font color=#1a73e8>作者：</font>** Qiushi Sun, Jingyang Gong, Yang Liu 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal code intelligence connects the symbolic world of programs with the visual world their execution creates. Interest in this capability is burgeoning, as models are increasingly asked to produce charts, webpages, animations, and semi-structured documents. Recently, proprietary models have pushed far ahead, producing interactive artifacts even from a text description or a screenshot alone. Yet their data and training remain closed, and open progress is held back by the quantity and quality of available data and by the pipelines and methods for producing it. Quality is the harder of the two, since a sample must be correct as a program, well built, and above all visually right once rendered. No existing signal covers all three. Execution often returns just a pass or fail, code similarity does not map to the visual output, and task-specific verifiers do not generalize. To push open progress further, we start from the data side with PrismaForge, a hierarchical data pipeline centered on a synthesized rubric that decomposes these factors into checkable criteria. The same rubric serves as both filter and reward: it curates the supervised corpus, then drives reinforcement learning on visual-coding tasks. Leveraging PrismaForge for data synthesis and filtering, we build PrismaCoder-2M, the most diverse open dataset for multimodal code intelligence and the largest to date. On the model side, we train PrismaCoder-9B and PrismaCoder-35B on this data and release both. They lead the open state of the art by a wide margin and rival leading proprietary systems. Our analyses further show that the proposed rubric-based pipeline improves multimodal coding performance across model backbones. We release our code and data at this https URL.

---


### 254. [Reliability-Aware Multimodal Sentiment Prediction Under Local Modality Missingness](https://arxiv.org/abs/2610.20543)

**<font color=#1a73e8>作者：</font>** Minghao Kong, Deng Yao, Xi Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal sentiment models are usually evaluated on complete utterances, yet streams often lose a contiguous span of text, audio, or video. We study local missingness on aligned CMU-MOSEI features. Our reliability-aware network (RM-Net) keeps the original temporal positions, represents unobserved positions with a learned token, outputs bounded per-modality intensity contributions gated by observation quality, and is trained with dual-view masking of contiguous segments. We fuse five RM-Net seeds with a LoRA-adapted BERT text expert, using a fusion weight that depends only on the visible fraction of content tokens. Architecture, checkpoint, and fusion choices were made on the validation split. On the held-out split, the fused model reaches a macro-F1 of 0.655 on clean inputs and 0.634 under 40\% mixed missingness; its two-view average exceeds the auxiliary-head baseline by 0.024 (95\% video-cluster bootstrap interval [0.003, 0.045]). Because this split was inspected during development, these numbers are not a blind test. For explanations, exact Shapley attributions over the eight modality subsets and position-level occlusion show that top-ranked positions reduce the predicted-class probability faster than random positions (AUC gap 0.113 on validation). We also describe an auditable word-level alignment pipeline for raw clips; its outputs do not feed the predictive models.

---


### 255. [Detection of Potato Plant Leaf Diseases using Convolutional Neural Networks](https://arxiv.org/abs/2610.20544)

**<font color=#1a73e8>作者：</font>** Haimanot Bitew Alemayehu, Simachew Melaku Ayalew, Chilotie Desalew Mengesha 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Potato is an important food-security crop in Ethiopia, but its production is affected by foliar diseases, particularly early blight and late blight. This study develops a lightweight convolutional neural network (CNN) to classify potato leaves into three categories: healthy, early blight, and late blight. The proposed model was trained using 2,215 images from the PlantVillage dataset and evaluated on an independent field dataset containing 247 images collected from potato farms in Banja, Awi Zone, Ethiopia. On PlantVillage, the model achieved 99.04% training accuracy, 98.21% validation accuracy, and 98.66% test accuracy. On the field dataset, it achieved 90.28% accuracy. The study also compares the proposed CNN with VGG16 and MobileNetV2 in terms of classification performance and computational efficiency. The proposed model contains 446,787 trainable parameters, occupies approximately 1.70 MB, and requires an average of 5.58 seconds per training epoch in the reported experimental setup, compared with 9.96 seconds for VGG16 and 7.68 seconds for MobileNetV2. The results demonstrate the potential of a compact CNN for potato leaf disease classification and highlight the importance of independent field evaluation, where image conditions are more variable than in controlled benchmark datasets. The proposed approach may support preliminary disease identification for smallholder farmers in Ethiopia and similar agricultural settings.

---


### 256. [Speculative Sampling in Interactive Video Generation](https://arxiv.org/abs/2610.20556)

**<font color=#1a73e8>作者：</font>** Yubo Huang, Yuxuan Zhang, Jiaming Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive video generation commonly relies on small bidirectional chunks to reduce response latency. Yet our preliminary experiments show that larger chunks improve video quality and better utilize GPU parallelism, allowing more latents to be sampled with only a modest increase in sampling time. Motivated by these observations, we propose Speculative Sampling, a strategy that combines the modeling power of large bidirectional windows with the low-latency interaction of small ones. It expands the modeling window by appending noise latents as padding and caches the resulting predictions for reuse when the condition remains unchanged. Predictions are delivered incrementally, while the uncommitted future remains replaceable. Our latency analysis shows that this removes the waiting-time lower bound imposed by chunk boundaries, shifting the optimization focus from reducing chunk size to accelerating per-chunk sampling. Bidirectional window size thus becomes a decision variable for jointly optimizing visual quality and sampling time, rather than a necessary constraint on low-latency interaction. This opens a path to serving large bidirectional models in interactive streaming systems without complex streaming post-training.

---


### 257. [A$^3$PreCore: Robust Rigid Registration for Native FLAIR-Space Brain-Mask Transfer](https://arxiv.org/abs/2610.20561)

**<font color=#1a73e8>作者：</font>** Elmira Mirzabeigi, Zahra Khalilzad, Taylor Snowden-Richardson 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable brain-mask transfer into native fluid-attenuated inversion recovery (FLAIR) space can fail when T1-to-FLAIR rigid registration is unstable. We developed A$^3$PreCore, a six-degree-of-freedom rigid-registration strategy that aligns the full bias-corrected T1-weighted image to native FLAIR using normalized mutual information while preserving the established T1-space anatomical mask. We also introduced extended quantitative quality control (E-QC), which characterizes mask extent, field-of-view-relative position, FLAIR intensity support, boundary support, inferior morphology, and pairwise geometric disagreement. In 78 participants with paired T1-weighted and FLAIR imaging, A$^3$PreCore was compared with fsl_anat and the Brain Extraction Tool (BET). Gross rigid-body misregistration occurred in 21/78 fsl_anat outputs (26.9%) and 0/78 A$^3$PreCore outputs (exact two-sided McNemar p=9.54 x 10^-7). Among 57 participants without gross fsl_anat misregistration, A$^3$PreCore preserved close agreement (median Dice=0.993; median paired Delta NMI=-0.00007, p=0.429). A$^3$PreCore remained broadly concordant with BET (median Dice=0.955), with less inferior and extracranial extension in representative comparisons. Method-blinded neuroscientists ranked A$^3$PreCore first in 35/40 participants (87.5%). E-QC additionally exposed severe orientation-related disagreement not evident from global descriptors or centroid displacement alone. These findings support A$^3$PreCore as a robust native-FLAIR brain-mask transfer strategy and E-QC as a complementary framework for multidimensional mask characterization and participant-specific geometric quality control.

---


### 258. [Any Time, Any Space: A World-State-Centric Framework for Agentic Video Generation](https://arxiv.org/abs/2610.20571)

**<font color=#1a73e8>作者：</font>** Weijie Wang, Haomin Zhang, Ye Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-form agentic video generation must turn a screenplay into shots that remain spatially and temporally consistent across nonconsecutive requests. Passing prompts or recent frames between shots does not provide a shared spatial frame for revisiting a scene or a time-indexed record for replaying an earlier event. We present Any Time, Any Space (ATAS), which compiles a screenplay into shot requests with explicit location, camera, and event-time references. Before generation, it retrieves relevant evidence from a scene memory of registered static geometry and an event memory of dynamic observations indexed by scene, event, and time. After generation, ATAS reconstructs and registers the clip. It updates memory only when review and state checks accept the observation, while film delivery remains independent of memory admission. Across four video generators, ATAS improves all reported cross-shot consistency measures and achieves the highest aggregate benchmark score for each backbone. It also outperforms the compared agents and 3D-guided methods on target-image spatial revisit, leads three event-recapture criteria, and receives the highest human ratings on all six criteria. The video results and code are available on our project page: this https URL.

---


### 259. [Continuum Attention](https://arxiv.org/abs/2610.20586)

**<font color=#1a73e8>作者：</font>** Afshin Khadangi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Continuum Attention (CA), a causal Transformer attention operator that replaces discrete key and value lookup with integration over a continuous, piecewise linear memory curve. Each query induces an exponential relevance density along the curve. Integrating the density and interpolated values yields exact normalized attention from closed form exponential moments, including half token boundary contributions. The gradients follow analytically from moments of order at most two, enabling parallel GPU implementations while retaining quadratic sequence complexity and the standard Transformer decoder. Compared with ordinary softmax and focal attention, CA reduces mean validation negative log likelihood by 0.0200 and 0.0480 nats per byte, respectively, winning all paired comparisons. An additional disjoint validation slice yields a 0.0457 nats per byte advantage over the strongest selected softmax baseline, with a paired 95% confidence interval. These findings motivate continuous integration as a promising attention alternative while leaving larger scale generalization open.

---


### 260. [Your Transformer Is Secretly Elastic](https://arxiv.org/abs/2610.20588)

**<font color=#1a73e8>作者：</font>** Walter Simoncini, Dheeraj Varghese, Gertjan J. Burghouts 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling up transformers has produced models with broad capabilities, deployed across heterogeneous hardware and fluctuating workloads. Yet, model families offer only a few fixed sizes (e.g., S, B, L), forcing users to commit to a model based on hardware and latency constraints. This rigidity is often suboptimal under varying query loads. We introduce a retraining-free method that elastifies pre-trained transformers into a single model that adapts on-the-fly across a continuum of computational budgets. Our key contribution is a differentiable relaxation of the functional unit-ranking problem: unlike prior work, which optimizes a single importance weight per MLP block or attention head, we rank every individual MLP neuron and attention head jointly, on a common scale, by minimizing the model's loss under soft pruning across many sparsity targets, all at once. Across 27 vision and text transformer encoders ranging from 22M to 8B parameters, our method yields smooth degradation up to 60% sparsity and outperforms one-shot baselines under deep pruning. For example, pruning DINOv3 ViT-H+/16 to 50% sparsity removes 427M parameters while reducing ImageNet-1k linear-probing accuracy by only 0.8%, without the need for weight correction or retraining. At 60% sparsity, a pruned AugReg ViT-B/16 model achieves up to $1.80\times$ higher throughput and $1.26\times$ lower single-query latency on an A100 GPU. Elastic models are produced in minutes, with construction time scaling sub-linearly with parameter count.

---


### 261. [Feed-Forward Multi-View Feature Coding for 3D Gaussian Splatting](https://arxiv.org/abs/2610.20590)

**<font color=#1a73e8>作者：</font>** Seungmi Choi, Ji-Hyoun Choi, Suhyun Jo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D Gaussian Splatting (3DGS) methods enable efficient reconstruction of 3D scenes from sparse multi-view images in a single forward pass, without scene-specific optimization. However, existing feed-forward scene-coding pipelines first generate a complete Gaussian representation and then encode its geometry and appearance attributes separately, often involving non-differentiable operations. The resulting 'generate-then-compress' pipeline requires complex attribute-specific codec designs and limits rate-distortion performance by restricting the exploitation of cross-attribute redundancy. We propose multi-view feature coding for Gaussian splatting (MFGS), an end-to-end feed-forward framework for scene coding. Instead of compressing an explicit Gaussian representation, MFGS extracts multi-view features from the input images and encodes them into a compact bitstream. Through end-to-end rate-distortion training, MFGS learns compact multi-view features that jointly represent geometry and appearance, enabling the receiver to predict Gaussian attributes from the decoded features. We further introduce importance-guided Gaussian selection to accommodate different rendering budgets, allowing the receiver to adjust the number of Gaussians used for rendering from the same bitstream. Across RE10K, ACID, and DL3DV, MFGS achieves 99.76-99.86% bitrate savings over the generate-then-compress pipeline, as measured by BD-rate, while reducing total GMACs by 52-55% and providing an approximately 12 times end-to-end speedup.

---


### 262. [VITAL: From Visual Motion to Precise Action](https://arxiv.org/abs/2610.20604)

**<font color=#1a73e8>作者：</font>** Ao Liang, Youquan Liu, Mingxiao Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World-action models aim to turn visual anticipation into driving decisions, yet typically train action experts on trajectory representations defined independently of visual dynamics. This motivates deriving action targets directly from visual motion. We first examine a simpler setting in which trajectories are reconstructed from recorded future images. Even without the need for future prediction, reconstruction captures the dominant maneuver but leaves centimeter-scale errors. We therefore introduce VITAL (Vision-Induced Tokens for Action Learning), an action tokenizer that couples a visually derived motion scaffold with a compact residual encoding the trajectory error left by that scaffold. This representation makes visual motion the principal prediction target and gives small metric corrections a separate, normalized learning scale. Using flow matching, the action expert jointly predicts both components from the current image, ego state, and navigation command, without generating future images at inference. The same residual coordinates support bounded reinforcement post-training that refines execution while keeping the predicted visual scaffold fixed. With only one action denoising step, VITAL achieves 90.8 PDMS on NAVSIM v1 navtest, within 0.13 points of its ten-step score at 3.29x the end-to-end inference speed. Without retraining, it achieves 91.1 EPDMS on NAVSIM v2 navtest and 38.6 on navhard. Project page: this https URL

---


### 263. [Representation Conditioning for Generation](https://arxiv.org/abs/2610.20608)

**<font color=#1a73e8>作者：</font>** Saeed Razavi, Xingjian Leng, Liang Zheng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Representation-alignment methods effectively accelerate the diffusion transformer training. REPA, for example, uses a pretrained vision encoder to supervise an intermediate layer through an MLP projection head which is discarded after training. It aims to import semantics from the vision encoder to the diffusion backbone. While this objective is achieved at early layers by back-propagating the alignment loss, there is no guarantee that later layers, supervised by the velocity prediction loss alone, can well access such semantics. We propose a simple solution, representation conditioning (RECON), to improve semantics in later layers. During training, we feed the pretrained vision encoder tokens into later layers; during inference, because we no longer have the clean image, we reuse the MLP head (as a proxy to the vision encoder) and project its output tokens to the later layers. Our method adds no parameters and leads to much faster convergence: RECON is $63\times$ faster than SiT and $25\times$ faster than REPA. Code is available at this https URL

---


### 264. [Can Learning to Answer Spatial Questions Improve Novel-View Generation?](https://arxiv.org/abs/2610.20610)

**<font color=#1a73e8>作者：</font>** Jahyeok Koo, Hyeonseo Yu, Seungho Jang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating novel views from limited observations requires preserving both the appearance and spatial structure of a scene. Although recent approaches exploit fine-grained geometric cues, they do not explicitly model high-level semantic and spatial properties such as object identity, attributes, and inter-object relationships. In this work, we investigate whether 3D language understanding can provide complementary supervision for novel-view generation. We introduce Ask4NV, built on a pretrained unified multimodal model with a Mixture-of-Transformers (MoT) architecture. Our model incorporates camera geometry into both VAE and ViT representations and leverages understanding features during generation through joint self-attention with a modality-aware attention masking strategy. Experiments demonstrate strong image quality and geometric consistency in novel-view generation, alongside competitive 3D language understanding. Further analysis shows that joint training improves cross-view correspondence in VAE representations and similarity in a 3D-aware feature space.

---


> [!TIP]
> 当前位于：**251-264**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-264**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
