# 📦 其他研究 | 2026年11月24日

> 本类共 **206** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-206](./part-05.md)

---

### 1. [On the loss landscape of the linear neural network: beyond critical points](https://arxiv.org/abs/2611.26671)

**<font color=#1a73e8>作者：</font>** Antoine Lejay, Lionel Lenotre, Sa{ï}d Toubra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While the critical points of the loss landscape in linear neural networks have been extensively studied since the seminal work of Baldi \& Hornik in the late 1980s, a description of this landscape at an intermediate or global scale is still lacking. Such a characterization is crucial, particularly as a substantial body of literature indicates that gradient descent circumvents critical points. The present article introduces an intermediate structure, termed the critical thalweg, which encompasses all critical points and exhibits key geometric properties. Beyond providing a geometric proof of Baldi \& Hornik's results using simpler assumptions than the existing literature, this framework offers a global view of the loss landscape that can be easily visualized in a two-dimensional plane. Empirical observations suggest that gradient descent is attracted toward the critical thalweg, along which the loss continues to decrease to its global minimum.

---


### 2. [Parasite Features: Causal Abstraction Through Spurious Pathways](https://arxiv.org/abs/2611.26711)

**<font color=#1a73e8>作者：</font>** Denis Sutter, Qing Yao, Sasha Boguraev 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal Abstraction defines a notion of \emph{equivalence} between a neural network and an algorithm, thus serving as a powerful framework for mechanistic interpretability. In this paper, however, we show the existence of a class of \emph{spurious features} which straightforwardly pass such equivalence tests. Suppose there are two directions in a model's representation space where: (i) one discriminates the input based on some feature, and (ii) the other steers the model towards a certain output. Interpretability methods based on Causal Abstraction (e.g., Distributed Alignment Search) can \emph{spuriously} simulate these directions' combined behavior by leveraging pathways passing through them, giving the impression that the model implements this feature. In such cases, we say the method discovered a \defn{parasite feature}. Experimentally, we show that Distributed Alignment Search finds parasite features using linear alignment maps in two tasks: syntactic agreement and two-digit addition. Our paper highlights an important consideration for Causal Abstraction and contributes to the ongoing debate about best practices for mechanistic interpretability.

---


### 3. [Forehead ROI Localization under Real-World Imaging Degradations via Cross-View Pseudo-Labeling](https://arxiv.org/abs/2611.26712)

**<font color=#1a73e8>作者：</font>** Geetanjali Sharma, Gaurav Jaswal, Aditya Nigam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Forehead region-of-interest (ROI) localization is important for forehead-creases biometrics, particularly when the lower face is occluded. However, localization remains challenging under varying image quality, pose, and illumination. We propose Confidence and Consistency Guided Pseudo-Labeling (CCGP), which adapts Grounding DINO using unlabeled facial images filtered by detection confidence and geometric consistency between original and horizontally flipped views, without modifying the detector architecture or loss. We evaluate CCGP on five external datasets and 350 images spanning seven imaging conditions. CCGP achieves the highest mean intersection over union (mIoU) on four of five external datasets, improving from 0.415 to 0.580 on RMFRD compared with supervised Grounding DINO. On the quality-stratified subset, the largest gains occur under blur (0.487 to 0.719) and low contrast (0.615 to 0.710). CCGP also outperforms conventional self-training on RMFRD (0.580 versus 0.551 mIoU). Despite a slight in-domain performance gap (0.861 vs. 0.866 mIoU) and challenges with off-angle poses, CCGP improves cross-dataset localization under challenging imaging conditions.

---


### 4. [SCATR-ITS: a scalable transformer for large-area individual tree segmentation from LiDAR point clouds](https://arxiv.org/abs/2611.26715)

**<font color=#1a73e8>作者：</font>** Lassi Ruoppa, Verneri Seppänen, Antero Kukko 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Individual tree segmentation (ITS) from LiDAR point clouds is one of the most widely studied segmentation tasks in forestry. Although deep learning methods define the state of the art on the majority of ITS benchmarks, their high computational complexity and long runtime currently prevent their adoption in large-scale operational workflows. In this work, we present SCATR-ITS, a scalable transformer model specifically designed for efficient ITS over large geographical areas. Based on the ForestFormer3D framework, SCATR-ITS transitions to superpoint-level processing to accelerate inference, with the superpoints constructed from learned embeddings. The architecture incorporates size-aware superpoint-level postprocessing, a dynamic query count module to handle high variation in forest structure, and a maximal input stride designed to minimize prediction redundancy. SCATR-ITS achieves accuracy on par with the state of the art on the FGI-EMIT and FOR-InstanceV2 datasets with an up to 8.5$\times$ higher inference speed. In addition, SCATR-ITS has a significantly lower GPU VRAM footprint during both training and inference, and exhibits excellent zero-shot generalization across multiple datasets. To demonstrate large-area ITS capabilities, SCATR-ITS is applied to a 142 km$^2$ region of Finnish national laser scanning data where it achieves an average throughput of 13.8 min/km$^2$, $\sim$18.6$\times$ faster than ForestFormer3D and approaching the speed of the unsupervised watershed algorithm, which it vastly outperforms in accuracy and segment quality. Overall, SCATR-ITS delivers state-of-the-art accuracy at speeds where operational-scale adoption becomes viable, paving the way toward countrywide deployment. The source code for SCATR-ITS and pretrained weights are available at this https URL.

---


### 5. [TOUMAII: A 4.5M-Pair Tool-Calling Preference Dataset and Its Source-Agnostic Generator](https://arxiv.org/abs/2611.26722)

**<font color=#1a73e8>作者：</font>** Moritz Pötzsch, Andrea Gentilini, Lisa Rossgoderer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> To autonomously execute multi-step tasks, enterprise agents must reliably interact with tools, call APIs, or query databases, making tool-calling a fundamental capability of AI models. Supervised fine-tuning (SFT) optimises for producing the correct call, but never contrasts it with a plausible incorrect one. In an environment where even a minor formatting error can invalidate a call and an incorrect decision can derail the interaction, direct preference optimisation (DPO) targets exactly this contrast. DPO, therefore, requires preference pairs rather than plain demonstrations. For tool-calling, such data, especially in realistic multi-turn settings, remains extremely scarce. To address this scarcity, we introduce TOUMAII, a large-scale tool-calling preference dataset containing ~4.5M validated preference pairs, derived from Agent-Ark/Toucan-1.5M (apache-2.0) conversations. The dataset consists of multi- and single-turn interactions and includes parallel and sequential function calls. Additionally, we release TOUMAII-Gen, a synthetic data generation pipeline that consumes tool-calling SFT datasets and generates a preference dataset with naturally occurring model-generated tool-calling failure modes. To validate the effectiveness of our DPO data, we fine-tune a 3-billion-parameter model, achieving performance parity with other high-quality tool-calling preference datasets. Furthermore, we release a second small preference dataset derived from ToolACE (apache-2.0), showcasing the source-agnostic nature of our pipeline.
We release the complete code and datasets: this https URL and this https URL

---


### 6. [Decomposing images in a PRISM: A Single-Source Multi-View Framework for Image Representation](https://arxiv.org/abs/2611.26726)

**<font color=#1a73e8>作者：</font>** Eduardo Campos, Willam Cardoso, Diego Furtado 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-view learning has shown that combining complementary views can improve predictive performance, yet many datasets provide a single raw source of information. How can multiple useful views be constructed from one source? We propose PRISM (Plural Representations of Images via Structural Maps), a framework that transforms an image into representations with distinct inductive biases through explicit structural maps, together with a protocol for measuring what each view contributes. We evaluate PRISM-HD, a hand-designed instantiation of PRISM in which the constructed views are summarized through representation-specific descriptors, on three artistic and four non-artistic image datasets. Analyses at a fixed feature budget show that the gains of the structural views are not explained by feature dimensionality alone. PRISM-HD by itself outperforms WND-CHARM on all seven datasets. Moreover, PRISM-HD and Fisher Vector provide complementary predictive signals: their equal-weight combination improves over the better individual representation by 5--8 percentage points on the artistic datasets. When combined with fine-tuned deep networks through a fixed parameter-free fusion rule, the PRISM-based representation improves performance on four of seven datasets and leaves it statistically unchanged on the remaining three, indicating that the constructed views provide predictive signals that are complementary to learned deep representations.

---


### 7. [SparseHPS: A Unified Model for Human Pose and Shape across Depth Cameras and LiDARs](https://arxiv.org/abs/2611.26730)

