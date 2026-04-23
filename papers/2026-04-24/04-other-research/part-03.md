# 📦 其他研究 | 2026年04月24日

> 本类共 **220** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-220](./part-05.md)

---

### 101. [Text-to-Distribution Prediction with Quantile Tokens and Neighbor Context](https://arxiv.org/abs/2604.20216)

**<font color=#1a73e8>作者：</font>** Yilun Zhu, Yuan Zhuang, Nikhita Vedula 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Many applications of LLM-based text regression require predicting a full conditional distribution rather than a single point value. We study distributional regression under empirical-quantile supervision, where each input is paired with multiple observed quantile outcomes, and the target distribution is represented by a dense grid of quantiles. We address two key limitations of current approaches: the lack of local grounding for distribution estimates, and the reliance on shared representations that create an indirect bottleneck between inputs and quantile outputs. In this paper, we introduce Quantile Token Regression, which, to our knowledge, is the first work to insert dedicated quantile tokens into the input sequence, enabling direct input-output pathways for each quantile through self-attention. We further augment these quantile tokens with retrieval, incorporating semantically similar neighbor instances and their empirical distributions to ground predictions with local evidence from similar instances. We also provide the first theoretical analysis of loss functions for quantile regression, clarifying which distributional objectives each optimizes. Experiments on the Inside Airbnb and StackSample benchmark datasets with LLMs ranging from 1.7B to 14B parameters show that quantile tokens with neighbors consistently outperform baselines (~4 points lower MAPE and 2x narrower prediction intervals), with especially large gains on smaller and more challenging datasets where quantile tokens produce substantially sharper and more accurate distributions.

---


### 102. [Geometric Layer-wise Approximation Rates for Deep Networks](https://arxiv.org/abs/2604.20219)

**<font color=#1a73e8>作者：</font>** Shijun Zhang, Zuowei Shen, Yuesheng Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Depth is widely viewed as a central contributor to the success of deep neural networks, whereas standard neural network approximation theory typically provides guarantees only for the final output and leaves the role of intermediate layers largely unclear. We address this gap by developing a quantitative framework in which depth admits a precise scale-dependent interpretation. Specifically, we design a single shared mixed-activation architecture of fixed width $2dN+d+2$ and any prescribed finite depth such that each intermediate readout $\Phi_\ell$ is itself an approximant to the target function $f$. For $f\in L^p([0,1]^d)$ with $p\in [1,\infty)$, the approximation error of $\Phi_\ell$ is controlled by $(2d+1)$ times the $L^p$ modulus of continuity at the geometric scale $N^{-\ell}$ for all $\ell$. The estimate reduces to the geometric rate $(2d+1)N^{-\ell}$ if $f$ is $1$-Lipschitz. Our network design is inspired by multigrade deep learning, where depth serves as a progressive refinement mechanism: each new correction targets residual information at a finer scale while the earlier correction terms remain part of the later readouts, yielding a nested architecture that supports adaptive refinement without redesigning the preceding network.

---


### 103. [Markov reads Pushkin, again: A statistical journey into the poetic world of Evgenij Onegin](https://arxiv.org/abs/2604.20221)

**<font color=#1a73e8>作者：</font>** Angelo Maria Sabatini  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study applies symbolic time series analysis and Markov modeling to explore the phonological structure of Evgenij Onegin-as captured through a graphemic vowel/consonant (V/C) encoding-and one contemporary Italian translation. Using a binary encoding inspired by Markov's original scheme, we construct minimalist probabilistic models that capture both local V/C dependencies and large-scale sequential patterns. A compact four-state Markov chain is shown to be descriptively accurate and generative, reproducing key features of the original sequences such as autocorrelation and memory depth. All findings are exploratory in nature and aim to highlight structural regularities while suggesting hypotheses about underlying narrative dynamics.
The analysis reveals a marked asymmetry between the Russian and Italian texts: the original exhibits a gradual decline in memory depth, whereas the translation maintains a more uniform profile. To further investigate this divergence, we introduce phonological probes-short symbolic patterns that link surface structure to narrative-relevant cues. Tracked across the unfolding text, these probes reveal subtle connections between graphemic form and thematic development, particularly in the Russian original.
By revisiting Markov's original proposal of applying symbolic analysis to a literary text and pairing it with contemporary tools from computational statistics and data science, this study shows that even minimalist Markov models can support exploratory analysis of complex poetic material. When complemented by a coarse layer of linguistic annotation, such models provide a general framework for comparative poetics and demonstrate that stylized structural patterns remain accessible through simple representations grounded in linguistic form.

---


### 104. [Learning Spatial-Temporal Coherent Correlations for Speech-Preserving Facial Expression Manipulation](https://arxiv.org/abs/2604.20226)

**<font color=#1a73e8>作者：</font>** Tianshui Chen, Jianman Lin, Zhijing Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Speech-preserving facial expression manipulation (SPFEM) aims to modify facial emotions while meticulously maintaining the mouth animation associated with spoken content. Current works depend on inaccessible paired training samples for the person, where two aligned frames exhibit the same speech content yet differ in emotional expression, limiting the SPFEM applications in real-world scenarios. In this work, we discover that speakers who convey the same content with different emotions exhibit highly correlated local facial animations in both spatial and temporal spaces, providing valuable supervision for SPFEM. To capitalize on this insight, we propose a novel spatial-temporal coherent correlation learning (STCCL) algorithm, which models the aforementioned correlations as explicit metrics and integrates the metrics to supervise manipulating facial expression and meanwhile better preserving the facial animation of spoken content. To this end, it first learns a spatial coherent correlation metric, ensuring that the visual correlations of adjacent local regions within an image linked to a specific emotion closely resemble those of corresponding regions in an image linked to a different emotion. Simultaneously, it develops a temporal coherent correlation metric, ensuring that the visual correlations of specific regions across adjacent image frames associated with one emotion are similar to those in the corresponding regions of frames associated with another emotion. Recognizing that visual correlations are not uniform across all regions, we have also crafted a correlation-aware adaptive strategy that prioritizes regions that present greater challenges. During SPFEM model training, we construct the spatial-temporal coherent correlation metric between corresponding local regions of the input and output image frames as an additional loss to supervise the generation process.

---


### 105. [Machine Learning for Two-Stage Graph Sparsification for the Travelling Salesman Problem](https://arxiv.org/abs/2604.20236)

**<font color=#1a73e8>作者：</font>** Bo-Cheng Lin, Yi Mei, Mengjie Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-performance TSP solvers like LKH search within a sparsified candidate graph rather than over all possible edges. Graph sparsification is non-trivial: keep too many edges and the solver wastes time; cut too many and it loses edges that belong to the optimal tour. The two leading heuristic methods, $\alpha$-Nearest and POPMUSIC, produce high-quality candidate graphs, but no single heuristic is both sparse and reliable across all instance sizes and distributions. Machine learning methods can potentially learn better sparsification models. However, existing approaches operate on the complete graph, which is expensive and mostly restricted to Euclidean distances. To address this issue, we propose a two-stage graph sparsification approach: Stage~1 takes the union of $\alpha$-Nearest and POPMUSIC to maximise recall; Stage~2 trains a single model to reduce density. We conducted experiments across four TSPLIB distance types, five spatial distributions, and problem sizes from 50 to 500. The two-stage approach substantially reduces candidate-graph density while retaining high coverage, generalises across distance types and distributions, outperforms recent neural sparsification methods that are restricted to Euclidean distances, and becomes increasingly valuable at larger scales where single-stage heuristics degrade.

---


### 106. [Construction of a Battery Research Knowledge Graph using a Global Open Catalog](https://arxiv.org/abs/2604.20241)

**<font color=#1a73e8>作者：</font>** Luca Foppiano, Sae Dieb, Malik Zain 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Battery research is a rapidly growing and highly interdisciplinary field, making it increasingly difficult to track relevant expertise and identify potential collaborators across institutional boundaries. In this work, we present a pipeline for constructing an author-centric knowledge graph of battery research built on OpenAlex, a large-scale open bibliographic catalogue. For each author, we derive a weighted research descriptors vector that combines coarse-grained OpenAlex concepts with fine-grained keyphrases extracted from titles and abstracts using KeyBERT with ChatGPT (gpt-3.5-turbo) as the backend model, selected after evaluating multiple alternatives. Vector components are weighted by research descriptor origin, authorship position, and temporal recency. The framework is applied to a corpus of 189,581 battery-related works. The resulting vectors support author-author similarity computation, community detection, and exploratory search through a browser-based interface. The knowledge graph is then serialized in RDF and linked to Wikidata identifiers, making it interoperable with external linked open data sources and extensible beyond the battery domain. Unlike prior author-centric analyses confined to institutional repositories, our approach operates at cross-institutional scale and grounds similarity in domain semantics rather than citation or co-authorship structure alone.

