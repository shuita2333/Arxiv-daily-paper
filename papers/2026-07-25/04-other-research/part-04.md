# 📦 其他研究 | 2026年07月25日

> 本类共 **271** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-271](./part-06.md)

---

### 151. [HiMe: Real-Time Self-Hosted Personal Agent Platform for Health Insights with Wearable Devices](https://arxiv.org/abs/2607.21019)

**<font color=#1a73e8>作者：</font>** Wei Liu, Siya Qi, Linhai Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Traditional approaches to wearable health signal analysis, such as smartwatches, are constrained by rigid analytical frameworks and limited personalisation. The emergence of LLM agents creates a new opportunity for Personal Health Agentic Analysis, where health insights can be generated adaptively and in context. However, currently there is no open-source locally deployable platform capable of processing personal health data in real time while preserving privacy. We present HiMe, a locally deployable, privacy-first agent platform that is fully compatible with real-time health data ecosystems across a wide range of wearable devices. HiMe is guided by three design principles. The database is treated as a first-class component. Effectiveness and efficiency are jointly optimised to achieve a low-cost Pareto-optimal balance. Data are processed in real time while the user is modelled over the long term. Together, these principles make it practical for individuals to harness Personal Health Agents for continuous, personalised health monitoring for better wellbeing.

---


### 152. [WAT3R: Feedforward Underwater 3D Reconstruction](https://arxiv.org/abs/2607.21023)

**<font color=#1a73e8>作者：</font>** Jiayi Xu, Jiahao Lu, Ziqiang Zheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable feedforward underwater 3D reconstruction remains challenging due to severe light attenuation and backscattering, which degrade visual quality and disrupt feature consistency across views, leading to inaccurate multi-view geometry. To address this issue, we propose WAT3R, a feed-forward framework for reconstructing 3D scenes directly from underwater images. By leveraging degradation adaptation as a geometry-constrained process, WAT3R integrates a lightweight neural adaptation module to flexibly account for these underwater imaging effects, thereby improving multi-view reconstruction quality. Implemented in a single forward pass, WAT3R directly and efficiently outputs pixel-aligned 3D point maps and camera poses from underwater videos, allowing a high-quality underwater 3D reconstruction. Experiments conducted on the FLSea, SQUID, and USOD10K datasets show that our method consistently outperforms state-of-the-art approaches on 3D reconstruction tasks, including multi-view/monocular depth estimation and camera pose estimation.

---


### 153. [GroupVideo: Multi-Identity Customized Text-to-Video Generation](https://arxiv.org/abs/2607.21027)

**<font color=#1a73e8>作者：</font>** Xinyang Song, Libin Wang, Jianxin Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current identity customized video generation methodologies are predominantly limited to single-identity scenarios, as the lack of explicit identity separation mechanisms often leads to identity confusion in multi-identity settings. Existing multi-identity approaches, which directly extend single-identity frameworks by concatenating face images as input conditions, frequently result in unnatural facial expressions and motions, manifesting as the "copy-paste" phenomenon. To overcome these limitations, we introduce GroupVideo, a novel framework that leverages multiple individual photographs to generate identitycustomized video. Built upon Video Diffusion Transformers, GroupVideo incorporates multimodal identity alignment: visual alignment jointly encodes multiple face images to provide robust identity references, while semantic alignment introduces a semantic perceiver to enhance the naturalness of motions. An ID localization module with spatial guidance is introduced to address identity blending and enhance identity fidelity, along with bounding box constraints and mask regularization loss, to focus on facial regions and improve training efficiency. In response to the shortage of multi-ID video datasets, we have curated a comprehensive high-quality dataset of 20,000 videos, thereby establishing a crucial resource to advance future research in multi-ID video generation. Extensive experiments demonstrate that GroupVideo outperforms existing methods in generating multi-character videos with consistent identities and natural motions.

---


### 154. [Spectral-Spatial Synergistic Guided Network for Hyperspectral Salient Object Detection](https://arxiv.org/abs/2607.21032)

**<font color=#1a73e8>作者：</font>** Yanyan Peng, Tingfa Xu, Yao Xiao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral salient object detection aims to identify visually salient regions from hyperspectral images. Existing methods often fail because they fundamentally misunderstand the data, confusing incidental spectral variations caused by external factors such as illumination with essential spectral differences caused by the intrinsic material properties of the object. This leads to fragile representations and noisy predictions. To this end, we propose a lightweight and efficient Spectral-Spatial Synergistic Guided Network (S3GNet), with structure perception as the core, to build a closed-loop information flow around spectrum robust modeling, cross-stream co-perception and multi-scale refinement decoding. S3GNet introduces a parameter-free Spectral Structure-Aware Module that leverages spectral derivatives and regional hierarchical modeling to extract intrinsic features of robustness against illumination variations. Our Stream-Aware Attention Module achieves effective spectral-spatial collaboration through inter-stream global interaction and intra-stream spatial guidance. Furthermore, a Progressive Gated Refinement Decoder ensures precise object boundaries and detail recovery by optimally integrating multi-scale features. Experimental results show that S3GNet achieves superior performance in both computational efficiency and detection accuracy compared to existing methods.

---


### 155. [Regularized Optimization on Grassmann Manifold: Theory, Algorithm and Applications](https://arxiv.org/abs/2607.21039)

**<font color=#1a73e8>作者：</font>** Zhuan Liang, Zheng Zhai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spectral methods are among the most widely used techniques for community detection, clustering, and graph learning. Their performance, however, critically depends on the accurate estimation of the underlying spectral subspace and can deteriorate substantially in the presence of noise, outliers, or model perturbations. To address this limitation, we propose a Regularized Projection Matrix Approximation (RPMA) framework for robust estimation of rank-$K$ projection matrices. RPMA extends classical spectral projection by incorporating a regularization term, producing projection estimates that are more robust, sparse, and interpretable. We formulate the proposed model as an optimization problem on the manifold of rank-$K$ projection matrices and exploit its geometric equivalence to the Grassmann manifold. Based on this manifold characterization, we derive the first- and second-order optimality conditions, establish the local stability of the regularized leading eigenspace, and characterize the stability of the critical-point landscape under sufficiently small regularization. To efficiently solve the resulting nonconvex optimization problem, we develop a Riemannian gradient projection algorithm with backtracking line search, together with a more efficient Cayley--Sherman--Morrison--Woodbury (Cayley--SMW) gradient method that avoids repeated eigendecompositions. Extensive experiments on both synthetic and real-world datasets demonstrate that RPMA substantially improves the recovery accuracy of projection matrices and consistently outperforms conventional spectral projection methods for community detection and clustering under noisy environments.

---


### 156. [Faster IndexTTS-2: Accelerating and Streaming Autoregressive Zero-Shot Text-to-Speech Synthesis on GPUs](https://arxiv.org/abs/2607.21042)

**<font color=#1a73e8>作者：</font>** Muyang Du, Shuang Yu, Junjie Lai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autoregressive text-to-speech models achieve strong naturalness but suffer from slow inference due to sequential token generation, limiting their deployment in production applications that require low latency. IndexTTS-2 is a state-of-the-art autoregressive TTS model consisting of a GPT, a flow-matching Diffusion Transformer, and a vocoder. Despite its high synthesis quality, its inference speed barely reaches real-time without streaming or batching support. We present Faster IndexTTS-2, which accelerates all neural network components of IndexTTS-2 for production deployment on GPUs using NVIDIA TensorRT and TensorRT-LLM. Faster IndexTTS-2 also enables streaming synthesis for latency-sensitive interactive applications, and batched inference across all components to maximize GPU utilization. Experiments on the Seed-TTS benchmark for both English and Chinese demonstrate up to 5.0$\times$ speedup on the autoregressive GPT and 3.6$\times$ end-to-end, with minimal degradation in word error rate, speaker similarity, and naturalness. Our methodology provides a practical reference for efficiently accelerating similar autoregressive speech models on GPUs.

---


### 157. [HyperImageNet: A Large-Scale High-Spatial Resolution Hyperspectral Imagery Classification Benchmark](https://arxiv.org/abs/2607.21050)

