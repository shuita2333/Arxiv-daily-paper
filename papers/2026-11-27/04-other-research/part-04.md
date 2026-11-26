# 📦 其他研究 | 2026年11月27日

> 本类共 **314** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-314](./part-07.md)

---

### 151. [The Reference Matters: Displacement Probing for Weight-Space Learning](https://arxiv.org/abs/2611.33998)

**<font color=#1a73e8>作者：</font>** Haechan Shin, Hoonki Lee, Jungwoon Kang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weight-space learning predicts a model's attributes directly from its parameters, and probing-based methods do so efficiently by reading a model's responses to learned probes. Prior work shows that probing succeeds within a Model Tree -- models fine-tuned from a shared pretrained origin -- but not why. We trace this to the shared origin itself: since a tree's leaves start from the same weights, what distinguishes them is their displacement from that origin. This motivates probing the displacement rather than the raw weight, an intervention we call the DiSplacement Probe (DSProbe). We develop this idea along two axes: extending it to second-order Gram responses, whose displacement, to first order, tracks the feature changes induced by fine-tuning; and treating the reference as a design choice, learning a shared component to subtract beyond the pretrained origin. Across four architectures on the Model Jungle benchmark, the resulting Refined-DSProbe (R-DSProbe) sets a new state of the art, matches prior accuracy with substantially fewer probes, and supports a single encoder shared across Model Trees, reducing metanetwork parameters by 3.61 times. Code is available at this https URL.

---


### 152. [ScaleCurve: From Constant Scale to Consistent Motion for World-Space Human Mesh Recovery](https://arxiv.org/abs/2611.34005)

**<font color=#1a73e8>作者：</font>** Sanghyeon Lee, Jong Taek Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World-space human mesh recovery can lose spatial consistency even when camera-space body estimates are accurate. A single sequence-wide scale resolves global scale ambiguity but cannot correct local scale distortion along a reconstructed camera path. We present ScaleCurve, a framework that estimates time-varying metric corrections from human-ground geometry. We construct scale observations by comparing predicted foot geometry with locally fitted ground planes. Joint temporal optimization downweights inconsistent observations and couples neighboring scale estimates, allowing calibration to adapt along the camera path without freely following measurement noise. We scale camera translation increments and integrate them into a calibrated trajectory. With this camera fixed, we refine the lifted body motion using 2D image evidence and pretrained 3D dynamics, while restricting global trajectory rescaling. ScaleCurve achieves state-of-the-art performance on most evaluated metrics on both EMDB-2 and SLOPER4D. Consistent gains across three HMR backbones demonstrate its compatibility with diverse body estimates without retraining. Code will be made publicly available.

---


### 153. [Manga Page Parser: Comprehensive Visual Parsing through Local Story Understanding](https://arxiv.org/abs/2611.34006)

**<font color=#1a73e8>作者：</font>** Yingxuan Li, Jiafeng Mao, Arata Furukawa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding manga requires connecting who appears and who speaks with the events, character states, and relationships that unfold across panels. We study manga visual parsing through local story understanding: analyzing each double-page spread independently to capture and organize its story information in a reusable structured representation. We propose MangaParser, an agentic reading framework that jointly performs character clustering, speaker diarization, and speaker-to-character binding within a shared multimodal conversation, without additional training or fine-tuning. The agent uses structured story memory to guide character and speaker identification, inspecting relevant image regions when uncertain and refining its predictions and story records together as evidence accumulates. Quantitative evaluations show that our parser substantially outperforms manga-specific models across multiple backbones. Parsing examples illustrate how a unified representation links the character and speaker predictions with narrative content and supporting evidence. We further test reusability through story question answering using outputs generated before the questions are provided. The results confirm output reusability, offering a foundation for manga translation, content retrieval, and question answering.

---


### 154. [Honest but Wrong: Formalizing Retraction in the Ethics of Speech Acts](https://arxiv.org/abs/2611.34011)

**<font color=#1a73e8>作者：</font>** Benjamin Icard, Gauvain Bourgne, Jeanne Bonnaventure 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A speaker who asserts honestly may later discover that its assertion was false. Such erroneous truths are not lies, yet they raise the question of whether, and on which moral grounds, the speaker must retract them. Using the FIPA-ACL performative disconfirm, we extend a belief-based framework that evaluates speech acts under deontologism and consequentialism to the case of retraction. We prove that the honesty duty of deontologism, which bears on utterances when they are made, never requires retracting an erroneous truth, and add a persistent one, which forbids letting the addressee believe what the speaker no longer believes. On a legal-advice case implemented in Answer Set Programming, we show that deontologism and consequentialism both require the retraction, but that consequentialism no longer does once it comes too late to prevent harm.

---


### 155. [CARROT: Competitive Adaptive Graph Clustering via Semi-Relaxed Optimal Transport](https://arxiv.org/abs/2611.34012)

**<font color=#1a73e8>作者：</font>** Ching Fan Chiang, Jia-Yu Pan, Wen-Chieh Lin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep graph clustering (DGC) has emerged as a prominent paradigm for unsupervised attributed graph clustering. However, existing methods often struggle with two practical challenges encountered in real-world applications: the number of clusters $K$ is unknown a priori, and cluster sizes are frequently highly imbalanced. Methods relying on a pre-specified $K$ may fail to recover the underlying clustering structure when $K$ is misspecified, while many approaches implicitly favor balanced partitions, hindering the discovery of minority clusters. We propose CARROT, a Competitive Adaptive gRaph clustering framework via semi-Relaxed Optimal Transport, which introduces semi-relaxed optimal transport into deep graph clustering to jointly address both challenges. CARROT first pre-trains node embeddings to establish a meaningful embedding space, and then jointly optimizes embeddings and cluster assignments through an Adaptive Clustering Mechanism. The mechanism combines semi-relaxed optimal transport to adapt cluster capacities to the underlying data, a competition loss to concentrate mass onto well-supported cluster prototypes, thereby starving degenerate ones, and hard pruning to progressively eliminate them. Extensive experiments on five public benchmarks demonstrate that CARROT achieves state-of-the-art NMI and ARI, accurately recovers the number of clusters without supervision, and faithfully preserves size-imbalanced community structures.

---


### 156. [Assessing the Physical Interpretability of AlphaEarth Foundation Embeddings Through Multi-Sensor Satellite Time-Series Benchmarking for Agricultural Mapping](https://arxiv.org/abs/2611.34019)

**<font color=#1a73e8>作者：</font>** El Houcine El Moussaoui, Chouaib El Hachimi, Saïd Khabba 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate and dynamic maps of agricultural LULC are important for agricultural water resource management, particularly in areas where water scarcity is prevalent, such as Morocco. Here, we evaluate the utility of AlphaEarth Foundation Model (AEF) embeddings for agricultural LULC and irrigation-type mapping in Morocco. AEF embeddings were compared to single-date and time-series remote-sensing features using three machine-learning classifiers: XGBoost, CatBoost, and TabPFN. We also evaluated whether AEF embeddings can: (a) provide an efficient and transferable alternative to conventional direct use of Earth observation products and (b) reconstruct biophysical information. Results showed that multi-temporal feature time series achieved the highest performance, with accuracies of 0.93 for agricultural LULC and 0.87 for irrigation-type mapping when using TabPFN. However, AEF embeddings yielded comparable results, achieving accuracies of 0.91 for agricultural LULC and 0.85 for irrigation-type mapping, while reducing the need for extensive data processing and manual feature engineering typically required for satellite products. Spatial LULC mapping using TabPFN achieved comparable overall accuracies (0.85-0.86) across the three feature configurations, but revealed substantial differences in mapped tree cover, ranging from 14.57% for surface reflectance to 29.79% for AFE. Physical probing revealed that AEF embeddings strongly encode spectral indices (A30-SWIR: rho=0.58-0.67), (A38-NDMI: rho=-0.72), vegetation (A49-NDVI: rho = 0.72-0.73), and SAR structure (A25-VH: rho = 0.71). Future research should focus on enhancing the interpretability of embedding-based approaches by incorporating physical knowledge to develop more transparent and trustworthy AI systems for agricultural applications.

---


### 157. [Rethinking Unsupervised Cross-Modal Homography Estimation:Spatially Aware Representations and Geometric Consistency Learning](https://arxiv.org/abs/2611.34021)

