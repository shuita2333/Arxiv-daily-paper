# 📦 其他研究 | 2026年10月21日

> 本类共 **534** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-534](./part-11.md)

---

### 1. [Forecasting Patient Trajectories from the Electronic Health Records with Action-Conditioned World Models](https://arxiv.org/abs/2610.23862)

**<font color=#1a73e8>作者：</font>** Simon A. Lee, Jiahang Hank Sha, Soomin Chung 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce a predictive world model for electronic health records (EHR) that represents patient histories as action conditioned latent trajectories. Rather than modeling clinical events solely through autoregressive token prediction, our framework explicitly separates patient states from observed clinical actions and learns their evolution through a state and action conditioned transition operator. At its core is a state dependent linearization predictor that propagates local changes in latent patient state, enabling time resolved prediction, multi step rollout, and action conditioned simulation. Empirically, we show that generated latent trajectories preserve downstream predictive signal, temporal structure, and subgroup level statistical relationships present in encoder derived representations. We further decode free running rollouts into the original clinical feature space and evaluate future clinical measurements against observed values using task matched forecasting baselines, demonstrating that the learned dynamics retain predictive information beyond latent space agreement. Across binary classification and time to event tasks, EHR WM achieves competitive, though task dependent, performance relative to substantially larger EHR foundation models while using a 30x smaller parameter footprint. Finally, perturbing observed action sequences produces corresponding changes in generated trajectories, demonstrating the action sensitivity of the learned dynamics. Together, these results support world modeling as a complementary framework for learning explicit, time indexed representations of patient evolution from longitudinal EHR.

---


### 2. [Latent Multimodal Memory Reasoning](https://arxiv.org/abs/2610.23890)

**<font color=#1a73e8>作者：</font>** Cai Ke, Xinghao Chen, Yuanchen Bei 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-term personalized agents are required to reason over distributed history across modalities and evolving dialogue states. While existing flat cross-modal methods compress visual evidence prematurely and struggle with temporally stale observations, they neglect the necessity to unify multimodal and cross-session evidence. Crucially, raw multimodal memories are inherently entangled and heterogeneous, making fine-grained visual grounding and cross-modal reasoning computationally prohibitive. To this end, we present latent multimodal memory reasoning, i.e., LMMR, a novel neuro-symbolic framework that shifts long-term multimodal memory organization into a continuous latent space. Specifically, (i) instead of converting images to text and relying on static retrieval, LMMR maps both textual hidden states and visual patch features into a shared Sparse Autoencoder concept space, establishing sparse activations as common semantic addresses to dynamically construct a turn-level multimodal memory graph. (ii) A graph encoder then aggregates cross-modal and temporal dependencies across the task-specific latent subgraph, injecting the graph readout as a continuous residual rollout into the generation backbone while retaining native visual tokens to preserve fine-grained details. Extensive experiments on nine Mem-Gallery tasks and twelve MemEye settings demonstrate that LMMR significantly outperforms state-of-the-art baselines in capturing complex multimodal dependencies while enabling faithful and grounded responses.

---


### 3. [Path-Conditioned Attention Mobility: From Depth to Execution Hubs in SegFormer](https://arxiv.org/abs/2610.23893)

**<font color=#1a73e8>作者：</font>** Aleksandr Druzhinin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transformer compression often couples two distinct quantities: retained attention capacity and the number of sequential depths at which that capacity is executed. We study whether useful attention functions in a hierarchical vision transformer are locally mobile across depth. Using SegFormer-B5 for human segmentation, we find that some task-relevant attention heads can be relocated to nearby depths, but only when their computational context is respected. Head-only relocation is insufficient, while joint adaptation of the relocated head and surrounding representation boundary improves functional preservation; replacing donor-specific normalization and spatial-reduction preprocessing causes large degradation. We use this path-conditioned mobility to reorganize retained attention from depth into width. Starting from a fixed parent with 120 retained Stage-3 heads across 40 attention execution depths, we consolidate the same 120-head budget into 20 execution hubs. Under a layout-matched three-seed recovery control, K20 reaches 0.960686 +/- 0.000059 mIoU versus 0.960400 +/- 0.000074 for the corresponding State120 control. The paired point difference is +0.000285, while a paired image-bootstrap confidence interval includes zero; we therefore interpret the result as no measurable quality penalty rather than statistical superiority. For deployment, FOLDED_VEC preserves donor-specific paths while vectorizing their execution. Relative to the same 120-head State120 parent, it reduces end-to-end NVIDIA L4 latency by 5.28%, 3.15%, and 3.58% at batch sizes 1, 4, and 8. These results suggest that attention redundancy includes not only removable capacity but also execution-depth redundancy, provided that the computational path defining a relocated function is preserved.

---


### 4. [GeoForward: Geometry-Guided Cross-View Alignment for Feedforward 3D Gaussian Splatting](https://arxiv.org/abs/2610.23895)

**<font color=#1a73e8>作者：</font>** Yiming Shu, Peng Sun, Lang Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feedforward 3D reconstruction has largely followed an {appearance-driven paradigm}: multi-view images are encoded into visual representations, cross-view correspondence is implicitly inferred from learned features, and 3D primitives are subsequently predicted from these representations. However, calibrated cameras and sparse metric measurements already provide explicit constraints on where the same physical point should appear across views. We propose a novel paradigm, \textbf{Geometry-Conditioned Feedforward Reconstruction}, in which metric geometry establishes cross-view correspondence before the 3D representation is formed, while learned visual features refine rather than discover this correspondence. Based on this paradigm, we introduce \textbf{GeoForward}. Sparse LiDAR points are unprojected into 3D and analytically projected across calibrated cameras to provide metric correspondence anchors. A bounded continuous local search then refines these anchors using visual features, and the resulting geometry-conditioned representation is fused with global multi-view context from VGGT. The shared representation drives separate metric-depth and Gaussian-attribute prediction, establishing a direct path from explicit geometry to both Gaussian centers and spatial attributes. A sparse 3D refinement module subsequently improves local attribute compatibility while preserving the geometrically determined centers. For temporal reconstruction, endpoint Gaussians are composed using vehicle masks and motion priors. On nuScenes, GeoForward achieves the lowest cross-camera depth-consistency error and Chamfer distance among the compared methods while maintaining competitive reconstruction quality. These results demonstrate that explicitly conditioning correspondence formation on metric geometry provides an effective alternative to purely appearance-driven feedforward 3D reconstruction.

---


### 5. [RhinoNet: Unsupervised Learning for Phenoscaping and Generation of High Dimensional Point Clouds](https://arxiv.org/abs/2610.23898)

**<font color=#1a73e8>作者：</font>** Siddharth Viswanath, Hiren Madhu, Eddie Cavallin 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present RhinoNet, a simplicial complex-based point cloud neural network, that creates a geometry-preserving embedding of high-dimensional point clouds. RhinoNet takes collections of datasets, also called {\em data cohorts}, and processes each dataset (point cloud) within the cohort as a simplicial complex. These simplicial complexes have datapoints as vertices and edges learned by Vietoris-Rips filtration. Using simplicial wavelets and MLP layers, RhinoNet computes a vector representation of each dataset in a latent space produced by an autoencoder. The latent space is optimized such that an optimal transport distance between pairs of point clouds is preserved between the latent representations. We apply RhinoNet to single-cell datasets collected on patients---a common source of such high-dimensional data. RhinoNet creates a patient level representation, known in biological contexts as a phenoscape. We establish that RhinoNet generates organized phenoscapes, whereas other methods such as static maps do not. Next we show that we can generate entire point clouds by sampling and decoding this phenoscape. We show two modes of generation via 1) latent flow matching and 2) geodesic interpolation in latent space, followed by a decoding back into the point cloud space. RhinoNet achieves state-of-the-art performance on single-cell and spatial data cohorts relative to tested baselines. Overall, RhinoNet lifts the concepts of representation learning and generative modeling to the point cloud or population level and defines a neural model for phenoscaping.

---


### 6. [EAGLE: Entropy-Aware Geometric Learning Enhancer for Partially Polygon-Supervised Object Localization](https://arxiv.org/abs/2610.23900)

**<font color=#1a73e8>作者：</font>** Naveen Stewart  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object detection is a critical application of computer vision, yet models trained uniformly on bounding boxes lack the geometric precision to be fully effective in inference settings, especially at high IoU thresholds. One common approach is the introduction of polygon-supervised localization, where a model is trained explicitly for localization but with access to polygon masks during training. Among such methods, partial polygon supervision is viable due to the higher annotation costs of developing fully supervised training datasets. However, this introduces a further challenge: in object classes of relatively low shape complexity, the addition of training masks and subsequent segmentation loss may obscure box localization, often worsening model performance despite access to deeper geometric information. To address the practical limitations of both full and partial polygon supervision, we introduce a mathematical framework for quantifying per-class geometric complexity by combining information theory and statistical shape analysis. With this framework, we develop Entropy-Aware Geometric Learning Enhancer (EAGLE), a lightweight, post-training model head that learns geometric information for the localization model, improving accuracy via edge refinement and localization rescoring using entropy-informed updates. Empirical analysis across MS COCO and Pascal SBD demonstrates the entropy framework meaningfully predicts shape reconstruction error and accuracy differences among mask-derived and standard box predictions, while the implemented EAGLE framework achieves consistent improvement on already SOTA detection frameworks (+0.9 mAP50-95 points on MS COCO) at minimal observed inference overhead.

