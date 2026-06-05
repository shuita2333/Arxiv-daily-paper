# 📦 其他研究 | 2026年06月06日

> 本类共 **289** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-289**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-289**

---

### 251. [AIS-Based Vessel Trajectory Prediction Using Memory-Augmented Neural Networks](https://arxiv.org/abs/2606.06311)

**<font color=#1a73e8>作者：</font>** Wonmo Koo, Sanha Chang, Heeyoung Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate vessel trajectory prediction is essential for safe and efficient maritime operations, enabling collision avoidance and supporting route optimization. Although memory-augmented neural networks have recently shown strong performance in pedestrian and road-vehicle trajectory prediction by selectively retrieving relevant information from an external memory, their potential for vessel trajectory prediction remains underexplored. This paper presents an empirical investigation of memory-based trajectory prediction using Automatic Identification System (AIS) data. Experiments on data from the Gulf of Mexico and the New York Bight demonstrate consistent and substantial performance gains over a range of deep learning baselines that do not incorporate an external memory.

---


### 252. [Efficient Mean Curvature Computation on High-Dimensional Data Manifolds](https://arxiv.org/abs/2606.06329)

**<font color=#1a73e8>作者：</font>** Alexandre L. M. Levada  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating local mean curvature at each point of a high-dimensional dataset is a key ingredient of geometry-aware machine learning algorithms, such as the Mean Curvature Boundary Points (MCBP) method. The naive implementation of this computation, based on a local shape operator approximated from k-nearest neighbor patches, involves an explicit construction of a matrix $H$ whose trace form yields an $O(m^4)$ cost per point, rendering the approach intractable for datasets with more than a few dozen features. This paper introduces two complementary contributions that together reduce this cost by several orders of magnitude. The first contribution is an exact algebraic identity. This identity, derived from the orthogonality of the eigenvectors of the covariance matrix and the cyclicity of the trace operator, eliminates $H$ entirely and reduces the per-point cost to $O(m^2)$ after the eigendecomposition. The second contribution addresses the remaining $O(m^3)$ bottleneck of the full eigendecomposition. Since the local covariance matrix has rank at most $k-1 \ll m$, we replace it with a truncated SVD of the $k \times m$ centered data matrix, an $O(k^2 m)$ operation, and derive an analytical approximation for the contribution of the null-space eigenvectors based on the expected value of their outer product under the Haar measure. The resulting estimator has total cost $O(k^2 m + k m p^2)$, where $p = k-1$. Experiments on real-world datasets confirm speedups of 50 to 300 times relative to the original implementation, with negligible loss when the fast estimator is used to replace the original version. By providing a scalable and data-driven estimate of local curvature, the proposed method establishes curvature as a practical geometric feature for a broad range of machine learning tasks, from classical to modern deep learning pipelines.

---


### 253. [Bridging Domain Expertise and Generalization for Performance Estimation](https://arxiv.org/abs/2606.06335)

**<font color=#1a73e8>作者：</font>** Shuxuan Li, Zhilin Zhao, Quyu Kong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Performance estimation under distribution shift aims to predict how a model behaves on an unlabeled test set whose distribution differs from the training data, a scenario that requires reliable indicators that can faithfully reflect model behavior without ground-truth labels. Existing approaches rely solely on the outputs of the given model whose biases are amplified once the distribution shifts, weakening the correlation with the true performance. Motivated by this limitation, we propose Fused Reference Alignment Prediction (FRAP), which leverages the complementary strengths of an external foundation model and the base model to construct a more reliable surrogate of the ground-truth labels. FRAP aligns the prediction distribution of the foundation model with that of the base model by applying temperature-scaled calibration that minimizes their divergence. The aligned predictions are fused through confidence-based weighting into a refined reference distribution that integrates robustness from the foundation model and domain-specific expertise from the base model, and performance estimation is obtained by measuring how closely the base model predictions agree with this reference. Extensive experiments across diverse datasets and architectures show that FRAP provides consistent and substantial improvements over representative performance-estimation methods under distribution shift.

---


### 254. [StoryVideoQA: Scaling Deep Video Understanding with a Large-Scale, Multi-Genre and Auto-Generated Dataset](https://arxiv.org/abs/2606.06338)

**<font color=#1a73e8>作者：</font>** Zhengqian Wu, Zhixian Liu, Aodong Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video question answering (VideoQA) aims to answer questions about given videos. While existing approaches excel on factoid VideoQA, they struggle with deep video understanding (DVU), which requires the comprehension of complex storylines. This challenge arises from the inherent long-range video content, multi-faceted question types, and instance-level story elements, all of which constrain the scale and diversity of manually constructed DVU datasets. These difficulties constrain the scale and diversity of manually-constructed DVU dataset. To address these, we previously introduced StoryMind to automatically construct DVU datasets with balanced fine-grained topics. Though it can generate high-quality question-answer pairs (QAs) for TV series, it suffers significant performance degradation when handling longer and more complex movies. In this paper, we further design StoryMindv2, an enhanced multi-agent collaboration framework to generate high-quality DVU datasets for both TV series and movies. By integrating a novel supervisor-guided generation mechanism and a refined multi-reviewer voting strategy, the framework is utilized to construct StoryVideoQA, the largest DVU dataset to date, featuring over 363K QAs on 393.2 hours diverse story videos including TV series (avg. 1,635 seconds) and movies (avg. 7,878 seconds). Comprehensive evaluations of 20 state-of-the-art VideoQA methods on this large-scale benchmark reveal that they cannot fully maintain long-range character associations or construct a coherent understanding of complex storylines. To bridge this gap, we propose PlotTree, a novel video understanding agent, re-organizing long-range video content into a hierarchical plot structure, enabling efficient storyline reasoning on StoryVideoQA. Project page: this https URL

---


### 255. [Equivariant Neural Belief Propagation](https://arxiv.org/abs/2606.06344)

**<font color=#1a73e8>作者：</font>** Zehua Cheng, Wei Dai, Jiahao Sun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Probabilistic inference over spatially embedded variables requires beliefs that respect $SE(3)$ symmetry, yet existing equivariant networks produce only scalars and vectors -- not the rank-2 precision tensors needed for anisotropic uncertainty, and single-component messages collapse multi-modal energy landscapes to physically meaningless averages. We introduce Equivariant Neural Belief Propagation (ENBP), a factor-graph framework whose messages are equivariant Gaussian mixture models with sufficient statistics that transform exactly under $SE(3)$. Rank-2 precision matrices are synthesised via equivariant outer products, ingested through differentiable spectral decomposition, and kept tractable by a greedy KL-based mixture reduction that provably commutes with $SE(3)$. On GEOM-QM9 and GEOM-Drugs, ENBP achieves 98.9% conformational coverage at 0.090 $\mathring{A}$ error with sub-second latency -- over $100\times$ faster than diffusion baselines at higher accuracy. On multi-body robotic inference, vanilla loopy BP diverges at 15+ agents while ENBP converges with near-zero collision rates and machine-precision equivariance error (${\sim}10^{-7}$ vs.\ $10^{-1}$ for augmented baselines).

