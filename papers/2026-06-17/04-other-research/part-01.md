# 📦 其他研究 | 2026年06月17日

> 本类共 **509** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-509](./part-11.md)

---

### 1. [RAMS: Resource-Adaptive and Detection-Conditioned Model Switching for Embedded Edge Perception](https://arxiv.org/abs/2606.14716)

**<font color=#1a73e8>作者：</font>** Kushal Khemani, Evan Leri, George Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Edge object detection on embedded hardware requires balancing inference latency and detection quality under changing resource pressure. We present RAMS, a lightweight runtime controller that monitors device pressure, calibrates switching thresholds from idle behavior, and dynamically selects among three resident YOLOv8 tiers (NANO/SMALL/MEDIUM at 320/416/640 px) without model-reload latency. RAMS defines five switching policies, including two detection-conditioned variants that prevent aggressive downgrades after recent vulnerable-road-user (VRU) detections. We further introduce the VRU-Weighted Accuracy Score (SWAS), a scalar metric for offline policy comparison without ground-truth annotations, together with an oracle-bounded variant that separates detector circularity from genuine tier-retention benefit. Across Raspberry Pi 5, x86 laptops, and Jetson Orin ONNX/TensorRT deployments, the same controller equations operate over a 37x latency range. On Jetson Orin TensorRT under heavy load, the safety2 policy achieves 3.41 ms mean latency, 5.6x faster than fixed-MEDIUM inference, while retaining 74% of its proxy accuracy through near-NANO operation with selective SMALL and MEDIUM locks during VRU-positive windows. Detection-conditioned switching improves SWAS by 25.4% under oracle scoring and 47.3% under detector-derived scoring relative to threshold-only policies under heavy load. Live KITTI evaluation reports per-tier VRU recall of 24.2%, 41.2%, and 59.0%, showing that reactive overrides are fundamentally limited by baseline detector recall.

---


### 2. [AI for Maritime Security: Comparative Evaluation of CNN and Vision Transformer Architectures for Maritime Object Detection](https://arxiv.org/abs/2606.14720)

**<font color=#1a73e8>作者：</font>** Ismet Gocer, Zakirul Bhuiayn, Shakeel Ahmad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This study aims to enhance maritime security by using advanced Artificial Intelligence (AI) and Computer Vision (CV) techniques. For this purpose, it was designed and assessed intelligent object detection systems that can detect the presence of ships on the sea surface under different real-time environments. To achieve this goal, a maritime image dataset with 6,468 images was used, covering different weather conditions like cloudy, foggy, rainy, and sunny environments. Six deep learning architectures were evaluated, including a base Convolutional Neural Network (CNN) model, four transfer learning models (Xception, VGG16, MobileNetV2, and EfficientNetV2L), and a Vision Transformer (ViT) model. The models were compared using multiple performance indicators, including accuracy, Type I and Type II errors, model size, and video processing time. The results show that model performance varies depending on computational constraints and deployment conditions. While lightweight architectures are suitable for resource-limited devices, the ViT achieved the best overall performance, reaching 100% accuracy with the lowest error rates and the fastest video processing time. The findings highlight the potential of AI-driven computer vision systems for maritime surveillance, border protection, and autonomous navigation.

---


### 3. [Disagreement-Based Cross-Model Routing for Implicit Video Question Answering](https://arxiv.org/abs/2606.14723)

**<font color=#1a73e8>作者：</font>** Durga Sandeep Saluru  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study multiple-choice video question answering on the ImplicitQA benchmark, where the correct answer is never explicitly shown but must be inferred from off-screen events, line-of-sight cues, causal structure, and cross-shot spatial layout. On this benchmark a single frontier video LLM already operates near its accuracy ceiling, and we observe that conventional self-consistency strategies -- majority voting across repeated samples of the same model -- can hurt rather than help, because the model's errors on hard questions are correlated. We propose disagreement-based cross-model routing, a pure inference-time procedure that requires no labels and no training. We triple-sample a native-video model (Gemini 3.1 Pro Preview) at temperature zero, exploit the genuine sample-to-sample variance of its video-processing pipeline to identify the roughly 20% subset of questions where the three samples disagree, and route only that subset to a second model from a different family (Claude Opus 4.8) that consumes uniformly sampled frames with adaptive thinking. On the 1001-question validation set with public ground truth -- our main evaluation -- the method improves AvgAcc by +1.43 over the best single sample of the primary model, with per-category gains concentrated on Motion & Trajectory (+5.49), Inferred Counting (+3.45), and Vertical Spatial Reasoning (+1.82) -- the categories most dependent on cross-shot reference resolution. The same pipeline applied to the held-out 172-question CVPR 2026 ImplicitQA challenge test set achieves 82.03 AvgAcc / 79.71 MacroAvgAcc (+1.81 over the best single sample of the primary model), confirming the validation result on an independent split.

---


### 4. [VigilFormer: Deformable Attention for Video Anomaly Detection with Causal Risk Inference](https://arxiv.org/abs/2606.14724)

**<font color=#1a73e8>作者：</font>** Xinze Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video anomaly detection in surveillance settings must balance detection accuracy against real-time throughput, a tension that existing methods address either through stronger feature extractors or more efficient architectures, but rarely both. We present VigilFormer, a unified framework that combines deformable spatio-temporal attention with causal temporal modeling to detect anomalies in untrimmed surveillance video. The proposed Deformable Spatio-Temporal Encoder (DSTE) attends to a sparse set of informative locations across frames, avoiding the quadratic cost of dense attention while retaining the ability to capture irregular motion patterns. A Causal Anomaly Classifier (CAC) applies dilated causal convolutions over snippet-level features and optimizes a contrastive multiple-instance learning objective that separates anomalous and normal representations without frame-level labels. To meet deployment constraints, an Adaptive Confidence Scheduler (ACS) dynamically skips low-information frames at inference time, reducing redundant computation in static scenes. Evaluated on UCF-Crime, ShanghaiTech, and CUHK Avenue, VigilFormer achieves AUC scores of 87.83%, 97.21%, and 89.74% respectively, at 41.5 FPS on a single GPU, outperforming recent weakly-supervised methods in both accuracy and speed.

---


### 5. [Interpolation between Convolution and Attention via K-Nearest Neighbors](https://arxiv.org/abs/2606.14725)

**<font color=#1a73e8>作者：</font>** Mingi Kang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The shift from Convolutional Neural Networks to Transformers has reshaped computer vision, yet these two architectural families are typically viewed as fundamentally distinct. Convolutional Neural Networks are defined by spatially local convolution operations, while Transformers rely on global self-attention. We argue that convolution and self-attention, despite their apparent differences, can be unified within a single k-nearest neighbor aggregation framework. The critical insight is that both operations are special cases of neighbor selection and weighted aggregation. Convolution selects neighbors by spatial proximity while self-attention selects by feature similarity, revealing that they lie on a continuous spectrum rather than representing categorically different computations.
We introduce Convolutional Nearest Neighbors (ConvNN), a unified framework that formalizes this connection. ConvNN exactly recovers standard and depthwise convolution by restricting neighbor selection to normalized spatial coordinates, and exactly recovers self-attention and its sparse variants, including KVT-attention, by replacing spatial proximity with scaled dot-product similarity. Beyond these special cases, ConvNN serves as a drop-in replacement for both convolution and attention layers, enabling systematic exploration of the intermediate spectrum between local and global aggregation through configurable similarity functions, neighbor selection strategies, positional encodings, and aggregation kernels.

---


### 6. [FairGen: Preference-Aligned Diffusion for Demographically Equitable Medical Image Synthesis](https://arxiv.org/abs/2606.14727)

**<font color=#1a73e8>作者：</font>** Zhimin Li, Ruichen Zhang, Zhen Tan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical imaging is central to modern diagnostics, and artificial intelligence (AI) systems are increasingly used to support image-based analysis by improving efficiency, accuracy, and access to care. However, inequities in healthcare access and differential disease prevalence create severe demographic imbalances in clinical image data. Such imbalances are compounded by the fact that diseases can manifest with distinct features across demographic groups, rendering certain phenotypic presentations naturally rare. AI models trained on such imbalanced data risk perpetuating diagnostic bias and widening healthcare disparities. Here we introduce FairGen, a fairness-aware diffusion framework that synthesizes demographically balanced medical images while preserving pathology-relevant visual features. By embedding physician-aligned preferences into the generation process, FairGen improves subgroup coverage during synthesis and downstream classification. Applied to dermatology, radiology, and neuroimaging benchmark tasks, FairGen achieves fairness improvements of 95.9% for skin images, 80.0% for chest radiography, and 35.2% for brain MRI, while maintaining competitive diagnostic accuracy relative to models trained on original clinical data. Clinician-facing expert review and external validation on independent cohorts further support that these gains extend beyond standard fidelity metrics and are not confined to the original in-distribution datasets.

