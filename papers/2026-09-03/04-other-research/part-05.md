# 📦 其他研究 | 2026年09月03日

> 本类共 **236** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-236**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-236**

---

### 201. [Accurate Reconstruction of Gas Turbine Blade Geometry Using 3D/2D Rigid Registration and CT View Optimization](https://arxiv.org/abs/2609.01368)

**<font color=#1a73e8>作者：</font>** Hristo Valtchanov, Nicolas Piché, Vladimir Brailovski 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Non-destructive X-ray and computed tomography (CT) testing are essential for ensuring the dimensional accuracy of manufactured components with complex internal structures, such as the cooling channels in gas turbine blades, which directly affect thermal performance and service life. This study presents a multipart 3D-2D rigid registration approach for aligning CAD models with X-ray projections as an alternative to CT reconstruction for part inspection and measurement. A greedy registration algorithm sequentially aligns the blade's exterior before registering its internal components by maximizing the mutual information between simulated and acquired X-ray images. This stepwise approach reduces problem complexity and improves alignment accuracy. View angles are optimized using a greedy method that iteratively selects angles to minimize dimensional measurement errors. The results indicate that a small number of oblique views provides the best accuracy, although a broad range of angles yields acceptable results. The method achieves subpixel registration accuracy, with errors below one-fifth of the magnified detector-pixel pitch. Image noise and defects reduce registration precision, but direct registration in projection space mitigates these effects compared with CT reconstruction. Appropriate view selection can therefore preserve acceptable subpixel accuracy in the presence of image noise and defects.

---


### 202. [Diffusion Based Unpaired Data Learning for Inverse Problems](https://arxiv.org/abs/2609.01370)

**<font color=#1a73e8>作者：</font>** Chenglong Bao, Yiming Dang, Chenguang Duan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Data is important in many deep learning-based inverse problem solvers. However, obtaining sufficient paired data in many scenarios remains highly challenging, while unpaired data is cheap. To maximize data utilization, this paper proposes LUD-DIF, a diffusion-based approach for solving inverse problems with unpaired data. Starting from the evidence lower bound (ELBO) of the joint distribution, we decouple it into two independent diffusion processes under the weak-coupling assumption. The method provides theoretical support from a variational inference perspective, derives the loss function, quantitatively analyzes the error bound introduced by the assumption, and offers a theorem-motivated heuristic for hyperparameter selection. Experimental results demonstrate that LUD-DIF achieves outstanding performance on multiple image inverse problems, validating its effectiveness and generalization capability in unpaired inverse problem settings.

---


### 203. [Polish ModernBERT: The Long and Short of Polish Language Understanding](https://arxiv.org/abs/2609.01379)

**<font color=#1a73e8>作者：</font>** Michał Perełkiewicz, Sławomir Dadas, Rafał Poświata 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Encoder-only Transformers remain effective for discriminative and representation-learning tasks, yet Polish encoders still largely rely on BERT/RoBERTa-style architectures. We introduce \textbf{Polish ModernBERT}, a family of four Polish encoders available at Base and Large scales, each with 512-token and 8K context variants. We adapt the ModernBERT pretraining recipe through staged selection experiments and release a long-context benchmark covering legal topic classification, ideological decision-direction prediction, factual-consistency assessment over literary plot summaries, and human-rights violation assessment. Across 30 tasks, Polish ModernBERT achieves the best overall performance among the evaluated Polish encoders, reaching 83.99 and 85.11 for the Base-8K and Large-8K models, respectively. On long-context tasks, the 8K variants improve over matched Polish RoBERTa-8K baselines from 67.47 to 77.15 and from 75.88 to 78.49 at the Base and Large scales, respectively. The Base-8K model achieves this gain with 22\% fewer parameters (149M vs.\ 190M). Efficiency measurements in representative inference setups show lower peak memory usage and latency than matched Polish RoBERTa baselines in both 512-token and 8K settings. Polish ModernBERT-8K-Base additionally achieves the best result on a Polish retrieval benchmark among the evaluated encoders below 300M parameters.

---


### 204. [Multimodal RGB-Infrared Combination for UAV-Based Wildfire Segmentation: A Comparative Study on FLAME3](https://arxiv.org/abs/2609.01390)

**<font color=#1a73e8>作者：</font>** Matheus F. Kovaleski, Luís Garrote, Cristiano Premebida 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unmanned Aerial Vehicles (UAVs) have emerged as a promising platform for firefighting operations due to their flexibility, low operational cost, and ability to acquire high-resolution imagery in locations that may be difficult or dangerous to access using conventional methods. Recent advances in deep learning have significantly improved the capabilities of UAV-based wildfire monitoring systems. The present work investigates RGB-infrared fusion for binary wildfire segmentation on the FLAME3 dataset. In this Study, RGB and Infrared baselines are compared with three representative fusion strategies across three segmentation architectures, including U-Net, DeepLabV3+, and SegFormer. The key motivation of this work is to analyze the contribution of each modality, evaluate the impact of fusion timing, and examine how different network architectures exploit multimodal information for UAV wildfire delineation. The findings indicate that thermal information plays a dominant role in UAV segmentation and that feature-level multimodal fusion combined with transformer-based architectures offers the most promising direction for future research.

---


### 205. [Scale-based Approach for Active Wildfire Segmentation on Satellite Imagery](https://arxiv.org/abs/2609.01392)

**<font color=#1a73e8>作者：</font>** Matheus F. Kovaleski, Cristiano Premebida, João Ruivo Paulo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Active wildfire mapping from satellite imagery is challenging due to the sparse and highly imbalanced nature of fire pixels, especially in early-stage or low-density fire observations. This work investigates the use of multispectral Landsat-8 imagery for active-fire segmentation under multi-scale wildfire size conditions. We propose a data-driven protocol to characterize fire-region size distributions through connected-component analysis and an interquartile range criterion, enabling the evaluation of model robustness across different local fire-region densities. Three segmentation architectures, U-Net, DeepLabV3+, and SegFormer, are evaluated under different SWIR-based spectral configurations. Results show that U-Net achieves the strongest robustness across the evaluated conditions, SegFormer provides competitive performance, and DeepLabV3+ tends to produce conservative predictions with reduced recall. Across architectures, SWIR2 consistently achieves the strongest or near-best results, highlighting its importance for active-fire segmentation in Landsat-8 imagery. These findings suggest that both spectral band selection and architectural design are critical for robust satellite-based active wildfire mapping trained on low active fire-pixel density images.