---


### 7. [Rethinking weakly supervised localization on chest radiographs: position nulls, protocol dependence, and PACE](https://arxiv.org/abs/2610.23902)

**<font color=#1a73e8>作者：</font>** Shixin Qiu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Weakly supervised localization on chest radiographs is reported as a single overlap accuracy, and those numbers are not comparable across papers. We measure what one contains. Against position-null controls that keep a readout's own box and move only its position, class activation mapping and its gradient-weighted variant beat the null on two to four of seven annotated findings on ChestX-ray14 and two of eight on CheXlocalize. The null is beatable: three board-certified radiologists clear it on four to seven. Three rarely stated choices each move a result by more than most reported method effects: the results regime, the extraction threshold, and the mask-to-box rule, whose cost is predicted by how fragmented the thresholded mask is. Predicted box area alone reverses a paired comparison. These measurements produced PACE, for \emph{population anomaly and class evidence}, which multiplies the finding identity from the label-trained head by the spatial evidence from a frozen radiograph backbone that never sees a pathology label. It is the case study that made the protocol dependence visible, and we report its costs beside its gain: in an exploratory matched-area analysis it improves strict-overlap accuracy on both corpora and beats a label-derived second map, but it is the least faithful of the three readouts to the classifier's causal map, its advantage depends on the box rule, and, this benchmark releasing no localization validation set, every design choice behind it was made on the boxes it is scored on. Its one clean transfer beats one baseline and loses to the other.

---


### 8. [Instance-Specific Classifier-Free Guidance for Text-to-Image Diffusion/Flow-Based Editing](https://arxiv.org/abs/2610.23905)

**<font color=#1a73e8>作者：</font>** Wajeeh Atrash, Tom Tirer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In recent years, a variety of prompt-based image editing methods have been developed based on text-to-image (T2I) diffusion/flow models. Image editing introduces an inherent trade-off between adhering to the original source image and realizing the change specified by the target prompt, which are typically measured by the LPIPS and CLIP-T metrics, respectively. Intuitively, this trade-off can be controlled by the classifier-free guidance (CFG) scale. Most existing editing methods, though, use a fixed CFG scale, ignoring that different edits require varying levels of modification. In this paper, we first explore the potential benefits of using an instance-specific CFG by exhaustively re-running prominent editing methods with a wide range of CFG scale values on benchmark datasets. We show that instance-specific setting can significantly improve LPIPS without compromising CLIP-T. Yet, tuning based on repeatedly executing an editing pipeline is inefficient. To prevent slow inference, we train a light-weight neural network that predicts the metrics of the underlying editing method for a given edit instance and CFG scale. At inference time, these predictions enable fast selection of an instance-specific CFG scale. Experiments across multiple editing methods and benchmark settings show the performance advantage of our approach over the baseline methods.

---


### 9. [Beyond Generator-Specific Shortcuts: Open-World AI-Generated Video Detection via Adversarial Training](https://arxiv.org/abs/2610.23906)

**<font color=#1a73e8>作者：</font>** Qi Zhou, Yuanfan Li, Huiqi Deng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-generated video (AIGV) detection is increasingly important for mitigating misinformation, impersonation, and other malicious uses of synthetic media, yet existing detectors often generalize poorly to unseen generators in open-world settings. To better understand this challenge, we analyze the failure modes of AIGV detectors under cross-generator out-of-distribution (OOD) shifts and observe that detector representations strongly encode generator-specific cues, which are associated with substantial ID-OOD performance drops. Further analysis shows that naively perturbing generator-sensitive tokens can even reduce OOD performance, indicating that generator-related cues and detection-relevant evidence are only partially separable. Motivated by these findings, we propose Forensic Obfuscation of geneRator-specific cues via Gradient-guided Embedding perturbation (FORGE), a token-aware adversarial training framework for open-world AIGV detection. FORGE identifies tokens that are strongly associated with generator-specific shortcuts yet less critical to real/fake discrimination, and selectively perturbs them during training to suppress generator-dependent patterns while preserving useful forensic evidence. Through synchronized adversarial training between an attacker and a detector, FORGE encourages the detector to learn more transferable generator-invariant forensic representations. Experiments on 29 held-out benchmark entries show that FORGE achieves an average F1 of 92.62, outperforming eight strong baselines by 5.31 points, while also remaining robust under four common post-processing attacks. We will release our code and datasets upon acceptance.

---


### 10. [Pseudo-Label Foreground Quality Weighting for Domain-Generalized Fundus Image Segmentation](https://arxiv.org/abs/2610.23911)

**<font color=#1a73e8>作者：</font>** Lucas Gabriel Telesco, José Ignacio Orlando  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optic disc (OD) and optic cup (OC) segmentation is central to automated glaucoma assessment, but models trained on limited labeled fundus datasets often degrade under domain shift. Semi-supervised Teacher-Student learning can improve generalization by leveraging unlabeled data, yet standard Noisy Student training treats all pseudo-labels as equally reliable. In this paper we investigate a targeted extension of Noisy Student training in which OD- and OC-specific pseudo-label supervision is modulated using a mask-derived reliability estimate. A multitask Dice predictor estimates OD- and OC-specific pseudo-label quality from Teacher-generated masks, and these estimates are used to weight the pseudo-label loss during Student training. This preserves the baseline contribution of low-scoring foreground pseudo-labels while assigning greater relative emphasis to pseudo-labels predicted to be more reliable. Experiments across known and unseen domains show improvements over the Noisy Student baseline, particularly for OC segmentation, while maintaining competitive generalization performance.

---


### 11. [Junction Geometry Survives an Unidentifiable Blur](https://arxiv.org/abs/2610.23912)

**<font color=#1a73e8>作者：</font>** Sohail, Sarkar, Shakuntala Baichoo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Thin filaments cross in microscopy, and dispersed spectra cross on X-ray detectors. At a junction, where these structures cross or branch, how many straight arms meet, and which way do they go? Unknown blur obscures the answer. At a balanced crossing, distinct Gaussian blurs can even produce the same observation law. We show that the arms can still be recovered. For separated rays of nonvanishing weight and an unknown centered Gaussian-mixture blur, a distance combining arm count, directions, relative weights and supporting lines is bounded by a constant times the Euclidean difference in cell probabilities on a sufficiently fine fixed grid. The bound is uniform over a bounded model class, including unidentifiable blurs. From $n$ positions or photon counts, the minimax error is of order $n^{-1/2}$. This rate is proved for a global estimator. In practice we fit rays and blur by constrained local likelihood, reducing the BIC count when two detectors agree on fewer arms in the microscopy studies. Across three studies with protocols fixed before evaluation, on 360 crossings and branches assembled from measured single-molecule localizations, the fit gets the arm count and every direction within $10^\circ$ 24 to 37 percentage points more often than a tuned fixed-scale Hessian ridge detector, averaged over 25 to 400 localizations. On acute angles with correct counts, mean absolute error is $3.5^\circ$ to $4.3^\circ$, versus $10.4^\circ$ to $15.5^\circ$. On Chandra spectra, 38 of 90 fits at 800 photons find all four arms within $10^\circ$; among these, median error is $0.023^\circ$.

---


### 12. [SPIRIT: Sparse Physics-Informed Inverse Rendering for SAR Imaging](https://arxiv.org/abs/2610.23914)

**<font color=#1a73e8>作者：</font>** Yimeng Liu, Maolin Gan, Jingkai Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radio-frequency (RF) and wave-based imaging systems play a critical role in sensing under adverse conditions, but are fundamentally constrained by a trade-off between collection speed and spatial resolution. Reducing measurements to enable rapid collection of fragment geometric information across sensing dimensions, leading to highly non-injective inverse problems that destabilize conventional image-domain reconstruction and super-resolution methods. Synthetic aperture radar (SAR) exemplifies this challenge in sparse-aperture sampling. We introduce SPIRIT, a physics-informed inverse rendering framework for sparse-aperture SAR. Rather than enhancing formed images, SPIRIT reconstructs an explicit three-dimensional surface. By adopting an optimization strategy and explicitly modeling visibility, phase coherence, and wave propagation, SPIRIT aggregates distributed geometric features across sparse aperture views into a coherent reconstruction. Extensive experiments on synthetic and real-world data demonstrate that SPIRIT recovers accurate geometry and signal under extreme sparsity, reducing data collection by over 90% while achieving low geometric and signal error and consistently outperforming baselines.

---


### 13. [Your Self-Supervised Projection Head Captures Object Co-Occurrence Statistics](https://arxiv.org/abs/2610.23915)