---


### 107. [Bio-inspired Color Constancy: From Gray Anchoring Theory to Gray Pixel Methods](https://arxiv.org/abs/2604.20243)

**<font color=#1a73e8>作者：</font>** Kai-Fu Yang, Fu-Ya Luo, Yong-Jie Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Color constancy is a fundamental ability of many biological visual systems and a crucial step in computer imaging systems. Bio-inspired modeling offers a promising way to elucidate the computational principles underlying color constancy and to develop efficient computational methods. However, bio-inspired methods for color constancy remain underexplored and lack a comprehensive analysis. This paper presents a comprehensive technical framework that integrates biological mechanisms, computational theory, and algorithmic implementation for bio-inspired color constancy. Specifically, we systematically revisit the computational theory of biological color constancy, which shows that illuminant estimation can be reduced to the task of gray-anchor (pixel or surface) detection in early vision. Subsequently, typical gray-pixel detection methods, including Gray-Pixel and Grayness-Index, are reinterpreted within a unified theoretical framework with the Lambertian reflection model and biological color-opponent mechanisms. Finally, we propose a simple learning-based method that couples reflection-model constraints with feature learning to explore the potential of bio-inspired color constancy based on gray-pixel detection. Extensive experiments confirm the effectiveness of gray-pixel detection for color constancy and demonstrate the potential of bio-inspired methods.

---


### 108. [Mol-Debate: Multi-Agent Debate Improves Structural Reasoning in Molecular Design](https://arxiv.org/abs/2604.20254)

**<font color=#1a73e8>作者：</font>** Wengyu Zhang, Xiao-Yong Wei, Qing Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text-guided molecular design is a key capability for AI-driven drug discovery, yet it remains challenging to map sequential natural-language instructions with non-linear molecular structures under strict chemical constraints. Most existing approaches, including RAG, CoT prompting, and fine-tuning or RL, emphasize a small set of ad-hoc reasoning perspectives implemented in a largely one-shot generation pipeline. In contrast, real-world drug discovery relies on dynamic, multi-perspective critique and iterative refinement to reconcile semantic intent with structural feasibility. Motivated by this, we propose Mol-Debate, a generation paradigm that enables such dynamic reasoning through an iterative generate-debate-refine loop. We further characterize key challenges in this paradigm and address them through perspective-oriented orchestration, including developer-debater conflict, global-local structural reasoning, and static-dynamic integration. Experiments demonstrate that Mol-Debate achieves state-of-the-art performance against strong general and chemical baselines, reaching 59.82% exact match on ChEBI-20 and 50.52% weighted success rate on S$^2$-Bench. Our code is available at this https URL.

---


### 109. [uLEAD-TabPFN: Uncertainty-aware Dependency-based Anomaly Detection with TabPFN](https://arxiv.org/abs/2604.20255)

**<font color=#1a73e8>作者：</font>** Sha Lu, Jixue Liu, Stefan Peters 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Anomaly detection in tabular data is challenging due to high dimensionality, complex feature dependencies, and heterogeneous noise. Many existing methods rely on proximity-based cues and may miss anomalies caused by violations of complex feature dependencies. Dependency-based anomaly detection provides a principled alternative by identifying anomalies as violations of dependencies among features. However, existing methods often struggle to model such dependencies robustly and to scale to high-dimensional data with complex dependency structures. To address these challenges, we propose uLEAD-TabPFN, a dependency-based anomaly detection framework built on Prior-Data Fitted Networks (PFNs). uLEAD-TabPFN identifies anomalies as violations of conditional dependencies in a learned latent space, leveraging frozen PFNs for dependency estimation. Combined with uncertainty-aware scoring, the proposed framework enables robust and scalable anomaly detection. Experiments on 57 tabular datasets from ADBench show that uLEAD-TabPFN achieves particularly strong performance in medium- and high-dimensional settings, where it attains the top average rank. On high-dimensional datasets, uLEAD-TabPFN improves the average ROC-AUC by nearly 20\% over the average baseline and by approximately 2.8\% over the best-performing baseline, while maintaining overall superior performance compared to state-of-the-art methods. Further analysis shows that uLEAD-TabPFN provides complementary anomaly detection capability, achieving strong performance on datasets where many existing methods struggle.

---


### 110. [RADS: Reinforcement Learning-Based Sample Selection Improves Transfer Learning in Low-resource and Imbalanced Clinical Settings](https://arxiv.org/abs/2604.20256)

**<font color=#1a73e8>作者：</font>** Wei Han, David Martinez, Anna Khanina 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A common strategy in transfer learning is few shot fine-tuning, but its success is highly dependent on the quality of samples selected as training examples. Active learning methods such as uncertainty sampling and diversity sampling can select useful samples. However, under extremely low-resource and class-imbalanced conditions, they often favor outliers rather than truly informative samples, resulting in degraded performance. In this paper, we introduce RADS (Reinforcement Adaptive Domain Sampling), a robust sample selection strategy using reinforcement learning (RL) to identify the most informative samples. Experimental evaluations on several real world clinical datasets show our sample selection strategy enhances model transferability while maintaining robust performance under extreme class imbalance compared to traditional methods.

---


### 111. [Rethinking Where to Edit: Task-Aware Localization for Instruction-Based Image Editing](https://arxiv.org/abs/2604.20258)

**<font color=#1a73e8>作者：</font>** Jingxuan He, Xiyu Wang, Mengyu Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instruction-based image editing (IIE) aims to modify images according to textual instructions while preserving irrelevant content. Despite recent advances in diffusion transformers, existing methods often suffer from over-editing, introducing unintended changes to regions unrelated to the desired edit. We identify that this limitation arises from the lack of an explicit mechanism for edit localization. In particular, different editing operations (e.g., addition, removal and replacement) induce distinct spatial patterns, yet current IIE models typically treat localization in a task-agnostic manner. To address this limitation, we propose a training-free, task-aware edit localization framework that exploits the intrinsic source and target image streams within IIE models. For each image stream, We first obtain attention-based edit cues, and then construct feature centroids based on these attentive cues to partition tokens into edit and non-edit regions. Based on the observation that optimal localization is inherently task-dependent, we further introduce a unified mask construction strategy that selectively leverages source and target image streams for different editing tasks. We provide a systematic analysis for our proposed insights and approaches. Extensive experiments on EdiVal-Bench demonstrate our framework consistently improves non-edit region consistency while maintaining strong instruction-following performance on top of powerful recent image editing backbones, including Step1X-Edit and Qwen-Image-Edit.

---


### 112. [Causal-Transformer with Adaptive Mutation-Locking for Early Prediction of Acute Kidney Injury](https://arxiv.org/abs/2604.20259)

**<font color=#1a73e8>作者：</font>** Weizhi Nie, Haolin Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate early prediction of Acute Kidney Injury (AKI) is critical for timely clinical intervention. However, existing deep learning models struggle with irregularly sampled data and suffer from the opaque "black-box" nature of sequential architectures, strictly limiting clinical trust. To address these challenges, we propose CT-Former, integrating continuous-time modeling with a Causal-Transformer. To handle data irregularity without biased artificial imputation, our framework utilizes a continuous-time state evolution mechanism to naturally track patient temporal trajectories. To resolve the black-box problem, our Causal-Attention module abandons uninterpretable hidden state aggregation. Instead, it generates a directed structural causal matrix to identify and trace the exact historical onset of severe physiological shocks. By establishing clear causal pathways between historical anomalies and current risk predictions, CT-Former provides native clinical interpretability. Training follows a decoupled two-stage protocol to optimize the causal-fusion process independently. Extensive experiments on the MIMIC-IV cohort (N=18,419) demonstrate that CT-Former significantly outperforms state-of-the-art baselines. The results confirm that our explicitly transparent architecture offers an accurate and trustworthy tool for clinical decision-making.

---


### 113. [TL-RL-FusionNet: An Adaptive and Efficient Reinforcement Learning-Driven Transfer Learning Framework for Detecting Evolving Ransomware Threats](https://arxiv.org/abs/2604.20260)