---


### 206. [Contribution-Aware Bandwidth Allocation for Multimodal Split Learning](https://arxiv.org/abs/2609.01406)

**<font color=#1a73e8>作者：</font>** Iason Ofeidis, Leandros Tassiulas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal models are increasingly the default option for perception at the network edge, yet they are trained almost entirely in the datacenter, because a client holding several sensor streams cannot host an encoder per modality. Split Learning makes such training feasible by keeping only the first layers on the device, at the cost of an uplink that must carry smashed activations for every modality at every step. Existing compression schemes give each modality the same keep-ratio, so the shared budget is divided in proportion to smashed-activation dimension, a quantity unrelated to how much each modality contributes to the fused prediction. We make that division an explicit decision and call it inter-modality allocation: under a fixed uplink budget, every policy transmits the same expected payload and differs only in how that payload is split across modalities. Our allocator, ModalShare, sets each modality's keep-ratio from a Shapley contribution score that the server computes over coalitions of activations it has already received. Measuring this score adds no uplink traffic and no client-side computation, and needs no prior knowledge of which stream is which. ModalShare improves accuracy over equal keep-ratios by 15.4 and 12.4 percentage points on CREMA-D and MVSA at matched payload in 5x compression, with strong performance across three compressors, three datasets, and four budgets. We show that existing compressors underperform in multimodal settings, with ModalShare recovering what gains are left behind.

---


### 207. [Neuro-Symbolic Geometric Abstraction (NeuSOGA): From Observations to Symbolic Mathematical Representations](https://arxiv.org/abs/2609.01408)

**<font color=#1a73e8>作者：</font>** Qingde Li, Qingqi Hong, Jie Tian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A fundamental challenge in artificial intelligence is the transformation of observations into explicit symbolic representations suitable for abstraction, interpretation, and reasoning. While modern AI systems achieve remarkable perceptual capabilities through large-scale statistical learning, the resulting knowledge is typically encoded within latent parameters that are difficult to inspect or manipulate analytically. Inspired by Neuro-Symbolic AI and theories of human abstraction, this paper investigates the formation of symbolic mathematical representations from geometric observations.
We propose NeuSOGA (Neuro-Symbolic Geometric Abstraction), a framework that progressively transforms observations into topological abstractions, geometric abstractions, and ultimately symbolic mathematical representations. The architecture combines topology-guided structural discovery using Euclidean Distance Transforms, foundation-model perception using Segment Anything, adaptive multi-scale geometric abstraction, and symbolic synthesis through Implicit Area Splines.
The resulting representation is an analytical implicit model supporting arbitrary-order smoothness, additive composition, and closed-form evaluation. Unlike neural latent encodings, the generated representation remains interpretable, editable, and mathematically explicit. Experiments on ModelNet40 point clouds, arbitrary-view projections, and segmented optical observations demonstrate that NeuSOGA transforms diverse observations into compact symbolic representations while preserving essential geometric and topological structure across sensing modalities and viewing directions.
NeuSOGA provides an interpretable and explainable pathway from observation to symbol and establishes

---


### 208. [Predicting Subsurface Abnormalities Growth using Physics-Informed Neural Networks](https://arxiv.org/abs/2609.01417)

**<font color=#1a73e8>作者：</font>** Mehrdad Shafiei Dizaji, Hoda Azari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The research explores the pioneering integration of Physics-Informed Neural Networks (PINNs) into the domain of Ground-Penetrating Radar (GPR) data prediction. This research presents a detailed development framework for a specialized PINN model, proficient at interpreting and forecasting GPR data, much like how medical imaging models predict tumor behavior. By harnessing the synergy between deep learning algorithms and the physical laws governing subsurface structures or in medical terms, human tissues the model effectively embeds the physics of electromagnetic wave propagation into its architecture. This ensures that predictions not only align with fundamental physical principles but also mirror the precision needed in medical diagnostics for detecting and monitoring tumors. The suggested deep learning structure comprises three components: a CNN, a spatial feature channel attention (SFCA) mechanism, and ConvLSTM, along with temporal feature frame attention (TFFA) modules. The attention mechanism computes channel attention and temporal attention weights using self-adaptation, thereby fine tuning the visual and temporal feature responses to extract the most pertinent and significant visual and temporal features. By integrating physics directly into the neural network, our model has shown enhanced accuracy in forecasting GPR data. This improvement is vital for conducting effective assessments of bridge deck conditions and other evaluations related to civil infrastructure. The use of Physics Informed Neural Networks (PINNs) has demonstrated the potential to transform the field of Non-Destructive Evaluation (NDE) by enhancing the precision of infrastructure deterioration predictions. Moreover, it offers a deeper insight into the fundamental mechanisms of deterioration, viewed through the prism of physics-based models.

---


### 209. [Provably Safe Sim-to-Real Transfer](https://arxiv.org/abs/2609.01418)

**<font color=#1a73e8>作者：</font>** Tingting Ni, Maryam Kamgarpour  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To mitigate the sample complexity of real-world reinforcement learning (RL), a common practice is to first train a policy in a simulator, where samples are cheap, and then deploy the learned policy in the real world with the hope that it generalizes effectively. Such direct sim-to-real transfer is not guaranteed to succeed: simulator-trained policies can be suboptimal in the real world due to sim-to-real mismatch. Correcting this mismatch requires collecting data from the real system, but in many applications, such as robotics and healthcare, this data-collection process is itself subject to safety constraints. This gives rise to the problem of safe sim-to-real transfer: how can an agent exploit an imperfect simulator while ensuring safe real-world data collection and learning a near-optimal feasible policy for the target system? We address this problem by formulating safe sim-to-real transfer within the framework of reward-free safe RL. We design a computationally efficient algorithm that exploits simulator information to provably reduce real-world interaction while ensuring safe exploration and enabling the computation of a near-optimal feasible policy for any potential reward function. Our real-world sample complexity bound characterizes the benefit of using the simulator in terms of the sim-to-real mismatch.

---


### 210. [MegaStyle++: Scaling Image Style Space through Hierarchical Style Definition](https://arxiv.org/abs/2609.01423)