**<font color=#1a73e8>作者：</font>** Arthur Aubret, Jochen Triesch, Céline Teulière  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-Supervised Learning (SSL) has achieved impressive success in learning semantic visual representations, yet the underlying principles driving this success remain underexplored. In this work, we hypothesize that common SSL pretext tasks implicitly model object co-occurrence statistics, a fundamental cue for visual learning. To test this, we curate three datasets of segmented objects from existing vision benchmarks using a state-of-the-art segmentation model. Through experiments across many SSL models, we reveal a hierarchical encoding of semantic information: while the visual backbone captures object categories, the projection head specializes in encoding co-occurrences between object categories. As a result, the projection head outperforms the backbone in aligning with human judgments of inter-category similarity. Furthermore, by controlling co-occurrence patterns during pre-training, we demonstrate that encoding object co-occurrences can significantly accelerate the emergence of category-level representations. Our findings uncover a previously hidden learning principle in SSL and suggest a path toward designing more effective pretext tasks by explicitly leveraging object co-occurrence structure.

---


### 14. [Announced Breaks Separate Conformal Reliability from Frequency Calibration](https://arxiv.org/abs/2610.23917)

**<font color=#1a73e8>作者：</font>** Karl Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An announced boundary reveals the partition before the first affected outcome, and a reset there serves one of two audits. The per-time audit reads conformal reliability, the expected distance of the threshold's coverage from nominal at miscoverage 0.1. The frequency audit reads frequency calibration, whether a closed window's error rate matched it. The reset rule, the post-boundary empirical quantile, attains the minimax per-time rate for independent scores. On bounded scores a recursion reset at the boundary attains a frequency gap of order one over the count when its floor adds a bounded total. At the 50th forecast after a large synthetic break, the reset rule's per-time gap stands below that of five adaptive methods, four from their authors' code, with every paired band below zero. After an electricity market reform, on 68 unseen scores, the band stands below zero against two, includes zero against two, adaptive conformal inference among them, and is a point at zero against one. After monetary policy decisions its pointwise band stands above zero against all five on 10 of the first 34 days. Of 9 announced boundaries one clears the smallest coverage difference its window detects, where every method's per-time gap at the 50th forecast exceeds the nominal miscoverage. Over the first 50 forecasts the reset recursion leads the frequency audit after every synthetic break.

---


### 15. [Cross-Modal Forgetting and Transfer in Unified Multimodal Post-Training](https://arxiv.org/abs/2610.23918)

**<font color=#1a73e8>作者：</font>** Francesco Colasurdo, Ivan Slobozhan, Joaquin Vanschoren 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified multimodal models answer questions about images and also generate images with one shared set of weights. This creates a post-training risk that single-purpose models do not have: fine-tuning one capability can damage another that works in a different modality. We measure this cross-modal forgetting for LoRA post-training of Janus-Pro-7B. Every target is chosen by how poorly the base model already handles it, from a poetic register to a language it barely speaks, so that retention is tested against a real intervention; we then evaluate the capabilities we never trained, first after a single run and then after chaining three. A single run looks entirely safe: nothing we did not train degrades on four public benchmarks or in free-form English, even when the adapter cuts held-out Welsh perplexity by 76% with a relative weight change under 2%. That safety belongs to the run, not to the recipe. Chaining three runs destroys the capability learned one run earlier and raises general-text perplexity by one to two orders of magnitude above the never-adapted model, on the very measures that stayed flat before. The cause is in the objective, which constrains only the modality being trained and leaves the other head unconstrained: cutting the learning rate to one fifth does not prevent the collapse, while anchoring the other head removes the damage to the capabilities we never trained, at no cost to what is learned. What is learned also stays inside its own modality, with Welsh acquired from text closing only 3% of the English-Welsh gap in image generation.

---


### 16. [SpinDoctor: Finding Innocuous Prompts for Biased Image Generation](https://arxiv.org/abs/2610.23925)

**<font color=#1a73e8>作者：</font>** Anna Gerchanovsky, Omer Akgul, Lujo Bauer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce SpinDoctor, a method for discovering innocuous prompts for text-to-image models that result in images with a chosen target bias, while retaining the quality of the images and prompts. These prompts present a risk for user manipulation, in that a user who is given these seemingly unbiased prompts might be willing to use them and would receive biased images in return. Our method is flexible: it uses models in a black-box way only and the target image bias can easily be changed, and so our method can be applied with various motivations and in various scenarios. Our method shows some transferability between models-we saw the same bias emerge in 78.6% of cases-such that a victim who uses a prompt generated via our method using one model still likely receives a biased image from another model. In our experiments, a subset of which we corroborated with human evaluation, we were able to find an innocuous prompt that moved generated images in the direction of the desired bias in all but two of 304 experiments, with an average improvement of 34.8% and 33.5% on two open-source text-to-image models.

---


### 17. [Improving Fake Profile Detection Through Multimodal Learning and Research-Guided Feature Integration](https://arxiv.org/abs/2610.23926)

**<font color=#1a73e8>作者：</font>** Jean Claude Hirwa, Jamiu Dahunsi, Candide Giramata 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fake accounts continue to undermine online platforms, yet it remains unclear whether multimodal learning offers meaningful improvements over strong metadata baselines or graph-based approaches. In this work, we study bot detection by integrating textual, visual, and account metadata signals on the TwiBot-22 benchmark using a subsample of 30,000 users. We propose a multimodal framework combining pretrained textual (XLM-RoBERTa) and visual (CLIP) embeddings with structured account-level features such as follower counts, posting frequency, and account age, and evaluate multiple modality combinations using CatBoost alongside a Relational Graph Convolutional Network (R-GCN). Results show that metadata alone is highly predictive, while multimodal fusion yields only marginal and largely statistically insignificant gains. The graph-based model underperforms classical variants under the subsampled graph conditions of this study. Overall, our findings suggest that under practical constraints, feature quality and metadata richness matter more than fusion complexity.

---


### 18. [Trimodal Context-Aware Micro-Expression Recognition in Real-World Conversations: A Dataset and a Hierarchical Fusion Network](https://arxiv.org/abs/2610.23930)

**<font color=#1a73e8>作者：</font>** Junbo Wang, Yan Zhao, Shigang Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recognizing micro-expressions in real-world conversations is challenging, as these facial movements are brief and faint, and their interpretations are strongly dependent on the contextual circumstances of their occurrence. Most existing methods are de-contextualized, as they analyze isolated video clips while disregarding the semantic and acoustic cues in the surrounding dialogue that help explain the emergence of an expression. Decades of psychological studies have shown that social context exerts influences on facial behavior over two key dimensions: how an expression is interpreted and how strongly it is generated to begin with. However, existing micro-expression research rarely incorporates such contextual factors into its models. As an example, provocative utterances from an interlocutor may elicit suppressed negative affective reactions, which isolated silent clips are unable to account for. We propose TriCoME, a trimodal dataset consisting of visual, audio and text data sourced from real-world conversations. In this dataset, each micro-expression is paired with its concurrent utterance and preceding context. We further annotate the context based on conversational role to denote two categories: external stimuli from an interlocutor's utterance and internal background from the subject's own utterance. On this basis, we propose the Hierarchical Focusing Fusion Network (HFFNet), which aligns acoustic and semantic streams at fine granularity, compresses long dialogue sequences, modulates attention toward conversational roles via a context-type embedding, and routes each sample between visual-only and multimodal decisions based on visual confidence to prevent noisy context from degrading recognition performance.

---


### 19. [STLQ: Spatio-Topological Linkage Quantization for Approximate Nearest Neighbor Search](https://arxiv.org/abs/2610.23931)

**<font color=#1a73e8>作者：</font>** Kuizhi Liu, Junying Zhang, Xindi Ma 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vector quantization is widely used for large-scale data compression and approximate nearest neighbor search (ANNS). Multi-codebook quantization (MCQ) is a practical paradigm that represents database vectors with compact codes and supports efficient retrieval through asymmetric distance computation (ADC). However, existing shallow MCQs encode vectors independently within each inverted file (IVF) cluster, without exploiting local references. Therefore, we propose Spatio-Topological Linkage Quantization (STLQ), a topological shallow MCQ method that organizes each IVF cluster as a directed-forest with compact codes and scaling coefficients. Its basic encoding phase first quantizes vectors independently, while the linked encoding phase re-encodes relative residuals with respect to selected reconstructed parents, reusing local reconstruction information to obtain finer representations. The corresponding linked-ADC preserves linear scanning complexity. STLQ further compresses the scaling coefficients and directed-forest structure to control the additional topology overhead. Extensive experiments show that STLQ achieves higher recall than the evaluated shallow MCQs at comparable bit budgets, although at a higher offline construction cost. Meanwhile, it has a competitive recall-QPS tradeoff against deep MCQs. The code is available at this https URL.

---


### 20. [Toward AI-Driven Phytoplankton Event Detection from Image Classification: Temporal Aggregation Under Domain Shift](https://arxiv.org/abs/2610.23932)