**<font color=#1a73e8>作者：</font>** Jannatul Ferdous, Rafiqul Islam, Arash Mahboubi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern ransomware exhibits polymorphic and evasive behaviors by frequently modifying execution patterns to evade detection. This dynamic nature disrupts feature spaces and limits the effectiveness of static or predefined models. To address this challenge, we propose TL-RL-FusionNet, a reinforcement learning (RL)-guided hybrid framework that integrates frozen dual transfer learning (TL) backbones as feature extractors with a lightweight residual multilayer perceptron (MLP) classifier. The RL agent supervises training by adaptively reweighting samples in response to variations in observable ransomware behavior. Through reward and penalty signals, the agent prioritizes complex cases such as stealthy or polymorphic ransomware employing obfuscation, while down-weighting trivial samples including benign applications with simple file I/O operations or easily classified ransomware. This adaptive mechanism enables the model to dynamically refine its strategy, improving resilience against evolving threats while maintaining strong classification performance. The framework utilizes dynamic behavioral features such as file system activity, registry changes, network traffic, API calls, and anti-analysis checks, extracted from sandbox-generated JSON reports. These features are transformed into RGB images and processed using frozen EfficientNetB0 and InceptionV3 models to capture rich feature representations efficiently. Final classification is performed by a lightweight residual MLP guided by an RL (Q-learning) agent. Experiments on a balanced dataset of 1,000 samples (500 ransomware, 500 benign) show that TL-RL-FusionNet achieves 99.1% accuracy, 98.6% precision, 99.6% recall, and 99.74% AUC, outperforming non-RL baselines by up to 2.5% in accuracy and 3.1% in recall. Efficiency analysis shows 55% lower training time and 59% reduced RAM usage, demonstrating suitability for real-world deployment.

---


### 114. [Opportunistic Bone-Loss Screening from Routine Knee Radiographs Using a Multi-Task Deep Learning Framework with Sensitivity-Constrained Threshold Optimization](https://arxiv.org/abs/2604.20268)

**<font color=#1a73e8>作者：</font>** Zhaochen Li, Xinghao Yan, Runni Zhou 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Background: Osteoporosis and osteopenia are often undiagnosed until fragility fractures occur. Dual-energy X-ray absorptiometry (DXA) is the reference standard for bone mineral density (BMD) assessment, but access remains limited. Knee radiographs are obtained at high volume for osteoarthritis evaluation and may offer an opportunity for opportunistic bone-loss screening.
Objective: To develop and evaluate a multi-task deep learning system for opportunistic bone-loss screening from routine knee radiographs without additional imaging or patient visits.
Methods: We developed STR-Net, a multi-task framework for single-channel grayscale knee radiographs. The model includes a shared backbone, global average pooling feature aggregation, a shared neck, and a task-aware representation routing module connected to three task-specific heads: binary screening (Normal vs. Bone Loss), severity sub-classification (Osteopenia vs. Osteoporosis), and weakly coupled T-score regression with optional clinical variables. A sensitivity-constrained threshold optimization strategy (minimum sensitivity >= 0.86) was applied. The dataset included 1,570 knee radiographs, split at the patient level into training (n=1,120), validation (n=226), and test (n=224) sets.
Results: On the held-out test set, STR-Net achieved an AUROC of 0.933, sensitivity of 0.904, specificity of 0.773, and AUPRC of 0.956 for binary screening. Severity sub-classification achieved an AUROC of 0.898. The T-score regression branch showed a Pearson correlation of 0.801 with DXA-measured T-scores in a pilot subset (n=31), with MAE of 0.279 and RMSE of 0.347.
Conclusions: STR-Net enables single-pass bone-loss screening, severity stratification, and quantitative T-score estimation from routine knee radiographs. Prospective clinical validation is needed before deployment.

---


### 115. [Rethinking Intrinsic Dimension Estimation in Neural Representations](https://arxiv.org/abs/2604.20276)

**<font color=#1a73e8>作者：</font>** Rickmer Schulte, David Rügamer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The analysis of neural representation has become an integral part of research aiming to better understand the inner workings of neural networks. While there are many different approaches to investigate neural representations, an important line of research has focused on doing so through the lens of intrinsic dimensions (IDs). Although this perspective has provided valuable insights and stimulated substantial follow-up research, important limitations of this approach have remained largely unaddressed. In this paper, we highlight a crucial discrepancy between theory and practice of IDs in neural representations, theoretically and empirically showing that common ID estimators are, in fact, not tracking the true underlying ID of the representation. We contrast this negative result with an investigation of the underlying factors that may drive commonly reported ID-related results on neural representation in the literature. Building on these insights, we offer a new perspective on ID estimation in neural representations.

---


### 116. [AgentLens: Adaptive Visual Modalities for Human-Agent Interaction in Mobile GUI Agents](https://arxiv.org/abs/2604.20279)

**<font color=#1a73e8>作者：</font>** Jeonghyeon Kim, Byeongjun Joung, Junwon Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Mobile GUI agents can automate smartphone tasks by interacting directly with app interfaces, but how they should communicate with users during execution remains underexplored. Existing systems rely on two extremes: foreground execution, which maximizes transparency but prevents multitasking, and background execution, which supports multitasking but provides little visual awareness. Through iterative formative studies, we found that users prefer a hybrid model with just-in-time visual interaction, but the most effective visualization modality depends on the task. Motivated by this, we present AgentLens, a mobile GUI agent that adaptively uses three visual modalities during human-agent interaction: Full UI, Partial UI, and GenUI. AgentLens extends a standard mobile agent with adaptive communication actions and uses Virtual Display to enable background execution with selective visual overlays. In a controlled study with 21 participants, AgentLens was preferred by 85.7% of participants and achieved the highest usability (1.94 Overall PSSUQ) and adoption-intent (6.43/7).

---


### 117. [Fourier Series Coder: A Novel Perspective on Angle Boundary Discontinuity Problem for Oriented Object Detection](https://arxiv.org/abs/2604.20281)

**<font color=#1a73e8>作者：</font>** Minghong Wei, Pu Cao, Zhihao Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the rapid advancement of intelligent driving and remote sensing, oriented object detection has gained widespread attention. However, achieving high-precision performance is fundamentally constrained by the Angle Boundary Discontinuity (ABD) and Cyclic Ambiguity (CA) problems, which typically cause significant angle fluctuations near periodic boundaries. Although recent studies propose continuous angle coders to alleviate these issues, our theoretical and empirical analyses reveal that state-of-the-art methods still suffer from substantial cyclic errors. We attribute this instability to the structural noise amplification within their non-orthogonal decoding mechanisms. This mathematical vulnerability significantly exacerbates angular deviations, particularly for square-like objects. To resolve this fundamentally, we propose the Fourier Series Coder (FSC), a lightweight plug-and-play component that establishes a continuous, reversible, and mathematically robust angle encoding-decoding paradigm. By rigorously mapping angles onto a minimal orthogonal Fourier basis and explicitly enforcing a geometric manifold constraint, FSC effectively prevents feature modulus collapse. This structurally stabilized representation ensures highly robust phase unwrapping, intrinsically eliminating the need for heuristic truncations while achieving strict boundary continuity and superior noise immunity. Extensive experiments across three large-scale datasets demonstrate that FSC achieves highly competitive overall performance, yielding substantial improvements in high-precision detection. The code will be available at this https URL.

---


### 118. [MambaLiteUNet: Cross-Gated Adaptive Feature Fusion for Robust Skin Lesion Segmentation](https://arxiv.org/abs/2604.20286)

**<font color=#1a73e8>作者：</font>** Md Maklachur Rahman, Soon Ki Jung, Tracy Hammond  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent segmentation models have demonstrated promising efficiency by aggressively reducing parameter counts and computational complexity. However, these models often struggle to accurately delineate fine lesion boundaries and texture patterns essential for early skin cancer diagnosis and treatment planning. In this paper, we propose MambaLiteUNet, a compact yet robust segmentation framework that integrates Mamba state space modeling into a U-Net architecture, along with three key modules: Adaptive Multi-Branch Mamba Feature Fusion (AMF), Local-Global Feature Mixing (LGFM), and Cross-Gated Attention (CGA). These modules are designed to enhance local-global feature interaction, preserve spatial details, and improve the quality of skip connections. MambaLiteUNet achieves an average IoU of 87.12% and average Dice score of 93.09% across ISIC2017, ISIC2018, HAM10000, and PH2 benchmarks, outperforming state-of-the-art models. Compared to U-Net, our model improves average IoU and Dice by 7.72 and 4.61 points, respectively, while reducing parameters by 93.6% and GFLOPs by 97.6%. Additionally, in domain generalization with six unseen lesion categories, MambaLiteUNet achieves 77.61% IoU and 87.23% Dice, performing best among all evaluated models. Our extensive experiments demonstrate that MambaLiteUNet achieves a strong balance between accuracy and efficiency, making it a competitive and practical solution for dermatological image segmentation. Our code is publicly available at: this https URL.

---


### 119. [Generative Augmentation of Imbalanced Flight Records for Flight Diversion Prediction: A Multi-objective Optimisation Framework](https://arxiv.org/abs/2604.20288)