**<font color=#1a73e8>作者：</font>** Junyao Gao, Sibo Liu, Jiaxing Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image style is a highly abstract, human-constructed concept shaped by a range of visual factors and intrinsically entangled with content, yet a unified and explicit definition of image style remains lacking. In this work, we first discuss the fundamental question of what is style and then propose a hierarchical style definition that describes image style from an overall style identity to fine-grained visual attributes, providing a more structured, transferable, and interpretable style representation. Based on this definition, we refine the style annotation pipeline of MegaStyle and construct MegaStyle++-8M, a large-scale style dataset containing 150K overall style identities, 1M fine-grained style prompts, and 8M stylized images. Extensive analyses demonstrate that our hierarchical definition substantially expands the style space in both diversity and semantic breadth, while precisely capturing intrinsic visual style of reference images. The dataset and code will be updated at this https URL, we hope MegaStyle++ provides a scalable foundation for studying and modeling diverse image styles.

---


### 211. [CATeye: Coupled Attribute-Topology Invariance Learning for Voucher Abuse Detection](https://arxiv.org/abs/2609.01425)

**<font color=#1a73e8>作者：</font>** Tian Tian, Shuaicheng Niu, Hao Kuang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Voucher abuse poses a major challenge in e-commerce, where malicious users exploit promotional vouchers for profit. Unfortunately, fraud patterns evolve rapidly over time and across regions, causing distribution shifts that degrade existing detection models unless retrained frequently. To tackle this, we propose the Coupled Attribute-Topology Invariance Learning framework (CATeye). The key challenge arises from coupled attribute-topology shift, where edges built from attribute proximity cause environment-driven attribute shift to induce shifted topology, thereby amplifying variant signals through GNN message passing. CATeye sees through such coupled shifts with two learnable selectors. First, an Attribute Invariance Selector (AIS) learns node-adaptive masks to filter out non-invariant attributes. Then, conditioned on retained invariant attributes, an Edge Invariance Selector (EIS) samples an invariant subgraph and isolates non-invariant edges. Using the resulting invariant and non-invariant components, CATeye constructs multiple views and applies view-specific objectives to emphasize domain-invariant representations while suppressing domain-specific variations. Experiments on both a proprietary dataset from Lazada, a major Southeast Asian e-commerce platform, and a public benchmark show that CATeye consistently outperforms nine strong domain generalization and graph anomaly detection baselines, achieving up to an 8.61% improvement in average F1 score over the strongest baseline. Source code is publicly available at this https URL.

---


### 212. [Semantic-Guided Multimodal Preprocessing for Vision Transformer-Based Clear Cell Renal Cell Carcinoma Grading](https://arxiv.org/abs/2609.01426)

**<font color=#1a73e8>作者：</font>** Fatemeh Javadian, Zhu Chen, Zahra Aminparast 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Clear cell renal cell carcinoma (CCRCC) grading is essential for treatment planning, yet existing approaches either analyze patch-level images directly or focus solely on nuclei-level classification, without linking to final tumor grading. We propose a semantic-guided multimodal preprocessing method that integrates nuclei classification maps from existing pre-trained models with RGB histopathology images for Vision Transformer (ViT)-based CCRCC grading. Our approach employs classification map channel concatenation and multiplicative modulation, with optimized overlays to leverage nuclei grading information, while preserving RGB textural features. Evaluation of multiple preprocessing strategies demonstrates that semantic-guided enhancement achieves 0.916 balanced accuracy, outperforming RGB-only baseline (0.707) and max-voting aggregation from prior studies (0.427). Sensitivity analysis reveals that this 21 percentage point improvement over baseline persists even under simulated perturbation at rates matching current state-of-the-art nuclei classification model error thresholds, suggesting both effective semantic utilization and practical robustness. These findings show that preprocessing-based multimodal fusion can leverage the diagnostic potential of existing imperfect nuclei classifiers, effectively bridging previously isolated fine-grained nuclear-level analysis with coarse-grained ViT-based patch classification. Per-class recall was consistent across grades (0.93, 0.91, 0.91), indicating that gains are not concentrated in the majority class. Because the sensitivity analysis perturbs ground-truth maps rather than predictions from an actual nuclei model, this result characterizes robustness under simulated error rather than deployment with a real upstream model, which remains for future work.

---


### 213. [Pix2Rep-v2: Data-Efficient Representation Learning for Dense Medical Imaging Applications](https://arxiv.org/abs/2609.01427)

**<font color=#1a73e8>作者：</font>** S. Sifaoui, E. Angelini, S. Toupin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dense self-supervised learning (SSL) is a powerful paradigm for learning without annotations the local descriptors required to solve dense medical imaging tasks. We present Pix2Rep-v2, a framework for SSL of pixel- and voxel-level representations suitable for few-shot downstream applications. Pix2Rep-v2 addresses the main challenges of dense SSL by leveraging a redundancy reduction objective at the pixel-level with a principle of equivariance of dense representations, that scales efficiently to 3D or wide field-of-view applications. We evaluate our method on four datasets, across multiple tasks, multiple modalities and anatomical structures using multiple backbones in 2D and 3D, and under various data regimes. As an alternative to linear probing or full fine-tuning on the downstream task, we also propose an in-context variant, without downstream training, based on a dense prototype approach. Pix2Rep-v2 shows substantially higher data-efficiency in few-shot scenarios compared to fully supervised baselines, and is competitive with the state-of-the-art e.g., +9.3 Dice points in one-shot segmentation on the M&Ms-2 dataset. Our code and pre-trained models are publicly available at this https URL.

---


### 214. [Learning Sparse Decision Trees via Transformer Variational Auto-Encoders](https://arxiv.org/abs/2609.01430)

**<font color=#1a73e8>作者：</font>** Giacomo Fidone, Alessio Cascione, Riccardo Guidotti  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decision trees are among the most widely used models in machine learning, largely due to their transparent decision logic, making them well-suited for high-stakes decision-making contexts. However, most existing learning algorithms focus on predictive performance, overlooking the joint optimization of other desirable properties, such as structural sparsity. In this work we propose TREVIS, an approach for learning decision trees with respect to complex objectives, based on the exploration of the latent space of a Tree Transformer Variational Auto-Encoder (TTVAE). By mapping decision trees onto latent representations, TREVIS replaces the discrete search space with a continuous one, enabling gradient-based optimization via a differentiable surrogate model. We experiment with TREVIS for learning decision trees that jointly optimize predictive performance and sparsity. Results show that TREVIS discovers decision trees matching the predictive performance of existing near-optimal algorithms while improving their structural sparsity.

---


### 215. [Gaussian Core LoRA: Distribution-Aware Dynamic Adaptation for Broad Concept Erasure](https://arxiv.org/abs/2609.01433)