**<font color=#1a73e8>作者：</font>** Ali Rohan, Hassan Shayan, Han-Gue Jo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Imaging FlowCytobot (IFCB) systems generate large volumes of phytoplankton imagery that exceed the capacity of manual expert analysis. Although machine-learning approaches achieve high image-level classification performance, it remains unclear whether their predictions can provide ecologically meaningful temporal information for monitoring. This study investigates whether AI-derived phytoplankton classifications can reproduce temporal occurrence patterns and elevated-occurrence signals under realistic sampling and independent-domain transfer. A monitoring-oriented framework was developed using MedPlanktonSet and evaluated on an independent IFCB dataset from the Swedish Meteorological and Hydrological Institute (SMHI). Eight biologically comparable taxa were selected as targets, while all remaining observations were retained as background to preserve the full image-stream denominator. Session-aware partitioning prevented temporal leakage, and alternative preprocessing strategies and convolutional neural network architectures were evaluated. Cross-domain experiments showed that preprocessing strongly affected generalisation. EfficientNet-B0 provided the strongest target-versus-background discrimination and was selected for temporal analysis. Despite residual image-level errors, AI-derived target-occurrence rates closely reproduced expert-derived signals after aggregation (mean absolute error = 0.0432, Pearson $r$ = 0.9696, Spearman $\rho$ = 0.9568). Agreement remained strong across multi-session windows, and elevated, strong, and persistent occurrence proxies were recovered in held-out testing. These results show that AI-based phytoplankton classification can support monitoring-relevant temporal indicators beyond image-level identification and support future operational early-warning development.

---


### 21. [SECURE-AI: Multi-Signal Uncertainty Quantification for Trustworthy Acoustic Cough Detection](https://arxiv.org/abs/2610.23937)

**<font color=#1a73e8>作者：</font>** Sejal Solkhan, Feiya Xiang, Mayur Sanap 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Acoustic models for cough detection achieve high accuracy on curated benchmarks but fail silently in deployment, where speech, environmental noise, and audio unlike the training data induce confident misclassifications. In health monitoring, a confidently wrong prediction is worse than no answer at all. We present SECURE-AI (Self-aware Estimation of Cough Uncertainty for Reliable Evaluation of AI), a multi-signal uncertainty quantification framework that wraps a frozen MobileNetV3 cough classifier and estimates when its predictions should not be trusted, combining Monte Carlo Dropout, Temperature Scaling, and Mahalanobis distance in the embedding space. On a held-out split of 12,161 Coswara recordings, the probability-space methods are individually insufficient: Monte Carlo Dropout assigns lower uncertainty to incorrect than to correct predictions, and temperature scaling improves calibration but not discrimination. The strongest signal is embedding-space distance: Mahalanobis distance separates true positives from false positives (means 44.7 versus 63.4; Cohen's $d = 0.94$; AUROC 0.86) and, among predicted non-coughs, false negatives from true negatives (AUROC 0.82), so the same signal can flag both false alarms and missed coughs. At a descriptive operating point selected from labeled test data, retaining 90 percent of true-positive detections removes about two-thirds of false positives and raises precision from 59.9 to roughly 80 percent. A rejection threshold tuned on one split does not transfer to another (validation F1 of 82 percent falls to 34 percent on test), so we report threshold-independent AUROC as the main measure. An error taxonomy shows that failures are systematic, with most false positives related to speech. The pipeline runs on Raspberry Pi hardware costing 30 to 90 US dollars. Probabilistic calibration alone is thus inadequate for reliable cough detection.

---


### 22. [Pack and Extract: An Effective Graph-Based Approach for Feature Selection](https://arxiv.org/abs/2610.23938)

**<font color=#1a73e8>作者：</font>** Faisal N. Abu-Khzam, Joseph R. Barr, Cynthia Chaaya 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many molecular biology data sets contain thousands of features, such as genes in single-cell experiments or other omics data. Standard predictive models often perform poorly in such settings, as they tend to retain a large number of features and fail to adequately handle correlations among them. Combinatorial approaches, such as feature selection based on the Independent Dominating Set (IDS) model, have shown promising results, but appear to have been largely overlooked, possibly due to their high computational complexity. In this paper, we propose an improvement to IDS-based feature selection that (i) favors features exhibiting greater diversity and (ii) generalizes the notion of independent dominating set to a node packing model. The resulting formulation is used as an intermediate step within the feature selection process. We evaluate our approach on five genetic data sets and compare the results with those obtained using existing methods. Our experimental results demonstrate notable improvements in predictive accuracy over traditional models, as well as increased stability of the selected feature sets.

---


### 23. [Fast Construction of Inner Sphere Trees Using Machine Learning](https://arxiv.org/abs/2610.23940)

**<font color=#1a73e8>作者：</font>** Jianneng Huang, Wenjia Rao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Collision detection for complex non-convex objects is a bottleneck in physics simulation, virtual reality, and robotics. Inner sphere trees (ISTs) answer proximity and penetration queries efficiently, but their greedy leaf-sphere construction is sequential and computationally expensive, which limits both large-scale preprocessing and runtime use. In this work, we present ML-IST, a machine-learning-based method that reformulates leaf-sphere generation as a single-shot set-prediction problem: a network predicts a fixed set of inscribed sphere candidates from multichannel voxel geometry, differentiable coverage feedback corrects the coarse prediction and fills residual gaps at finer scales, and a lightweight geometric projection enforces validity. Averaged over the test set, a single-GPU implementation of ML-IST reduces mean leaf-generation time by a factor of $2.0$--$2.6$ over single-core CPU construction across target capacities of 64--512 spheres, and qualitative results on complex models show multiscale sphere distributions that follow principal volumes and slender features. We further integrate ML-IST into the Jolt Physics and Bullet engines; in an alpha-puzzle benchmark it reaches 55.89~FPS, the highest among the compared representations (conventional IST, GImpact, and convex decomposition). These results support learned leaf generation as a practical component for fast, runtime construction of detailed collision representations.

---


### 24. [A Group-Aware Comparative Study of Classical Machine Learning and Deep Learning Methods for Sensor-Based Human Activity Recognition](https://arxiv.org/abs/2610.23941)

**<font color=#1a73e8>作者：</font>** Wahyu Pebrianto  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Human Activity Recognition (HAR) using wearable or smartphone inertial sensors is commonly evaluated with both classical machine learning and deep learning methods. However, reported performance can be strongly affected by sensor modality, dataset characteristics, and data-splitting strategy. This study presents a controlled comparative evaluation of four classical machine learning models and four deep learning models on two public HAR datasets, UCI-HAR and KU-HAR. Three sensor modalities were considered: accelerometer (ACC), gyroscope (GYRO), and their combination (ACC+GYRO). Classical machine learning models used handcrafted statistical features, while deep learning models operated directly on raw sensor sequences. The primary evaluation employed five-fold StratifiedGroupKFold cross-validation, with subject- or participant-level grouping to prevent group overlap between training and test folds. Macro-F1 was used as the primary performance metric. The results show that deep learning did not consistently outperform classical machine learning. On UCI-HAR, the evaluated deep learning models achieved slightly higher macro-F1 values, whereas on KU-HAR, LightGBM achieved 0.857 compared with 0.828 for the highest-performing evaluated deep learning model. Regarding sensor modality, the combined ACC+GYRO configuration generally outperformed ACC or GYRO alone on both datasets. The evaluation protocol also had a substantial effect: for CNNBiLSTMAttn with ACC+GYRO, random splitting increased macro-F1 by 0.033 on UCI-HAR and 0.093 on KU-HAR compared with grouped evaluation. These findings highlight the importance of model family, sensor modality, dataset characteristics, and group-aware evaluation when assessing sensor-based HAR systems.

---


### 25. [Parameter misspecification in physics-informed neural networks: A closed-form audit and its limits](https://arxiv.org/abs/2610.23948)

**<font color=#1a73e8>作者：</font>** David McShannon, Nicholas Dietrich  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) are trained to minimize the residual of a prescribed equation, so a low training loss does not indicate whether a coefficient in that equation was specified incorrectly. This study evaluates what can be inferred about the encoded parameter from the trained network alone. When the residual is linear in the parameter, written as $A - \nu B$, the least-squares estimate $\hat{\nu} = A^{\top}B/B^{\top}B$ is obtained from a single evaluation of the frozen network, without retraining or reference data. Its accuracy depends on how closely the network satisfies its own equation, quantified by a normalized residual $\rho$. Recovery error is associated with $\rho$ (log-log correlation 0.72 across 36 convection-diffusion networks), and empirical exponents of 0.63 to 1.20 across three equations decompose into one half plus a measurable angular term. For Burgers' equation, a single-model test based on a block-bootstrap standard error flagged 3 of 300 correctly specified networks (observed false-alarm rate 1%), all 2% misspecifications at a practical budget, and two thirds of 1% misspecifications after convergence. For the self-similar blowup rate of the Córdoba-Córdoba-Fontelos equation, where the rate also enters the architecture, the estimator recovers about half of the misspecification, whereas $\rho$ increases approximately quadratically and distinguishes a 0.2% error. When the incorrect rate enters both the equation and the architecture, errors of up to 2% were not detected at the precision reached. At practical budgets, the raw loss can be lower for the misspecified model, a scaling effect that $\rho$ does not share.

---


### 26. [DS-Net: A Dynamic Split Network for Edge-Cloud Collaborative Inference](https://arxiv.org/abs/2610.23949)