---


### 256. [Boosting Brain-to-Image Decoding with TRIBE v2 Data Augmentation](https://arxiv.org/abs/2606.06345)

**<font color=#1a73e8>作者：</font>** Yohann Benchetrit, Marlène Careil, Simon Dahan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Brain decoding is limited by the availability of labeled neural data, and remains challenging in low-data regimes. To address this issue, we investigate whether and when brain decoding can be boosted by augmenting small fMRI datasets with synthetic data generated by a pretrained model of fMRI responses to stimuli. We use TRIBE v2, a large encoding model pretrained on more than 1000 hours of fMRI responses to video, audio and language. For each dataset, we evaluate systematic grids that show how the performance of image decoders varies with the amount of synthetic data used for training. Our results, based on two datasets (the 7T fMRI Natural Scenes Dataset and 3T fMRI BOLD5000), show up to 68% improvement in Top-10 image-retrieval accuracy compared to decoders trained only on real data. Importantly, the proportion of augmented data required to reach a given image decoding performance needs to be adjusted depending on the data source. Surprisingly, image decoders trained exclusively on synthetic fMRI can perform above chance in some settings, suggesting that TRIBE v2 can support zero-shot brain-to-image decoding. Together, these results show how large-scale models of the fMRI responses to sight, sound and language may provide a foundation to improve the data efficiency for image decoding.

---


### 257. [Performance Evaluation of GraphCast for Medium-Range Weather Forecasting over Brazil](https://arxiv.org/abs/2606.06348)

**<font color=#1a73e8>作者：</font>** Wolfgang R. Rowell Jr., Lucas S. Kupssinskü  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The paradigm of global weather forecasting is rapidly shifting with the emergence of Machine Learning Weather Prediction models (MLWP). While these data-driven architectures demonstrate remarkable global skill, regional benchmarks in the Global South remain scarce, leaving their efficacy in complex, highly convective environments largely unverified. This study evaluates the performance of GraphCast operational against the deterministic ECMWF IFS HRES as baseline across four distinct Brazilian climatic sub-regions. Utilizing a scalable, cloud-native pipeline and the WeatherBench-X framework for benchmarking weather models, we assess selected tropospheric variables ($T_{850}$, $Q_{850}$, $Z_{500}$) over four selected seasonal windows, employing the operational IFS analysis as the ground truth to calculate the statistical metrics for both models. Results reveal a regime-dependent skill profile. During the austral winter, GraphCast underperforms in the medium range (lead days 2-7) for $Z_{500}$ when resolving fast-propagating baroclinic systems over southern Brazil, but regains an advantage in the extended range, where its inherent smoothing of chaotic small-scale variability becomes beneficial under deterministic skill metrics. Conversely, during the austral summer wet season, GraphCast accurately captures large-scale moisture transport while intrinsically dampening the high-frequency convective variability that degrades deterministic NWP temperature forecasts. These findings establish a baseline for Brazil and define the specific physical boundaries that will guide future ``tropicalization'' efforts, aiming to optimize these foundational AI models for regional resilience.

---


### 258. ["Chi nas dal soch el sent de legn" -- Auditing Text Corpora for Lombard](https://arxiv.org/abs/2606.06349)

**<font color=#1a73e8>作者：</font>** Edoardo Signoroni, Pavel Rychlý  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Several of the world's languages are still under-resourced in terms of Natural Language Processing (NLP) tools. This is mostly due to the lack of high-quality datasets to train, develop, and evaluate systems and models for several tasks, such as Machine Translation (MT). We conduct a manual audit of the parallel and monolingual corpora available for Lombard, an under-resourced language continuum from Italy. Our analysis reveals that the perceived abundance of web-scraped data is an illusion, with massive datasets plagued by severe language misidentification, boilerplate text, and non-linguistic noise. Furthermore, we analyze the orthographic composition of the valid Lombard portions across web-scraped datasets, curated corpora, and benchmarks. Our findings show conflicting orthographical systems and severe representational bias across all corpora: high-quality data is heavily skewed towards Western Lombard varieties, with Eastern ones left on the margins. This underscores the need for variety-aware, community-driven data curation rather than purely quantity-driven scraping.

---


### 259. [Maximising the Set-Piece Return: Optimising Football Corner Tactics with Graph Reinforcement Learning](https://arxiv.org/abs/2606.06353)

**<font color=#1a73e8>作者：</font>** Sean Groom, Michael Groom, Francisco Belo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning is increasingly employed for the evaluation of football tactics. However, existing approaches focus on characterising historical actions or analyst-specified counterfactual scenarios. In this work, we seek to go beyond the imitation of historically observed patterns towards discovering new generalisable player configurations and strategies. To tackle this, we focus on optimising corner kick routines, and formulate a decision-making problem in which a central policy makes adjustments to attacking player positions and velocities to maximise first contact shot probability. Unlike classic optimisation that solves for isolated setups, we contribute a reinforcement learning architecture operating on graph-structured data that yields a general policy for adjusting arbitrary starting player positions. Evaluated on over 3,000 Premier League corners, our approach strongly outperforms baseline optimisation techniques under matched inference budgets. Our results suggest that graph reinforcement learning can shift set-piece analysis from historical evaluation and imitation towards reward-driven tactical discovery.

---


### 260. [Credential Disclosure in (EU) Digital Identity Wallets: Privacy Risks and Practical Mitigations](https://arxiv.org/abs/2606.06354)

**<font color=#1a73e8>作者：</font>** Sheila Zingg, Daniele Lain, Yoshimichi Nakatsuka 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The European Union will introduce the EUDI Wallet by late 2026, which allows users to hold digital credentials (i.e., representations of physical official identity documents) on their devices. This will allow users to securely and privately disclose identity attributes to websites. Although such a system has many benefits, it also introduces risks caused by poor credential disclosure decisions. In this paper, we (i) conduct a large-scale survey on credential disclosure with users and experts and (ii) evaluate the effectiveness and feasibility of our Credential Assistant that displays expert recommendations and user opinions. Our results show that users are likely to overshare (e.g., ~20% of users disclosed their official ID to news websites). This indicates that users struggle to protect their privacy, which will impact the usability of the EUDI Wallet and lead to privacy violations, identity theft, and other abuses of leaked credentials. Finally, we show that our Credential Assistant significantly reduces users' credential disclosure mistakes from ~15% to ~7%. However, it does not fully eliminate poor credential disclosure decisions, indicating that stronger interventions may be necessary, especially for sensitive attributes.