---


### 7. [Hierarchical GRU with Input-Conditioned Slot Queries for Ball Action Anticipation](https://arxiv.org/abs/2606.14730)

**<font color=#1a73e8>作者：</font>** Parthsarthi Rawat  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a hierarchical model for ball action anticipation in football broadcast video. Given a 30-second observation window, the system predicts actions occurring in the subsequent 5-second window across 10 classes. A shared local Transformer encodes clip-level features within each 5-second sub-window; a GRU then aggregates temporal context across all sub-windows; finally, a Transformer decoder with K input-conditioned event slots decodes the anticipation target via three decoupled heads (objectness, class, temporal offset). We introduce frequency-reweighted Hungarian matching that systematically favours rare action classes, and Gaussian soft targets for temporal bin supervision. On the SoccerNet Ball Action Anticipation benchmark, our method achieves 17.91% mAP on the test server.

---


### 8. [BBR-Net: Boundary-Balanced Replay for Continual Medical Image Segmentation](https://arxiv.org/abs/2606.14731)

**<font color=#1a73e8>作者：</font>** Zahid Ullah, Sieun Choi, Jihie Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continual learning for medical image segmentation remains challenging under domain shift because replay-based methods often preserve appearance information without explicitly modeling anatomical structure. This study investigates whether structural consistency governs knowledge retention in continual cardiac ultrasound segmentation. We propose the Boundary-Balanced Replay Network (BBR-Net), which selects replay samples using boundary-aware priority and class balance to preserve anatomically informative regions. The method is evaluated on CAMUS and CardiacNet under forward (CAMUS to CardiacNet) and reverse (CardiacNet to CAMUS) task orders. In the forward setting, BBR-Net retains source-task performance close to an offline joint-training reference, while markedly reducing catastrophic forgetting and preserving competitive target-task adaptation. Ablation results show that boundary-aware prioritization contributes to retention and improves the balance between source-task preservation and target-task adaptation when combined with class-aware sampling. In contrast, the reverse setting reveals that structure-aware replay fails when initial representations are learned from noisy and structurally inconsistent data. To isolate this effect, we conduct a controlled structural perturbation analysis by progressively corrupting source-task boundaries while keeping the dataset, architecture, and training protocol fixed. Forgetting increases consistently as structural reliability decreases, suggesting that replay effectiveness is strongly influenced by the quality of stored structural information, rather than by memory capacity alone. These findings indicate that preserving anatomical structure under domain shift is a central factor in continual medical image segmentation, and that replay mechanisms should account for structural reliability to support robust knowledge retention.

---


### 9. [Steady-Forcing: Balancing Spatial Persistence and Motion Continuity in Long-Horizon Nature Video Diffusion](https://arxiv.org/abs/2606.14732)

**<font color=#1a73e8>作者：</font>** Matiur Rahman Minar, Seunghun Oh, GangHyeon Jeong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video diffusion models enable streaming generation but often degrade over long rollouts: static scene layouts drift, while mechanisms that improve spatial stability tend to suppress motion, causing natural flows such as water, fire, or smoke to stagnate. We study this stability-motion trade-off in fixed-camera long-horizon nature video generation, where the two failure modes can be more clearly separated than in moving-camera settings. We propose Steady-Forcing, a memory and training framework combining a persistent visual anchor (V-Sink), an exponential moving-average motion memory (EMA-Sink), block-relative temporal encoding, periodic cache purification, and distillation from a Wan2.1-14B teacher with motion-rewarded priors under task-focused configurations. Together, these components are designed to preserve background identity while sustaining visually plausible fluid dynamics over multi-minute autoregressive rollouts. Evaluations across seven baselines show that Steady-Forcing improves long horizon background consistency and imaging quality, while a blind user study indicates stronger perceived stability and motion continuity. The benchmark evaluation further suggest that generic VBench aggregate scores under-penalize fixed-camera artifacts as well as rewarding drift-induced optical flow as Dynamic Degree while not directly penalizing texture hardening or flow stagnation - motivating future task-specific benchmarks for static-camera nature-flow evaluation. Project page: this https URL

---


### 10. [UtVAA: Ultra-tiny Vision Transformer with Affix Attention for Mobile Image Classification](https://arxiv.org/abs/2606.14735)

**<font color=#1a73e8>作者：</font>** Romiyal George, Sathiyamohan Nishankar, Selvarajah Thuseethan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) have demonstrated strong representation capability in image classification. However, their quadratic self-attention complexity and large parameter counts limit deployment on resource-constrained mobile and edge devices. This paper introduces UtVAA, an ultra-tiny Vision Transformer architecture designed for efficient visual recognition under strict computational budgets. It incorporates a novel Affix Attention block that combines depthwise-pointwise local feature extraction, linear self-attention, coordinate attention for spatial dependency modelling, and a lightweight ternary fusion strategy to integrate local and global representations. In addition, Dilated Bottleneck blocks expand the receptive field using dilated depthwise separable convolutions while maintaining low FLOPs and stable optimisation through residual connections. UtVAA is implemented in scalable Tiny, Medium, and Large variants, with the smallest model containing 204.67K parameters and 53.95M FLOPs. Experimental results on CIFAR-10, CIFAR-100, PlantVillage-Tomato and SLIF-Tomato datasets show that UtVAA achieves competitive accuracy within a sub-million-parameter regime. Overall, the results demonstrate that transformer-based vision models can be redesigned into ultra-tiny architectures without significant loss in discriminative performance, making UtVAA suitable for mobile and edge deployment. Code is available at this https URL

---


### 11. [HorusEye: Language as Dynamic Attention for Emergency Visual Analysis](https://arxiv.org/abs/2606.14741)

**<font color=#1a73e8>作者：</font>** Armel Yara  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce HorusEye, Language as Dynamic Attention for Emergency Visual Analysis. Our investigation followed five stages. The first one is benchmarking RefCOCO-Degraded, a dataset of 15,244 images (3,811 base images x 4 conditions: Clean, Fog, Smoke and Thermal) with systematic visual degradation. Through four research questions, we evaluate multiple VLMs (Gemini, Qwen2-VL, BLIP-2, LLaVA, Kosmos-2) across visual grounding the second stage, language feedback recovery the third one, health VQA tasks the fourth, and hallucination analysis the final stage. Our key finding is that language feedback effectiveness is model-dependent: Gemini achieves +47.3% improvement in thermal conditions through iterative language feedback, while Qwen2-VL shows -5.1% degradation under the same protocol. We also identify the 'Thermal Paradox' where cropping strategies that improve RGB performance catastrophically fail in thermal imagery. Furthermore, BLIP-2 uniquely hallucinates more under degradation, making it unsuitable for emergency deployment

---


### 12. [Style-CCL: Content-Preserving Style Transfer via Curriculum Continual Learning](https://arxiv.org/abs/2606.14746)

**<font color=#1a73e8>作者：</font>** Shiwen Zhang, Haoyuan Wang, Xianghao Zang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Content-Preserving Style transfer, given content and style references, remains challenging for Diffusion Transformers (DiTs) due to entangled content and style features. With a reverse triplet synthesis pipeline to build a million-scale training set and a dual-branch Style-Content DiT (SC-DiT) that decouples style and content via separate ROPE embeddings and causal masking, we observe that such a one-stage training paradigm on mixed style categories causes semantic styles to dominate, hindering texture style learning, and harming content preservation. To address these issues, we propose Style-CCL, a Multi-Stage Curriculum Continual Learning framework that trains SC-DiT from semantic (easy) to texture (hard) styles, and from clean to synthetic data, with Random Memory Rehearsal across stages to avoid catastrophic forgetting. Extensive experiments demonstrate that our Style-CCL achieves state-of-the-art performance in three core metrics: style similarity, content consistency, and aesthetic quality.