**<font color=#1a73e8>作者：</font>** Xinyun Zhang, Li Wang, Lei Jin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Collaborative inference serves as a critical methodology in edge intelligence. Existing collaborative inference methods operate by splitting the deep neural network (DNN) model between edge devices and cloud servers. However, these methods need to load different models for multiple split points when the communication or device changes, thus resulting in long switching times and substantial storage overhead on the edge side. To address this issue, we propose a Dynamic Split Network (DS-Net), which not only enables efficient split point switching but also enhances the collaborative speed and accuracy across various scenarios. Specifically, we design a dynamic switching framework that enables flexible selection among multiple split points within a single model, thereby reducing storage, memory, and switching overhead. To mitigate the feature distribution shifts and task-relevant information loss caused by dynamic splitting and high-ratio compression, we further propose a hierarchical compensation mechanism. Local alignment calibrates the decoded feature distribution at each split point, while task-specific global compensation restores task-relevant information at the global level. In addition, we incorporate sample-adaptive global compensation selection into split-point selection based on sample complexity and runtime resource conditions. Experimental results demonstrate that DS-Net reduces memory overhead by 74.6% and achieves millisecond-level switching latency. Moreover, under a 10 Mbps bandwidth constraint on the Nano platform, DS-Net outperforms state-of-the-art collaborative methods by achieving 1.2% higher accuracy on the COCO dataset, reducing latency by 42.5%, and improving throughput by a factor of 1.8$\times$.

---


### 27. [DISCERN: Identifiable Disease Evidence for Generalizable Medical Multimodal Learning](https://arxiv.org/abs/2610.23952)

**<font color=#1a73e8>作者：</font>** Xiaoguang Zhu, Pengyi Jiang, Juncen Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clinical multimodal models can learn enrollment shortcuts shared across modalities and fail on new cohorts. We model these data through a latent structural causal model: disease state and background factors generate physiology through shared mechanisms, while cohorts differ in selection and measurement. Holding acquisition fixed, we identify conditional disease evidence without observing disease-state labels or recovering the full causal model. In common Gaussian coordinates, cross-cohort state alignment and natural-parameter changes identify a minimal selection statistic; conditioning on it removes enrollment-dependent evidence and yields an identifiable reference posterior within the specified shift family. State-dependent interactions can carry evidence invisible to individual-modality posteriors, motivating joint, information-preserving representations. DISCERN combines an information-lattice encoder, a latent-state model, and an outcome head through joint training. Under reversed synthetic enrollment on known latent coordinates, conditioning raises state AUROC from 0.043 to 0.883 and from 0.265 to 0.825, while random conditioning does not. Exploratory cross-database mortality experiments between eICU and MIMIC-IV improve AUROC over matched empirical risk minimization by 0.036 and 0.035. Learned-coordinate diagnostics distinguish preservation of state information from identification of the coordinates required by the estimator.

---


### 28. [Physics-Aware Self-Supervised Pretraining on Multi-Domain Raman Spectra](https://arxiv.org/abs/2610.23955)

**<font color=#1a73e8>作者：</font>** Charalampos Davalas, Georgios Levantinos, Anastasios Dimitriou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Raman spectroscopy generates large volumes of unlabeled data that are difficult to exploit with conventional supervised learning. This work introduces a multi-domain self-supervised learning framework based on a masked autoencoder (MAE) for learning transferable Raman spectral representations from heterogeneous biological, chemical, forensic, and materials datasets. The proposed pretraining strategy incorporates physics-aware objectives by combining masked intensity reconstruction with a sparse Voigt-profile decoder that models spectral peak structure through differentiable peak centers, widths, and amplitudes. A denoising objective is further included to improve robustness to spectral corruption. The learned encoder is evaluated on substance classification, component identification, concentration estimation, and spectral denoising under linear probing, attention-based probing, end-to-end fine-tuning, and training from scratch. Experimental results show that self-supervised pretraining is most beneficial for challenging tasks with limited labeled data. Attention-based probing also reveals substantially more useful information in the frozen representation than linear probing, indicating that conventional linear evaluation may underestimate representation quality. In addition, the benefits of pretraining become more pronounced with increasing encoder capacity. Overall, the proposed framework demonstrates that physics-aware, multi-domain self-supervised pretraining can improve label efficiency, robustness, and transferability across diverse Raman spectroscopy tasks.

---


### 29. [Generalizable fetal brain biometry via adaptive artificial intelligence](https://arxiv.org/abs/2610.23966)

**<font color=#1a73e8>作者：</font>** Yijin Li, Mingxuan Liu, Yi Liao 等 27 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable fetal brain biometry on magnetic resonance imaging (MRI) is essential for diagnosing congenital brain anomalies, but artificial intelligence models often lose accuracy under domain shifts. We developed BioTTA, a backbone-agnostic, source-free unsupervised test-time adaptation framework that adapts pretrained models online to individual unlabeled target volumes. This retrospective multicohort study included 394 reconstructed 3D fetal brain MRI volumes at 20-39 gestational weeks, with 11 biometric measurements annotated by radiologists. BioTTA was developed on single-center turbo spin-echo MRI and evaluated on three datasets representing cross-sequence, cross-center, and cross-nation shifts. Biometry accuracy was assessed using mean absolute error (MAE) and the percentage of correct measurements within 4 mm. A web-based reporting platform mapped measurements onto normative growth trajectories and was evaluated against radiologists in four multicenter disease cohorts covering germinal matrix-intraventricular hemorrhage, ventriculomegaly, and cerebellar abnormality. Across all three target datasets, BioTTA outperformed auto-SVRTK, source-only models, and FetalSynthGen, while matching models finetuned with target labels. MAEs ranged from 1.10 to 1.46 mm with a convolutional backbone and from 1.46 to 2.25 mm with a transformer backbone. Diagnostic accuracy ranged from 82.1% to 95.0%, comparable to a senior radiologist. BioTTA supports accurate, generalizable fetal brain biometry and standardized prenatal brain growth assessment across heterogeneous MRI sources.

---


### 30. [Geo-vision: Native-Resolution Geometry and Sampled Topology for Vehicle-Part Damage Classification](https://arxiv.org/abs/2610.23967)

**<font color=#1a73e8>作者：</font>** Usef Faghihi, Amir Saki, Serge Jonathan Kogbeti-Wongo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geo-vision classifies vehicle-part damage using a fixed representation combining appearance, multiscale geometry, orientation, and sampled digital topology. Connected components, holes, Euler characteristics, and spatial arrangement complement amplitude-sensitive pooling and a supervised tree classifier. We establish amplitude preservation, axial sign invariance, and conditional operator stability. Retrospective checkpoint evaluation on 55,303 crops from 4,916 source groups yields average precision 0.7577, exceeding 0.7458 for an ImageNet-pretrained frozen YOLO11n comparator on identical crops. The complete added structural block, comprising topology, occupancy, and component location, improves average precision by 0.00493 beyond appearance and geometry. Geo-vision uses no external encoder pretraining and has higher AP point estimates at every matched label budget. With approximately 25% fewer task labels, its AP point estimate exceeds full-data YOLO, although the adjusted interval includes zero. Complete serial CPU inference requires 26.98 ms per crop versus YOLO's 11.20 ms, with peak memory 185 versus 437 MiB. Independent external validation remains necessary.

---


### 31. [IMPULSE: Push First, Then Predict in V-JEPA 2 Feature Space](https://arxiv.org/abs/2610.23968)

**<font color=#1a73e8>作者：</font>** Tingan Jin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent world models such as V-JEPA 2 forecast in the feature space of a video encoder, but one look at an object does not reveal how hard it is to rotate, how much it bounces or how much it slides. People find out by trying: a few pokes reveal how an object responds. IMPULSE, named after the impulse response it infers, gives a predictor in frozen V-JEPA 2 feature space the same ability. A Bayesian contact memory summarizes three short calibration pushes, a predicted object pose carries it into the predictor, and a lightweight random-Fourier pose head lets the predictor use the pose. On 512 fresh objects, in a pre-specified held-out confirmation with models sealed before the data existed, the memory lowers the 1-second feature-forecast error by 11.6-12.8% relative to the same predictor without experience, for all 8 training seeds, with a 95% seed-and-object interval excluding zero. The gain also holds for 128 objects with out-of-range physics (11.7-14.0%), and the full extension beats a plain predictor by 15.5-16.6%. An information-ladder argument, exact for ideal predictors, shows that physics reaches the features only through motion, so we measure how much the pathway lets pose help. On fresh objects, the Fourier head roughly triples the gain of a perfect memory over plain pose tokens (2.8-3.2x). Raw push measurements fed through the same pathway give a similar gain, so the Bayesian summary is not required; it condenses the trials into eight interpretable numbers. The gain is absent at contact onset and grows afterwards.

---


### 32. [Spatio-Temporal Detection of Photovoltaic Systems on Industrial Building Rooftops Using Satellite Imagery and Machine Learning](https://arxiv.org/abs/2610.23970)

