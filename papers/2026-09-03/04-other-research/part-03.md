# 📦 其他研究 | 2026年09月03日

> 本类共 **236** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-236](./part-05.md)

---

### 101. [GazeTune: Facilitating Precise Gaze-Driven Interactions with Cascaded Touch Input](https://arxiv.org/abs/2609.00716)

**<font color=#1a73e8>作者：</font>** Jina Kim, Eric J. Gonzalez, Yang Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Eye gaze has become an essential input for spatial computing, but its coarse targeting and saccadic nature limit precision and complicate continuous interactions such as dragging, especially under user motion. Gaze+pinch has also become standard in XR for its convenience, yet mid-air gestures remain imprecise, fatiguing, and socially unacceptable. These limitations underscore the need for an approach that preserves the speed of gaze while enabling stable, fine control. We present GazeTune, a cascaded multimodal interaction technique combining gaze and touch to refine gaze-based selection and manipulation. Touch serves as a refinement channel within gaze pointing, allowing precise cursor and target control. Our work investigates how gaze-and-touch enhances dragging and mitigates Motion-Induced instability. In a study (N=20), we compared GazeTune against gaze-only and gaze-pinch methods in 2D dragging. Results show that GazeTune achieves significantly lower error with comparable execution time, validating its effectiveness and balanced trade-off between time and accuracy.

---


### 102. [A Closed-Loop Evaluation of Capability Loss and Recovery in Compressed Driving Policies](https://arxiv.org/abs/2609.00718)

**<font color=#1a73e8>作者：</font>** Ahmad Alfan Alfian Irfan, Nur Ahmad Khatim, Mansur Arief  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many automobile and mobility companies deploy learned driving policies on embedded computers with limited memory and power. Pruning, knowledge distillation, and quantization are the standard methods to reduce the size and the inference cost of these policies. However, these methods are commonly assessed by aggregate numerical scores, and such scores may not reflect the ability of the policy to drive safely when interacting with other road users. In this study, we propose a stage-wise closed-loop evaluation approach to follow a driving policy through a compression pipeline. We formulate the driving task as a partially observable Markov decision process (POMDP) and train a belief-state policy with proximal policy optimization (PPO) in Gym-Duckietown. We then extract the actor, compress it one stage at a time, and evaluate it on five driving curricula. We show that structured pruning is the stage at which the driving capability is first lost. Meanwhile, distillation improves the pruned actor, but the improvement is limited by its rehearsal data. Integer quantization of the improved actor loses some of the curricula that require the vehicle to stop and then resume. Interestingly, the same procedure on the unpruned actor preserves all five curricula. Our study thus provides an empirical analysis aiming to answer the currently active discussions on how to accept a compressed driving policy, so as to achieve a safe and statistically reliable deployment of automated driving functions.

---


### 103. [Design and Implementation of a Kalman Filter-Infused Algorithm for Tilt Estimation](https://arxiv.org/abs/2609.00730)

**<font color=#1a73e8>作者：</font>** Yuehan Ma, Hongji Dai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate tilt angle estimation is important in many engineering applications, such as robotics, motion tracking, and embedded control systems. However, measurements from low-cost inertial sensors are often degraded by noise and drift. This paper presents a single-axis tilt angle estimation system based on the MPU6050 inertial measurement unit, implemented on an RP2040 microcontroller platform, with sensor fusion achieved through a Kalman filter. The accelerometer provides a direct estimate of tilt angle from gravity but is sensitive to noise and short-term fluctuations. The gyroscope provides smooth angular rate measurements, but integration over time introduces drift. To overcome these limitations, a Kalman filter is used to combine measurements from both sensors, leveraging the long-term stability of the accelerometer and the short-term smoothness of the gyroscope. Both simulation and hardware experiments are performed. In simulation, sensor noise and drift are modeled to evaluate the filter performance under control conditions. In the hardware implementation, real-time MPU6050 data is acquired and processed by the RP2040 platform, and the estimated tilt angle is compared with accelerometer-only and gyroscope-only outputs. The results show that the proposed method effectively reduces noise measurements and suppresses long-term drift while preserving good dynamic response. Overall, the system provides more stable and accurate tilt estimation than either sensor alone, demonstrating a practical and accessible approach for Kalman filter based sensor fusion in embedded application.

---


### 104. [Mind the Rift: Cross-Scale Coupling Mismatch for AI-Generated Video Detection](https://arxiv.org/abs/2609.00742)

**<font color=#1a73e8>作者：</font>** Siyu Li, Jin Yang, Weiheng Liang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As AI video generators achieve cinematic realism, reliable detection becomes essential for safeguarding digital trust. We identify cross-scale coupling mismatch as a new forensic signal, where scale refers to the level of abstraction (semantic dynamics vs. pixel-level residuals): in natural videos, macro-level temporal dynamics and micro-level residual patterns are intrinsically coupled by the unified imaging physics pipeline, whereas AI generators, whose training objectives do not explicitly preserve this joint distribution, systematically violate this coupling. Detecting such mismatch is challenging because it requires independently extracting information at both scales while simultaneously quantifying their cross-scale relationship. We propose RIFT (Representation Inconsistency Forensics on Trajectories), an orthogonal forensic framework that addresses this through three interlocking components: a macro stream that builds a dynamic baseline of expected temporal evolution via differential geometry and persistent homology on learned manifold trajectories, a micro stream that acts as a sensitive forensic probe via steganalytic filtering and temporal modeling, and a coupling divergence module that measures the conditional dependency between the two streams. Gram-Schmidt orthogonality guarantees the information-theoretic validity of this measurement. Experiments on two benchmarks (VidProM, 120K videos, 7 generators; GenVidBench, 68K videos, 4 generators) demonstrate that RIFT achieves 99.33% and 99.72% F1-score respectively, with 97.87% unseen-generator detection rate in leave-one-out evaluation, while exhibiting encoder agnosticism: scaling from ViT-S/14 (22M) to ViT-L/14 (300M) changes F1 by less than 0.1%, and switching to a different encoder family (DINOv1) reduces F1 by only 0.73 pp. Code is available at this https URL

---


### 105. [Feed-Forward Multi-view Multi-person Reconstruction with Contrastive Human-Aware 3D Representation](https://arxiv.org/abs/2609.00745)

**<font color=#1a73e8>作者：</font>** Yuanwang Yang, Buzhen Huang, Zongxuan Ren 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-view human reconstruction has been extensively studied under simplified settings, yet robust and efficient multi-person reconstruction in unconstrained environments remains challenging. Existing bottom-up methods often rely on accurate camera calibration and explicit cross-view matching, and therefore struggle with severe occlusions and ambiguities. We propose a new top-down paradigm that maintains a unified, instance-centric human-aware 3D space, enabling simultaneous camera calibration, cross-view association, and human reconstruction via cross-modal contrastive learning. Observations from multiple views are lifted and fused into this shared 3D space, where geometric structure, visual appearance, and human-centric semantic cues are jointly encoded at the instance level. We further introduce a spatial contrastive learning strategy that aligns 3D features corresponding to the same human instance across different views and modalities while separating different instances. This enables correspondence reasoning, semantic aggregation, and instance discrimination to be performed natively in 3D, improving cross-view consistency and robustness under severe occlusions. Finally, structured human body models are recovered in a feed-forward manner by regressing SMPL parameters from instance-level 3D human tokens. Extensive experiments demonstrate robust, accurate, and efficient multi-view human reconstruction in challenging real-world scenarios.

---


### 106. [Measuring Optimal Transport in Transformer Depth](https://arxiv.org/abs/2609.00748)

**<font color=#1a73e8>作者：</font>** Alexandre Quemy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A transformer carries each token's state from layer to layer, and the whole vocabulary carried together forms a cloud that moves with depth. We ask whether a trained network moves this cloud the way optimal transport would: at the cheapest cost, and along the map that pairs each token with its optimal destination. We measure both on Pythia-160m and Pythia-410m, with an exact assignment between consecutive layer clouds, a measured sampling floor, calibration on couplings known to be optimal, and a split of the cost into the common shift of the cloud and the token-specific moves. At the last layer, both models move their tokens where the optimal-transport map sends them, at the optimal cost for Pythia-410m and slightly above it for Pythia-160m. At the first layer they do not. In between, single layers can be judged on cost at only two of ten transitions, and blocks of several layers move the cloud at close to the optimal cost. The agreement at the last layer is much weaker at initialisation (0.64 against 0.86) and grows with training.

---