**<font color=#1a73e8>作者：</font>** Karim Aly, Alexei Sharpanskykh, Jacco Hoekstra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flight diversions are rare but high-impact events in aviation, making their reliable prediction vital for both safety and operational efficiency. However, their scarcity in historical records impedes the training of machine learning models utilised to predict them. This study addresses this scarcity gap by investigating how generative models can augment historical flight data with synthetic diversion records to enhance model training and improve predictive accuracy. We propose a multi-objective optimisation framework coupled with automated hyperparameter search to identify optimal configurations for three deep generative models: Tabular Variational Autoencoder (TVAE), Conditional Tabular Generative Adversarial Network (CTGAN), and CopulaGAN, with the Gaussian Copula (GC) model serving as a statistical baseline. The quality of the synthetic data was examined through a six-stage evaluation framework encompassing realism, diversity, operational validity, statistical similarity, fidelity, and predictive utility. Results show that the optimised models significantly outperform their non-optimised counterparts, and that synthetic augmentation substantially improves diversion prediction compared to models trained solely on real data. These findings demonstrate the effectiveness of hyperparameter-optimised generative models for advancing predictive modelling of rare events in air transportation.

---


### 120. [Efficient INT8 Single-Image Super-Resolution via Deployment-Aware Quantization and Teacher-Guided Training](https://arxiv.org/abs/2604.20291)

**<font color=#1a73e8>作者：</font>** Pham Phuong Nam Nguyen, Nam Tien Le, Thi Kim Trang Vo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Efficient single-image super-resolution (SISR) requires balancing reconstruction fidelity, model compactness, and robustness under low-bit deployment, which is especially challenging for x3 SR. We present a deployment-oriented quantized SISR framework based on an extract-refine-upsample design. The student performs most computation in the low-resolution space and uses a lightweight re-parameterizable backbone with PixelShuffle reconstruction, yielding a compact inference graph. To improve quality without significantly increasing complexity, we adopt a three-stage training pipeline: Stage 1 learns a basic reconstruction mapping with spatial supervision; Stage 2 refines fidelity using Charbonnier loss, DCT-domain supervision, and confidence-weighted output-level distillation from a Mamba-based teacher; and Stage 3 applies quantization-aware training directly on the fused deploy graph. We further use weight clipping and BatchNorm recalibration to improve quantization stability. On the MAI 2026 Quantized 4K Image Super-Resolution Challenge test set, our final AIO MAI submission achieves 29.79 dB PSNR and 0.8634 SSIM, obtaining a final score of 1.8 under the target mobile INT8 deployment setting. Ablation on Stage 3 optimization shows that teacher-guided supervision improves the dynamic INT8 TFLite reconstruction from 29.91 dB/0.853 to 30.0003 dB/0.856, while the fixed-shape deployable INT8 TFLite artifact attains 30.006 dB/0.857.

---


### 121. [Synthetic Flight Data Generation Using Generative Models](https://arxiv.org/abs/2604.20293)

**<font color=#1a73e8>作者：</font>** Karim Aly, Alexei Sharpanskykh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The increasing adoption of synthetic data in aviation research offers a promising solution to data scarcity and confidentiality challenges. This study investigates the potential of generative models to produce realistic synthetic flight data and evaluates their quality through a comprehensive four-stage assessment framework. The need for synthetic flight data arises from their potential to serve as an alternative to confidential real-world records and to augment rare events in historical datasets. These enhanced datasets can then be used to train machine learning models that predict critical events, such as flight delays, cancellations, diversions, and turnaround times. Two generative models, Tabular Variational Autoencoder (TVAE) and Gaussian Copula (GC), are adapted to generate synthetic flight information and compared based on their ability to preserve statistical similarity, fidelity, diversity, and predictive utility. Results indicate that while GC achieves higher statistical similarity and fidelity, its computational cost hinders its applicability to large datasets. In contrast, TVAE efficiently handles large datasets and enables scalable synthetic data generation. The findings demonstrate that synthetic data can support flight delay prediction models with accuracy comparable to those trained on real data. These results pave the way for leveraging synthetic flight data to enhance predictive modeling in air transportation.

---


### 122. [FSFM: A Biologically-Inspired Framework for Selective Forgetting of Agent Memory](https://arxiv.org/abs/2604.20300)

**<font color=#1a73e8>作者：</font>** Yingjie Gu, Bo Xiong, Yijuan Guo 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> For LLM agents, memory management critically impacts efficiency, quality, and security. While much research focuses on retention, selective forgetting--inspired by human cognitive processes (hippocampal indexing/consolidation theory and Ebbinghaus forgetting curve)--remains underexplored. We argue that in resource-constrained environments, a well-designed forgetting mechanism is as crucial as remembering, delivering benefits across three dimensions: (1) efficiency via intelligent memory pruning, (2) quality by dynamically updating outdated preferences and context, and (3) security through active forgetting of malicious inputs, sensitive data, and privacy-compromising content. Our framework establishes a taxonomy of forgetting mechanisms: passive decay-based, active deletion-based, safety-triggered, and adaptive reinforcement-based. Building on advances in LLM agent architectures and vector databases, we present detailed specifications, implementation strategies, and empirical validation from controlled experiments. Results show significant improvements: access efficiency (+8.49%), content quality (+29.2% signal-to-noise ratio), and security performance (100% elimination of security risks). Our work bridges cognitive neuroscience and AI systems, offering practical solutions for real-world deployment while addressing ethical and regulatory compliance. The paper concludes with challenges and future directions, establishing selective forgetting as a fundamental capability for next-generation LLM agents operating in real-world, resource-constrained scenarios. Our contributions align with AI-native memory systems and responsible AI development.

---


### 123. [AktivTalk: Digitizing the Talk Test for Voice-Based Exercise Intensity Self-Assessment and Exploring Automated Classification from Speech](https://arxiv.org/abs/2604.20302)

**<font color=#1a73e8>作者：</font>** Rania Islambouli, Laura Geiger, Daniela Wurhofer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Monitoring exercise intensity is critical for safe and effective physical activity, particularly for individuals with cardiovascular disease, where overexertion can pose serious risks. Although physiological measures such as heart rate are widely used for avoiding overexertion, they can be unreliable in certain cases, such as when affected by medication or when wearables are worn too loosely. We introduce AktivTalk, a mobile prototype that digitizes the clinically validated Talk Test to support voice-based, in-the-moment self-assessment of exertion. In a within-subject study with 20 participants, we collected exertion-labeled voice samples and found that AktivTalk was rated as highly usable and preferred over conductor-guided assessment. We further explored automated exertion classification from Talk Test speech. Using MFCC-based features with class balancing and cross-validation, a lightweight neural classifier achieved up to 90% accuracy for detecting high this http URL-high exertion from Talk Test recordings. This work highlights the potential of structured voice interactions for accessible exertion assessment and motivates future passive exertion monitoring from speech.

---


### 124. [Dual Causal Inference: Integrating Backdoor Adjustment and Instrumental Variable Learning for Medical VQA](https://arxiv.org/abs/2604.20306)

**<font color=#1a73e8>作者：</font>** Zibo Xu, Qiang Li, Ke Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical Visual Question Answering (MedVQA) aims to generate clinically reliable answers conditioned on complex medical images and questions. However, existing methods often overfit to superficial cross-modal correlations, neglecting the intrinsic biases embedded in multimodal medical data. Consequently, models become vulnerable to cross-modal confounding effects, severely hindering their ability to provide trustworthy diagnostic reasoning. To address this limitation, we propose a novel Dual Causal Inference (DCI) framework for MedVQA. To the best of our knowledge, DCI is the first unified architecture that integrates Backdoor Adjustment (BDA) and Instrumental Variable (IV) learning to jointly tackle both observable and unobserved confounders. Specifically, we formulate a Structural Causal Model (SCM) where observable cross-modal biases (e.g., frequent visual and textual co-occurrences) are mitigated via BDA, while unobserved confounders are compensated using an IV learned from a shared latent space. To guarantee the validity of the IV, we design mutual information constraints that maximize its dependence on the fused multimodal representations while minimizing its associations with the unobserved confounders and target answers. Through this dual mechanism, DCI extracts deconfounded representations that capture genuine causal relationships. Extensive experiments on four benchmark datasets, SLAKE, SLAKE-CP, VQA-RAD, and PathVQA, demonstrate that our method consistently outperforms existing approaches, particularly in out-of-distribution (OOD) generalization. Furthermore, qualitative analyses confirm that DCI significantly enhances the interpretability and robustness of cross-modal reasoning by explicitly disentangling true causal effects from spurious cross-modal shortcuts.

---


### 125. [Improving Facial Emotion Recognition through Dataset Merging and Balanced Training Strategies](https://arxiv.org/abs/2604.20307)