**<font color=#1a73e8>作者：</font>** Zhuoran Yang, Junchen Yu, Runmin Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsupervised cross-modal homography estimation is challenging because appearance differences obscure shared geometric structures. Separating modality transfer from homography estimation helps reduce these differences, but accurate alignment still requires effective geometric representations and consistency constraints on the two subtasks. We propose GeoCo (Geometry-Aware and Consistency-Constrained Homography Estimation), a framework that addresses these two requirements without cross-modal transformation labels. Its homography estimator, RVHomo, adapts hierarchical features from a frozen vision foundation model (VFM) and fuses them with local CNN features to capture structural context and spatial detail. Two geometric consistency constraints encourage modality transfer to preserve geometry and homography predictions to remain consistent under synthetic geometric transformations. Through two-stage progressive distillation, we further obtain GeoCo-D, which uses the lightweight RVHomo-D estimator. An intermediate model first learns to perform cross-modal matching without modality transfer, then transfers prediction and feature knowledge to the student, eliminating online VFM extraction. Experiments on GoogleMap, OPT-SAR, FSD, and VIS-IR show that GeoCo reduces mean average corner error by 17.4-46.7% relative to the best-performing baseline on each dataset. GeoCo-D also outperforms all compared baselines while using 98.5% fewer parameters and 70.4% fewer FLOPs than the complete GeoCo teacher.

---


### 158. [Incorporating the Knowledge Distillation to Improve the EfficientNet Transfer Learning Capability](https://arxiv.org/abs/2611.34025)

**<font color=#1a73e8>作者：</font>** Tjeng Wawan Cenggoro  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Due to the Deep Learning requirement for a large training dataset, Transfer Learning has become a central method in the field of Computer Vision, which heavily used Deep Learning. Since the adoption of transfer learning in the field, the performance of the models in computer vision is significantly upgraded. The common transfer learning practice in computer vision research is to use state-of-the-art architectures in the ImageNet dataset as the backbone network. The best performing architecture in ImageNet is currently held by EfficientNet, which is a set of architectures that were progressively grown from a baseline architecture.
By observing the EfficientNet development approach, it is natural to hypothesize that the smaller EfficientNet architecture is capable to contain the knowledge of the larger architecture. This hypothesis comes from the fact that the larger EfficientNet architecture was grown from the smaller architecture. Therefore, in this study, we experimented if it is beneficial to transfer the knowledge from the larger architecture to the smaller architecture of the EfficientNet. To achieve this goal, we proposed a transfer learning method that uses Knowledge Distillation as the knowledge transfer mechanism from the larger to smaller architecture. We found that the proposed method is able to upgrade the performance of each of the EfficientNet architecture. Several smaller architectures are even able to outperform the larger architecture that was trained using the standard transfer learning method.

---


### 159. [ContextHands: Completing Hand Motion with Learned Context and Joint-Specific Body Kinematics](https://arxiv.org/abs/2611.34027)

**<font color=#1a73e8>作者：</font>** Taewoo Kim, Seunghun Koh, Hyosup Shin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detailed hand motion contributes to the realism and expressiveness of generated human motion. Completing these details from body motion and language requires connecting the context of an action to the articulation of the hands. We introduce ContextHands, which completes hand motion from an observed body sequence and text descriptions assigned to hands and time intervals. Our approach learns probabilistic hand features from the descriptions and body motion, using auxiliary hand prediction to connect these features to hand articulation. A body encoder preserves joint and body-part features across multiple temporal scales, allowing each hand joint to query these features for joint-specific body information. The diffusion generator combines this joint-specific body information with the learned hand context. Both encoders and the generator are trained jointly, so the final generation objective also shapes the context features. Experiments on the OakInk2 dataset show that ContextHands generates more accurate hand motion and achieves lower Fréchet Hand Distance than existing hand-motion and general human-motion generation methods adapted to the task. In qualitative examples of grasping and tool use, ContextHands more closely reproduces the detailed hand poses in the reference motion. We will release our code and pretrained models to support further research.

---


### 160. [Counter-DECEIVR: Counterfactual Explanations for Deepfake Detectors using Detector-Guided Rectified Flow Inversion](https://arxiv.org/abs/2611.34032)

**<font color=#1a73e8>作者：</font>** Mariano V. Ntrougkas, Vasileios Mezaris, Ioannis Patras  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep-learning-generated media are increasingly passed off as real, driving an arms race between image generators and deepfake detectors. Trust in the latter is limited by their often black-box nature; and, while region-based explanations can sometimes be extracted, these become less useful as generation quality improves. Counterfactual examples, which show the minimal change that flips a detector's decision, reveal what evidence drives a verdict, helping analysts decide whether to trust it. This work introduces Counter-DECEIVR (DEtector-guided reCtifiEd flow InVeRsion for counterfactuals), a novel training-free framework that generates counterfactual examples. Counter-DECEIVR steers latents in the velocity field of a rectified flow model using gradients from off-the-shelf deepfake detectors, without training a generator or adapting the detector; unlike prior methods, it requires no per-instance or per-detector fitting and no diffusion training on the target data. It also leverages the detector's explanation maps to concentrate editing to salient regions, turning low-level feature importance into localised counterfactual edits. A single parameter controls the strength of the edits. Across two deepfake detectors and two widely used forensics datasets, Counter-DECEIVR outperforms prior counterfactual generation methods, including training-based ones. Code will be made available upon acceptance.

---


### 161. [Post-Training Policy Replication for Strategy-Following Multi-Agent Deep Reinforcement Learning across Team Sizes](https://arxiv.org/abs/2611.34035)

**<font color=#1a73e8>作者：</font>** Yamato Takahagi, Yoshinari Motokawa, Toshiharu Sugawara  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Although multi-agent deep reinforcement learning enables coordinated behavior, aligning it with managerial intent remains difficult due to complex agent interactions. Although the strategy-following distributed attentional actor architecture (sfDA7-X) improves controllability via regional instructions, instruction combinations scale exponentially with team and instruction sizes, leading to prohibitive training costs and poor transferability. To reduce this computational cost, we introduce a team-size-independent observation architecture and reconstruct collective behavior by replicating a single trained policy across agents in teams of different sizes, thereby eliminating the need to train from scratch. Additionally, we evaluate warm-start retraining by initializing policy networks with a pre-trained policy to significantly lower computational overhead. In an object collection game, a policy trained in a four-agent team is deployed to teams of three to eight agents. Experiments demonstrate that training with the proposed aggregated observation matrix achieves performance comparable to that of the baseline method, sfDA7-X. Furthermore, policy replication preserves performance without substantial degradation in three- and five-agent teams, and warm-start retraining outperforms training from scratch while reducing required training episodes by up to 90%. Deployments to six- and eight-agent teams further confirm effective spatial region allocation following given instructions. These results demonstrate that the proposed method enables zero-shot collective behavior reconstruction via policy replication.

---


### 162. [Decentralized Clustered Federated Learning for Cellular Traffic Forecasting over LEO Constellations](https://arxiv.org/abs/2611.34049)

**<font color=#1a73e8>作者：</font>** Jonas Kirch, Tiago Koketsu Rodrigues, Yuichi Kawamoto  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low Earth Orbit (LEO) satellite constellations are positioned to act as orbital edge-compute nodes in emerging 6G non-terrestrial networks, supporting forecasting and control tasks for ground cellular infrastructure. However, training such models is challenged by heterogeneous ground-cell traffic patterns, intermittent links to ground stations, and the satellites' own orbital motion, which continuously shifts the data each satellite observes. In this work, we extend Decentralized Federated Clustering (DFCA) to the LEO setting and apply it to cellular internet-traffic forecasting on the Telecom Italia Milan+Trentino dataset. Satellites cooperate exclusively through $k$-nearest inter-satellite gossip with no ground-side aggregator, while zero-shot head selection lets each satellite specialize to the latent traffic regime of the ground cell currently beneath it. Averaged over $K{=}20$ post-training orbital snapshots, our extension reduces forecasting Root Mean Squared Error (RMSE) by $15.3\%$ over a decentralized FedAvg baseline of equivalent capacity, with cluster recovery accuracy of $85.3\%$. The results indicate that clustered specialization yields measurable gains under the structural heterogeneity inherent to realistic cellular-over-LEO scenarios.

---


### 163. [CARE-WM: Same-Horizon Self-Conditioning with Constraint-Adaptive Regularization for Latent World Models](https://arxiv.org/abs/2611.34054)

**<font color=#1a73e8>作者：</font>** Yuchen Lin, Kai Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Planning with latent world models requires both accurate multi-step predictions and latent distances that reflect physical proximity to the goal. However, models are typically trained on ground-truth observations but must rely on their own imaginations during planning, while closer latent distances do not necessarily correspond to better task outcomes. Existing methods resort to auxiliary training objectives or additional task-cost readouts, which respectively incur extra training overhead or leave the latent geometry itself misaligned with task cost. We introduce CARE-WM, a drop-in training method that meets both requirements without additional supervision, a separate cost model, or any change to LeWM's architecture and Euclidean-cost planner. CARE-WM trains the predictor on its own predictions and adaptively calibrates the strength of latent regularization. With a single hyperparameter configuration, CARE-WM improves mean planning success over LeWM across all evaluated continuous-control tasks and matches or exceeds the best results of other LeWM-family methods on most tasks. Further analyses show lower open-loop latent prediction error and closer agreement between latent-cost rankings and physical task costs.