### 107. [VOIM: Training-Free Open-Vocabulary 3D Instance Mapping for RGB-D and Monocular SLAM](https://arxiv.org/abs/2609.00775)

**<font color=#1a73e8>作者：</font>** Sangmin Song, Sarath Kodagoda, Marc G. Carmichael 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Voxel-Grounded Online Instance Manager (VOIM), a training-free voxel-grounded instance manager that builds open-vocabulary 3D instance maps from RGB-D or from monocular RGB alone, a regime no prior training-free system addresses. Online systems typically segment object instances and label them at first detection, committing when evidence is weakest. VOIM instead defers label and instance decisions until soft evidence from unmodified, off-the-shelf perception has accumulated per voxel across views. We show that the mapping stage, rather than the particular perception models, carries the result: across four perception configurations on ScanNet++, varying the region descriptor, the detector label prior and the mask source, the map exceeds the strongest online RGB-D system, OVO-SLAM, by between 4.8 and 11.7 mIoU. Perception is not neutral, and substituting that baseline's own descriptor family costs 4.1 of the margin, yet the baseline carries the marginally better 2D descriptor (33.7 vs. 31.5 mIoU over three scenes) and still realizes the weaker map. Under a like-for-like protocol VOIM reaches 44.07 mIoU on ScanNet++ against 32.37, winning all ten scenes and both aggregations (pooled 33.31 vs. 25.97), and the same system runs unchanged to fully monocular RGB, matching that baseline pooled on Replica (27.80 vs. 27.50). The advantage is regime-specific: under Replica's all-classes scoring, matched inputs give a split result, 28.60 vs. 27.50 pooled against 24.59 vs. 30.11 on the per-scene mean. Room scale is label-limited and building scale drift-limited. Labeling does not run in real time, dominated by per-class detection over the full vocabulary. The maps export occupancy grids and resolve free-form queries to object instances.

---


### 108. [When Features Become Instances: Inverted Contrastive Learning for Unsupervised Feature Selection](https://arxiv.org/abs/2609.00782)

**<font color=#1a73e8>作者：</font>** Utsab Ghosh, Roshni Chakraborty  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Unsupervised feature selection seeks a compact subset of informative features without access to class labels, making feature utility difficult to define. Existing UFS methods therefore rely on indirect structural criteria, such as similarity preservation, locality, sparsity, cluster geometry, or reconstruction quality. In this paper, we instead study UFS through representation consistency and propose Inverted Contrastive Learning for Unsupervised Feature Selection (ICLFS), a feature-wise contrastive framework that reformulates UFS as a representation learning problem over features rather than samples. ICLFS first inverts the data matrix so that each feature is represented by its sample-profile vector, then constructs multiple masked positive views together with a shuffled negative view, and learns projector-space representations that remain consistent across these structured perturbations under an InfoNCE-based objective. Motivated by recent findings that cosine-based and InfoNCE-based training affect embedding norms, we use projector-space embedding magnitude as the saliency signal for ranking features. The resulting norm-based ranking is subsequently refined through Laplacian-Gated Ranking Correction, which suppresses locally redundant candidates while preserving salient ones. Extensive experiments on 12 benchmark datasets show that ICLFS achieves the best clustering accuracy on 10 datasets against both classical and neural baselines under the standard clustering-based UFS evaluation protocol, while remaining competitive on the other two. These results show that feature-wise contrastive representation consistency provides a strong and effective alternative to neighborhood, cluster, and reconstruction-based UFS formulations.

---


### 109. [MROP: Mask-Region Optimized Purification Against Backdoor Attack in Deep JSCC](https://arxiv.org/abs/2609.00786)

**<font color=#1a73e8>作者：</font>** Seongkyu Yang, Hyeonho Noh, Hyun Jong Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deep joint source and channel coding (JSCC) transmits a source by mapping it directly to channel symbols through an end-to-end deep neural network (DNN) and reconstructing it at the receiver. Taking image transmission as an application, this DNN pipeline behaves as a black box: the receiver cannot readily detect security attacks when the transmitted images are corrupted, thereby introducing a new security vulnerability. In this letter, we study defense against input-patch backdoor attacks on deep JSCC, in which a small trigger patch attached to the input forces the decoder to emit an attacker-chosen target image. Most existing patch-trigger defenses are designed for classification, leaving the reconstruction setting of deep JSCC unaddressed. We adapt the gradient mask defense to this reconstruction setting as a baseline and then propose mask-region optimized purification (MROP), which operates at inference and requires no retraining of the JSCC model. Unlike the baseline, which localizes the trigger from the input--output gradient, MROP instead places a per-pixel mask at the encoder input and optimizes it via a Gumbel-sigmoid relaxation to localize the trigger, then refines the trigger region to reconstruct the pure images better. In numerical results, we evaluate the proposed method on CIFAR-10 and STL-10 datasets along with the DeepJSCC and SwinJSCC models. By doing so, we show that the proposed method substantially lowers the attack success rate (ASR) while preserving the peak signal-to-noise ratio (PSNR) of clean reconstructions.

---


### 110. [StudyBench: Can Self-Evolution Squeeze Textbooks for Olympiad Capability?](https://arxiv.org/abs/2609.00787)

**<font color=#1a73e8>作者：</font>** Yinghao Chen, Zixi Chen, Bingxiang He 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Humans need to study only a handful of well-written textbooks to master a discipline and attempt its hardest problems. We argue that an ideal self-evolution method should share the same property, that is autonomously learning from raw training material for transferable problem-solving capability. However, we still lack a direct measurement for it. We introduce StudyBench, a controlled physics benchmark that directly measures how efficiently a self-evolution method converts training material into capability. We organise the test set into an Application Set, consisting of difficult textbook problems and evaluating absorption ability, and a Transfer Set, consisting of olympiad-level problems and evaluating transfer ability. Benchmarking representative self-evolution methods across three base models, we find that improvements on the Application Set rarely translate to the harder Transfer Set. A guidance ablation exposes a Guidance Gap: even the strongest method closes only a small fraction of what the same material unlocks when supplied as in-context guidance. Besides, every method hits a Compute Plateau, saturating well before exhausting its compute budget. The remaining gap is therefore a method problem rather than a data or compute problem. By offering a clean and controlled benchmark, StudyBench turns self-evolution progress from an open-ended pursuit into a measurable target for future research. Our code is released at this https URL.

---


### 111. [Subspace Levenberg Marquardt Algorithms in Training Neural Networks](https://arxiv.org/abs/2609.00789)

**<font color=#1a73e8>作者：</font>** M. Duc Hoang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Levenberg-Marquardt (LM) algorithm is a well-known second-order method for rapid convergence and strong robustness when training small- to medium-sized neural networks (NNs). However, its computational and memory costs increase significantly as the number of parameters in an NN grows. To address this limitation, subspace methods have been proposed, such as the Krylov subspace LM (KSLM) and the hybrid subspace LM (HSLM), making second-order algorithms more efficient. In this work, we evaluate the subspace Levenberg-Marquardt algorithms for regression and classification tasks in neural networks. We compare the performance of subspace LM variants with the classical LM method, as well as other popular first-order algorithms, such as stochastic gradient descent (SGD) and Adam.

---


### 112. [Advanced Pixel Diffusion Model with Guided Sparse Global Refinement](https://arxiv.org/abs/2609.00798)

**<font color=#1a73e8>作者：</font>** Weiyi You, Jinhua Zhang, Xingyu Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pixel-space diffusion has recently emerged as a promising direction for high-fidelity image generation by modeling images directly in the original pixel domain. However, pixel-space diffusion is computationally demanding due to the extremely high dimensionality of natural images. For efficiency, existing pixel diffusion models either compromise fine details with large-patch tokenization or confine subsequent refinement within individual patches. Such intra-patch refinement inevitably restricts structural continuity across patch boundaries and long-range token interactions, limiting refinement quality. To address these issues, we propose PixSGR, a novel Pixel diffusion framework with Sparse Global Refinement tailored for modeling the distribution of natural images directly in pixel space. PixSGR starts from a supervised low-channel bottleneck to efficiently capture the low-dimensional manifold of natural images. It then progressively expands the channel dimensionality and spatial resolution to recover increasingly fine-grained structures. At the spatial refinement stage, coarse-scale attention maps preselect globally relevant interactions to pre-sparsify fine-scale attention, enabling non-local refinement beyond isolated patches without the quadratic cost of dense attention. Extensive experiments on ImageNet validate the effectiveness of PixSGR. It achieves an FID of 1.51 at 256$\times$256 and maintains performance when scaled to 512$\times$512, attaining an FID of 1.60.