**<font color=#1a73e8>作者：</font>** Serap Kırbız  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, a deep learning framework is proposed for automatic facial emotion based on deep convolutional networks. In order to increase the generalization ability and the robustness of the method, the dataset size is increased by merging three publicly available facial emotion datasets: CK+, FER+ and KDEF. Despite the increase in dataset size, the minority classes still suffer from insufficient number of training samples, leading to data imbalance. The data imbalance problem is minimized by online and offline augmentation techniques and random weighted sampling. Experimental results demonstrate that the proposed method can recognize the seven basic emotions with 82% accuracy. The results demonstrate the effectiveness of the proposed approach in tackling the challenges of data imbalance and improving classification performance in facial emotion recognition.

---


### 126. [Sheaf Neural Networks on SPD Manifolds: Second-Order Geometric Representation Learning](https://arxiv.org/abs/2604.20308)

**<font color=#1a73e8>作者：</font>** Yuhan Peng, Junwen Dong, Yuzhi Zeng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks face two fundamental challenges rooted in the linear structure of Euclidean vector spaces: (1) Current architectures represent geometry through vectors (directions, gradients), yet many tasks require matrix-valued representations that capture relationships between directions-such as how atomic orientations covary in a molecule. These second-order representations are naturally captured by points on the symmetric positive definite matrices (SPD) manifold; (2) Standard message passing applies shared transformations across edges. Sheaf neural networks address this via edge-specific transformations, but existing formulations remain confined to vector spaces and therefore cannot propagate matrix-valued features. We address both challenges by developing the first sheaf neural network operates natively on the SPD manifold. Our key insight is that the SPD manifold admits a Lie group structure, enabling well-posed analogs of sheaf operators without projecting to Euclidean space. Theoretically, we prove that SPD-valued sheaves are strictly more expressive than Euclidean sheaves: they admit consistent configurations (global sections) that vector-valued sheaves cannot represent, directly translating to richer learned representations. Empirically, our sheaf convolution transforms effectively rank-1 directional inputs into full-rank matrices encoding local geometric structure. Our dual-stream architecture achieves SOTA on 6/7 MoleculeNet benchmarks, with the sheaf framework providing consistent depth robustness.

---


### 127. [Formalising the Logit Shift Induced by LoRA: A Technical Note](https://arxiv.org/abs/2604.20313)

**<font color=#1a73e8>作者：</font>** Xiang Shi, Shuaizhi Cheng, Mingwei Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This technical note provides a first-order formalisation of the logit shift and fact-margin change induced by Low-Rank Adaptation (LoRA). Using a first-order Fréchet approximation around the base model trajectory, we show that the multi-layer LoRA effect can be decomposed into a linear summation of layerwise contributions and a higher-order remainder term representing inter-layer coupling.

---


### 128. [Image Generators are Generalist Vision Learners](https://arxiv.org/abs/2604.20329)

**<font color=#1a73e8>作者：</font>** Valentin Gabeur, Shangbang Long, Songyou Peng 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent works show that image and video generators exhibit zero-shot visual understanding behaviors, in a way reminiscent of how LLMs develop emergent capabilities of language understanding and reasoning from generative pretraining. While it has long been conjectured that the ability to create visual content implies an ability to understand it, there has been limited evidence that generative vision models have developed strong understanding capabilities. In this work, we demonstrate that image generation training serves a role similar to LLM pretraining, and lets models learn powerful and general visual representations that enable SOTA performance on various vision tasks. We introduce Vision Banana, a generalist model built by instruction-tuning Nano Banana Pro (NBP) on a mixture of its original training data alongside a small amount of vision task data. By parameterizing the output space of vision tasks as RGB images, we seamlessly reframe perception as image generation. Our generalist model, Vision Banana, achieves SOTA results on a variety of vision tasks involving both 2D and 3D understanding, beating or rivaling zero-shot domain-specialists, including Segment Anything Model 3 on segmentation tasks, and the Depth Anything series on metric depth estimation. We show that these results can be achieved with lightweight instruction-tuning without sacrificing the base model's image generation capabilities. The superior results suggest that image generation pretraining is a generalist vision learner. It also shows that image generation serves as a unified and universal interface for vision tasks, similar to text generation's role in language understanding and reasoning. We could be witnessing a major paradigm shift for computer vision, where generative vision pretraining takes a central role in building Foundational Vision Models for both generation and understanding.

---


### 129. [Stability-Driven Motion Generation for Object-Guided Human-Human Co-Manipulation](https://arxiv.org/abs/2604.20336)

**<font color=#1a73e8>作者：</font>** Jiahao Xu, Xiaohan Yuan, Xingchen Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Co-manipulation requires multiple humans to synchronize their motions with a shared object while ensuring reasonable interactions, maintaining natural poses, and preserving stable states. However, most existing motion generation approaches are designed for single-character scenarios or fail to account for payload-induced dynamics. In this work, we propose a flow-matching framework that ensures the generated co-manipulation motions align with the intended goals while maintaining naturalness and effectiveness. Specifically, we first introduce a generative model that derives explicit manipulation strategies from the object's affordance and spatial configuration, which guide the motion flow toward successful manipulation. To improve motion quality, we then design an adversarial interaction prior that promotes natural individual poses and realistic inter-person interactions during co-manipulation. In addition, we also incorporate a stability-driven simulation into the flow matching process, which refines unstable interaction states through sampling-based optimization and directly adjusts the vector field regression to promote more effective manipulation. The experimental results demonstrate that our method achieves higher contact accuracy, lower penetration, and better distributional fidelity compared to state-of-the-art human-object interaction baselines. The code is available at this https URL.

---


### 130. [Hallucination Early Detection in Diffusion Models](https://arxiv.org/abs/2604.20354)

**<font color=#1a73e8>作者：</font>** Federico Betti, Lorenzo Baraldi, Lorenzo Baraldi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-Image generation has seen significant advancements in output realism with the advent of diffusion models. However, diffusion models encounter difficulties when tasked with generating multiple objects, frequently resulting in hallucinations where certain entities are omitted. While existing solutions typically focus on optimizing latent representations within diffusion models, the relevance of the initial generation seed is typically underestimated. While using various seeds in multiple iterations can improve results, this method also significantly increases time and energy costs. To address this challenge, we introduce HEaD+ (Hallucination Early Detection +), a novel approach designed to identify incorrect generations early in the diffusion process. The HEaD+ framework integrates cross-attention maps and textual information with a novel input, the Predicted Final Image. The objective is to assess whether to proceed with the current generation or restart it with a different seed, thereby exploring multiple-generation seeds while conserving time. HEaD+ is trained on the newly created InsideGen dataset of 45,000 generated images, each containing prompts with up to seven objects. Our findings demonstrate a 6-8% increase in the likelihood of achieving a complete generation (i.e., an image accurately representing all specified subjects) with four objects when applying HEaD+ alongside existing models. Additionally, HEaD+ reduces generation times by up to 32% when aiming for a complete image, enhancing the efficiency of generating complete and accurate object representations relative to leading models. Moreover, we propose an integrated localization module that predicts object centroid positions and verifies pairwise spatial relations (if requested by the users) at an intermediate timestep, gating generation together with object presence to further improve relation-consistent outcomes.

---


### 131. [SignDATA: Data Pipeline for Sign Language Translation](https://arxiv.org/abs/2604.20357)

**<font color=#1a73e8>作者：</font>** Kuanwei Chen, Tingyi Lin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sign-language datasets are difficult to preprocess consistently because they vary in annotation schema, clip timing, signer framing, and privacy constraints. Existing work usually reports downstream models, while the preprocessing pipeline that converts raw video into training-ready pose or video artifacts remains fragmented, backend-specific, and weakly documented. We present SignDATA, a config-driven preprocessing toolkit that standardizes heterogeneous sign-language corpora into comparable outputs for learning. The system supports two end-to-end recipes: a pose recipe that performs acquisition, manifesting, person localization, clipping, cropping, landmark extraction, normalization, and WebDataset export, and a video recipe that replaces pose extraction with signer-cropped video packaging. SignDATA exposes interchangeable MediaPipe and MMPose backends behind a common interface, typed job schemas, experiment-level overrides, and per-stage checkpointing with config- and manifest-aware hashes. We validate the toolkit through a research-oriented evaluation design centered on backend comparison, preprocessing ablations, and privacy-aware video generation on datasets. Our contribution is a reproducible preprocessing layer for sign-language research that makes extractor choice, normalization policy, and privacy tradeoffs explicit, configurable, and empirically this http URL is available at this https URL.

---


### 132. [ConeSep: Cone-based Robust Noise-Unlearning Compositional Network for Composed Image Retrieval](https://arxiv.org/abs/2604.20358)