---


### 164. [Understanding Diffusion Acceleration: Methods, Trade-Offs, and Open Questions](https://arxiv.org/abs/2611.34056)

**<font color=#1a73e8>作者：</font>** Xiaofeng Mao, Fu-yun Wang, Le Zhuo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion and flow-based generative models support high-quality image, audio, and video synthesis. Sampling can require dozens to hundreds of denoiser evaluations, with each pass becoming more expensive as resolution, video length, or model size increases. This cost affects latency and energy use in interactive and edge applications. We examine four approaches to accelerating inference: distillation, consistency training, sampling methods, and denoiser design. We express training objectives, transition maps, and numerical updates in a common notation to compare changes to the learning target, the sampling trajectory, and the work performed within each denoiser pass. Published image and video benchmarks illustrate the quality--cost trade-offs of one- and few-step generation, the interaction between solvers and timestep schedules, the effect of feature caching, and the difference between first-frame latency and sustained streaming throughput. We close with open problems in visual-native architectures and post-compression distillation, solver-aware few-step training, and semantic trajectory alignment with factorized distribution matching.

---


### 165. [Surf-Style: Surface-Based Scene Stylization](https://arxiv.org/abs/2611.34062)

**<font color=#1a73e8>作者：</font>** Wanrong Hong, Ancheng Lin, Mukesh Prasad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Consistent and controllable 3D stylization is critical for visual computing applications such as immersive visualization, augmented and virtual reality content creation, and artistic scene rendering. While 2D image stylization has advanced significantly, extending these methods to 3D remains challenging due to the need for cross-view consistency, where stylized renderings must align across all viewpoints. Applying 2D stylization independently to each rendered view often results in inconsistencies across perspectives. Existing methods attempt to improve consistency by leveraging implicit radiance field representations, which model scene appearance as a function of spatial locations. However, these methods struggle with ambiguity in updating colors, as the indirect dependence between pixel appearance and learnable scene parameters makes it difficult to enforce consistent stylization during optimization. This work presents Surface-based Scene Stylization (Surf-Style), which reconstructs object surfaces in a 3D scene and uses these surfaces to achieve geometric consistency and localized stylization. Surf-Style defines a learnable appearance model over 3D space, which is modified to replicate the visual style of a reference image. Compared to state-of-the-art methods, our method achieves superior consistency and offers greater flexibility in controllable stylization, including the ability to target specific surface regions and combine different styles.

---


### 166. [SPARC: Geometry-Guided Attention Pruning for Long-Horizon Camera-Controlled Video Generation](https://arxiv.org/abs/2611.34064)

**<font color=#1a73e8>作者：</font>** Zesong Yang, Weikai Chen, Liyuan Cui 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present SPARC, a geometry-guided attention pruning framework that turns the native self-attention of pretrained video diffusion transformers into a unified mechanism for camera control and persistent scene memory. Our key insight is that attention connectivity can simultaneously serve as geometric conditioning for camera control and spatial addressing for historical memory retrieval. Motivated by the asymmetric contextual requirements of reconstructing observed content and synthesizing novel regions, SPARC restricts observed tokens to geometrically corresponding historical tokens and local spatiotemporal context, while preserving dense attention for unobserved regions. Correspondence-aware attention biasing and order-invariant historical positioning further enable stable retrieval across long temporal gaps. Without introducing additional learnable control or memory modules, SPARC achieves precise camera adherence and faithful scene revisitation while substantially reducing attention computation. Extensive experiments demonstrate the effectiveness of aggressive attention pruning in improving camera adherence, revisit consistency, and visual fidelity, with an inference speedup of over 50x when combined with four-step distillation. Project page is available at this https URL.

---


### 167. [Hijacking 3D Generation: Targeted Adversarial Attacks against Image-to-3D Models via Prefix Trajectory Alignment](https://arxiv.org/abs/2611.34075)

**<font color=#1a73e8>作者：</font>** Yilong Yang, Jiale Teng, Yule Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online services that deploy Image-to-3D models enable users to generate high-quality 3D assets from a single image. However, the generated 3D geometry can violate content policies and cause broader security risks. To prevent such content, these services typically use policy-restricted inspectors to examine uploaded images before generation. Since the inspector examines only the visible content of the input, a visually benign image can still induce the generation of policy-restricted 3D geometry. However, turning this vulnerability into an effective attack is non-trivial in the black-box setting: global backpropagation through the long DiT generation trajectory is difficult to fit, while different image preprocessing pipelines across services can substantially reduce transferability. In this paper, we present PTA3D, a targeted adversarial attack against Image-to-3D models that addresses these challenges through Prefix Trajectory Alignment (PTA) and Preprocessing Aware Optimization (PAO). PTA progressively aligns the prefix DiT outputs of the adversarial trajectory with those of the target trajectory, where the core geometric structure is formed, allowing the final geometry to be controlled without optimizing through the complete generation trajectory. PAO exposes adversarial optimization to diverse image transformations rather than a single preprocessing pipeline, reducing sensitivity to the mismatch between surrogate and target services. We establish a prefix-to-output bound and a preprocessing-aware transfer bound to theoretically characterize the effectiveness of the two designs. Experiments on three open-source Image-to-3D models and three online services show that PTA3D achieves 41.5%-88.5% ASR on online services and 90.8%-94.6% ASR in white box settings, substantially outperforming existing attacks.

---


### 168. [WorldBridge: Bridging Scattered Views for Coherent 3D World Generation](https://arxiv.org/abs/2611.34079)

**<font color=#1a73e8>作者：</font>** Weilong Yan, Jingyu Hu, Hongli Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating coherent and explorable 3D worlds from scattered images with little or no visual overlap is a fundamental and long-standing challenge in computer vision, which existing geometry-aware methods fail to address. Meanwhile, existing image- and video-based methods may generate unseen regions but produce inconsistent geometry across views. To bridge this gap, we present WorldBridge, a framework for coherent and controllable 3D world generation under scattered images with little or no visual overlap. WorldBridge encodes scattered references into a global scene context to guide geometry and appearance generation across views. Our temporal and spatial reference attention mechanism further enhances the fidelity of temporal references along the target trajectory and supports flexible spatial references outside it. A plug-and-play latent-reference consistency strategy improves reference fidelity through reprojection-guided test-time optimization. We also introduce the WorldBridge benchmark suite to evaluate 3D world generation from scattered, low-overlap references, which is rarely explored by current benchmarks. Both qualitative and quantitative results demonstrate that our method enables controllable and coherent 3D world generation, surpassing the existing state-of-the-art solutions. Our project page is available at this https URL.

---


### 169. [TaCo: Rethinking Correlation for Visual Tracking on Edge Devices](https://arxiv.org/abs/2611.34084)

**<font color=#1a73e8>作者：</font>** Qingmao Wei, Fagui Liu, Quan Tang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lightweight trackers have replaced cross-correlation with attention, and on low-power edge hardware they pay for it, since memory-bound softmax, normalization and reshaping operators of attention cost far more time than their arithmetic suggests. Benchmarking efficient trackers on an edge Neural Processing Unit (NPU) and an Arm CPU under one numerically validated protocol, we find that correlation trackers are the fast ones, but they lag in accuracy unless they adopt a ViT backbone, which brings attention back. We revisit what correlation lacks. Template--search interaction serves two roles: conditioning the search features on the target and matching them against it spatially. Attention does both, whereas correlation only matches, and does so on features extracted without knowledge of the target. We present TaCo (Target-aligned Correlation), which supplies the missing conditioning without attention by letting the template enter the per-frame network only as operands computed once per video. A descriptor of the target scales and shifts the search features channel by channel inside the backbone, and kernels aligned with the target box, each with a weight predicted from the template, correlate with them in one matrix product. With the backbone fixed, our correlation remains essential while incurring negligible NPU overhead, offering a better speed-accuracy trade-off than the attention-based interactions we tested. TaCo-T achieves 62.3% LaSOT AUC at 184 FPS on the Rockchip RV1126B NPU and 96 FPS on a Raspberry Pi 5 CPU, 3.0x and 3.5x the NPU speed of HiT-Tiny and AsymTrack-T at higher accuracy. TaCo-B reaches 65.6% at 50 FPS on the NPU, more than twice the speed of HiT-Base, AsymTrack-B and LightFC-vit, again at higher accuracy. Code and models are available at this https URL.

---


### 170. [Feature Engineered Reinforcement Learning for S-pair Selection in Buchberger's Algorithm](https://arxiv.org/abs/2611.34088)