**<font color=#1a73e8>作者：</font>** Chuguang Zeng, Jingtao Li, Yinhe Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present HyperImageNet, a large-scale benchmark for fine-grained hyperspectral land-cover understanding. The dataset contains 26,084 airborne hyperspectral image patches with 224 spectral bands and 138 fine-grained land-cover categories. Unlike existing datasets, HyperImageNet provides raw imagery, pixel-level semantic labels, and object-level instance masks, supporting both semantic and instance segmentation. Furthermore, we establish an open-environment benchmark with strict spatial separation to evaluate representative methods and the HyperFree foundation model. Experimental results demonstrate the effectiveness of HyperImageNet for fine-grained hyperspectral understanding and open-environment remote sensing research.

---


### 158. [Sample-Efficient Learning from Agent Experience](https://arxiv.org/abs/2607.21051)

**<font color=#1a73e8>作者：</font>** Chenhui Gou, Haoqin Tu, Yunhao Fang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Real-world agent learning is often constrained by costly environment interactions, such as running time-consuming experiments or obtaining human feedback. In-context learning offers a highly sample-efficient way for agents to learn from their own interaction histories, but its gains disappear once that experience is removed from the context. Separately, context distillation provides a mechanism for internalizing contextual information into model weights. However, applying it to agents' interaction histories without sacrificing environment sample efficiency remains underexplored. We term this problem Experience Distillation and develop an implementation that requires no further environment interaction beyond the collected experience. Experiments on 749 curated software-engineering tasks and six text-adventure games show that it retains at least 64.8\% of the gains from in-context learning across both domains, whereas direct supervised fine-tuning on the collected experience recovers only 3.8\%. Compared with classical reinforcement-learning baselines, in-context learning from trial-and-error experience followed by Experience Distillation matches their performance with at least \(9.6\times\) fewer environment samples.

---


### 159. [Achieving Text-based Person Retrieval with Any Granularity](https://arxiv.org/abs/2607.21057)

**<font color=#1a73e8>作者：</font>** Jialong Zuo, Hanyu Zhou, Dongyue Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-based person retrieval faces a critical but under-explored challenge: the inherent uncertainty of query granularity in real-world scenarios. This paper introduces a new paradigm, Text-based Person Retrieval with Any Granularity, and provides a systematic solution. First, we formalize a five-level granularity spectrum and construct UFine6926-MG, a high-quality multi-grained dataset annotated comprehensively at all granularities via a novel Multi-grained Text Annotation Engine. Second, acknowledging that coarse queries naturally correspond to multiple valid candidates, we propose MG-Eval, a holistic evaluation benchmark with progressively detailed texts and cross-identity labels that reflect real-world semantics, alongside tailored evaluation metrics and protocols. Third, after a comprehensive diagnosis reveals the systemic limitations of existing research, we propose the Cross-modal Multi-grained Aligning and Matching (CMAM) framework. CMAM achieves granularity-aware retrieval through: 1) orthogonal-expert perception to disentangle granularity-specific features; 2) probabilistic alignment to model many-to-many matches under query uncertainty; and 3) granularity-consistent reasoning to steer feature learning via joint cross-modal granularity verification. Experiments demonstrate that CMAM significantly outperforms state-of-the-art methods across all granularity levels. This work establishes a foundational benchmark and a robust baseline, paving the way for more practical person retrieval systems.

---


### 160. [Counterfactual Explainability Framework With CycleGAN And Counterfactual-Classifier Alignnment Score for Retinal Disease Classification](https://arxiv.org/abs/2607.21068)

**<font color=#1a73e8>作者：</font>** Kritanu Chattopadhyay, Sayanjit Singha Roy, Soumya Chatterjee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated detection of vision impairing retina-based ocular conditions from fundus images is important for early screening, timely referral and reducing dependency on specialist-only assessment, for which neural network-based deep learning (DL) models have been widely utilized. However, explainability of the DL frameworks remains a major bottleneck for clinical adoption, particularly when model decisions are not linked to retinal regions that are clinically meaningful. To address this issue, this study presents CounterFundus, a novel CycleGAN-driven counterfactual explainability framework, integrating EfficientNet-B5-based retinal disease detection with visually interpretable disease-to-normal fundus image translation. For each pathological image, the counterfactual yielded by the CycleGAN generator represents an estimated healthy counterpart and the resultant difference map is utilized to localize disease-associated retinal changes. Unlike conventional post-hoc saliency methods, CounterFundus provides counterfactual explanations through visually plausible disease-to-normal retinal translation. Thereafter, to quantify the spatial agreement between counterfactual difference maps and classifier saliency, the Counterfactual-Classifier Alignment Score (CCAS) is introduced, embedding Spearman correlation, binary IoU and pointing accuracy into a single assessment protocol. To this end, EigenCAM-aligned evaluation demonstrates that the generated counterfactual explanations remain spatially consistent with classifier-relevant retinal evidence across all CCAS dimensions. Along with that, ablation studies further confirm that CCAS-filtered counterfactual augmentation improves the downstream classification performance in fundus images, establishing CounterFundus as a clinically-grounded, explainable artificially intelligence (XAI) framework for retinal disease detection.

---


### 161. [From Evaluation to Optimisation: Hierarchy-Aware Training Signals for CWE Prediction in Python](https://arxiv.org/abs/2607.21069)

**<font color=#1a73e8>作者：</font>** Muntasir Adnan, Manile Srun, Carlos C. N. Kuhn  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The original ALPHA benchmark introduced a taxonomy-aware penalty for evaluating CWE-level vulnerability prediction in Python and proposed that the penalty could theoretically also serve as a training signal. This paper provides that validation. We compare three delivery mechanisms: supervised fine-tuning, a dual-head classification loss, and reinforcement learning with a dense reward derived from the normalised penalty. We find that supervised approaches consistently regress below the zero-shot baseline under distribution shift, while GRPO succeeds. Our best policy reduces the cumulative ALPHA penalty of Qwen2.5-Coder-7B on Security Hardening and Adversarial Testing (SVEN) dataset by 27.9% under greedy decoding, and by 25.5% under sampled decoding(p = 0.005, Welch's t-test), reaching statistical parity with its 4.5x larger zero-shot teacher. We conclude that the value of a hierarchical penalty as a training signal depends largely on the directness of its delivery.

---


### 162. [TransBiolab: A Real-World Multi-View Dataset of Cluttered Transparent Biomedical Objects](https://arxiv.org/abs/2607.21071)

**<font color=#1a73e8>作者：</font>** Ke Ma, Yifei Wang, Meng Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous biomedical laboratories increasingly rely on visual perception to recognize, localize, and manipulate transparent plasticware, yet high-quality real-world datasets for this setting remain limited. The scarcity of domain-relevant data is particularly restrictive in cluttered multi-object scenes, where mutual occlusion and view-dependent appearance changes remain challenging even for contemporary visual foundation models. Existing transparent-object datasets have advanced segmentation, depth, and pose estimation, but they usually do not evaluate the combined setting of multi-object clutter, occlusion, and calibrated multi-view capture that characterizes real laboratory manipulation scenes. To address this gap, we present TrainsBiolab, a real-world RGB-D dataset of cluttered transparent biomedical objects captured as calibrated multi-view sequences. TrainsBiolab contains 161,315 frames from 98 scenes and 1.03M instance annotations over 15 laboratory object types, including 6D poses, full and visible masks, depth, and per-frame camera calibration. The dataset is organized along three axes that reflect operational difficulty: object category, the total number of objects in a frame, and camera viewpoint. We further define dataset-centric benchmarks for segmentation, depth estimation and completion, and 6D pose estimation, and report a system-level robot manipulation evaluation enabled by the released annotations and calibrations. By focusing on repeated transparent instances, clutter, and multi-view laboratory capture, TrainsBiolab provides a resource for segmentation, depth estimation, 6D pose estimation, and multi-view reasoning in autonomous laboratory manipulation. Project page: this https URL.

---


### 163. [Spectral Transformation for Layer-wise Global Rank Discovery in Federated LoRA for Vision Transformers](https://arxiv.org/abs/2607.21074)