**<font color=#1a73e8>作者：</font>** Frederick Bruch, Christian Knoth, Florian Detsch 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The global transition toward carbon-neutral energy systems is heavily dependent on the rapid deployment of solar photovoltaic (PV) infrastructure, yet the speed of this expansion has outpaced the ability of administrative registries to maintain accurate records. While high-resolution commercial imagery is often used for monitoring, its high cost and infrequent updates can create an information gap for grid operators, energy infrastructure developers and policymakers. This study addresses the lack of scalable monitoring for industrial-scale rooftop PV systems by developing a machine learning framework that utilizes open-access, multispectral Sentinel-2 satellite imagery. By integrating building geometries from OpenStreetMap with Sentinel-2 reflectance data, a Random Forest model was trained to identify the specific spectral signatures of PV modules. Moving beyond theoretical modeling, this work emphasizes practical implementation through the development of an interactive web-based prototype for on-demand site monitoring. The application enables users to retrieve up-to-date satellite observations and assess the presence of PV systems on industrial building rooftops. The tool incorporates quality metrics that inform users whether a prediction is supported by sufficient training data density or requires manual verification. This end-to-end framework demonstrates that open-source medium-resolution data can effectively bridge this monitoring gap.

---


### 33. [Super-resolution as Spatial Downscaling: Coherence, Structure and Task Utility in Earth Observation](https://arxiv.org/abs/2610.23972)

**<font color=#1a73e8>作者：</font>** Bright Wiredu Nuakoh, Ebenezer Afrifa-Yamoah  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learned satellite super-resolution is commonly assessed by pixel fidelity and potential downlink savings, but these criteria do not establish whether the reconstructed field preserves spatial structure or supports reliable downstream analysis. We treat single-image super-resolution as a spatial downscaling problem and evaluate four lightweight networks, including our compact 0.36 million-parameter model, against interpolation using pixel metrics, directional variograms, spectral band correlation, codispersion and observation coherence. On 735 satellite tiles from 190 scenes, the networks differ by at most 0.03dB and outperform bicubic interpolation by $1.39-1.42$dB at $\times 2$. They recover about 30% of the spectral power above the observation's Nyquist frequency and, at $\times 4$, produce more isotropic fields than the reference (range anisotropy 0.59 against 0.49). Energy-based metrics can favour invented detail. Enforcing coherence reaches the quantisation limit, yet at least 99.7% of the remaining error lies in the observation operator's null space, which coherence cannot constrain. Under spatially blocked, paired evaluation with two backbones and a sharpening control, learned reconstruction changes land-use accuracy by $-1.0$ to $+3.1$ percentage points (significant in 7 of 24 comparisons) and building-change F1 by $-0.015$ to $+0.024$ (none significant) relative to bicubic interpolation, and amplifies spurious change between two observations of an unchanged scene by $1.3-1.5$ times where interpolation attenuates it. Full-resolution JPEG\,2000 matches or exceeds reduced-resolution transmission with reconstruction at every matched bitrate. Learned reconstruction is most useful when only low-resolution imagery is available, and its evaluation should combine pixel metrics with spatial structure, observation coherence and task-level tests under spatial validation.

---


### 34. [SituHOI: Scalable Capture of Scene-Situated Full-Body Human-Object Interaction](https://arxiv.org/abs/2610.23980)

**<font color=#1a73e8>作者：</font>** Qifan Wang, Qihang Fang, Boao Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modeling human-object interaction (HOI) in real environments requires jointly representing whole-body motion, manipulated objects, and scene geometry, yet existing datasets trade off scalable capture against structured, scene-aligned supervision. We introduce SituHOI, a large-scale RGB-D dataset containing 18,429 annotated clips across 16 indoor rooms and approximately 86 hours of quality-screened activity. It pairs recordings from a single moving RGB-D camera with static scene scans, object geometry, language descriptions, and estimated human and object trajectories. Using the scans as persistent references, our pipeline combines camera localization and depth-based metric alignment with human mesh recovery, object tracking, and temporal refinement to register all geometric annotations in a shared floor-aligned frame. These data support FlexHOI-Bench, a goal-conditioned joint motion prediction benchmark with variable observation and prediction durations. Given observed histories, scene and object geometry, and a terminal object pose, models predict future human and object motion. We provide SharedHOI as a reference predictor and evaluate world-space accuracy and human-object coordination. On a MoCap subset, our pipeline reduces human G-MPJPE from 195.4 to 68.3 mm and object translation error from 43.0 to 28.7 mm. SharedHOI leads four adapted baselines on all three aggregate FlexHOI-Bench metrics. Data will be released upon acceptance. An anonymized code repository is available at this https URL.

---


### 35. [Time-JEPA: Grounding Video World Models with Physical Time Series](https://arxiv.org/abs/2610.23982)

**<font color=#1a73e8>作者：</font>** Shenyi Li, Ziyang Zhang, Wen Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models learn how visual environments evolve by predicting missing or future content. However, physical-state information can provide useful context for predicting how environments evolve. Prior work incorporates this information through different mechanisms: domain-specific physical laws can complicate multi-domain training, while supervision on individual frames or frame pairs gives limited attention to how physical state evolves over time. We introduce Time-JEPA, which fine-tunes a video world model using low-dimensional, temporally aligned physical time series as auxiliary supervision. Physical time series connect video representations with physical state at corresponding temporal positions, encouraging the model to preserve how physical state evolves. In multiple domains including autonomous driving, robot manipulation, and human motion, Time-JEPA improves current-state decoding, multi-horizon future-state prediction, and kinematic reconstruction over matched video-fine-tuned controls across both condition and state-variable distribution shifts. Multi-domain training provides aggregate gains over matched single-domain training in all three tasks. External evaluations further suggest that time-series supervision improves sensitivity to physical anomalies and the representation of physical interactions, including in unseen scenarios. Aggregate gains on a second video backbone indicate that the method can be applied to more backbones. These results suggest that physical time series help video world models better understand the physical world.

---


### 36. [Pretrained Features as Teachers, Not States: Compact Latent World Models for Visual Planning](https://arxiv.org/abs/2610.23984)

**<font color=#1a73e8>作者：</font>** Yanbo Wang, Nan Lin, Wendelin Böhmer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A key design choice in visual world models is what information the latent state is encouraged to preserve. Models that learn a latent space with only a latent-prediction objective adapt to environment dynamics, but the predictive objective alone admits collapsed solutions and provides no explicit constraint on the visual information retained by the latent. Models built directly on pretrained visual features inherit a strong visual prior, but tie prediction and planning to a frozen state space. We propose Anchor-WM, which instead uses pretrained visual features as a teacher for learning a compact latent state rather than as the world-model state itself. Anchor-WM learns this compact latent with action-conditioned dynamics, while distilling the dense DINO representations through a training-only distillation head. This encourages the compact latent to retain visual information captured by the pretrained representation while discouraging representational collapse. At inference, the DINO encoder and distillation head are discarded, allowing prediction and planning to operate entirely in the learned latent space. Anchor-WM achieves the best average success rate across the four evaluated environments while enabling substantially faster planning than world models operating directly on DINO patch features. These results show that pretrained visual features can effectively guide world-model learning without defining the state space used for prediction and planning.

---


### 37. [Automatic Cause Determination in Road Scene Understanding Using Qualitative Reasoning and Four-Valued Logic](https://arxiv.org/abs/2610.23990)

**<font color=#1a73e8>作者：</font>** Nassim Belmecheri, Arnaud Gotlieb, Nadjib Lazaar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Road scene understanding in automated driving (AD) aims to build a comprehensive analysis of video sequences taken on the road by embedded or fixed cameras (e.g., mounted on vertical road signals). One goal is to identify the relevant actors in the scene and another goal is to determine the causes that have triggered a specific action of the ego car (i.e., stop, slow down, turn left, etc.). In a complex urban environment, these causes can be multiple, confusing, possibly contradictory to other causes and not easily expressible using simplistic reasoning. Still, providing accurate {\it automatic cause determination} supports a) user acceptance by providing appropriate explanations to the car passengers and road users; b) increased road safety by providing detailed road scene understanding to traffic. In this paper, we propose using spatiotemporal reasoning and Belnap's four-valued logic to formulate complex causes of AD action in a road scene. We compute these causes by analysing a Qualitative eXplainable Graph (QXG), which is an abstract representation of the road scene capturing spatiotemporal relations between road entities. Starting from a QXG, our approach called \tool, is targeted to determine complex causes of a selected AD action occurring in a specific frame of a road scene. The usefulness of \tool is demonstrated on several scenes extracted from the well-known NuScene dataset.

---


### 38. [Causal Spatio-Temporal Neural Distance Fields for Counterfactual Cardiac Anatomy](https://arxiv.org/abs/2610.24001)