**<font color=#1a73e8>作者：</font>** Uzma Shafiq, Matthew England, Nayyar Zaidi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Selecting the order in which to process S-pairs is a crucial decision in Buchberger's algorithm for computing Groebner bases: this choice can change the cost by orders of magnitude. Recent work has shown that reinforcement learning agents viewing exponent vectors of the polynomials outperform classical heuristics on binomial ideals. We extend this line of work to general polynomial ideals by using statistical features. We introduce a 17-dimensional feature vector to describe a polynomial and use PPO to train policies on five distributions of random ideals. We find that using S-polynomial features significantly outperforms S-pair features on all five distributions. The new policies also outperform the retrained RL baseline on all five distributions, reducing algorithmic work by 41--53\% relative to the degree heuristic on four distributions where learning helps. The additional cost of the feature engineering means that wall-clock cost remains similar to the baseline, but our new approach benefits from easier transfer to unseen distributions.

---


### 171. [Disciplined Anthropomorphism: How to Extend Cognitive Language to Artificial Intelligence](https://arxiv.org/abs/2611.34090)

**<font color=#1a73e8>作者：</font>** Matthieu Queloz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Researchers increasingly describe AI in cognitive terms such as "understanding" and "believing", while critics denounce this as wishful anthropomorphism. Both sides align in taking a subsumptive approach, however: they ask whether AI systems fall under concepts minted for human beings, reporting verdicts as discoveries about those systems when they are largely determined by conceptual frames. Yet the problem AI poses is precisely the problem of how to conceptually frame these systems, and the explosive rise of anthropomorphism is best seen as a response to this problem that needs disciplining rather than discouragement. A disciplined anthropomorphism, I argue, should disentangle the inferential connections bundled up in our cognitive concepts and ask which connections to preserve, sever, or forge for AI. The disciplining then comes, on the one hand, from the human conceptual needs that give point to the drawing of these connections and motivate the concepts' extension in the first place; and, on the other hand, from empirical and especially mechanistic evidence that supports and constrains these connections. By reverse-engineering a concept's point in relation to a particular need before re-engineering it to better serve that point in our dealings with AI, anthropomorphizing extensions can be point-based, transposing the work those concepts do for us while revising the inferential workings through which they do it. Transposing human-tailored conceptions of understanding and belief on the pivot of the underlying conceptual needs gives us just the definitional freedom required to accommodate how AI systems differ from us, yielding conceptions that are not just thinned-out versions of existing ones, but potentially richer and better fitted to the peculiarities of AI.

---


### 172. [Exploring the Design Factors of Pixel-space Diffusion](https://arxiv.org/abs/2611.34093)

**<font color=#1a73e8>作者：</font>** Mang Ning, Le Zhang, Albert Ali Salah 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we introduce EiT by exploring the key design factors of pixel-space diffusion from three perspectives: model architecture, representation, and frequency domain. Inspired by Denoising Autoencoders (DAE) which perform denoising through a bottleneck, we construct a U-shaped pixel diffusion transformer that performs explicit compression along the channel dimension. In terms of representation, we find that both pixel and latent diffusion transformers exhibit a three-stage representation dynamics across layers and timesteps: denoising/local feature expansion, basis lift-up, and posterior projection. Moreover, earlier denoising and a longer basis lift-up stage are associated with better generation, which EiT naturally achieves through its channel bottleneck and increased network depth. From the frequency perspective, we establish the equivalence between pixel-space and frequency-space diffusion when keeping the network operating in pixel space. On ImageNet $256\times256$ and $512\times512$, EiT consistently outperforms JiT (Just image Transformers) in generation quality. Specifically, our EiT achieves better FID than JiT: 1.61 vs. 1.85 at $256\times256$, and 1.73 vs. 1.99 at $512\times512$. Remarkably, EiT can be seamlessly applied to video pixel diffusion by simply extending the patch size to temporal dimension and outperforms video latent diffusion in FVD evaluated on Kinetics-600 (resolution 256), under comparable total network parameters. Code is available at this https URL

---


### 173. [FoMNet: Adaptive Kernels Meet Contextual Matching for Cross-Modal Homography Estimation](https://arxiv.org/abs/2611.34096)

**<font color=#1a73e8>作者：</font>** Zhuoran Yang, Zhenyu Yi, Runmin Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-modal homography estimation requires reliable correspondences despite appearance differences between sensing modalities. Multi-scale refinement progressively reduces the search range, but its accuracy remains limited by the ability of matching features to distinguish nearby candidates. The vision foundation model (VFM) provides complementary representations, yet integrating these features through fixed interpolation leaves their spatial aggregation independent of image content and the correspondence objective. We propose the Foundation Model-Enhanced Matching Network (FoMNet), which combines learned spatial adaptation of VFM features with contextual correspondence estimation. Patch Feature Upsampling (PFU) progressively predicts location-specific kernels to aggregate neighboring features on upsampled grids, preparing VFM representations for fusion with CNN features at different matching scales. Contextual Correlation Refinement (CCR) then jointly processes source descriptors and local correlations with spatial context to refine candidate scores before each homography update. To reduce upsampling overhead, we develop FoMNet-D, which replaces PFU with bicubic interpolation and uses multi-scale feature-relation distillation to recover accuracy. Experiments on five cross-modal datasets show that FoMNet achieves the lowest mean average corner error (MACE) among the evaluated methods, reducing MACE by 10.6%-72.7% relative to MCNet. FoMNet-D retains competitive accuracy while reducing inference latency by 34.0% relative to FoMNet.

---


### 174. [When Position Favors the Wrong Part: Evaluating Left-Right Discrimination in Semantic Correspondence](https://arxiv.org/abs/2611.34100)

**<font color=#1a73e8>作者：</font>** Pingan Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Overall part-discrimination accuracy can conceal failures when image position favors the wrong bilateral part. We examine whether dense descriptors distinguish the correct part under this conflict and whether their discrimination scores help select matching coordinates. We evaluate position agreement and conflict within the same target images and annotated part pairs, using a bounding-box-side score to define the conditions. We compare the original descriptors with their even and odd components under horizontal reflection, examine feature upsampling with the backbone and adapters fixed, and test candidate-selection rules based on odd scores. On SPair-71k, odd discrimination accuracy falls from 86.66% under agreement to 19.63% under conflict for frozen DINOv2, compared with 95.27% to 86.16% for MARCO. With MARCO's input geometry fixed, odd accuracy in box-side conflict was 34.12% on the native grid and 88.84% after learned upsampling and pooling back to that grid. Odd-score rules improve on the original hard-peak matchers overall for DINOv2 and DINOv3 and on conflict queries for MARCO. With MARCO's soft decoder fixed, reranking the cosine peaks changes mean per-pair PCK by +0.47 pp. For supervised GeoAware-SC, using the odd score to select the localization window center yields only 15 net additional correct matches, with 330 corrections and 315 introduced errors. Evaluating discrimination under position conflict reveals failures hidden by aggregate accuracy. Reporting corrections and introduced errors separately also shows whether a discriminative score produces useful matching decisions.

---


### 175. [AlignPre: Skill-Aligned Post-Training for Latent-Free Generative Precipitation Nowcasting](https://arxiv.org/abs/2611.34101)

**<font color=#1a73e8>作者：</font>** Demin Yu, Kenghong Lin, Xutao Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Precipitation nowcasting requires accurate short-term predictions under rapidly evolving spatiotemporal dynamics. Generative diffusion models can produce detailed and competitive radar forecasts by modeling conditional distributions. However, most existing approaches rely on separately trained components, such as deterministic branches or latent compression modules. More fundamentally, distribution matching alone fails to explicitly optimize operational forecast skill. We propose AlignPre, a streamlined pixel-space nowcasting framework that bridges this gap via skill-aligned post-training (SAPT). AlignPre employs an end-to-end flow-matching forecaster with a hierarchical spatiotemporal architecture for distribution matching and direct radar-field synthesis, without latent compression. During post-training, SAPT exploits the analytic structure of forecast verification scores to construct a differentiable objective. By backpropagating gradients of this objective from radar fields to the generator, SAPT turns forecast verification into direct training feedback. Across three real-world benchmarks spanning different forecast horizons, AlignPre consistently surpasses state-of-the-art deterministic and generative baselines in forecast skill, demonstrating that aligning generative modeling with domain-specific verification provides an effective paradigm for meteorological forecasting.

---


### 176. [Do Machine Learning Ensembles Beat Published Quotas? Target Parameterization, Censored Baselines, and Conformal Intervals Under Admissions Reform](https://arxiv.org/abs/2611.34104)