**<font color=#1a73e8>作者：</font>** Hariharan Ramesh, Jyotikrishna Dass  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning Vision Transformers (ViTs) with low-rank adapters (LoRA) promises better communication efficiency under federated setup, yet existing aggregation strategies face fundamental limitations. Independently averaging these LoRA factors is mathematically inconsistent, introducing cross-term aggregation error. In contrast, approaches that preserve heterogeneous client ranks by concatenating local adapters on the server substantially increase download cost and often require merging global LoRA updates into pretrained weights on the clients, causing reinitialization lag and unstable convergence. Other approaches further increase server-side overhead by reconstructing dense weight updates or training auxiliary models to refine aggregation error. In this work, we propose SpecTraL, spectral transformation for layer-wise global rank discovery, that resolves these challenges within a unified design. SpecTraL stacks local LoRA modules from clients and performs orthonormal Householder Transformation of the stacked adapters directly in the low-rank latent space, eliminating dense reconstruction of the global update and any auxiliary refinement on the server. By leveraging the Spiked Covariance Model from Random Matrix Theory, SpecTraL analytically separates the global consensus signal from non-IID noise, discovering optimal layer-wise global ranks without manual hyperparameter tuning. To match local ranks in subsequent rounds, we introduce a padding-aware initialization framework that lets clients incorporate residual LoRA dimensions without re-merging them into the pre-trained base model. Experiments on federated fine-tuning of ViT-B/16 and ViT-L/16 over DomainNet and NICO++ demonstrate improved accuracy-communication trade-offs, reduced server computation, and elimination of hyperparameter search for rank selection. Our code is available at this https URL

---


### 164. [The RealDefocus Benchmark for Defocus Deblurring](https://arxiv.org/abs/2607.21078)

**<font color=#1a73e8>作者：</font>** Tim Seizinger, Zhuyun Zhou, Radu Timofte  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-Image Defocus Deblurring (SIDD) aims to recover an all-in-focus image from a single defocused observation, but rigorous and reproducible evaluation remains challenging due to the scarcity of realistic, high-resolution datasets with well-aligned defocused/sharp pairs and standardized protocols. We build on RealDefocus, a benchmark derived from the real-world RealBokeh dataset originally proposed for Bokeh Rendering. RealDefocus provides paired defocused inputs and sharp ground truth images, predefined training/validation/test splits, and a unified evaluation framework for comparing image restoration and neural rendering approaches. We further outline a benchmarking protocol with cross-dataset validation to assess reconstruction quality and generalization. The project page is publicly available at: this http URL.

---


### 165. [CASC: Causal Adversarial Subspace Clustering for Multivariate Spatiotemporal Data](https://arxiv.org/abs/2607.21088)

**<font color=#1a73e8>作者：</font>** Francis Ndikum Nji, Vandana Janeja, Jianwu Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep subspace clustering plays a critical role in applications involving multivariate spatiotemporal data, such as sea ice monitoring, disease spread analysis, and tracking neuro-degeneration over time. Despite recent advances, existing methods primarily rely on geometric self-expressiveness, assume static subspace structures, and often fail to capture causal dependencies, local spatial interactions, and long-range temporal dynamics inherent in complex spatiotemporal systems. To address these limitations, we propose a novel Causal Adversarial Subspace Clustering (CASC) framework for discovering evolving latent regimes in high-dimensional spatiotemporal data. CASC integrates a U-Net-inspired deep adversarial clustering architecture with stacked FAConvLSTM layers to preserve spatial and temporal structure while learning robust latent representations. A graph attention transformer-based self-expressive network is introduced to jointly model local spatial relationships, global dependencies, and long-range temporal interactions. Furthermore, we propose two new learning objectives: (1) a Causal Subspace Preservation Loss that aligns self-expression coefficients with latent causal relationships, encouraging clusters to reflect underlying causal processes rather than simple feature similarity, and (2) a Dynamic Temporal Subspace Evolution Loss that captures evolving subspace structures and temporal regime transitions in nonstationary environments. Together, these components transform deep subspace clustering from a correlation-driven paradigm into a causal-temporal regime discovery framework.

---


### 166. [Loss Landscape Topology Reveals Why Simple Baselines are Competitive at 3D Point Cloud Segmentation Under Class Imbalance](https://arxiv.org/abs/2607.21089)

**<font color=#1a73e8>作者：</font>** Antonis Savva, Christos Kyrkou, Theocharis Theocharides  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic segmentation of 3D point clouds faces severe class imbalance, yet the effectiveness of specialized imbalance-aware methods from 2D computer vision remains unclear in 3D contexts. We systematically evaluate 11 imbalance mitigation approaches across datasets with extreme (641:1) and moderate (56:1) imbalance ratios, revealing a surprising finding: standard cross-entropy with uniform weighting achieves competitive performance, typically within 0.8-3.3% mIoU of specialized methods across architectures and datasets. Through multifaceted mechanistic analysis of error patterns, decision boundaries, and the geometry of the optimization landscape, our analyses suggest that imbalance severity shapes the topology, creating narrow solution basins under extreme imbalance and flat plateaus under moderate imbalance. This appears to constrain the effectiveness of loss-level modifications, as all methods must navigate these geometric constraints. Our findings offer practical guidance; standard cross-entropy provides a robust baseline, with specialized methods offering modest improvements (0.8-3.3% mIoU) that vary by architecture and dataset but risk substantial degradation if poorly tuned. This work provides the first mechanistic explanation for why techniques proven effective in 2D do not readily transfer to point-based 3D point cloud segmentation, validated across two representative architectures.

---


### 167. [A Polynomial Architecture-Attribution Co-Design Framework for Exact Aumann-Shapley Attribution in GNNs](https://arxiv.org/abs/2607.21094)

**<font color=#1a73e8>作者：</font>** Bizu Feng, Zhimu Yang, Shuming Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study feature-level and node-level explanations for graph neural networks (GNNs) through the lens of Aumann-Shapley attribution. Path-integral methods such as Integrated Gradients provide an axiomatic formulation of attribution, but their practical use in deep GNNs typically relies on finite-sample numerical approximations to the path integral, requiring a trade-off between quadrature error and computational cost. This paper proposes APEX, a model-attribution co-design framework that makes the attribution integral exactly computable under a polynomial GNN architecture. The key component is PolyGIN, a GIN-style graph network whose message-passing, normalization, and transformation operations preserve a bounded multivariate polynomial form for scalar model scores, such as pre-softmax logits. We show that, for a PolyGIN with $L$ polynomial transformation blocks, the derivative along the attribution path has degree at most $2^L-1$. Therefore, Gauss--Legendre quadrature can evaluate the Aumann--Shapley path integral exactly, up to floating-point precision, with $2^{L-1}$ deterministic evaluation points. The resulting attributions can be computed at the feature level and then aggregated into node-level scores while preserving completeness. Experiments on synthetic and real-world graph benchmarks show that PolyGIN maintains competitive predictive performance, while the complete APEX framework achieves higher attribution fidelity than the compared baselines and substantially reduces the number of evaluations required for path integration.

---


### 168. [Smooth Neural Point Processes via B-Splines](https://arxiv.org/abs/2607.21098)

**<font color=#1a73e8>作者：</font>** Michele Bellomo, Riccardo Ramaschi, Alberto Dolara 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temporal point processes (TPPs) provide a general and flexible framework for modeling sequences of events in continuous time. Neural networks have been successfully employed to model TPPs in a highly expressive and data-driven way. Neural TPPs are typically trained via Maximum Likelihood Estimation (MLE) by minimizing the negative log-likelihood (NLL), which depends on both the conditional intensity function (CIF) and its integral over time, the compensator. Recent neural TPP approaches enable exact evaluation of the NLL without numerical integration. However, these methods typically model the compensator rather than the CIF directly, impose constraints on the neural network architecture, and are computationally expensive during training, as event contributions to the NLL are evaluated sequentially rather than in parallel. In this work, we propose a novel neural TPP model that directly parametrizes the CIF as a non-negative combination of B-spline basis functions, whose coefficients are predicted by a neural network. This formulation enables exact evaluation of the NLL, preserves full flexibility in the neural architecture, allows efficient parallelization during training, and naturally supports CIF smoothness regularization through the integrated squared second derivative. Experiments on both synthetic and real-world datasets show improved computational efficiency and predictive accuracy compared to the reference neural TPP baseline.

---


### 169. [Can Generative Recommendation Reach Cold Items? A Temporal Perspective on Semantic-ID Generation](https://arxiv.org/abs/2607.21101)