---


### 13. [Is My Vision-Language Data in Your AI? Membership Inference Test (MINT) Demo 2](https://arxiv.org/abs/2606.14748)

**<font color=#1a73e8>作者：</font>** Daniel DeAlcala, Gonzalo Mancera, Julian Fierrez 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present the Membership Inference Test (MINT) Demo 2, a framework designed to improve transparency in machine learning training processes. MINT is a technique for experimentally determining whether specific data were used during machine learning model training. We establish the theoretical framework and propose multiple architectures for MINT depending on the amount of information known about the models that are being audited. Experimental results using a popular face recognition model, 4 state-of-the-art LLMs, and multiple, diverse, and large-scale public image and text databases achieve promising accuracy levels in the detection of training data of up to 90%. Building on these results, we introduce a comprehensive web platform1 that expands these capabilities to image and text modalities. The platform integrates a diverse technological stack, including MINT, aMINT, and gMINT, allowing users to audit a wide range of models. This demonstrator aims to promote AI transparency and provides a practical tool to foster compliance with emerging AI regulations.

---


### 14. [Automated 3D Kinematic Monitoring for Circadian Activity and Anomaly Detection in Juvenile Fish](https://arxiv.org/abs/2606.14749)

**<font color=#1a73e8>作者：</font>** Chih-Wei Huang, Chang-Wen Huang, Chung-Ping Chiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Precision aquaculture faces a "phenotyping bottleneck" in tracking high-resolution behavioral traits, as conventional methods cannot quantify instantaneous three-dimensional (3D) physical exertion. To address this, we present a high-throughput 3D behavioral phenotyping framework integrating deep learning object detection with binocular stereo vision for real-time monitoring of juvenile tilapia in high-density environments. The system automates non-contact body length estimation and reconstructs 3D swimming trajectories from absolute spatial coordinates. By eliminating 2D perspective distortions, this approach precisely quantifies 3D velocity and acceleration, marking the first estimation of true physical swimming speeds in free-roaming juveniles. Results show the framework successfully establishes circadian locomotor baselines, serving as an early warning system for physiological stress and providing an objective metric for fish vitality.

---


### 15. [Beyond Self-Attention: Sub-Quadratic Vision Transformers for Fast Image Captioning](https://arxiv.org/abs/2606.14753)

**<font color=#1a73e8>作者：</font>** Chiradeep Ghosh, Dakshina Ranjan Kisku  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image captioning is a challenging and significant task that aims to generate coherent and semantically meaningful textual descriptions for given images. To accomplish this task, it requires a deep understanding of visual content along with the ability to express that understanding in natural language. Despite remarkable progress with transformer-based architectures, existing approaches often suffer from limitations, such as a lack of rich local feature representations and the high computational cost of quadratic self-attention. The proposed model focuses on improving computational efficiency by restructuring the vision transformer architecture. In designing this approach, the standard self-attention mechanism in Vision Transformers is replaced with a probabilistic transformer approach based on a Gaussian Mixture Model (GMM), a soft-clustering technique. Instead of computing pairwise attention among all image patches, the model groups similar patches into a fixed number of clusters using an Expectation-Maximization (EM) algorithm. This clustering-based mechanism reduces the computational complexity from quadratic O(n^2) to linear O(nK), where K << n. The autoregressive GPT-based decoder is used for caption generation. The model is evaluated on the Flickr 30K dataset, demonstrating competitive and significant improvement over existing works.

---


### 16. [Sub-Semantic Image Segmentation](https://arxiv.org/abs/2606.14754)

**<font color=#1a73e8>作者：</font>** Aviad Cohen Zada, Nadav Orenstein, Shai Avidan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Images can be segmented based on visual cues (i.e., texture segmentation) or into objects (i.e., semantic segmentation). We propose a new category of sub-semantic image segmentation that blurs the line between the two. In sub-semantic image segmentation, language is not used to name whole objects. Instead, it is used to partition an image into stable appearance patterns that can be described by language. To do that, we couple a general-purpose vision-language model to SAM 3, a promptable segmentation backbone whose native text pathway can ground rich descriptions into masks. Simple coupling fails for a number of reasons that we identify in the paper, and we overcome them by introducing DETECTURE that resolves three concrete failure modes -- language leakage between texture regions, prompt competition inside the segmentation backbone, and semantic distortion at the language-to-mask interface. Since there is no dataset of sub-semantic image segmentation, we introduce one, termed TextureADE. The new dataset is derived from the ADE20K dataset using a system we designed. We compare DETECTURE to a number of baselines and find that it achieves the strongest performance on several datasets using different metrics. Code is available at this https URL.

---


### 17. [Where Does Texture Evidence Live in SAM? Features, Proposal Masks, and Texture Segmentation](https://arxiv.org/abs/2606.14755)

**<font color=#1a73e8>作者：</font>** Nadav Orenstein, Aviad Cohen Zada, Shai Avidan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Texture segmentation stresses foundation segmentation because meaningful regions are defined by material or repeated appearance rather than object identity. Segment Anything Models (SAMs) often fail by default on such texture-defined partitions, but this failure is ambiguous: the texture evidence may be absent, missing from the proposal bank, or present but selected or assembled incorrectly by an object-centric readout. We ask what texture-relevant evidence is already preserved in frozen SAM before adaptation. We study two frozen evidence spaces: multiscale features, probed with a minimal clustering readout, and the automatic proposal bank, treated as evidence for a supervised consolidation readout. SAM is frozen throughout; we do not fine-tune the backbone or retrain the proposal generator. Across RWTD, STLD, an ADE20K-selected refined-crop complement, and a ControlNet-stitched PTD bridge archive, frozen SAM is not a texture segmenter by default, but its failures are not simple texture blindness. Coarse frozen features preserve texture organization, and proposal banks often contain texture-aligned masks or fragments. Natural scenes more often require assembly and commitment over fragments, while cleaner synthetic cases more often reduce to selecting an already coherent proposal. Default mask failure should therefore be decomposed into representation evidence, proposal-bank support, readout mismatch, and commitment failure.

---


### 18. [Divide-and-Denoise: A Game-Theoretic Method for Fairly Composing Diffusion Models](https://arxiv.org/abs/2606.14756)

**<font color=#1a73e8>作者：</font>** Abhi Gupta, Polina Barabanshchikova, Vikas Garg 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The abundance of pre-trained diffusion models provides an opportunity for composition. Combining several models, however, runs the risk of one model dominating or models disagreeing with each other. Here, we propose Divide-and-Denoise, a method for coordinating multiple pre-trained diffusion models during sampling. Much like managing a specialized workforce, our method creates a fair but efficient division of labor across models. Central to our method is the notion of an allocation which defines the responsibility of each model to every region of the noisy sample. At every timestep, we then denoise by (i) updating the allocation by solving a fair division game, where we divide the sample into regions that maximize total utility under fairness constraints, and (ii) aligning the models with this allocation, where we guide each model to denoise within its assigned region. This leads to a new composite denoising process that evolves in tandem with a division process. We evaluate Divide-and-Denoise on conditional image generation. Across several quality metrics, including the GenEval benchmark, our method outperforms baselines and resolves common failures including missing objects and mismatched attributes. Experiments show that Divide-and-Denoise utilizes each model's expertise without neglecting any other model.

---


### 19. [Spatial Priors via Space Filling Curves for Small and Limited Data Vision Transformers](https://arxiv.org/abs/2606.14757)

**<font color=#1a73e8>作者：</font>** Leyla Naz Candogan, Arshia Afzal, Pol Puigdemont 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Though Vision Transformers (ViTs) have become the dominant backbone in many computer vision tasks, due to permutation equivariance, their attention mechanism lacks explicit spatial inductive biases. This become particularly important in two settings: when model capacity is small or training data is limited. Inspired by the attention masking strategies in Linear Transformers and the scanning patterns of Vision SSMs, we introduce VIOLIN, a lightweight masked attention mechanism that encodes spatial structure within attention via Space Filling Curves (SFCs) with less than 0.0015% extra parameters and negligible computational overhead. VIOLIN scans the image using multiple SFCs to construct curve-specific decay masks, which are then combined and multiplied with the attention matrix. Across a wide range of evaluations, VIOLIN consistently improves performance. In limited data regimes such as fine-tuning on VTAB-1K, it boosts accuracy across all task groups and by up to 8.7% on the tasks where spatial information is essential. It can be combined with parameter-efficient fine-tuning methods such as LoRA to further increase the performance. Beyond fine-tuning, VIOLIN improves various small scale ViT architectures (e.g., DeiT, DINO) during pretraining on ImageNet-1K. Additionally, on pixel-level CIFAR-100 training, a task that is highly dependent on location information, VIOLIN increases accuracy by up to 7.2%. Overall, VIOLIN provides a computationally efficient yet effective way to inject spatial inductive bias into ViTs, especially benefiting small models and limited data settings.