**<font color=#1a73e8>作者：</font>** Dat Tat Mai, James Jin Kang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Public admission capacity caps published prior to matriculation are widely used by ministries and institutional analysts as default intake projections in centralized postsecondary clearinghouses. Using an audited 2022 to 2026 Vietnamese undergraduate panel (26,895 program-year records across 309 universities) linked to strictly lagged t-1 occupational vacancy signals, this paper evaluates machine learning, multilevel, and censored econometric estimators against published quotas across 5,385 continuing 2024 programs (five-fold university-grouped cross-validation) and 3,348 matched (2,179 grain-consistent) 2025 programs strictly out of time. Because 62.8% of 2024 programs enroll their exact published quota, unanchored log-growth ensembles degrade accuracy, while the worst 5% generate half of total quota error via unfilled "phantom capacity." Controlled target ablations, including a single-factor test under widened non-binding clipping, show that parameterizing the log fill ratio ln(D_it / S_it) instead of log growth reduces 2024 MAE by 21.5% (14.86 to 11.67), aligns ML with Tobit, Cragg, REML HLM, and capped L1 baselines, and lifts combined tuition and institutional-tier TreeSHAP attribution from 2.5% to 45.8%. Hurdle stacking attains the lowest full-census 2024 MAE (H-Hard 11.29; H-Soft 11.32 vs. 12.35, p = 0.022, clearing 10% not 5% FDR; fold-overlap p = 0.134), whereas continuous QA-Stack outperforms H-Soft on mixed-reporting campuses, Tobit (median) ties H-Soft across both 90% MCS sets, and interior-only Cragg-ML lowers RMSE to 28.1. Under Vietnam's 2025 unified-clearing reform, exact filling falls to 10.4%, H-Soft and capped L1 tie quotas (p = 0.979), and 90% cluster-weighted conformal coverage drops from 89.3% to 74.6%. Across 257 reporting campuses, reconciled 2026 national totals (627,114 to 629,256) lie squarely within 604,533 to 662,044.

---


### 177. [SysBio-SR: Benchmarking Symbolic Regression for Trajectory Fidelity and Mechanism Recovery in Systems Biology](https://arxiv.org/abs/2611.34106)

**<font color=#1a73e8>作者：</font>** Heng Rao, Dan Gao, Benjamin J Hoffman 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Symbolic regression seeks to discover interpretable governing equations for dynamical systems from data. In systems biology, however, accurately reproducing system trajectories does not necessarily imply recovery of the underlying reaction mechanisms. Existing benchmarks evaluate numerical accuracy, expression complexity, or equation-level similarity, but not agreement between recovered reactions and reference mechanisms in biological systems. We introduce SysBio-SR, a benchmark of 198 literature-based biological ODE systems with reaction annotations spanning mass action, Michaelis--Menten, Hill, and complex kinetics. Trajectory fidelity is evaluated across all systems under in-distribution reconstruction and out-of-distribution (OOD) extrapolation, while mechanism recovery is assessed on the subset of 161 systems. We evaluate trajectory fidelity across 11 symbolic-discovery methods and assess mechanism recovery for three reaction-based methods. Joint analysis across systems highlights how severely trajectory-based evaluation overestimates true mechanism recovery. Motivated by these findings, we develop KineSelect, a framework that searches candidate reaction topologies under biologically grounded kinetic laws to select optimal mechanisms that balance trajectory fidelity with structural parsimony. Compared with the strongest baseline, KineSelect improves aggregate OOD extrapolation \(R^2\) by 19.2\% and overall reaction F1 score by 14.3\%.

---


### 178. [Detectable by Design: Learning a Continuous 3D Saliency Field from 2D Detector Responses](https://arxiv.org/abs/2611.34108)

**<font color=#1a73e8>作者：</font>** Han Sun, Jun Li, Christy Jie Liang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The 3D points kept in a map decide whether a camera can be localized against it, and this choice matters more as the map becomes sparser. Existing 3D keypoint detectors usually define saliency by semantics, repeatability, reconstruction or descriptor matchability. None of these definitions asks whether a point will actually be detected in an image, and as a result most of the points they select are not detected again in images.
In this paper, we define 3D saliency as image detectability: the response of a 2D interest-point detector at a surface point, aggregated over all views in which the point is visible. We propose DetField, a continuous field over 3D space that takes a point cloud as input and predicts detectability at any location around it. The supervision is the response of a 2D detector, back-projected from images onto the point cloud. Multi-scale curvature invariants are passed to the decoder at every query point, bypassing the voxel pooling of the encoder.
In a localization benchmark that isolates the choice of 3D points, DetField outperforms Harris-3D and five learned 3D keypoint methods on objects and on real indoor scenes. On unseen rooms, it improves localization success by 7.4 points over Harris-3D, the strongest baseline. On objects, it also leads under a 2D detector not used in training. On sparse maps, it stays ahead of Harris-3D on both objects and real scenes.

---


### 179. [Not Every Input Needs Everything: Unifying Expert Gating, Model Cascades, and Agent Orchestration](https://arxiv.org/abs/2611.34112)

**<font color=#1a73e8>作者：</font>** Dat Tat Mai, Hung Tran Quy, Thai Viet Pham 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Executing monolithic neural weights, frontier foundation models, or entire multi-agent workflows uniformly on every input incurs substantial computational, latency, and monetary overhead. Conditional computation mitigates this cost by deciding dynamically which internal experts, model endpoints, or specialized agents to invoke per request. Yet token-level gating in sparse neural architectures, query-level model cascades, and task-level multi-agent coordination have largely progressed in disconnected research silos, obscuring recurring system failures and transferable fixes. In this systematic review, we synthesize 2,289 studies published between 2017 and September 2026 (selected from 13,884 unique records) across 20 methodological families under a unified two-step inspect-then-allocate framework. Discrete hard selection accounts for 70%, 83%, and 91% of token-, query-, and task-scale literature respectively, and computational overhead appears as a top operational bottleneck across every layer. Engineering safeguards remain sharply asymmetric: intra-layer gating prioritizes load balancing while rarely incorporating uncertainty estimation, whereas model selection and agent orchestration rely on confidence thresholds and budget rules while confronting miscalibration and cascading errors. At the same time, publication volume is accelerating fastest in agentic task delegation, where routing mechanisms are least often isolated experimentally and methodological bias risk is highest.

---


### 180. [MUSE: Multi-Task Uncertainty-Aware Self-Supervised Encoder for mmWave ISAC](https://arxiv.org/abs/2611.34122)

**<font color=#1a73e8>作者：</font>** Nabeel Nisar Bhat, Jalees Nehvi, Rafael Berkvens 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Integrated sensing and communication (ISAC) allows a wireless system to use the same waveform for communication and environment sensing. At mmWave frequency bands, ISAC enables diverse human sensing tasks, such as localization, gesture recognition, and pose estimation, with high precision. However, each task requires training a dedicated model, typically from scratch on a task-specific dataset, with no mechanism to flag unreliable predictions. This hurts the scalability, transferability, and reliability of mmWave ISAC models. In this work, we propose MUSE (Multi-task Uncertainty-aware Self-supervised Encoder), a unified framework for mmWave human sensing. MUSE leverages a self-supervised transformer model with per-dataset tokenization and is trained via masked autoencoding across five datasets. During fine-tuning, MUSE uses evidential classification heads that enable uncertainty quantification. MUSE replaces N separate encoders with a single shared transformer encoder, an N-times backbone parameter reduction, while achieving a 9.7 percentage points improvement in classification performance compared to the task-specific model, showing that learning jointly across tasks improves per-task generalization. Across four classification tasks, MUSE produces reliable uncertainty estimates that enable selective prediction, improving accuracy by abstaining on the least confident 20% of predictions. We further improve the reliability of the model's confidence estimates using temperature scaling and conformal prediction. Finally, MUSE's uncertainty signal remains reliable even under cross-user deployment, assigning higher uncertainty to wrong predictions than to correct ones 78% of the time, and recovering 9.2 percentage points of accuracy through selective prediction, with no additional retraining on the unseen user.

---


### 181. [FoundSurface: Feedforward Ray-Based 3D Scene Surface Reconstruction from Unposed Images](https://arxiv.org/abs/2611.34128)

**<font color=#1a73e8>作者：</font>** Shenxing Wei, Jinxi Li, Zihui Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate 3D surface reconstruction from unposed images remains a fundamental challenge in computer vision. Recent feed-forward pointmap methods eliminate the need for camera poses but inherently produce discrete, sparse representations. In this paper, we present a generalizable pipeline that directly recovers continuous, high-fidelity 3D surfaces from unposed images by seamlessly integrating pointmap- and ray-based representations. Our approach first extracts explicit geometric priors using a pre-trained pointmap model. A query-view-centric selection module then identifies geometrically relevant reference views via a robust surfel voting mechanism. Next, a cross-attention regressor bridges target query rays with reference features to estimate a continuous coarse surface. Lastly, a raylet-based module aggregates local 3D features to carve out high-frequency details and analytical normals. Trained as a single foundation model on 9 diverse datasets, our method demonstrates exceptional zero-shot generalization on 6 unseen datasets, clearly surpassing state-of-the-art baselines in geometric accuracy and detail preservation.

