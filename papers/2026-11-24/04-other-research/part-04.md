# 📦 其他研究 | 2026年11月24日

> 本类共 **206** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-206](./part-05.md)

---

### 151. [Segment Everything, Materialize Nothing: Exact Streaming Inference for Many-Class 3D Segmentation](https://arxiv.org/abs/2611.27630)

**<font color=#1a73e8>作者：</font>** Fabian Isensee, Jakob Wasserthal, Lalith Kumar Shiyam Sundar 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Whole-body segmentation tools such as TotalSegmentator and MOOSE split more than 100 classes across five or six networks. The reason is memory. Standard 3D inference, as implemented in nnU-Net and MONAI, holds a logit for every class and voxel, on the working grid and again on the scanner's grid. For a median whole-body CT at 125 classes, that is 76 GB. We show that this memory wall lies in what inference materializes, not in the task, and remove it without approximation. Every step after the network is local along one axis, so its outputs can be streamed through a ring one patch thick. The classification head commutes with blending and resampling, so the ring carries the network's features instead of the class logits. Memory thus no longer grows with classes times volume, and the label map on the scanner's grid stays exact. This holds for any model with a pointwise affine head, without retraining. Many-class models, previously impractical, become deployable. One model trained on all classes matches or slightly exceeds the toolkits' five or six specialists in segmentation quality and runs 5.8-15x faster end to end, with 3.2-7.6x less RAM and under 8 GB of VRAM. We provide the method as a drop-in for nnU-Net, TotalSegmentator and MOOSE. The code is part of nnU-Net (this https URL), and unified models for both toolkits will be released.

---


### 152. [Learning Inside Types: Epistemic Typestates for Safe Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2611.27631)

**<font color=#1a73e8>作者：</font>** Lorenzo Bacchiani, Mario Bravetti, Giovanni Pau 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Type disciplines make programs safe by construction: components checked against each other's types compose into programs that cannot go wrong in the ways the types exclude. Types suit reinforcement learning: a type constrains what an agent may choose, not how it chooses, so the guarantee holds for every policy a learner produces. We introduce epistemic typestates, a type discipline for safe multi-agent reinforcement learning. An agent's type is a protocol whose states record its beliefs, the worlds it cannot rule out from its own observations and actions, and permits only actions that are safe in every world of the belief, whatever the others do within their public types. Agents learn inside their types, which are built and checked one agent at a time and run without communication. We prove type soundness and team safety, give a synthesis that is sound and complete, build types from guards when worlds are infinite, and show that shields are a special case. All proofs are mechanised in Rocq. On nine benchmarks, no typed learner causes a safety violation, and task performance does not differ significantly from that of two recent multi-agent shielding methods. Where a contract-based method fails at five and ten agents, types for ten agents are built in under a second. In the two continuous benchmarks, Lagrangian learners cause thousands of violations in every training run.

---


### 153. [MoHA: Model-Conditioned Harness Adaptation for Long-Video Agents](https://arxiv.org/abs/2611.27646)

**<font color=#1a73e8>作者：</font>** Jianghan Chao, Wenhui Tan, Hang Su 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-video understanding increasingly relies on agentic systems that actively acquire evidence rather than process fixed video representations. Their execution harnesses must coordinate language-level planning with video-level observation and evidence acquisition, yet are typically fixed across model stacks. We therefore introduce MoHA, a framework for model-conditioned harness adaptation that adapts a common initial execution harness to the specific planner and observer models it hosts. MoHA treats the harness itself as a model-conditioned optimization object: under the same task distribution and initialization, different planner-observer stacks can benefit from different executable harnesses. Starting from a common initial harness, MoHA analyzes failed calibration traces to diagnose model-harness mismatches and adapts both planner-side reasoning support, such as overview, memory, and verification, and observer-side capability assignments, including OCR and ASR specialists. After structural adaptation, MoHA separately calibrates observer execution configurations for the hosted model stack. Across three frozen planner stacks, MoHA improves Video-MME Full accuracy by 6.2-27.1 percentage points and Video-Holmes accuracy by 3.1-20.1 points over the fixed initial harness. Cross-model transfer further shows that the adapted harnesses generalize only partially to other models, highlighting the harness as a model-conditioned optimization layer for long-video understanding. Code is available at this https URL.

---


### 154. [Late-Time Dynamics of Flow Matching: Distance Geometry and Learning](https://arxiv.org/abs/2611.27653)

**<font color=#1a73e8>作者：</font>** Umberto Biccari, Junqing Huang, Kang Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models transform simple random inputs into samples that resemble observed data. For a finite training set, a central question is how its geometry shapes the terminal dynamics and the probabilities assigned to individual samples. We address this question for flow matching with linear interpolation between independent Gaussian and empirical samples. The squared distance to the training set generates explicit paths contracting exponentially toward the nearest sample. We prove that exact trajectories restarted at prescribed late-time states approximate these paths uniformly over all elapsed times and compact sets of starting states away from Voronoi interfaces, with an error exponentially small in the inverse squared restart noise scale. The initial mass near interfaces controls the quadratic Wasserstein error between the exact and reference laws. For Gaussian and fixed Gaussian-tube restart laws, this gives a square-root rate in the restart noise scale, uniform over time, which a two-site example shows to be sharp in general. At ties, the Clarke subdifferential characterizes the graphical limit of the rescaled velocity field. This geometry motivates two learning methods: fitting the distance potential with value and gradient supervision, and fitting velocities along explicit contraction paths. A transport estimate separates initialization mismatch, velocity error, incomplete contraction, and endpoint allocation. MNIST experiments illustrate the distinct roles of support proximity, nearest-site retention, and feature fidelity. These results connect flow matching and score-based diffusion through a common limiting geometry and show how asymptotic analysis can inform the design and evaluation of generative models.

---


### 155. [SMSD: A Semantic Misinformation Spreader Detection Approach](https://arxiv.org/abs/2611.27661)

**<font color=#1a73e8>作者：</font>** Zeeshan Bin Siddique, Michael Bewong, Md Geaur Rahman 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Misinformation spreaders on social media significantly amplify false narratives, making early detection critical to mitigate their spread. Existing approaches often overlook evolving user behavior, introduce semantic noise by ignoring user stance, and fail to handle newly emerging users effectively. To address these limitations, we propose a \underline{S}emantic \underline{M}isinformation \underline{S}preader \underline{D}etection approach (SMSD) that models misinformation propagation as a temporal, user-centric, and behavior-driven learning problem. SMSD adopts a multimodal architecture that incorporates three categories of features: user-level, network-level, and conversation propagation. A stance-aware labeling strategy is also introduced to differentiate supportive, opposing, questioning, and neutral users towards misinformation claims. Additionally, a monthly quantile analysis is introduced to simulate realistic, evolving user participation. Initial experimental results on the FibVid COVID-19 benchmark dataset demonstrate that SMSD improves recall by 45.0\%, F1 by 49.5\%, and MCC by 74.6\% under stance-aware labeling and by 17.7\%, 7.4\%, and 11.4\%, respectively, under threshold-based labeling. It consistently outperforms all baselines in both settings.

---


### 156. [GeoScaffold: From Latent to Realized Geometry in Collaborative Detection](https://arxiv.org/abs/2611.27667)

**<font color=#1a73e8>作者：</font>** Kang Yang, Yance Fang, Gaochen Cui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most collaborative 3D detectors fuse bird's-eye-view (BEV) features from connected vehicles and roadside infrastructure to aggregate complementary observations. Although modern communication, alignment, and fusion pipelines encode rich latent geometry in the fused BEV features, the standard readout pipeline inherited from single-agent detectors, i.e., anchor scoring, box decoding, and non-maximum suppression (NMS), does not fully exploit these geometric cues. We empirically identify and quantify this gap on UrbanIng-V2X. Collaboration improves localization at about two-thirds of positive anchors, yet when NMS resolves two overlapping collaborative boxes of one object, it keeps the better-localized box less than half of the time. A key cause is a supervision mismatch: classification scores are trained only for foreground-background discrimination, so nothing in training requires them to rank boxes by localization quality. To address this limitation, we introduce GeoScaffold, a lightweight training-only auxiliary objective. It predicts a foreground mask at each positive anchor, i.e., the cells of a grid over the anchor that lie inside the ground-truth box, to supply the dense spatial supervision that the seven-dimensional box code leaves implicit. Its loss, added to the detection loss, updates the encoder and fusion modules through the fused BEV and trains the detector toward a better-localized box at every positive anchor, including the top-scored one. The auxiliary head is removed at inference, preserving the original detector architecture, communication logic, and inference cost. GeoScaffold raises AP@0.5 and AP@0.7 by 0.98 and 0.55 points on average across all 11 fusion methods on the UrbanIng-V2X validation split, with gains extending to most methods on an unseen intersection and to all ten methods that produce detections on V2V4Real.

---


### 157. [CanopyFormer: Attention-Guided SegFormer for Explainable Forest Cover Segmentation](https://arxiv.org/abs/2611.27674)