**<font color=#1a73e8>作者：</font>** Ilya Zaychuk  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering 3D human pose and shape from point clouds is central to motion capture, robotics and self-driving vehicles, because depth cameras and LiDARs sense a person directly in metric 3D and work under any lighting. However, current approaches are each tailored to one sensor type: point density differs by more than ten times between devices, public datasets are labeled with incompatible body models, and LiDAR approaches need long input sequences to offset sparse scans. In this work, we present SparseHPS, a novel sensor-agnostic network that recovers SMPL-X pose, shape and global translation from a human point cloud with one set of weights, for single frames and streams alike. Specifically, SparseHPS encodes the cloud with a LitePT backbone over sparse voxels, represents every joint by a learnable query decoded with one common head, localizes the body by voting over voxels, and draws temporal context from a causal memory of tokens from the seven preceding frames. A single model is trained on ten datasets that mix rendered clouds with real depth-camera and LiDAR captures, all converted to one body model. Experiments demonstrate state-of-the-art results on the SLOPER4D and FreeMotion LiDAR benchmarks, where SparseHPS lowers the root-relative joint error by 22% and 11%, respectively, compared with the strongest prior method, which needs 32 frames. On real Azure Kinect captures of held-out HuMMan subjects, SparseHPS attains a joint error of 34.7 mm. Moreover, the current frame alone already yields the bulk of this accuracy.

---


### 8. [Cross-Attack Robust Aggregation for Federated Learning](https://arxiv.org/abs/2611.26731)

**<font color=#1a73e8>作者：</font>** Eyhab Al-Masri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) lets resource-constrained IoT and edge devices train a shared model without exchanging raw data, but compromised or faulty devices can poison the global model. Existing robust aggregators each fail in some regime: naive averaging (FedAvg) collapses under high-magnitude attacks, whereas distance- and statistics-based defenses (Krum, median, trimmed mean) sacrifice accuracy on non-IID data and remain vulnerable to stealthy attacks. We present FedTether, which reweights client updates by their deviation from a coordinatewise median through a robust, dead-zoned score applied as a server-side optimizer step. Across three datasets, three attack types, and Byzantine fractions up to 40%, FedTether is the only method top-tier in every regime: it matches FedAvg under stealthy attacks with no robustness tax, exceeds robust baselines by up to 42 accuracy points, and stays accurate where high-magnitude attacks reduce FedAvg to near-random. These properties persist at 50 clients under partial participation, with no shared data or validation set.

---


### 9. [INCISE: Training-Free In-Context Segmentation of Surgical Videos](https://arxiv.org/abs/2611.26734)

**<font color=#1a73e8>作者：</font>** Yifan Xu, Bofang Zheng, Guangyu Meng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surgical video analysis requires video object segmentation (VOS), yet existing methods are commonly based on pretrained model fine-tuning using a large number of expert labels. In-context segmentation (ICS) offers the promise of bypassing this high cost by segmenting a target video using a few annotated references, which are the sole source of surgical knowledge for a frozen model. However, existing ICS methods tend to draw such references at random, which concentrate on a few views that dominate a surgical video and can miss other objects of interest (e.g., transient instruments and small structures). To address these challenges, we propose INCISE, a training-free ICS framework for surgical videos. INCISE selects unlabeled frames from multiple surgical videos that jointly cover the local appearances of a target video, and then segments the target video using these references. With only 1.7% of training frames selected and annotated as references and no target video frame labeled, INCISE obtains 67.2% mean mIoU and outperforms the best SOTA fine-tuned method by 9.2 points. We hope INCISE can help establish ICS as a practical alternative to fine-tuning in surgical video analysis and other domains with a costly labeling burden.

---


### 10. [ConRef: Auditing Reference Reliability in 2D/3D Registration Benchmarks](https://arxiv.org/abs/2611.26758)

**<font color=#1a73e8>作者：</font>** Jianfeng Yue, Feng Li, Tianyu Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Purpose: Accurate 2D/3D registration is crucial for image-guided orthopedic interventions, enabling the alignment of preoperative 3D anatomy with intraoperative X-ray observations for surgical navigation. Public benchmarks have facilitated the development and evaluation of increasingly accurate registration methods. However, as registration errors approach the uncertainty of benchmark reference poses, measured performance may be limited by reference inaccuracies rather than algorithmic errors alone. Methods: We propose Consensus Reference (ConRef), a multi-view framework for auditing reference poses in existing X-ray/computed tomography (CT) registration benchmarks. By jointly exploiting multiple X-ray observations, ConRef estimates an additional reference pose, quantifies its uncertainty, and identifies potential X-ray outliers. We validate the framework using independent anatomical evidence and a newly acquired X-ray/cone-beam CT (CBCT) phantom dataset with bead-based reference poses. Results: On our BeadPhant dataset, ConRef differed from independent bead-based references by 0.08-0.12 mm, while discrepancies with original references reached 2.06 mm on the Femur dataset. It also flagged 22 DeepFluoro X-rays as potential outliers. On Femur F5, reference choice changed the submillimeter success conclusions of the same registrations. Conclusion: Our findings demonstrate that reference discrepancies can influence the evaluation of high-accuracy 2D/3D registration methods. By providing an additional, independently validated reference and identifying potential inconsistencies, ConRef enables systematic auditing of existing benchmarks and supports more reliable evaluation of registration error.

---


### 11. [Who Should Verify? Reviewer Selection with Partial Information and Outcome Audits](https://arxiv.org/abs/2611.26770)

**<font color=#1a73e8>作者：</font>** Viet Bui, Tien Mai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Selecting an AI reviewer requires evidence about what it does after reading a draft. On a fixed batch of items, a team can keep the original answers or adopt one reviewer's answers throughout. We ask how much it costs to certify that the chosen procedure falls at most a specified number of correct answers short of the best available procedure, for every completion of the unobserved evidence. When all reviews are available and only verified answer keys cost money, we give an exact stopping rule and an integer program for the cheapest certificate in hindsight. When reviews and keys both have prices, a polynomial-time algorithm using the completed record approximates the minimum certificate cost within a factor logarithmic in the number of procedures. This dependence is tight to leading order unless P equals NP. Finding a certificate can be much more expensive. We exhibit a two-procedure family with $n$ unresolved items where one purchase suffices in hindsight but the exact minimax expected search cost is $(n+1)/2$. For two binary procedures under a known independent and identically distributed item law, five counts suffice to compute an optimal search policy. We replay reviews on 2,000 MMLU questions, 896 numerical reports, and 48 Singapore electricity forecast reports. With reviews available, a targeted audit used 6.9% fewer keys on MMLU and 1.2% fewer on numerical reports than a fixed order selected on development data. Compared with selection by stand-alone accuracy, the chosen procedures gained 2.94 percentage points on held-out MMLU questions and zero on numerical reports. On electricity reports, five checks certified a tie across all 48, yet each procedure was correct only eight times.

---


### 12. [FACET: A Data-Efficient Regional Parametric Head Model](https://arxiv.org/abs/2611.26773)

**<font color=#1a73e8>作者：</font>** Mathieu Lamarre, Elly Akhoundi, Thibault Goyallon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Production face pipelines need parametric head models that are expressive, FACS-controllable, and buildable on a small, fixed pool of identities. More training identities would always help, but high-quality registered head scans are expensive to capture; when scaling the data is not an option, the remaining lever is architecture. We present FACET, a parametric head model that makes the most of a fixed identity pool through architectural locality rather than more scans, and makes three contributions, each isolated against a matched global-PCA ablation on our own topology, training set, and normalization. (1) A regional identity decomposition into 16 anatomical regions bypasses the N-1 rank ceiling of a global PCA, driving held-out neutral-fit error from a 1.95 mm floor down to 0.23 mm on the same training identities. (2) A learned FACS action-unit expression model with per-identity neural personalization not only stays FACS-controllable but beats a properly-regularized global expression PCA at every component count -- refuting the argument that FACS is too overcomplete to fit. (3) A dedicated neck/shoulder region reduces pose leakage into the pose-invariant upper face during unposing. Together, these show that architectural locality is the effective lever for a production head model under a fixed identity budget.

---


### 13. [Tracktail: Multi-View 3D Point Tracking without Depth Input](https://arxiv.org/abs/2611.26779)

**<font color=#1a73e8>作者：</font>** Katie L Rupp, Jonathan Wong, Sharmishtaa Seshamani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Tracktail, a novel architecture designed to efficiently track query points in 3D from multiple calibrated views without any depth input. Our architecture separates the task as a per-camera video encoding of features and a per-query decoder. Notably, camera cross-attention is only performed across queries in the decoder, allowing for efficient inference (7 FPS and less than 4 GB memory for 10 views and 100 query points). We further introduce a per-camera scene scale computed from camera geometry, which allows us to normalize inputs and predictions appropriately across a vast variety of dataset scales. We train on a synthetic Multi-View Kubric dataset as well as a novel Multi-View Point Odyssey benchmark dataset, which consists of synthetic renders of humans and animals across 499 frames. Tracktail achieves state-of-the-art results on the Panoptic Studio, DexYCB, and Multi-View Kubric benchmarks, outperforming methods that rely on estimated depth. Tracktail also demonstrates a strong ability to maintain accurate tracking over longer ranges compared to existing methods. Our code, data, and weights are publicly available: this https URL