**<font color=#1a73e8>作者：</font>** Jie Peng, Yanping Zheng, Zhewei Zhe 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Semantic-ID-based generative recommendation represents items as sequences of shared semantic tokens, enabling token recombination beyond isolated item IDs. However, closed-world recombination does not necessarily imply temporal open-token cold-start induction, where new items enter the item catalog with unseen atomic tokens or weakly supported SID paths. In this work, we revisit SID-based generative recommendation under an absolute-time temporal protocol that separates seen and unseen targets and diagnoses the cold item reachability at the token level. Through seen/unseen-hit analysis, coldness taxonomy, and oracle-prefix probing, we show that current SID-based models can occasionally reach future items supported by observed tokens and prefixes, but struggle with unseen atomic tokens and unsupported SID paths. We further explain this boundary by interpreting SID generation as hierarchical semantic bucketing: early tokens select coarse semantic regions, while later tokens refine item-specific paths. These findings show that SID generation is compositional but not fully open-ended, and suggest future directions in more independent SID spaces, scoring-based interfaces, and dynamic textual context.

---


### 170. [AttriMem: Attribution-Guided Process Feedback for Agent Memory Learning](https://arxiv.org/abs/2607.21106)

**<font color=#1a73e8>作者：</font>** Qinfeng Li, Yuntai Bao, Xinyan Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Effective memory is crucial for LLM agents, yet constructing it effectively remains challenging. A memory-construction policy decides what information to extract, store, update, compress, or discard as interactions accumulate. Heuristic memory methods rely on subjective, task-specific rules, which can misalign with downstream objectives and limit cross-task adaptability. RL-based methods, by contrast, learn from task feedback but mainly use outcome- or module-level rewards. These coarse signals indicate task success but cannot identify which intermediate memory contents support the final answer, creating a fine-grained credit-assignment bottleneck. However, constructing such process feedback is prohibitively difficult because intermediate memory decisions lack unique ground-truth targets, while the appropriate credit varies with the agent's uncertain reasoning trajectory and therefore cannot be specified in advance. We propose AttriMem, an attribution-guided process-feedback framework for learning memory-construction policies with RL. AttriMem augments the global outcome reward with local rewards derived from token-level contributions to the final answer. Experiments on long-horizon dialogue question answering show that AttriMem outperforms retrieval-based, heuristic, and RL-based baselines, generalizes across benchmarks and answer models, stabilizes RL optimization.

---


### 171. [TOUR: A Trajectory-Level Unlearning Benchmark for Offline Reinforcement Learning](https://arxiv.org/abs/2607.21111)

**<font color=#1a73e8>作者：</font>** Chaofan Pan, Lingfei Ren, Xiangyu Jiang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline Reinforcement Learning (RL) agents are trained on fixed behavioral trajectories, which makes trajectory-level deletion important when selected data must be removed after training. Evaluating such deletion is difficult because a lower membership score can reflect trajectory removal, residual memorization visible to another attack, or policy collapse that destroys useful behavior. We introduce Trajectory-level memOrization and Unlearning in offline RL (TOUR), a benchmark that combines trajectory-level partitioning, matched non-member controls, retraining references, retained-performance anchors, and multi-attack privacy auditing. Across D4RL locomotion experiments and an exploratory AntMaze extension, TOUR shows that common deletion baselines have environment-dependent privacy-utility behavior. Retraining and fine-tuning often provide stronger retained-utility references than uniform GA+Refit, while TrajDeleter remains a useful comparator but is not uniformly stronger under the same audit. Reference-model, threshold, deviation, equivalence, action-error, representation-based, and query-limited attacks further show that a single likelihood-based membership score can overstate deletion quality. In the evaluated settings, conclusions about offline RL unlearning are therefore not stable under single-score auditing. They depend on matched non-member construction, retraining-relative calibration, attack family, retained utility, and explicit scope for diagnostic architecture or component-level evidence.

---


### 172. [GlucoTune: A Unified Framework for Blood Glucose Preprocessing, Forecasting, and Benchmarking in Diabetes](https://arxiv.org/abs/2607.21117)

**<font color=#1a73e8>作者：</font>** Davide Marelli, Giorgia Rigamonti, Mirko Paolo Barbato 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Preprocessing blood glucose time-series data is a critical yet often overlooked step in developing data-driven methods for diabetes management, particularly for type 1 diabetes. The lack of standardized preprocessing workflows and evaluation protocols hinders reproducibility and complicates fair comparison across studies. These challenges are further exacerbated by data-sharing restrictions, as privacy and licensing constraints often prevent the redistribution of preprocessed medical datasets. To address these limitations, we present GlucoTune, a comprehensive and extensible framework for reproducible experimentation with blood glucose time-series data. The framework standardizes the entire experimental workflow, from preprocessing to model evaluation, enabling reproducible experiments directly from the original datasets. Reproducible preprocessing is achieved through configurable pipelines defined in portable YAML configuration files, ensuring consistent data handling without distributing sensitive preprocessed data. Beyond preprocessing, GlucoTune provides a unified interface for implementing, training, and evaluating blood glucose prediction models. The framework integrates public datasets through standardized wrappers and provides a curated collection of state-of-the-art blood glucose prediction and general time-series forecasting methods, while remaining readily extensible to additional datasets, preprocessing strategies, and forecasting models. To promote transparent and consistent evaluation, GlucoTune includes a benchmarking leaderboard that reports results across datasets, preprocessing configurations, and forecasting methods, enabling systematic comparison of experimental settings. We demonstrate the effectiveness of GlucoTune through comprehensive experiments and assess its usability in a user study.

---


### 173. [The Second LoViF 2026 Challenge on Real-World All-in-One Image Restoration: Methods and Results](https://arxiv.org/abs/2607.21118)

**<font color=#1a73e8>作者：</font>** Xiang Chen, Hao Li, Jiangxin Dong 等 92 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents a review of the second LoViF Challenge on Real-World All-in-One Image Restoration. The challenge aims to advance unified image restoration under diverse real-world degradation conditions, including blur, low-light, haze, rain, and snow. It provides a common benchmark for evaluating the restoration accuracy, robustness, and generalization capability of models across multiple degradation categories within a unified framework. The competition attracted 158 registered participants, and 20 teams were included in the final ranking after their submitted results were successfully reproduced and verified. This report provides a comprehensive analysis of the submitted solutions and corresponding results, highlighting recent advances in real-world all-in-one image restoration. The summarized methods and empirical findings reveal effective design strategies and establish an updated benchmark for future research in real-world low-level vision.

---


### 174. [Relative Value Learning](https://arxiv.org/abs/2607.21120)

**<font color=#1a73e8>作者：</font>** Marc Höftmann, Jan Robine, Stefan Harmeling  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In reinforcement learning, critics typically estimate absolute state values $V(s)$, estimating how good a particular situation is in isolation. However, it turns out that only differences in value are relevant for control. Motivated by this, we propose Relative Value Learning (RV), a framework that learns value differences directly via an antisymmetric function $\Delta(s_i, s_j) = V(s_i) - V(s_j)$. We introduce a pairwise Bellman operator and prove it is a $\gamma$-contraction with a unique fixed point equal to the true value differences, derive well-posed $1$-step, $n$-step and $\lambda$-return targets and reconstruct generalized advantage estimation from pairwise differences to obtain an unbiased policy-gradient estimator (R-GAE). Beyond theoretical results, we integrate RV with PPO and achieve competitive performance on the Atari benchmark (49 ALE games) compared to standard PPO, indicating that relative value estimation is an effective alternative to absolute critics.

---


### 175. [Causal-AgentIR: Self-Evolving Causal Memory for Adaptive Image Restoration Agents](https://arxiv.org/abs/2607.21125)