**<font color=#1a73e8>作者：</font>** Dhinanjaya Fernando, Dinura Ginige, Kalana Lakshan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In transformer segmentation models, attention is usually visualized after training rather than supervised. Although attention supervision has been explored for natural images and driving scenes, aerial forest segmentation typically uses attention only as an architectural component and evaluates interpretability qualitatively. We present CanopyFormer, an attention-guided SegFormer-B0 that uses an Attention Consistency Loss to align attention with the ground-truth forest mask, encouraging attention to focus on canopy regions. Since SegFormer uses spatial-reduction attention, we adapt Gradient-weighted Attention Rollout by restricting it to the final encoder stage, where the attention matrix is square. We introduce Average Attention-Mask Overlap (AAMO) to measure attention alignment and incorporate a deletion test to evaluate faithfulness. On 5108 images, our method increases AAMO from 0.0334 to 0.7476, approximately 22 times the vanilla SegFormer-B0 result, with a modest decrease in Dice score from 0.8743 to 0.8577. The deletion test reveals that improved alignment does not necessarily translate into improved faithfulness: removing the most-attended 25% of patches reduces the forest score by 12.1%, compared with 33.0% when removing random patches. Attention supervision introduces no additional inference cost, although double backpropagation makes each training step 2.6 to 2.8 times slower. The attention alignment improvement also generalizes to a second dataset, LoveDA. Additionally, a Boundary Refinement Module provides no consistent Dice improvement and reduces AAMO, while mean squared error substantially outperforms Kullback-Leibler divergence as the attention loss.

---


### 158. [Learning in Symbiosis: Heterogeneous Federated Learning with ANNs and SNNs](https://arxiv.org/abs/2611.27686)

**<font color=#1a73e8>作者：</font>** Manh V. Nguyen, Liang Zhao, Bobin Deng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spiking Neural Networks (SNNs), widely regarded as the third generation of neural networks, represent a promising neuromorphic computing paradigm with the potential to reduce the energy footprint of Artificial Intelligence (AI). Their en-ergy efficiency makes SNNs particularly attractive for resource-constrained Edge AI devices, motivating growing research interest in Federated Learning (FL) with SNNs. Despite these advantages, integrating SNNs into existing FL systems remains challenging, as replacing all conventional Artificial Neural Network (ANN) devices with SNN-based alternatives is impractical. Instead, we envision a gradual transition toward neuromorphic Edge AI, where ANN and SNN devices coexist and collaboratively participate in FL. To facilitate this transition, we propose Hybrid Neuromorphic Federated Learning (HNFL), a framework that enables joint training of heterogeneous ANN and SNN devices within an FL environment. Through experiments on CIFAR-10 using both VGG9 and ResNet architectures, we demonstrate the mutual benefits of collaborative ANN-SNN training. Specifically, HNFL achieves an average improvement of 16.85% when incorporating SNN devices into ANN-based FL and 8.02% when incorporating ANN devices into SNN-based FL. Furthermore, HNFL produces sparser spiking activity in the trained SNN models, with reductions of 12.4% for SResNet and 22.4% for SVGG9. To the best of our knowledge, this is the first work to demonstrate that ANNs and SNNs can coexist and mutually benefit from collaborative training in FL, providing a practical path toward the gradual integration of neuromorphic computing into existing Edge AI systems.

---


### 159. [Comparative Performance of Machine Learning Architectures for Fault Detection and Diagnosis in Chemical Processes](https://arxiv.org/abs/2611.27696)

**<font color=#1a73e8>作者：</font>** Rayane Ammar Khodja, Alexandre Voisin, Victor Costa 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fault Detection and Diagnosis (FDD) is crucial for both maintenance and control in chemical industries, where early fault detection can prevent costly failures and optimize operations. This is particularly critical in pilot units like those at IFP Energies Nouvelles (IFPEN), which operate under short-term experimental conditions with frequently varying operational parameters. This study conducts an extensive benchmarking analysis using the Tennessee Eastman Process (TEP), a widely used simulated chemical process dataset, to evaluate multiple approaches for fault detection and diagnosis, featuring numerous continuous operations with different sensors and faults. Several methods were implemented and compared including Multi Scale PCA (MS-PCA), AutoEncoder, Ensemble Learning, and LSTM models for fault detection, alongside Random Forest, XGBoost, and BLSTM (Bidirectional LSTM) for fault diagnosis. Our results demonstrate that Ensemble Learning achieves detection rates ranging from 80% to 100% across various fault scenarios. For the fault diagnosis task, BLSTM achieved a diagnosis accuracy of 98.76%. The study reveals that ensemble-based approaches consistently outperform individual models in handling the complex, multivariate nature of chemical process data, due to its robustness in combining multiple perspectives, comprehensive data capture, and localized detection capabilities. Furthermore, the superior performance of the BLSTM is due to its ability to capture both past and future temporal dependencies in the sequential data, particularly important in chemical processes where fault patterns may manifest with complex temporal relationships. This research contributes to the field of Fault Detection and Diagnosis by providing empirical evidence for the effectiveness of ensemble methods and Bidirectional LSTMs in order to address industrial FDD applications on chemical processes.

---


### 160. [Spatiotemporal Graph Neural Networks for Fault Detection and Structural Learning in Chemical Processes: Use Case on the Tennessee Eastman Process](https://arxiv.org/abs/2611.27698)

**<font color=#1a73e8>作者：</font>** Rayane Ammar Khodja, Alexandre Voisin, Victor Costa 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Classical Fault Detection and Diagnosis (FDD) methods, including many data-driven approaches, assume a static normal operating space and interpret deviations from a fixed reference as fault indicators. When Operating Conditions (OCs) vary over time, this assumption breaks down: legitimate transitions trigger false alarms while moderate faults go undetected. We propose a spatiotemporal Graph Neural Network (GNN) framework that decomposes the normal operating space into OC-specific subspaces linked by transition functions, with a dual learning objective combining reconstruction loss and a Deep SVDD one-class term. It learns adjacency matrices through Graph Attention Networks (GATs) and integrates spatial modelling with temporal encoding to represent process dynamics under evolving OCs. This paper evaluates the framework's foundational components (fault detection, GATv2 spatial graph learning and temporal encoding) on the Tennessee Eastman Process (TEP) benchmark, training only on fault-free data. The architecture achieves competitive detection from reconstruction error alone, with similarity-based feature selection improving both accuracy and graph structure diversity. We then evaluate the physical interpretability of the learned attention matrices against 22 ground-truth sensor pairs derived from the TEP control structure and process topology. GATv2 attention fails to recover all known physical pairs across multiple hyperparameter configurations, suggesting a structural limitation of reconstruction-driven attention rather than a tuning issue. This challenges a common assumption in GNN-based FDD: that learned attention weights provide a basis for fault diagnosis and root-cause analysis. The architecture detects faults effectively, but the learned graph does not encode the physical topology needed for interpretable diagnosis, motivating physics-informed graph construction.

---


### 161. [Geometrically Constrained Learning II: Agnostic Proper Learning of Lipschitz Functions](https://arxiv.org/abs/2611.27700)

**<font color=#1a73e8>作者：</font>** Jane Lange, Cassandra Marcussen, Arsen Vasilyan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We give a proper learner for Lipschitz functions over the Gaussian distribution on $\mathbb{R}^d$. Given random Gaussian examples labeled by a $\lambda$-Lipschitz function, $\lambda \ge 1$, the learner returns a function $h:\mathbb{R}^d\to\mathbb{R}$ that is globally $\lambda$-Lipschitz and has loss (absolute or squared) at most $\varepsilon$. The sample complexity, running time, and representation size are \[
(d+1)^{\mathsf{poly}(\lambda/\varepsilon)}. \] The learning algorithm can be made \emph{agnostic}, given a known bound on the variance of the label marginal distribution. Some known control of label scale is information-theoretically necessary. For arbitrary labels with variance at most $V^2 \ge 1$, the complexity is \[
(d+1)^{\mathsf{poly}(V\lambda/\varepsilon)}, \] and the error is $\mathsf{opt} + \varepsilon$, where $\mathsf{opt}$ is the minimal error among Lipschitz approximators.
Our approach combines $L_1$ polynomial regression under a convex gradient constraint with local correction of the Lipschitz property. The learner finds a polynomial that, after smoothing and clipping its range, is very close to a canonical Lipschitz correction of itself, the lower Lipschitz envelope. Our local corrector modifies the lower envelope by replacing distances to sublevel sets with a Gaussian sampling proxy, allowing the construction to be locally and stably estimated from samples.

---


### 162. [When Are Images Needed in Multimodal Machine Translation? Text-Only Routing for On-Demand Visual Context](https://arxiv.org/abs/2611.27712)