**<font color=#1a73e8>作者：</font>** Zixu Li, Yupeng Hu, Zhiwei Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The Composed Image Retrieval (CIR) task provides a flexible retrieval paradigm via a reference image and modification text, but it heavily relies on expensive and error-prone triplet annotations. This paper systematically investigates the Noisy Triplet Correspondence (NTC) problem introduced by annotations. We find that NTC noise, particularly ``hard noise'' (i.e., the reference and target images are highly similar but the modification text is incorrect), poses a unique challenge to existing Noise Correspondence Learning (NCL) methods because it breaks the traditional ``small loss hypothesis''. We identify and elucidate three key, yet overlooked, challenges in the NTC task, namely (C1) Modality Suppression, (C2) Negative Anchor Deficiency, and (C3) Unlearning Backlash. To address these challenges, we propose a Cone-based robuSt noisE-unlearning comPositional network (ConeSep). Specifically, we first propose Geometric Fidelity Quantization, theoretically establishing and practically estimating a noise boundary to precisely locate noisy correspondence. Next, we introduce Negative Boundary Learning, which learns a ``diagonal negative combination'' for each query as its explicit semantic opposite-anchor in the embedding space. Finally, we design Boundary-based Targeted Unlearning, which models the noisy correction process as an optimal transport problem, elegantly avoiding Unlearning Backlash. Extensive experiments on benchmark datasets (FashionIQ and CIRR) demonstrate that ConeSep significantly outperforms current state-of-the-art methods, which fully demonstrates the effectiveness and robustness of our method.

---


### 133. [LaplacianFormer:Rethinking Linear Attention with Laplacian Kernel](https://arxiv.org/abs/2604.20368)

**<font color=#1a73e8>作者：</font>** Zhe Feng, Sen Lian, Changwei Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The quadratic complexity of softmax attention presents a major obstacle for scaling Transformers to high-resolution vision tasks. Existing linear attention variants often replace the softmax with Gaussian kernels to reduce complexity, but such approximations lack theoretical grounding and tend to oversuppress mid-range token interactions. We propose LaplacianFormer, a Transformer variant that employs a Laplacian kernel as a principled alternative to softmax, motivated by empirical observations and theoretical analysis. To address expressiveness degradation under low-rank approximations, we introduce a provably injective feature map that retains fine-grained token information. For efficient computation, we adopt a Nyström approximation of the kernel matrix and solve the resulting system using Newton--Schulz iteration, avoiding costly matrix inversion and SVD. We further develop custom CUDA implementations for both the kernel and solver, enabling high-throughput forward and backward passes suitable for edge deployment. Experiments on ImageNet show that LaplacianFormer achieves strong performance-efficiency trade-offs while improving attention expressiveness.

---


### 134. [Cold-Start Forecasting of New Product Life-Cycles via Conditional Diffusion Models](https://arxiv.org/abs/2604.20370)

**<font color=#1a73e8>作者：</font>** Ruihan Zhou, Zishi Zhang, Jinhui Han 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Forecasting the life-cycle trajectory of a newly launched product is important for launch planning, resource allocation, and early risk assessment. This task is especially difficult in the pre-launch and early post-launch phases, when product-specific outcome history is limited or unavailable, creating a cold-start problem. In these phases, firms must make decisions before demand patterns become reliably observable, while early signals are often sparse, noisy, and unstable We propose the Conditional Diffusion Life-cycle Forecaster (CDLF), a conditional generative framework for forecasting new-product life-cycle trajectories under cold start. CDLF combines three sources of information: static descriptors, reference trajectories from similar products, and newly arriving observations when available. Here, static descriptors refer to structured pre-launch characteristics of the product, such as category, price tier, brand or organization identity, scale, and access conditions. This structure allows the model to condition forecasts on relevant product context and to update them adaptively over time without retraining, yielding flexible multi-modal predictive distributions under extreme data scarcity. The method satisfies consistency with a horizon-uniform distributional error bound for recursive generation. Across studies on Intel microprocessor stock keeping unit (SKU) life cycles and the platform-mediated adoption of open large language model repositories, CDLF delivers more accurate point forecasts and higher-quality probabilistic forecasts than classical diffusion models, Bayesian updating approaches, and other state-of-the-art machine-learning baselines.

---


### 135. [Towards Event-Aware Forecasting in DeFi: Insights from On-chain Automated Market Maker Protocols](https://arxiv.org/abs/2604.20374)

**<font color=#1a73e8>作者：</font>** Huaiyu Jia, Jiehshun You, Yizhi Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated Market Makers (AMMs), as a core infrastructure of decentralized finance (DeFi), uniquely drive on-chain asset pricing through a deterministic reserve ratio mechanism. Unlike traditional markets, AMM price dynamics is triggered largely by on-chain events (e.g., swap) that change the reserve ratio, rather than by continuous responses to off-chain information. This makes event-level analysis crucial for understanding price formation mechanisms in AMMs. However, existing research generally neglects the micro-structural dynamics at the AMMs level, lacking both a comprehensive dataset covering multiple protocols with fine-grained event classification and an effective framework for event-aware modeling. To fill this gap, we construct a dataset containing 8.9 million on-chain event records from four representative AMMs protocols: Pendle, Uniswap v3, Aave and Morpho, with precise annotations of transaction type and block height timestamps. Furthermore, we propose an Uncertainty Weighted Mean Squared Error (UWM) loss function, which incorporates the block interval regression term into the traditional Time-Point Process (TPP) objective function by weighting the uncertainty with homoscedasticity. Extensive experiments on eight advanced TPP architectures demonstrate that this loss function reduces the time prediction error by an average of 56.41\% while maintaining the accuracy of event type prediction, establishing a robust benchmark for event-aware prediction in the AMMs ecosystem. This work provides the necessary data foundation and methodological framework for modeling the discreteness and event-driven characteristics of on-chain price discovery. All datasets and source code are publicly available. this https URL

---


### 136. [TLSCheck 2.0: An Enhanced Memory Forensics Approach to Efficiently Detect TLS Callbacks](https://arxiv.org/abs/2604.20378)

**<font color=#1a73e8>作者：</font>** Kartik N. Iyer, Parag H. Rughani  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Memory analysis is a crucial technique in digital forensics that enables investigators to examine the runtime state of a system through physical memory dumps. While significant advances have been made in memory forensics, the detection and analysis of Thread Local Storage (TLS) callbacks remain challenging due to their dual nature as both legitimate Windows constructs and potential vectors for malware execution. An early version of the TlsCheck plugin received recognition in the Volatility Plugin Contest 2024. In this paper, we present an enhanced version of TlsCheck for Volatility 3, designed to detect and analyze TLS callbacks in process memory. It implements precise detection of TLS callback tables through analysis of PE headers and memory structures, combined with disassembly of identified callback routines. The plugin supports both 32-bit and 64-bit architectures, offering investigators insights into callback locations, assembly behavior, and potential signs of suspicious activity. To enhance detection, we incorporate pattern matching using custom regular expressions and YARA rules, helping analysts identify specific code patterns or suspicious constructs within TLS callbacks. The framework also includes instruction-level analysis to highlight behavior often linked to malware, such as anti-debugging, code injection, and process manipulation. This implementation significantly improves defenders' ability to detect and investigate TLS-based threats during memory forensics, supporting more effective malware analysis and incident response operations.

---


### 137. [Distributional Value Estimation Without Target Networks for Robust Quality-Diversity](https://arxiv.org/abs/2604.20381)

**<font color=#1a73e8>作者：</font>** Behrad Koohy, Jamie Bayne  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quality-Diversity (QD) algorithms excel at discovering diverse repertoires of skills, but are hindered by poor sample efficiency and often require tens of millions of environment steps to solve complex locomotion tasks. Recent advances in Reinforcement Learning (RL) have shown that high Update-to-Data (UTD) ratios accelerate Actor-Critic learning. While effective, standard high-UTD algorithms typically utilise target networks to stabilise training. This requirement introduces a significant computational bottleneck, rendering them impractical for resource-intensive Quality-Diversity (QD) tasks where sample efficiency and rapid population adaptation are critical. In this paper, we introduce QDHUAC, a sample-efficient, target-free and distributional QD-RL algorithm that provides dense and low-variance gradient signals, which enables high-UTD training for Dominated Novelty Search whilst requiring an order of magnitude fewer environment steps. We demonstrate that our method enables stable training at high UTD ratios, achieving competitive coverage and fitness on high-dimensional Brax environments with an order of magnitude fewer samples than baselines. Our results suggest that combining target-free distributional critics with dominance-based selection is a key enabler for the next generation of sample-efficient evolutionary RL algorithms.

---


### 138. [Self-supervised pretraining for an iterative image size agnostic vision transformer](https://arxiv.org/abs/2604.20392)