---


### 113. [No Pixel Left Behind: Filling Gaps in Anime Colorization](https://arxiv.org/abs/2609.00800)

**<font color=#1a73e8>作者：</font>** Masahiro Kono, Akinobu Maejima, Yuki Koyama 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Animation production workflows often involve digital colorization of line art, where small unpainted regions ("gaps") frequently occur and remain an underexplored challenge. We conducted a formative study in Japanese animation (anime) pipelines and found that while the paint bucket tool is widely used for base coloring, tiny enclosed areas are frequently overlooked, resulting in time-consuming manual detection and filling. We introduce GapFill, a tool grounded in professional practices that reduces the effort of gap detection, zooming, and color selection. Our deep-learning method suggests appropriate fill colors by referencing surrounding regions, leveraging the flat-color nature of anime-style images. In a user study with 13 professional colorists, our system improved performance and usability in gap-filling tasks over conventional methods. The study also suggested that prediction accuracy alone is not the primary factor for usability, that appropriate colors can be contextually ambiguous, and that GapFill can complement existing tools depending on users' trust in new AI-powered assistance.

---


### 114. [TEIDAN: A Multilingual Multiparty Dialogue Corpus](https://arxiv.org/abs/2609.00802)

**<font color=#1a73e8>作者：</font>** Taiga Mori, Koji Inoue, Mikey Elmers 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-party interaction is a central setting for human communication and a necessary target for human-agent interaction systems that must participate in group conversation. Yet available corpora often focus on meetings, task-oriented interaction, text-based interaction, or acted scenarios, and fewer resources support cross-linguistic comparison of spontaneous face-to-face triadic discussion. This paper presents TEIDAN, a multilingual multimodal corpus that currently consists of Japanese and English three-party conversations. TEIDAN records groups of three participants discussing open-ended topics with individual pin microphones, a microphone array, and participant-facing cameras, and provides IPU-based transcripts for both language portions. Earlier studies used subsets of the Japanese portion for task-specific benchmarks in multi-party dialogue modeling; in contrast, this paper presents TEIDAN as a corpus resource spanning both Japanese and English, with planned expansion to additional languages. We describe the collection design, participants, recording setup, transcription format, and corpus statistics, and provide preliminary analyses to illustrate how TEIDAN can support research on turn-taking, addressee recognition, and multimodal grounding in human-human and human-agent interaction.

---


### 115. [Effective Interventions Against AI-Enhanced Scams](https://arxiv.org/abs/2609.00806)

**<font color=#1a73e8>作者：</font>** Kyle Fredrickson  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In 2025, scams were responsible for an estimated $442 billion in direct losses globally. In the United States, reported losses increased by nearly 400% between 2020 and 2025. Though AI in scamming is a relatively new phenomenon, its use significantly changes the economics of scams as well as the bottlenecks in scam operations. In this paper I investigate what interventions will remain effective under this new AI-driven scamming regime.
I develop a simple model of scam profits to understand how different interventions asymptotically affect scam operations. I find that three levers--reporting rate, centralization of reporting, and report accuracy--multiply in their effect on expected victims per scam channel, reducing revenue per scam channel while increasing costs. Because effects multiply, interventions affecting all three could have a significant effect on the profitability of the scam business model. My analysis suggests that even modest reporting rates against high-value scam infrastructure could have significant impacts on scam profitability.

---


### 116. [Ctrl-F-Resist. Practices, Challenges, and Technical Needs of Civil Society Organizations Monitoring the Far-Right Online](https://arxiv.org/abs/2609.00808)

**<font color=#1a73e8>作者：</font>** Elisabeth Steffen, Helena Mihaljević  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As far-right actors increasingly exploit online platforms to disseminate ideology and mobilize supporters, civil society organizations (CSOs) play a vital yet underrecognized role in monitoring antidemocratic dynamics online. Unlike fact-checkers or content moderators, CSOs engage in long-term, contextualized analysis, often in resource-constrained settings and under precarious conditions. Despite their critical societal role, CSOs face significant barriers to adopting or co-developing technical solutions, including legal uncertainty, limited platform access, and chronic underfunding. Existing research and tool development efforts have largely overlooked these actors in favor of more institutionally embedded stakeholders. This paper addresses this gap through a qualitative study with 15 practitioners from 12 Germany-based CSOs engaged in online monitoring, positioning them as key yet overlooked stakeholders in the governance of digital spaces. We explore their current practices, challenges, and expectations regarding technological support. Our findings show that monitoring remains largely manual due to the lack of tailored tools, with enhanced search capabilities emerging as the most pressing technical need. While participants express openness to AI-supported features such as media processing and content discovery, many remain skeptical of automated classification, citing concerns around trust, legal usability, and professional credibility. Grounded in these findings, we introduce a conceptual monitoring workflow and describe its implementation in an open-source Telegram monitoring prototype designed to flexibly support diverse monitoring goals. We outline concrete design, policy, and research recommendatios, and introduce the manual labor trap as an empirically grounded concept that explains why monitoring CSOs tend to remain locked into labor-intensive, low-capacity arrangements.

---


### 117. [ReBridge-Flow: Re-Coupling Posterior Bridges in Flow Matching for Image Restoration](https://arxiv.org/abs/2609.00811)

**<font color=#1a73e8>作者：</font>** Jiaqi Zhang, Yiqi Wang, Hongjie Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flow Matching provides an efficient generative prior for image restoration by learning continuous transport between source and data distributions. However, existing methods typically incorporate measurement constraints through local corrections. Such corrections may disrupt the source-clean endpoint coupling implicitly encoded by the pretrained flow, making the corrected endpoint pair incompatible with the current state. To address this issue, we propose ReBridge-Flow, a posterior bridge re-coupling method. Specifically, given the current state, ReBridge-Flow first decodes the corresponding local source and clean endpoints. It then incorporates measurement information through clean-side anchoring and synchronously re-couples the source endpoint, yielding a measurement-aware endpoint pair with improved local bridge compatibility. The re-coupled endpoints further define a posterior-informed transport direction for advancing the sampling process. We also introduce the Posterior Bridge Defect, which jointly characterizes measurement error, deviation from the flow prior, and bridge mismatch, and leads to explicit updates for clean-side anchoring and source-side re-coupling. Extensive experiments on multiple natural and medical image restoration tasks demonstrate that ReBridge-Flow effectively alleviates bridge mismatch and improves the structural consistency of restored images.

---


### 118. [RingMoClaw: An Experience-Inspired Multi-Agent Framework for Self-Evolving Research in Remote Sensing](https://arxiv.org/abs/2609.00814)

**<font color=#1a73e8>作者：</font>** Kaiyue Kang, Qixuan He, Peijin Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing visual models have continuously advanced various interpretation tasks. However, the research process behind model improvement still heavily relies on manual expertise, requiring extensive trial-and-error iterations in model design, data processing, and performance diagnosis. Existing agent-based approaches mainly focus on task execution and workflow orchestration, while lacking the capability of autonomous research iteration for continuous performance optimization. To address this issue, we propose RingMoClaw, an experience-inspired self-evolving multi-agent framework for remote sensing visual interpretation. RingMoClaw integrates a research branch, a quality-control branch, and a dual-stream dynamic experience bus to establish a closed-loop optimization process covering strategy generation, experiment execution, independent review, and experience accumulation. The heterogeneous Critic mechanism provides stage-wise diagnosis and feedback, while the dual-stream experience bus incorporates external knowledge and internal experimental experience to guide strategy evolution and eliminate ineffective searches. Extensive experiments on four remote sensing downstream tasks, including object detection, scene classification, semantic segmentation, and change detection, demonstrate the effectiveness and generalization of RingMoClaw. Compared with the corresponding baseline models, RingMoClaw improves performance by 1.84\% mAP$_{50}$ on object detection and achieves consistent gains across the other three tasks, while reducing the required evolution steps by over 40\% compared with existing research automation frameworks. These results suggest that RingMoClaw offers a feasible route from task execution toward continuous research driven model evolution in remote sensing.

---


### 119. [Can Scene Text Recognition Read Rare Compositions?](https://arxiv.org/abs/2609.00816)