**<font color=#1a73e8>作者：</font>** Xinyu Wang, Yingfeng Luo, Yuxin Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Image-guided multimodal machine translation (MMT) leverages visual context to resolve translation-relevant uncertainty. However, prevailing systems either process images unconditionally or apply gating only after visual encoding, leaving redundant visual computation unavoidable. To mitigate this computational overhead, routing decisions must rely on a pre-visual source signal. Crucially, surface-level ambiguity does not equate to visual dependence, as intra-sentence textual context often suffices for disambiguation. We therefore formulate visual invocation as source-text sufficiency prediction: determining exclusively from the source text whether translation-relevant uncertainty remains unresolved. To support this formulation, we construct a visual-dependency dataset with three fine-grained labels (no_ambiguity, text_resolved, and vision_needed) and verify discriminative visual evidence for vision_needed instances. We further propose PreVIR, a lightweight, backend-agnostic text-only router that selects between text-only and multimodal branches before computing visual features. Experiments on English-to-Chinese MMT demonstrate that PreVIR achieves a favorable COMET-budget trade-off relative to strong routing baselines. At its default operating point, it substantially reduces visual calls while maintaining translation quality comparable to always-on multimodal inference. Label-wise and case analyses show that this trade-off stems from distinguishing genuine visual dependency from contextually resolved ambiguity.

---


### 163. [Recoverable Symbols, Unstable Execution: Auditing Internal Pathways and Decision Identity in Visual State Tracking](https://arxiv.org/abs/2611.27715)

**<font color=#1a73e8>作者：</font>** Ruiqi Liu, Jinming Li, Mo Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Visual features can retain every symbol a task needs while a model built on them still changes its answer when irrelevant parts of the image change. We study this gap in visual state tracking, where a recurrent executor reads a sequence of symbol tiles through a frozen ViT encoder and decides whether a displayed candidate equals the final state. Our diagnostic pairs each input with a donor view that preserves every queried tile, checks with a symbol-supervised decoder that the full symbol chain is recoverable from both feature sequences, and swaps individual internal channels of the same fitted executor in both directions. On 3,526 pairs in which every symbol is recovered in both views, changing the surrounding context lowers the balanced accuracy of a rotary recurrent head by 17.13 points. The loss runs mainly through the input-dependent rotation phase: restoring the original phase repairs 351 of 391 new errors and brings accuracy back to 88.54%, yet 142 individual predictions still differ from the original ones. A locked test on 192 unseen program families reproduces the pathway (28 of 29 new errors repaired; 382 of 384 predictions unchanged), and the effect partly carries over to single-image canvases. Consistency objectives derived from this analysis reduce the internal discrepancy they target but do not outperform ordinary data augmentation.

---


### 164. [Solving the pre-image problem in kernel PCA: The reproducing property is all you need](https://arxiv.org/abs/2611.27718)

**<font color=#1a73e8>作者：</font>** Joel-Pascal Ntwali N'konzi, Stefan Klus  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Kernel PCA extends PCA to nonlinear dimensionality reduction by implicitly mapping data into a reproducing kernel Hilbert space (RKHS) via the kernel trick, with applications ranging from image denoising to out-of-distribution detection. While its projection map is well understood, appropriately defining the associated reconstruction map is a longstanding challenge since projecting back from the RKHS to the input space is non-trivial. This is known as the pre-image problem. Existing approaches have tackled this problem by either relying on nonlinear optimization, which is prone to numerical instabilities and sensitive to initialization, or by solving a separate supervised learning problem, incurring additional computational overhead. Furthermore, although the projection map of kernel PCA reduces to that of standard PCA when a linear kernel is used, most of these approaches are not guaranteed to recover PCA's reconstruction map in this case, a consistency property that one would naturally expect to hold. In this paper, we leverage the reproducing property of the RKHS to derive a reconstruction map for kernel PCA that is provably consistent. Our derivations rely on the mild assumption that the RKHS either contains linear functions or the kernel is universal, which holds for standard kernels. We further extend the method to the random Fourier features (RFFs) approximation of kernel PCA by introducing a corresponding notion of RFF reproducing property. Numerical experiments on synthetic and real-world datasets demonstrate that the proposed method performs comparably with state-of-the-art methods across kernel choices, while remaining more computationally efficient and maintaining consistent performance in settings where these baseline methods drastically fail.

---


### 165. [VeilGS: Solving Darkness as a Veil of 2D Basis Maps over Retinex 3DGS](https://arxiv.org/abs/2611.27719)

**<font color=#1a73e8>作者：</font>** Mohab Kishawy, Chengzhou Tang, Shahram Shirani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In a dark capture, the darkness is not uniform. How much light reaches a surface depends on where it lies relative to the few light sources, and the camera compresses what remains with a tone curve. Most low-light 3D reconstruction methods either apply one curve to every pixel of a view, so a dark object beside a lamp and a bright one in an unlit corner receive the same correction, or store the darkness in the 3D representation, where it can absorb scene detail. We present VeilGS, a 3D Gaussian Splatting method for low-light novel view synthesis that treats the degradation as a veil drawn over a clear scene. Each Gaussian carries an albedo and a shading latent instead of spherical harmonics, separating surface colour from illumination. Each view is darkened by a spatially varying gain followed by a global tone curve, and rendering without this veil gives the restored scene. A small network predicts a coarse basis for the gain from the observation, and its coefficients are solved for each view rather than learned. Training through this solve discourages the Gaussians from absorbing what the veil can explain. VeilGS needs no paired normal-light supervision and stores no per-view parameters. On Gaussian-DK, its restored renders score best on no-reference NIQE and CLIP-IQA and are rated highest in a blind user study with 55 participants. On LOM, it achieves results competitive with the state of the art.

---


### 166. [PAWS: A Parametric Model of Canine Pose and Shape](https://arxiv.org/abs/2611.27720)

**<font color=#1a73e8>作者：</font>** Theo Wieland, Zala Žgank, Silvia Zuffi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce PAWS, a parametric model of canine shape and pose, learned from 3D scans of real dogs. Capturing the full diversity of dogs is challenging, as different breeds vary in size, proportion, and body shape. To capture this range, we scanned 31 dogs across multiple breeds and sizes performing a range of natural movements. From this dataset, we build a parametric model that combines an anatomically faithful skeleton with a linear shape space learned from the 3D scans. Unlike previous models, our model is learned from real dogs in varying poses, allowing for realistic modelling of canine pose and shape.
We demonstrate that building on PAWS provides a robust framework for downstream tasks, such as surface reconstruction and image regression. In particular, we show that a limited number of anatomically valid degrees of freedom is sufficient to accurately estimate dog pose and shape.

---


### 167. [A Switching Mechanism for Selecting Environment-Adaptive Personalized Gains in Hearing Aids](https://arxiv.org/abs/2611.27726)

**<font color=#1a73e8>作者：</font>** Nafisa Zarrin Tasnim, Nasser Kehtarnavaz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Personalized amplification gains for hearing aids have been shown to be preferred over prescriptive gains. Since the preferred settings can vary depending on the background audio environment, this paper presents a switching mechanism or system that automatically selects personalized gains for a current background audio environment. To prevent foreground speech from interfering with background environment analysis, a one-class voice activity detector is designed to identify speech activity from speech mixed with noise. A consistency check is conducted to enable distinguishing foreground speech from background speech, preserving babble as a background environment of interest because hearing aid users often struggle to understand speech in background babble. Sound segments without foreground speech are then analyzed by an online discovery method combining Bayesian change-point detection with a memory of previously encountered environments. This discovery method detects changes, recognizes returning environments, and discovers new ones without a predefined number of environments. Experimental results show that three-seed mean macro-averaged F1 scores of 85.53%-91.98% across eight speech/background-corpus pairs covering 36 background noise types were achieved. Furthermore, the discovery method achieved adjusted Rand indices of 0.91 and 0.96 on two families of test streams. In the same-recording-return condition of audio streams combining speech with four background audio environments often encountered by hearing aid users, the switching mechanism selected the correct personalized gain profile after 105 environment changes, recalled the stored gain profile at every return, and made no switches to an incorrect gain profile.

---


### 168. [Quantitative Measurement of Pavement Distress based on Vehicle Camera and Perspective Correction](https://arxiv.org/abs/2611.27728)

**<font color=#1a73e8>作者：</font>** Sike Wang, Yizhou Lin, Shuo Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Using image data is becoming an important method for highway agencies to automatically evaluate pavement conditions. However, most studies focus on improving detection accuracy rather than obtaining quantitative measurements, such as the length or area of pavement distress. Although field camera calibration can provide such measurements, it is impractical for large volumes of onboard images collected from different vehicles. This study develops a method to quantitatively measure pavement distress directly from in-vehicle camera images without on-site camera calibration. A quadrilateral region of interest is first identified based on lane detection and used to construct a perspective transformation matrix for image correction. Size correction is then performed using the proportions of road markings in the image and a specified scale, which also enables estimation of the actual width of the selected region. The corrected images are subsequently processed using object detection algorithms to obtain quantitative distress measurements. The proposed method can efficiently perform perspective correction for images collected by the same vehicle camera with minimal manual effort. The measured pavement patch lengths show a trend consistent with pavement friction data. By calibrating vehicle cameras using only image information, this study enables quantitative pavement distress detection without additional field experiments. The approach provides a practical solution for processing large volumes of vehicle-camera data, particularly as connected vehicles generate increasing amounts of uncalibrated roadway imagery.

---


### 169. [Do Alice and Bob Dream of the Oracle? Wishful Cryptanalysis](https://arxiv.org/abs/2611.27729)