**<font color=#1a73e8>作者：</font>** Mathias Lowes, Kurt Butler, Kristine Aavild Sørensen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Counterfactual cardiac anatomy can support risk modelling and intervention planning, by predicting how a patient's heart would change under altered clinical conditions. However, current shape generative models are conditional on clinical variables and disregard causal links between these variables. Thus, they cannot answer counterfactual questions about how a given subject's anatomy would change under a different clinical profile. Modelling the heart's continuous movement over the cardiac cycle requires a representation that is itself continuous in space and time. Spatio-temporal neural distance fields provide this while separating clinical conditioning from subject-specific shape. We place a structural causal model (SCM) over the set of clinical variables (age, sex, smoking, BMI, heart rate, systolic blood pressure), before the condition encoding of the spatio-temporal neural distance field which represents the left atrial complex over a cardiac cycle by signed distance fields. An intervention of the clinical variables, propagated through a SCM before the 4D counterfactual, is constructed from the neural distance field. The generated counterfactuals follow dose-response under age interventions and transforms the male distribution to closely match the female distribution under the intervention $\mathrm{do(\mathrm{female}{=}1)}$. By doing inverse interventions the model also approximates the original anatomy with sub millimeter precision. To our knowledge, this is the first counterfactual generation of 4D cardiac anatomy and the first integration of an SCM with an implicit neural representation as its imaging mechanism.

---


### 39. [spora: A Unified Multimodal Dataset and Platform for Spatial Proteomics](https://arxiv.org/abs/2610.24002)

**<font color=#1a73e8>作者：</font>** Benedikt von Querfurth, Johann Wenckstern, Eeshaan Jain 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial proteomics (SP) captures the molecular composition and spatial organization of tissues at single-cell resolution, opening a direct view of the cellular ecosystems that drive disease. Protein panels, acquisition platforms, and tissue contexts differ from one cohort to the next, and a coherent picture of tissue biology can only emerge from models trained to bridge this heterogeneity. Foundation models offer the natural path forward, but their training depends on large, harmonized corpora that span platforms, panels, and cohorts. No public resource currently approaches that scale; available data sit in small, narrowly scoped releases with incompatible formats and conventions. We present $\texttt{spora}$, a large-scale multimodal SP dataset of 13,546 standardized multiplex images from 5,477 patients across 35 cohorts and five major SP technologies. Curated with biomedical experts, $\texttt{spora}$ provides model training-ready formats together with cell and tissue segmentations, structured clinical metadata, and, where available, paired H&E enabling the training of virtual staining models. It is complemented by $\texttt{spora [io]}$, a unified interface for tiling, sampling, and standardization across all cohorts and modalities, and $\texttt{spora [bench]}$, a benchmark suite spanning cell phenotyping, diagnostic and therapeutic prediction as well as virtual staining tasks across twelve cohorts that places current SP foundation models on common ground against task specific baselines.

---


### 40. [What Social Media Teaches Us About Accumulative AI Risks](https://arxiv.org/abs/2610.24006)

**<font color=#1a73e8>作者：</font>** Dawei Li, Bohan Jiang, Huan Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prominent AI safety discussions emphasize existential threats and catastrophic events, such as AI-enabled nuclear conflict or engineered biological outbreaks. This position paper argues that there is another type of AI risk that arises and accumulates from the widespread use of AI. Drawing on lessons from social media, we argue that safety assessments must also address accumulative harms that develop through repeated use, recurring decisions, and feedback across interconnected deployments. Repeated reassurance, selective exposure, recurring decision biases, and growing personal profiles may gradually narrow perspectives, weaken independent judgment, or enable exploitative influence without a single clearly harmful event. We advance the Trajectory Neglect Thesis: a focus on vivid catastrophic events and identifiable incidents risks overlooking less visible harms that accumulate through the widespread daily use of AI. Social media research motivates this position by showing how reciprocal media effects, social reinforcement, and individual susceptibility shape outcomes beyond individual encounters. We examine how related mechanisms may operate in AI systems, using conversational AI as a concrete setting where generation, semantic inference, and persistent memory may tighten feedback loops. Sycophancy, manipulation, and privacy loss provide a case study of how these risks may interact and accumulate. This comparison identifies mechanisms to investigate rather than assuming that repeated AI use is harmful. We therefore call for evaluation of cumulative patterns of use and deployment, individual and societal outcomes, careful causal inference, and proportionate safeguards that preserve useful assistance and informed user choice.

---


### 41. [SPADE-KD: Peer-to-Peer Collaborative Learning under Heterogeneous Settings](https://arxiv.org/abs/2610.24013)

**<font color=#1a73e8>作者：</font>** Harikrishna Kuttivelil, Katia Obraczka  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Peer-to-peer collaborative learning is an emerging distributed deep learning paradigm that eliminates the need for a central aggregator and disseminator, avoiding the single-point-of-failure and bottleneck issues they can bring. Many such approaches use parameter averaging, requiring clients to have homogeneous model architectures, whereas others use knowledge distillation as an alternative while leaning on shared public data or centralized control infrastructure. Many of these approaches also make a one-size-fits-all assumption, i.e., jointly training a single, globally optimal solution for all clients, when in reality, clients' underlying data distributions might differ such that a globally optimal solution may not be locally optimal for all clients. To enable collaborative learning in environments with both model architecture and data distribution heterogeneity, we present SPADE-KD -- a fully decentralized model distillation framework that optimizes collaboration towards personalized rather than global performance. SPADE-KD leverages two mechanisms -- adaptive distillation and utility-driven peer selection. Adaptive distillation modulates the strength of each incoming model transfer by the performance advantage of the incoming model compared to the native model measured by their task losses, such that a client will distill more aggressively from incoming models that outperform it on its own local data. Utility-driven peer selection uses the loss-informed utility derived from adaptive distillation to rank prospective partners, focusing on exchanges that measurably improve the local model while suppressing low-utility transfers. Using federated classification tasks, we demonstrate that SPADE-KD consistent outperforms naive decentralized distillation with lower loss and faster convergence and that its individual components are more effective together than independently.

---


### 42. [Dynamical Kernel Attention: Estimating the Present from a Record of the Past](https://arxiv.org/abs/2610.24026)

**<font color=#1a73e8>作者：</font>** Peter Racioppo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard self-attention compares tokens by similarity but does not account for how much of a past state survives to the present. We introduce Dynamical Kernel Attention (DKA), which derives attention from robust estimation of a latent state evolving under stochastic dynamics. As a past state decays toward equilibrium under the dynamics, the information it carries about the present vanishes, bounding the total evidence a head can draw. Unlike recency biases, DKA can abstain when relevant evidence is weak and guarantees a bounded error when old tokens are discarded. DKA preserves the parallel structure and computational cost of standard attention. We present the model and its theory; empirical evaluation is deferred to a subsequent version.

---


### 43. [SynerGest: Temporal-Spatial Synergistic Gesture Generation for Dyadic Conversations](https://arxiv.org/abs/2610.24031)

**<font color=#1a73e8>作者：</font>** Chengxiang Guo, Jian Wang, Lanmiao Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Co-speech gesture generation in dyadic conversations for creating immersive virtual avatars remains highly challenging. Existing models often struggle to balance kinematic stability with rhythmic responsiveness and suffer from semantic entanglement, leading to either generic mean-pose regression or unnatural micro-jitters. To address these challenges, we propose SynerGest, a high-fidelity dyadic gesture generation framework grounded in Contrastive Flow Matching (CFM). Specifically, our CFM objective explicitly penalizes mismatched semantic pairs during training, discouraging spatial shortcuts and over-smoothed predictions while improving conditional semantic alignment. Furthermore, to overcome architectural bottlenecks, we introduce the Impulse-Trend Synergistic Attention (ITSA) module. Grounded in the key insight of decoupling "what moves" from "when it moves," ITSA models sharp, speech-driven rhythmic impulses separately from continuous kinematic trends, supporting precise audio-motion synchronization and global structural stability. Extensive qualitative and quantitative evaluations on two public datasets demonstrate that SynerGest achieves state-of-the-art performance, delivering contextually responsive and kinematically fluid dyadic interactions.

---


### 44. [Client-Aware Security Adaptive Early Exit Vision Transformers for Heterogeneous Federated Learning](https://arxiv.org/abs/2610.24036)

**<font color=#1a73e8>作者：</font>** Sahar Refaei Ghalibafan, Samira Nazari, Christian Herglotz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) trains a shared model across data-owning clients without centralizing raw data, but client data difficulty and compute budgets can differ. We study local early-exit Vision Transformer (ViT) inference, where an intermediate classifier may return a prediction before the final Transformer stage. The proposed method replaces one global acceptance threshold with a client-specific base threshold from label entropy and shallow-exit confidence, then adjusts each input using predictive entropy, confidence, top-two class margin, and exit depth. Aggregation uses only clients that updated a parameter. Security-aware routing reaches 88.70% CIFAR-10 accuracy with 32.0% depth saving and 73.7% ImageNet-1K top-1 accuracy with 30\% saving. On matched six-client non-IID CIFAR-100, full-depth accuracy is 72.28% versus 68.20--71.80% for four heterogeneous-FL baselines; robustness-aware routing reaches 70.01% with 32.55% saving.

---


### 45. [What Remains Without Test Labels? Re-evaluating a Graph-Level Anomaly Detection Benchmark](https://arxiv.org/abs/2610.24045)