---


### 14. [CADENCE:Temporally Coherent Whole-Body Human Mesh Recovery that Preserves Expressive Hand Motion](https://arxiv.org/abs/2611.26783)

**<font color=#1a73e8>作者：</font>** Keniel Peart, Jagmohan Chauhan, Indu P. Bodala 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Whole-body SMPL-X estimators recover body, hand, and face meshes from single images, but applied frame by frame to video they produce jittery motion. Smoothing the output removes the jitter at a cost that body-only benchmarks do not measure: a temporal filter strong enough to steady the torso also flattens the fast finger strokes that carry meaning in sign language and gesture. We present CADENCE, a whole-body SMPL-X system for monocular video designed around this trade-off. A per-frame estimator built on a shared C-RADIOv4 encoder, with a high-resolution hand pathway that reuses the same encoder on hand crops, produces each frame's estimate. An offline temporal refiner then filters the SMPL-X rotation sequence: attention along the kinematic tree selects, for every joint and every frame, a mixture of learned zero-phase filters, so the torso is smoothed while fast finger strokes pass through. On 3DPW, the refiner reduces acceleration error from 17.4 to 5.4 mm/s2 while lowering PA-MPJPE from 41.9 to 40.2 mm; generic smoothers applied to the same predictions reach 6.2 to 7.7 mm/s2. On SignAvatars/How2Sign sign-language sequences, the refiner has the lowest hand jitter among the compared smoothers while keeping a hand-speed peak amplitude of 0.98, against 0.35 for a SmoothNet retrained on the full SMPL-X vector. The per-frame estimator also obtains the lowest full-body mesh error (25.7 mm) and hand joint error (8.3 mm) among the compared methods on EHF.

---


### 15. [Memorization and Generalization in Generative Models: A Perspective From Energy-based Modeling and Associative Memory](https://arxiv.org/abs/2611.26797)

**<font color=#1a73e8>作者：</font>** Bao Pham  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative models now write working code, produce realistic images, and hold long conversations, yet the mechanisms behind their intelligence still evade our understanding. This thesis explores that puzzle through Associative Memory (AM), in which patterns are stored as energy minima and retrieved through attractor dynamics. Beyond their capacity, AMs form new minima known as spurious states, long regarded as a failure of memory. We argue that this failure is where creativity begins, and that memorization and generalization can coexist as outcomes of one retrieval process. First, we show that diffusion models behave as AMs. With little data, a diffusion model forms a distinct basin of attraction around each training sample. As the data grows, these basins shrink, and spurious states emerge as attractors that blend stored samples yet match none of them. They are the first signs of generative capability. We characterize this transition by measuring the volume, energy, and curvature of these basins across datasets and architectures, including Stable Diffusion. We then turn to language and move beyond the energy-based view of AM. We show that uniform-state discrete diffusion models are AMs capable of retrieving unseen data, with basins of attraction that arise from conditional likelihood maximization alone. As the training set grows, basins around training examples contract while basins around unseen examples expand, until corrupted test sentences are recovered as reliably as training ones. Conditional entropy exposes this coexistence within a single sequence and cheaply diagnoses where a model lies along the transition. Together, these results suggest that AM is a general principle defined by basins of attraction, and that memorization and generalization can coexist within one model. AM thus offers a framework for asking when a generative model recalls and when it creates.

---


### 16. [Trajectories Through Parsons Problems: Making Student Difficulty Patterns Visible to Instructors](https://arxiv.org/abs/2611.26799)

**<font color=#1a73e8>作者：</font>** Daniel Prol, Juho Leinonen, Arto Hellas 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Existing Parsons problem tools primarily focus on correctness, indicating whether a student solved a problem, but providing limited visibility into the underlying problem-solving process. Without that visibility, instructors cannot see which blocks caused repeated confusion or which distractors were consistently selected. We introduce Pulla, a Parsons problem tool that instruments programming assignments to capture fine-grained interaction data. We examine what these behavioral traces make visible to instructors, namely how long students take on a problem and how many moves they make, which recurring errors the distractors expose and how the class arrives at them, whether those errors follow a student from one problem to the next, and which students complete the whole assignment without a single error.

---


### 17. [LEAN: Library-Based Adaptation for Asynchronous, Federated Fine-Tuning](https://arxiv.org/abs/2611.26805)

**<font color=#1a73e8>作者：</font>** Erdong Hu, Zhimin Ding, Yuxin Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated fine-tuning of foundation models with low-rank adapters (LoRA) is typically reconciled by averaging locally trained adapters. In cross-device settings, where participants hold heterogeneous data and join or leave asynchronously, averaging is poorly suited: locally trained adapters are not identifiable up to permutation, and averages of adapters trained on dissimilar data can be uninformative or unstable. We propose a simple idea called federated library-based adaptation (LEAN), which replaces averaging altogether. The server maintains a library of rank-1 basis pairs; participants check out random subsets, fine-tune them locally as a LoRA adapter, and check them back in, so that each pair is shuffled across sites and trained on many participants' data. Because no aggregation step is required, LEAN operates fully asynchronously and communicates only low-rank parameters. We prove that, in a synchronous setting, LEAN converges to a neighborhood of a stationary point, with the shuffle canceling data heterogeneity at first order. Across image and text fine-tuning benchmarks, LEAN outperforms averaging-based baselines in most settings with substantially less communication, and remains effective under heavy data heterogeneity, where averaging-based methods fail to reach nontrivial accuracy, and under heavy asynchrony, where they degrade substantially.

---


### 18. [NitroGen: Observations on the Action Dynamics, Visual Instruction Following, and Spatial Exploration](https://arxiv.org/abs/2611.26807)

**<font color=#1a73e8>作者：</font>** Shengyuan Lin, Zhiling Li, Haoyu Nie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> NitroGen is an open vision-action foundation model for game control. It is trained by behavior cloning on online gameplay videos. In this paper, we study the frozen controller in Hollow Knight and Trackmania as examples along three dimensions: action adaptation, visual instruction following, and spatial exploration. Our results indicate that NitroGen can adapt its actions to local context, but it lacks the planning, recovery, and exploration needed for longer-horizon game control.

---


### 19. [Realistic Robustness Evaluation of Tabular Data Driven Models](https://arxiv.org/abs/2611.26818)

**<font color=#1a73e8>作者：</font>** Miguel Silva, Eva Maia, João Vitorino 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The increasing adoption of Machine Learning (ML) models in high-stakes applications has raised critical concerns regarding their robustness against adversarial attacks. While extensive research has focused on adversarial example generation in image and text domains, the study of such examples in tabular data remains comparatively limited, despite its widespread use in real-world systems. This work introduces AURORA, a modular, open-source tool for evaluating the robustness of ML models on tabular data classification. It integrates multiple adversarial perturbation methods and evaluation metrics within a unified framework to systematically assess model behavior under adversarial conditions. Central to AURORA is its evaluation report, which focuses on robustness analysis by quantifying performance degradation, comparing the impact of different perturbation strategies, and identifying model vulnerabilities across features and input regions. The report is complemented by visual artifacts that facilitate the interpretability of robustness patterns. Additionally, AURORA incorporates a distance adjustment mechanism that penalizes implausible adversarial samples based on feature-level constraints, ensuring that the robustness assessment remains grounded in realistic perturbations and is therefore more reliable.

---


### 20. [A Unified Framework for Intelligent Cyber Attack Detection and Alert Correlation](https://arxiv.org/abs/2611.26824)

**<font color=#1a73e8>作者：</font>** Miguel Silva, João Vitorino, Daniela Pinto 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A Security Operations Center (SOC) plays a critical role in detecting, correlating, and responding to modern cyber threats. However, SOCs continue to face challenges related to alert overload, fragmented detection capabilities, and limited collaboration between analysts and automated systems. These issues often result in delayed incident response, analyst fatigue, and an increased risk of overlooking sophisticated, multi-stage attacks that unfold gradually across different layers of the network. To address these challenges, this paper proposes a unified framework for network traffic classification and alert correlation through the use of signature rules, machine learning, and sequential pattern mining algorithms. The solution was evaluated in a controlled testbed environment emulating realistic, multi-stage attack scenarios, including malware exploitation, lateral movement, reconnaissance, and data exfiltration. The obtained results demonstrate the effectiveness of the proposed framework in detecting and correlating complex attack behaviors, while providing analysts with actionable insights in line with a human-in-the-loop approach to SOC operations.