**<font color=#1a73e8>作者：</font>** Genpei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scene text recognition is reported as 89--97% accurate on the six standard benchmarks, and the problem is widely treated as saturated. We present an alternative reading. When the same test images are stratified jointly by ground-truth word rarity and character n-gram novelty against a reference corpus, accuracy at the rare-word x rare-trigram corner of the resulting 5x5 grid drops 10--18 pt below the q3/q3 centre across nine English specialised recognisers, and the same direction (corner below centre) holds on all 13 of 13 (language, model) pairs we test across four writing systems (Latin, Han, Han+kana, Arabic). The drop is not a capacity bottleneck. A 6x vision-backbone scale-up (CLIP4STR-Base 158M -> CLIP4STR-Huge 1.0B, OpenCLIP ViT-H/14 LAION-2B) leads every benchmark in aggregate accuracy yet leaves the stress corner unchanged (86.9 -> 86.5, within paired-bootstrap noise). Four converging probes--layer-wise probing, confidence-when-wrong, attention re-balancing, and a cross-script commit-vs-abstain error split--localise the failure to the autoregressive decoder's lexical prior. We then ask how much of the gap existing techniques recover. Of 16 non-architectural mitigations, the largest mean q5/q5 gain is +1.3 pt and none clears the paired-bootstrap noise floor; the only intervention that does is the architectural shift from autoregressive to CTC decoding (SVTRv2, +2.5 pt, p=0.02, n=474). A confidence-routed AR-CTC ensemble adds a directionally consistent +0.6 pt that stays within noise, and its dominant learned coefficient is each model's own minimum-softmax confidence--independently echoing the mechanism above. No configuration we test improves both the compositional corner and aggregate accuracy. The rare-input long tail thus points to architectural change rather than added capacity.

---


### 120. [Polished but Unresolved: Identifying Late-Stage Pressure States in Long-Horizon Tool-Use Agents](https://arxiv.org/abs/2609.00823)

**<font color=#1a73e8>作者：</font>** Haoyang Chen, Yi Liu, Jianzhi Shao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon tool-use agents need not only to search and plan, but also to decide when to finalize. We study late-stage pressure states, in which an agent is biased toward submitting a final answer that appears complete and polished while key constraints remain unresolved. We first train a linear probe to show that this pressure state is identifiable from the agent's hidden states. Then, we use activation interventions along this pressure direction and find that shifting the hidden states changes both the pressure score and whether the agent continues tool use or submits early. Through controlled context manipulations, we further see that the pressure is mitigated by constraint clarity and action mapping. Based on these findings, we propose Probe-Sensed Pressure Relief (PSPR), a plugin that applies lightweight pressure relief direction under moderate pressure and moves to structured organization under high pressure risk. Experiments on multiple long-horizon benchmarks show that our method consistently strengthens existing agent methods.

---


### 121. [HarnessEvolve: Learning from Reference Trajectories for Reliable Agent Self-Evolution](https://arxiv.org/abs/2609.00829)

**<font color=#1a73e8>作者：</font>** Wen Jiang, Mingmin Chu, Yimeng Tian 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-evolving agents advance toward autonomy by optimizing their harness---prompts, skills, tools, and execution logic---based on environmental feedback. This paradigm, however, is hampered by three challenges: \textit{credit assignment failure}, where terminal success/failure feedback makes it ambiguous which step caused the error; \textit{shortcut learning}, where agents memorize task-specific patterns rather than acquire generalizable capabilities; and \textit{catastrophic forgetting}, where unguarded updates degrade previously acquired competence. In this paper, we introduce HarnessEvolve, a self-evolving framework that learns from reference trajectories to achieve reliable agent self-evolution. HarnessEvolve decouples the execution agent from the evolutionary pipeline, assigning execution, evaluation, optimization, and gating to independent agent modules, enabling generalizable and stable harness improvements. Specifically, HarnessEvolve overcomes credit assignment failure by generating reference trajectories (execution paths produced when given the ground-truth answers) and aligning failed executions against them to extract error signals, which are clustered to reveal systematic failure patterns. To prevent shortcut learning and catastrophic forgetting, candidate harness updates must pass two gates: a quality gate that filters data leakage and prompt bloat, and a performance gate that accepts each update if it improves on the current batch without degrading recent batches, with epoch-end validation on a held-out set selecting the best-performing accepted agent snapshot. We conduct extensive experiments on several benchmarks spanning open-domain and enterprise scenarios, using different models and agent frameworks. Results demonstrate that HarnessEvolve consistently outperforms state-of-the-art baselines across all benchmarks and settings, confirming reliability across task domains.

---


### 122. [FLaG: Frequency-Domain Latent-attention Gated Pooling for Token Aggregation](https://arxiv.org/abs/2609.00831)

**<font color=#1a73e8>作者：</font>** Kewei Li, Rongying Zhang, Xueli Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Token aggregation converts token-level representations into fixed-dimensional sample representations, but most pooling methods operate only in the original token space. We introduce Frequency-Domain Latent-attention Gated Pooling (FLaG), a plug-in aggregation module that re-expresses encoder outputs in the Fourier domain before final pooling. FLaG represents the nonredundant rFFT spectrum through concatenated real and imaginary components, summarizes spectral tokens with learnable latent queries, derives a sample-conditioned channel gate, and reconstructs modulated token representations for downstream aggregation. We evaluate the same architecture across ESM2-based antimicrobial peptide (AMP) activity prediction, ResNet18 image classification on CIFAR-10 and CIFAR-100, and three RoBERTa-based language tasks. FLaG achieves the best macro-averaged Spearman correlation coefficient, RMSE, and Recall@50 across four AMP backbone-species settings and the highest top-1 accuracy on CIFAR 10. It also achieves the best mean results on five of seven language metrics, although mean pooling remains strongest on STSBenchmark. AMP-side mechanistic analyses reveal low-frequency prediction sensitivity across most encoder layers, with increased relative high-frequency sensitivity in the final layer, and pronounced peptide-specific positional responses. The residual gate broadly amplifies spectral channels while preserving the low-frequency-dominated energy profile, whereas latent cross-attention exhibits sample- and species-specific spectral allocation. Overall, FLaG provides a transferable frequency-domain aggregation bias across protein, visual, and textual representations, with benefits that depend on the backbone and downstream task. Supplementary materials, source code, and data are available at this https URL and this https URL.

---


### 123. [TWIX: a Two-Stage Approach for End-To-End Named Entity Recognition and Relation Extraction](https://arxiv.org/abs/2609.00832)

**<font color=#1a73e8>作者：</font>** Marco Martinelli, Laura Menotti  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The exponential growth of scientific publications calls for automatic Information Extraction (IE) systems to support knowledge discovery. In this context, the GutBrainIE benchmark evaluates Named Entity Recognition (NER), Named Entity Recognition and Disambiguation (NERD), and Relation Extraction (RE) systems in the gut-brain axis domain. We propose Two-stage Workflow for Information eXtraction (TWIX), an end-to-end IE pipeline featuring three interconnected modules, each leveraging a two-stage framework to solve all four GutBrainIE subtasks. Evaluation on the development and test sets shows that our method substantially outperforms the baseline by a wide margin, while also ranking first among all participant submissions across all subtasks. These results indicate that the proposed two-stage pipeline effectively improves both precision and recall in practical settings.

---


### 124. [Dense Process Supervision for Search Agents via Fact Utility Estimation](https://arxiv.org/abs/2609.00833)

**<font color=#1a73e8>作者：</font>** Rongzhi Zhu, Xiangyu Liu, Yi Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) for search agents typically relies on outcome rewards. However, it often fails to achieve effective credit assignment, due to the unclear value of intermediate steps. It is hard to separate their contributions from the final result. In this paper, we propose a dense process supervision method based on fact utility estimation, which models the reasoning process as the accumulation of discrete evidence facts. We first extract structured facts from raw observations and organize them into an explicit fact store. To support credit assignment, we then cluster semantically equivalent facts and infer the posterior utility of each fact cluster using Bayesian estimation over group rollouts. Finally, we convert the estimated fact utilities into dense step-level rewards to guide RL training. Experiments on seven single-hop and multi-hop QA benchmarks show that our method consistently outperforms existing baselines. Ablation studies validate clear relative improvements on multi-hop QA compared to outcome reward-only training.

---


### 125. [Residual Kalman Dynamics for Event-Based UAV Forecasting](https://arxiv.org/abs/2609.00839)