**<font color=#1a73e8>作者：</font>** Hu Gao, Yulong Chen, Lizhuang Ma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image restoration agents have recently emerged as a flexible paradigm for handling diverse and unpredictable degradations in real-world scenarios. Existing agents typically formulate restoration as a tool-using process, where the agent perceives degradations, searches candidate tools, executes restoration operations, and revises the plan through reflection or rollback. However, their knowledge is often stored as static tool descriptions, manually defined degradation priors, or unstructured textual summaries, which limits the accumulation, verification, revision, and forgetting of restoration knowledge over long-term experience. In this paper, we propose Causal-AgentIR, a hierarchical multi-agent framework with self-evolving causal memory for collective image restoration intelligence. Instead of representing restoration experience as isolated textual records, Causal-AgentIR organizes degradation patterns, image regions, restoration tools, actions, quality changes, and user preferences into a structured causal memory graph. This graph supports graph-based retrieval and multi-hop causal reasoning, enabling agents to infer how specific restoration operations or tool sequences affect restoration quality under different degradation conditions. The framework further organizes multiple agents into a collaborative system, including planning, degradation analysis, tool expertise, causal memory reasoning, outcome critique, and memory curation. Through this design, restoration experience can be added, updated, merged, reinforced, ignored, or discarded according to observed quality changes and feedback, allowing the agent to maintain reliable and transferable restoration knowledge.
Extensive experiments demonstrate the effectiveness of the proposed framework.

---


### 176. [Demographically-Informed Heat-Mortality Risk Curves via Risk Graph Neural Networks](https://arxiv.org/abs/2607.21131)

**<font color=#1a73e8>作者：</font>** Alex O. Davies, Eunice Lo, Rui Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating heat-related mortality risk is a core task in environmental epidemiology, typically addressed with Distributed Lag Non-linear Models (DLNMs); interpretable exposure-response surfaces fitted to temperature-mortality time series. DLNMs are effective but ignore demographic and geographic context, despite well-established relevance to heat vulnerability. We propose Risk Graph Neural Networks (RGNNs), a hierarchical GNN encoder that uses granular census features to optimise DLNM coefficient vectors, preserving interpretable risk curve outputs while substantially improving predictive calibration. Evaluated across 10 regions of England and Wales on two unprecedented heat years, RGNN variants maintain both lower point-errors and near-nominal uncertainty coverage during the 2022 heatwave where baselines collapse.

---


### 177. [Safety-oriented sidewalk and road segmentation for smartphone-based assistive navigation](https://arxiv.org/abs/2607.21137)

**<font color=#1a73e8>作者：</font>** Hakan Calim, Anamaria Dumitrescu, Adarsh Bhandary Panambur 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Independent sidewalk mobility is essential for blind and visually impaired pedestrians (BVIPs), yet smartphone-based assistive navigation requires perception models that distinguish walkable sidewalks from adjacent unsafe regions. This study presents a safety-oriented semantic segmentation framework for future mobile guidance. We introduce SENSATION-DS, a chest-height pedestrian-view dataset with 2,752 image-mask pairs and nine-class navigation-relevant taxonomy. External urban and sidewalk datasets were harmonized to this label space, and five segmentation architectures were evaluated using staged target-domain adaptation with mask-conditioned synthetic images and Segment Anything Model 2 (SAM2) pseudo-labels. Models were assessed using mean Intersection over Union (mIoU), road- and sidewalk-specific metrics, Road-as-Sidewalk Error Rate as a proxy false-safe measure, and Android Open Neural Network Exchange benchmarking. Synthetic augmentation generally improved segmentation accuracy, whereas SAM2 pseudo-labels more consistently reduced Road-as-Sidewalk errors. UPerNet-MobileNetV3 achieved the highest offline mIoU (0.715 +/- 0.006), while DeepLabV3Plus-MobileNetV3 achieved the lowest Road-as-Sidewalk Error Rate (0.079) and highest Android runtime at 512x384 (7.383 FPS). These results show that assistive sidewalk perception should be evaluated jointly by segmentation accuracy, proxy false-safe behavior, and smartphone deployment feasibility, while real-world benefit requires validation with BVIP users. This evaluation supports selecting models that balance accurate perception, conservative error behavior, and practical runtime.

---


### 178. [DTIF: Robust Loop Closure Detection via Delaunay Triangle Topology in Complex Forests](https://arxiv.org/abs/2607.21138)

**<font color=#1a73e8>作者：</font>** Xin Zhao, Jianping Li, Qin Zou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate forest inventory and large-scale mapping are essential for ecosystem monitoring and sustainable forest management. Multiple low-cost edge platforms enable efficient large-area data acquisition, but merging independently constructed local maps in GNSS-denied understory environments still requires initialization-free loop closure detection and global registration. This task is challenging because low-cost LiDAR point clouds are sparse and noisy, while repetitive trunk layouts and the lack of distinctive geometric landmarks lead to severe perceptual aliasing and false correspondences. To address these issues, we propose DTIF (Delaunay Triangulation in Forests), a lightweight trunk-topology-based framework for forest loop closure detection and global registration. Tree trunks are first extracted as stable landmarks and encoded using a Delaunay topology for compact scene representation. Candidate submaps are then screened using edge-length and radius statistics, followed by edge--radius consistency verification and strong/weak vertex support aggregation to construct weighted vertex correspondences. Finally, topology-derived reliability weights are incorporated into a decoupled robust pose estimator that separately estimates yaw, horizontal translation, and elevation translation under gravity alignment. Experiments on simulated and real-world forest datasets demonstrate that DTIF achieves accurate registration with low computational overhead, providing a favorable balance among robustness, efficiency, and deployability on resource-constrained edge platforms.

---


### 179. [SafeStep: AI-powered Travel Assistance for Elderly People with Frailty or Dementia](https://arxiv.org/abs/2607.21156)

**<font color=#1a73e8>作者：</font>** Elderly People with Frailty or Dementia Azul Debenedetti, David Gamez, Franco Such 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> More than a million people in the UK suffer from frailty or dementia, which severely compromise their ability to travel in urban environments. This paper presents SafeStep, an AI-driven travel system that assists elderly users with their journeys. At the core of SafeStep is a novel travel graph representation, which integrates route planning with predictive modelling. For each stage of a journey, the system (i) generates personalized failure scenarios using a combi-nation of LLMs and the Anticip8 behavioral prediction engine, (ii) proposes targeted interventions, and (iii) estimates the impact of interventions on out-come probabilities. This enables SafeStep to select interventions that maximize the likelihood of the person reaching their destination. SafeStep was evaluated through experiments on travel graph generation and a field study involving 26 real-world journeys. Results showed that combining Anticip8 for failure pre-diction with GPT-based models for intervention evaluation yields the most re-liable performance. User feedback indicated that SafeStep improves confidence and perceived safety during travel, although interface usability needs to be im-proved for the target demographic. In the future, we would like to improve and release SafeStep. The AI system that was developed for SafeStep could be ap-plied in other areas, such as mental health, career coaching and addiction treatment.

---


### 180. [Agree on the Model, Verify the Inference: GKR Protocols for HND-Based Transformer Inference](https://arxiv.org/abs/2607.21162)

**<font color=#1a73e8>作者：</font>** Xiaolong Liang, Juanjuan Li, Rui Qin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Outsourced Transformer inference exposes clients to model substitution and incomplete execution, while direct replay removes the computational benefit of delegation. We present GKR-HND, a registered-model protocol for verifying the polynomial backbone of Homomorphic--Nonhomomorphic Decomposition Transformers. The retained verifier checks the GKR transcript and registered-weight openings, but delegates expensive public evaluations to an assigned computation worker. Assuming an honest retained verifier and prover--worker non-collusion, the verifier accepts only when the worker's signed, request-bound response agrees with the proof claims. Experiments with pretrained HND models validate the proof path and the delegated public computation without dense-matrix replay.

---


### 181. [Automated Synthesis and Adversarial Validation of Executable Causal Research Pipelines](https://arxiv.org/abs/2607.21173)

**<font color=#1a73e8>作者：</font>** Irena Girshovitz, Dan Zeltzer, Ran Gilad-Bachrach  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While automated research systems promise to accelerate empirical analysis, they are prone to silent failures: instances in which analysis code executes successfully yet relies on invalid causal assumptions. We present the Artificial Intelligence (AI)-based Epidemiology Research Assistant (ARA), a framework that makes these failures visible by explicitly encoding causal design principles, study-specific assumptions, and methodological constraints. ARA integrates protocol construction, synthetic data generation, and adversarial validation into a unified pipeline. The framework translates natural language research questions into structured causal protocols and executable analysis code by first constructing a protocol and then generating synthetic datasets using Structural Causal Models (SCMs) with known ground-truth effects. This synthetic-data step can also support pipeline development when access to confidential data, such as medical data, is restricted. The generated analysis is then evaluated under controlled violations of identification assumptions. We evaluate ARA on the Automated Causal Reasoning Benchmark, assessing recovery of identification strategies, causal quantities, treatment and outcome variables, and consistency between generated code and approved protocol. Protocol construction and adversarial validation did not consistently improve numerical agreement with benchmark estimates compared with standard LLM-based generation. However, they changed the failure mode: instead of silently returning causal estimates, ARA often surfaced protocol concerns, diagnostic failures, incomplete inference, or downgraded non-causal interpretations. These findings suggest that validity-first automated science systems should be evaluated not only by answer accuracy, but also by whether they indicate when causal claims are unwarranted.