**<font color=#1a73e8>作者：</font>** Qinghui Gong, Xunlei Chen, Yu-Xuan Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Concept erasure aims to suppress unsafe, privacy-sensitive, or undesirable generations in text-to-image diffusion models while preserving benign semantics, visual quality, and deployment efficiency. Existing adapter-based methods, such as Low-Rank Adaptation (LoRA), typically freeze the diffusion backbone and learn lightweight parameter updates to steer generation away from target semantics. However, these methods usually assign a static semantic erasure direction to each target concept. This assumption is overly coarse for broad and complex target concepts, since a concept often contains multiple latent semantic prototypes involving different objects, scenes, or relations, and requires different local erasure directions. A single LoRA update averages these heterogeneous erasure demands, leading to under-erasure on difficult prototypes and over-editing of nearby benign semantics. To address this limitation, we propose Gaussian Core LoRA, a distribution-aware low-rank adaptation framework. It fits a Gaussian mixture model in the prompt feature space to estimate latent semantic prototypes within the target concept. During inference, each input prompt is projected into this feature space to compute its Gaussian posterior responsibilities, which condition the core generator to produce a prompt-specific, norm-bounded residual reconfiguration of the shared LoRA rank space. This enables prototype-adaptive erasure with a single lightweight adapter. Compared with the strongest baseline on each metric, Gaussian Core LoRA reduces average Attack Success Rate (ASR) by 7.95%, lowers COCO Fr'echet Inception Distance (FID) by 14.72%, and improves CLIP Score by 4.98%. Further experiments show robustness to adversarial prompts, scalability to multi-identity and multi-style erasure, and compatibility with SDXL and FLUX.

---


### 216. [Cross-Modal Guidance for Out-of-View Object Search in Simulated Prosthetic Vision](https://arxiv.org/abs/2609.01438)

**<font color=#1a73e8>作者：</font>** Adyah Rastogi, Apurv Varshney, Tobias Höllerer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Out-of-view guidance is well established in virtual and augmented reality, but its effectiveness may depend on the visual bandwidth available to the user. We test this under simulated prosthetic vision (SPV), where visual guidance must share the same sparse representation used to inspect the scene. Nineteen participants performed object search under two SPV conditions differing in electrode density and phosphene spread (10x10 and 20x20) and four guidance conditions (no guidance, visual, haptic, audio) all driven by the same horizontal target-offset variable. All three modalities reduced search time and head movement. The tested auditory and haptic cues produced approximately 25% faster overall search and 11-13% faster target acquisition than the visual cue, despite similarly direct orienting trajectories. The tested haptic and auditory cues also shortened post-acquisition search. Final head-target angular offset was reduced substantially more in the 10x10 SPV condition; there, all three cues also reduced vertical localization error by approximately 45-58% despite providing no elevation information. Under severe visual constraints, guidance performance depended on cue implementation and search stage.

---


### 217. [Edge-Girth as a Structural Edge Feature for Graph Neural Networks](https://arxiv.org/abs/2609.01441)

**<font color=#1a73e8>作者：</font>** Lilian Marey, Charlotte Laclau  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks (GNN) based on message passing are provably no more powerful than the one-dimensional Weisfeiler--Leman colour-refinement test (1-WL): two graphs it cannot tell apart receive identical representations, however deep or wide the network. A common remedy augments node or edge features with precomputed structural descriptors, most often counts of a fixed small subgraph such as triangles or longer cycles, but such counts require committing in advance to the size of the substructure counted, a choice usually made blind to the data. We study a descriptor that avoids this choice. The edge-girth of an edge is the length of a shortest cycle through it, and its multiplicity is the number of such shortest cycles; together they form a per-edge invariant that reports cycles of arbitrary length, computable exactly by a single breadth-first search per edge. Injected into a gated message-passing architecture, EGAGNN, it reaches a test MAE a factor three below the closest gated comparator on the ZINC-12k regression benchmark at 104k parameters; against bounded cycle-counting descriptors under the same architecture, it matches only a dictionary counting cycles up to length eight, using twice as many channels, while a dictionary capped at length four performs no better than no structural information at all. On graph discrimination we prove a matching limitation: on graphs where every edge sees the same number of shortest cycles of the same length, the descriptor becomes constant and any model built on it collapses back to the 1-WL bound. This holds without exception across all 400 pairs of the BREC benchmark: not one of the 90 such pairs is distinguished.

---


### 218. [Better Situational Awareness in AR-HRC? A Comparative Study of Augmented Reality and Mobile Interfaces for Human-Robot Collaboration](https://arxiv.org/abs/2609.01461)

**<font color=#1a73e8>作者：</font>** Zhehan Qu, Christian Fronk, Jaewoong Jeong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Augmented reality (AR) facilitates human-robot collaboration (HRC) by enabling in-situ spatial visualizations of the robot and the joint task. However, in safety-critical HRC scenarios such as search-and-rescue, spatial visualizations may also reshape visual attention in ways that create competing situational awareness (SA) demands, potentially introducing new safety concerns. While prior AR-HRC work suggests potential benefits for SA, rigorous evaluations that jointly consider robot and environmental awareness across multiple levels of SA remain limited. We address this through a between-subjects study with 30 participants comparing custom AR and mobile interfaces presenting equivalent information, measuring robot and environmental SA with the Situation Awareness Global Assessment Technique (SAGAT) across all three levels, with concurrent eye tracking to identify the attentional mechanisms underlying any SA differences. Both interfaces achieved high usability; relative to the mobile baseline, AR improved perception-level awareness of the robot but yielded no gains in higher-level robot awareness or in environmental awareness at any level. Gaze analysis explained this: AR freed attention from the map, but that attention was re-invested in the conformal visuals rather than the physical environment. Freeing the eyes from a screen is not the same as directing them to the world, a distinction AR interfaces for safety-critical HRC must design around.

---


### 219. [CameraEditor: Camera-Controlled Image Editing via Video-Prior Sequential Modeling](https://arxiv.org/abs/2609.01479)