**<font color=#1a73e8>作者：</font>** Per Nyblom, Hannes Ovrén, David Gustafsson  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study short- and mid-horizon UAV bounding-box forecasting on the FRED event-camera dataset. We use a constant-velocity Kalman filter over a full center-size box state as a strong physical baseline, and train a residual model to predict acceleration-like corrections from recent box history, filtered state features, and local event representations. This simple residual formulation consistently improves over the Kalman baseline, with event-conditioned models giving the strongest results among the evaluated methods. We further show that part of the residual target is predictable from anchor position and velocity alone, indicating that canonical FRED results can reflect both visual evidence and dataset-specific motion priors. To analyze this effect, we introduce decorrelated subsets as a diagnostic stress test, showing that event-conditioned residual models retain useful predictive signal even when measured position- and velocity-based shortcuts are weakened.

---


### 126. [An Intelligent Decision Support System for Emotion Monitoring using Microscopic Fixational Dynamics](https://arxiv.org/abs/2609.00846)

**<font color=#1a73e8>作者：</font>** Xiangyu Shen, Feiyang Deng, Zijian Dai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rising prevalence of psychological disorders necessitates effective emotion monitoring, yet current methods relying on facial or physiological signals often suffer from intrusiveness and privacy issues. This paper proposes an intelligent decision support system and pervasive edge-computing framework that leverages smart glasses and a companion smartphone to infer emotional states from microscopic visual fixation patterns. Moving beyond traditional macroscopic gaze metrics, the proposed system extracts and decomposes three distinct neurophysiological micro-movements: microsaccades, ocular drifts, and ocular microtremors. We introduce an interpretable hybrid artificial intelligence pipeline combining a multi-head attention mechanism, extreme gradient boosting, and a support vector machine to extract deep temporal features, quantify their physiological importance, and perform efficient on-device classification. Through an extensive evaluation involving 60 volunteers, we rigorously validate the framework under a strict leave-one-subject-out cross-validation protocol across both controlled and naturalistic mobile scenarios. Ablation studies unequivocally demonstrate that these fixational micro-movements are substantially more discriminative for emotion inference than traditional macroscopic features. Furthermore, aligned with contemporary affective science, the system incorporates a few-shot personalization mechanism to bridge universal physiological baselines with individual emotional heterogeneity, achieving a highly robust personalized F1-score of 83.6%. This work establishes a physiologically interpretable, unobtrusive, and deployable paradigm for continuous real-time emotion monitoring.

---


### 127. [ADGNet: Asymmetric Dual-text Guided Network for Infrared Small Target Detection](https://arxiv.org/abs/2609.00853)

**<font color=#1a73e8>作者：</font>** Tongtong Wang, Mingzhu Xu, Chenglong Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> InfRared Small Target Detection (IRSTD) is a challenging task. Relying solely on pixel-level information, vision-only methods struggle to distinguish targets from clutter. Current multimodal methods typically describe both targets and backgrounds with a single textual prompt. Such an approach lacks dedicated regional guidance and ignores infrared semantic asymmetry. Consequently, it provides insufficient background suppression information and introduces severe feature optimization conflicts, overwhelming small targets with noise. To address these issues, we propose a novel Asymmetric Dual-text Guided Network (ADGNet). Specifically, accounting for the infrared semantic asymmetry, we first design the Asymmetric Dual-text Prompt (ADP), comprising an image-agnostic abstract target prompt and an image-specific detailed background prompt. To leverage these prompts, we introduce an Asymmetric Dual-Branch Interaction (ADBI) module to separately guide visual features with their respective text priors, protecting targets from noise while suppressing background clutter. Subsequently, we introduce an Adaptive Feature Aggregation (AFA) module to dynamically fuse features from the two branches. Furthermore, we construct a multimodal Asymmetric Image-Text Infrared (AITIR) dataset by providing asymmetric text annotations for three public datasets (IRSTD-1K, NUDT-SIRST, and SIRST). Extensive experiments demonstrate that ADGNet outperforms 21 state-of-the-art (SOTA) methods. Code is available at this https URL.

---


### 128. [Training-Free Inpainting Across Domains with a Frozen Text-to-Image Diffusion Model](https://arxiv.org/abs/2609.00862)

**<font color=#1a73e8>作者：</font>** Zhenhuan Wang, Fengyi Yuan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We show that a frozen generic text-to-image diffusion model can perform conditional inpainting across three evaluated natural-image domains with one fixed controller configuration, without inpainting-specific weight training, dataset-specific weight adaptation, or learned inpainting-specific conditioning channels. Step-PI augments known-region projection with boundary-interior latent feedback, persistent PI state, and a predefined four-field release schedule that modulates controller signals along the reverse trajectory. Developed only on Main35-disjoint CelebA-HQ pilots, the controller transfers unchanged to AFHQ and Places2. Across two field-identical comparisons on the same 3,500 cases, adding persistent state and replacing uniform release with the predefined schedule each improve all 15 dataset-metric cells; 95% bootstrap intervals exclude zero for all five metrics in both comparisons. In descriptive native-route comparisons, Step-PI leads LanPaint and PILOT (the closest evaluated training-free baselines using vanilla SD1.5) on all five equal-dataset macro metrics. Inpainting-trained systems retain the absolute metric leads but rely on substantial inpainting-specific offline optimization. Our method provides a complementary approach for repurposing a frozen generic text-to-image model for cross-domain inpainting through test-time latent control.

---


### 129. [Conditional Flow Matching for ML-Based Inverse Design Problems](https://arxiv.org/abs/2609.00863)

**<font color=#1a73e8>作者：</font>** Juliana Felder, Milad Habibi, Soheyl Massoudi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Engineering inverse design is often limited by the high computational cost of iterative solvers for optimization problems constrained by partial differential equations (PDEs) and by their sensitivity to initialization. Deep generative models can produce candidate designs without rerunning the simulator at inference time. Generative adversarial networks (GANs) sample in one forward pass, whereas diffusion models require iterative reverse-time integration.
In this work, we add conditional flow matching (CFM) to EngiOpt and compare it with a conditional diffusion model and a conditional generative adversarial network (cGAN) on structural (beams2d) and thermal (heatconduction2d) benchmarks from EngiBench using the same downstream optimization protocol. We use cumulative optimality gap (COG) and final optimality gap (FOG) as the primary metrics for evaluating the generated designs as warm starts for gradient-based refinement. On the evaluated EngiOpt implementations and two EngiBench tasks, CFM achieves the lowest measured COG, FOG, maximum mean discrepancy (MMD), and volume-fraction deviation on both tasks. CFM has mean volume-fraction deviations of 0.4% and 1.0% on beams2d and heatconduction2d, respectively, compared with 3.8% and 11.2% for diffusion. At Euler s = 16, CFM achieves 53.2 samples/s on beams2d, about 66 times the measured throughput of the evaluated diffusion baseline using 1000 network evaluations under the same timing protocol, with COG 1.182 +/- 3.126, compared with 1.173 +/- 3.100 for Euler s = 32.
Across the two tasks, CFM produces warm starts with lower measured COG than both baselines and uses fewer network evaluations than diffusion.

---


### 130. [Beyond the Clock: Measuring the Value of Adaptive Revision](https://arxiv.org/abs/2609.00874)

**<font color=#1a73e8>作者：</font>** Ayushi Chadha  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As agentic systems become compound systems, increasingly important decisions move above task execution itself: when should a higher-level controller preserve the strategy guiding another process, and when should it revise it? We study this meta-level control problem in a hierarchical latent reasoner whose manager can retain or replace a commitment governing lower-level computation. Across three precommitted training seeds, learned revision timing produces qualitatively different policies, ranging from an almost deterministic early clock to substantially more state conditioned schedule distributions, yet none outperforms the best forced timing policy evaluated on the same frozen checkpoint. This separates state dependence from decision value: a controller can vary its actions with internal state without turning that variation into a reproducible task-performance benefit. A deeper intervention study on the original checkpoint shows that timing itself is consequential and order-sensitive, while exhaustive enumeration reveals that a strong fixed schedule captures most of the measurable value available from timing at this decision budget. Counterfactual PERSIST/REPLAN diagnostics further show why score-level evidence can be misleading when predictability is dominated by decision position rather than within-position discrimination. Together, these results argue that learned meta-level control should be evaluated along three separate axes: whether its score depends on state, whether that dependence changes realized behavior, and whether those changes capture outcome value beyond a strong non-adaptive policy.

---


### 131. [FractalNet-Based Heterogeneous Federated Learning for Orbital Edge Intelligence in Satellite Mega-Constellations: A Wildfire Case Study](https://arxiv.org/abs/2609.00875)