---


### 182. [Is Sara Omar the true author of Dødevaskeren (The Dead Washer)? Authorship attribution in Danish literature](https://arxiv.org/abs/2611.34131)

**<font color=#1a73e8>作者：</font>** Jacques Savoy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The bestseller Dødevaskeren (The Dead Washer) was published in 2017 under the name Sara Omar. A Danish colleague has suggested that the novel may have been written by another author, possibly Mads Peder Nordbo. To investigate this authorship question, four authorship attribution methods were applied, namely Delta, intertextual distance, Nearest Shrunken Centroids (NSC), and naïve Bayes. Using various parameter settings, these approaches consistently identify Nordbo's writing style in the doubtful novel, although the results do not provide conclusive evidence that he authored the novel in its entirety. In a second step, the novel was divided into non-overlapping segments of 5,000 tokens. Once again, Nordbo's style was identified in the majority of the segments. However, a small number of passages do not clearly support this conclusion and instead suggest the possible involvement of another, as yet unidentified, author, possibly Sara Omar herself.

---


### 183. [Somatic Alignment: Scaffolding Non-Visible Inner Body Sensations in and beyond Vocal Pedagogy](https://arxiv.org/abs/2611.34133)

**<font color=#1a73e8>作者：</font>** Ziyue Piao, Theodora Nestorova, Leon Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Inner bodily sensations inform expressive musical performance but can be difficult to interpret and communicate. Through two separate workshops with five singing learners and four senior voice teachers, we investigate breath control in vocal pedagogy. Participants reported difficulty interpreting bodily sensations (Opacity of Inner Sensations) and translating awareness into intended adjustments (Disconnected Regulation of Inner Sensations), alongside strategies involving touch, demonstration, and imagery. Building on these accounts, we propose the Somatic Alignment Model (SAM), connecting an Intrapersonal Self-Sensing Loop with an Intercorporeal Co-Sensing Loop. SAM examines how external guidance relates to learners' bodily calibration and how interpretive and regulatory authority is negotiated. We articulate three generative design dimensions, Modality, Agency, and Temporality, and illustrate their possible applications in interactive learning systems and first-person soma design inquiries. SAM offers a conceptual lens for supporting bodily awareness and regulation through interaction design.

---


### 184. [A Calibration-Referenced Protocol for Measuring Decision Stability under Reference Bank Compression](https://arxiv.org/abs/2611.34134)

**<font color=#1a73e8>作者：</font>** Yiwen Chen, Shengming Yu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reference banks used for industrial image inspection can be compressed to fit a deployment budget, but the resulting anomaly decisions depend on both the compressed scores and the operating threshold. We present a four-step protocol that compares compression methods at matched deployment sizes, establishes a reference distribution from 200 recalibrations, evaluates disagreement against two calibration benchmarks, and measures changes by distance from the full-bank threshold. With WideResNet-50, budget-matched product quantization (PQ) at the 10% budget has the lowest decision disagreement among five matched methods, including int8 scalar quantization, on VisA and MVTec AD at both operating levels. Int8 scalar quantization gives lower disagreement than PQ at the other four budgets. On MVTec AD at the lower operating level, PQ meets the calibration median in 34/39 cells and the upper quantile in 39/39 cells. Category-equally weighted image-level AUROC loss at this budget ranges from 0.0003 to 0.0037 across the evaluated configurations. On VisA at the 1% budget and a 1% operating level, disagreement reaches 28.12% (95% CI 23.25--33.58%) among near-threshold anomalies and 1.30% (0.79--2.14%) across the normal holdout. The 10% budget-matched PQ setting retains the lowest disagreement among four compared methods with ResNet-18, with clean reference banks, and when thresholds are estimated from normal-directory probes. The protocol connects deployment size to a calibration-referenced decision measure and identifies the evaluation populations most informative for inspection.

---


### 185. [SOC-Net: Second-Order-Cone-Constrained Neural Networks](https://arxiv.org/abs/2611.34136)

**<font color=#1a73e8>作者：</font>** Seungseok Oh, Youngjae Min, Navid Azizan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In many applications, neural networks must learn input-output maps that respect prior knowledge such as physical laws, safety requirements, and operating limits. These requirements constrain which outputs are admissible for a given input and often admit second-order cone (SOC) representations, including norm bounds and robust linear inequalities. Examples in control include friction cones, thrust bounds, and input-robust control barrier function (CBF) conditions. However, existing approaches to enforcing general input-dependent SOC constraints require a conic solver, an iterative scheme whose feasibility depends on convergence, or an interior feasible point for each input. We propose SOC-Net, a neural network architecture that enforces input-dependent SOC constraints by construction for every input, even outside the training distribution. SOC-Net projects an affine lifting of the backbone output onto the reachable slice of a fixed product of Lorentz cones and maps the correction back to the output space. For separable constraints, this projection splits into one projection per cone, and each is available in closed form or reduces to a single scalar equation, regardless of the cone dimension. We prove that SOC-Net retains the expressive power of the backbone network under regularity conditions and accommodates end-to-end training by standard backpropagation with an explicit Jacobian. Experiments on contact force allocation with friction constraints and 3-D obstacle avoidance with an input-robust CBF demonstrate that SOC-Net satisfies the constraints at every evaluated input, with lower evaluation latency than the tested solver-based and iterative baselines.

---


### 186. [How resampling method can help us: Improving the Delta model](https://arxiv.org/abs/2611.34137)

**<font color=#1a73e8>作者：</font>** Jacques Savoy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Delta has been successfully employed as an authorship attribution method in various contexts, although its effectiveness is not always perfect. Since it is based on the most frequent words, its results can be readily interpreted and explained in plain English. In this study, we propose improving its performance by applying a resampling method to the selected stylistic features. The results show that this approach increases the accuracy of the model while preserving the interpretability of its outcomes. However, the main drawback of the proposed technique is the additional computational time required to obtain more accurate results.

---


### 187. [An Image Detectability Field as a Viewpoint Utility for 2D-3D Localization in Sparse Maps](https://arxiv.org/abs/2611.34139)

**<font color=#1a73e8>作者：</font>** Han Sun, Jun Li, Christy Jie Liang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In 2D-3D localization, a camera estimates its pose by matching an image to a 3D map. A camera held in a hand or mounted on a robot can often choose its viewpoint before it takes the image. In this work, we ask whether an image detectability field is a useful viewpoint utility when the planner reads only the geometry of the map. The field can be queried at any 3D point near a surface. From the local geometry around the point, it predicts how likely a 2D image detector is to fire at the projection of the point. We use the trained field as it is, without fine-tuning it for view selection. A fixed SuperPoint and EPnP-RANSAC localizer then estimates the pose from the chosen view. We answer in two settings, each with a test registered before the runs. On synthetic ShapeNet objects with sparse point maps, summing the field over the visible landmarks beats counting them by +2.0 points of localization success rate (object-clustered 95% interval [+0.7, +3.2]). It also beats summing Harris-3D ranks by +2.2 [+0.8, +3.5]. On real indoor scenes from SceneFun3D, our adaptation of the learned view scorer LWL falls below counting on the test rooms. We therefore add the field to a learned per-landmark planner. On the test rooms with sparse maps whose landmarks the field also selects, the planner with the field beats the same planner without it by +1.8 points. It beats the planner with Harris-3D or curvature in its place by +1.0 and +0.8 points. All three room-clustered intervals lie above zero. In both settings, the field helps in sparse maps and is on par with Harris-3D in dense maps.

---


### 188. [Benefit of Structured Representations: When Equivariance Helps in Image Classification](https://arxiv.org/abs/2611.34140)

**<font color=#1a73e8>作者：</font>** Florian A. Hölzl, Daniel Rueckert, Georgios Kaissis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Equivariant neural networks promise improved representation learning through structural guarantees. However, mainstream vision encoders rarely incorporate equivariance for most geometric symmetries. Images are a particularly interesting modality with many such symmetries and extensive datasets from which to learn this structure. In this work, we investigate when vision encoders benefit from geometric inductive biases. We study the discrete rotation group of quarter-turns (C4) which acts losslessly without interpolation or boundary artifacts. Combined with image classification as a controlled invariant objective, this allows for a principled empirical investigation into the role of structural guarantees. We introduce ConvNeXt-C4 as a rotation equivariant ConvNeXt with dimension-equivalent yet orientation-structured representations. Training from scratch, our experiments show, that the C4 variant outperforms its base model across all tasks while operating with 6x fewer parameters and 1.6x fewer FLOPs. Its performance advantage increases log-linearly with decreasing training set size, with pre-training providing a similar improvement across both model variants. Analyzing the classifier head reveals that orientation information from the representations' structure is actively used, improving performance by 4.90% across all datasets. Our results highlight the sample-efficiency benefits of equivariance and the value of retained orientation information, motivating further investigation beyond image classification. Code is available at this https URL.