**<font color=#1a73e8>作者：</font>** Xin Shen, Chengyou Jia, Keshuo Xing 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Beyond semantic content, camera parameters play a pivotal role in dictating the geometric perspective and appearance of any given image. While recent image editing models excel at semantic and stylistic manipulation, they struggle with explicit camera parameter control. When handling large perspective shifts, instruction-driven models face a dilemma: they either suffer from structural tearing or generate conservative outputs that ignore geometric instructions. To address this, we introduce CameraEditor, a framework that reformulates camera-controlled editing from a spatial problem into a temporal sequence prediction task. By leveraging the temporal coherence of video diffusion models, our approach integrates an explicit geometric perception module with a dynamic reference routing mechanism. This allows us to construct geometrically rigorous visual reference pairs via dynamic panorama cropping, overcoming the ambiguity of text-based instructions. Furthermore, CameraEditor strategically inserts intermediate transition frames to decompose large perspective shifts, providing a robust temporal buffer that preserves content identity and spatial coherence. We construct a training dataset of 5,760 instances. As an independent contribution, we introduce CamEditor-Bench, a model-agnostic evaluation suite of 462 test cases. Extensive experiments demonstrate that CameraEditor achieves state-of-the-art camera control precision and source identity preservation, outperforming existing methods.

---


### 220. [Rethinking Learnability in Offline Data-driven Optimization](https://arxiv.org/abs/2609.01493)

**<font color=#1a73e8>作者：</font>** Chao Qian, Chen-Guang Wang, Rong-Xi Tan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Black-Box Optimization (BBO) has found broad applications, but evolutionary algorithms and Bayesian optimization face efficiency challenges as real-world BBO problems grow increasingly complex. Data-driven optimization improves the efficiency of BBO algorithms by learning from data. Offline data-driven optimization seeks high-quality solutions using only a fixed set of previous evaluations, attracting substantial attention because it requires no additional online evaluations. Many offline optimization methods have been proposed, but a fundamental question remains unanswered: what learnability is sufficient for offline optimization? Prior theoretical studies show that Probably Approximately Correct (PAC) learnability is insufficient, as the optimal region may remain poorly learned even when most regions are well learned. In this paper, we propose algorithm-dependent learnability, which requires accuracy only on the optimizer's trajectory. We prove that its value-query form is sufficient for representative discrete settings, including greedy and local search for submodular maximization, while its first-order analogue is sufficient for projected gradient descent on convex minimization. Motivated by this notion, we formalize a trajectory-learning framework comprising trajectory construction, trajectory modeling, and candidate generation, and analyze existing trajectory-based methods under it. We further propose Uncertainty-aware Gradient-guided Trajectory Learning (UGTL), which constructs locally coherent improvement trajectories reflecting plausible search paths, models them with conditional diffusion, and selects a diverse candidate set. On five Design-Bench tasks, UGTL achieves the best aggregate mean rank, $3.1/25$, among 25 methods. Controlled trajectory analyses and cross-architecture replacements confirm that our trajectory construction plays a significant role in the improvement.

---


### 221. [Optimizing Byzantine Node Placement in Decentralized Federated Learning](https://arxiv.org/abs/2609.01495)

**<font color=#1a73e8>作者：</font>** Edoardo Gabrielli, Gabriele Tolomei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Security evaluations of decentralized federated learning (DFL) typically focus on how Byzantine participants behave, while largely overlooking which participants are compromised. Yet, because aggregation is distributed over a communication graph, the placement of Byzantine nodes determines how malicious influence propagates through the network. We therefore treat Byzantine placement as an explicit adversarial decision and formulate the attacker's objective as selecting, under a fixed compromise budget, the set of participants that maximizes its finite-time impact on honest nodes. To approximate this objective without executing the learning process for every candidate placement, we introduce Byzantine Placement Influence (BPI), a set-level measure derived from the actual gossip dynamics that quantifies the cumulative exposure of honest nodes to Byzantine sources over the training horizon. Unlike placement criteria based on node centrality heuristics, BPI directly accounts for weighted multi-hop propagation and interactions among compromised nodes. We develop efficient algorithms for optimizing BPI and evaluate them across six heterogeneous graph families, untargeted model poisoning, and backdoor attacks. BPI-guided placements consistently identify highly damaging configurations across different network structures and remain effective when the linear gossip assumption is relaxed through Byzantine-robust aggregation. Our results show that Byzantine placement is a critical but under-modeled dimension of DFL threat models and robustness evaluations.

---


### 222. [Benchmarking Spatial, Spectral, and Self-Supervised Cues for Face Forgery Detection under Realistic Degradation](https://arxiv.org/abs/2609.01511)

**<font color=#1a73e8>作者：</font>** Lucas Cunha, Lucas Sotomaior, Lucas Gasperin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face forgery detectors often achieve strong results on controlled benchmarks, but their reliability under realistic image degradations remains limited. This paper presents a standardized benchmark for face forgery detection using the Multi-Dimensional Face Forgery Image (MFFI) dataset and evaluates performance on both clean and degraded test partitions. We compare six model families, including convolutional networks, transformer-based models, and a frozen self-supervised DINOv3 backbone, across spatial, spectral, and hybrid input representations. The results show that clean-set performance is not a reliable indicator of robustness under compression, resizing, and blurring. Xception with RGB obtains the best clean performance, reaching 0.884 mean ROC-AUC, but degrades substantially on the harder partition. In contrast, frozen DINOv3 achieves the strongest degraded-set result, with 0.726 mean ROC-AUC, while training only a linear classification head. The representation analysis indicates that Fourier-domain cues are most useful when combined with RGB information, whereas purely spectral inputs consistently underperform spatial representations. Qualitative attribution maps further suggest that convolutional detectors focus on localized artifacts, while DINOv3 relies on broader facial structure. These findings reinforce the need for degraded evaluation protocols and highlight self-supervised visual representations as a promising direction for robust face forgery detection. Our source code is publicly available at this https URL.

---


### 223. [DualDiff3D: Dual Structure-Appearance Diffusion Priors for Reliability-Enhanced 3D Gaussian Splatting](https://arxiv.org/abs/2609.01516)