---


### 21. [Graph-XGB: A Hybrid GNN Framework for Outdoor-to-Indoor 5G Signal Reconstruction via Aerial-Only UAV RF Sensing](https://arxiv.org/abs/2611.26828)

**<font color=#1a73e8>作者：</font>** David Hason Rudd, Eunkwang Shin, Nithiwat Pattrapong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Delivering robust In-Building Coverage (IBC) is critically impeded by severe Outdoor-to-Indoor (O2I) attenuation, a constraint that intensifies as deployments move from 5G mid-band towards mmWave and prospective 6G sub-THz carriers, where losses of 60-80 dB have been reported across modern building envelopes. While Unmanned Aerial Vehicles (UAVs) offer scalable exterior RF sensing platforms, a fundamental inversion problem persists: interior 3D signal states cannot be directly sampled from constrained exterior flight paths. This paper proposes Graph-XGB, a hybrid inference framework that decouples spatial topology reasoning from non-linear signal regression to resolve this challenge. A modified SpiderGNN encoder, operating on a topology-aware graph constructed with a physically grounded Floor-Aware 3D Distance metric and Bridge Edge Guarantees, propagates UAV boundary measurements into 128-dimensional indoor embeddings. Principal Component Analysis (PCA) compresses these into a 10-dimensional manifold retaining 96.6% of embedding variance, fused with raw spatial features and decoded by independent, physics-tailored XGBoost regressors. This decoupling mitigates the optimization conflict between smoothly decaying path-loss signals and volatile interference-dependent metrics. Evaluated on a real-world 5G NR dataset of 613 verified nodes spanning the 10 floors of a single building, Graph-XGB attains the strongest accuracy among the architectures compared, with $R^2$ of 0.759 (RSSI) and 0.770 (RSRP), improvements of 35.5% and 64.9% over the SimpleGNN baseline, using no interior RF measurement as a model input; indoor observations enter only as training supervision, with evaluation on held-out internal nodes. Interference-dependent targets (RSRQ, SNR and CQI) remain bounded well below the path-loss metrics, delimiting the reach of purely spatial inference.

---


### 22. [Cross-Linguistic Distinctive-Feature Constraints on Segmental Triphones: Evidence for Contrastive Dispersion](https://arxiv.org/abs/2611.26837)

**<font color=#1a73e8>作者：</font>** Leonardo Araújo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural speech reflects articulatory and perceptual constraints, yet how these pressures shape consecutive segment transitions across languages remains underexplored. We analyze adjacent distinctive-feature distances in token-weighted segmental triphones across 17 Universal Dependencies corpora spanning nine language families, transcribed into IPA and mapped to 24 PanPhon features using Hamming and cosine metrics. Natural sequences exhibit an intermediate-distance mode (8-10 features under Hamming, except Vietnamese; 0.28-0.38 under cosine). Against an unrestricted within-word shuffled baseline, natural words reject the inventory-only null (W = 0, p < 10-4), showing higher expected distance, narrower dispersion, and lower joint triphone entropy in all 17 languages. Under a stricter within-word consonant-vowel template baseline, expected distance and dispersion are no longer separated, whereas joint entropy remains lower in 16 languages (p = 1.07x10-4). Entropy decomposition reveals higher mutual information between incoming and outgoing transitions in all 17 languages and all nine families (W = 0, p < 10-4), demonstrating sequential coupling beyond syllable-template alternation. Word-level mean-SD correlations and directional asymmetries do not replicate cross-linguistically.

---


### 23. [AROMA: Understanding AI Support For Mental Well-being through Role Theory](https://arxiv.org/abs/2611.26843)

**<font color=#1a73e8>作者：</font>** Issac Ting, Ethan Pan, Koustuv Saha 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI supporters for mental well-being are becoming more prevalent. When these AI supporters start acting in ways beyond their expected function it leads to relational harm. Standard approaches to evaluating such AI supporters are limited to inspecting their efficacy in narrow task-specific settings, which do not explain these discrepancies in expected and actual behavior. To address this gap, we propose the AROMA (A Role-Oriented Model of Analysis) framework to provide a common role taxonomy for different support contexts. We developed AROMA using a theory-informed annotation of over 7,515 conversations from 13 datasets and propose eight "Role States" based on observed-not prescribed-behavior. We show these Role States vary according to the context of support; depict unique structural and temporal characteristics of AI supporters vis-a-vis Humans; and inform novel AI support prompting strategy for better role alignment. This framework provides a new lens to understand AI support failures.

---


### 24. [A Sparsity Analysis of Traffic Forecasting Architectures: How Much Missing Data is Too Much?](https://arxiv.org/abs/2611.26847)

**<font color=#1a73e8>作者：</font>** Mohamed Hamad, Bilal Mutahir, Mohamed Mabrok 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traffic forecasting models are typically evaluated under ideal conditions with complete data. This evaluation does not reflect the frequent sensor failures and communication outages common in real-world deployments. This paper presents a comprehensive analysis of multivariate traffic prediction models to evaluate their performance under varying levels of sensor data loss during inference. We benchmark several architectural paradigms, including graph neural networks, attention-based Transformers, and selective state-space models, across sparsity levels ranging from zero to complete sensor loss, using two widely used multi-channel traffic benchmarks. To ensure consistent comparison across traffic variables, we use normalized metrics and define a usability threshold to identify when predictions become unreliable. Our results show a clear trade-off between baseline accuracy and robustness: models with the highest accuracy under full-data conditions often degrade most sharply as data becomes sparse, while less accurate models maintain more stable performance. These findings show that model selection should be based on the expected reliability of the sensor network rather than peak accuracy alone. This work provides a practical framework for assessing traffic forecasting models and highlights the importance of robustness in real-world applications.

---


### 25. [Scoliosis5K: Multimodal Gait Analysis via Clip-Conditioned RGB-Silhouette Fusion](https://arxiv.org/abs/2611.26849)

**<font color=#1a73e8>作者：</font>** Zizhao Peng, Zihan Wang, Zheng Lv 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Color walking video records body boundary motion alongside clothing folds, surface appearance, and recording-environment cues. To examine what an explicit binary silhouette contributes to participant-level classification of scoliosis-related gait when a classifier already observes the paired color sequence, we construct Scoliosis5K, a multi-site collection of 4,998 corridor-walking sequences across 3,010 participant identifiers in which RGB person crops, binary silhouettes, and two-dimensional poses share each recording identifier and frame index. Our architecture uses each patch's pixel deviation from its clip mean to weight two low-rank query and value updates inside a pretrained RGB encoder, fusing the resulting video representation with a silhouette transformer sequence and regional kernel ridge scores extracted from one native-resolution RGB frame per window. Across 988 participants in five participant-disjoint cross-validation folds and three training seeds, the complete system reaches 83.77% accuracy and 79.91% macro-averaged F1, compared with 83.27% accuracy and 79.56% macro-F1 when the video RGB encoder remains frozen under identical inputs. Zeroing the silhouette vector at fixed weights shifts overall accuracy by only 0.10 percentage points while raising positive-category recall from 68.52% to 77.78% and lowering recall for both remaining categories. Macro-averaged AUROC is 0.950 across the cohort and 0.879 among participant pairs matched on acquisition site and recording-count group.

---


### 26. [Self-Supervised Learning with Recursive Quadrature Filters for Neural Time Series](https://arxiv.org/abs/2611.26856)

**<font color=#1a73e8>作者：</font>** Mirko Morello, Shivang Rawat, David J. Heeger  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop self-supervised methods for training Recursive Quadrature Filter (RQF) encoders on unlabeled time series. RQFs are biologically motivated, complex-valued temporal filters that form a special class of diagonal state-space models (SSMs). Each RQF acts as a band-pass filter whose selectivity is determined by two learnable parameters: its tuning frequency and bandwidth. We separately introduce a self-supervised learning objective based on prediction error; the encoder is trained so that its current state predicts its own future activity. In the windowed mode, the summary of the current window predicts the summary of a later window; in the dense mode, the state at the current timestep predicts future log-power. Each RQF encoder is pretrained on a dataset and then a readout (e.g., a task-specific classifier) is trained on the output of the RQF encoder, with the encoder either frozen or fully fine-tuned. For multichannel EEG and intracranial recordings, a shared encoder processes each channel separately, and a spatial readout combines the channel representations using electrode locations. Across four neural benchmarks using scalp or intracranial EEG, the pretrained RQF system performs close to the state of the art while using a small fraction of the parameters of the competing models. For example, a 110k-parameter RQF system achieves 0.9247 +/- 0.0022 test AUROC on 100-s TUAB segments, above SAMBA (0.9054) at the same context with 9 times as many parameters, and 0.9040 +/- 0.0019 on 10-s segments, comparable to EEG foundation models with 3.2M-369M parameters.