**<font color=#1a73e8>作者：</font>** Guoxiao Liu, Keting Jia, Hongbo Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> For two millennia, offense and defense have forged cryptographic security boundaries. Tools automated calculation and search, while humans drove discovery. Foundation models now mark a shift from automated computation to intelligent scientific discovery. Because cryptanalysis rests on exact mathematical definitions and immediately executable truth, it offers a proving ground for autonomous intelligence to move past security reliant on scarce human attention and explore structures beyond human working memory. Unguided models stall between two opposite traps: authority hallucination, where they surrender whenever prior literature declares a route blocked, and reasoning hallucination, where they produce subtle, unverifiable flaws. Closed platforms and generic agent loops further impede sustained open inquiry. We introduce wishful cryptanalysis, a harness-agnostic methodology that pairs constructive optimism against entrenched assumptions with blinded, zero-import verification against error. Agents first compress reduced-scale theory within provisioned compute so live witnesses certify their mathematics automatically. They then co-adapt primitive, algorithm, and hardware, and climb parameter ladders toward high-round theory. Applied across frontier open-weight and proprietary models with minimal human intervention beyond targets and compute, this paradigm yielded novel attack techniques and thirteen verifiable practical results across Keccak (SHA-3) and AES. These include breaking a fifteen-year-open public challenge and closing longstanding practical gaps, released alongside an early-preview open-source workbench (agent-framework). Extending Kerckhoffs's principle into the AI era, we envision an Open Oracle, an open and auditable public infrastructure that frees cryptographers to legislate security goals, challenge assumptions, distill theory, and co-design resilient standards.

---


### 170. [AutoOntologyBench: A Task-Grounded Benchmark for Agentic Knowledge Engineering](https://arxiv.org/abs/2611.27734)

**<font color=#1a73e8>作者：</font>** Minye Shao, Chenghao Xiao, Xingyue Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Foundation-model agents are increasingly extending beyond software engineering (SWE) into autonomous scientific research, where acquiring and integrating domain knowledge remains a critical challenge. Recent industrial advances have increasingly adopted knowledge graphs and ontology-based semantic layers to organize heterogeneous knowledge into reusable representations. We ask: Can autonomous agents construct ontologies that help them solve real tasks, and do they offer measurable benefits over alternative knowledge representations? Existing benchmarks evaluate ontology correctness or agent task success in isolation, leaving the value of autonomously acquired knowledge unresolved. We therefore introduce AutoOntologyBench, a task-grounded benchmark comprising 19,947 audited tasks grounded in 18 real-world knowledge sources across 7 domains, with source-native verification. Spanning Application, Repair, Organization, and Construction, AutoOntologyBench compares nine frontier-model agents under matched knowledge representations. Layered on retrieval, agent-built ontologies add 6.1 points of task success, yet trail an expert-derived reference by 13.0, identifying autonomous knowledge acquisition as the bottleneck to scalable scientific research. Code and resources are available at this https URL.

---


### 171. [Post-Quantum Migration in Brownfield 5G Core Networks: Verified Hybrid Key Establishment, Performance, and Rollback](https://arxiv.org/abs/2611.27735)

**<font color=#1a73e8>作者：</font>** Shubham Verma  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Migrating brownfield 5G Core networks to post-quantum cryptography (PQC) is difficult because deployed network functions, base images, and TLS libraries evolve under different upgrade constraints. This paper evaluates a deployment-controlled migration strategy that enables hybrid post-quantum/traditional key establishment through externally deployed Boundary Cryptographic Execution Entities (BCEEs), without modifying participating network function source code. The approach is evaluated using the Open5GS AMF-NRF Service-Based Interface as a representative 5G Core scenario. Classical and hybrid configurations are compared under an unchanged mediation topology. Packet-level analysis confirms successful negotiation of X25519MLKEM768, and functional validation demonstrates that representative SBI procedures remain operational through the mediated path. In 120 NF-registration transactions, the median AMF-facing registration latency increased from 22.968 ms under the classical state to 26.351 ms under the hybrid state, reflecting a 3.383 ms (14.73 percent) increase, with a whole-block 95 percent confidence interval of [1.193, 7.872] ms. At the mediated TLS boundary, the hybrid configuration shows a 4.599 ms higher median segment-local TLS-establishment time than the classical configuration. These two reported differences reflect system-level runtime effects and do not isolate key-encapsulation cost. Packet evidence verifies rollback from hybrid-mediated operation to classical mediated operation and, separately, restoration of the native direct path. NF-facing compatibility legs remained plaintext and outside the hybrid post-quantum scope. The results demonstrate a packet-verifiable and manually reversible brownfield mechanism for introducing hybrid post-quantum key establishment on a controlled 5G SBI segment.

---


### 172. [Shared Understanding in Human-AI Teams: Coordination Continuity in Evolving Work](https://arxiv.org/abs/2611.27746)

**<font color=#1a73e8>作者：</font>** Siân Lindley, Britta Burlin, Christian Poelitz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> People are increasingly working with AI agents as part of extended, asynchronous workflows. In these settings, shared access to information does not guarantee a shared basis for action: goals, plans, and roles may persist while their current significance changes. We introduce coordination continuity, the extent to which collaborators sustain a workable basis for interdependent action as work progresses. Drawing on research on collaborative work, along with two qualitative team studies and a reflexive case from our own repository-based environment, we present a framework of three elements: durable representations of collaborative work; relative coordination properties that support interpretation of representations in the moment; and interaction mechanisms through which the status of representations can be understood and altered. We use a build-act-drift-rebuild heuristic and the notion of consequential moments to characterise when rebuilding may be needed. We draw eight design implications for collaborative AI infrastructure.

---


### 173. [SUPERVISE: A Unified Framework for Standardized and Reproducible Superpixel Evaluation](https://arxiv.org/abs/2611.27753)

**<font color=#1a73e8>作者：</font>** Julien Walther, Rémi Giraud, Michaël Clément  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image segmentation into superpixels is a widely used technique in computer vision, with a large body of work developed over the years. Yet, its evaluation remains poorly standardized, as methods are compared under heterogeneous protocols, across inconsistent scale ranges, and with redundant or misaligned metric subsets. In this work, we introduce SUPERVISE (SUperpixel PERformance VISualization and Evaluation), a unified and reproducible benchmark that addresses these longstanding inconsistencies. Built on a scale-normalized protocol based on interpolation over the actual number of generated superpixels, SUPERVISE enables fair and consistent cross-method comparisons. We leverage this standardized framework to conduct the first large-scale statistical analysis of 20 evaluation metrics across 7 datasets and 31 methods, revealing strong inter-metric correlations and significant redundancy that challenge common evaluation practices. These findings provide empirical support for reporting a compact set of representative metrics. SUPERVISE is released as a lightweight, modular framework built on precomputed shared label maps, making large-scale reproducible evaluation accessible to the community. All code, label maps, and evaluation results are publicly available at: this https URL

---


### 174. [Ref-YOLO-World: Decoupling Text-Side Computation for Efficient Referring Expression Comprehension on Edge Devices](https://arxiv.org/abs/2611.27756)

**<font color=#1a73e8>作者：</font>** Yuki Aoki, Hiroo Bekku, Tadashi Okoshi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many high-accuracy referring expression comprehension (REC) methods produce image-dependent multimodal representations. These representations must be recomputed for every video frame, even when the referring expression remains unchanged. Fast open-vocabulary detectors such as YOLO-World instead pre-encode text once and reuse it throughout the stream. However, encoding each referring expression as a single embedding prevents explicit token-level correspondence. We propose Ref-YOLO-World, which separates text-side computation that depends only on the referring expression from image processing and reuses its outputs across frames. Two lightweight modules inject cached per-token text features into YOLO-World's detection path. Ref-YOLO-World achieves 81.29% Acc@0.5 on RefCOCOg val, the highest among REC models with a decoupled text branch, and consistently outperforms a fine-tuned YOLO-World. Precomputation reduces per-image inference time by 18.5%, yielding 47.0 FPS. A Core ML version runs at 15.73 FPS on an iPhone 15 Pro, demonstrating efficient on-device REC. Code is available at this https URL.

---


### 175. [From Novel Combinations to Informative Absence: Structural permission, communicative opportunity, and form choice in language learning](https://arxiv.org/abs/2611.27762)

**<font color=#1a73e8>作者：</font>** Yanzhe Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language learners must infer which novel expressions are grammatically licensed and when continued absence is evidence against them. Our generative theory unites these capacities via counterfactual expression opportunities, decomposing utterance generation into structural permission, communicative opportunity, and form choice. First, shared predictive continuations recover structural permission for unseen word-construction pairings across 30 artificial grammars (mean AUC 0.945 after 120 sentences). Second, under hierarchical uncertainty, we derive a joint evidence law linking omissions to context diversity and within-context repetition, and an exact finite-sample context-refinement inequality. Thus, observing related expressions calibrates expected use to sharpen negative evidence, and higher expected use can drive steeper posterior declines for stronger-permission candidates (reversing initial order after six omissions in a fixed-rate example). Third, we prove that while raw counts confound semantic availability and form selection, scene-level opportunity observations identify both. Empirically, reanalyzing adult and child artificial-language experiments shows meaning-conditioned restriction; judgments of restricted combinations improve held-out production predictions across 399 participants (+0.036 nats/production). Naturalistic child-directed and child speech (11 families, six corpora) shows pervasive source-level usage clustering beyond lexical, number, and dependency-role controls, grounding hierarchical rate uncertainty. Finally, modeling causative judgments across five languages shows that structural compatibility and calibrated usage probabilities draw on distinct distributional, semantic, and discriminative cues. Together, these findings show how the organization and calibration of communicative opportunities govern the evidential value of linguistic absence.