---


### 182. [Explaining Weather Bulletins via ILP](https://arxiv.org/abs/2607.21184)

**<font color=#1a73e8>作者：</font>** Enrico Santi, Alessandro Dal Palù, Agostino Dovier 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Inductive Logic Programming (ILP) originated within the Logic Programming community in the Nineties as a framework for combining symbolic learning with declarative knowledge representation. Nowadays, mature ILP frameworks exist and they are capable of learning complex, non-monotonic hypotheses, thus broadening both the modeling capabilities and the scope of real-world applications of ILP. This work is primarily based on the FastLAS2 framework and aims to generate simple, interpretable hypotheses to help clarify the weather bulletins issued by OSMER FVG, the Regional Meteorological Observatory of the Italian region of Friuli Venezia-Giulia. In this paper we present a pipeline that, starting from simulated meteorological raw data and from OSMERs' bulletins (used as ground truth), extracts data as ASP facts and generates ILP examples. From such examples an explanatory hypothesis is then inferred via FastLAS2. Such a hypothesis (translated into natural language) explains the weather forecast issued by human experts, and in particular the rationale behind experts' choices of specific symbols in the bulletin pictogram (the symbol-annotated meteorological map of the forecast). The proposed approach is general, not specific to any particular region and it can equally be applied to bulletins from other sources and to different regions.

---


### 183. [Differentiable Logic Programming to Mitigate Reasoning Shortcuts in Neurosymbolic Systems](https://arxiv.org/abs/2607.21185)

**<font color=#1a73e8>作者：</font>** Akihiro Takemura, Katsumi Inoue  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neurosymbolic (NeSy) systems integrate neural networks with logical reasoning to achieve both generalization and interpretability, but recent work has shown they are susceptible to shortcut reasoning behaviors.  We propose a novel method using matrix-based differentiable logic programming to mitigate reasoning shortcuts in two phenomena: constraint satisfaction shortcuts, where constraints are satisfied without achieving the intended task, and cognition shortcuts, where biased data leads to semantically incorrect concept mappings despite logically sound inference. Building on recent matrix-based logic programming semantics, we introduce design elements to mitigate shortcuts, including a unified encoding of rules and constraints in a single matrix.  We also identify connections to fuzzy logic t-norms and empirically compare their gradient flow properties. Through carefully designed experiments on MNIST variants, we show that one-to-one grounding of neural outputs to logical atoms significantly reduces both shortcut types compared to previous methods that rely on soft probability distributions.  We then confirm that architectural choices in coupling symbolic knowledge with neural learning play a critical role in shortcut mitigation.

---


### 184. [Identifying Good Rules for Efficient SAT Encodings of Single-Constant Multiplication Using Machine Learning](https://arxiv.org/abs/2607.21188)

**<font color=#1a73e8>作者：</font>** Chufeng Jiang, Neng-Fa Zhou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Single Constant Multiplication problem is a fundamental NP-hard optimization task in hardware design, which seeks to decompose a fixed constant using only additions, subtractions, and bit-shifts. Although dynamic programming methods can produce near-optimal SAT encodings for SCM, their encoding cost remains high for large constants. We propose a neuro-symbolic framework that accelerates SCM SAT encoding by identifying good rules for guiding operator selection during decomposition. Our approach employs a graph neural network model to predict promising operator types from constant decompositions, and exploits the resulting confidence scores to prune no-good choices in the symbolic search. Experimental results on unseen 17-32 bit constants demonstrate one to two orders of magnitude reductions in encoding time, over 97% reduction in memory usage, and an order-of-magnitude decrease in branching, while preserving near-optimal encoding quality in terms of additions. These results show that learning-guided symbolic strategies can significantly improve the scalability and efficiency of SCM encoding. Our code and data are publicly available at: this https URL

---


### 185. [Physics-Informed Deep Learning Model for Cross-Modality Super-Resolution in Fluorescence Microscopy](https://arxiv.org/abs/2607.21190)

**<font color=#1a73e8>作者：</font>** Mohammad Soltaninezhad, Elena Corbetta, Francisco Paez Larios 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-modality image translation offers a route to super-resolution fluorescence microscopy from low-resolution images while reducing phototoxicity and instrumentation demands. However, purely data-driven models can produce visually plausible outputs that are inconsistent with optical image formation. Here, we propose a physics-informed generative adversarial network for confocal-to-STED image translation that incorporates microscope-specific point spread function information into the training objective. Simulated and experimentally measured PSFs were evaluated using a limited paired confocal-STED dataset of TOM20-labeled mitochondria in human primary M2 macrophages acquired across different experimental days. Performance was assessed using reference-based and non-reference-based image-quality metrics, together with complementary frequency- and distribution-sensitive analyses. The no-reference metrics probed physics-relevant image properties, including spatial-frequency content, contrast, and signal-to-noise behavior. PSF-guided models improved structural fidelity, reduced local deviations, and achieved closer agreement with STED references than non-PSF baselines, particularly in frequency-domain analyses. These results demonstrate that optical priors can improve the structural fidelity and physical plausibility of generative microscopy models for cross-modality super-resolution imaging.

---


### 186. [Bound-Founded Semantics for Answer Set Programming with Difference Constraints: Preliminary Report](https://arxiv.org/abs/2607.21201)

**<font color=#1a73e8>作者：</font>** Pedro Cabalar, Jorge Fandinno, Nicolas Rühling 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While the integration of linear constraints has significantly expanded the reach of Answer Set Programming (ASP), existing hybrid solvers often rely on disparate semantic underpinnings that lack a unified logical foundation. We address this gap by introducing a many-sorted variant of the Bound-founded Logic of Here-and-There (HTb), providing a versatile framework capable of characterizing equilibrium models across a wide spectrum of alternative semantics for extensions of ASP with linear constraints. We apply this framework to the setting of difference constraints, focusing on the semantic characterization of clingo[DL]. Central to our approach is the formalization of foundedness for numeric variables. By investigating how different hybrid systems - such as clingo[DL], clingcon, and flingo - justify constraint atoms, we uncover the semantic roots of their varying behaviors. This investigation results in a single, consistent framework that not only formalizes the foundations of current systems like clingo[DL] but also facilitates the rigorous study of program simplifications and the future integration of diverse semantic principles.

---


### 187. [A New Well-Supported Semantics for Description Logic Programs](https://arxiv.org/abs/2607.21203)

**<font color=#1a73e8>作者：</font>** Spencer Killen, Jia-Huai You  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Description logic programs are a powerful formalism for combining rules with ontologies. The well-supported semantics for description logic programs ensures that no answer sets rely on cyclic dependencies. Most popular semantics for logic programming have this property of well-supportedness. We recognize two limitations of the current well-supported semantics for DL programs: its increased computational complexity for the consistency problem and its lack of a reduct transformation characterization.  In this work, we present a new semantics which evaluates ontological atoms more strictly than the current semantics. This keeps the complexity of its consistency problem NP-complete, rather than increasing it to the second level of the polynomial hierarchy. Additionally, we identify a syntactic class of description logic programs for which our new semantics is equivalent to the current semantics. We characterize our semantics using a fixpoint operator and a reduct-based transformation. Our new semantics is a strict subset of the current well-supported semantics, so it maintains the prior notion  of well-supportedness while inducing its own stricter notion. We prefer our new notion of well-supportedness due to its similarities with logic programming.

---


### 188. [How Rules Represent Causal Knowledge: Causal Modeling with Probabilistic Logic Programming](https://arxiv.org/abs/2607.21208)