---


### 20. [Disentangling Hallucinations: Orthogonal Semantic Projection for Robust Interpretability](https://arxiv.org/abs/2606.14758)

**<font color=#1a73e8>作者：</font>** Emirhan Bilgiç, Baptiste Caramiaux, Zhi Yan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As Vision-Language Models are increasingly deployed in safety-critical applications, the trustworthiness of their explanations becomes crucial. Explainable AI (XAI) methods for Vision-Language Models often suffer from semantic hallucination, where attribution maps highlight prominent image regions even when prompted with incorrect text descriptions (e.g., highlighting a dog when prompted ``cat''). Although this problem is widespread, a formal mathematical analysis of XAI methods and CLIP embeddings is largely missing in the literature. We demonstrate that this phenomenon is not specific to a single architecture but is a fundamental consequence of Linear Semantic Leakage in high-dimensional embedding spaces. We propose a unified theoretical framework, Linear Semantic Attribution (LSA), which generalizes across discriminative methods. We introduce OSP, a geometric intervention that utilizes the residual property of OMP to disentangle unique semantic signals from shared concepts. We prove theoretically and demonstrate empirically that OSP minimizes hallucination by orthogonalizing the query vector against distractor concepts, rendering the attribution model blind to shared features while preserving fidelity for correct prompts. Our code is available at: this https URL

---


### 21. [Temporally Consistent and Controllable Video Generation of 2D Cine CMR via Latent Space Motion Modeling](https://arxiv.org/abs/2606.14759)

**<font color=#1a73e8>作者：</font>** Yiheng Cao, Gustavo Andrade-Miranda, Jiatian Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cine cardiac magnetic resonance is the gold standard for assessing cardiac function, but the scarcity of public datasets limits the development of advanced data-driven models. To address this limitation, we propose a generative method for synthesizing temporally coherent and anatomically consistent cardiac sequences. Our text-to-video framework decouples cardiac spatial structure from temporal motion. First, a fine-tuned diffusion model synthesizes an initial frame from a clinical text prompt, controlling anatomical features. Then, a latent flow model conditioned on a cardiac phase embedding generates the complete cardiac motion, ensuring spatial consistency and temporal control. Our model generates anatomically and pathologically diverse sequences with high temporal coherence and strong fidelity to input prompts, achieving a FID of 31.68 for image realism and a CLIP score of 31.04 for text-image alignment. These experimental results highlight its potential to produce high-fidelity, on-demand medical data, offering a scalable solution to data scarcity.

---


### 22. [Avoiding Exponential Blow-Up in Distributive Lattice Submodular Minimization](https://arxiv.org/abs/2606.14764)

**<font color=#1a73e8>作者：</font>** Ishant Shanu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Submodular function minimization has gained a lot of interest in recent years. They are highly applicable in the area of Computer Vision and Machine Learning. Often such applications require to work with submodular functions defined on distributive lattice. Current best way of dealing with it is using a transformation which extrapolates the submodular function for the respective boolean lattice. It makes optimization system too inefficient due to enlargement of the working space. Quantitatively, the expanded space has additional exponential (in set size) number of elements. We propose a generic framework for dealing with distributive lattice which only works within distributive lattice. Our framework allows one to use already established submodular function minimization algorithms for boolean lattice. In our experiment, we show the huge improvement in terms of running time over tranditional methods for handling distributive lattice.

---


### 23. [Momentum-Guided Semantic Forecasting (MoFore) for Self-Supervised Video Representation Learning](https://arxiv.org/abs/2606.14765)

**<font color=#1a73e8>作者：</font>** Qinwu Xu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised video representation learning has recently advanced through contrastive learning, masked reconstruction, and predictive representation learning. Reconstruction-based approaches such as MAE and VideoMAE learn representations by recovering masked visual content \cite{he2022mae,tong2022videomae}, while contrastive methods such as CLIP learn semantically meaningful embedding spaces through representation alignment \cite{radford2021clip}.
In this work, we introduce a Momentum-Guided Semantic Forecasting framework (MoFore) for self-supervised video representation learning. Instead of optimizing for pixel-level reconstruction or task-specific semantic alignment, the proposed method learns temporally predictive video representations by forecasting future latent embeddings from temporally distant context clips. To improve robustness across temporal scales, we further introduce randomized temporal-gap forecasting during training. The framework combines predictive latent forecasting with contrastive regularization to encourage temporal consistency while preventing representation collapse.
Experiments on the UCF101 dataset demonstrate that the proposed framework learns temporally consistent and semantically meaningful video representations without using action labels during training. Quantitative analysis shows strong temporal stability and emergent category-level structure in the learned embedding space, while qualitative retrieval experiments reveal motion-aware organization across related activities. Overall, the results suggest that long-range latent forecasting provides an effective and computationally efficient approach for self-supervised video representation learning without relying on reconstruction-based objectives.

---


### 24. [An Empirical Analysis of Optimization Dynamics and Sparsity Boundaries in Large-Scale Pedestrian Attribute Recognition](https://arxiv.org/abs/2606.14770)

**<font color=#1a73e8>作者：</font>** Houssam El Mir  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pedestrian Attribute Recognition (PAR) is critical for video surveillance, enabling forensic search and re-identification systems. Extreme class imbalance remains a fundamental obstacle when merging PETA and PA-100K into a 109,000-image composite corpus, where minority attributes have positive sample fractions below 1%. This causes standard BCE optimization to suppress rare traits, a phenomenon we term the majority negative class cheating trap. We present a systematic ablation of Multi-Label Focal Loss hyperparameters (alpha and gamma) on a ResNet-18 backbone. A calibrated configuration (alpha=0.50, gamma=2.0) achieves a Macro F1-score of 62.32%, matching BCE baseline while preserving superior hard-example mining and convergence dynamics. Our approach uses pure loss-function engineering with zero computational overhead for edge deployment. We identify the Sparsity Wall, a hard boundary where positive sample fractions below 0.1% make global loss reweighting ineffective, requiring instance-level intervention.

---


### 25. [ScoutVLA: UAV-Centric Active Perception via a Dual-Expert VLA Model for Open-World Embodied Question Answering](https://arxiv.org/abs/2606.14772)

**<font color=#1a73e8>作者：</font>** Wenhao Lu, Zhengqiu Zhu, Xiaofeng Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aerial Embodied Question Answering (EQA) requires Unmanned Aerial Vehicles (UAVs) to actively perceive the environment and answer natural language questions. Existing outdoor EQA systems usually stop once the target enters the UAV's field of view, leaving the fine-grained viewpoint adjustment needed for evidence-seeking questions largely unresolved. To address this issue, we introduce FG-EQA, a fine-grained active perception EQA benchmark with more than 40K simulated trajectories and 1K real-world trajectories. Drawing inspiration from the ``waggle dance'' of scout bees, which iteratively adjust their flight paths to verify target information, we propose ScoutVLA, an evidence-driven Vision-Language-Action model for outdoor EQA. To emulate this active exploration behavior, ScoutVLA features a decoupled dual-expert architecture: a vision-language expert infers the semantic intent to identify missing evidence, while an independent action expert employs high-DoF flow matching to generate continuous viewpoint-refinement trajectories. To balance the competing demands of continuous control and semantic reasoning, we devise a decoupled training strategy with a knowledge insulation mechanism that prevents the action gradients from erasing the model's multimodal reasoning ability. Extensive simulated experiments and a qualitative real-world field study both verify the superiority of ScoutVLA over the state-of-the-art baselines, demonstrating a 10.48$\boldsymbol{\times}$ higher average strict success rate and a 7.72$\boldsymbol{\times}$ higher average QA correctness.