---


### 27. [FlowScope: 3D Scene Flow Pretraining Improves Surgical Robot Policies](https://arxiv.org/abs/2611.26865)

**<font color=#1a73e8>作者：</font>** John J. Han, Adam Schmidt, Jingpei Lu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Imitation learning for surgical robots is limited by the cost of collecting demonstrations. Meanwhile, many robot-assisted procedures are recorded as stereo video, yet policies cannot learn from them directly; clinical video carries no action labels. We present FlowScope, which pretrains a surgical policy network on unlabeled clinical video by forecasting scene flow, the metric 3D motion of scene points, with labels computed by off-the-shelf stereo depth and optical flow models. We pretrain the trunk of an Action Chunking Transformer (ACT) on a dataset of 1,149 clinical procedures (1.35M clips) and discard the flow head afterward, so the deployed policy is a standard ACT with no added inference cost. On a real surgical robotic system, FlowScope raises needle pickup success from 54% to 90% and first-handover success on needle regrasp from 4% to 52% (full task: 2% to 14%) over training from scratch (n=50 trials each), and retains its gains with a generative flow-matching action head. Ablations indicate that metric 3D motion is the strongest pretraining signal among those tested; kinematics, 2D tracks, depth alone, and scale-free 3D flow, each paired with kinematics, yield smaller or no gains. Representation analyses suggest that scene-flow pretraining encodes metric needle depth more accurately, that kinematics pretraining increases reliance on the robot state, and that needle-depth probes follow the ordering of real-robot success where offline validation error does not.

---


### 28. [SonoAtlasWorld: Anatomy-Grounded Ultrasound World Models for Wide-Range Scanning](https://arxiv.org/abs/2611.26867)

**<font color=#1a73e8>作者：</font>** Zheyuan Zhang, Boris Mailhe, Hang Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning robotic ultrasound policies requires interactive environments for scalable data generation and repeatable evaluation, while exploration on real patients is limited by acquisition costs and safety constraints. Generative world models offer an alternative, but image history and probe actions alone do not ensure anatomical consistency across wide-range scans and changing acoustic windows. We introduce SonoAtlasWorld, an ultrasound world model built on anatomy as state. A persistent 3D anatomical asset extracted from computed tomography (CT) anchors each scan to a specific anatomy. Probe actions determine anatomical and acoustic visibility conditions for a causal ultrasound generator trained on clinical videos. Our three-stage pipeline combines anatomy-conditioned pretraining, causal conversion and long-rollout alignment. Inference optimizations achieve pose-to-ultrasound throughput of 81.2 FPS. To evaluate anatomical control beyond image similarity, we introduce the Action-Following Index (AFI), which measures normalized reconstruction gain over a static-prefix baseline. On 40 held-out 3D volumes, SonoAtlasWorld achieves liver and macro-organ AFI of 0.428 and 0.262, compared with at most 0.117 and 0.038 for the tested action- and geometry-conditioned methods. Long-rollout alignment reduces brightness drift by 3.46x at the end of 40 repeated scan cycles. SonoAtlasWorld also generates offline policy-training demonstrations and supports anatomically grounded closed-loop evaluation. Scaling the generated training data improves key-plane acquisition success from 48.2% to 81.2% on unseen anatomies in simulation, demonstrating its utility for robotic ultrasound policy learning.

---


### 29. [Effectiveness of Synthetic Defects for Anomaly Detection in Industrial Small Load Carriers](https://arxiv.org/abs/2611.26868)

**<font color=#1a73e8>作者：</font>** Vincent Wahyudi, Kuniko Paxton, Amila Akagić 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent industrial anomaly detection methods use procedural noise to generate synthetic training defects. Their effectiveness in real-world settings and the impact of different noise generation methods have not been sufficiently investigated. We evaluate the effectiveness of training using synthetic defects for both supervised and unsupervised methods, the impact of different noise generation methods, and the differences in detection performance between benchmark datasets and a real-world small load carrier (SLC) dataset. Trained on synthetic defects only, a supervised classifier reaches 0.65 AUROC on real SLC defects, while three unsupervised methods using the same kind of noise (Perlin) reach 0.87--0.90. Except for SuperSimpleNet, which fails with the foreground-confined fractal Brownian motion (fBm) recipe, models trained with the custom recipe or with nine other noise types do not differ reliably from those trained with Perlin noise. Finally, results with synthetic defects on benchmark datasets do not carry over to the SLC dataset, possibly because the synthetic defects differ too much from the real ones (a larger angle in feature space). These results call for caution when training models on synthetic defect images.

---


### 30. [Towards Robust Partial-Edit Deepfake Localization: An edit and Generator Conditioned Analysis](https://arxiv.org/abs/2611.26903)

**<font color=#1a73e8>作者：</font>** Aishwarya Fursule, Vamshi Nallaguntla, Yuan Tseng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Partial-edit deepfake localization aims to identify manipulated regions within otherwise authentic speech. Recent systems report strong overall results, but aggregate scores do not reveal whether this performance holds across different editing conditions. In this work, we present an edit- and generator-conditioned analysis of Segment-Aware Localization (SAL) using WavLM-Large and XLS-R representations on the VoiceCraft and SSR-Speech subsets of PartialEdit. We categorize edits along three transcript-derived axes, namely content, meaning change, and editing operation, and evaluate each generator separately. While both representations achieve strong overall performance, localization is noticeably weaker on SSR-Speech. From our experiments, we found that the deletion is the hardest operation, and deletions produced by SSR-Speech are the most challenging condition for both representations. In contrast, edit content, meaning change, and sentence novelty have smaller effects. These findings show that a single aggregate score can mask important weaknesses, and that partial-edit localization should be evaluated separately across generators and edit types.

---


### 31. [Large Reported CHB-MIT Adaptation Gains Disappear with Pretrained Encoders and Matched Probes](https://arxiv.org/abs/2611.26929)

**<font color=#1a73e8>作者：</font>** Joseph Sankoorikal Johny, Antony J. Sankoorikal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dani and Liebe (2026) (DL) report that adapting the final encoder block of BIOT and CBraMod with self-supervised learning (SSL) improves CHB-MIT seizure-detection ROC-AUC by 36.2 and 29.5 points over linear probing. We investigate these results with their released code and an independent pipeline. The release loads pretrained weights for adaptation only when an otherwise unset configuration key is supplied, and its CBraMod probe reads the reconstruction head with dropout active. With pretrained initialisation and a probe on the encoder output in evaluation mode, the fixed-recipe adaptation gain on DL's split is -0.6 points for BIOT (95% interval [-3.8, +2.6]) and +0.01 for CBraMod ([-0.02, +0.04]) across five seeds. Across DL's split and five subject rotations on CHB-MIT and Siena Scalp EEG, with equally tuned linear probes (30 configurations, up to 500 epochs, validation-based early stopping), mean adaptation effects range from -1.1 to +5.7 ROC-AUC points over 18 comparisons (related settings and feature variants). Twelve of 18 support equivalence within +/-3 points under dependence-adjusted inference (8 of 12 rotation and 4 of 6 fixed-split comparisons); six are unresolved. After correcting rotation intervals for dependence, no positive effect has a 95% interval excluding zero. The +/-3 margin is an analysis threshold, not a clinically validated one, and smaller margins support fewer equivalences. Two fixed-probe gains near +21 points shrink under the same tuning, with smaller benefits unresolved. We also audit a CHB-MIT protocol shared by at least 14 papers. No tested configuration reproduces DL Table 1 as a whole. These findings concern the tested configurations; the encoder-level probe and subsequent checks were chosen post hoc.

---


### 32. [CENTRY: A Probabilistic Latent-State Model for Continual AI Risk Estimation, Monitoring, and Regulation](https://arxiv.org/abs/2611.26940)

**<font color=#1a73e8>作者：</font>** Bonny Banerjee, Geetha Raju  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Artificial Intelligence (AI) systems are increasingly deployed in safety-critical applications, yet existing AI safety frameworks primarily define, categorize, or govern AI risk rather than proposing implementable models and methods for continually estimating, monitoring, and regulating risk throughout an AI system's operational lifetime. This paper proposes CENTRY, a probabilistic framework that enables continual risk estimation, monitoring, and regulation of a deployed AI system from its interactions with its environment. The framework models AI risk as arising from three intrinsic sources: datasets, hardware resources, and models/algorithms. A structured latent-variable model is developed in which the latent representation is decomposed into a fast interaction subspace that captures the evolving AI--environment dynamics and three slow latent subspaces that encode the long-term risk states associated with the dataset, hardware, and model components. Rather than requiring a ground-truth risk label at every time step, the component-risk states are treated as latent variables and are learned by maximizing a variational evidence lower bound, optionally informed during training and continual refinement by evidence-supported behavior--cause records. The resulting framework unifies continual probabilistic inference, online risk estimation, and adaptive risk regulation in an implementable architecture. Under the explicit assumptions stated for the corresponding results, we establish formal guarantees spanning safety, learning, inference, and operations, including finite-horizon and asymptotic risk-budget compliance, regret and convergence bounds for adaptive regulation, consistency and identifiability of component-risk ratings, and detection-delay, false-alarm, containment, and computational-complexity characterizations.