**<font color=#1a73e8>作者：</font>** Sai Puppala, Koushik Sinha  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Satellite mega-constellations are emerging as large-scale sensing, communication, and computation fabrics, yet their learning architectures remain largely inherited from terrestrial federated learning and ground-centric mission operations--- ill-suited to satellites that differ by orders of magnitude in Size, Weight, Power, and Cost (SWAP-C), radiation tolerance, link availability, and propagation delay. We propose a heterogeneous federated learning method based on the FractalNet architecture for orbital edge intelligence. We formalize contact-window-constrained, depth-heterogeneous federated optimization and introduce a distributed path scheduler that assigns model depth as a function of SWAP-C constraints, predicted inter-satellite contacts, and training statistics. To reduce message overhead and energy consumption, each tier pools updates periodically rather than at every contact opportunity, and a three-tier agentic control plane governs in-space scheduling, anomaly escalation, and policy-governed autonomy. As a case study, we apply the framework to wildfire detection, where each orbital shell naturally learns a different semantic level of situational awareness: pixel-scale thermal anomalies at low Earth orbit (LEO), regional fire-front dynamics at medium Earth orbit (MEO), and larger-scale risk propagation at geostationary or high Earth orbit (GEO/HEO). Experiments on simulated mega-constellations validate the approach across convergence, communication efficiency, energy adaptation, scheduled-pooling savings, robustness, and latency.

---


### 132. [iPINN for Broadband CARS Phase Retrieval: A Framework for Function Approximation and Inverse Modeling Problems in Nonlinear Spectroscopy](https://arxiv.org/abs/2609.00883)

**<font color=#1a73e8>作者：</font>** Ravi Teja Vulchi, Carl Messerschmidt, Mohammadsadegh Vafaeinezhad 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Phase retrieval in broadband coherent anti-Stokes Raman spectroscopy (BCARS) is an ill-posed inverse problem. The Raman-like signal is encoded in the imaginary part of the resonant susceptibility, which mixes coherently with a non-resonant background (NRB) that varies across acquisitions. We introduce an inverse physics-informed neural network (iPINN) that predicts Lorentzian peak parameters from raw BCARS spectra and reconstructs the resonant susceptibility through a differentiable analytical forward model. A transformer encoder assigns spectral features to 24 learnable peak slots, and a multi-view consistency loss enforces invariance across NRB pattern, NRB strength, and noise. Unlike direct spectral regression approaches, the method retains accuracy under varying acquisition conditions. On a public benchmark, iPINN achieves the lowest error among the tested baselines (MAE 0.016 vs. next-best 0.046). On 28 zero-shot test spectra acquired across seven solvents and four focal positions, accuracy is depth-invariant in five of seven solvents. These results show that inverse parametric prediction with a differentiable physical decoder supports robust phase retrieval across measurement conditions.

---


### 133. [Denoising Diffusion Generative Models Secretly Calculate Attentions](https://arxiv.org/abs/2609.00885)

**<font color=#1a73e8>作者：</font>** Farzan Haddadi, Leila Monfared, Ebrahim Rezaii 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Denoising diffusion models are the dominant architecture for image generation, whereas most natural language generation and modeling are primarily handled by well-known transformer architectures employing attention mechanism. Here, we show that diffusion models also inherently use an attention mechanism very similar to that of transformers. Therefore, attention emerges as a universal machine learning principle, based on a general training objective. We also show similarities in basic functional principle of auto-encoders and attention-based models. These equivalences allows us to interchange these designs based on practical requirements. As an example, we can reformulate the diffusion framework to reduce the lengthy training process and computation-intensive image generation. Using this approach, a simplified algorithm is proposed for image generation which is based on attention mechanism. Results show that the attention-based implementation achieves comparable performance with significantly less effort and computational resources.

---


### 134. [Poisson-Gamma Dynamical Systems with Time-varying Transition Dynamics](https://arxiv.org/abs/2609.00896)

**<font color=#1a73e8>作者：</font>** Jiahao Wang, Yijun Wang, Nan Fang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian methodologies for handling count-valued time series have gained prominence due to their ability to infer interpretable latent structures and to estimate uncertainties. Among these Bayesian models, Poisson-Gamma Dynamical Systems (PGDSs) are proven to be effective in capturing the evolving dynamics underlying observed count sequences. However, the state-of-the-art PGDS still falls short in capturing the transition dynamics that are commonly observed in real-world count time series. To mitigate this limitation, a PGDS with time-varying transition kernel (TV-PGDS), is proposed to allow the underlying transition matrices to evolve over time. Three specifically-designed Dirichlet Markov chains (Dir-Dir, Dir-Gam-Dir, PR-Gam-Dir) are constructed to accommodate heterogeneous structural mutations within these dependencies. Leveraging Dirichlet-Multinomial-Beta data augmentation techniques, a fully-conjugate and efficient Gibbs sampler is developed to perform posterior simulation. Experiments show that, in comparison with related models, the proposed PGDS achieves improved predictive performance due to its capacity to learn time-varying dependency structure captured by the time-evolving transition matrices.

---


### 135. [Vision-Language-Guided Pseudo-Labels for Unsupervised Domain Adaptation in Semantic Segmentation for Waste Sorting](https://arxiv.org/abs/2609.00898)

**<font color=#1a73e8>作者：</font>** Udo Schlegel, Shubhangi, Gabriel Dax 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Obtaining labeled data for semantic segmentation in applied settings (e.g., autonomous driving, industrial waste sorting) is expensive and often infeasible at scale. We present a cross-modal pseudo-labeling pipeline that enables unsupervised domain adaptation without any target-domain annotations. The pipeline is built on two core foundation models: SAM generates class-agnostic region proposals, and EVA-CLIP assigns semantic labels based on region-text similarity, with confidence filtering ensuring that only reliable pseudo-labels are used for self-training a segmentation model. As an optional extension, BLIP provides language-grounded verification for ambiguous regions, thereby improving pseudo-label quality without altering the overall pipeline. Evaluated on two domain shifts, synthetic-to-real autonomous driving and, with a primary focus, lab-to-factory industrial waste sorting, the pipeline consistently improves over source-only baselines. Our results demonstrate that pseudo-label quality, not quantity, is a decisive factor in self-training under domain shift, and that cross-modal language grounding offers a practical path to reliable automatic annotation in deployment-critical applications.

---


### 136. [HELIOS: From midnight to noon, continuous outdoor urban scene relighting](https://arxiv.org/abs/2609.00901)

**<font color=#1a73e8>作者：</font>** Hala Djeghim, Nathan Piasco, Luis Roldão 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modifying the illumination of driving images is a fundamental challenge, as most datasets are captured at specific times of day. Existing methods rely on synthetic data or paired multi-illumination supervision, which limits their generalization to the diverse and challenging conditions of real-world scenarios. To address this, we propose HELIOS, a novel image relighting approach that relies on unlabeled real-world datasets without requiring any paired images for training. Our approach integrates albedo-based conditioning into a cycle-consistent diffusion pipeline to prevent identity collapse and ensure accurate domain translation. To handle low-visibility nighttime conditions, we introduce a robust albedo distillation strategy that transfers structural stability from the daytime domain. Additionally, we replace traditional text prompts with a fine-grained control mechanism based on GPS-derived solar angles, enabling smooth and continuous lighting manipulation across the day-night cycle. Through extensive evaluation and a user study, we demonstrate that HELIOS produces structurally consistent and realistic results in both night-to-day and day-to-night tasks, outperforming state-of-the-art methods.

---


### 137. [On-the-Fly3R: Towards Robust Online 3D Reconstruction with Feed-Forward 3R Models for Large-Scale UAV Scenarios](https://arxiv.org/abs/2609.00923)

**<font color=#1a73e8>作者：</font>** Zhe Shen, Liyuan Lou, Yifei Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While feed-forward 3D reconstruction (3R) offers efficient end-to-end modeling, its application in large-scale UAV mapping is hindered by the prohibitive memory cost of Transformer attention. Current scalable streaming 3R methods assume temporally and spatially continuous inputs, rendering them ineffective for the weakly ordered or unordered image streams common in cross-strip UAV operations. To address this, we propose On-the-Fly3R, a training-free, progressive online 3D reconstruction framework for large-scale UAV images that upgrades various 3R backbones for large-scale UAV scenarios. Our method enables reconstruction from unordered inputs via retrieval-guided dynamic subset construction, which adaptively selects spatially relevant images. To further improve the robustness, a validation-rejection-retry mechanism is designed to guarantee global consistency, performing a pre-integration consistency check and automatically rejecting misaligned images and retrying with alternative subset. Finally, inspired by VSLAM, pose graph optimization based on the retrieval loop closure is employed to mitigate camera drift. Evaluations on several UAV benchmarks show that our On-the-Fly3R successfully scales various 3R models to over 5,000 images across square-kilometer UAV scenes, delivering substantially superior accuracy compared to several SOTA streaming 3R methods. Code is available at this https URL