**<font color=#1a73e8>作者：</font>** Kilian Rueckschloss, Felix Weitkaemper  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pearl famously argues that causal knowledge enables the prediction of intervention effects. By contrast, purely descriptive knowledge supports only conclusions drawn from observations. His theory of causality, however, is developed exclusively within Bayesian networks and causal models. Consequently, it is largely restricted to acyclic causal relationships, and transferring its ideas to other formalisms risks misinterpretation or inconsistency.
This paper brings Pearl's approach to causality into probabilistic logic programming (PLP). To this end, such programs are aligned with philosophical foundations established in prior work that do not rely on temporal notions; that is, all relevant events are assumed to occur simultaneously. A formal causal semantics for these programs, together with a notion of intervention and an implementation, is proposed. It is shown that this semantics coincides with the P-log semantics for stratified ProbLog programs, while the two may differ in the non-stratified case and for other PLP formalisms.

---


### 189. [Learning-based Seam Correspondence Reconstruction in Sewing Patterns](https://arxiv.org/abs/2607.21213)

**<font color=#1a73e8>作者：</font>** Zhendong Wang, Jintong Wang, Chen Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Digital sewing patterns typically consist of disjoint 2D panels without explicit stitch annotations, making downstream 3D modeling reliant on labor-intensive expert specification. In this paper, we present a graph-based learning framework that reconstructs two-level stitching information, coarse panel connectivity and fine-grained seam correspondence, from 2D panel geometry alone. At the coarse level, panel connectivity is inferred by predicting panel semantics associated with anatomical body regions, enforcing consistency with body structure and garment design conventions. Based on the reconstructed panel graph, fine-grained seam correspondences between panel pairs are inferred by learning latent edge representations that jointly encode local seam geometry and global garment context through graph message passing. The resulting edge embeddings are subsequently decoded into detailed seam correspondences. Our method supports complex sewing-pattern topologies, including many-to-one correspondences, intra-panel seams, and curved seams. Experiments demonstrate high stitching accuracy and strong generalization across garment styles.

---


### 190. [ICAE-Bench: Evaluating Coding Agents as Interactive Project Builders](https://arxiv.org/abs/2607.21217)

**<font color=#1a73e8>作者：</font>** Zhongyuan Peng, Dan Huang, Chuyu Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The recent emergence of vibe-coding workflows is changing what coding agents are expected to do. Instead of merely completing code under fully specified instructions, agents are increasingly expected to transform incomplete product intent into working software by combining various abilities including planning, requirement clarification, tool use, debugging, and repository-level construction. Yet existing benchmarks have not fully caught up with this shift, evaluating agents on static, fully specified tasks.
In this paper, we introduce ICAE-Bench, a benchmark for evaluating coding agents under interactive project-building settings. The basic idea is to start from a fuzzy product requirement, simulating the dynamic paradigm with an automated User Agent. To make this setting both realistic and evaluable, ICAE-Bench introduces three key designs. First, to avoid the ambiguity of unconstrained fuzzy requirements, each task derives ambiguity from a precise real open-source repository with executable behavior. Second, to ensure high-quality and reproducible user simulation, ICAE-Bench grounds interaction through User Agent Data, allowing the User Agent to reveal hidden constraints without inventing new requirements or leaking implementation artifacts. Third, to evaluate open-ended repositories fairly, ICAE-Bench uses standardized black-box tests together with multi-dimensional diagnostics, including functional correctness, semantic and API similarity, structural fidelity, design quality, and interaction quality.

---


### 191. [DART: A Degradation-Aware Recurrent Transformer for Archival Film Restoration](https://arxiv.org/abs/2607.21219)

**<font color=#1a73e8>作者：</font>** Mikołaj Jastrzębski, Wojciech Kozłowski, Kamil Adamczewski  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Archival film restoration is a challenging problem because historical footage contains compound degradations such as scratches, dust, blur, noise, flicker, and photometric aging, while clean reference videos are unavailable. Existing video restoration methods largely treat these degradations implicitly, reconstructing frames without explicit knowledge of where damage occurs or how severe it is. We propose DART, a degradation-aware recurrent transformer for archival film restoration. DART predicts and propagates a soft defect mask through time, using it to guide temporal fusion and condition the restoration network on both damage location and severity. This makes the restoration process explicitly aware of film artifacts rather than relying only on reconstruction losses. Experiments on real archival benchmarks show that DART improves no-reference perceptual quality over prior restoration architectures while remaining compact and efficient, producing cleaner and more temporally consistent restorations of structured film damage.

---


### 192. [T-STAR: A Large-Scale Benchmark for Spatio-Temporal Panoptic Scene Graph Generation in Satellite Video](https://arxiv.org/abs/2607.21228)

**<font color=#1a73e8>作者：</font>** Linlin Wang, Xue Yang, Zhihuang Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Structured understanding of satellite video is essential for advancing dynamic geospatial scene analysis from low-level perception to high-level cognition. To move beyond object-centric perception, this paper introduces spatio-temporal panoptic scene graph generation (TPSG) in satellite video as a new benchmark task. TPSG aims to generate a structured graph composed of a set of triplets <subject, relationship, object> with explicit temporal spans, thereby describing dynamic geospatial scenes by jointly modeling identity-consistent instance masks and spatio-temporal relationships among panoptic scene elements. However, there is still no dedicated dataset for TPSG in satellite video. Moreover, TPSG in satellite video is intrinsically challenging, as objects are often small and weakly textured, cross-frame association is easily disrupted by occlusion and background clutter, and relationship semantics are highly coupled with spatial structure and temporal evolution. Consequently, TPSG models developed for natural videos are not directly applicable to satellite video. This paper presents T-STAR, a large-scale benchmark dataset for TPSG in satellite video, comprising over 1.1 million instance masks and over 3.8 million spatio-temporal triplets across 39 fine-grained object categories and 70 fine-grained relationship categories. To enable TPSG in satellite video, we propose a unified framework to enhance cross-frame instance consistency and spatio-temporal relationship prediction. Extensive experiments demonstrate the significance of T-STAR and the effectiveness of the proposed framework, establishing a strong benchmark for future research on structured satellite video understanding. The dataset and code are available at this https URL.

---


### 193. [Progressive Cramming: Reliable Token Compression and What It Reveals](https://arxiv.org/abs/2607.21231)

**<font color=#1a73e8>作者：</font>** Dmitrii Tarasov, Timofei Lashukov, Elizaveta Goncharova 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Token cramming compresses sequences into learned embeddings with near-perfect reconstruction, but fixed token budgets and 99\% accuracy thresholds leave it unclear whether residual errors reflect optimization failures or fundamental limits. We introduce progressive cramming, which grows the target prefix token-by-token, stopping only when reconstruction is no longer achievable within a fixed optimization budget. Progressive trajectories occupy low-dimensional structure in embedding space. Prepending a crammed embedding causes a moderate but consistent accuracy drop on multiple-choice benchmarks even with the original prefix in context, and collapses capability almost entirely under generative evaluation. Causal attention-knockout interventions trace this degradation to the embedding's interactions in the model's early layers. These results position progressive cramming as a tool for studying compression limits and show that perfect reconstruction - achievable through brittle steering rather than transferable semantics - is insufficient for meaningful compression.

---


### 194. [Logic Programming Semantics for Causal Processes](https://arxiv.org/abs/2607.21233)

**<font color=#1a73e8>作者：</font>** Felix Weitkämper  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Motivated by challenging modelling issues in the life sciences, we investigate the relationship between logic programming semantics and the eventual states of causal processes compatible with those logic programs. More precisely, we show that while stable models of positive logic programs correspond to the eventual states of processes commencing from a neutral state and continuing undisturbed indefinitely, supported models describe the eventual states reachable from arbitrary starting points. This also contributes to the discussion of the appropriate semantics for logic programming as a causal rule language, adding a temporal perspective to recent interpretations of the stable and supported model semantics from an explanatory viewpoint of causality.

---


### 195. [Stokes-Informed Diffusion for Robust Linear Polarization Estimation](https://arxiv.org/abs/2607.21239)