---


### 189. [Spe3DUp: Faithful Trajectory Distillation for Fast Image-to-3D Generation](https://arxiv.org/abs/2611.34141)

**<font color=#1a73e8>作者：</font>** Liangchao Xu, Jiaye Fu, Youtian Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent 3D generative models can produce high-quality meshes with complex structures and fine geometric details, with broad applications in games, film, and digital design. However, high-quality generation typically relies on long multi-step sampling processes that repeatedly evaluate large networks, leading to long inference times. At the same time, reference-driven tasks such as game-asset reconstruction and product digitization demand close correspondence to the input image: generated geometry must faithfully reconstruct the specific reference object. Acceleration must therefore reduce sampling computation while preserving the model's ability to reconstruct that object. To enable fast and faithful 3D generation, we introduce Spe3DUp, a coarse-to-fine framework based on Faithful Trajectory Distillation (FTD). FTD directly supervises few-step students with the teacher's input-conditioned denoising trajectories to preserve its generation behavior. We apply FTD separately to coarse geometry generation and geometric refinement, compressing both sampling processes while maintaining correspondence to the reference input. We further accelerate the complete mesh-generation pipeline with efficient geometry decoding and parallel remeshing. Experiments show that Spe3DUp maintains geometric quality and input correspondence close to those of the teacher, accelerates the coarse and refinement DiTs by 10.0x and 19.9x, respectively, and achieves a 7.7x end-to-end speedup over the original teacher pipeline.

---


### 190. [Non-Linear Motion from Two Frames: Cubic Hermite Trajectories for Video Frame Interpolation](https://arxiv.org/abs/2611.34143)

**<font color=#1a73e8>作者：</font>** Md Rifat Ur Rahman, Md Abtahi Majeed Chowdhury, Md Sakib Hossain Shovon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Two-frame video frame interpolation commonly resamples endpoint optical flow by the query time, which selects a constant-velocity straight-line path even though the same endpoint displacement is compatible with many intermediate trajectories. We present HermiteVFI, which replaces independent query-time motion prediction with one explicit continuous trajectory per pixel. The measured endpoint displacement fixes the two trajectory positions, while two latent endpoint derivatives learned from the frame pair control the interior path. A cubic Hermite curve is the minimum-degree polynomial that can independently satisfy these two position and two derivative boundary quantities. Its residual form contains linear motion exactly, structurally preserves the measured displacement endpoints for any network output, and has coefficients that are predicted once per frame pair and evaluated in closed form at arbitrary t. We further show that one interior query time gives a rank-deficient constraint on the two free trajectory coefficients, whereas any two distinct interior times are full rank at the representation level, motivating multi-time supervision. Appearance-derived directional cues help infer the latent derivatives that endpoint displacement alone cannot identify. On X4K1000FPS, SNU-FILM, and Vimeo90K-Septuplet, the largest gains occur for difficult non-uniform motion and high interpolation ratios. The amortization applies to trajectory-coefficient prediction; downstream reversal, refinement, and synthesis remain query dependent.

---


### 191. [HSTTA: Hierarchical Selective Test-Time Adaptation for Label-Free Cross-Subject EEG-to-Image Retrieval](https://arxiv.org/abs/2611.34153)

**<font color=#1a73e8>作者：</font>** Hongzhou Chen, Yuhao Wei, Lianghua He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-subject EEG-to-image retrieval suffers from substantial performance degradation on new subjects due to subject shift. Test-time adaptation (TTA) can mitigate this shift by adapting pretrained models with unlabeled target-subject EEG. However, most existing TTA methods struggle to match supervision granularity to each query's prediction confidence, leaving many queries without reliable pseudo-labels. To address this, we propose a novel framework named Hierarchical Selective Test-Time Adaptation (HSTTA). HSTTA builds a hierarchy over gallery image embeddings, uses hierarchical selective prediction to assign each EEG query a supervision granularity matching its current prediction confidence, and constructs adaptation objectives accordingly. We further propose Cross-Session Consistency Calibration (CSCC), an unsupervised method that calibrates the global confidence threshold to target a predefined accuracy level for hierarchical predictions. Moreover, we introduce Reciprocal Hierarchical Backoff (RHB), which moves queries lacking reverse-matching support to coarser nodes to mitigate error reinforcement. Experiments on two public benchmarks and ablation studies validate the effectiveness of HSTTA and its key components. On THINGS-EEG2, HSTTA outperforms the strongest EEG-specific TTA baseline by 17.9 (13.4) and 8.9 (3.7) percentage points in Top-1/Top-5 accuracy, respectively, under cosine (CSLS) ranking. Further analyses show that HSTTA yields more accurate pseudo-labels during adaptation, supporting more reliable model updates.

---


### 192. [When High Capacity Becomes Undeployable: Pore-Filling Constraints for Multi-Objective Optimization of Direct Air Capture Sorbents](https://arxiv.org/abs/2611.34154)

**<font color=#1a73e8>作者：</font>** Yujie Liu, Xuehua Shen, Zuotai Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Amine-impregnated sorbents with the highest nominal CO2 capacity are frequently the least deployable, as amine beyond the pore-volume limit blocks active sites. Yet multi-objective Bayesian optimization (MOBO) for direct air capture (DAC) treats formulation search as unconstrained. We encode the pore-filling boundary as an explicit outcome constraint, c(x) = tanh(1 - phi_hat) - tau, and use it as a diagnostic instrument on a hand-curated, DOI-traceable benchmark of 618 solid-amine formulations from 43 publications. Unconstrained MOBO attains higher nominal capacity (3.639 +/- 0.815 vs. 2.964 +/- 0.728 mmol/g, p = 1.0e-11), but across 100 seeds 63.2% of its Pareto-optimal candidates violate the pore-filling boundary versus 39.3% under the constraint: it is rewarded for proposing candidates outside the pore-confined design regime. The constraint steers the front to lower loadings (55.8 vs. 65.2 wt%) and larger pores. The boundary is corroborated once apparatus effects are harmonized hierarchically: 77.8% of kinetic variance is between-laboratory, and pore filling carries a significant kinetic penalty (p = 0.002). Standard hypervolume over-credits feasibility-agnostic methods by 13.9-16.1% (vs. 11.1% constrained), and three surrogate-based analyses---the constrained front, a regeneration-energy third objective, and harmonized kinetics---consistently point to a conservative deployable window at pore filling phi_hat ~ 0.4-0.5 (45-55 wt% loading). The benchmark and associated analysis outputs accompany this submission.

---


### 193. [OceanFix: Reference-Guided Diffusion for Sparse-View Underwater 3D Reconstruction](https://arxiv.org/abs/2611.34155)

**<font color=#1a73e8>作者：</font>** Gen Li, Maoxin Chen, Yao Xiao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in Gaussian splatting have enabled efficient underwater reconstruction, but sparse observations, light attenuation, and backscatter still leave scene regions underconstrained and cause novel-view artifacts. We present OceanFix, a reference-guided framework for sparse-view underwater 3D reconstruction that combines diffusion-based view repair with Gaussian scene refinement. Our repair model follows a two-stage training strategy that separates underwater appearance adaptation from geometric refinement. The first stage learns underwater appearance from reference observations and estimated medium features. The second uses camera poses and reference depth to align reference features, with relative-depth supervision guiding structural repair without requiring target-view depth at inference. We further propose medium-aware distillation that transfers repaired views into the 3D scene according to geometric repair demand and channel-specific optical observability. Through iterative rendering, repair, and distillation, OceanFix refines underconstrained regions while retaining supervision from the observed views. Experiments on underwater datasets demonstrate that OceanFix improves rendering quality in sparse-view 3D reconstruction, reducing visible artifacts and recovering finer scene details.

---


### 194. [Strategic and Robust Task Allocation for Combat Objectives in Adversarial Multi-Agent Environments](https://arxiv.org/abs/2611.34158)

**<font color=#1a73e8>作者：</font>** Jonas Peché, Dmitry Matveev, Vladimir Ciric 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Task allocation in contested-objective team games requires coordinated decisions under uncertainty, spatial constraints, and changing tactical conditions. In such settings, multiple agents must anticipate both teammate behavior and opponent actions. We study a hybrid predict-then-optimize approach for assigning controllable agents to objectives in real time. A masked multi-head model predicts tactical signals for each agent, including survival chance, local superiority, combat interaction, travel time, and objective contribution. These signals are combined with rule-based terms in a score matrix, and a minimum-cost flow solver computes coordinated global assignments constrained by capacity, occupancy, stability, and defensive strategies. Learning is limited to tactical scoring, while explicit rules and solver structure preserve controllability and interpretability. We evaluate the system using predictive metrics, offline assignment diagnostics, online A/B evaluation, and latency measurements. The system is an R\&D research prototype built on a commercial game and is not deployed in the shipped game. The results indicate that learned tactical estimates can support stable, feasible, and inspectable objective allocation under strict real-time constraints.