---


### 261. [Comparison of Deep Learning Frameworks For Rice Disease Mapping From UAV Multispectral Imaging](https://arxiv.org/abs/2606.06359)

**<font color=#1a73e8>作者：</font>** Yadav Raj Ghimire, Jagrati Talreja, Tewodros Syum Gebre 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this study, UAV multispectral imagery is used to segment the severity of bacterial leaf blight (BLB) in rice using convolutional neural networks (CNNs) and transformer-based models. The evaluated architectures include U-Net with a ResNet- 101 encoder, U-Net++ with EfficientNet-B3 and EfficientNetB7, DeepLabV3+, and SegFormer, all trained under a common pipeline with three input configurations (multispectral only, multispectral+NDVI, and multispectral+NDRE). Experiments are conducted using the publicly available BLB dataset with performance reported using mean IoU (mIoU), mean F1 (mF1), mean accuracy (mAcc), precision, and recall. U-Net++ with EfficientNet-B3 achieved the highest performance, with an mIoU of 97.62%. SegFormer obtained lower segmentation accuracy but comparable inference speed. Overall, the results indicate that lightweight CNN backbones remain more reliable for operational BLB monitoring while integration of vegetation indices provides small and consistent improvements. The study also highlights the value of standardised UAV datasets to compare disease mapping methods and encourages the use of CNN architectures for field implementation.

---


### 262. [Physics in 2-Steps: Locking Motion Priors Before Visual Refinement Erases Them](https://arxiv.org/abs/2606.06361)

**<font color=#1a73e8>作者：</font>** Woojung Han, Seil Kang, Youngjun Jun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image-to-Video diffusion models leverage input images to generate visually stunning content, yet frequently produce motion that violates physical laws. We reveal a surprising finding: a 2-step generation often exhibits better physical consistency than a 50-step output from the same model. Through spectral analysis, we trace this to phase erosion during denoising; the phase degrades significantly (dropping by $\approx 18\%$ from step 2 to step 50), whereas the magnitude remains relatively stable. Building on this insight, we propose PhaseLock, a training-free framework that preserves the valid motion priors from few-step inference throughout the denoising trajectory. Rather than relying on full-step inference for physical consistency, PhaseLock extracts a motion prior from just 2 steps and enforces it onto high-fidelity generation via Latent Delta Guidance. Our approach effectively mitigates phase degradation, improving physical consistency by an average of 6.2 points across diverse models while largely maintaining visual fidelity, with negligible overhead ($1.06\times$ time, $1.02\times$ memory) and reduced reliance on expensive external guidance methods ($\sim5\times$ time).

---


### 263. [GMBFormer: An NDVI-Guided Global Memory Bank Transformer for Urban Green-Space Extraction from Ultra-High-Resolution Imagery](https://arxiv.org/abs/2606.06363)

**<font color=#1a73e8>作者：</font>** Hao Lei, Xi Cheng, Chenlu Shu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Urban green-space extraction from ultra-high-resolution (UHR) imagery is commonly performed patch by patch, which limits semantic reuse among spatially separated but visually similar vegetation patterns. Directly injecting the Normalized Difference Vegetation Index (NDVI) into red-green-blue (RGB) backbones can also blur the roles of visual appearance learning and physical vegetation confidence. We propose GMBFormer, a SegFormer-based framework that replaces adjacency-driven feature propagation with selective, similarity-driven prototype retrieval. Only RGB channels enter the backbone and decoder, while NDVI is decoupled as a physics-informed gate that admits high-confidence vegetation descriptors into a compact global memory bank through momentum updates. During training and inference, the current patch queries stored prototypes through memory-mediated cross-attention, and the retrieved response is integrated with bounded overhead. Experiments use a self-constructed Chengdu UHR dataset with 7,700 labeled 512 x 512 patches and two reduced-label settings derived from the public International Society for Photogrammetry and Remote Sensing (ISPRS) Potsdam dataset. Under the same training and evaluation protocol, GMBFormer obtains mean intersection over union (mIoU)/mean Dice (mDice) scores of 89.25%/94.31%, 92.17%/95.92%, and 83.72%/90.86%, respectively, improving the controlled SegFormer-B4 baseline in each setting. Ablation studies indicate that decoupled NDVI admission, memory retrieval, capacity, and momentum jointly shape the final performance.

---


### 264. [End-to-End Subgraph Detection with GraphDETR](https://arxiv.org/abs/2606.06364)

**<font color=#1a73e8>作者：</font>** Dexiong Chen, Till Hendrik Schulz, Karsten Borgwardt  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Subgraph detection seeks to identify whether and where instances of query patterns occur within a larger graph. This problem is fundamental across scientific domains and is closely related to subgraph isomorphism, which is NP-complete, limiting combinatorial approaches to small patterns or moderately sized graphs. We introduce GraphDETR, a deep learning framework that formulates subgraph detection as a set prediction problem, analogous to DETR in object detection. GraphDETR encodes the target graph with a graph neural network, and employs a fixed set of learnable query vectors, decoded via a transformer decoder, to predict all pattern occurrences jointly in a single forward pass. This is enabled by training the model end-to-end with bipartite matching. Unlike traditional combinatorial methods that only solve exact structural matching, GraphDETR naturally extends to approximate matching, enabling detection beyond exact pattern correspondence. Empirically, we show that GraphDETR can detect diverse patterns, such as molecular structures, cycles, cliques, and fuzzy patterns of up to 50 nodes, in target graphs with up to 1000 nodes. We further evaluate on molecular functional group detection over the ChEMBL dataset, where GraphDETR predicts the complete set of functional groups per molecule, achieving a strong performance of $\text{AP}_{100} = 91.2$.

---


### 265. [Visual Commonsense Driven Knowledge Refinements for Scene Graph Generation](https://arxiv.org/abs/2606.06369)

**<font color=#1a73e8>作者：</font>** Maëlic Neau, Salim Baloch, Jakob Suchan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning-driven Scene Graph Generation (SGG) models excel on frequent relation types but degrade sharply under annotation sparsity, failing to capture reliable visual commonsense knowledge. We propose a model-agnostic, semantically-guided knowledge refinement framework that systematically mines commonsense-grounded constraints from training data - capturing spatial, functional, and qualitative relational regularities - and uses general declarative commonsense reasoning to correct and refine ranked SGG predictions at inference time. The framework requires no manual rule authoring, no model retraining, and transfers across datasets and architectures. On three standard benchmarks, we obtain consistent improvements over strong baselines, demonstrating that structured visual commonsense reasoning over deep scene semantics is a practical and effective complement to purely learning-based scene graph generation.