---


### 176. [Search-RSI: Expanding Search Worlds Along Multimodal Agents' Capability Frontier](https://arxiv.org/abs/2611.27780)

**<font color=#1a73e8>作者：</font>** Chengchao Lv, Yin Wang, Chunzheng Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal search agents answer knowledge intensive visual questions by grounding them in retrieved evidence, and recent recipes train them on multi hop tasks that are synthesized from knowledge graphs and grown online to keep pace with the agent. These recipes, however, treat the searchable world as fixed: a new question can be well formed and verifiable while its evidence is absent from the retrieval backend, so the agent issues the right query, retrieves nothing, and is penalized as if its policy were at fault. Such unreachable negatives accumulate with every round of growth. We propose Search-RSI, a recursive self improvement framework that expands the search world along the agent's capability frontier. In each round, the current policy diagnoses its partially mastered regions of a task space spanned by hop depth, relation rarity, and distractor density; new tasks there are grown together with their evidence; and the same policy decides how they are used: candidates on which its probes disagree feed reinforcement learning, while those beyond its reach become hint guided demonstrations of its own. Keeping the policy inside this loop matters: an improver frozen at the start of training loses 3.2 points. On nine multimodal search benchmarks, Search-RSI keeps improving where static task growth saturates, raising the average accuracy of the recipe it builds on by 9.8 and 9.5 points at 9B and 27B, of which 7.0 points are out of reach for a world that is merely made consistent. The loop uses no external model and only privileged task structure that is removed before training, at 1.27x the compute of static growth.

---


### 177. [A Benchmark Protocol and Fairness Analysis Towards Open-Set EEG Seizure Type Classification](https://arxiv.org/abs/2611.27783)

**<font color=#1a73e8>作者：</font>** Targol Bakhtiarvand, Terrance E. Boult, Jugal Kalita 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated EEG seizure type classification systems are typically trained and evaluated under the closed-set assumption, where all seizure types encountered at deployment are seen during training. In clinical practice, this assumption fails: patients present with rare or atypical seizure types that fall outside the training label space, and a system that forces a wrong label is worse than one that abstains. We introduce the first open-set recognition protocol for EEG seizure type classification on the Temple University Hospital Seizure Corpus (TUSZ v2.0.3), defining known and unknown classes using the clinical taxonomy itself: seizure types with sufficient subject representation (at least 12 subjects) form the known set, and rare types form the unknown set. We evaluate seven post-hoc open-set scorers (MSP, MaxLogit, energy, Mahalanobis, kNN, GHOST, and COSTARR) applied to a partially fine-tuned EEG Foundation Model (EFM), using a subject-disjoint leave-one-class-out (LOCO) protocol over three seeds that tests whether methods can detect seizure types excluded from fine-tuning. On true unknown classes, the best scorer (Mahalanobis) reaches a mean AUROC of 0.66, and differences among the top scorers are within seed-to-seed variation. Held-out known seizure types from unseen subjects are detected only slightly above chance (AUROC 0.54-0.58 for all scorers). Per-subject rejection rates are highly uneven for all scorers, and GHOST does not significantly improve per-subject fairness over energy scoring (two-sided Wilcoxon signed-rank, p >= 0.25). We release the protocol, subject splits, and code as an initial baseline; our results indicate that open-set seizure type recognition remains a hard, open problem.

---


### 178. [When Does Looking Closer Pay Off? Simple Foveated ViTs for Fine-Grained Recognition](https://arxiv.org/abs/2611.27788)

**<font color=#1a73e8>作者：</font>** Boris Kriuk, Mohamed Sobhy  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained recognition benefits from high resolution, but not every image region needs it. We study a foveated Vision Transformer (FoVT) that uses last-block class attention from a 224-pixel glance to select regions for refinement. Fine patches from the 448-pixel image replace the selected coarse cells, and the same backbone classifies the mixed-resolution input. We evaluate FoVT on five benchmarks with two seeds and 26 configurations per dataset. Attention beats random selection on all five benchmarks, by up to 2.45 percentage points overall and 4.18 points on the smallest objects. At equal transformer cost, Holm-corrected tests detect no FoVT deficit relative to a port of the official CF-ViT, but no dataset shows a corrected FoVT advantage in both seeds. FoVT requires no feature reuse, distillation loss, or selection schedule. Reusing coarse features shows no significant benefit and costs 1 to 3 points when the reuse module is trained at the head learning rate. Skipping refinement for the most confident 19 to 24 percent of images leaves accuracy unchanged to two decimal places. At the transformer cost of uniform 336-pixel inference, gated FoVT improves accuracy on four benchmarks, with the largest gains on NABirds and FGVC-Aircraft and no significant gain on Stanford Dogs. Foveation primarily saves computation: relative to a uniform 448-pixel model trained with the same auxiliary glance loss, ungated FoVT uses 44 percent fewer transformer operations, with no significant accuracy difference on four benchmarks and a 0.53-point deficit on FGVC-Aircraft. Wall-clock savings are smaller than the reduction in transformer operations.

---


### 179. [$\varepsilon$-SegFormer: Multi-Resolution Vision Transformers for Sparsely Supervised Segmentation in Electron Microscopy](https://arxiv.org/abs/2611.27796)

**<font color=#1a73e8>作者：</font>** Erfan Amidi, Sheida RahnamaiKordasiabi, Edoardo Giacomello 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Segmenting organelles in electron microscopy (EM) volumes requires dense annotations that take experts months to produce, and every gain in imaging resolution adds to this cost. Sparsely supervised methods reduce this cost to a small fraction of labeled pixels, but the convolutional networks they build on see a limited neighborhood around each pixel, while the identity of an organelle often depends on context far beyond it. We introduce $\varepsilon$-SegFormer, a multi-resolution Vision Transformer for sparsely supervised semantic segmentation, which builds on the architecture of MuViT and extends the training method of $\varepsilon$-Seg. For each labeled pixel, $\varepsilon$-SegFormer samples views at three physical resolutions centered on it, embeds their patches into a single token sequence, and encodes every token's position in image coordinates, so that attention relates all views in one shared frame. A segmentation head classifies the pixel from the tokens around it; during training, the pixel's own token is hidden, so the label must be predicted from context rather than local appearance. The model is trained in a single stage, without pretraining, with an auxiliary reconstruction loss. On the BetaSeg FIB-SEM dataset, $\varepsilon$-SegFormer learns from about 10,000 labeled pixels among the 670 million voxels inside three cells, and, given the cell mask, segments nuclei, mitochondria and insulin granules in a slice of a fourth, unseen cell with an average Dice of 0.89 (0.91 after post-processing). Ablations show that coarser views improve accuracy and that a compact head on local tokens works best, with the wider context entering through attention in the encoder.

---


### 180. [Refrain: Learning Multi-Shot Consistency from Inconsistent References for A$^2$O Video Generation](https://arxiv.org/abs/2611.27806)

**<font color=#1a73e8>作者：</font>** Hongru Yan, Yue Wu, Jian-Wei Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A comic-book character, a photorealistic cityscape, an oil-painted coffee cup -- such stylistically diverse references provide visual guidance across shots and frames, yet generating a coherent multi-shot video that unifies their visual styles while preserving subject identities and scene content remains challenging. Existing methods maintain cross-shot continuity through additional attention control or memory processing. However, they struggle to resolve disparate per-shot styles or handle reference-target duration mismatches within a single framework. We introduce Refrain, a unified model that learns cross-shot consistency through a self-supervised reconstruction task. Reference clips from the same original video are deliberately perturbed with distinct visual edits, and the model recovers the unedited source footage under a shared style prompt. The resulting pipeline yields DurMix-300K, which pairs independently edited references of varying durations with their original videos. Operating on the A$^2$O principle (Any Reference, Any Duration, One Timeline), Refrain maps image and video references onto a shared temporal canvas without auxiliary conditioning modules. For evaluation, experiments show that standard CLIP or DINO metrics frequently overlook stylistic clashes or misinterpret intended narrative cuts as inconsistency. We propose Shot-Debiased Consistency (SDC), which uses an extensive real-video bank to establish a baseline for style variation associated with content changes within shots. By discounting this baseline divergence, SDC evaluates cross-shot style shifts against real-world distributions, where smaller residual differences indicate higher stylistic continuity. Extensive experiments demonstrate that Refrain achieves state-of-the-art performance in cross-shot consistency, while excelling at shot timing, reference adherence, and text alignment.

---


### 181. [$\mathtt{DistP}$: Scaling Local-Update Training with Zero-Shot Hyperparameter Transfer](https://arxiv.org/abs/2611.27808)