**<font color=#1a73e8>作者：</font>** Nedyalko Prisadnikov, Danda Pani Paudel, Yuqian Fu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) dominate self-supervised learning (SSL). While they have proven highly effective for large-scale pretraining, they are computationally inefficient and scale poorly with image size. Consequently, foundational models like DINO are constrained to low-resolution processing. A recent foveal-inspired transformer achieves resolution agnosticism by iteratively processing a fixed-size context of multi-zoom patches. This model demonstrated promising results via supervised learning, utilizing a sequential, recurrent-like process without backpropagation through time. To unlock its potential as a foundational backbone, we introduce a novel sequential-to-global SSL framework based on DINO's self-distillation objective. Supported by an efficient integral-image patch extraction method, our approach enables large-scale pretraining for image-size agnostic vision encoders. We achieve competitive performance on ImageNet-1K and downstream classification tasks, maintaining a constant computational budget regardless of input resolution.

---


### 139. [MLG-Stereo: ViT Based Stereo Matching with Multi-Stage Local-Global Enhancement](https://arxiv.org/abs/2604.20393)

**<font color=#1a73e8>作者：</font>** Haoyu Zhang, Jingyi Zhou, Peng Ye 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the development of deep learning, ViT-based stereo matching methods have made significant progress due to their remarkable robustness and zero-shot ability. However, due to the limitations of ViTs in handling resolution sensitivity and their relative neglect of local information, the ability of ViT-based methods to predict details and handle arbitrary-resolution images is still weaker than that of CNN-based methods. To address these shortcomings, we propose MLG-Stereo, a systematic pipeline-level design that extends global modeling beyond the encoder stage. First, we propose a Multi-Granularity Feature Network to effectively balance global context and local geometric information, enabling comprehensive feature extraction from images of arbitrary resolution and bridging the gap between training and inference scales. Then, a Local-Global Cost Volume is constructed to capture both locally-correlated and global-aware matching information. Finally, a Local-Global Guided Recurrent Unit is introduced to iteratively optimize the disparity locally under the guidance of global information. Extensive experiments are conducted on multiple benchmark datasets, demonstrating that our MLG-Stereo exhibits highly competitive performance on the Middlebury and KITTI-2015 benchmarks compared to contemporaneous leading methods, and achieves outstanding results in the KITTI-2012 dataset.

---


### 140. [SpaCeFormer: Fast Proposal-Free Open-Vocabulary 3D Instance Segmentation](https://arxiv.org/abs/2604.20395)

**<font color=#1a73e8>作者：</font>** Chris Choy, Junha Lee, Chunghyun Park 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary 3D instance segmentation is a core capability for robotics and AR/VR, but prior methods trade one bottleneck for another: multi-stage 2D+3D pipelines aggregate foundation-model outputs at hundreds of seconds per scene, while pseudo-labeled end-to-end approaches rely on fragmented masks and external region proposals. We present SpaCeFormer, a proposal-free space-curve transformer that runs at 0.14 seconds per scene, 2-3 orders of magnitude faster than multi-stage 2D+3D pipelines. We pair it with SpaCeFormer-3M, the largest open-vocabulary 3D instance segmentation dataset (3.0M multi-view-consistent captions over 604K instances from 7.4K scenes) built through multi-view mask clustering and multi-view VLM captioning; it reaches 21x higher mask recall than prior single-view pipelines (54.3% vs 2.5% at IoU > 0.5). SpaCeFormer combines spatial window attention with Morton-curve serialization for spatially coherent features, and uses a RoPE-enhanced decoder to predict instance masks directly from learned queries without external proposals. On ScanNet200 we achieve 11.1 zero-shot mAP, a 2.8x improvement over the prior best proposal-free method; on ScanNet++ and Replica, we reach 22.9 and 24.1 mAP, surpassing all prior methods including those using multi-view 2D inputs.

---


### 141. [Onyx: Cost-Efficient Disk-Oblivious ANN Search](https://arxiv.org/abs/2604.20401)

**<font color=#1a73e8>作者：</font>** Deevashwer Rathee, Jean-Luc Watson, Zirui Neil Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Approximate nearest neighbor (ANN) search in AI systems increasingly handles sensitive data on third-party infrastructure. Trusted execution environments (TEEs) offer protection, but cost-efficient deployments must rely on external SSDs, which leaks user queries through disk access patterns to the host. Oblivious RAM (ORAM) can hide these access patterns but at a high cost; when paired with existing disk-based ANN search techniques, it makes poor use of SSD resources, yielding high latency and poor cost-efficiency. The core challenge for efficient oblivious ANN search over SSDs is balancing both bandwidth and access count. The state-of-the-art ORAM-ANN design minimizes access count at the ANN level and bandwidth at the ORAM level, each trading-off the other, leaving the combined system with both resources overutilized. We propose inverting this design, minimizing bandwidth consumption in the ANN layer and access count in the ORAM layer, since each component is better suited for its new role: ANN's inherent approximation allows for more bandwidth efficiency, while ORAM has no fundamental lower bounds on access count (as opposed to bandwidth). To this end, we propose a cost-efficient approach, Onyx, with two new co-designed components: Onyx-ANNS introduces a compact intermediate representation that proactively prunes the majority of bandwidth-intensive accesses without hurting recall, and Onyx-ORAM proposes a locality-aware shallow tree design that reduces access count while remaining compatible with bandwidth-efficient ORAM techniques. Compared to the state-of-the-art oblivious ANN search system, Onyx achieves $1.7-9.9\times$ lower cost and $2.3-12.3\times$ lower latency.

---


### 142. [Robustness of Spatio-temporal Graph Neural Networks for Fault Location in Partially Observable Distribution Grids](https://arxiv.org/abs/2604.20403)

**<font color=#1a73e8>作者：</font>** Burak Karabulut, Carlo Manna, Chris Develder  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fault location in distribution grids is critical for reliability and minimizing outage durations. Yet, it remains challenging due to partial observability, given sparse measurement infrastructure. Recent works show promising results by combining Recurrent Neural Networks (RNNs) and Graph Neural Networks (GNNs) for spatio-temporal learning. Still, many modern GNN architectures remain untested for this grid application, while existing GNN solutions have not explored GNN topology definitions beyond simply adopting the full grid topology to construct the GNN graph. We address these gaps by (i) systematically comparing a newly proposed graph-forming strategy (measured-only) to the traditional full-topology approach, and (ii) introducing STGNN (Spatio-temporal GNN) models based on GraphSAGE and an improved Graph Attention (GATv2), for distribution grid fault location; (iii) benchmarking them against state-of-the-art STGNN and RNN baselines on the IEEE 123-bus feeder. In our experiments, all evaluated STGNN variants achieve high performance and consistently outperform a pure RNN baseline, with improvements up to 11 percentage points F1. Among STGNN models, the newly explored RGATv2 and RGSAGE achieve only marginally higher F1 scores. Still, STGNNs demonstrate superior stability, with tight confidence intervals (within +/- 1.4%) compared to the RNN baseline (up to +/- 7.5%) across different experiment runs. Finally, our proposed reduced GNN topology (measured-only) shows clear benefits in both (i) model training time (6-fold reduction) and (ii) model performance (up to 11 points F1). This suggests that measured-only graphs offer a more practical, efficient, and robust framework for partially observable distribution grids.

---


### 143. [Calibrating conditional risk](https://arxiv.org/abs/2604.20409)

**<font color=#1a73e8>作者：</font>** Andrey Vasilyev, Yikai Wang, Xiaocheng Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce and study the problem of calibrating conditional risk, which involves estimating the expected loss of a prediction model conditional on input features. We analyze this problem in both classification and regression settings and show that it is fundamentally equivalent to a standard regression task. For classification settings, we further establish a connection between conditional risk calibration and individual/conditional probability calibration, and develop theoretical insights for the performance metric. This reveals that while conditional risk calibration is related to existing uncertainty quantification problems, it remains a distinct and standalone machine learning problem. Empirically, we validate our theoretical findings and demonstrate the practical implications of conditional risk calibration in the learning to defer (L2D) framework. Our systematic experiments provide both qualitative and quantitative assessments, offering guidance for future research in uncertainty-aware decision-making.

---


### 144. [Self-Awareness before Action: Mitigating Logical Inertia via Proactive Cognitive Awareness](https://arxiv.org/abs/2604.20413)