---


### 138. [Beyond the Image Plane: World-Grounded Queries for Multi-Object Tracking](https://arxiv.org/abs/2609.00924)

**<font color=#1a73e8>作者：</font>** Orcun Cetintas, Guillem Brasó, Tim Meinhardt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular videos record 3D scenes as sequences of 2D image-plane projections, obscuring depth and spatial relationships. Multi-object trackers localize and associate objects primarily using appearance and geometry observed only in the image plane, inheriting these ambiguities. To address this limitation, we introduce PLANET, an end-to-end multi-object tracker designed to move beyond the image plane. As an enabling step, we lift existing 2D tracking datasets into 3D. We then form world-grounded queries by embedding reconstructed 3D scene geometry into the features and positional encodings used during query formation. An auxiliary 3D location prediction task further encourages the queries to encode object positions during training. A complementary dual-resolution temporal memory preserves this evidence across longer temporal gaps. As a result, PLANET achieves state-of-the-art performance across three diverse benchmarks.

---


### 139. [CERF: Communication-Efficient and Retraining-Free Collaborative Perception](https://arxiv.org/abs/2609.00951)

**<font color=#1a73e8>作者：</font>** Jiuwu Hao, Ziyi Ni, Liguo Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Collaborative perception shares information among multiple agents to obtain a comprehensive scene representation, enhancing the perceptual capability of individual agents. However, most existing methods rely on transmitting and fusing dense feature maps for collaboration, which incurs inevitable communication overhead and heterogeneity challenges, limiting their practicality for real-world deployment. To address these challenges, we propose CERF, a novel Communication-Efficient and Retraining-Free framework for open heterogeneous collaborative perception. In CERF, we introduce a new virtual modality (termed Poture), which is generated from the perception outputs of other agents, to augment the extracted Bird's Eye View (BEV) features of the ego agent. To mitigate transmission delays, we employ a Kalman-filter based tracker and a motion forecasting model to derive the current predictions from historical perception results. Extensive experiments demonstrate that CERF achieves performance comparable to mainstream intermediate-collaboration methods while reducing communication overhead by 95% across various downstream tasks. Furthermore, CERF enables seamless integration of unknown heterogeneous agents into the existing collaborative framework without additional retraining costs. Code is available at this https URL.

---


### 140. [Influence of Logging Frameworks on Bind9](https://arxiv.org/abs/2609.00954)

**<font color=#1a73e8>作者：</font>** Max Schrötter, Hannes Signer, Bettina Schnor  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Host-based Intrusion Prevention Systems (IPS) rely on application logs to detect and block malicious activity. However, on modern high-speed networks the logging subsystem itself becomes a bottleneck: an attacker can hide traces simply by generating enough traffic to overwhelm the application's log pipeline, dropping crucial traces. In this work, we show that widely deployed setups such as Fail2Ban monitoring BIND9 can be defeated with less than 65 Mbps of DNS traffic. Further, we show that when replacing core components of the IPS architecture with their higher-performance equivalent, iptables with eBPF and regex matching with Hyperscan, the logging backends themselves become the bottleneck. Therefore, we present FIPS, a new IPC designed for high-performance logging that bypasses the kernel and reduces copying of the log messages to a minimum. FIPS uses per-thread lock free shared memory ring buffers, supporting multiple independent consumers reading the same log stream at their own pace. FIPS offers both a native API and a drop-in replacement for the syslog interface. Our evaluation with BIND 9 shows that FIPS introduces almost no overhead compared to disabled logging, logs more requests than any other evaluated framework, and enables the IPS to ban malicious clients $2.5\times$ faster than with file logging while sustaining $2^{16}$ attacking clients at one million requests per second.

---


### 141. [ASSERT: Adaptive Stochastic Sampling for Robust Diffusion Models on Analog Compute-in-Memory Hardware](https://arxiv.org/abs/2609.00955)

**<font color=#1a73e8>作者：</font>** Yuannuo Feng, Yizhe Chen, Wenshuai Yao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models achieve strong image generation quality but incur high iterative denoising costs. Analog compute-in-memory (CIM) can accelerate matrix-vector multiplications, yet spatial memory variations perturb weights and accumulate during sampling. Unlike conventional neural networks, diffusion models' temporal sensitivity to hardware noise remains underexplored. We investigate diffusion inference using a noise model calibrated and validated against measurements collected from multiple physical CIM chips. Our results show that the early, high-noise denoising stage is substantially more vulnerable than the final refinement stage. A first-order trajectory analysis attributes this behavior to the repeated propagation of correlated prediction errors induced by a fixed hardware mapping. Based on this observation, we propose ASSERT, a training-free sampler that uses higher stochasticity early and smoothly transitions to deterministic denoising. The injected stochasticity changes subsequent activation trajectories and thereby reduces their alignment with persistent spatial errors. Across the evaluated settings, ASSERT achieves up to 2.58$\times$ lower FID than deterministic DDIM on high-resolution datasets and 7.68$\times$ lower FID in the CIFAR-10 step-count study, without changing model parameters or the number of network evaluations.

---


### 142. [PredErase: Training-Free Object-and-Effect Removal with Predictive Latent Guidance](https://arxiv.org/abs/2609.00956)

**<font color=#1a73e8>作者：</font>** Waikit Xiu, Qiang Lu, Junbiao Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Removing an object is not the same as filling its mask. Cast shadows and contact shading usually lie outside the user-provided instance mask M_obj, so a frozen Fill model that edits only that mask leaves the object's photometric footprint on nearby surfaces. Supervised removers learn this joint erasure from paired clean plates. Training-free editors freeze pretrained weights, yet most still treat M_obj as the entire editable support and steer sampling with CLIP or DINO energies that do not predict the occluded scene. We present PredErase, a training-free inference procedure on frozen FLUX.2 and I-JEPA. The method separates where Fill may rewrite pixels from what structure should occupy the hole. A contact-band expansion M_flux of M_obj exposes local residuals on the supporting plane. I-JEPA, pretrained for masked token prediction, supplies a context-conditioned hole target in representation space; sparse projected gradients align decoded Fill completions with that target inside the instance, while coordinates outside the packed support stay locked. Under instance-only masks on RemovalBench, RORD-Val, and DEFACTO-Val, PredErase improves the native FLUX.2 backbone. Supervised removers remain stronger on several full-image appearance metrics; the supported claim is training-free object-and-effect editing of frozen Fill, not replacement of paired-data erasers.

---


### 143. [Candidate-Expanding Routing with Permutation-Stabilized Experts for Mixed-Format Medical VQA](https://arxiv.org/abs/2609.00959)

**<font color=#1a73e8>作者：</font>** Hai-Dang Nguyen, Huy-Hieu Pham  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mixed-format medical visual question answering (VQA) requires stable option selection and machine-readable free-text output. The two formats fail differently: multiple-choice predictions can change with option symbols or positions, while clinically plausible open answers can fail automated evaluation when serialization is malformed. We address both challenges with an answer-text memory, a permutation-stabilized vision--language expert, and a sparse candidate- expanding router. The cyclic schedule follows prior work; our contribution is to make expert top-2 a routable candidate alongside memory and expert top-1. On a 1,403-case retrospective internal analysis, this expansion improves a matched binary router from 88.95% to 91.73% (+2.78 percentage points; 95% CI 1.57--3.99), with 56 rescued errors and 17 regressions. Oracle coverage rises from 90.31% to 96.15%, and the final submitted configuration reaches 92.23% on the same retrospective split. For open questions, strict generation and deterministic guards produce 475/475 schema- valid participant-facing outputs without repair, retry, or hard-gate failure. Visual ablations reveal substantial textual dependence. Candidate expansion supplies the principal controlled routing gain; open-path evidence establishes output-contract validity rather than clinical correctness in medical use or deployment.

---


### 144. [Conditional Flow Matching for Cross-Field MRI Harmonisation](https://arxiv.org/abs/2609.00960)