**<font color=#1a73e8>作者：</font>** Andrej Jovanović, Alex Iacob, Philipp Wiesner 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Local-update methods offer a communication-efficient alternative to Distributed Data Parallelism ($\mathtt{DDP}$), but introduce additional hyperparameters that require costly tuning. For $\mathtt{DDP}$, zero-shot hyperparameter transfer reduces this cost by reusing settings tuned on smaller models, but its applicability to local-update training remains unclear. We propose $\mathtt{DistP}$, a theoretical framework extending existing transfer rules from $\mathtt{DDP}$ to local-update training with varying worker counts, local steps, and outer optimizers. With averaging as the outer optimizer, $\mathtt{DistP}$ supports learning-rate transfer across width and depth while improving model quality. The tuned inner learning rate also directly transfers across synchronization intervals, but follows two regimes when increasing the global batch size: square-root learning-rate scaling for larger local batches and a fixed reference rate for additional workers. We then generalize width and depth transfer to other outer optimizers, enabling stable scaling with $\mathtt{Adam}$. However, with momentum in the outer optimizer, changing batch size or local steps can require inner--outer learning-rate tuning, consistent with prior work. In language-modeling experiments at $823$M parameters, $\mathtt{DistP}$ reduces validation loss by $8.1\%$ and improves mean downstream accuracy by $10\%$ relative to baselines without retuning at the larger scale. Fitted scaling laws suggest that this advantage grows with the compute budget, reinforcing the benefits of $\mathtt{DistP}$ for communication-efficient training.

---


### 182. [Redesigning Neural Networks to Not be Confidently Wrong even to Strong Adversarial Attacks](https://arxiv.org/abs/2611.27811)

**<font color=#1a73e8>作者：</font>** Michael W. Spratling, Heiko H. Schütt  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Early deep learning models attempted to simulate visual perception using a neural hierarchy that alternated between two types of layer: one modelled on cortical simple cells (that was designed to increase selectivity), and one modelled on cortical complex cells (that aimed to increase tolerance). We show that such a neural network (NN) architecture, when implemented with novel components that are better able to learn selective and tolerant representations, is capable of accurate and robust image classification and improved alignment between the behaviour of the model and the perceptual abilities of humans. Firstly, the proposed models are shallow, fewer than ten layer-pairs, which is more consistent with the rapid feedforward object categorisation performed by the biological visual system. Secondly, they are far less prone to producing classification predictions with high confidence for samples from unknown classes or for image consisting of pure noise, and hence, like humans are not easily fooled into perceiving objects that are not present in the image. Thirdly, for the proposed NNs adversarial samples cause predictions with low confidence, enabling them to be accurately identified. In contrast to humans, our networks still do not correctly classify adversarial samples. However, the behaviour of our networks is a significant step towards human-like behaviour compared to standard DNNs that produce highly confident, but incorrect, classification predictions for adversarial samples. The increased robustness to adversarial and unknown samples is achieved while maintaining competitive performance in terms of generalisation to novel samples from the training categories. This enables models of this type to be competitive with state-of-the-art DNNs across multiple different evaluation metrics and benchmark tasks.

---


### 183. [Mixture of Latent Recursions for Low-Rank Adaptation](https://arxiv.org/abs/2611.27823)

**<font color=#1a73e8>作者：</font>** Weixun Luo, Ye Mao, Ranran Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-Rank Adaptation (LoRA) performs task-specific adaptation using a fixed low-rank architecture, whose expressiveness is typically increased by enlarging or adding learnable modules with a proportional parameter overhead. We introduce Mixture of Latent Recursions (MoLR), an adaptive recursion framework that enhances adaptation expressiveness while preserving parameter efficiency. MoLR recursively refines the down-projected latent representation of each input using a shared transformation. A lightweight threshold-based router independently determines whether each token should undergo further refinement, while dynamically adjusted thresholds encourage balanced utilization across recursion depths. Extensive experiments across diverse language and vision tasks demonstrate that MoLR consistently outperforms representative LoRA variants with negligible parameter overhead over LoRA. Further analyses show that MoLR learns input-dependent recursion-depth allocation and enables a controllable inference-time compute-performance trade-off without requiring retraining. Code will be publicly available.

---


### 184. [Graph Signal Generation via Graph-Aware Diffusion Models](https://arxiv.org/abs/2611.27826)

**<font color=#1a73e8>作者：</font>** Vimal K B, Sergio Rozada, Antonio G. Marques 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many signals are defined on the nodes of a graph, such as traffic flow at road sensors or user purchases of related products. They are often partly observed, and learning their distribution enables imputing missing values and forecasting future ones. Diffusion models learn such distributions, but their forward noise is independent across nodes and does not depend on the graph. We introduce graph-aware diffusion (GAD), whose forward process is a heat diffusion on the graph driven by Gaussian noise. In the graph Fourier basis, the forward transition is a scalar Gaussian channel at each frequency. With a shared diffusion rate, high graph frequencies are attenuated faster than low ones. We propose Mode-Adaptive SNR Scheduling (MASS), which assigns each graph frequency its own diffusion rate and keeps all of them at the same SNR. For graph-stationary signals, MASS equalizes the normalized error of the optimal linear denoiser across frequencies. We bound reverse-SDE stiffness as a function of the (shifted) Laplacian's condition number, with a logarithmic upper bound for MASS and a linear lower bound for shared rates. GAD with MASS improves recommendation accuracy by 5-19%, reduces traffic-imputation RMSE by up to 7.8% with half as many reverse steps, and improves forecasting MAE and RMSE using only 3 reverse steps.

---


### 185. [DGC-Net: A Depth-Geometric Conditioning Network for Projection-Supervised OCTA Segmentation](https://arxiv.org/abs/2611.27854)

**<font color=#1a73e8>作者：</font>** Lucas Santiago, Bisheng Wang, Jaime S. Cardoso 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> OCTA segmentation is commonly formulated as a projection supervised task: models observe 3D volumetric scans but are supervised by 2D en-face semantic maps. Existing 2D and 3D-to-2D methods either discard axial information or compress depth responses into latent projections, leaving vessel crossings, diffuse capillary regions, and FAZ boundaries vulnerable to projection-induced ambiguity. We propose DGC-Net, a Depth-Geometric Conditioning Network that recasts 3D-to-2D OCTA segmentation as depth-geometrically conditioned prediction, where projected features are decoded with compact descriptors of axial vascular evidence. DGC-Net preserves local depth geometry through Depth-Moment Conditioning (DM), which injects axial localization and dispersion cues into the projection stream, and captures global depth layout through Holistic Depth-Geometry Modulation (HDM), which derives a raw-volume axial prior for final 2D decoding. Experiments on the OCTA-500 6mm and 3mm subsets show that DGC-Net achieves 83.58% and 88.62% mIoU, respectively, reaching state-of-the-art performance.

---


### 186. [Anchors That Move Without Collapsing: Exclusive-Region Anchor Routing for Vision Transformers](https://arxiv.org/abs/2611.27855)

**<font color=#1a73e8>作者：</font>** Aadi Gupta  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Anchor tokens let a vision transformer exchange global information through a few summaries, but nothing forces different anchors to summarise different things. On one shared backbone we show that a Perceiver-style pathway and an AnchorFormer pathway collapse to a single summary, the latter despite its mass normalisation (pooling-map similarity 0.99), while other soft pathways, including Representative Attention, stay partly redundant (0.59-0.79). These results concern the routing modules inside our block, not the full published models. An exclusive partition of the patch grid cannot collapse by construction, and matched component by component it is 2.4-3.6 points more accurate than Representative Attention on CIFAR-100. We then propose focus anchors, which place most anchors at the peaks of a learned importance map while all anchors keep one exclusive Voronoi partition. Focus anchors beat a fixed partition on a cluttered canvas (+1.5 points, 95% CI [0.5, 2.6]) but not on full-HD traffic-sign recognition. There, both variants match dense attention with local windows at about a fifth of its FLOPs, and the fixed partition also trains 1.5x faster per step than dense attention with FlashAttention, though both use more memory; a ViT on a downsampled input loses half its mean average precision. Hard exclusive assignment is the only region assignment we tested that is both stable and most accurate: softmax and Sinkhorn relaxations diverge, and Gumbel-softmax trains but is less accurate. We also report the limits: a ResNet-18 is more accurate on every task we trained it on in this from-scratch regime, and anchors train faster than FlashAttention only from about 1536x1536 pixels and never use less memory.

---


### 187. [OpenAHBU: Open-sourced Automatic Human Behaviour Understanding Toolkit Through Facial Behaviour Analysis](https://arxiv.org/abs/2611.27862)