---


### 195. [Admoab-DETR: Resolution-Tiered Fusion for Infrared-Visible Object Detection with Missing Modalities](https://arxiv.org/abs/2611.34163)

**<font color=#1a73e8>作者：</font>** Wenchao Li, Haoran Jia, Shuyuan Wen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared and visible images offer complementary cues for all-weather object detection, yet real-world sensor dropouts can leave one stream unavailable and degrade paired-input detectors. Meanwhile, existing modality-adaptive methods apply heavy cross-modal attention uniformly across scales, incurring prohibitive token overhead on high-resolution maps. We propose Admoab-DETR, a unified real-time detector supporting infrared-only, visible-only, and paired inputs with a single set of weights. Specifically, \emph{Resolution-Tiered Fusion} (RTF) allocates fusion capacity by spatial token density and feature granularity: a lightweight Spatial Modality Gate governs fine local fusion at the highest-resolution scale with zero-cost single-view pass-through, while channel-compressed deformable Admoab necks capture cross-modal correspondence at coarser semantic scales. Furthermore, \emph{Mode-Matched Feature Distillation} (MMFD) aligns multi-scale encoder features with an availability-synchronized full-fusion teacher, avoiding ill-posed cross-modal hallucination while cutting parameters by 18.1\% and paired latency by 39.6\% at zero inference overhead. We also construct Admoab, a strictly registered 20,000-pair infrared--visible benchmark across diverse scenes. Experiments show Admoab-DETR achieves state-of-the-art accuracy--efficiency trade-offs across missing-modality and paired benchmarks. Our code will be available at this https URL.

---


### 196. [Cell-Type-Specific Expression Is Hard to Predict from Bulk, but It Is Still Useful](https://arxiv.org/abs/2611.34166)

**<font color=#1a73e8>作者：</font>** Gadi Naveh, Amit Miller, Gal Keinan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Single-cell-informed deconvolution provides cell-type-resolved features for clinical bulk RNA cohorts. Most existing methods predict the proportions $\pi_k$ of the $K$ constituent cell types (CTs). Fewer predict cell-type-specific expression (CTSE) $\mu_{kg}$ of gene $g$ in CT $k$, which can capture cell states that proportions miss, but recent benchmarks find it much harder. We explain this gap with closed-form accuracy bounds. For CTSE, we derive an $R^2$ ceiling for per-gene linear estimators. For proportions, the best linear estimator, which pools evidence across genes, has a closed-form $R^2$, and a computable lower bound on it predicts which CTs are learnable. We study targeted deconvolution of 106 biologically curated (CT, gene) pairs, found post hoc to have higher learnability scores. On overall survival in non-small cell lung cancer, estimation difficulty does not predict prognostic value across these targets. Yet a sparse survival model on deconvolved features, mostly CTSE, predicts survival as well as a sparse model on the bulk genes themselves, while attributing its signal to specific cell types. Some deconvolved CTSE features reveal prognostic signal not seen in the corresponding bulk gene.

---


### 197. [Loop4D: Embodied World Modeling with 4D VAEs and Looped Diffusion Transformers](https://arxiv.org/abs/2611.34199)

**<font color=#1a73e8>作者：</font>** Gen Li, Fan Luo, Mengjun Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Predicting the outcomes of robotic manipulation requires modeling both visual appearance and evolving 3D geometry. This poses two challenges: video compression can obscure fine-grained robot motion, while jointly predicting RGB and geometry demands sufficient generative capacity. We introduce Loop4D, a framework that addresses these challenges through motion-preserving 4D representations and recurrent generative refinement. Our 4D VAE encodes RGB and pointmap sequences into compact spatiotemporal latents while preserving motion details and geometric structure. Our RGB VAE combines geometry-guided supervision with predictive reconstruction to reduce compression-induced motion artifacts. Our geometry VAE uses lightweight adapters to adapt pretrained RGB representations while preserving their priors. Building on these representations, our Dual-Stream Looped Diffusion Transformer maintains separate appearance and geometry streams with shared Transformer weights and cross-modal connections. By reusing Transformer blocks across loops, we increase effective depth without replicating backbone parameters, enabling models with fewer parameters to improve joint RGB-geometry prediction through additional computation. Experiments demonstrate high-quality 4D generation and validate Loop4D in simulated robotic manipulation tasks.

---


### 198. [Compute-Aware Submodular Online Learning in Open Multi-Agent Systems](https://arxiv.org/abs/2611.34211)

**<font color=#1a73e8>作者：</font>** Jing Liu, Luca Ballotta, Fangfei Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper studies policy learning for cooperative task allocation in open multi-agent systems, where submodular utilities model diminishing marginal returns due to overlapping agent contributions. While standard methods evaluate every candidate action to update the policy, this may incur an excessive computational cost online. Hence, we impose a budget on these evaluations and analytically study the effect of query budget on online learning. Our algorithm samples a prescribed number of agent-action pairs and applies inverse-probability weighting to their marginal gains, yielding an unbiased gradient estimate of the expected stage utility for a Kullback-Leibler (KL) mirror-ascent update. We derive a $1/2$-approximate regret bound that elegantly splits into a tracking error between optimal and learned policies, quantified by their KL divergence, and a query-dependent feedback term. Experiments on cooperative information coverage show that our approach retains high performance with significantly less computation online.

---


### 199. [GeoCAM: Self-Supervised Sonar-Optical Representation Learning via Geographic Overlap Supervision](https://arxiv.org/abs/2611.34218)

**<font color=#1a73e8>作者：</font>** Fadi Abdeladhim Zidi, Andrea De Salve, Giuseppe Celeste 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-modal self-supervised learning for paired side-scan sonar and underwater optical imagery is a promising direction for benthic habitat understanding, but it remains underexplored because existing methods do not fully exploit the one-to-many correspondences and geographic metadata available in real opti-acoustic surveys. This limits the ability to learn representations that are both semantically meaningful and geometrically consistent from abundant unlabeled marine data. To address this problem, we present GeoCAM, a geography-guided framework that learns a shared embedding space for sonar tiles and their associated optical views without semantic annotations. GeoCAM achieves its goal by combining three components: (i) a Set Attention Aggregator that adaptively summarizes multiple optical observations into a single tile-level representation; (ii) a geometry-weighted InfoNCE objective that converts GPS-derived footprint overlap into soft positive supervision; and (iii) an optional cross-modal masked reconstruction branch that encourages physically grounded cross-modal alignment. Experiments on the BenthiCat SSS-CAM dataset show that GeoCAM can be effectively exploited to learn which sonar and camera samples describe the same seabed patch, improving cross-modal retrieval and alignment over strong contrastive baselines. Code is available at this https URL.

---


### 200. [Variation-aware Temporal Correspondence for Self-Supervised Video Representation Learning](https://arxiv.org/abs/2611.34220)

**<font color=#1a73e8>作者：</font>** Yang Liu, Qianqian Xu, Peisong Wen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised video representation learning has achieved remarkable progress by leveraging large-scale unlabeled video data. Recent methods commonly extend Masked Image Modeling (MIM) to Masked Video Modeling (MVM), where video representations are learned by capturing semantic information from temporal contexts during masked content recovery. Unlike static images, videos exhibit inherent temporal variation, as visual objects continuously change their positions, appearances, and motion states across frames. Therefore, MVM needs to preserve semantic consistency while capturing temporal changes of corresponding regions, which raises two central challenges: 1) how to establish reliable temporal correspondence across frames, and 2) how to formulate an appropriate representation learning objective for modeling both semantic consistency and temporal variation. To address these challenges, we propose Variation-aware Temporal Correspondence for video Representation learning (VT-CoRe) framework. For challenge 1), VT-CoRe introduces a sandwich sampling strategy to construct two-sided temporal references and a Patch Registration Module (PRM) to establish reliable patch-level correspondence. For challenge 2), VT-CoRe imposes latent-space semantic alignment on registered representations through a self-distillation architecture and further proposes temporal variation modeling to constrain representation trajectories over time. Experiments on 8 downstream tasks across 16 benchmarks demonstrate the effectiveness and applicability of VT-CoRe across pixel-level, frame-level, video-level, and vision-based robotic learning scenarios. Complementary representation analysis shows that VT-CoRe learns a more structured latent space for variation-aware temporal correspondence learning.

---


> [!TIP]
> 当前位于：**151-200**（第 4/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-314](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