---


### 33. [CodeReviewBench: An Automated Benchmark for Evaluating the Software Factory](https://arxiv.org/abs/2611.26942)

**<font color=#1a73e8>作者：</font>** Ashley Zhang, Narmeen Fatimah Oozeer, Aleksandr Zverianskii 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI agents ship more code with minimal human oversight, code review becomes the critical quality-control checkpoint -- but one without a reliable, objective verifier: review quality is nuanced and ultimately a judgment call by the PR author. Existing benchmarks are structurally misaligned with this: annotators are third-party reviewers, like the bots they evaluate, not the PR authors who actually decide what to fix. They also rely on small, static issue sets that require full re-evaluation as tools update, limiting how frequently progress can be tracked. We introduce CodeReviewBench, built on a fundamentally different signal: revealed developer preferences -- if a developer acts on a bot's suggestion, we treat it as useful; if they ignore it, we do not. This signal is mined daily from the public GitHub event stream, yielding 500K+ judged PRs across 18 tools, and refreshes continuously as tools evolve. We validate the developer preference against an independent offline benchmark: the two agree on precision rankings and independently detect the same product updates within days of vendor releases. Together, these form the benchmark.

---


### 34. [Causal Diffusion for Extreme Super-Resolution in Interactive Games](https://arxiv.org/abs/2611.26963)

**<font color=#1a73e8>作者：</font>** Christina Zhang, Jenna Kang, Colin Groth 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing game super-resolution methods typically operate at moderate upscaling factors, struggling to recover fine visual details from extremely low-resolution inputs (e.g., 120p). At such resolutions, super-resolution shifts from reconstructing existing information toward synthesizing missing visual details. While video diffusion models offer powerful generative priors for this challenging task, their dependence on future frames limits their applicability to interactive games. We present CIDER, a causal diffusion framework for extreme game super-resolution that synthesizes high-frequency details from current and past low-resolution frames, guided by G-buffers (depth and motion vectors) to preserve scene structure and temporal consistency. We collect data from two AAA games (Cyberpunk 2077 and Black Myth: Wukong). To reduce inference load, we develop a lightweight latent projection encoder tailored to ultra-low-resolution inputs, fine-tune a decoder (TAE) on our high-resolution outputs, and distill the diffusion model to reach interactive frame rates. Our experiments demonstrate high-fidelity 8$\times$ upscaling from 120p to 960p at around 13 FPS, outperforming state-of-the-art game upscalers in visual quality and showing potential for 16$\times$ magnification.

---


### 35. [Affine-Image Propagation for Tight and Scalable Neural Network Verification](https://arxiv.org/abs/2611.26978)

**<font color=#1a73e8>作者：</font>** Hong-Ming Chiu, Haoyu Li, Huan Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While bound propagation methods are highly effective for certifying neural networks against $\ell_{\infty}$ adversaries, tight and scalable verification for $\ell_{2}$ adversaries remains a significant open challenge. Existing methods incur geometric loss by enclosing preactivation sets in elementwise intervals or axis-aligned ellipsoids, and functional loss by restricting the linear bounds constructed over those domains. Consequently, tight $\ell_{2}$ verification is currently restricted to Lipschitz-regularized networks where these approximations are accurate. In this paper, we introduce affine-image SDP-CROWN, a novel bound propagation method that better approximates preactivation domains using affine-image constraints and jointly optimizes the linear bound to adapt to the resulting domain. To bypass the prohibitive computational cost of dense semidefinite constraints required by the affine-image representation, we replace them with scaled diagonal-dominance conditions, allowing a GPU-accelerated implementation. Our method preserves the bound propagation recursion and can be integrated with branch-and-bound. On five MNIST and CIFAR-10 non-Lipschitz-regularized networks, our method improves verified accuracy over state-of-the-art methods by 17% to 57.5%. With branch-and-bound, these improvements increase to between 27% and 63.5%.

---


### 36. [ViewDreamer: A Robot World Model beyond Fixed Camera Setups](https://arxiv.org/abs/2611.26981)

**<font color=#1a73e8>作者：</font>** Ye Mao, Jinhui Xiong, Egor Larionov 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation models are increasingly important for robot learning, yet most generate each camera view separately or tile all views in a fixed layout. Robot demonstrations, however, are captured by synchronized cameras whose number, placement, and order vary across embodiments. We present ViewDreamer, a single world model that handles variable sets of cameras by disentangling per-view generation from cross-view interaction. Each view follows the generation path of a pretrained single-view model, and views interact only through shared slot tokens. We stabilize multi-view training with a curriculum that gradually increases the number of views. Cross-View Slot Agreement uses visual foundation models to group geometrically and semantically similar regions across views into shared slots. On RoboView-Bench, which covers one to four cameras, ViewDreamer achieves the best generation quality among the models evaluated and improves cross-view consistency over independent per-view generation. These gains carry over to our world-action model (WAM) and action-conditioned world model (AC-WM). Our WAM outperforms the FastWAM-Joint baseline on LIBERO-Plus, RoboTwin 2.0, and RoboDojo, and on a real Franka robot. Both variants improve out-of-domain generalization to various camera settings and scenes.

---


### 37. [Privacy Protection in Self-Evolving Personal Agents: Persistent Memory and Cross-Carrier Transfer](https://arxiv.org/abs/2611.26983)

**<font color=#1a73e8>作者：</font>** Zibin Lin, Taotao Wang, Shengli Zhang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Personal agents carry private experience into later decisions through persistent memory. This thematic survey compares memory admission, maintenance, release, and withdrawal by protected change, observer, and validation setting. Direct evidence in the screened corpus comes from controlled memory workflows. Three worked scenarios follow one private fact through booking, feedback-driven learning, and withdrawal. We show when prompt revision and memory reads compose, when skills inherit a private head's bound, and why reader non-use does not establish cleanup of learned state. Diagnostic experiments measure the utility costs of wider label protection and broad memory deletion, and test how missing lineage obscures descendants.

---


### 38. [Comparing Visual Motion Patterns for Pedestrian Guidance with Multi-Display Signage: Two Field Studies](https://arxiv.org/abs/2611.26984)

**<font color=#1a73e8>作者：</font>** Yuri Mikawa, Taiki Fukiage, Yuki Kubota 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Public multi-display signage (MDS) has the potential to provide subtle pedestrian guidance through visual motion while retaining its conventional role in advertising and information delivery. However, it remains unclear how different visual motion patterns relate to pedestrian spatial distributions and how these relationships vary across deployment settings. We conducted two exploratory field studies in a museum, involving 18,402 pedestrian passages over 25 experimental days, to examine lateral positions in relation to stripe-motion contrast and coverage patterns. In Test Case 1 (TC1), involving predominantly one-way pedestrian flow, partial stripe presentation was associated with more leftward lateral positions than wider-coverage patterns in some comparisons, and lower contrast in full-screen stripes was not associated with a detectable reduction in the observed lateral bias. In Test Case 2 (TC2), conducted in a different spatial configuration permitting bidirectional walking, lateral positions differed by stripe-motion direction during one-way flow, but coverage effects on lateral position and stripe-advertisement differences in lateral position or passing-side choice were not significant. In both test cases, partial stripes received lower self-reported sickness ratings than full-screen stripes. These findings suggest that lower-contrast and reduced-motion-coverage designs hold practical potential for pedestrian guidance, with spatially restricted cues potentially allowing such guidance to coexist with existing advertising while reducing discomfort. At the same time, the contrasting patterns in TC1 and TC2 suggest that spatial context may shape how pedestrians respond to stripe coverage, highlighting the context-dependent suitability of visual-motion-based guidance and the need for further investigation.

---


### 39. [Distributional Algebro-Geometric Persistence (dAGP): Wasserstein-Stable Polynomial-Relation Signatures](https://arxiv.org/abs/2611.26986)