---


### 26. [Double-Helix Vision (DH-V2): A Geometry-Based Visual Sampler for Bandwidth-Constrained Perception](https://arxiv.org/abs/2606.14773)

**<font color=#1a73e8>作者：</font>** Jinwen Wen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Double-Helix Vision (DH), a geometry-based visual sampler that compresses 2D images into compact 1D signals using paired golden-ratio-inspired spiral trajectories. Rather than processing every pixel uniformly, DH employs two phase-shifted helices (Alpha and Beta, offset by 180 degrees) to sample the image with biologically-inspired foveation: high density at the center, sparse coverage at the periphery. At 4K resolution, DH achieves a 1,433x compression ratio (99.93% reduction) while preserving the geometric structure of the scene. The full perception pipeline -- including spatial mapping, temporal collision detection, and intra-frame structural disparity estimation -- runs in 0.52 ms at 1080p on CPU-only hardware, with no neural network dependencies. On CIFAR-10 at extreme sampling budgets (K=128 points per helix), DH achieves a +6.03% accuracy gain over uniform random sampling. A JSON-serializable Robotics API is provided, delivering sub-millisecond spatial perception reports in 2.7 KB packets. Code and benchmarks are available under the MIT License.

---


### 27. [JoyAI-VL-Interaction: Real-Time Vision-Language Interaction Intelligence](https://arxiv.org/abs/2606.14777)

**<font color=#1a73e8>作者：</font>** Dingyu Yao, Junhao Zhou, Chenxu Yang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many moments in the real world do not wait for a user to ask. A fire starts on a security monitor, an expression flickers across a video call, or a product a viewer wants flashes by in a livestream. Yet today's large models remain mostly turn-based by design: they answer only when addressed, and even video-call apps that appear interactive still operate as question-answer systems, reacting only when polled or prompted. We argue for a different paradigm: a model that is present in the world like a person. It continuously watches what is happening now, decides on its own whether to speak or stay silent, interacts in real time, and delegates to a background model when the problem is hard. To advance interaction models and their adoption across domains, we make two fully open-sourced contributions. First, we release JoyAI-VL-Interaction, an 8B-scale, vision-first VL-interaction model. The model makes the response decision internally, choosing each second to stay silent, respond, or delegate to a background model, and it excels at vision-triggered responsiveness and time awareness. We pair it with a transferable training recipe, from which capabilities we never trained for emerge, such as guiding a shopper through changing app screens or improvising a lecture from a slide deck. Second, we release a complete, deployable system built around that model. The system streams any ongoing video into the model, making it genuinely present in the world. All other components are pluggable, including ASR/TTS modules, memory, visualization UI, and a background brain that can connect to any API or agent. Across six real-world scenarios, human raters prefer JoyAI-VL-Interaction over the in-app video-call assistants of Doubao and Gemini by a wide margin. To our knowledge, this is the first open, vision-driven interaction model released together with its training recipe, data, and complete deployable system.

---


### 28. [FactCheck: Feasibility-aware Long-term Action Anticipation with Multi-agent Collaboration](https://arxiv.org/abs/2606.14778)

**<font color=#1a73e8>作者：</font>** Rui Cao, Jiannong Cao, Bo Yuan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-term action anticipation (LTA) aims to predict an ordered sequence of future verb-noun actions from a partially observed video. While this task serves as the foundation for embodied intelligence, anticipating physically feasible long-term actions remains a critical challenge. Existing methods, which operate in an open-loop manner, often hallucinate non-existent objects, violate object affordances, or disregard object states, as they lack explicit mechanisms to verify action feasibility against the physical environment. To address this, we propose FactCheck, a novel multi-agent collaboration framework that improves feasibility through a closed-loop "Observe-Plan-Verify" mechanism. FactCheck decomposes the complex LTA task into specialized roles: an Observer that recognizes historical actions from video observations and constructs a dual-form structured memory, comprising a History Action Abstract that captures high-level human intentions and environmental status, and a History Action Graph that encodes object states and temporal dependencies; a Planner that generates draft future actions conditioned on both low-level historical actions and high-level History Action Abstract; and a Verifier that rigorously validates the draft against the History Action Graph and refines infeasible actions. Extensive experiments on the EPIC-Kitchens-55 and EGTEA Gaze+ benchmarks demonstrate that FactCheck consistently outperforms state-of-the-art methods. Our work establishes a new paradigm for feasibility-aware long-term action anticipation, effectively closing the loop of action recognition, action prediction and action verification.

---


### 29. [Variational Deep Unfolding with Mamba-Based Nonlocal Modeling for Underwater Image Enhancement](https://arxiv.org/abs/2606.14781)

**<font color=#1a73e8>作者：</font>** Daniel Torres, Julia Navarro, Catalina Sbert 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Underwater imaging plays a crucial role in ocean engineering, although captured data often suffer from poor visibility and color distortion. To address these challenges, we propose a model-based deep unfolding network for underwater image enhancement that integrates variational modeling into a learnable architecture. The framework is guided by a variational formulation based on a dehazing decomposition, incorporating a multiplicative residual component to absorb remaining artifacts and a nonlocal gradient-type constraint to preserve structural details and enhance edge sharpness. We provide a theoretical analysis establishing the existence of solution for the associated minimization problem. The proposed unfolding method incorporates Mamba layers to efficiently capture self-similarities in the scene. In addition, we introduce a proximal trajectory loss that enforces consistency between the unfolding stages and the iterations of an ideal restoration regularizer. Experimental results demonstrate that the proposed unfolding approach achieves improved visual quality and competitive quantitative performance compared with recent state-of-the-art methods. The source code will be available at this https URL .

---


### 30. [Vision-Encoder Behavioral Fingerprints of Image-to-Image Generative Models: A Training-Paradigm-Driven Taxonomy of Six Commercial APIs](https://arxiv.org/abs/2606.14787)

**<font color=#1a73e8>作者：</font>** Hunter Hill  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study six production image-to-image AI systems (gpt-image-1, Gemini 2.5 Flash Image, Flux Kontext, SDXL img2img, SD3 img2img, and Qwen Image Edit) under a content-adaptive sub-JND adversarial perturbation pipeline, scoring all outputs by frozen DINOv2 ViT-B/14 token distances against clean references. Across a 3,588-call corpus spanning COCO photographs, CelebA-HQ portraits, and AI-generated inputs, the six systems partition into two image-invariant behavioral bands on a 2D (patch_mean, ssim_clean) plane: edit-trained models (Flux Kontext, Qwen Edit, Gemini) cluster in a tight band, while T2I-base models adapted at sampling time (SDXL, SD3, gpt-image-1) cluster in a drift band.

---


### 31. [Efficient Reinforcement for Visual-Textual Thinking with Discrete Diffusion Model](https://arxiv.org/abs/2606.14792)

**<font color=#1a73e8>作者：</font>** Yoonjeon Kim, Yuhta Takida, Chieh-Hsin Lai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> RL-based post-training has been widely adopted to enable interleaved visual and textual reasoning in unified multimodal models capable of both text and image generation. However, most existing approaches are built upon autoregressive (AR) unified models, which require full image regeneration during visual reasoning. In this work, we demonstrate that multimodal discrete diffusion models are effective alternatives to AR models for reinforcement learning in interleaved reasoning, owing to their ability to perform efficient visual rollouts via localized visual editing rather than full image-token regeneration. This reduces rollout computation during GRPO by 26.9\% compared to AR baselines, with minimal performance drop. Despite the improved efficiency, we find that joint reward assignment, which employs a shared reward signal across modalities, introduces cross-modal interference between unrelated image and text token sequences during RL updates. To address this issue, we propose factorized reward assignment, a strategy that assigns rewards independently to text and vision segments. With factorized reward assignment, our RL approach achieves an 11.2% improvement over joint reward assignment and a 38.04% improvement over the base model.

---


### 32. [Position: The Systemic Lack of Agency in Visual Reasoning](https://arxiv.org/abs/2606.14795)