**<font color=#1a73e8>作者：</font>** Fulong Fan, Peilin Liu, Fengzhe Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models perform well on many reasoning tasks, yet they often lack awareness of whether their current knowledge or reasoning state is complete. In non-interactive puzzle settings, the narrative is fixed and the underlying structure is hidden; once a model forms an early hypothesis under incomplete premises, it can propagate that error throughout the reasoning process, leading to unstable conclusions. To address this issue, we propose SABA, a reasoning framework that explicitly introduces self-awareness of missing premises before making the final decision. SABA formulates reasoning as a recursive process that alternates between structured state construction and obstacle resolution: it first applies Information Fusion to consolidate the narrative into a verifiable base state, and then uses Query-driven Structured Reasoning to identify and resolve missing or underspecified premises by turning them into queries and progressively completing the reasoning state through hypothesis construction and state refinement. Across multiple evaluation metrics, SABA achieves the best performance on all three difficulty splits of the non-interactive Detective Puzzle benchmark, and it also maintains leading results on multiple public benchmarks.

---


### 145. [Scalable AI Inference: Performance Analysis and Optimization of AI Model Serving](https://arxiv.org/abs/2604.20420)

**<font color=#1a73e8>作者：</font>** Hung Cuong Pham, Fatih Gedikli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI research often emphasizes model design and algorithmic performance, while deployment and inference remain comparatively underexplored despite being critical for real-world use. This study addresses that gap by investigating the performance and optimization of a BentoML-based AI inference system for scalable model serving developed in collaboration with this http URL. The evaluation first establishes baseline performance under three realistic workload scenarios. To ensure a fair and reproducible assessment, a pre-trained RoBERTa sentiment analysis model is used throughout the experiments. The system is subjected to traffic patterns following gamma and exponential distributions in order to emulate real-world usage conditions, including steady, bursty, and high-intensity workloads. Key performance metrics, such as latency percentiles and throughput, are collected and analyzed to identify bottlenecks in the inference pipeline. Based on the baseline results, optimization strategies are introduced at multiple levels of the serving stack to improve efficiency and scalability. The optimized system is then reevaluated under the same workload conditions, and the results are compared with the baseline using statistical analysis to quantify the impact of the applied improvements. The findings demonstrate practical strategies for achieving efficient and scalable AI inference with BentoML. The study examines how latency and throughput scale under varying workloads, how optimizations at the runtime, service, and deployment levels affect response time, and how deployment in a single-node K3s cluster influences resilience during disruptions.

---


### 146. [Unlocking the Forecasting Economy: A Suite of Datasets for the Full Lifecycle of Prediction Market: [Experiments \& Analysis]](https://arxiv.org/abs/2604.20421)

**<font color=#1a73e8>作者：</font>** Huaiyu Jia, Luofeng Zhou, Wentao Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prediction markets are markets for trading claims on future events, such as presidential elections, and their prices provide continuously updated signals of collective beliefs. In decentralized platforms such as Polymarket, the market lifecycle spans market creation, token registration, trading, oracle interaction, dispute, and final settlement, yet the corresponding data are fragmented across heterogeneous off-chain and on-chain sources. We present the first continuously maintained dataset suite for the full lifecycle of decentralized prediction markets, built on Polymarket. To address the challenges of large-scale cross-source integration, incomplete linkage, and continuous synchronization, we build a unified relational data system that integrates three canonical layers: market metadata, fill-level trading records, and oracle-resolution events, through identifier resolution, on-chain recovery, and incremental updates. The resulting dataset spans October 2020 to March 2026 and comprises more than 770 thousand market records, over 943 million fill records, and nearly 2 million oracle events. We describe the data model, collection pipeline, and consistency mechanisms that make the dataset reproducible and extensible, and we demonstrate its utility through descriptive analyses of market activity and two downstream case studies: NBA outcome calibration and CPI expectation reconstruction.

---


### 147. [MedSkillAudit: A Domain-Specific Audit Framework for Medical Research Agent Skills](https://arxiv.org/abs/2604.20441)

**<font color=#1a73e8>作者：</font>** Yingyong Hou, Xinyuan Lao, Huimei Wang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Background: Agent skills are increasingly deployed as modular, reusable capability units in AI agent systems. Medical research agent skills require safeguards beyond general-purpose evaluation, including scientific integrity, methodological validity, reproducibility, and boundary safety. This study developed and preliminarily evaluated a domain-specific audit framework for medical research agent skills, with a focus on reliability against expert review. Methods: We developed MedSkillAudit (skill-auditor@1.0), a layered framework assessing skill release readiness before deployment. We evaluated 75 skills across five medical research categories (15 per category). Two experts independently assigned a quality score (0-100), an ordinal release disposition (Production Ready / Limited Release / Beta Only / Reject), and a high-risk failure flag. System-expert agreement was quantified using ICC(2,1) and linearly weighted Cohen's kappa, benchmarked against the human inter-rater baseline. Results: The mean consensus quality score was 72.4 (SD = 13.0); 57.3% of skills fell below the Limited Release threshold. MedSkillAudit achieved ICC(2,1) = 0.449 (95% CI: 0.250-0.610), exceeding the human inter-rater ICC of 0.300. System-consensus score divergence (SD = 9.5) was smaller than inter-expert divergence (SD = 12.4), with no directional bias (Wilcoxon p = 0.613). Protocol Design showed the strongest category-level agreement (ICC = 0.551); Academic Writing showed a negative ICC (-0.567), reflecting a structural rubric-expert mismatch. Conclusions: Domain-specific pre-deployment audit may provide a practical foundation for governing medical research agent skills, complementing general-purpose quality checks with structured audit workflows tailored to scientific use cases.

---


### 148. [The Origin of Edge of Stability](https://arxiv.org/abs/2604.20446)

**<font color=#1a73e8>作者：</font>** Elon Litman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Full-batch gradient descent on neural networks drives the largest Hessian eigenvalue to the threshold $2/\eta$, where $\eta$ is the learning rate. This phenomenon, the Edge of Stability, has resisted a unified explanation: existing accounts establish self-regulation near the edge but do not explain why the trajectory is forced toward $2/\eta$ from arbitrary initialization. We introduce the edge coupling, a functional on consecutive iterate pairs whose coefficient is uniquely fixed by the gradient-descent update. Differencing its criticality condition yields a step recurrence with stability boundary $2/\eta$, and a second-order expansion yields a loss-change formula whose telescoping sum forces curvature toward $2/\eta$. The two formulas involve different Hessian averages, but the mean value theorem localizes each to the true Hessian at an interior point of the step segment, yielding exact forcing of the Hessian eigenvalue with no gap. Setting both gradients of the edge coupling to zero classifies fixed points and period-two orbits; near a fixed point, the problem reduces to a function of the half-amplitude alone, which determines which directions support period-two orbits and on which side of the critical learning rate they appear.

---


### 149. [Decoding Text Spans for Efficient and Accurate Named-Entity Recognition](https://arxiv.org/abs/2604.20447)

**<font color=#1a73e8>作者：</font>** Andrea Maracani, Savas Ozkan, Junyi Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Named Entity Recognition (NER) is a key component in industrial information extraction pipelines, where systems must satisfy strict latency and throughput constraints in addition to strong accuracy. State-of-the-art NER accuracy is often achieved by span-based frameworks, which construct span representations from token encodings and classify candidate spans. However, many span-based methods enumerate large numbers of candidates and process each candidate with marker-augmented inputs, substantially increasing inference cost and limiting scalability in large-scale deployments. In this work, we propose SpanDec, an efficient span-based NER framework that targets this bottleneck. Our main insight is that span representation interactions can be computed effectively at the final transformer stage, avoiding redundant computation in earlier layers via a lightweight decoder dedicated to span representations. We further introduce a span filtering mechanism during enumeration to prune unlikely candidates before expensive processing. Across multiple benchmarks, SpanDec matches competitive span-based baselines while improving throughput and reducing computational cost, yielding a better accuracy-efficiency trade-off suitable for high-volume serving and on-device applications.

---


### 150. [Not all ANIMALs are equal: metaphorical framing through source domains and semantic frames](https://arxiv.org/abs/2604.20454)

**<font color=#1a73e8>作者：</font>** Yulia Otmakhova, Matteo Guida, Lea Frermann  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Metaphors are powerful framing devices, yet their source domains alone do not fully explain the specific associations they evoke. We argue that the interplay between source domains and semantic frames determines how metaphors shape understanding of complex issues, and present a computational framework that allows to derive salient discourse metaphors through their source domains and semantic frames. Applying this framework to climate change news, we uncover not only well-known source domains but also reveal nuanced frame-level associations that distinguish how the issue is portrayed. In analyzing immigration discourse across political ideologies, we demonstrate that liberals and conservatives systematically employ different semantic frames within the same source domains, with conservatives favoring frames emphasizing uncontrollability and liberals choosing neutral or more ``victimizing'' semantic frames. Our work bridges conceptual metaphor theory and linguistics, providing the first NLP approach for discovery of discourse metaphors and fine-grained analysis of differences in metaphorical framing. Code, data and statistical scripts are available at this https URL.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-220](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