**<font color=#1a73e8>作者：</font>** Zijian Wu, Yupeng Huo, Cheng Luo 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic facial behaviour understanding (AFBU) is fundamental to various human-centred applications, yet existing academically available toolkits offer limited functionality, closed training pipelines, and weak generalisation. This paper presents OpenAHBU, a fully open-sourced, generalisable toolkit integrating 11 AFBU functions across three semantic levels: (i) short-term external facial attributes, including landmarks, blendshapes, Action Units, and expressions; (ii) short-term facial behaviour-related human psychological states, including valence/arousal and pain; and (iii) long-term facial behaviour-related psychological traits, including depression and personality. Particularly, we re-developed eight functions, where at least four deep learning models covering different computational complexities are developed for each function, providing flexible deployment on resource-constrained and high-throughput computing scenarios. More importantly, models of most functions are trained on a comprehensive corpus aggregating multiple academically available datasets, ensuring robust cross-dataset this http URL addition, we include a Synergistic Multi-task Enhancement (SMTE) module to efficiently and adaptively enhance each OpenAHBU function by leveraging the complementary cues contained in its most-related support function's this http URL evaluations demonstrate that our OpenAHBU outperformed existing open-source toolkits not only in functional coverage but also the predictive performances, while providing superior deployment flexibility across diverse computational this http URL fully publicly available training and inference scripts, pre-trained weights, user-friendly GUI, Python library, and cross-platform compatibility, our OpenAHBU provides a reproducible, scalable and extensible toolkit at this https URL.

---


### 188. [SLICR: Strategy Logic-Guided Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2611.27865)

**<font color=#1a73e8>作者：</font>** Arshia Rafieioskouie, Matthew Lucas, Tzu-Han Hsu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Specification-guided reinforcement learning (RL) translates formal specifications of desired behavior of agents into shaped rewards. This paper introduces SLICR, a significant paradigm shift that advances the state of the art to specification-guided RL in adversarial settings under partial observability. We employ Strategy Logic (SL), which allows explicit quantification over agents' strategies and uses the linear temporal logic (LTL) to specify the agents' objectives and constraints. This enables reasoning not only about how agents should act to satisfy a specification, but also about how they should respond to the strategies and behaviors of other agents. We evaluate SLICR on three popular benchmarks: Predator-Prey, Google Research Football, and our home-grown extension of SMAC-HARD, demonstrating its effectiveness, scalability, and ability to adapt to diverse adversarial strategies.

---


### 189. [Beyond Visual Fidelity: Comparing Categorical and Continuous World Models](https://arxiv.org/abs/2611.27870)

**<font color=#1a73e8>作者：</font>** Sarah Parisot, Melanie Fernandez Pradier, David Bignell 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Visual world models can now generate compelling interactive worlds, but visual realism does not guarantee faithful dynamics. We systematically compare how categorical and continuous prediction shape learned dynamics under both next-token and iterative whole-frame generation. These choices are often bundled in approaches such as autoregressive token models and whole-frame flow matching. We design controlled 2D and 3D environments and evaluate dynamics validity, calibration, and visual quality. In 2D with lossless visual encoding, categorical models achieve higher rollout validity with less training compute, particularly for stochastic entities. Among categorical models, greedy decoding produces the highest rollout validity, while sampling from a next-token model yields the best-calibrated stochastic predictions. Failures in continuous models, such as disappearing game characters, echo those seen in more complex environments. Here, known dynamics let us measure their impact. In 3D, categorical models also achieve stronger long-horizon performance with less training compute. Even models with lossy tokenization remain competitive on semantic accuracy and FVD, despite lower next-frame RGB accuracy. Together, these findings make a strong case for categorical prediction as a compute-efficient route to learning world dynamics.

---


### 190. [From Gist to Verbatim: The Controllable Path of One Image Through a Diffusion Prior](https://arxiv.org/abs/2611.27875)

**<font color=#1a73e8>作者：</font>** Luca Saglietti, Luca Giammanco, Marc Mezard 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern generative models are typically studied for their ability to generalize, while memorization is treated as a failure mode. We invert this perspective and ask how a generative model can recall a single datum. We frame memorization as a control problem: a learned conditioning signal steers a frozen diffusion model toward a target image, and we follow the formation of this memory throughout training. Before converging to exact reproduction (verbatim), memory passes through a regime of abstraction: samples preserve the target's semantic content (gist) while remaining diverse in appearance, leaving predictable detail to the generative prior. This semantic organization emerges despite the absence of labels, captions, or any explicit semantic objective. In the abstraction regime, the learned memory approaches ordinary text conditioning and supports editing, one-shot recognition, and retrieval more effectively than in the near-perfect reconstruction regime. These results suggest that memorization can serve as a probe of the relevance structure encoded by a generative model: what must be stored about a datum, what can be reconstructed from prior knowledge, and how learned memories interpolate between reconstructive recall and literal data storage.

---


### 191. [Renormalized Entropy from Symmetries: Simplicity Bias and Neural Heat Death](https://arxiv.org/abs/2611.27889)

**<font color=#1a73e8>作者：</font>** Vasco Portilheiro, Samuel Liebana, Andrew Saxe 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural networks have parameter symmetries: parameter transformations that do not affect the represented function. How do these symmetries affect the functions that neural networks ultimately learn? We study the implicit bias arising from these symmetries by calculating the equilibrium distribution over represented functions under Langevin dynamics with Gaussian regularization. To isolate the effect of symmetries on this distribution, we study the limit in which the strength of the regularization is taken to zero. In certain cases, we show that the zero-regularization and infinite-time limits commute. In the low temperature limit, we recover known effective regularizations. At positive temperature, a renormalization procedure allows us to derive a novel entropy which predicts symmetry-induced preference for certain functions. For linear networks, we obtain explicit entropy terms that favor singular and low-rank functions. For networks with homogeneous activations, we find entropy terms that favor inactive neurons, which can lead to neural "heat death" in which equilibrium mass concentrates on networks with vanishing output. We interpret these results through the neural tangent kernel, as a simplicity bias selecting for functions that vary slowly under variations in the parameters.

---


### 192. [FairITR: Fairness-Aware Learning of Multicategory Individualized Treatment Rules](https://arxiv.org/abs/2611.27894)

**<font color=#1a73e8>作者：</font>** Zeyu Chen, Wei Qian, Bintong Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Individualized treatment rules (ITRs) recommend treatment decisions based on individual characteristics and can improve treatment outcomes beyond traditional one-size-fits-all strategies. However, similar to other commonly used algorithmic decision-making methods, ITRs without considering model fairness may result in unfair decisions across groups defined by sensitive attributes, such as race or gender. Although extensive methods have been developed for ITR estimation, most focus solely on optimizing treatment outcomes, while research on fairness-aware ITRs remains limited. Moreover, the practical scenario of multicategory treatments is rarely considered in existing fair ITR studies. To address these gaps, we introduce a fairness notion for multicategory ITRs that requires treatment decisions to be independent of sensitive attributes, and then formulate the corresponding problem of estimating fair ITRs. To solve this problem, we further propose FairITR, a fairness-aware learning framework that jointly optimizes treatment outcomes and fairness. FairITR builds on angle-based classification for multicategory ITR learning and integrates adversarial learning with covariance-based regularization to mitigate unfairness in treatment decisions. A theoretical justification for the fairness properties induced by the adversarial debiasing mechanism is also provided. Extensive experiments on real-world datasets show that FairITR substantially reduces unfairness in ITRs while maintaining competitive treatment values relative to existing baselines.

---


### 193. [Metadata-Private Voice Communication over Tor using Post-Quantum Key Encapsulation](https://arxiv.org/abs/2611.27909)

**<font color=#1a73e8>作者：</font>** Noah Zeinali Yazdi, Samuel Zeinali Yazdi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Encrypted voice communication systems commonly protect call content but expose significant metadata, including the network identities of both parties, call timing, and traffic patterns. Simultaneously, advances in quantum computing threaten the asymmetric primitives underlying conventional key exchange, creating a harvest-now, decrypt-later risk for long-lived sensitive communications. Existing systems address at most one of these concerns: secure VoIP applications such as Signal and Wire rely on centralized infrastructure and classical cryptography, while anonymous communication tools built on the Tor network support only text messaging and lack post-quantum key encapsulation. This paper presents SAPEC (Secure Anonymous Peer Exchange Communicator), a peer-to-peer voice communication system that simultaneously addresses anonymity, decentralization, and quantum resistance. SAPEC routes all traffic exclusively through Tor hidden services, concealing the IP addresses of both parties, and augments the standard TLS handshake with a custom protocol layer that performs ML-KEM-1024 key establishment, a settle on AES-256 symmetrical keys and mutual Dilithium identity verification before any audio is transmitted. All audio is subsequently encrypted under AES-256. A removable Crypto Ignition Key prevents identity key material from being stored on the device. Empirical evaluation across 45 independently circuit-rebuilt test runs yielded a median one-way audio delay of 355 milliseconds and a median connection setup time of 7.61 seconds on same-region Tor circuits, demonstrating that interactive voice communication over onion routing is practically achievable.

---


### 194. [Functional Depth Is Learned: Isolating the Computation That Layers Produce Only Together](https://arxiv.org/abs/2611.27911)