**<font color=#1a73e8>作者：</font>** Yizhao Huang, Haoyang Chen, Shiqin Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper argues that a systemic lack of Agency constrains the implicit reasoning capabilities of current Vision-Language Models (VLMs). Implicit reasoning refers to the ability to autonomously discover and utilize hidden visual evidence to bridge information gaps, rather than merely relying on explicitly specified targets. This capacity underlies human visual understanding and everyday reasoning. We argue that this limitation arises from a tendency to approach visual reasoning primarily as passive semantic retrieval, rather than as active, situated reasoning that depends on autonomous visual exploration. As a result, most existing benchmarks primarily assess Passive Capacity, leaving this aspect of reasoning largely unmeasured. To address this gap, we introduce the Visual Implicit Reasoning Diagnosing Benchmark (V-IRD), which targets this missing quadrant by requiring models to derive answers strictly through autonomous visual analysis. Our results show that, despite strong retrieval abilities, prominent VLMs struggle to utilize reference objects and to attend to visual evidence that requires self-directed inquiry. Simply put, strong semantic recognition does not equate to active visual exploration, revealing a critical gap in current VLMs. More information can be found at this https URL

---


### 33. [QPILOTS: Efficient Test-Time Q-Steering for Flow Policies](https://arxiv.org/abs/2606.14801)

**<font color=#1a73e8>作者：</font>** Yifan Ruan, Chenyang Cao, Andreas Burger 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow-matching and diffusion policies are expressive action generators, but optimizing them with temporal-difference reinforcement learning (RL) remains difficult. Effective policy extraction requires exploiting the critic's action gradient, yet directly backpropagating this signal through a multi-step denoising process can be numerically unstable. Existing methods work around this either by discarding gradient information, distilling the policy into a simpler one-step actor, or repeatedly fine-tuning the denoising policy as the critic improves. We propose QPILOTS, a method that leaves the original policy unmodified and steers the denoising process at inference time. At each denoising step, instead of evaluating the critic on the noisy intermediate action where critic predictions are unreliable, we first project that intermediate state to an estimate of the final clean action and compute the critic gradient there. We introduce two variants: QPILOTS-U uses a fast single-point approximation, while QPILOTS-M draws differentiable posterior samples via a learned auxiliary network. On a standard offline-to-online RL benchmark, QPILOTS achieves the best aggregate performance, reaching an average success rate of 90% across 50 tasks. We also apply QPILOTS to steer a large, frozen, pretrained Vision-Language Action (VLA) foundation model, outperforming or matching prior inference-time approaches across six manipulation tasks in simulation.

---


### 34. [HSQ-VLM: A Novel Spatially-Constrained Quadrant Segmentation VLM Model for Explainability in Diabetic Retinopathy](https://arxiv.org/abs/2606.14803)

**<font color=#1a73e8>作者：</font>** Shivum Telang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diabetic Retinopathy (DR) is an aggressive retinal disease and a leading cause of global blindness, yet its clinical management is currently hindered by the black-box nature of diagnostic AI. While deep learning models achieve high classification accuracy, there is a critical lack of explainability methods capable of detailing the exact anatomical landmarks and lesion distributions that lead to a clinical decision for DR. Therefore, we propose HSQ-VLM, a novel quadrant segmentation pipeline on fundus images that utilizes a Landmark-Anchored Cartesian Cross-Attention mechanism to unify visual feature extraction with structured clinical reasoning. Unlike traditional methods that rely on arbitrary image partitioning, our pipeline implements 4-quadrant Topological Latent Partitioning (TLP) to dynamically align retinal features with a fovea-centered coordinate system. This allows the Vision-Language Model to generate natural language reports that quantify pathology with anatomical precision. On a dataset of 3,500 high-resolution fundus images, this innovative methodology achieved a lesion detection sensitivity of 99.6% for hemorrhages and 96.4% for microaneurysms, while demonstrating a significant reduction in boundary-ambiguity errors compared to standard segmentation baselines.

---


### 35. [S23DR 2026: End-to-End 3D Wireframe Prediction via DETR-Style Set Prediction with Contrastive Denoising](https://arxiv.org/abs/2606.14811)

**<font color=#1a73e8>作者：</font>** Nitiz Khanal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present WireframeDETR, our submission to the Structured Semantic 3D Reconstruction (S23DR) 2026 Challenge, which requires predicting a 3D building wireframe from multi-view COLMAP point clouds. Our method applies DETR-style set prediction directly to 3D point clouds, producing wireframes as sets of edge coordinate pairs without any intermediate vertex detection stage. We introduce three technical contributions: (1) contrastive denoising training that stabilises noisy Hungarian matching in early epochs; (2) a multi-scale encoder that aggregates the last encoder layer outputs via learned scalar weights; and (3) progressive auxiliary loss weighting that concentrates gradient signal on the decoder layers that most benefit from it. Our model achieves a public test HSS of 0.575 (F1~=~0.664, IoU~=~0.516) and a best validation HSS of 0.534 on the cleaned val split.

---


### 36. [Selective Control under Noisy Perception: Governance Failures Hidden by Aggregate Metrics in Modular Networks](https://arxiv.org/abs/2606.14819)

**<font color=#1a73e8>作者：</font>** Igor Itkin  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> A content-moderation system can score well on every standard accuracy metric and still cause real harm, if its mistakes fall on the few users who connect otherwise separate communities. We show this in an agent-based model where N=240 learning agents on a community-structured network each post harmless, productive, or dangerous content, and a regulator removes or penalizes whatever a noisy classifier flags. Overall usefulness barely moves as the noise changes (one-way ANOVA, p=0.96): by aggregate measures, nothing looks wrong. The damage instead concentrates on these bridge users, whose useful posts are wrongly suppressed and whose dangerous posts are wrongly spared. A governance loss (L_gov) that prices these two mistakes separately from the cost of enforcement more than doubles under false-positive-heavy noise. Aggregate accuracy hides who is harmed, and the cheap quantity to audit is how many connections a user has (degree), a near-perfect proxy for the betweenness that defines a bridge (r=0.96).

---


### 37. [PhoneHarness: Harnessing Phone-Use Agents through Mixed GUI, CLI, and Tool Actions](https://arxiv.org/abs/2606.14832)

**<font color=#1a73e8>作者：</font>** Chenxin Li, Zhengyao Fang, Zhengyang Tang 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Phone agents are increasingly expected to complete real mobile workflows rather than merely predict the next screen action. However, much of the current mobile-agent literature still evaluates agents primarily as GUI controllers that observe a screen, emit taps and swipes, and are scored by target app state. Real phone-use tasks are broader: they require deciding when to use app GUIs, device-side commands, or structured tools, while leaving evidence that the intended side effect actually occurred. We introduce PhoneHarness, a mixed-action benchmark and execution harness for studying phone-use agents on verifiable mobile workflows. PhoneHarness runs a device-side agent loop over GUI, CLI, and host-side tool actions, combining deterministic action routing with bounded GUI delegation and auditable execution traces. Its benchmark, PhoneHarness Bench, evaluates whether agents complete tasks with observable side effects, not only whether they produce plausible final answers. On the annotated evaluation split, PhoneHarness reaches a 75.0% pass rate, outperforming the strongest non-PhoneHarness settings by 12.9 percentage points. PhoneHarness and PhoneHarness Bench therefore play distinct but mutually dependent roles: the harness makes mixed phone workflows executable, while the benchmark measures whether agents can use that harness reliably and safely. Our findings suggest that reliable phone automation depends on action-surface routing and verifiable execution, not only visual GUI control.

---


### 38. [Multi-HMR 2: Multi-Person Camera-Centric Human Detection, Mesh Recovery and Tracking](https://arxiv.org/abs/2606.14841)

**<font color=#1a73e8>作者：</font>** Guénolé Fiche, Philippe Weinzaepfel, Romain Brégier 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most advances in human mesh recovery (HMR) have focused on pelvis-centered recovery, overlooking metric 3D localization and detection accuracy in the camera coordinate system - two key factors for real-world applications such as human-robot interaction and social scene understanding. Current evaluation protocols often ignore these aspects, emphasizing per-person, root-centered recovery rather than camera-space perception. As a result, existing approaches rely on fixed camera assumptions or handcrafted post-processing, limiting their robustness and practical deployment. We introduce Multi-HMR 2, a simple yet robust DETR-based framework for Multi-person Camera-centric Human detection, mesh Recovery, and tracking. Multi-HMR 2 predicts a scene-consistent camera together with human meshes, enabling metric 3D localization without ground-truth intrinsics. Moreover, by distilling image-based memory features from SAM2, Multi-HMR 2 extends to tracking, achieving consistent identity association without video supervision. Despite its conceptual simplicity - no handcrafted components, no video input, and no ground-truth cameras - Multi-HMR 2 achieves state-of-the-art pelvis-centered performance while substantially improving detection accuracy and metric 3D localization.