**<font color=#1a73e8>作者：</font>** Edisy Kin Wai Chan, Andersen Ang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A circle and a quartic superellipse have the same homology, but their defining equations have degrees two and four, respectively. We study this algebraic distinction for point-cloud distributions. For a probability measure $\mu$ on $\Omega=[-1,1]^d$ and an orthonormal polynomial feature map $\phi_m$ of degree $m$, the moment matrix $G_m(\mu)=\mathbb{E}_{X\sim\mu}[\phi_m(X)\phi_m(X)^\top]$ satisfies $c^\top G_m(\mu)c=\mathbb{E}_\mu[f_c(X)^2]$, so coefficient directions associated with its small eigenvalues represent low-degree polynomials that nearly vanish on $\mu$. Counting these near-relation directions across degree $m$ and the tolerance $\varepsilon$ gives a two-parameter integer signature. We call this representation distributional algebro-geometric persistence (dAGP), the population counterpart of the point-cloud algebro-geometric persistence (AGP) construction. For empirical measures, dAGP is the sample-normalised counterpart of point-cloud AGP. We also show that $\mu\mapsto G_m(\mu)$ is Lipschitz in the $1$-Wasserstein distance, so its ordered eigenvalues vary Lipschitz-continuously under transport of mass, while its threshold counts remain unchanged under perturbations satisfying a spectral-margin condition. We give an explicit support-localised Lipschitz constant and identify the regime in which the resulting guarantee is informative. Experimentally, the population noise-floor prediction agrees with the finite-sample mean to $0.1\%$, within sampling error. At a selected tolerance, relation onset orders the conic, quartic, and non-algebraic closed curves, while their count profiles distinguish them from the two-dimensional control. Calibration identifies an empirical tolerance range. A $100$-repetition sensitivity study quantifies onset recovery and shows that the count grid and two continuous spectral baselines nearly saturate the four-family discrimination task.

---


### 40. [JevRisk: Zero-Shot Financial Risk Assessment with a Language Decision Model](https://arxiv.org/abs/2611.26999)

**<font color=#1a73e8>作者：</font>** Yaodong Yang, Li Huang, Junpeng Liang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Banks must monitor every customer's financial risk, such as money laundering and credit default, by interpreting financial activity in the context of the customer's profile. Existing risk monitoring systems of banks are mostly based on expert-designed risk indicators, which apply predefined thresholds to every customer and cannot adapt to their personal situations. Supervised models recognise risk patterns from labelled customers, but each label often needs an expert's review or months of repayment history, which is slow and costly. Financial risk assessment therefore calls for a zero-shot decision system that minimises the need for labels and generalises across customers and risk types. To this end, we present JevRisk, a system for zero-shot financial risk assessment with a language decision model. JevRisk works in two steps. First, following regulatory guidelines in the finance domain, JevRisk computes exact risk indicators with code. Second, the language decision model (e.g., \jev{}) reads these indicators together with the customer's profile and activity, judges the case in context with broad world knowledge, and returns the score of high risk. We evaluate JevRisk on the anti-money laundering task with public synthetic data from Scotiabank and on the credit risk task with real data from Home Credit and Lending Club. On both tasks, JevRisk outperforms rule-based and unsupervised methods, and is on par with or better than supervised methods (e.g., GBDT and TabPFN) trained on about a thousand labelled customers.

---


### 41. [S2D-Splat: Static-First Gaussian Reconstruction of Dynamic Driving Scenes with Layer-Wise Feature Guidance](https://arxiv.org/abs/2611.27003)

**<font color=#1a73e8>作者：</font>** Jinheng Li, Tianchen Deng, Bufan Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Moving objects introduce cross-frame inconsistencies that complicate camera estimation and static geometry recovery in driving scenes. Recent feed-forward Gaussian methods explicitly separate static and dynamic primitives, but often estimate camera parameters and geometry from shared features that jointly encode both components, leaving static reconstruction susceptible to dynamic interference. To address this challenge, we propose S2D-Splat, a feed-forward framework for static-first Gaussian reconstruction with layer-wise feature guidance. Our framework separates static and dynamic features before camera and geometry estimation, enabling the static branch to recover camera parameters and static 3D Gaussians with reduced dynamic interference. Intermediate static features are cached at each layer and reused as fixed conditioning at corresponding layers of the dynamic branch. This asymmetric information flow preserves the established static representations while providing stable geometric context for reconstructing dynamic 3D Gaussians. An instance-level motion decoder further queries the fused static and dynamic representations to estimate object trajectories, supporting motion-aligned Gaussian fusion and temporal interpolation. Experiments on Waymo and zero-shot evaluations on nuScenes and the MM-AU accident dataset demonstrate that S2D-Splat outperforms existing approaches on most evaluated metrics and generalizes to highly dynamic, pre-collision driving scenarios.

---


### 42. [Fair Property Tax: Reducing Regressivity in Machine-Learning Valuation](https://arxiv.org/abs/2611.27009)

**<font color=#1a73e8>作者：</font>** Nicolas Acevedo Villena, Haihao Lu, Michael Wagner 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Advanced machine-learning models are increasingly used for property valuation in tax assessment. Although these models can achieve high predictive accuracy, they may systematically assign higher valuation-to-sale ratios to lower-priced properties, a pattern known as regressivity. In collaboration with the Cook County Assessor's Office (CCAO), we develop and evaluate two training methods that substantially reduce this regressive pattern while maintaining price-scale predictive accuracy. The Direct method has been incorporated into CCAO's public residential valuation software. Retaining the LightGBM model class used at CCAO, we propose a Direct penalty on squared covariance between log valuation errors and log sale prices, and an observation-additive Surrogate that yields a weighted squared-error loss. We evaluate both methods in our implementation of the CCAO workflow, using seven chronological validation folds, a held-out test set, and a 2025-forward test set. Measured by the magnitude of price-related bias (PRB), regressivity falls by approximately 49% on held-out sales and 39% on 2025 sales at a Surrogate setting selected by cross-validation, relative to the same LightGBM model fitted without the penalty. Price-scale $R^2$ is essentially unchanged. Its small rise, from 0.893 to 0.897 on held-out sales and from 0.904 to 0.908 on 2025 sales, reflects overall valuation level. Log-price RMSE rises by 3.1% and 1.7%, respectively. Paired sale-bootstrap 90% intervals for the PRB reductions lie within about two percentage points of these estimates. In an additional eight-county benchmark, both methods reduce regressivity in every county, with higher log-price prediction error as the expected tradeoff. These findings demonstrate a practical way to reduce measured regressivity within an existing assessor workflow while preserving price-scale predictive performance.

---


### 43. [Many Plans at Once: Diverse Top-Quality Planning in Continuous Time](https://arxiv.org/abs/2611.27012)

**<font color=#1a73e8>作者：</font>** Mahyar Jahani-nasab, Hamid Rezatofighi, Mor Vered 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Planners for physical systems usually return a single trajectory, which leaves no alternative when an unmodeled constraint invalidates the chosen route or downstream preferences change. A set of plans computed in advance provides ready-made alternatives and warm-starts for fast adaptation, but only if the plans are both low-cost and mutually distinct. Discrete planning addresses this with top-quality and diverse planning, but these ideas do not transfer to continuous time, where every valid trajectory has infinitely many valid near-copies, and existing trajectory planners converge to one or a few solutions. We present Many Plans at Once (MPAO), which treats every plan it finds as a reason to search elsewhere: it samples untrained neural networks whose outputs meet the boundary conditions by construction, trains corrections shared by networks from the same distribution, stores every validated plan, and adapts its sampling to what it has found, which makes it anytime. We define the goal by bringing the cost bound of top-quality planning and the distinctness threshold of diverse planning to continuous time. Under equal budgets against five baselines, MPAO is the only method that solves all 40 instances across four domains. On contact-rich manipulation, it is the only method with plans within 25% of the best known cost on one task, and returns about ten times as many such plans as the strongest baseline on the other two.

---


### 44. [Ruby: State-of-the-Art Potency Prediction across Discovery Regimes Using Learned Structural Representations](https://arxiv.org/abs/2611.27015)

**<font color=#1a73e8>作者：</font>** Michael Atkin, Dominique Beaini, Jules Berman 等 37 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Small-molecule drug discovery proceeds through repeated design-make-test-analyze cycles. The goal is often to maximize potency while keeping other properties within the ranges required for a viable therapeutic candidate. Compound prioritization places different demands on computational methods as drug discovery progresses from hit identification through hit-to-lead and lead optimization, with changing computational budgets and increasing amounts of on-target experimental data. We introduce Ruby, a Robust Universal Binding affinitY predictor that uses intermediate representations from the structural foundation model Pearl without requiring an explicit binding pose for every compound. Ruby is trained on proprietary data plus GenesisPotency-2026, an audited public-source potency training dataset released for academic and commercial use under a CC BY-SA 4.0 license with row-level provenance and audit annotations. Ruby achieves the highest aggregate early enrichment across seven public hit-identification targets among evaluated methods, with adjustable inference effort trading off enrichment and computational cost over more than two orders of magnitude. Ruby achieves the highest average correlations across four public benchmarks: OpenFE, CASP16, FEP+ 4, and OpenBind. Ruby significantly outperforms other methods in zero-shot prediction across eight biochemical and cellular assays from five ongoing Genesis-Incyte programs, widening its performance advantage relative to the public benchmarks. Ruby continues to improve more than other methods when all are given the opportunity to recalibrate using earlier assay measurements. Together, these contributions provide an annotated training resource for the field and a state-of-the-art potency predictor for broad screening, prioritization within related chemical series, and assay-specific prediction as experimental measurements accumulate.