---


### 266. [Rethinking Infrastructure Inspection as Image Difference Classification: A Traffic Sign Case Study](https://arxiv.org/abs/2606.06375)

**<font color=#1a73e8>作者：</font>** Ching Yau Fergus Mok, Lavindra de Silva, Varun Kumar Reja 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Digital twins (DTs) allow the digitalization of road infrastructure inspection, though this is hindered by limited annotated data. This work exploits the relational nature of continuous asset condition monitoring to reformulate image-based defect detection as image difference classification (IDC) to reduce data reliance. This was evaluated in a case study on low-resource traffic sign inspection with different IDC classifiers using a newly-curated, high quality dataset. Results indicate that the instruction-based classifier outperforms encoder-based ones and gains from comparison with reference images. This shows that IDC can be an effective task modeling for tackling data constraints in infrastructure inspection and DT asset condition updating.

---


### 267. [Emergent Language as an Approach to Conscious AI](https://arxiv.org/abs/2606.06380)

**<font color=#1a73e8>作者：</font>** Zengqing Wu, Chuan Xiao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The question of whether artificial systems can be conscious remains open, in part because existing approaches either evaluate systems against theory-derived checklists (discriminative) or engineer consciousness-inspired modules directly (architectural); both leave open whether observed structures are artifacts of human language priors. We propose a generative methodology: emergent language (EL) in multi-agent reinforcement learning, where agents start from minimal (no language, no concept of self, minimal exposure to human text) and develop communication under task pressure alone, ensuring causal attributability to task demands rather than inherited human language priors. We position our methodology by discussing how EL serves as a generative tool for studying consciousness-relevant structure, including the role of environment complexity and the interpretation of emergent communication. As a proof of concept, we instantiate this methodology in a minimal environment and show that agents develop self-referential communication, including an echo-mismatch detection circuit that is not predicted by task structure or architecture alone but emerges from a specific environmental affordance.

---


### 268. [Learned Response-Field Inertia Operator for HEC-RAS 2D Water-Surface Elevation Prediction](https://arxiv.org/abs/2606.06385)

**<font color=#1a73e8>作者：</font>** Edward Holmberg, Elias Ioup, Md Meftahul Ferdaus 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This article presents a cross-dataset evaluation of learned native-cell surrogate models for solver-consistent water-surface elevation (WSE) prediction in HEC-RAS 2D. To avoid raster remapping error and information-access confounding, surrogates are evaluated directly on the original nonuniform computational cells under an explicit policy that separates static project inputs, current hydraulic state, project-input forcing, calibration-derived quantities, and future solver-output targets. We introduce the Learned Response-Field Inertia Operator (LRFIO), a no-forcing, increment-based learned surrogate that calibrates an inertial response operator from solved HEC-RAS trajectories and deploys the retained operator through closed-form native-cell rollout. LRFIO evaluates a base-case-first response hierarchy consisting of persistence, global calibrated inertia, and segmented response-field inertia. Segmentation, residual correction, and neuralized inertia are treated as learnable modeling choices, with added complexity retained only when validation evidence justifies its cost. Evaluated across four diverse HEC-RAS 2D benchmarks, LRFIO retains different response structures for different domains, demonstrating adaptive learned complexity. The selector audit shows controlled complexity with a maximum validation regret of 4.30%. During deployment, retained rollout times range from 0.003 s to 0.242 s, and the Beaver Bayou measured-solve comparison gives an estimated 2.75 x 10^4 horizon-normalized speedup over HEC-RAS. These results indicate that the current native-cell increment is a strong solver-conditioned predictive scaffold and that added response-field, neural, or spatial complexity should be retained only when empirically justified.

---


### 269. [Humans' ALMANAC: A Human Collaboration Dataset of Action-Level Mental Model Annotations for Agent Collaboration](https://arxiv.org/abs/2606.06388)

**<font color=#1a73e8>作者：</font>** Jiaju Chen, Yuxuan Lu, Jiayi Su 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in LLM agents have enabled complex cognitive capabilities, such as multi-step reasoning, planning, and tool use, that increasingly position these agents as human collaborators. Effective collaboration, however, requires collaborators to continuously maintain and align mental models of their own reasoning,partners' intentions, and shared goals during the collaborative process. Today's agents rarely develop such capabilities since they are primarily optimized for task completion, and the community lacks authentic human collaboration data with action-level mental model annotations that could guide agents toward process-level collaborative competence. To bridge this gap, we present ALMANAC, a dataset of Action-Level Mental model ANnotations for Agent Collaboration built from the Map Task, a classic dyadic routing task from social science. ALMANAC contains 2,987 collaboration actions, each paired with theory-informed mental model annotations that record the participants' self-reasoning, perceived partner intent, and perceived team goal. We benchmark six LLMs on predicting humans' next-turn behavior and mental models. Our results demonstrate ALMANAC's utility in evaluating models' ability to simulate human collaborative behaviors and infer their underlying mental models.

---


### 270. [HomeWorld: A Unified Floorplan-to-Furnished Framework for Generating Controllable, Densely Interactive Whole-Home Scenes](https://arxiv.org/abs/2606.06390)

**<font color=#1a73e8>作者：</font>** Wenbo Li, Xiaoliang Ju, Zipeng Qin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Indoor scene generation is crucial for robot simulation and modern interior design. However, complex layouts together with scarce 3D scene data make learning-based generation challenging. Existing methods often rely on hand-crafted rules or focus on isolated sub-tasks (e.g., floorplan synthesis or single-room furnishing), producing whole-home scenes that lack global coherence, realism, and simulation readiness. To mitigate these limitations, we propose a unified hierarchical framework that decomposes indoor scene synthesis into controllable stages. First, we curate a large-scale dataset of 300K real residential floorplans to train a large language model for whole-home floorplan generation. With detailed descriptions and a K-D tree-based representation, our method enables fine-grained, controllable whole-home floorplan generation. Building upon the generated whole-home floorplan, we leverage image generation models to draft furniture layouts from multi-level roaming viewpoints, and then generate the layouts of small manipulable objects on different supporting surfaces (e.g., cabinets, desks, and dining tables) for embodied AI simulation. During furniture and object layout generation, a VLM-based refiner iteratively corrects furniture and object placement, and a 3D generative model enables flexible replacement of individual assets. We further attach basic physical attributes and simple surface texture and lighting setups to complete the pipeline for embodied AI use. Experiments and user studies demonstrate that our pipeline produces indoor spaces with greater layout diversity and stronger 3D design appeal, outperforming prior methods on both quantitative and qualitative metrics. Finally, alongside our generation pipeline, we will release the floorplan dataset and 5K fully furnished scenes to the community. Project Page: this https URL