---


### 39. [GRAPE: Guided Parameter-Space Evolution for Compact Adversarial Robustness](https://arxiv.org/abs/2606.14865)

**<font color=#1a73e8>作者：</font>** Zhiyuan Ye, Xiangyu Zhou, Ji Qi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adversarial Training (AT) improves neural network robustness, but most methods train a fixed parameter space from the start. This paper asks whether the order in which parameters become optimizable can affect the final robust solution, even when the final architecture or computation budget is controlled.
We propose GRAPE, Guided Parameter-Space Evolution, a training framework for compact adversarial robustness. GRAPE combines parameter-space stabilization with progressive hidden expansion: it stabilizes robust optimization in the currently exposed space, gradually releases new optimizable dimensions, and uses an adversarial spectral utilization score to guide newly released capacity toward high-pressure modules. In contrast to fixed-structure AT, GRAPE treats robust model learning as a process of progressive parameter-space exposure and evolution.
Under the standard $\ell_\infty$ threat model on CIFAR-10, with fixed-structure ResNet-18 AT as a controlled reference, GRAPE improves PGD-20 robust accuracy from 51.70% to 56.94% at a nearly matched computation budget with a FLOPs ratio of 1.009x, while reducing parameter count by about 21.4%. A sequential grow variant with the same final ResNet-18 architecture reaches 56.52% PGD-20 robust accuracy, indicating that the gain is not only due to final architecture differences but also to the parameter-space exposure path. These results suggest that guided parameter-space evolution can yield compact and robust parameter configurations under matched computation.

---


### 40. [Evaluating the Robustness of Proof Autoformalization in Lean 4](https://arxiv.org/abs/2606.14867)

**<font color=#1a73e8>作者：</font>** Zhengtao Gui, Sheng Yang, Zhouxing Shi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Proof autoformalization aims to translate a mathematical informal proof written in natural language into a formal proof in a formal language such as Lean~4. Several works have developed LLM-based models for proof autoformalization. However, existing evaluations have typically focused on translating well-formed informal proofs from curated datasets. We argue that a robust proof autoformalizer must remain faithful even for informal proofs that diverge from these idealized ones, and we present the first study on the robustness of proof autoformalization models. We formulate two categories of perturbations and evaluate robustness under each: a global perturbation paraphrases the informal proof in a different style, under which the formalization should remain consistent; a local perturbation alters a value, symbol, or proof step, possibly in a counterfactual way, and a robust formalization should faithfully reflect the perturbation rather than reverting to the original one or inferring a different one on its own. We build a benchmark with both perturbations on miniF2F and MATH-500, and automatically measure how stable a proof autoformalization's correctness is under global perturbations and how faithfully its output reflects local perturbations. We evaluate seven recent models, all of which are sensitive to global perturbations and mostly fail to remain faithful under local perturbations. Code and data are available via this https URL.

---


### 41. [An Ensemble Deep Learning Approach for Reliable and Scalable Lemon Leaf Disease Classification](https://arxiv.org/abs/2606.14871)

**<font color=#1a73e8>作者：</font>** Shayan Abrar, Sudeepta Mandal, Abdul Awal Yasir 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Early detection of plant diseases is crucial to plants and for the farmers. Plant diseases reduce fruit yield and quality, and plants are more susceptible to other stresses when they are infected. The lemon leaf disease dataset contains 1354 images. The dataset has 9 classes. Among the 9 classes only one class is for healthy leaf, and the other 8 classes are leaf diseases. The dataset was split into training (70%), testing (15%) and validation (15%) sets after comprehensive preprocessing. Two pretrained models (InceptionV3 and MobileNetV2) were applied and then combined these models using an ensemble technique to boost robustness. Ensemble models showed a promising performance of 99.27% accuracy. Adversarial Training is applied to improve models' ability and ensure reliable predictions under noisy data. Grad-CAM visualization highlights the important regions of leaf images that validate the model prediction with confidence level.

---


### 42. [Context Compression Is Not One Thing: Readable Symbolic Re-expression vs. Coherent Summary at Matched Budget](https://arxiv.org/abs/2606.14875)

**<font color=#1a73e8>作者：</font>** Sisong Bei, Mikhail L. Arbuzov, Ziwei Dong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study context compression for multi-hop question answering with small language models. We propose Telegraph English, a readable symbolic format that rewrites retrieved passages into structured entity-relation statements, preserving reasoning evidence at lower token cost. In controlled experiments on MuSiQue, TwoWiki, and HotpotQA, Telegraph English outperforms three matched-budget compression baselines (character-level deletion, truncation, and random sub-sampling) on every dataset, with gains of 13 to 20 F1 percentage point. It also outperforms a coherent prose summary produced by the same encoder on the hardest dataset. A pre-registered depth-interaction hypothesis is null: the advantage does not grow with reasoning depth within datasets. We interpret these results as evidence that readable symbolic re-expression preserves entity content more densely than either natural language or coherent summarization at matched token budget.

---


### 43. [Dr-DCI: Scaling Direct Corpus Interaction via Dynamic Workspace Expansion](https://arxiv.org/abs/2606.14885)

**<font color=#1a73e8>作者：</font>** Yi Lu, Zhuofeng Li, Ping Nie 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic search over large corpora relies on retriever-mediated interfaces (e.g., BM25 or ColBERT) for scalable candidate discovery. While effective at ranking relevant documents, these interfaces expose evidence only as ranked results or bounded document views, limiting agents' ability to reorganize material and verify constraints across documents. Direct Corpus Interaction (DCI) addresses this limitation by exposing shell-executable corpus operations for flexible search, filtering, comparison, and verification. However, full-corpus terminal commands become slow and unstable as the corpus grows, degrading performance and efficiency. We introduce DR-DCI, a retriever-steered DCI framework that treats retrieval as an agent-callable action for expanding a local workspace. Rather than operating directly over the full corpus, the agent dynamically pulls relevant documents into an evolving workspace and conducts DCI operations within it. This design combines retriever-level recall with DCI-style precision: retrieval keeps exploration scalable, while DCI preserves the local operations needed for effective evidence resolution. Experiments show that DR-DCI is both effective and efficient across scales. On Browsecomp-Plus, DR-DCI reaches 71.2\% accuracy, improving over raw DCI and ablated variants by up to 8.3 points while reducing tool usage, wall time, and estimated cost. With workspace-preserving context reset, accuracy further improves to 73.3\%. In corpus-scaling experiments, DR-DCI remains effective from 100K to 10M documents, whereas raw DCI becomes unstable and BM25 performs substantially worse. DR-DCI also scales to a 20M-scale file-per-document Wiki-18 QA setting, achieving an average score of 63.0 across six benchmarks and outperforming retrieval-based and trained search-agent baselines. Ablation analysis further shows that ranked previews and inter-document DCI are key to performance.

---


### 44. [Improved Knowledge Distillation for Land-Use Image Classification](https://arxiv.org/abs/2606.14886)

**<font color=#1a73e8>作者：</font>** Arundhuti Sur, Abhiroop Chatterjee, Susmita Ghosh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In the present article, an improved Knowledge Distillation (KD) framework has been proposed for efficient compression of deep convolutional neural networks for land-use image classification task. Motivated by the need to achieve competitive classification accuracy while reducing computational complexity, a teacher-student learning paradigm is adopted in which a VGG16 network transfers knowledge to a lightweight MobileNetV2 model. The proposed framework integrates hard supervision from ground truth labels with a soft supervision strategy that combines Kullback-Leibler divergence and Cosine Similarity losses. Experiments conducted on three land-use datasets show that the proposed KD-based method yields improved performance, and achieves an accuracy of 99.04%, outperforming both baseline student training and single-loss distillation approaches, while retaining substantial model compression.

---


### 45. [Relational Structural Causal Models](https://arxiv.org/abs/2606.14892)