**<font color=#1a73e8>作者：</font>** Yujie Lu, Da Yan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph-level anomaly detectors are trained only on normal graphs, yet benchmarks may use test labels for model selection. We examine whether UB-GOLD results reused by later papers support label-free detection. We audit UB-GOLD and 14 GLAD code bases, re-run 21 detectors on UB-GOLD's folds under selection rules with and without test labels, and evaluate sensitivity to known structural changes. Test labels select checkpoints in UB-GOLD's shared training loop and checkpoints or hyperparameters in 8 of the 14 code bases. UB-GOLD also evaluates its kernel baselines against misaligned labels. Across nine datasets, selecting checkpoints by test AUROC adds an average of 5.12 AUROC points [3.97, 6.24] for the 12 UB-GOLD detectors relative to the final checkpoint and 4.13 [3.32, 4.79] relative to held-out normal graphs. In a post hoc permutation analysis with no truly better checkpoint, picking the best of noisy test evaluations still yields a gain more than half as large as the one observed against the final checkpoint. Configurations tuned on test labels score a further 1.53 points [0.64, 2.42] above repository defaults, a gap that mixes the value of test labels with that of tuning itself. With tuned hyperparameters and label-free checkpoint selection, the two strongest detectors retain their lead, while comparisons below them are less stable. Six of eight detectors evaluated out of sample miss size-preserving composition changes that graphlet counts detect. We recommend reporting results selected without test labels as the main comparisons and release per-run outputs that allow verification without retraining.

---


### 46. [Discuss More, Comment Less: Boosting Automated Research via Multi-Perspective Collaborative Review](https://arxiv.org/abs/2610.24050)

**<font color=#1a73e8>作者：</font>** Junkai Zhou, Jiajia Wu, Zhaoyi Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As automated research is increasingly adopted for writing papers, automated review has become a critical link between paper generation and quality control. However, existing methods largely rely on single-model feedback or simple review aggregation, failing to explicitly model expert responsibilities or collective deliberation in actual peer reviews, which limits effective cross-examination and reliable decision-making. Therefore, we formulate paper review as a computational modeling problem of peer review mechanisms and propose RoundtableReview, a deliberative multi-agent framework for enhancing automated research. RoundtableReview structures each paper into eight semantic slots and coordinates six academic and industry reviewers with complementary perspectives, retrieval sources, and specialized responsibilities. Through independent assessment, cross-examination, roundtable deliberation, dynamically weighted voting, and chair synthesis, the framework generates evidence-based and traceable feedback. Experiments on two automated research backbones show that the method improves paper quality in both backbones and outperforms baselines in automatic and human evaluations with fewer comments.

---


### 47. [LogicVal:A Logic-Formalized Benchmark for Constraint Satisfaction in Text-to-Image Generation](https://arxiv.org/abs/2610.24051)

**<font color=#1a73e8>作者：</font>** Savitha Sam Abraham, Marjan Alirezaie, Hossein Rahnama  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text-to-Image (T2I) generative models have made significant progress in producing high-fidelity images from natural-language prompts. Alongside this progress, numerous benchmarks have been developed to evaluate capabilities such as attribute binding, numeracy, spatial reasoning, and commonsense reasoning. In this work, we propose a new perspective on T2I evaluation by casting it as a constraint-satisfaction problem. We introduce a logical framework that formally specifies the benchmark domain, including objects, attributes, and relations, alongside the constraints that generated images must satisfy. We evaluated four state-of-the-art T2I models across 9 classes of constraints ranging from a single-object-attribute to multi-object relationships constraints involving logical operators ($\forall, \exists, count, \rightarrow$). Our results reveal a substantial gap between single-object and complex conditional multi-object relationship constraint classes, with the best-performing model achieving 98% accuracy on the former and just 53% on the latter. We assess compositional generalisation, finding that the best-performing model`s accuracy drops from 84% on single-constraint prompts to 20% when satisfying multiple constraints simultaneously. Identifying unsatisfiable constraints is also challenging, with the best model correctly recognizing only 23% of such prompts. Building on this framework, we introduce \textbf{LogicVal}, an evaluation methodology that combines neural visual detection with logical reasoning to assess constraint satisfaction in generated images. On CLEVR, LogicVal achieves ROC-AUC scores ranging from 0.88 to 0.98, indicating strong alignment with human judgments. These findings underscore the value of logic-based evaluation for characterizing T2I model capabilities and limitations.

---


### 48. [World of SWECraft: Agent Collaboration at Scale via Simulated Software Worlds](https://arxiv.org/abs/2610.24061)

**<font color=#1a73e8>作者：</font>** Shannon Zejiang Shen, Yapei Chang, Qiyao Liang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As teams of AI agents take on larger projects and long-standing open problems, agent collaboration offers another dimension for scaling inference-time compute. To understand what makes such collaboration effective and scalable, we develop Software World, a framework for simulating multi-agent coworking in realistic software ecosystems. It comes with a pipeline to create environments of real, interdependent Python packages of different topics, sizes, and dependency structures, which we call software worlds. In a simulation, agents maintain packages in the world with a high-level goal of improving software efficiency, and they are free to discover tasks to work on and collaborate with others. We evaluate agents' work in a world collectively by measuring speedup in hidden dependent packages. The framework allows us to study different elements of collaboration by varying communication, ownership, and resource allocation. We run simulations in three different worlds, totaling more than 10,000 hours of agent work across eight models. Overall, performance improvement scales with inference-time compute, with the best model improving downstream efficiency by up to 31%. We show that most agents can find meaningful tasks via collaboration, but some frontier models can prematurely stop looking for improvements and make little progress. We release the simulation framework and traces to support future studies of agent collaboration at this https URL.

---


### 49. [OrTeN: Neural Inverse Graphics for Joint Terrain and Line-scan Camera Trajectory Reconstruction](https://arxiv.org/abs/2610.24075)

**<font color=#1a73e8>作者：</font>** Josef Biberstein, Sertac Karaman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Digital terrain maps (DTMs) are used for landing site selection, terrain-relative navigation, and geological analysis in planetary exploration. Existing state-of-practice reconstruction techniques for creating DTMs from satellite imagery use multi-view stereo, requiring complex pipelines for dealing with camera error, changing illumination, and images with limited disparity. This work introduces Orbital Terrain Networks (OrTeN), a DTM construction method that uses neural inverse rendering to jointly optimize a textured height map and orbital camera corrections from line-scan satellite images. OrTeN operates directly on calibrated line-scan images with pixel values expressed as radiance factor (I/F) and corrects both broad trajectory pose inconsistencies and high-frequency pointing jitter jointly with surface reconstruction during training. Surface-projected patch normalized cross-correlation (NCC) enforces consistency between observations of the same terrain, refining an initial rough reconstruction. A semi-empirical reflectance model and shadow rendering are used to fit surface appearance from multi-date imagery with differing solar illumination. OrTeN requires only calibrated line-scan images and initial camera poses and does not use any structural priors including ranging/depth measurements or initial rough DTMs. OrTeN is evaluated on four planetary imagery datasets. Aligned terrain RMSEs are 2.35 m at Jezero Crater, 2.82 m at Gale Crater, 16.18 m at Olympus Mons, and 0.43 m at McGetchin Crater.

---


### 50. [GLOW: General Linear Models Optimized with Ward's Method](https://arxiv.org/abs/2610.24085)

**<font color=#1a73e8>作者：</font>** Matt Higger  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neuroimaging seeks brain regions whose imaging features correlate with variables of interest (e.g., diagnosis, age), usually via the General Linear Model (GLM). Region-Based Analysis dilutes or splits any effect that does not fill exactly one atlas region. Voxel-Based Analysis, with Cluster Extent Thresholding and Threshold-Free Cluster Enhancement built on it, fits a GLM per voxel and groups adjacent significant voxels. But neighboring voxels can share a statistic without sharing a GLM, which a per-voxel statistic cannot detect.
GLOW (General Linear Models Optimized with Ward's method) instead builds a hierarchy of nested regions by greedily minimizing GLM error (provably a special case of Ward's clustering). Maximum-statistic (Westfall-Young) permutation controls family-wise error over all regions. Significance spreads to an effect's nested fragments and the regions containing it; a final pruning step seeks whole, pure effect extents.
We plant synthetic effects of known extent and varying strength in Human Connectome Project (HCP) diffusion images and in white noise. Pruning delivers wholeness: GLOW returns a spatially consistent effect as one region on 57% of HCP trials, the best baseline on 35%; baselines recover comparable volume, but in many pure pieces. The cost is positive predictive value (PPV): GLOW is more sensitive (by up to 0.29), but its regions overrun the effect, mostly because no hierarchy region isolates it, not because of pruning. On HCP, GLOW's mean Dice gains 0.059 over the best baseline at weaker effects and gives back 0.005 at stronger ones.
On white noise, GLOW trails by up to 0.61 Dice: its hierarchy holds the effect, but its permutation test does not certify it. Runtime grows roughly linearly with voxel count, about 4.5 times the voxel-wise methods' on the full HCP volume. The PPV loss may trace to the assumption of spatially independent residuals.

---


> [!TIP]
> 当前位于：**1-50**（第 1/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-534](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