**<font color=#1a73e8>作者：</font>** Qian Wang, Yu Wang, Weiqi Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While 3D Gaussian Splatting (3DGS) has revolutionized 3D reconstruction and novel-view synthesis, scenarios with limited input views often lead to poor reconstruction quality and artifacts in rendered novel views. Recent efforts attempt to utilize powerful diffusion priors, yet they typically process rendered and reference views concatenated along an additional dimension in a single network. These methods overlook an inherent nature that different views should maintain appearance similarity but differ in structure due to view shifts, leading to blur caused by conflicts between the two properties. In this paper, we propose DualDiff, a novel pipeline that leverages dual diffusion priors with a Structure-Appearance Attention (SAA) module to introduce reference guidance for refining low-quality novel views rendered from flawed 3D representations. Specifically, we retain one diffusion branch to focus on extracting structural information from the low-quality novel views, while introducing another branch to ensure appearance consistency with reference views. Furthermore, we present a 3D reconstruction framework named DualDiff3D, which integrates a reliability-enhanced Render-Refine-Optimize (RRO) loop to progressively and robustly incorporate the refined novel views, yielding more accurate 3DGS. Extensive experiments demonstrate that our approach outperforms state-of-the-art methods even in the inference-only setting, with further performance gains achievable through training. Our code and pre-trained weights are available at this https URL.

---


### 224. [Revisiting Cross-View Completion: Self-Supervised Pre-Training via Reconstruction Error Comparison](https://arxiv.org/abs/2609.01530)

**<font color=#1a73e8>作者：</font>** Thibaut Loiseau, Guillaume Bourmaud, Vincent Lepetit  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised pre-training via cross-view completion learns strong features for 3D vision from co-visible regions of image pairs. However, the reference view provides little information for reconstructing non-co-visible patches, implicitly yielding a monocular training signal in these regions. We introduce Gekko, which turns this limitation into a useful signal. The relative improvement of the cross-view reconstruction error over a masked-autoencoder error is a self-supervised proxy for co-visibility: large improvements indicate co-visible regions, negligible ones non-co-visible areas. Gekko is a network, trained from scratch, that jointly performs cross-view completion, masked autoencoding, and per-pixel prediction of this relative improvement, providing an additional binocular signal for all masked regions without any ground-truth 3D annotation. Under identical architectures and training data, Gekko consistently outperforms CroCo on zero-shot correspondence estimation, relative pose estimation, and pointmap regression, with up to 6 times higher accuracy at the strictest relative-pose threshold and a 22% drop in end-point error on ETH3D. The extra channel it learns is itself a strong co-visibility detector on unseen scenes, and Gekko's frozen features outperform released cross-view backbones of comparable or larger size. It can also be trained directly from raw videos with a simple stride-based curriculum, removing the cumbersome 3D preprocessing prior methods require while matching models trained on curated data. Code and pre-trained models are publicly available.

---


### 225. [Quantum Sparse Autoencoders for Q-Matrix Estimation in Cognitive Diagnosis](https://arxiv.org/abs/2609.01537)

**<font color=#1a73e8>作者：</font>** Arif Hassan Zidan, Yi Pan, Bowen Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Q-matrices play a central role in cognitive diagnosis within educational data mining (EDM), specifying which latent skills each assessment item requires. Data-driven Q-matrix estimation remains challenging when assessments involve many correlated skills and when real response patterns depart from idealized generative assumptions. We introduce a novel quantum sparse autoencoder (QSAE) for Q-matrix estimation, which, to the best of our knowledge, is the first application of quantum machine learning (QML) to cognitive diagnosis. Overall, the QSAE embeds each student's binary response vector into a quantum circuit using an encoder, compresses it into a sparse latent representation, and maps that representation to the Q-matrix. We benchmark the QSAE against a classical autoencoder (CAE) across 60 simulated datasets and 9 real-world assessment datasets. The results reveal complementary strengths. Although the CAE partially achieves higher average accuracy under several simulation conditions, the QSAE is substantially more stable across replications, exhibiting lower variance in 49 of the 60 conditions. Moreover, on real assessment data, the QSAE outperforms the CAE on 6 of the 9 datasets. These findings suggest that the principal advancement of QML in this setting is not universal accuracy improvement, but enhanced robustness and capability to explore latent-structure complexity in real datasets.

---


### 226. [NashDreamer: Model-Based Reinforcement Learning for Zero-Sum Imperfect-Information Games](https://arxiv.org/abs/2609.01549)

**<font color=#1a73e8>作者：</font>** Tomáš Holeček, Viliam Lisý  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model-based reinforcement learning (MBRL) has achieved remarkable results in single-agent domains, yet its extension to competitive imperfect information games (IIGs) remains underexplored. In multi-agent settings, opponent-induced non-stationarity complicates the learning process, and decentralized model learning faces severe identifiability barriers, which we argue make centralized model learning a mathematical necessity. Building on this analysis, we propose NashDreamer, a principled MBRL framework for two-player zero-sum IIGs. It introduces a centralized Multi-Agent Recurrent State-Space Model (MARSSM) that decouples environment dynamics from the effect of players' strategies on their individual observations. NashDreamer is designed to use arbitrary policy gradient algorithms and inherits their convergence guarantees towards Nash equilibria under an idealized model. Empirical evaluations across four benchmark games demonstrate that NashDreamer substantially improves sample efficiency over model-free baselines early in the training. Finally, we theoretically analyze the architecture's optimization landscape, identifying the vulnerability of the Dreamer family of algorithms to posterior collapse in stochastic environments. We leave it as an open challenge.

---


### 227. [A Mathematical Theory of Reusable Neural Bases for Network Compression](https://arxiv.org/abs/2609.01550)

**<font color=#1a73e8>作者：</font>** Binshuai Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As large AI models become increasingly prevalent across a wide range of applications, memory cost has become a critical bottleneck in both training and inference. To mitigate this issue, we introduce the Linear Reusable Neural Bases Architecture (LRNBA), a novel framework aimed at improving parameter efficiency and reducing memory cost. Inspired by recurrent neural network (RNN) designs, the core idea of our approach is to represent each network block as a linear combination of a shared set of neural bases, thereby enjoying highly network compression rate while maintaining stable training. The proposed architecture allows for the construction of significantly wider and deeper networks under the same parameter budget. Extensive experiments demonstrate that our model achieves comparable or even faster convergence and lower loss than classical architectures, while maintaining stable training dynamics.

---


### 228. [BS: Take the Hint - Interactive Multitracer PET/CT Lesion Segmentation with a Scribble-Conditioned ResEnc U-Net](https://arxiv.org/abs/2609.01554)