---


### 271. [Proper Scoring Rules for Right-Censored Survival Data](https://arxiv.org/abs/2606.06393)

**<font color=#1a73e8>作者：</font>** Jef Jonkers, Glenn Van Wallendael, Luc Duchateau 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Proper scoring rules provide a rigorous theoretical basis for the training and evaluation of probabilistic forecasts. However, in the presence of right censoring, the event time is only partially observed, rendering conventional scoring rules inapplicable in their standard form. We propose a framework for proper scoring of right-censored survival outcomes based on a simple idea: first, map the predictive distribution through the censoring mechanism, then apply the underlying proper score on the induced observed-data law. This yields localized scores for fixed censoring times and marginalized scores when the censoring time is random or only partially observed. The resulting construction recovers familiar right-censored likelihood and IPCW-type criteria within a coherent framework, while also yielding right-censored versions of the CRPS, pinball loss, Brier score, and energy score. We show that the marginalized score is proper under conditional independent censoring and strictly proper on the identifiable region. The same principle also leads to censored engression, a sample-based learning objective for multivariate right-censored survival modeling. In experiments, our scores correctly rank the oracle forecast across several censoring regimes, whereas forecast-dependent plug-in weighted scores can exhibit ranking reversals. Censored engression likewise substantially improves over naive training on censored outcomes.

---


### 272. [Risk Assessment of Autonomous Driving: Integrating Technical Failures, Ethical Dilemmas, and Policy Frameworks](https://arxiv.org/abs/2606.06396)

**<font color=#1a73e8>作者：</font>** Boyi Chen, Shengqin Chu, Zicheng Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous driving technology has the potential to reduce the large number of road traffic accidents caused by human error each year, but it also brings new types of risks that need to be evaluated from the aspects of technology, ethics and regulations. Based on public crash data from the National Highway Traffic Safety Administration (NHTSA), disengagement reports from the California Department of Motor Vehicles (DMV), the MIT Moral Machines dataset, and a comparative regulatory analysis of five jurisdictions, we have found that the main types of technical failure modes are perception and classification errors. These account for a relatively large proportion of the reported accidents, and it can be concluded that there are different ethical frameworks for autonomous vehicle decision-making, and inconsistent regulations in different areas increase the uncertainty of widespread application. Generally speaking, the problems of technology, ethics and regulation are closely related and need to be solved together. Therefore, this paper recommends a more adaptive and cooperative governance approach that combines engineering standards, ethical discussion, and institutional supervision.

---


### 273. [The Post-GCN Decade Revisited: Curvature-Stratified Evaluation of Relational Learning](https://arxiv.org/abs/2606.06397)

**<font color=#1a73e8>作者：</font>** Shuo Wang, Xiangyu Wang, Quanxin Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Current evaluation practices in relational learning rely heavily on flat leaderboards that average performance across heterogeneous datasets, implicitly assuming a uniform underlying structure. We show that this assumption introduces systematic bias: it obscures geometry-dependent performance variations and can lead to misleading conclusions about model generalization. In this work, we identify intrinsic geometry as a key latent factor governing model effectiveness. We demonstrate that conventional aggregated metrics mask critical performance trade-offs that only become visible when datasets are stratified by their geometric properties. To address this issue, we introduce a curvature-stratified evaluation framework that partitions datasets into positive, negative, and near-zero curvature regimes. Our benchmark evaluates 18 representative models including Graph Convolutional Networks (GCNs), Graph Foundation Models (GFMs), and tabular learning methods across 14 datasets. We find that model rankings are highly stable within each curvature regime but shift significantly across regimes, indicating that performance is fundamentally geometry-dependent rather than universally transferable. Notably, we identify regimes where GFMs offer diminishing returns compared to geometry-aligned GNNs. Based on these findings, we propose a geometry-aware evaluation protocol that yields more reliable and interpretable comparisons than standard aggregated benchmarks. We release all code, curvature-stratified dataset splits, and evaluation tools to support reproducible and rigorous assessment of future relational learning methods. Code and datasets are provided in our project homepage: this https URL.

---


### 274. [A Vision-language Framework for Comparative Reasoning in Radiology](https://arxiv.org/abs/2606.06407)

**<font color=#1a73e8>作者：</font>** Tengfei Zhang, Ziheng Zhao, Lisong Dai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical imaging artificial intelligence has achieved strong performance in isolated image interpretation, but remains poorly aligned with radiological practice, where diagnosis and follow-up rely on comparison across prior studies and analogous reference cases. Here we formulate radiological comparison as an entity-aware cross-image reasoning problem and introduce a framework that supports both reference-case retrieval and temporal comparative interpretation. We construct MedReCo-DB, a large-scale comparative imaging resource derived from routine image-report pairs, comprising more than 690,000 images from over 160,000 patients across eight institutions, four countries and seven imaging modalities. Reports are decomposed into anatomical structures, abnormal findings and pathological conditions to provide supervision for entity-conditioned retrieval and comparative visual question answering. Using this resource, we develop MedReCo, an entity-aware visual encoder for controllable retrieval of clinically analogous cases, and MedReCo-VLM, a vision--language extension for generative interpretation of interval change. Across internal, external and cross-center evaluations, MedReCo achieved the highest Recall@1 in all 12 internal retrieval settings and improved external retrieval by a mean of 6.0 percentage points. In clinically confusable differential groups, it consistently outperformed the strongest baselines. MedReCo-VLM achieved the best performance across all comparative generation evaluations and improved longitudinal follow-up accuracy by 14.5-46.5 percentage points on chest radiographs and 13.0-27.9 percentage points on CT. These findings suggest that entity-aware comparative reasoning can be learned from routine clinical data at scale and may provide a more clinically aligned foundation for medical imaging AI.

---


### 275. [Double Preconditioning (DoPr): Optimization for Test-Time Performance, not Validation Loss](https://arxiv.org/abs/2606.06418)