**<font color=#1a73e8>作者：</font>** JaeSeong Kim, KyungTae Lim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Transformer performance scales with depth, but layer count merely counts the opportunities for sequential computation: layers could still behave as nearly independent refinements that barely depend on one another. We study how transformers develop functional depth during pretraining, introducing an exact inclusion-exclusion decomposition that isolates the connected component, i.e., the computation that appears only when a specified set of layers acts together under identity ablation. Tracking this quantity across public checkpoints of Pythia, OLMo, and Amber yields three findings. First, write-relative connected coordination strengthens from its initialization or earliest-checkpoint baseline as pretraining proceeds, across all measured interaction orders. Second, these connected components are behaviorally consequential under direct intervention: deleting them damages perplexity more than deleting a norm-matched random direction at the same site in all 35 measured model-order cells. Third, pairwise representation similarity is consistently negatively correlated with pairwise connected coordination across seven models, yet the two signals are not interchangeable: similarity- and coordination-based block-removal criteria often agree in Pythia but diverge on Amber. Together, these results suggest that architectural depth provides the opportunity for sequential computation, while pretraining progressively organizes cross-layer dependencies within that depth.

---


### 195. [Star Panoptic Quality: Selectively Evaluating Split and Merged Instances](https://arxiv.org/abs/2611.27913)

**<font color=#1a73e8>作者：</font>** Erik Großkopf, Paula Tamara Buzduga, Hendrik Möller 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detecting individual instances is crucial for many segmentation problems. However, expert instance annotations are often unavailable, so instances are approximated heuristically (e.g., as connected components of semantic maps), which can merge touching objects or split fragmented ones. Even when expert annotations exist, expert disagreement or structural delineation biases can yield split or merged reference instances, corresponding to over- or under-segmentation, respectively. Panoptic Quality (PQ) and related metrics capture both segmentation and detection quality while weighting all instances equally, regardless of size. Yet when the references are biased, these metrics can neither detect split or merged instances nor distinguish valid from invalid overor under-segmentation. We present Star Panoptic Quality (StarPQ), a novel evaluation ramework, which closes this gap in two steps: First, we construct a so-called star forest in the bipartite graph whose clean, merge, and split stars isolate different failure modes. Second, we calculate the final metric by individually weighting each failure mode, allowing practitioners to account for instance delineation biases. Across various experiments, we demonstrate that StarPQ not only enables targeted penalization or eniency towards specific failure modes, but also serves as a diagnostic tool to reveal their prevalence.

---


### 196. [SUAF: Spectral Universal Advantage Features for Zero-Shot Policy Improvement](https://arxiv.org/abs/2611.27919)

**<font color=#1a73e8>作者：</font>** Huaze Tang, Runqing Miao, Tianren Peng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reward-independent representations enable reinforcement learning agents to reuse knowledge across tasks, but limited representation capacity raises three fundamental questions: what statistical dependence should these representations capture, which components of that dependence should be retained for policy improvement, and how does discarding the remaining components affect decision-making? We address these questions through canonical dependence analysis. For a reference policy, we construct an action-centered, positive-lag canonical dependence matrix (CDM) that isolates the additional predictive contribution of the current action beyond the current state. Its singular value decomposition yields Spectral Universal Advantage Features (SUAF), paired features that recover delayed advantage through linear reward projections. We show that the spectrum quantifies mutual information between current action and future state-action visitation conditioned on current state and determines reward specific approximation errors. Retaining the leading modes gives optimal rank-constrained approximations under both isotropic average-case and reward-uniform minimax criteria. Separating the immediate reward contrast also avoids the spectral floor arising from direct compression of the full advantage operator. To learn SUAF from reward-free data, we develop an action-centered Soft-HGR objective with bidirectional temporal-difference estimation. We further connect spectral approximation errors to sufficient conditions for policy improvement. Finite-state experiments validate the spectral predictions and feature-learning method, while zero-shot evaluations on discrete tasks and continuous-control benchmarks demonstrate the utility of the learned representations across rewards.

---


### 197. [ESSI: Computationally Efficient Semantic Search for Sparse Autoencoder Concepts](https://arxiv.org/abs/2611.27921)

**<font color=#1a73e8>作者：</font>** James Baker  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) decompose diffusion model activations into interpretable features, but steering a model with them requires identifying which features map to a given semantic concept, if any. Existing methods for this concept to feature task are expensive, relying on grid searches or repeated passes through the frozen UNet. We propose Efficient Semantic Sparse Identification (ESSI). Using segmentation masks to label SDXL activations as concept or non-concept, ESSI ranks SAE features and binary-searches for the smallest set on which a linear classifier still separates positive from negative samples while not falling below a performance threshold, then reuses that classifier to calibrate the steering strength. We evaluate the same selected features on both concept insertion and object unlearning. Compared with prior work, ESSI is as cheap or cheaper, and performs well on both insertion and removal.

---


### 198. [BioEmu2: Scalable Emulation of Biomolecular Dynamics](https://arxiv.org/abs/2611.27924)

**<font color=#1a73e8>作者：</font>** Michael Gastegger, Adam E. Foster, José Jiménez-Luna 等 30 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite major advances in structure prediction, modelling the motions and interactions that drive biomolecular function at scale remains a central challenge. We introduce BioEmu2, a generative model for atomically resolved biomolecular structures combining static structure prediction, equilibrium sampling and time evolution, that samples orders of magnitude faster than molecular dynamics (MD). Trained on experimental and synthetic structures and extensive MD data, it supports multi-component systems containing proteins, nucleic acids, modified residues, ligands and ions. Structure-prediction accuracy is comparable to top open-weight biomolecular folding models, and a context parallel mode enables prediction of megadalton complexes. Equilibrium distributions approximate MD references with free-energy errors near 1 kcal/mol across tested proteins and complexes. Time propagation predicts long-timescale dynamical trajectories and kinetics of binding and conformational changes. Generated structures can be controlled by conditioning on residue contacts or steering with user-defined bias potentials. Enhanced sampling enables free energy calculation involving rare states. BioEmu2 makes the study of biomolecular ensembles and dynamics scalable.

---


### 199. [The Optimal Sample Complexity of Agnostic PAC Learning for Partial Concept Classes](https://arxiv.org/abs/2611.27946)

**<font color=#1a73e8>作者：</font>** Liang-Yu Zou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Let $\mathcal H\subseteq\{-1,+1,\star\}^{\mathcal X}$ be a partial concept class of finite VC dimension $d$. We construct a deterministic agnostic PAC learner that, for every $\varepsilon,\delta\in(0,1)$, uses $O((d+\log(1/\delta))/\varepsilon^2)$ i.i.d. examples from an arbitrary distribution $\mathcal D$ over $\mathcal X\times\{-1,+1\}$ and returns a total concept $\hat h:\mathcal X\to\{-1,+1\}$ satisfying $\text{er}_{\mathcal D}(\hat h)\leq \min_{h\in\mathcal H}\text{er}_{\mathcal D}(h)+\varepsilon$ with probability at least $1-\delta$, where $\text{er}_{\mathcal D}(h)=\mathbb P_{(x,y)\sim\mathcal D}[h(x)\neq y]$. This establishes the optimal sample complexity, matching the lower bound of Alon et al. (FOCS 2021).

---


### 200. [Topology Hub Optimal Transport: Eliminating Long Context Dilution at Flash Speed](https://arxiv.org/abs/2611.27951)

**<font color=#1a73e8>作者：</font>** Dylan Forde  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-context models use sparse or structured attention to avoid quadratic cost, yet retrieving a small set of relevant facts embedded among hundreds of thousands of distractors degrades as normalization mass disperses with length. Hub-and-spoke optimal transport (OT) replaces the dense $L \times L$ matrix with a linear-size graph over local windows and $K$ shared hubs balanced by Sinkhorn scaling. Building on block-wise tail refinement and fixed-support transport topology (arXiv:2605.08123, arXiv:2609.07954), we introduce Topology Hub Optimal Transport (THOT): (1) bounded-support capacity gating via simplex sparsemax ($O(L\log L)$) or sorting-free token-local thresholded ReLU ($O(L)$), driving excess distractor mass to zero; (2) a three-sweep $1+2$ annealed row-closed Sinkhorn schedule that damps bipartite residuals; (3) an exact rank-$(D+2R+1)$ One-Reference-Tile adjoint in batched split-factor Triton kernels (BF16 Tensor Cores, FP32 potentials); and (4) a chunked exclusive-prefix causal variant with verified zero future leakage. On NVIDIA L4, sparsemax THOT trained at $L=128$ reaches 97.40% zero-shot recall of fixed bindings at $L=262{,}144$ under pure task loss ($\alpha=0$) and 98.83% at $\alpha=0.05$ (matched by $O(L)$ thresholded ReLU at $\alpha=0.05$, vs. 80.60% at $\alpha=0$), while softmax-gated hub OT drops to 3.52%. In bidirectional operator microbenchmarks, our kernel runs forward+VJP in 100.1 ms at $H=8, D=64, L=262\mathrm{K}$ (2.2x faster with 4.0x smaller compiler temporaries than latent softmax) and 1.34 ms vs. 4.37 ms for cuDNN FlashAttention at $L=4{,}096$; multi-layer LM runs use the unfused path. Zero-shot WikiText-103 multi-needle retrieval hits 100.00% (128/128 queries at $L=65\mathrm{K}$) vs. 0.78% for short-trained RoPE FlashAttention, and compact 4-layer WikiText-4K runs show modest causal and masked LM gains.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-206](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