**<font color=#1a73e8>作者：</font>** Baris Imre, Aram Salehi, Levente Baljer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Magnetic resonance images of the same subject look markedly different across field strengths, which complicates the comparison and pooling of data across sites. We address cross-field brain-MRI translation for the MRIxFields2026 challenge, and in particular its Task~3: a single model that translates between any directed pair of the five field strengths and across three contrasts. We phrase the problem as a conditional flow matching path: because the source and target volumes are spatially registered, we learn a velocity field that carries the source slice directly to the target slice, rather than starting from noise. To learn this mapping from only three paired subjects, the unified model is trained in three stages: a degradation-bridge pretraining that distills a restoration prior from the abundant unpaired retrospective cohort, a cross-field finetuning over all directed pairs on the paired cohort, and an adversarial refinement that sharpens the output. At inference, we integrate the learned velocity with a second-order Heun solver in a handful of steps. A restoration prior learned without any paired data already reaches a mean SSIM of 0.837, and each subsequent training stage improves on it. A single 6.3M-parameter model thereby covers all 60 field-pair and contrast combinations, with inference in five solver steps per slice. On the challenge evaluation set the model reaches a mean SSIM of 0.909, averaged over the three contrasts, outperforming regression and diffusion baselines built on the identical network on all three challenge metrics.

---


### 145. [Few-Shot Out of Domain Intent Detection with Covariance Corrected Mahalanobis Distance](https://arxiv.org/abs/2609.00961)

**<font color=#1a73e8>作者：</font>** Jayasimha Talur, Oleg Smirnov, Paul Missault  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conversational agents like chatbots and voice assistants are trained to understand and respond to user intents. On encountering an utterance with an intent different from the ones they have been trained on, these agents are expected to classify the intent as `unknown' or `out of domain'. This problem is known as out of domain (OOD) intent detection. Podolskiy et al. (2021), showed that Mahalanobis distance can be used effectively for identifying OOD intents, outperforming competing approaches. However, their method fails to outperform the baselines in the practically important few-shot setting. In this paper we analyze the reason for low performance and propose a covariance corrected Mahalanobis distance for detecting out-of-domain intents.

---


### 146. [ReFlowSET: Representation-Aligned Latent Flow Matching for SAR-to-EO Image Translation](https://arxiv.org/abs/2609.00968)

**<font color=#1a73e8>作者：</font>** Jeonghyeok Do, Seungchul Lee, Munchurl Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> SAR-to-EO image translation aims to generate electro-optical (EO) imagery from synthetic aperture radar (SAR) observations. Existing latent diffusion approaches typically inherit a predetermined autoencoder, although reconstruction fidelity can vary substantially across codecs and modalities. Because the latent codec affects the round-trip preservation of both SAR conditions and EO targets, codec selection constitutes a fundamental design choice; nevertheless, existing methods largely rely on codecs pretrained on natural images. To remedy this, we introduce ReFlowSET, a conditional latent flow-matching framework that selects its codec through a joint SAR--EO reconstruction audit. Rather than inheriting a heavyweight pretrained generator, ReFlowSET trains a substantially smaller conditional DiT from scratch in the selected latent space, using dual-stream SAR conditioning followed by joint feature refinement. To provide semantic guidance for this from-scratch training, intermediate noisy-EO features are aligned with clean target-EO representations extracted by a frozen vision foundation model. This alignment is used only during training and introduces no additional inference cost. Experiments on QXS-SAROPT and SAR2Opt demonstrate state-of-the-art performance across diverse perceptual fidelity and distributional metrics. Code and pretrained weights are publicly available at this https URL.

---


### 147. [Semi-Supervised Virtual Staining via Morphology Preservation and Histopathological Realism Constraints](https://arxiv.org/abs/2609.00984)

**<font color=#1a73e8>作者：</font>** Baoshun Wang, Weiping Lin, Linwu Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Virtual staining aims to computationally generate target-stained histopathological images while reducing the cost and time associated with conventional staining procedures. However, existing methods rely predominantly on strictly paired and accurately registered training data, which are difficult and expensive to obtain in routine practice. To reduce this dependence, we propose a stable semi-supervised virtual staining framework that jointly exploits both limited paired data and abundant unpaired source images. Directly incorporating unpaired images is challenging because their generated results lack corresponding targets for supervision, potentially leading to unrealistic staining, morphological degradation, or even training collapse. To obtain reliable supervision from these images, Hessian-derived morphology preservation extracts structural cues from each source image and constrains the generated output to retain tissue morphology. Histopathological realism constraints further guide the output toward plausible target-stain characteristics, preventing the source-derived structural supervision from degenerating into contour enhancement or simple color transformation. Together, the two components suppress structural and appearance drift, stabilize semi-supervised stain translation, and promote the preservation of diagnostically relevant information. Extensive experiments on H&E-to-IHC translation for Ki67 and HER2, as well as FFPE-to-H&E translation, demonstrate consistent improvements in image quality, morphology preservation, robustness, and downstream diagnostic performance. Code will be available.

---


### 148. [EvoGS: Modeling Deformation Evolution for Dynamic Gaussian Splatting](https://arxiv.org/abs/2609.00994)

**<font color=#1a73e8>作者：</font>** Wei Dong, Shahram Shirani, Jun Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent extensions of 3D Gaussian Splatting (3DGS) enable real-time novel view synthesis in dynamic scenes by learning time-conditioned Gaussian deformations. However, existing MLP-based methods typically estimate deformations independently at each timestamp, making them less robust to large or abrupt motions. To address this issue, we propose \textbf{EvoGS}, a 3DGS-based dynamic reconstruction framework that models Gaussian deformation as a temporal evolution process. EvoGS maintains persistent deformation states for each Gaussian, extrapolates future states from historical deformation states, and corrects the predictions with MLP-derived observations. The correction is adaptively weighted using a temporal residual memory and evolution statistics such as deformation velocity and trajectory deviation. To further improve reconstruction quality, EvoGS introduces deformation-aware densification. Clone and split operations are performed along corrected deformation directions, while an uncertainty-aware strategy suppresses densification for Gaussians with unstable deformation histories. Experiments show that EvoGS improves dynamic novel view synthesis quality and achieves competitive performance across benchmarks.

---


### 149. [CQF-HMR: Continuous Quaternion Flows for Probabilistic 3D Human Mesh Recovery from a Single Image](https://arxiv.org/abs/2609.00995)

**<font color=#1a73e8>作者：</font>** Cuong Le, Bao-Long Tran, Pavlo Melnyk 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering 3D digital humans from a single 2D image is an ill-posed computer vision problem due to the loss of depth information. Probabilistic 3D human pose estimation compensates for this by estimating a set of 3D hypotheses from a prior distribution via generative models. However, most prior work focuses only on 3D keypoints, which often leads to implausible poses that are difficult to apply to downstream tasks, e.g. animation or digital humans. SMPL-based methods are more scalable thanks to the explicit body priors, but it requires more complex modeling of the generation process due to the non-additive nature of the joint rotations. In this work, we propose a novel approach for probabilistic 3D humans using quaternion-constrained continuous normalizing flows conditioned on 2D pose estimations. Our proposed quaternion flows show significant advantages over approaches using other rotation representations. Experiments demonstrate state-of-the-art results of our method on Human3.6M, particularly in ambiguous settings, and comparable pose estimation accuracy on challenging 3DPW and EMDB benchmarks.

---


### 150. [Does This Moment Justify the Recommendation? Counterfactual Behavior-Grounded Evidence Retrieval for Personalized Video Recommendation](https://arxiv.org/abs/2609.00996)

**<font color=#1a73e8>作者：</font>** Xin Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Personalized video recommendation predicts user preference at the video level, while temporal video grounding localizes query-relevant moments. However, strong localization does not establish whether the retrieved moment constitutes valid evidence for recommending the video to a particular user. We study counterfactual behavior-grounded evidence retrieval, which separates where personalized evidence occurs from whether such evidence exists and evaluates whether model predictions respond consistently when that evidence is replaced. We introduce CBGER-10K, containing 5,000 controlled factual--counterfactual pairs for 3,026 users, where each pair replaces only the focal behavior-supported segment while preserving the user, temporal position, and hard distractors. We further propose CBGER, a compact framework that decouples segment-level localization from video-level evidence estimation and learns both through structured counterfactual supervision. CBGER achieves $0.4432$ MRR, $0.6977$ Pair Accuracy, and $0.6987$ Intervention Consistency across five adapted personalized-highlight and temporal-grounding baselines. Notably, compared with QD-DETR, its MRR improvement is not statistically significant, while Pair Accuracy improves by $11.03$ points. These results show that accurate temporal localization does not necessarily imply reliable personalized evidence existence, motivating explicit evaluation of Whether alongside Where.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-236](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