**<font color=#1a73e8>作者：</font>** Marven Sherif, Amgad Elmasry, Youssef Ghazal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated lesion segmentation in whole-body PET/CT is complicated by the variety of physiological tracer uptake patterns and by the differing appearance of lesions across tracers. The autoPET/CT V challenge addresses this by making segmentation interactive: user scribbles marking foreground and background are supplied alongside the image, and the algorithm is expected to exploit them. We present our submission, a scribble-conditioned residual encoder U-Net operating on four input channels: CT, PET, and a sparse scribble map for each of foreground and background. The network is initialised from the autoPET-III winning weights and extended from two to four input channels, with the two scribble channels zero-initialised so that the pretrained representation is preserved exactly at initialisation. Every model is fine-tuned per fold from the corresponding autoPET-III fold checkpoint, so that no validation case is seen during pretraining. PET intensities are normalised against a per-scan aorta blood-pool reference derived from a CT segmentation, which removes tracer- and centre-specific scaling without requiring lesion labels. At inference the five fold models are ensembled by averaging their softmax outputs per sliding-window patch, before Gaussian-weighted stitching. On the challenge's five-fold split, with each fold evaluated on its own validation cases, mean Dice is 0.554 and mean lesion-level F1 is 0.528 without scribbles, rising to 0.751 and 0.733 after five correction rounds. About 85% of that gain follows the first scribble, and the spread between fold models narrows five-fold over the same rounds, so interaction largely compensates for how well or badly a given model segments unaided.

---


### 229. [Gradient-Update Mismatch: Rethinking Conflict-Free Training of Physics-Informed Neural Networks](https://arxiv.org/abs/2609.01558)

**<font color=#1a73e8>作者：</font>** Jing Xiao, Xinhai Chen, Qinglin Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training Physics-Informed Neural Networks (PINNs) requires jointly optimizing physics residual and initial/boundary condition loss terms, which often induce conflicting gradients. Gradient surgery methods mitigate this issue by constructing directions from loss-specific gradients to reduce conflict before optimizer transformation. However, even when the constructed direction is conflict-free, this property may not be preserved after optimizer transformation. Let $a_t$ denote the direction constructed by gradient surgery, $u_t$ the optimizer proposal, and $\mathcal{C}_t$ the conflict-free cone induced by the loss-specific gradients. We show that modern optimizers can transform $a_t$ through mechanisms such as historical state, adaptive scaling, preconditioning, or decoupled weight decay, so $a_t \in \mathcal{C}_t$ does not generally imply $u_t \in \mathcal{C}_t$. We refer to this optimizer-induced discrepancy in conflict-freeness between $a_t$ and $u_t$ as Gradient-Update Mismatch (GUM). Accordingly, we propose Gradient-Update Alignment (GUA), which projects $u_t$ onto $\mathcal{C}_t$ to obtain the aligned update $p_t$ and applies $p_t$ to the parameters. When the optimizer maintains internal state, GUA further adjusts this state toward targets reconstructed from the applied update. We conduct extensive experiments and find that GUM is widespread across momentum, adaptive, and curvature-based optimizers, with conflict rates reaching up to 86.3%. Across all PINN settings, GUA achieves conflict-free applied updates and consistently improves various gradient surgery methods, reducing the relative $L_2$ error by up to 98.2% in individual settings. Data and code are available at this https URL.

---


### 230. [H3-World: Turning Language Understanding into World Control](https://arxiv.org/abs/2609.01560)

**<font color=#1a73e8>作者：</font>** Danze Chen, Zeqing Wang, Ziyue Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present H3-World, an efficient framework that turns the 33B MiniMax-H3 video generator into an interactive world model. Our key finding is that, as large video generators become more capable, language is emerging as a natural interface for control. MiniMax-H3, for example, already supports zero-shot control of character behavior and camera motion through natural-language instructions. Building on this, H3-World turns this coarse language interface into precise, temporally grounded world control, without introducing dedicated action modules. Specifically, we represent each action as a structured combination of character and camera instructions, and align them with the corresponding temporal video latents. To make the control temporally precise, we further introduce temporal attention routing, which restricts each instruction to its intended time interval and reduces control leakage across actions. Importantly, H3-World directly reuses the semantic representations learned during large-scale video pretraining and requires only lightweight adaptation. With only 8,000 gameplay samples, 10,000 LoRA optimization steps, and 0.199% trainable parameters, H3-World achieves effective character and camera control while preserving strong generation quality. It also generalizes to unseen scenarios. These results show that the control capabilities emerging in large video generators can be efficiently transformed into interactive world control.

---


### 231. [Evaluating Usability in Biomedical Visualization: Rethinking Heuristic Evaluation for Spatial Omics and Multidisciplinary Research Platforms](https://arxiv.org/abs/2609.01569)

**<font color=#1a73e8>作者：</font>** Yulia A. Levites Strekalova, Rachel Liu Galvin, Jessica M. Ray 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Introduction: Clinical research informatics (CRI) platforms support biomedical discovery by integrating advanced computational tools into research workflows. Emerging technologies such as spatial omics and AI-enabled imaging expand research capabilities but introduce complex interfaces that increase cognitive burden and alter established analytical processes. Traditional usability frameworks identify general usability issues but often miss challenges specific to high-dimensional biomedical data. Methods: We conducted two complementary studies involving 39 participants to evaluate conventional usability heuristics and identify CRI-specific criteria. Study 1 included 19 undergraduates completing interactive tasks, and Study 2 involved 20 clinical professionals completing an asynchronous hierarchical task framework. Observational and interview data were analyzed using deductive coding based on standard usability heuristics and emerging CRI-specific themes. Results: Simultaneous presentation of complex data overlays and analytical tools overwhelmed users, particularly those with limited spatial-omics experience. Participants relied on trial-and-error exploration and struggled with unlabeled tools in data-rich environments. Feedback indicated that users benefit from phased onboarding, contextual guidance, and progressive feature introduction rather than immediate access to all functionality. Discussion: High-dimensional research platforms require domain-specific usability criteria beyond traditional frameworks. We propose three specialized heuristics: Active Parameter Transparency, Point-of-Use Guidance, and Phased Feature Disclosure. These heuristics help developers manage complexity, provide contextual support, and improve accessibility for multidisciplinary research teams.

---


### 232. [SpatialGuard: Harness-Guided Verifiable Spatial Reasoning for Text-to-Image Generation](https://arxiv.org/abs/2609.01582)