**<font color=#1a73e8>作者：</font>** Thomas T. Zhang, Alok Shah, Yifei Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many modern applications of deep learning involve training a neural network via a one-step prediction loss (e.g., $L^2$ regression, cross-entropy), but deploy the network by rolling out along its own predictions. Key examples include autoregressive language modeling, flow-based generative modeling, and robot policy learning. It is well-documented that these settings induce a phenomenon we call test-time feedback (TTF): the mismatch between the training/validation loss and downstream metrics of interest, such as task success rate and generation quality, which grows with task length. While data curation, architecture, and objective design have been proposed to combat train-test shift in TTF settings, this paper proposes optimization as a new design axis to mitigate error accumulation. Specifically, we introduce a new optimization paradigm called double-preconditioning (DoPr) uniquely tailored to the challenges of TTF. DoPr combines gradient-wise preconditioning, as in Adam and Muon, with activation-wise preconditioning (AP), such as in KFAC. We show that the addition of AP yields a drop-in intervention for increasing downstream model performance across a range of TTF settings. Interestingly, these gains in test-time performance do not consistently accompany improvements in validation loss, opening new questions about how to properly evaluate models trained with one-step supervised objectives.

---


### 276. [Computational Modeling of Human Adaptation in Urban Infrastructure Management under Extreme Conditions: A Case Study of Subway Flood Scenarios](https://arxiv.org/abs/2606.06429)

**<font color=#1a73e8>作者：</font>** Jinfeng Lou, Zijie Liang, Pengkun Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Decision-making in urban infrastructure management during extreme events relies heavily on human operators, yet current computational support systems often fail to account for non-monotonic human adaptation and latent psychological biases like overconfidence and defensive overcorrection. This study addresses this gap by integrating Instance-Based Learning Theory (IBLT) into the domain of civil engineering computing. We establish a computational cognitive architecture that simulates operator decision processes through the mathematical mechanisms of memory retrieval and utility blending. This model functions as a computational baseline, representing boundedly rational adaptation driven by experiential priors, thus allowing for the algorithmic isolation of latent psychological biases from the baseline dynamics of memory-based learning. We demonstrated this framework using a human-in-the-loop microworld experiment simulating subway flood-induced track suspensions, where dispatchers must balance passenger safety against service efficiency. Analysis revealed a complex, non-linear human adaptation cycle consisting of four phases: acquisition, overconfidence, overcorrection, and recalibration. Specifically, the computational model exposed a significant divergence during the post-accident "overcorrection" phase: while human operators exhibited immediate, defensive risk overestimation, the model maintained a stable trajectory based on accumulated experience. This strategic divergence confirms that operational instability following failure is often attributable to acute psychological bias overriding stable memory-based adaptation, a pattern theoretically expected to recur across analogous high-stakes environments and validatable through multi-modal behavioral and sensor data from professional operators.

---


### 277. [Causal Atlases from Entropic Inference: Bayesian Networks beyond Optimal DAGs](https://arxiv.org/abs/2606.06440)

**<font color=#1a73e8>作者：</font>** Hazhir Aliahmadi, Irina Babayan, Greg van Anders  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data-driven causal relationship identification is pertinent to advancing understanding of complex systems both within and beyond science. Bayesian networks offer a probabilistic method for modelling generic causal relationships via directed acyclic graphs (DAGs). However, typical techniques for constructing Bayesian networks rely on optimization, which can be ill-suited for learning causal relationships because the underlying data may admit multiple chains of causation. More data-faithful representations of causal relationships would provide frameworks for constructing multiple causal maps that are consistent with the variability that is inherent in underlying data. Here, we show that entropy-based inference generates atlases of plausible causal relationships that are consistent with underlying data. On simulated noisy data of 2- and 20-node linear structural equation models, we sample a maximum-entropy ensemble of graphs that allow us to quantify the inherent structural ambiguity in underlying causal relationships. Our method shows that "optimized" DAGs can contain causal artifacts are not consistent across equivalently accurate topologies.

---


### 278. [Latent Reasoning with Normalizing Flows](https://arxiv.org/abs/2606.06447)

**<font color=#1a73e8>作者：</font>** Guancheng Tu, Xiangjun Fu, Suhao Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models often improve reasoning by generating explicit chain-of-thought (CoT), demonstrating the importance of intermediate computation. However, textual CoT forces this computation through a discrete, serial, and communication-oriented token stream: each reasoning step must be verbalized before the model can proceed, even when the underlying update is semantic, uncertain, or only partially formed. Latent reasoning offers a higher-bandwidth alternative by performing intermediate computation in compact continuous states before committing to text. Yet existing latent-reasoning methods often sacrifice key advantages that make CoT effective in autoregressive language models, including native left-to-right generation, probabilistic sampling, compatibility with KV-cache decoding, and tractable likelihood estimation. We propose NF-CoT, a latent reasoning framework that preserves these advantages by modeling continuous thoughts with normalizing flows. NF-CoT instantiates a TARFlow-style normalizing flow inside the LLM backbone, defining a tractable probability model over compact continuous thoughts distilled from explicit CoT. Continuous-thought positions are generated by an NF head, while text positions are generated by the standard LM head within the same causal stream. This design provides exact likelihoods for latent thoughts, enables probabilistic left-to-right decoding with the original KV cache, and supports direct policy-gradient optimization in the latent reasoning space. On code-generation benchmarks, NF-CoT improves pass rates over explicit-CoT and prior latent-reasoning baselines while substantially reducing intermediate-reasoning cost.

---


### 279. [Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads](https://arxiv.org/abs/2606.06448)

**<font color=#1a73e8>作者：</font>** Yasmine Omri, Ziyu Gan, Zachary Broveak 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents are increasingly deployed on long-horizon tasks requiring sustained reasoning over extended interaction histories. Realizing this at scale requires agents to persistently store, retrieve, and update their own memory across sessions. A rich ecosystem of agent memory systems has emerged spanning flat retrieval, LLM-mediated extraction, consolidating fact stores, and agentic control flows. Yet, their system-level behavior remains uncharacterized. We present the first systems characterization of agent memory. First, we introduce a system-oriented taxonomy classifying agent memory systems along four axes. Second, we build a phase-aware profiling harness attributing cost to construction, retrieval, and generation. Third, we characterize ten representative systems across two benchmark suites, uncovering how design choices shift cost across the write and read paths. Finally, we derive 10 system recommendations covering construction scheduling, capability floors, amortization via query volume, freshness-latency tradeoffs, and fleet-scale management.

---


### 280. [Vortex: Efficient and Programmable Sparse Attention Serving for AI Agents](https://arxiv.org/abs/2606.06453)