**<font color=#1a73e8>作者：</font>** Adiba Ejaz, Elias Bareinboim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An artificial intelligence must have a model of its environment that is causal, supporting reasoning about interventions and counterfactuals, and also combinatorial, supporting generalization to unseen combinations of objects. In this work, we formally study when and how such a model can be learned. We develop relational structural causal models, extending structural causal models (Pearl 2009) to settings where objects and their relations vary. First, we show how answers to not only causal but also observational queries about unseen combinations of objects can not be identified without further assumptions. To enable such identification--including in the presence of unobserved confounding--we define relational causal graphs and derive symbolic identification criteria. Finally, we propose relational neural causal models, a provably correct approach that outperforms non-relational baselines on simulated traffic scenes with varying cars, signals, and pedestrians.

---


### 46. [Automated Gaze-based Behavioral Segmentation and Temporal Representation for Bridge Inspection in Unconstrained 3D Environments](https://arxiv.org/abs/2606.14893)

**<font color=#1a73e8>作者：</font>** Daniel Jimenez Gil, Haosen Zhang, Zixin Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Visual bridge inspection is a knowledge-intensive task in which inspectors coordinate visual search, spatial navigation, structural reasoning, and defect identification and documentation. It is a central maintenance task for bridges and a key basis for safety assessments, yet its results are susceptible to individual subjectivity. While eye-tracking-based behavioral studies quantify underlying processes, existing research often imposes restrictive simplifications to reduce environmental complexity, thereby compromising ecological validity. This study proposes an automated data analytics framework for converting multimodal inspection data into an inspection mode time series. Unconstrained 3D gaze, head-movement, drone navigation, and scene geometry data are segmented into temporal windows and classified into three functional modes: global scanning, local inspection, and navigation. The resulting temporal representation enables the extraction of interpretable behavioral descriptors, including transition probabilities, dwell times, transition entropy, fixation measures, and spatial revisit metrics. A feasibility study using a virtual bridge inspection platform demonstrates that the proposed representation captures meaningful differences in inspection strategy and reveals exploratory relationships with inspection performance. This study contributes a framework for human-informed computer-aided infrastructure inspection systems, inspector training, and data-driven assessment of constructed facilities.

---


### 47. [α-Fair Insurance Pricing: A Fairness Continuum](https://arxiv.org/abs/2606.14898)

**<font color=#1a73e8>作者：</font>** Tianhe Zhang, Xiguang Liu, Peng Shi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fairness in insurance pricing remains a long-standing and deeply debated puzzle. On one hand, insurers, driven by profitability considerations, set premiums that differentiate across individual risks to achieve actuarial fairness. On the other hand, insurance serves a critical societal function by pooling risks across a population, motivating cross-subsidization among groups to promote solidarity fairness. The tension between these two competing notions of fairness makes insurance pricing inherently complex, particularly in modern settings where granular data allow for increasingly fine risk differentiation and regulators face growing pressure to protect vulnerable groups. To address this challenge, we propose an $\alpha$-\textbf{F}air \textbf{I}ndividual \textbf{S}olvent \textbf{P}remium ($\alpha$-FISP) framework for insurance pricing that explicitly captures the trade-off between actuarial and solidarity fairness while guaranteeing solvency, a fundamental requirement in insurance operations. We formulate the pricing problem as a constrained optimization task, where actuarially fair premiums are adjusted subject to budget constraints on cross-subsidization within each risk class. This formulation naturally yields a family of solutions parameterized by $\alpha$, tracing a continuum between purely actuarial and purely solidarity-based pricing and enabling decision-makers to select an operating point along this fairness spectrum. We derive theoretical guarantees for the proposed framework. Numerical experiments show that $\alpha$-FISP is computationally tractable and aligns well with the U.S. regulatory regimes featuring heterogeneous state-level fairness requirements.

---


### 48. [GRASP: Gradient-Aligned Sequential Parameter Transfer for Memory-Efficient Multi-Source Learning](https://arxiv.org/abs/2606.14900)

**<font color=#1a73e8>作者：</font>** Mary Isabelle Wisell, Nicholas Jacobs, Aayush Manandhar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-source transfer learning faces a fundamental scalability bottleneck: existing approaches require either loading all K source models into memory simultaneously during parameter fusion, requiring O(K) memory, or deploying all models at inference time, making production deployment infeasible. We propose GRASP (Gradient-Aligned Sequential Parameter Transfer), which achieves superior knowledge integration while maintaining O(1) memory consumption through three key innovations: (1) sequential processing that merges one source at a time into an evolving target model, (2) parameter-wise gradient alignment that selectively transfers only parameters whose optimization directions align with the target domain, avoiding negative transfer, and (3) iterative fine-tuning that adapts transferred knowledge before integrating the next source. Extensive experiments across three continual learning benchmarks (Yearbook, CLEAR-10, CLEAR-100) spanning 10 to 108-year temporal distribution shifts and four architectures (1.3M to 25.6M parameters) demonstrate that GRASP achieves 93.5% mean accuracy over all datasets and architectures compared to ensemble method's 71.7% accuracy while requiring only constant memory versus K models for standard multi-source fusion. Critically, GRASP's sequential previously merged models and scales to arbitrarily many sources without memory growth, making it uniquely suitable for resource-constrained deployment and continually evolving source domains.

---


### 49. [Deep Learning in Seismic Interpretation: Federated Advances in Salt Dome Segmentation](https://arxiv.org/abs/2606.14905)

**<font color=#1a73e8>作者：</font>** Muhammad Zain Mehdi, Muhammad Zaid, Owais Aleem  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Salt-dome delineation is a critical, high-impact task in subsurface geological interpretation, driving decisions in hydrocarbon exploration, reservoir modeling, and drilling safety. While convolutional encoder-decoder architectures have delivered significant improvements in automated salt segmentation, their widespread application is severely limited by data sovereignty concerns, dataset bias, and the scarcity of labeled seismic volumes. This paper introduces FedSaltNet, a Federated Learning (FL) framework explicitly engineered for robust, generalizable, and privacy preserving salt-dome segmentation. We couple a lightweight Small U-Net backbone, chosen for its efficiency and regularization properties with a novel Foreground-Weighted (FG-WEIGHTED) aggregation strategy designed to tackle domain-specific class imbalance. Through an extensive comparative study emulating non-IID conditions across four diverse seismic datasets (TGS, SEAM, F3, GBS), we demonstrate two critical findings: The FG-WEIGHTED algorithm effectively mitigates data heterogeneity, yielding a 4.0% relative improvement in Intersection over Union (IoU) over the best conventional FL method. The simple U-Net architecture proved essential, outperforming the higher capacity ResNet-18 U-Net variant by 166% in average IoU, underscoring the necessity of architectural simplicity in data-constrained federated environments. FedSaltNet provides a validated, high-performance solution that establishes the viability of federated deep learning for collaborative, next-generation subsurface interpretation.

---


### 50. [Mask Proposal Voting Based on Geodesic Framework for Robust Image Segmentation](https://arxiv.org/abs/2606.14912)

**<font color=#1a73e8>作者：</font>** Li Liu, Mingzhu Wang, Zhenjiang Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite great advances, finding accurate segmentation remains a challenging task, especially in scenarios with cluttered backgrounds, complex intensity variations and topology appearance. Minimal path models have exhibited their strong ability in addressing image segmentation tasks. However, the performance of minimal paths-based segmentation approaches is heavily influenced by model initialization, hence limiting their application scope in practice. In this work, we propose a novel mask proposal voting framework that overcomes the major drawback of classical approaches, allowing robust segmentation even in complicated scenarios. Firstly, we introduce an efficient method for constructing adaptive domain cuts as a constraint for initializing the region-based min-cut evolution, by which diverse and reliable mask proposal candidates can be generated, substantially increasing the possibility of accurately covering the objective region by these proposals. Secondly, we propose a new mask voting scheme to build a voting score map encoding the final segmentation information. In contrast to classical path voting methods, our model allows incorporating priors to assign different importance to each individual mask. As a consequence, the proposed segmentation model is capable of accurately delineating object boundaries under complex scenarios, and is insensitive to initialization. Experiments demonstrate that our method consistently outperforms state-of-the-art minimal path-based approaches in both accuracy and robustness.

---


> [!TIP]
> 当前位于：**1-50**（第 1/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-509](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