---


### 45. [Same Facts, Different Decision: Fact-Invariant Manipulation and Provenance-Based Defense in Typed Decision Models](https://arxiv.org/abs/2611.27016)

**<font color=#1a73e8>作者：</font>** Yujie Wang, Haotian Chi, Shunrong Jiang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Typed decision models such as TypeSafe's Jev answer only with a probability, an option, or a score, so software can act on them directly. Their inputs, however, often include text from outsiders. Prior attacks test this risk poorly. Injected instructions rarely work on these models, and added facts can make a changed decision correct. We show that outside comments can persuade these models to make a wrong decision without adding any fact. We propose LEVER, an attack that writes such comments with four levers from argumentation theory, uses a separate verifier to discard any comment that adds a fact, and searches for effective comments guided by the model's output probabilities. We further propose the Provenance Gate, a defense that accepts a changed decision only if the model reaches it again without the outside comments. On three benchmarks, LEVER flips about a third of Jev's correct decisions, 2.8 times as many as the strongest prior attack under the same limit on facts, and more on five other models. The gate blocks all of these attacks with at most one extra query and still accepts trusted updates.

---


### 46. [Real-Time On-Drone Hyperspectral Anomaly Detection for Wilderness Search and Rescue](https://arxiv.org/abs/2611.27017)

**<font color=#1a73e8>作者：</font>** Jacqueline Liu, Gyabaah Kyere, Chengyan Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Wilderness search-and-rescue (WSAR) teams use uncrewed aerial systems (UASs) to survey terrain for indicators of missing persons that are rare, blend into the background, or lack thermal signatures. Hyperspectral imaging (HSI) provides rich spectral information, but its high data volume challenges real-time on-drone processing. We present SABL, an edge-computing pipeline for on-drone Spectral Anomaly-Based Localization. SABL integrates hyperspectral streaming with exponentially moving Reed-Xiaoli (ERX) anomaly detection and DBSCAN spatial filtering to group pixel-level anomalies into candidate search regions. SABL is evaluated on data collected during a 10-day deployment with Quinhagak Search and Rescue (QSAR) in remote Alaska. It processes hyperspectral scanlines at 5.67-5.73 ms per line, meeting the camera's 10-ms acquisition interval; DBSCAN requires only 6.5-12.5 ms per 100-line update for filtering. SABL achieves approximately 56% and 99% object-level precision on QSAR-selected search indicators across two scenes, with corresponding recall of 55% and 29%, providing significant background filtering while identifying difficult-to-see anomalous search indicators.

---


### 47. [Integral Multipliers and Arithmetic Obstructions for Two-Hidden-Layer ReLU Maxima](https://arxiv.org/abs/2611.27018)

**<font color=#1a73e8>作者：</font>** Pengcheng Cheng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study exact representations of maximum functions by ReLU networks with two hidden layers and integer parameters. The least positive output multiplier is two for the six-input maximum, and either two or six for the seven-input maximum. We obtain these bounds from integral cubical fillings and a coefficient-preserving passage from polytope identities to networks. For the coordinate-facet complex of the six-simplex, we compute a coning index of six over the integers and three after inverting two, allowing arbitrary integral directions within each facet. A class in the homology of the unrestricted kernel complex characterizes the remaining seven-input problem; its vanishing is equivalent to an integral filling of a fixed target. We also construct a finite character that separates rational from three-local representability in a dictionary containing two known constructions and all pairs of edge-disjoint three-edge forests. This obstruction permits nonsymmetric coefficients and is confined to the specified dictionary. Control of lower-dimensional remainders yields a sufficient criterion in the top-dimensional quotient. Exact certificates and verification programs accompany the finite calculations.

---


### 48. [ReactDrive: Self-Reactive Driving World Model](https://arxiv.org/abs/2611.27024)

**<font color=#1a73e8>作者：</font>** Yifan Wang, Xiaoqi Wang, Cho-Ying Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The world evolves through the dynamics of its constituent entities and their interactions, with changes in one entity influencing the behavior of others. To simulate this evolution under different actions, interactive world models need to capture the resulting agent responses as part of the world's own dynamics. In autonomous driving, errors in modeling these responses can misrepresent maneuver safety and undermine the reliability of generated videos used for policy evaluation and learning. To formalize this intrinsic requirement for driving world model, we define self-reactivity as the capability to model agent responses from observed history and a specified ego action, and generate visual futures that reflect those responses without prescribed future agent trajectories. To realize this capability, we introduce ReactDrive, a driving world model that jointly learns agent dynamics and visual generation through a shared agent state representation. Within this framework, dynamics supervision grounds a reactive dynamics prior in observed agent states, while the video objective jointly optimizes the self-reactivity and visual realism. Experiments show improved agent responses, ego controllability, and video quality, a 96.0% preference for agent reactivity in human comparisons across five baselines, and better downstream planning through augmentation with generated videos. We hope this work encourages the community to recognize self-reactivityas a foundational capability for developing and evaluating interactive world models. Project page: this https URL .

---


### 49. [Toward a digital twin of the ICU patient: Forecasting and treatment response in a generative event model](https://arxiv.org/abs/2611.27028)

**<font color=#1a73e8>作者：</font>** Zhuoyang Lyu, Yiming Li, Peter C. Hou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A digital twin of a patient in intensive care would forecast the patient's course and what a treatment would change. Generative event models, trained to continue a patient's electronic health record (EHR), have been proposed as a path toward such twins. We trained TWICE, a 79M-parameter decoder-only transformer, on the ICU records of one academic health system (127,332 training patients and 1.57 billion tokens). We evaluated it on clinical prediction tasks, generation fidelity, individual trajectories and counterfactual validation. Reading 19 clinical outcomes off 50 simulated futures, with no task-specific training, TWICE matched the best of 144 supervised configurations on held-out patients (mean AUROC 0.836 vs. 0.834). It led on events that change care within a day and trailed on death. With the training data fixed, more and longer simulated futures were worth more than a 6.8-fold larger model. Its generated records matched real ones closely and were as specific to each patient as its own variability allowed. Its predicted risk rose as events approached. Pre-specified controls showed that it reproduced the side effects of drugs and was barely moved by an inert drug. On the values that treatments are given to correct, however, an opposite treatment moved its forecasts like the right one. TWICE forecasts ICU events about as well as task-specific models, and we see it as a step toward a digital twin of the ICU patient.

---


### 50. [Mind World Models: Joint Learning of Motor EEG Representations and Action-Conditioned World Dynamics](https://arxiv.org/abs/2611.27029)

**<font color=#1a73e8>作者：</font>** Weikang Qiu, Zheng Huang, Tinglin Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Motor decoding from electroencephalography (EEG) supports non-invasive brain-computer interfaces, yet existing methods either rely on costly cue-based trials and coarse categorical labels or use pretraining objectives that do not directly capture how movement unfolds, limiting their ability to learn transferable motor representations. To this end, we propose the Mind World Model (MWM), a framework that learns motor EEG representations from scalable naturalistic EEG and egocentric video without action annotations. MWM treats EEG observed up to the current frame as the latent action of a world model: a mind model encodes the EEG, and a world model uses it to predict the representation of a future frame, yielding a movement-grounded pretraining objective. We further introduce the Lateralization-Aware Transformer (LAT), which uses frame averaging to separate shared bilateral from side-specific lateral features, encoding hemispheric correspondence to reduce the burden of learning left-right relationships from data. MWM pretraining produces two models: a mind model for downstream motor decoding and a world model that can be adapted to prediction conditioned on real actions, opening a scalable and flexible path to collect egocentric data for embodied AI. Across 9 classification and 7 regression tasks, the mind model improves task-averaged balanced accuracy by 5.9% and Pearson correlation by 16.2% relative to the strongest baseline in each task family. Compared with an inverse-dynamics latent-action baseline, the world model achieves lower prediction error and benefits 3.3 times more from matched real actions within recordings and 4.7 times more on held-out subjects.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-206](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