**<font color=#1a73e8>作者：</font>** Ziyun Qian, Zizhi Chen, Yizhou Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Complex 3D spatial text to image generation requires models to convert natural language into stable visual geometry, not merely semantic appearance. Existing prompt-driven or layout-conditioned methods improve controllability, but often lack an optimizable and verifiable spatial intermediary before visual sampling. As a result, object relations, occlusion, visibility, and camera constraints can decay during multi-round generation. This paper presents SpatialGuard, a structured layout-guided framework for complex 3D spatial text-to-image generation. SpatialGuard parses prompts into image synthesis-oriented 3D layouts through a Spatial Layout Architect, realizes them as visual conditions and candidate images through a Visual Realizer, and uses a Visual Alignment Critic to validate consistency among prompt, layout, and image. To keep constraints stable across iterations, SpatialGuard introduces a Layout Harness that organizes rule constraints, tool invocation, shared knowledge, and feedback loops around the editable layout state. This design turns complex spatial generation from implicit prompt following into a verifiable process of planning, realization, validation, and repair. Comprehensive experiments show that SpatialGuard achieves state-of-the-art performance in complex 3D spatial layout generation and improves spatial faithfulness over existing text-to-image and layout control baselines.

---


### 233. [A Benchmark for Vehicle Attribute Classification in Cross-Domain Surveillance Scenarios](https://arxiv.org/abs/2609.01584)

**<font color=#1a73e8>作者：</font>** Sergio M. Silva Jr., Otavio T. Remer, Gabriel E. Lima 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vehicle attribute analysis is a key component of Intelligent Transportation Systems (ITS), supporting applications such as vehicle identification, traffic monitoring, and forensic investigation. However, models trained under controlled conditions often degrade in real surveillance scenarios due to changes in viewpoint, occlusion, illumination, and sensor characteristics. This paper introduces Unconstrained Vehicle Identification Benchmark (UVIB), a benchmark for evaluating three operational vehicle-analysis tasks: front/rear orientation, occlusion-related suitability for Vehicle Make and Model Recognition (VMMR), and color clarity. The benchmark contains 84,835 vehicle images from seven public Brazilian datasets, grouped into surveillance and general acquisition domains, with unified binary annotations that were not jointly available in the original sources. Four representative architectures, EfficientNetV2-S, ResNet-50, ViT/B-16, and YOLO11s-cls, are evaluated under mixed-domain, cross-domain, and cross-dataset protocols. The results show that domain shift has a stronger impact than architecture choice, with substantial degradation in cross-domain settings, especially for VMMR suitability and color clarity. While orientation generalizes more reliably, VMMR suitability remains affected by class imbalance and ambiguous occlusions, and color clarity is highly sensitive to illumination and sensor modality. These findings highlight the need for benchmarks and evaluation protocols that explicitly measure operational robustness beyond standard in-domain accuracy. The proposed benchmark is publicly available at this https URL.

---


### 234. [Designing Proactive Thought Partners for Writing](https://arxiv.org/abs/2609.01588)

**<font color=#1a73e8>作者：</font>** Chao Zhang, Abe Davis, Chih-Wei Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Writing involves diverse cognitive activities, from ideation to revision, and writers' needs vary across individuals and moments. Proactive AI promises to provide the right support at the right time, yet existing proactive tools largely focus on generic textual assistance, such as autocomplete. This paper studies the design space of proactive thought partners: AI agents that proactively offer customizable, higher-level cognitive support during writing. We instantiated this concept in a technology probe and deployed it with 16 participants for one week. The probe allows users to create partners by configuring their roles and proactivity. As users write, relevant partners take the initiative at appropriate moments to offer suggestions. Our findings show that participants configured proactive support through prospective planning, used suggestions for both idea generation and self-monitoring, and valued lightweight visual representations alongside non-directive rhetorical framing for non-intrusive interventions. We derive implications for designing proactive writing assistants around customization, timing, engagement, and representation.

---


### 235. [UI-VISA: U-Net Initialized Vascular Image Segmentation Architecture](https://arxiv.org/abs/2609.01598)

**<font color=#1a73e8>作者：</font>** Asees Kaur, Suzanne S. Sindi, Erica M. Rutter  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate segmentation of vascular structures in digital subtraction angiography (DSA) images remains challenging due to the thin, elongated, and branching nature of blood vessels. Pixel-wise deep learning approaches such as U-Net achieve strong general-purpose segmentation performance but often produce fragmented or discontinuous predictions in fine vascular regions, since they do not explicitly enforce structural connectivity. Region growing algorithms preserve spatial context and topological continuity, but are highly sensitive to seed point initialization and can be computationally expensive. We propose UI-VISA (U-Net Initialized Vascular Image Segmentation Architecture), a hybrid pipeline that combines the complementary strengths of both approaches. UI-VISA uses U-Net's foreground predictions as informed seed points for a CNN-guided region growing algorithm, which then iteratively refines the segmentation by enforcing local connectivity and recovering fine vessel details that U-Net alone tends to miss or over-predict. We evaluate UI-VISA against standalone U-Net and a prior region-growing-based method (VISA) using 5-fold cross-validation on 26 DSA images. UI-VISA achieves the highest mean Dice and clDice scores across folds, and a paired Wilcoxon signed-rank test shows the improvement in clDice is statistically significant ($p=0.023$), consistent with the method's design goal of preserving vascular connectivity, while the improvement in Dice does not reach significance ($p=0.104$).

---


### 236. [Uncovering Understanding-Generation Synergy in Native Unified Multimodal Models: From Representation, Task to System](https://arxiv.org/abs/2609.01607)

**<font color=#1a73e8>作者：</font>** Penghao Wu, Haiwen Diao, Weichen Fan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While unified multimodal models (UMMs) jointly perform visual understanding and generation within a single model, functional unification does not guarantee learning synergy: the two objectives may reinforce each other, compete for capacity, or merely coexist. We investigate their relationship at the representation, task, and system levels in a controlled, structurally native setting without pretrained vision priors. At the representation level, we find that each objective provides useful signal to the other: generation enriches the visual features learned for understanding, while understanding strengthens vision--language alignment for generation. However, when both objectives are forced through the same computation path, one tends to dominate. A task-decoupled architecture that specializes conflicting visual computation while preserving semantic interaction avoids this asymmetric degradation. At the task level, through three case studies, we find positive bidirectional transfer when understanding and generation tasks rely on shared knowledge. At the system level, we show that an end-to-end UMM outperforms a matched planner--executor pipeline on complex tasks that explicitly require both image understanding and generation. Together, these results show that the value of UMMs extends beyond a unified interface: appropriate specialization, shared task knowledge, and end-to-end optimization can turn coexistence into synergy.

---


> [!TIP]
> 当前位于：**201-236**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-236**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