**<font color=#1a73e8>作者：</font>** Zhuoming Chen, Xinrui Zhong, Qilong Feng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sparse attention is becoming increasingly important for serving large language models (LLMs) as generation lengths continue to grow. However, deploying and evaluating new sparse attention algorithms at scale remains highly engineering-intensive, slowing both human researchers and AI agents in exploring the sparse attention design. To address this challenge, we present Vortex, a system that combines a Python-embedded frontend language atop a page-centric tensor abstraction for expressing a broad range of sparse attention algorithms, with an efficient backend tightly integrated into modern LLM serving stacks. Vortex enables rapid prototyping, deployment, and evaluation of sparse attention algorithms, effectively translating their theoretical efficiency gains into real-world throughput improvements. As a result, Vortex substantially accelerates the design and iteration of sparse attention algorithms. First, AI agents use Vortex to automatically generate and refine diverse algorithms, the best reaching up to $3.46\times$ higher throughput than full attention while preserving accuracy. Second, Vortex extends sparse attention to emerging architectures and very large models that are otherwise hard to experiment with, reaching up to $4.7\times$ higher throughput on the MLA-based GLM-4.7-Flash and $1.37\times$ on the 229B-parameter MiniMax-M2.7 on NVIDIA B200 GPUs.

---


### 281. [In-Context Multiple Instance Learning](https://arxiv.org/abs/2606.06458)

**<font color=#1a73e8>作者：</font>** Alexander Möllers, Marvin Sextro, Julius Hense 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multiple Instance Learning (MIL) addresses problems where supervision is available at the level of bags of instances and has been successfully applied in fields ranging from computational pathology to satellite imagery. Nevertheless, existing algorithms struggle in the low-label regime that characterizes many real-world applications. Flexible models overfit and rigid ones fail to adapt to the task at hand. We show that pretraining an in-context learner with a Perceiver-style architecture on synthetic data yields a model that can solve new tasks from a handful of labeled bags. At inference time, classification happens in a single forward pass and requires no gradient updates. We propose and investigate different synthetic data generators for bag-structured data and find that they capture complementary inductive biases. A model pretrained on a mixture of these generators inherits their per-task strengths and achieves the best average performance across twelve MIL benchmarks, outperforming supervised baselines that require task-specific training.

---


### 282. [Event Detection for Parameter-to-KPI Dependency Learning for AI-RAN](https://arxiv.org/abs/2606.06459)

**<font color=#1a73e8>作者：</font>** Christie Djidjev, Nicholas Kaminski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Next-generation wireless networks are expected to rely on multiple concurrent AI-driven control functions that optimize different network objectives simultaneously, particularly in AI-integrated and open radio access network architectures such as AI Radio Access Network (AI-RAN) and Open Radio Access Network (O-RAN). When these functions interact, they can interfere with one another in ways that are difficult to detect from raw network data alone. A key missing piece for managing such interactions is a reliable, interpretable dependency structure that captures which control parameters are actively influencing which network performance outcomes at any given time. This paper focuses on the event-detection step needed to support such dependency learning by converting noisy continuous telemetry into binary indicators of parameter activity and KPI response. The central difficulty is that not every fluctuation in the data reflects a genuine control interaction, so the method must distinguish real parameter-outcome relationships from background variation. Because real AI-RAN traffic traces with known parameter-KPI ground truth are difficult to obtain, we introduce a synthetic closed-loop traffic generator with planted latent dependencies. We use this controlled telemetry to evaluate a machine-learning-based dependency recovery pipeline that formulates the conversion of continuous traces into binary event indicators as a significance-detection problem. Experimental evaluation shows that the proposed pipeline reliably recovers the latent dependency structure from noisy continuous traces when the signal is sufficiently separated from background variation, while highlighting threshold calibration as the key factor controlling event-detection quality. These results constitute a foundational step toward interpretable dependency learning for adaptive AI-RAN control systems.

---


### 283. [You Only Index Once: Cross-Layer Sparse Attention with Shared Routing](https://arxiv.org/abs/2606.06467)

**<font color=#1a73e8>作者：</font>** Yutao Sun, Yanqi Zhang, Li Dong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context inference in modern LLMs is increasingly constrained by decoding efficiency, especially in reasoning-heavy settings where models generate long intermediate chains of thought. Existing sparse attention methods often face a practical efficiency-quality trade-off. Structured block sparse methods typically provide stronger acceleration but incur noticeable quality loss, while token sparse methods are usually more accurate yet deliver limited end-to-end speedup because top-k routing over the full cache remains expensive. In this work, we propose cross-layer sparse attention (CLSA), which is built on top of KV-sharing architectures such as YOCO. The core idea is to share not only the KV cache across cross-decoder layers, but also the routing index. A single indexer computes token-level top-k selection once and reuses the resulting index across layers, thereby preserving the fine-grained selectivity of token sparse attention while amortizing the routing overhead. The resulting architecture improves all major inference bottlenecks jointly, including pre-filling, KV-cache storage, and long-context decoding. Experiments across short-context and long-context benchmarks show that CLSA is both accurate and efficient, achieving up to 7.6x decoding speedup and 17.1x overall throughput improvement at 128K context. These results suggest a more complete architectural solution for long-context LLMs that jointly advances model quality and inference efficiency.

---


### 284. [Goedel-Architect: Streamlining Formal Theorem Proving with Blueprint Generation and Refinement](https://arxiv.org/abs/2606.06468)

**<font color=#1a73e8>作者：</font>** Jui-Hui Chung, Ziyang Cai, Zihao Li 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce Goedel-Architect, an agentic framework for formal theorem proving in Lean 4 centered on blueprint generation and refinement. A blueprint is a dependency graph of definitions and lemmas that builds up to the main theorem. First, Goedel-Architect generates a blueprint of formally stated definitions and lemmas, along with declared dependencies. This blueprint is optionally guided by a natural language proof. Then, a tool-equipped Lean prover component closes each open lemma node in parallel using relevant dependencies. Failed lemmas in turn drive refinement of the global blueprint. This strategy contrasts with other mainstream approaches which use recursive lemma decomposition, and can inefficiently loop on dead-end strategies. Using the open-weight DeepSeek-V4-Flash (284B-A13B) as the backbone, Goedel-Architect attains 99.2% pass@1 on MiniF2F-test and 75.6% pass@1 on PutnamBench. With an optional natural-language proof seeding the initial blueprint on the harder problems, we additionally close the remaining two MiniF2F-test problems (reaching 100%), lift PutnamBench to 88.8% (597/672), and solve 4/6 on IMO 2025, 11/12 on Putnam 2025, and 3/6 on USAMO 2026. This represents state-of-the-art performance for an open-source pipeline at a price point up to 500x less than comparable open-source pipelines.

---


### 285. [Complexity-Balanced Diffusion Splitting](https://arxiv.org/abs/2606.06477)