**<font color=#1a73e8>作者：</font>** Yidong Luo, Chenggong Li, Yuchao Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Polarization cues benefit applications such as material detection and de-reflection, yet acquiring them typically requires dedicated hardware. This motivates us to estimate the linear polarization from a single RGB image. However, the task is inherently ill-posed, with the Angle of Polarization (AoP) becoming particularly unstable in weak polarization regions, where the polarimetric signal is overwhelmed by noise, leading to erratic angle estimates. To address these limitations, we propose GenPolar, a Stokes-informed diffusion framework grounded in the Mueller formalism from an intensity observation. Specifically, GenPolar predicts channel-wise linear Stokes components (S1,S2) from intensity S0, from which degree of linear polarization (DoLP) and AoP are analytically derived; AoP is further supervised with an observability-aware loss. In addition, to enable efficient and high-fidelity inference, we adopt a two-stage training strategy. Firstly, a multi-step conditional diffusion model is trained with a physics-based loss. Subsequently, we distill it into a one-step generator, which further supports stable Low-Rank Adaptation (LoRA) of the VAE encoder to mitigate domain-specific autoencoding bias. Extensive experiments across rotating-polarizer, division-of-focal-plane, and hybrid datasets demonstrate that GenPolar achieves state-of-the-art performance in both DoLP fidelity and AoP stability. Crucially, these improvements translate to significant and consistent gains in downstream applications, including material detection and de-reflection.

---


### 196. [Detectors Learn the Wrong Thing: Shortcut-Resistant Adversarial Training Against Physically Realizable Attacks](https://arxiv.org/abs/2607.21243)

**<font color=#1a73e8>作者：</font>** Yuanhao Huang, Yilong Ren, Jinlei Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-enabled visual perception systems are increasingly deployed in intelligent transportation infrastructure and autonomous vehicle related applications. However, physically realizable adversarial appearances pose a significant reliability challenge for these safety-critical systems. Adversarial training is effective, but repeated co-occurrence between adversarial texture and positive person instances can cause detectors to treat the texture itself as evidence of object presence, forming a patch texture shortcut. The detector may then treat texture as evidence for the target, causing false detections on texture-only inputs and weakening cross attack generalisation. We propose InsCAT, an instance-level contrastive adversarial training framework that prevents detectors from using adversarial texture as an independent decision cue. SICA aligns adversarial person features with matched clean features and separates them from texture-only negatives, while ROPO and Guard maintain online attack pressure and coordinate training. We evaluate eight independently generated attack textures on rendered nuScenes, INRIAPerson, printed garments, and three detector families. InsCAT achieves an average attack AP of 82.3% on rendered nuScenes, exceeding the strongest baseline by 11.1 this http URL to AT-Mix, texture FPR decreases from 46.9% to 7.3%. Physical tests yield an F1 score of 96.6% and an FPR of 1.8%. Consistent gains across separately trained detectors demonstrate applicability across architectures with direct inference. The findings show that robust physical detection depends on preserving target related evidence while preventing adversarial texture from becoming an independent decision cu

---


### 197. [slang.gr as a Large-Scale Crowdsourced Resource for Non-Standard Greek](https://arxiv.org/abs/2607.21255)

**<font color=#1a73e8>作者：</font>** Panagiotis Papadakos, Katerina Papantoniou, Dimitris Plexousakis  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Slang is a central component of everyday language, reflecting linguistic creativity, social identity, and cultural change, yet its dy- namic and non-standard nature makes it difficult to model computationally. We present the first large-scale computational study of this http URL, a crowdsourced lexicon of Greek non-standard language, combining lexical content, user-generated tags, and interaction data. To enable the systematic analysis, we map noisy folksonomic tags to a structured multi-layer taxonomy capturing both semantic categories and sociolinguistic metadata. Using this representation, we analyze the linguistic structure of Greek slang and the behavior of its contributor community. We find that slang is strongly centered on person-related and evaluative language, exhibits high morphological creativity, and is shaped by highly skewed participation with short user lifespans and overlapping communities. Building on these signals, we introduce a community-based confidence score for definitions that integrates user roles, interaction patterns, and moderation signals. Our results show that taxonomy-based representations improve interpretability while retaining meaningful aspects of behavioral structure, enabling a more structured and interpretable analysis of confidence signals. Overall, this work establishes this http URL as a computational resource for non-standard Greek and provides a foundation for sociolinguistic NLP, bias analysis, and the study of informal language in LLMs.

---


### 198. [Filter Learning for Subgraphs: Algebras and Performance Risk Bounds](https://arxiv.org/abs/2607.21263)

**<font color=#1a73e8>作者：</font>** Purui Zhang, Feng Ji, Yanan Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph signal processing tasks that leverage spectral information typically assume access to the complete graph topology, which is often unavailable in practice. We propose a systematic framework for subgraph filter learning (SFL), where subgraph-supported operators approximate ambient graph filters under partial observations. We formulate SFL as a statistical learning problem in which optimal subgraph operators are inherently data-dependent. To address the difficulty of directly estimating such operators, we develop a subgraph filter algebra based on distance-aware Laplacian constructions, defining a structured and controllable class of filters for effective approximation. We further establish performance risk bounds under the least squares loss, quantifying how well the learned operator approximates the restricted ambient mapping. Experiments real-world datasets show that, for SFL tasks, the proposed algebraic models consistently outperform polynomial filters, distribution-agnostic operators, and direct numerical filter learning baselines that attempt to recover the underlying structure from data.

---


### 199. [BasketEvent: Understanding Who Did What and When in Basketball Videos](https://arxiv.org/abs/2607.21267)

**<font color=#1a73e8>作者：</font>** Yu Zhang, Jiayuan Rao, Haoning Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Comprehensive basketball video understanding requires resolving not only what event occurs, but also who is responsible and when the key evidence appears. However, exist- ing methods typically treat spatial perception and semantic recognition as isolated tasks, failing to ground events to individual players or pinpoint their temporal boundaries within complex collective dynamics. To bridge this gap, we introduce BasketEvent, a player- centric basketball event understanding dataset curated from real NBA broadcasts. In BasketEvent, event labels are grounded to the responsible players, and a manually an- notated subset of 1,000 samples with precise event intervals is provided to evaluate tem- poral evidence localization. Based on this data, we propose PlayNet, a player-centric reasoning framework that maps basketball videos to player-level event predictions with temporal evidence. Concretely, PlayNet tracks key entities, associates player identities, and reasons about events by modeling player-player, player-ball, and global court inter- actions, while aggregating sparse temporal evidence via gated pooling. Extensive experi- ments demonstrate that PlayNet significantly outperforms representative video-level and crop-based baselines, proving the superiority of player-centric modeling for fine-grained sports video understanding. Our data, code, and models will be made publicly available.

---


### 200. [Flash EQ-Linear: Accelerating Equivariant Linear Layers via Group-wise Discrete Fourier Transform](https://arxiv.org/abs/2607.21271)

**<font color=#1a73e8>作者：</font>** Zhongchen Zhao, Jixin Wang, Qi Xie 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Equivariant networks embed geometric symmetries as structural priors through weight sharing, achieving remarkable parameter efficiency across vision tasks. However, this parameter efficiency does not translate into compute efficiency: existing implementations unroll the structured weights into dense matrices and dispatch them to generic dense kernels, so the FLOPs of an equivariant layer are no smaller than those of a non-equivariant counterpart. In this paper, we observe that the equivariant linear (EQ-Linear) layer---the most fundamental and frequently used module in modern equivariant architectures---is essentially a circular convolution along the group dimension composed with a linear transform along the channel dimension. Building on this observation, we propose Flash EQ-Linear, an exact acceleration algorithm that reduces the complexity from $\mathcal{O}(NDC)$ to $\mathcal{O}(NDC/T)$ by combining the Fourier convolution theorem along the group dimension with the conjugate symmetry of the real DFT. We further provide dedicated CUDA kernels for Flash EQ-Linear, covering both forward and backward passes and both FP32 and FP16 precision. At the operator level, Flash EQ-Linear achieves up to ${2\times}$ forward speedup over PyTorch's this http URL; at the network level, Flash EQ-ViT and Flash EQ-Swin achieve up to ${1.7\times}$ end-to-end speedup over both equivariant and non-equivariant baselines. To our knowledge, this is the first time equivariant networks strictly dominate their non-equivariant counterparts along all three axes simultaneously: accuracy, parameter efficiency, and inference this http URL is available at this https URL.

---


> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-271](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