**<font color=#1a73e8>作者：</font>** Noam Issachar, Dani Lischinski, Raanan Fattal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Standard continuous-time generative models rely on monolithic architectures that must navigate vastly different signal regimes, from isotropic noise to intricate data distributions. While scaling model capacity improves performance, deploying a massive network uniformly across the entire generative timeline is inherently inefficient. In this work, we propose Complexity-Balanced Splitting (CBS), a principled framework for temporal capacity allocation that distributes the generative workload across multiple specialized sub-networks. Grounded in function approximation theory and de Boor's equidistribution principle, CBS partitions the diffusion timeline into segments of equal approximation burden, allocating more representational capacity to regions where the generative dynamics are more difficult to model. To estimate this local complexity, we introduce two complementary and tractable monitor functions: a spatial measure based on the flow's Dirichlet energy, and a geometric measure based on the acceleration of the sampling trajectories. Using a lightweight auxiliary model to estimate these complexity profiles, our approach eliminates the need for heuristic temporal splits or computationally expensive search procedures. Extensive evaluation across multiple architectures (SiT, JiT, and UNet) and datasets demonstrates that CBS consistently improves synthesis quality without increasing per-step inference cost. In particular, CBS improves FID by ~35% on SiT-XL with CFG relative to naive temporal partitioning. Project page is available at this https URL.

---


### 286. [Pretraining Recurrent Networks without Recurrence](https://arxiv.org/abs/2606.06479)

**<font color=#1a73e8>作者：</font>** Akarsh Kumar, Phillip Isola  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training recurrent neural networks (RNNs) requires assigning credit across long sequences of computations. Standard backpropagation through time (BPTT) addresses this problem poorly: it is sequential in time, limiting parallelism, and suffers from vanishing or exploding gradients, making long-range associations difficult to learn. We propose Supervised Memory Training (SMT), a method for training nonlinear RNNs that sidesteps recurrent credit propagation entirely by reducing RNN training to supervised learning on one-step memory transition labels $(m_t, x_{t+1}) \rightarrow m_{t+1}$. SMT acquires these memory labels by training a Transformer-based encoder on a predictive state objective--retaining only information from the past necessary to predict the future. By decoupling what to remember from how to update memory, SMT enables time-parallel RNN training with a stable $O(1)$ length gradient path between any two tokens--without ever unrolling the RNN. We find that SMT outperforms BPTT when pretraining various RNN architectures on tasks like language modeling and pixel sequence modeling. SMT enables nonlinear RNNs to better capture long-range dependencies and train in parallel, potentially unlocking the scaling of models that build temporal abstractions of past experience.

---


### 287. [Operation-Guided Progressive Human-to-AI Text Transformation Benchmark for Multi-Granularity AI-Text Detection](https://arxiv.org/abs/2606.06481)

**<font color=#1a73e8>作者：</font>** Sondos Mahmoud Bsharat, Jiacheng Liu, Xiaohan Zhao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As AI writing assistants become increasingly integrated into real-world drafting and revision workflows, many documents are no longer purely human-written or AI-generated, but instead result from progressive human-AI co-editing. However, existing AI-text detection benchmarks largely focus on final outputs and provide limited understanding of how AI authorship signals emerge, accumulate, or disappear throughout the revision process. We introduce OpAI-Bench, an operation-guided benchmark for studying progressive human-to-AI text transformation across document, sentence, token, and span granularities. Starting from human-written documents, OpAI-Bench constructs nine sequentially revised versions for each sample under predefined AI coverage levels and five representative AI edit operations, covering four domains while preserving complete authorship provenance at multiple granularities. The benchmark supports comprehensive evaluation with 8 document-level detectors, 7 sentence-level detectors, and 2 fine-grained token/span-level detectors. Experiments reveal that AI-text detectability is governed not only by the proportion of AI-edited content, but also by edit operation, domain, and cumulative revision history. Interestingly, we notice that mixed-authorship intermediate versions are often harder to detect than both fully human and heavily AI-edited endpoints, exposing non-monotonic detection patterns missed by existing benchmarks. OpAI-Bench provides a controlled testbed for analyzing whether, when, and how AI-assisted writing becomes detectable under realistic progressive editing scenarios. Our code and benchmark are available at this https URL.

---


### 288. [Regret Minimization with Adaptive Opponents in Repeated Games](https://arxiv.org/abs/2606.06486)

**<font color=#1a73e8>作者：</font>** Mingyang Liu, Asuman Ozdaglar, Tiancheng Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we study regret minimization in repeated games with \emph{adaptive} opponents who can respond based on histories of play. The standard metric of \emph{external regret} in online learning is known to fail to capture such adaptivity. To account for players' counterfactual reasoning, we introduce {\tt Repeated Policy Regret (RP-Regret)}, a game-theoretic metric that measures the difference between the \emph{realized} and the \emph{best-in-hindsight} accumulated utility when all players can \emph{respond} to the history of play. Compared to existing regret notions in this setting, ours is native to repeated game playing, enabling stronger comparators and opponents with fewer constraints, while maintaining the possibility of finding better equilibria when all players minimize it. We first identify necessary conditions for obtaining {\tt RP-Regret} sublinear in time, on the variation of the player's comparator strategies in the regret definition and on the memories of both the comparator and opponents' strategies. We then study additional conditions and provable algorithms to minimize {\tt RP-Regret}, which is by definition \emph{non-convex} in the strategy space. To address this challenge, we propose three algorithms: (i) one based on an optimization oracle, as assumed in some prior work in online non-convex learning; (ii) one that minimizes a convex and \emph{linearized} surrogate of {\tt RP-Regret} at each iteration; (iii) one that directly minimizes {\tt RP-Regret} when opponents change strategies slowly. Furthermore, when all players can run algorithms to minimize the {\tt RP-Regret} (or its linearized variant), certain subgame perfect equilibria of the repeated game can be learned. We also provide experiments showing that minimizing our regret notions can lead to more cooperative solutions with higher utility in games such as Stag-Hunt.

---


### 289. [TailLoR: Protecting Principal Components in Parameter-Efficient Continual Learning](https://arxiv.org/abs/2606.06494)

**<font color=#1a73e8>作者：</font>** Marius Dragoi, Ioana Pintilie, Alexandra Dragomir 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient finetuning methods based on spectral decomposition have enabled progress in Continual Learning. In this paper we introduce TailLoR, which utilizes the singular bases U and V of the pre-trained weights as a fixed reference frame to learn a low-rank update applied to the singular value matrix. A soft spectral penalty discourages updates aligned with dominant singular directions, reducing interference while routing fine-grained adaptation into the highly flexible, long-tail spectral coordinates.

---


> [!TIP]
> 当前位于：**251-289**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-289**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
