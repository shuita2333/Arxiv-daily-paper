# 📦 其他研究 | 2026年06月18日

> 本类共 **205** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-205](./part-05.md)

---

### 151. [KANLib -- An Modular, Extensible and Fast Kolmogorov-Arnold Network Implementation](https://arxiv.org/abs/2606.17927)

**<font color=#1a73e8>作者：</font>** Julian Hoever, Gregor Schiele  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Kolmogorov-Arnold Networks (KANs) have recently emerged as a promising alternative to traditional multilayer perceptrons by replacing linear weights with learnable univariate functions. Despite their theoretical advantages in interpretability and expressiveness, practical research of KANs remains difficult due to high computational costs and inconsistent feature support across existing frameworks. This paper introduces KANLib, a modular, extensible, and computationally efficient framework for developing and evaluating KAN architectures. KANLib unifies core concepts from existing implementations, including PyKAN, EfficientKAN, and FastKAN, within a consistent software architecture that emphasizes flexibility, feature parity, and high performance. The framework supports two basis function types, adaptive grid rescaling, grid extension, and fine-grained architectural customization while maintaining compatibility with standard PyTorch workflows. Experimental evaluation on the California Housing benchmark demonstrates that KANLib reproduces the predictive behavior of established reference KAN implementations while achieving competitive computational efficiency. Furthermore, the framework enables the exploration of architectural variations beyond standard KAN formulations with only minor impacts on predictive performance. Overall, KANLib provides a robust foundation for future research on scalable and extensible KAN architectures.

---


### 152. [PreAct: Computer-Using Agents that Get Faster on Repeated Tasks](https://arxiv.org/abs/2606.17929)

**<font color=#1a73e8>作者：</font>** Bojie Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-using agents drive real software through the screen -- clicking and typing -- but they solve every task from scratch: asked to repeat a task, an agent re-reads the screen, re-reasons every tap, and pays the full cost again. We present PreAct, which lets such an agent get faster on tasks it has done before. The first time it succeeds, PreAct compiles the run into a small state-machine program-states that check the screen, transitions that act-and on later runs replays it directly instead of invoking the agent 8.5-13x faster, with no per-step language-model calls. Replay is not blind: at each step PreAct checks that the screen matches what the program expects before acting, and hands control back to the agent the moment something is off.
PreAct applies the same discipline when deciding what to keep: a freshly compiled program enters the store only if, re-run from a clean state, an independent evaluator confirms it solved the task-catching programs that replay to their last step yet leave the task undone. Across a mobile, a desktop, and a web benchmark, this store-time check separates repeated runs that improve from ones that degrade as faulty programs accumulate, worth 1.75-2.6 tasks per benchmark, the same direction on all three; a fallback that explores afresh when no program fits brings PreAct level with a strong record-and-replay baseline. We also report what did not matter: prompt wording, runtime guardrails, and whether a language model or a plain embedding retriever selects which program to reuse.

---


### 153. [Predictive Analytics in E-Commerce for CustomerBehavior Forecasting using hybrid Ret-DNN withXGBoost Model](https://arxiv.org/abs/2606.17931)

**<font color=#1a73e8>作者：</font>** Degala Pushpa Sri, Mayank Atreya, Lakshmi. H 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In recent years, electronic (E) commerce services have rapidly increased in the daily lives of people, which helpsthem to purchase products online. However, retail platforms have struggled to understand customer behavior and make it difficult to predict their future purchases. To overcome these challenges, this study proposes a hybrid Retail Deep NeuralNetwork (Ret-DNN) with an Extreme Gradient Boosting(XGBoost) model for capturing temporal features and tabular dynamics of retail data. First, data were sourced from a UnitedKingdom (UK)-based online retailer that contains transactions with almost 500,000 records. Then, the collected data were pre-processed using a series of techniques, such as data cleaning, outlier handling, temporal feature extraction, feature encoding, and z-score normalization, to ensure that the data were ready for model training and testing. Subsequently, the preprocessed data were fed into the Ret-DNN model, which acts as a feature extractor to understand the complete context of customer transactions. Further, the extracted data were fed as input into the XGBoost model, which predicted the final output as the purchase probability of customers. Finally, the proposed Ret-DNN XGBoost model achieved better results by attaining aMean Absolute Error (MAE) 0.2193 when compared to the existing Ret-DNN model.
Keywords: Customer behavior forecasting, extreme gradientboosting, electronic commerce, predictive analytic, retail deepneural networks.

---


### 154. [MoonSplat: Monocular Online Gaussian Splatting with Sim(3) Global Optimization](https://arxiv.org/abs/2606.17935)

**<font color=#1a73e8>作者：</font>** Guo Pu, Yixuan Han, Haofeng Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online 3D reconstruction from monocular image sequences is a challenging and ongoing research topic. 3D Gaussian Splatting (3DGS), leveraging its high-quality real-time rendering capability, empowers online 3D reconstruction to represent dense scenes with enhanced expressiveness, and thus holds great promise for a wide range of applications such as robotics and AR/VR. However, existing online 3DGS methods still suffer from some key challenges: fragile camera pose estimation due to the lack of global optimization, and low optimization efficiency in large-scale or long-sequence scenarios. To address these issues, we propose a robust and efficient online voxelized 3DGS reconstruction framework integrated with global $\text{Sim}(3)$ optimization, which enables reliable camera tracking and efficient global loop closure for both camera poses and voxelized 3DGS. To accelerate the convergence of the voxelized 3DGS, we further introduce a color residual learning strategy, which not only boosts optimization speed but also enhances rendering quality. Extensive experiments on diverse indoor and outdoor datasets demonstrate that our method achieves state-of-the-art performance in both camera pose estimation accuracy and rendering quality, while retaining real-time efficiency. Additionally, we develop and deploy a real-world UAV-based active reconstruction system grounded on our proposed method, validating its robustness and generalizability for practical online 3D reconstruction tasks. Our code and data are available at this https URL.

---


### 155. [Children Are Not the Enemy: Child-Fit Security as an Alternative to Bans and Surveillance](https://arxiv.org/abs/2606.17957)

**<font color=#1a73e8>作者：</font>** Kopo M. Ramokapane, Rui Huan, Zaina Dkaidek 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Digital technologies are now central to children's learning, play, communication, identity formation, and social participation. Yet dominant approaches to children's online safety often rely on containment mechanisms, including bans, age gates, parental controls, monitoring, and screen-time restrictions. These approaches can be useful in specific contexts, but they often frame child protection primarily as a problem of restricting access to systems designed for adults. In this paper, we argue that this framing is inadequate for children's digital lives and insufficient as a security paradigm. We propose Child-fit security, a design paradigm in which technologies likely to be used by children treat a child as legitimate users, not attackers to be excluded, vulnerabilities to be patched, or risks to be managed. In this paradigm, children's wellbeing, development, privacy, safety, agency, and rights become core security requirements. This shifts the focus of protection from apps, accounts, and data to the child-system relationship, which means protecting both the child and their participation. We conceptualise child-fit security, contrast it with containment-oriented approaches, define its core principles, and discuss its implications for security design. We conclude by presenting a research agenda for making child-fit security operational.

---


### 156. [Robustness of Similarity-based Positional Encoding Under Rotations: Theoretical Analysis and Experimental Validation](https://arxiv.org/abs/2606.17961)

**<font color=#1a73e8>作者：</font>** Andrea Santomauro, Luigi Portinale, Giorgio Leonardi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Positional encoding is a fundamental component of Transformer architectures, as it injects information about the spatial or sequential arrangement of inputs. Among recent alternatives to standard absolute and sinusoidal encodings, similarity-based positional encoding (simPE) has emerged as a flexible framework for representing positional structure through pairwise relations. simPE was originally designed for medical imaging applications, where geometric robustness is especially relevant: small rotations naturally arise during image acquisition, induced by imaging instruments, patient positioning, or slight acquisition misalignments. Despite its empirical promise, the theoretical behavior of simPE under geometric perturbations has not been fully characterized. In this paper, we study the robustness of simPE with respect to rotations, combining formal theoretical analysis with experimental validation. We first show that simPE is generally not rotation-invariant. We then prove that, under mild Lipschitz assumptions on the elementary components, simPE is stable under rotational perturbations and derive explicit perturbation bounds in Frobenius norm. We validate these findings experimentally on four controlled datasets--a synthetic Arrow dataset, a synthetic Shapes dataset (four geometric shape categories), a synthetic Digits dataset, and a benchmark image classification dataset (FashionMNIST)--in which training and validation images are kept in a fixed canonical orientation while test images are subjected to increasing rotation angles. Across all datasets, simPE consistently outperforms standard learned positional encoding in terms of accuracy, F1 score, precision, and recall under rotation, particularly in the small-to-moderate angle regime, corroborating the theoretical stability guarantees.

---


### 157. [Reload-Mamba: Hierarchical Anti-Dilution State-Space Modeling for Multi-Class Semantic Segmentation](https://arxiv.org/abs/2606.17966)

**<font color=#1a73e8>作者：</font>** Sheng-Wei Chan, Hsin-Jui Pan, Jen-Shiun Chiang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mamba-based state space models offer linear-time long-range modeling for high-resolution dense prediction, but sequential state-space propagation can attenuate boundary-sensitive and detail-sensitive responses that are critical in multi-class semantic segmentation. We propose Reload-Mamba, a semantic segmentation framework that addresses this propagation-induced response dilution through three segmentation-specific designs: (i) a boundary-supervised local detail prior that is explicitly trained with ground-truth boundary masks to identify regions requiring response restoration; (ii) a class-uncertainty-aware Reload Gate that incorporates per-pixel class entropy from a pre-reload auxiliary head as an additional gating signal, a formulation that is informative only under multi-class dense prediction; and (iii) a hierarchical multi-level Reload mechanism that applies anti-dilution refinement at three decoder levels and fuses the restored representations top-down. Built upon a ConvNeXt-Tiny encoder with a multi-scale decoder and four-directional Mamba scanning with pixel-wise directional attention, Reload-Mamba achieves 47.9% single-scale (48.9% multi-scale) mIoU on ADE20K and 83.2% single-scale mIoU on Cityscapes. With ResNet-101 + COCO pre-training under the standard DeepLab-style protocol, Reload-Mamba reaches 87.8% mIoU on PASCAL VOC 2012 val. Controlled ablations show that each of the three segmentation-specific designs contributes beyond a direct port of the prior anti-dilution architecture proposed for binarization, cumulatively improving over the direct-port baseline by +2.2 mIoU on ADE20K.

---


### 158. [SegDINO: Introducing Multi-Scale Structure into DINO for Efficient Medical Image Segmentation](https://arxiv.org/abs/2606.17972)

**<font color=#1a73e8>作者：</font>** Sicheng Yang, Hongqiu Wang, Zhaohu Xing 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised DINO models provide strong transferable visual representations, yet applying them directly to image segmentation remains challenging. Existing approaches commonly rely on heavy decoders with complex upsampling, introducing substantial parameter and computational overhead. We observe that introducing scale into DINO features is far more critical than increasing decoder capacity. In this work, we present SegDINO, an efficient segmentation framework that integrates a DINOv3 backbone with lightweight scale modeling. SegDINO introduces Token Pyramid Adaptation (TPA) to reorganize intermediate DINO features into a pseudo multi-scale hierarchy, and Scale-Aware Decoding (SAD) for efficient intra-scale refinement and top-down multi-scale propagation. We further curate PanCT, a new CT dataset containing 284 patients with expert-annotated pancreatic tumors, to assess SegDINO's ability to handle difficult small-lesion cases. Extensive experiments on PanCT and three public benchmarks demonstrate that SegDINO achieves state-of-the-art results with high efficiency. The code is available at this https URL.

---


### 159. [MoCo-AIS: A Contrastive Learning Framework for Similarity Computation of Vessel Trajectories](https://arxiv.org/abs/2606.17978)

**<font color=#1a73e8>作者：</font>** Ruixin Song, Md Mahbub Alam, Zahra Sadeghi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Trajectory similarity is a fundamental task in analyzing mobility patterns, essential for applications such as route pattern extraction, mobility prediction, and anomaly detection. Traditional distance-based measures for computing similarity incur high computational cost, driving the adoption of lightweight learning-based approaches. Supervised methods rely on extensive labels derived from traditional distance measures and often reproduce these metrics, which limits generalization. While self-supervised learning addresses this issue through contrastive learning, it lacks a unified framework, making it difficult to compare deep learning (DL) models for consistent trajectory representation. Accordingly, this paper presents MoCo-AIS, a unified framework for learning vessel trajectory embeddings based on the Momentum Contrast (MoCo) paradigm, which formulates similarity learning through positive and negative trajectory pairs. Within this framework, we evaluate a diverse set of leading DL models on large-scale, real-world vessel-tracking AIS datasets that capture diverse navigation behaviors and operating conditions. Results demonstrate that our framework significantly improves similarity learning over existing baselines, while providing a benchmarking platform for evaluating trajectory representation models.

---


### 160. [Gaussian Light Field Splatting: A Physical Prior-Driven Vision Transformer for Unsupervised Low-Light Image Enhancement](https://arxiv.org/abs/2606.17985)

**<font color=#1a73e8>作者：</font>** Yuhan Chen, Wenxuan Yu, Guofa Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing unsupervised low-light image enhancement methods often encounter local exposure imbalance and color distortion under complex non-uniform illumination. In addition, most Vision Transformers lack an explicit mechanism for modeling the physical priors of illumination degradation. To address these limitations, we propose GLFS, a Gaussian light field splatting-based Vision Transformer that integrates continuous physical illumination modeling from Gaussian splatting into the Transformer architecture. In GLFS, scene illumination is represented by a superposition of anisotropic Gaussian basis functions. Physics-guided biases are introduced into self-attention to adaptively infer a spatial gain field, enabling accurate and uniform restoration under complex illumination. To reduce color bias and structural degradation during enhancement, a color-vector angular loss and a luminance-edge loss are further developed. These losses enforce hue consistency and improve the structural fidelity of local details. Extensive ablation studies and quantitative evaluations show that GLFS provides clear advantages in illumination correction and detail preservation. It achieves state-of-the-art performance and offers a new representation paradigm for low-light image enhancement.

---


### 161. [Recover Semantics First, Generate Better: Improved Latent Modeling for 3D MRI Reconstruction and Cross-Contrast Synthesis](https://arxiv.org/abs/2606.17989)

**<font color=#1a73e8>作者：</font>** Yonghao Chen, Sicheng Yang, Rui Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-contrast magnetic resonance imaging (MRI) provides complementary information for clinical diagnosis. However, acquiring all MRI sequences is often time-consuming and costly. Recent generative models perform cross-contrast synthesis to address this issue by inferring absent contrasts from the available ones. Nevertheless, synthesizing 3D MRI presents significant challenges. Due to the massive volume sizes, operating directly in the pixel space is computationally prohibitive; therefore, a common approach is to first compress the 3D volumes into a latent space and subsequently train generative models in that space. We observe that existing compression architectures face several critical issues: they under-preserve long-range anatomical coherence, discard clinically meaningful semantics, and rely on optimization objectives that lead to over-smoothed reconstructions. Ultimately, these shortcomings compromise the performance of subsequent generative models. In this work, we propose a semantics-first latent modeling framework for 3D MRI reconstruction and cross-contrast synthesis. Specifically, we introduce a Latent Harmonization Encoder (LHE) to capture global anatomical dependencies, ensuring coherent volumetric representations. To mitigate semantic degradation during latent compression, we further design a Semantic Recovery Block (SRB) that injects high-level priors from a self-supervised semantic teacher, enhancing contrast-aware separability in the latent space. Additionally, we propose an Anatomy-aware Frequency Loss (AFL) to adaptively preserve diagnostically relevant high-frequency structures. Extensive experiments on two public multi-contrast MRI datasets demonstrate consistent improvements in reconstruction fidelity and cross-contrast synthesis quality. Our code is available at this https URL.

---


### 162. [Multiple cyclicity and Wavelet Decomposition with Channel Correlation for Long-term Time Series Forecasting](https://arxiv.org/abs/2606.17996)

**<font color=#1a73e8>作者：</font>** Bin Wang, Heming Yang, Jinfang Sheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cyclicity and trend are important components of time series data and many studies based on cyclicity and trend have achieved good results in long-term time series forecasting. However, we believe that current work neglects the influence of real-world inter-channel correlations in time series data which leads to suboptimal predictions. Furthermore, these models rely on complex designs to capture diverse information so that resulting in low computational efficiency. To address this challenge, we propose McWC, a long-term time series forecasting model that separately models the cyclicity, trend, and inter-channel correlations. Specifically, McWC first decouples cyclical information from data using a multi-layer cyclicity construction module. Then, it extracts inter-channel correlations using multi-layer perceptron. Next, it models and fuses the multi-layer high-frequency and low-frequency information from data using a multi-level wavelet decomposition module. Finally, it aggregates the results of different components to obtain the output. Simultaneously, we decouple intra-channel autocorrelations by calculating a loss function in the frequency domain. Experiments on six real-world datasets demonstrate that McWC achieves state-of-the-art performance, exhibiting excellent computational efficiency and historical information extraction capabilities.

---


### 163. [AIGS-Net: Compact Illumination Field Modeling via 2D Gaussian Splatting for Fast Low-Light Image Enhancement](https://arxiv.org/abs/2606.17998)

**<font color=#1a73e8>作者：</font>** Yuhan Chen, Kunyang Huang, Fuchen Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing low-light image enhancement methods often face a bottleneck between the representation capacity of illumination-field modeling and computational complexity. To address this issue, this paper proposes an Adaptive Illumination Gaussian Splatting Network (AIGS-Net), an ultra-lightweight architecture for fast low-light enhancement. Unlike conventional static priors, AIGS-Net constructs an input-adaptive 2D Gaussian Splatting illumination field. The opacity of Gaussian basis functions is dynamically modulated by relative luminance statistics of the input image, and spatially varying illumination compensation is rendered through ordered alpha compositing. To guide adaptive illumination compensation efficiently, a zero-parameter nonlinear multiscale contextual encoding module is introduced to extract low-frequency structures and local contrast cues without additional convolutional weights. To suppress noise amplification and sensor-induced color bias, AIGS-Net integrates noise-mask estimation, locked single-channel Gamma mapping, cross-channel consistency regularization, and target color-alignment constraints. Experiments on LOL and LSRW benchmarks show that AIGS-Net improves detail recovery and color fidelity while requiring only approximately 40 learnable parameters, achieving an effective trade-off between enhancement quality and extreme inference efficiency.

---


### 164. [C2FL: Clustered Continual Federated Learning under Spatial and Temporal Drift](https://arxiv.org/abs/2606.18003)

**<font color=#1a73e8>作者：</font>** Davide Domini, Gianluca Aguzzi, Lorenzo Pellegrini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Collective Adaptive Systems (CAS) increasingly rely on machine learning to let each node learn from locally sensed data, aligning its behavior with the surrounding environment. Scaling this intelligence, however, raises fundamental challenges: sensed data is often privacy-sensitive, preventing centralized collection; nodes are mobile, traversing regions where nearby nodes perceive similar phenomena while distant ones observe radically different conditions, creating natural spatial clusters; and these distributions evolve over time due to mobility, introducing temporal drift that makes local models progressively stale. These dynamics arise across domains - vehicular sensing, drone-based monitoring, smartphone crowdsensing - yet the interplay of privacy, spatial heterogeneity, and temporal drift severely undermines conventional learning strategies. Therefore, we propose C2FL, a fully distributed Federated Learning (FL) approach where nodes self-organize into learning groups through spatial clustering, reflecting the geographic structure of the environment. To counteract temporal drift, each node combines experience replay with a dwell-time-aware adaptive averaging step, progressively incorporating the regional consensus as it remains longer within the same area, while preserving previously acquired knowledge under evolving distributions. We evaluate our approach on synthetic experiments that systematically reproduce spatial and temporal shifts, showing that standard federated strategies degrade significantly under these conditions and that our method restores robust collective adaptation.

---


### 165. [PhaseWin: An Efficient Search Algorithm for Faithful Visual Attribution](https://arxiv.org/abs/2606.18008)

**<font color=#1a73e8>作者：</font>** Zihan Gu, Ruoyu Chen, Junchi Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual attribution is a fundamental tool for interpreting modern vision and vision-language models, particularly when their decisions must be inspected, diagnosed, or audited. Its goal is to explain how a model's decision depends on local regions of the visual input, typically by assigning an importance ordering over candidate image regions. Given an image partitioned into $n$ regions, faithful attribution can be cast as an ordered subset-search problem, in which progressively inserting the selected regions should recover the target model response as early as possible. Exhaustive search over region subsets incurs exponential cost, while the widely used greedy search still requires a quadratic number of model evaluations, because every selection step rescores all remaining candidates. We propose PhaseWin, an efficient subset-search algorithm for faithful visual attribution. PhaseWin reorganizes greedy region selection into a phased window-search procedure: rather than re-evaluating the full candidate set at every step, it alternates between global candidate screening, adaptive pruning, and localized window refinement, while preserving the essential region-ranking behavior of greedy search. We analyze PhaseWin under monotone evidence-accumulation conditions and show that, under feature-level structural assumptions, it attains controllable linear evaluation complexity together with near-greedy faithfulness guarantees. Extensive experiments on image classification, object detection, visual grounding, and image captioning show that, among all compared attribution methods, PhaseWin reaches high faithfulness with the fewest forward passes, empirically realizing the predicted reduction from $O(n^2)$ to $O(n)$. The code is available at this https URL.

---


### 166. [Co-Creativity at the Table: A Qualitative Analysis of Creative Interactions in the Podcast "Adventure AI"](https://arxiv.org/abs/2606.18010)

**<font color=#1a73e8>作者：</font>** Hanna Dodd, Daniel G. Brown  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Tabletop role-playing games provide a unique environment for interaction with artificial intelligence (AI) due to their complex and collaborative nature. We analyze Adventure AI, a podcast featuring human-AI interactions in Dungeons & Dragons play, to examine how AI is and can be used in tabletop role-playing gaming and how players perceive this use. We complete a qualitative analysis of three seasons of this podcast, from 2023 to 2025, reporting on the overarching themes of roles of AI, roles of humans, the evaluations and failures of AI, and its treatment as a person and character at the table. There are many aspects of the game where artificial intelligence succeeds, while there are others where it is less appropriate. This analysis gives a basis for future work on where artificial intelligence should and should not be used in gaming spaces.

---


### 167. [LegalHalluLens: Typed Hallucination Auditing and Calibrated Multi-Agent Debate for Trustworthy Legal AI](https://arxiv.org/abs/2606.18021)

**<font color=#1a73e8>作者：</font>** Lalit Yadav, Akshaj Gurugubelli  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI systems deployed in legal workflows hallucinate at rates that aggregate metrics report at ~52%, but this average conceals where errors concentrate and in which direction they run, leaving compliance officers without an actionable signal for trustworthy deployment. We present LegalHalluLens, an auditing framework with three components: typed hallucination profiles across four legally-motivated claim categories (numeric, temporal, obligation/entitlement, factual) over CUAD (Hendrycks et al., 2021); a Risk Direction Index (RDI) that reduces omission-versus-invention bias to a single deployment-comparable scalar; and a typed debate pipeline calibrated to both magnitudes and directions. Across 510 contracts and 249,252 clause-level instances we measure a within-model gap of approximately 38-40 pp between obligation/numeric and temporal claims that aggregate reporting hides, and show that two systems with matched 52% rates can carry opposite RDIs. The debate pipeline reduces fabricated detections by 45% with per-category gains tracking the diagnosis, matching commercial APIs with a substantially smaller backbone (4B active parameters). Typed profiles and RDI surface failure modes that aggregate metrics hide; we further show these diagnostics serve as calibration inputs for multi-agent debate pipelines, where Skeptic challenges and asymmetric gates targeted at measured failure modes outperform generically-tuned debate. The framework supports direction-aware procurement, accountability, and agent design for legal AI deployed in the wild.

---


### 168. [Recursive Scaling in Masked Diffusion Models](https://arxiv.org/abs/2606.18022)

**<font color=#1a73e8>作者：</font>** Alba Carballo-Castro, Julianna Piskorz, Paulius Rauba 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Masked diffusion models (MDMs) have recently emerged as a promising paradigm for sequence generation. Scaling MDMs is conventionally achieved by increasing the parameter count or the number of denoising steps. We introduce Recursive Masked Diffusion Models (R-MDMs), which add recursive depth as a third scaling axis by repeatedly applying the same denoising transformer within each diffusion step. Recursion enables iterative refinement of the output through parameter reuse, increasing effective model depth without increasing parameter count. Across structured generation tasks, including Sudoku and Countdown, we show that R-MDMs achieve substantially improved parameter efficiency: a model with $L$ recursive iterations often matches the performance of non-recursive baselines with roughly $L\times$ more parameters. Moreover, recursive refinement can partially substitute for additional denoising steps, allowing recursive models to reach the same generation quality with fewer forward passes at inference time. These results suggest that recursive depth is a practically useful scaling mechanism for MDMs, improving both parameter efficiency and the allocation of test-time compute.

---


### 169. [LoopCoder-v2: Only Loop Once for Efficient Test-Time Computation Scaling](https://arxiv.org/abs/2606.18023)

**<font color=#1a73e8>作者：</font>** Jian Yang, Shawn Guo, Wei Zhang 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped Transformers scale latent computation by repeatedly applying shared blocks, but sequential looping increases latency and KV-cache memory with the loop count. Parallel loop Transformers (PLT) alleviate this cost through cross-loop position offsets (CLP) and shared-KV gated sliding-window attention, making loop count a practical design choice. We therefore study PLT loop-count selection through a gain--cost view: an extra loop may refine representations, but CLP also introduces a positional mismatch at each loop boundary. We instantiate this study by training LoopCoder-v2, a family of 7B PLT coders with different loop counts, from scratch on 18T tokens, followed by matched instruction tuning and evaluation. Empirically, the two-loop variant delivers broad gains over the non-looped baseline across code generation, code reasoning, agentic software engineering, and tool-use benchmarks, improving SWE-bench Verified from 43.0 to 64.4 points and Multi-SWE from 14.0 to 31.0 points. In contrast, variants with three or more loops regress, revealing a strongly non-monotonic loop-count effect. Our diagnostics show that loop 2 provides the main productive refinement, while later loops yield diminishing, oscillatory updates and reduced representational diversity. Because the CLP-induced mismatch remains roughly fixed as refinement gains shrink, the offset cost increasingly dominates. This gain--cost trade-off explains PLT's saturation at two loops and provides diagnostics for loop-count selection.

---


### 170. [Catastrophic Forgetting is Low-Rank: A Function-Space Theory for Continual Adaptation](https://arxiv.org/abs/2606.18024)

**<font color=#1a73e8>作者：</font>** Ido Nitzan Hidekel, Dan Raviv  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Catastrophic forgetting in continual adaptation is usually studied through parameter drift, replay, or distillation, but these views do not identify which output-space directions are vulnerable. We give a function-space account in the NTK regime: new-task training induces old-task prediction drift through the cross-task kernel, yielding a closed-form predictor for the forgetting vector before any new-task gradient step. In frozen-backbone linear-head PEFT-CL, where the model is linear in the trainable parameters, the predictor is exact up to numerical precision; for nonlinear adapters/full fine-tuning, it is a local NTK approximation. The same expression reveals that forgetting concentrates in a small number of old-task NTK eigenmodes and under frozen linear heads gives a Kronecker scaling rule for the vulnerable rank. These results clarify the relation to prior NTK-overlap theory, explain why parameter-space regularizers can miss output-space interference, and motivate a targeted spectral regularizer.

---


### 171. [ConTex: Reformulating Counterfactual Generation For Time Series Forecasting](https://arxiv.org/abs/2606.18049)

**<font color=#1a73e8>作者：</font>** Jan Voets, Hasan Tercan, Tobias Meisen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decision-making with deep learning-based time series forecasting requires not only accurate predictions but also actionable insights. However, current architectures do not inherently provide such information. Specifically, guidance is needed on how current conditions must be modified to shift from a predicted outcome to a desired future scenario. Counterfactual explanations provide a natural framework for this task, as they represent minimal input changes that alter the model's prediction, indicating when and how intervention is required. Existing approaches rely on instance-wise optimization, leading to inconsistency across instances, high computational costs, and limited applicability in real-time settings.
To address these limitations, we reformulate counterfactual generation for time series forecasting as the problem of learning a globally consistent intervention strategy, allowing counterfactuals to be generated through a single shared function. We propose Counterfactual Time Series Explanations (ConTex), a model-agnostic, decomposed architecture comprising a temporal context encoder and a conditional encoder, followed by two heads that capture interventions in terms of temporal relevance and modification strength. This structure overcomes the instability and inconsistency of instance-based approaches by producing targeted, interpretable interventions across time and feature dimensions in a single forward pass, making it suitable for real-time applications.
Across multiple forecasting architectures and benchmark datasets, ConTex achieves state-of-the-art validity while generating sparse counterfactuals that minimize the number of necessary interventions. Additionally, our approach reduces computational cost by at least 12-36x compared to instance-wise generation and supports real-time inference at approximately 0.007 seconds.

---


### 172. [An Empirical Analysis of AI Slop in Music Streaming](https://arxiv.org/abs/2606.18052)

**<font color=#1a73e8>作者：</font>** Stanley Wu, Josephine Passananti, Viresh Mittal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Generative AI models lower the bar for content creation, making it easy for any user to create professional-looking images, text and music with minimal effort. This has enabled a new cottage industry around creation of "AI slop" mass quantities of mediocre content produced to generate revenue, often through misrepresentation as human-authored content, or scams involving automated scripts and fake consumption.
While there are obvious parallels between the AI-slop industry and "traditional" email spam networks, it might be too early to determine if AI slop generation can grow into a similar self-sustaining industry. In this paper, we look specifically at the music industry, and explore the question: Can we prevent AI music slop from growing into a self-sustaining shadow industry?
To answer this question, we characterize the current state of AI slop in music, and its pipeline from generation, distribution, and consumption by users on streaming platforms. By examining growth and engagement on Spotify, we confirm that AI music exhibits AI slop characteristics: the overwhelming majority (93%) of AI music receive few, if any listener plays, and are rarely recommended. AI musicians "spray and pray," releasing large volumes of music across multiple genres in hopes of generating a hit. We also explore the AI slop pipeline by generating and publishing our own AI tracks onto streaming through 11 indie music distributors. We find distributors have inconsistent and largely unenforced policies on AI music, making it surprisingly easy to publish mass produced AI songs. Finally, we consider AI music detection, and find that current methods lack accuracy or robustness. As generation costs decrease, we believe slop generation in music will become self-sustainable, unless concrete steps are taken by the music industry. We consider and discuss potential mitigation methods based on our findings.

---


### 173. [ConSA: Controllable Sparsity in Hybrid Attention via Learnable Allocation](https://arxiv.org/abs/2606.18056)

**<font color=#1a73e8>作者：</font>** Yao Chen, Yinqi Yang, Junyuan Shang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hybrid architectures combining full attention (FA) and sliding-window attention (SWA) are a promising paradigm for efficient LLM inference. However, existing methods typically rely on hand-crafted rules or simple post-hoc heuristics for FA/SWA allocation and offer limited analysis of the attention behaviors underlying these designs. We propose Controllable Sparsity in Hybrid Attention (ConSA), a framework that learns optimal FA/SWA assignment under a user-specified sparsity target. ConSA employs L0 regularization to learn binary masks selecting between FA and SWA for each attention unit, while an augmented Lagrangian constraint enforces the target sparsity at either layer or KV-head granularity. We evaluate ConSA on two LLMs at the 0.6B and 1.7B scales. Learned allocations consistently outperform rule-based baselines, with KV-head-wise allocation yielding clear gains over layer-wise allocation. The learned patterns place SWA in the bottom layers and concentrate FA into contiguous middle-layer blocks, diverging from evenly interleaved patterns in rule-based methods. This structure persists across model scales, sparsity levels, and allocation granularities, revealing a fine-grained spectrum of intrinsic attention behaviors that underlies the learned allocation.

---


### 174. [When AI Says "I have been in similar situations": Synthetic Lived Experience in Peer-Like Caregiver Support](https://arxiv.org/abs/2606.18057)

**<font color=#1a73e8>作者：</font>** Drishti Goel, Violeta J. Rodriguez, Daniel S. Brown 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Caregivers often turn to online communities for informational and emotional support. In these spaces, peer supporters frequently draw on personal narratives to respond to emotionally complex caregiving situations. As LLMs are increasingly designed as peer-like sources of support, they introduce a critical tension: AI can provide immediate, private, and nonjudgmental support, but it cannot authentically possess the lived experiences that make human peer support meaningful. Yet, when prompted to sound peer-like, LLMs may generate language that implies lived experience. This creates a synthetic lived experience paradox: the same experiential language that may make AI support feel warm, relatable, and peer-like can also falsely position the system as someone with lived experience. We examine this paradox in the context of family caregivers of people living with Alzheimer's Disease and Related Dementias (ADRD). Drawing on caregiver support exchanges from online communities and prompted peer-like responses from three LLMs -- LLaMA, GPT-4o-mini, and MedGemma -- we analyze how human peers use personal narratives and how AI incorporates similar narrative forms. Psycholinguistic analysis shows that peer responses used significantly more first-person and past-focused language than peer-like AI responses. Qualitatively, we identify seven types of personal narratives in human peer support and show that AI often captures their emotional work, but can fabricate experiential grounding. These findings reveal a narrative authenticity gap: peer-like AI can generate synthetic lived experience without the real experience that makes peer support meaningful. We argue that caregiver-support AI systems need mechanisms to distinguish supportive peer-like framing from fabricated lived experience, ensuring that models can offer warmth and validation without falsely positioning themselves as experiential peers.

---


### 175. [Intelligence Entropy Principle and the ADE Stability Engineering Framework](https://arxiv.org/abs/2606.18065)

**<font color=#1a73e8>作者：</font>** Dexing Liu  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> As LLM-driven multi-agent systems (MAS) transition from lab to production, system behavior exhibits nonlinear degradation. We introduce the Intelligence Entropy Principle: probability-driven systems spontaneously drift toward disorder, formalized as S(t) = S0 * exp(alpha*t/Cm), where Cm is a model capability coefficient we propose. Lyapunov analysis yields the stabilization condition lambda > alpha/Cm. We construct the ADE (Agent Delivery Engineering) four-layer framework (L1 Physical Laws through L4 User Adaptation) with 23 core components. Validation spans 100K-scale experiments and 33.6 days of production monitoring. We propose a Five-Layer Disorder Taxonomy unifying failures under structural collapse, and present Elastic Organization as an original MAS morphology. Results: channel fracture reduced from 69-98% to near 0%; system death probability below 0.02%.

---


### 176. [Volterra Generative Models](https://arxiv.org/abs/2606.18071)

**<font color=#1a73e8>作者：</font>** Yusen Jia, Bingyan Han  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Score-based diffusion models typically use Brownian perturbations, which provide tractable reverse-time dynamics but impose memoryless noising. We introduce Volterra generative models, a continuous-time score-based framework whose forward process injects path-dependent noise through fractional kernels. To handle the non-Markovian and non-semimartingale dynamics, we construct finite-dimensional Markovian lifts using Gaussian quadrature in both regimes and a hybrid finite-difference exponential approximation in the smooth regime. We prove squared error bounds, derive an augmented linear-Gaussian forward process, and show that the learning can remain data-dimensional by considering residual states and analytic auxiliary Gaussian scores. We also identify covariance and reverse-time degeneracies caused by shared Brownian factors and signed smooth-regime weights. The degeneracy motivates stabilized conditioning and, for stiff larger lifts, a Gaussian-bridge reconstruction sampler. Experiments on MNIST and CIFAR-10 show that persistent fractional perturbations with small Markovian lifts can improve score-based generation on MNIST and provide a promising extension to natural images, while the bridge sampler provides a stability mechanism for larger lifts.

---


### 177. [Edge Flow: A Tractable and Predictive Continuous-Time Model for Gradient Descent at the Edge of Stability](https://arxiv.org/abs/2606.18080)

**<font color=#1a73e8>作者：</font>** Pierre Marion  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gradient descent in deep learning may operate at the edge of stability (EoS), a regime in which the largest eigenvalue of the loss Hessian hovers near the stability threshold $2/\eta$, where $\eta$ is the learning rate. Classical analysis tools such as gradient flow and the descent lemma do not apply here, motivating the search for a continuous-time model valid at EoS. We propose Edge Flow, a system of three coupled ordinary differential equations that provides a tractable, faithful, and predictive model of gradient descent dynamics at EoS. Edge Flow decomposes the dynamics into a center, an oscillation direction, and an oscillation magnitude. The center follows a modified gradient flow on a symmetrized loss; the direction tracks a top eigenvector of the Hessian via Rayleigh quotient dynamics; and the magnitude grows or decays exponentially depending on whether the sharpness exceeds or falls below the threshold $2/\eta$. Crucially, sharpness stabilization emerges from the coupled dynamics via a self-stabilization feedback loop. Discretizing Edge Flow only requires two gradient evaluations and one Hessian--vector product at each iteration. We demonstrate empirically that Edge Flow tracks the dynamics of gradient descent at least as faithfully as previously proposed continuous-time EoS models, while in addition resolving the oscillation of the sharpness at the onset of EoS, and that it provides a principled framework for understanding and mitigating instabilities in this regime.

---


### 178. [S4oP: Operator-level Pruning of Structured State Space Models for Resource-Constrained Devices](https://arxiv.org/abs/2606.18096)

**<font color=#1a73e8>作者：</font>** Marco Deano, Filippo Ziche, Nicola Bombieri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Structured State Space Models (SSMs), including the S4 and S4D architectures, have recently emerged as powerful alternatives to attention-based models for capturing long-range dependencies in sequential data. Despite their strong empirical performance, deploying these models in time- and resource-constrained settings remains challenging due to their computational and memory demands. In this paper, we propose a novel incremental, operator-level pruning approach for S4- and S4D-based models that significantly reduces inference cost while preserving predictive performance. To the best of our knowledge, this is the first work to systematically investigate structured operator pruning for SSMs. Our method progressively prunes model operators by interleaving structured masking with fine-tuning, while jointly monitoring accuracy and inference latency. We implement this approach within a unified training and evaluation framework that enables systematic exploration of efficiency-accuracy trade-offs. Experiments across multiple benchmark datasets show that pruning up to 70% of the model operators preserves the performance of the original models in most cases, while substantially reducing inference latency. These results demonstrate that structured operator pruning is an effective and previously unexplored strategy for improving the efficiency of SSMs and facilitate their deployment in practical, resource-constrained scenarios.

---


### 179. [Trust the Right Teacher: Quality-Aware Self-Distillation for GUI Grounding](https://arxiv.org/abs/2606.18101)

**<font color=#1a73e8>作者：</font>** Jingyuan Huang, Zuming Huang, Yucheng Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graphical user interface (GUI) grounding requires vision-language models (VLMs) to identify small target elements in high-resolution screenshots and predict precise screen coordinates. On-policy self-distillation (OPSD) is a promising post-training approach for this coordinate-sensitive task, since it provides dense token-level teacher signals beyond hard coordinate labels. However, naive OPSD is not well suited to GUI grounding: OPSD evaluates the teacher on student-generated prefixes, the quality of coordinate-token teacher signals can degrade when the prefix has already deviated from the target coordinate, leading to unreliable teacher signal. To mitigate this, We propose quality-aware self-distillation for VLM-based GUI grounding, which improves coordinate-token teacher-signal quality through soft correctness-aware gating and teacher-probability scaling. The soft correctness-aware gate checks whether the teacher's current coordinate-token prediction can still be completed into the ground-truth box under the student-generated prefix. If not, the corresponding teacher signal is down-weighted. Teacher-probability scaling then uses the teacher's confidence as a lightweight factor to further calibrate the strength of the gated supervision. A key empirical finding is that neither component alone improves overall performance, whereas combining them consistently improves performance. This suggests that the two mechanisms play complementary roles: correctness-aware gating suppresses unreliable coordinate-token supervision, while teacher-probability scaling calibrates the strength of the remaining signals. Experiments across six GUI grounding benchmarks show that our method consistently improves the base model and outperforms strong baselines.

---


### 180. [Deep Reinforcement Learning for Minimum Zero-Forcing Sets](https://arxiv.org/abs/2606.18106)

**<font color=#1a73e8>作者：</font>** Steve Halley, Maurício Gruppi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper explores the problem of finding the minimum zero-forcing set on undirected graphs and proposes an adapted machine-learning framework to solve the problem. The minimum zero-forcing set problem is a graph coloring problem where the color of an initial set of nodes propagates throughout a network. The set of nodes is zero-forcing if it forces all uncolored nodes to change color under the constraint of the color-change rule. There are several applications to this problem across different domains such as network science, network control, and designing logical circuits. Finding the minimum zero-forcing set is shown to be NP-hard. We propose a reinforcement learning framework, SD-ZFS, that adapts the S2V-DQN architecture to the ZFS problem. We train several models on this adapted framework and analyze the performance across graph datasets that have varying structures. We evaluate how the models trained on the framework generalize, scale, and transfer to different network types. The results demonstrate the effectiveness of the framework when compared against the optimal solution and greedy heuristic. We provide further insight into how the ZFS problem can be solved through machine-learning and the influence of network structure on the problem.

---


### 181. [Learning Fair Pareto-Optimal Policies in Multi-Objective Reinforcement Learning](https://arxiv.org/abs/2606.18111)

**<font color=#1a73e8>作者：</font>** Umer Siddique, Peilang Li, Yongcan Cao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fairness is an important aspect of decision-making in multi-objective reinforcement learning (MORL), where policies must ensure both optimality and equity across multiple, potentially conflicting objectives. While single-policy MORL methods can learn fair policies for fixed user preferences using welfare functions such as the generalized Gini welfare function (GGF), they fail to provide the diverse set of policies necessary for dynamic or unknown user preferences. To address this limitation, we formalize the fair optimization problem in multi-policy MORL, where the goal is to learn a set of Pareto-optimal policies that ensure fairness across all possible user preferences. Our key technical contributions are threefold: (1) We show that for concave, piecewise-linear welfare functions (e.g., GGF), fair policies remain in the convex coverage set (CCS), which is an approximated Pareto front for linear scalarization. (2) We demonstrate that non-stationary policies, augmented with accrued reward histories, and stochastic policies improve fairness by dynamically adapting to historical inequities. (3) We propose three novel algorithms, which include integrating GGF with multi-policy multi-objective Q-Learning (MOQL), state-augmented multi-policy MOQL for learning non-statoinary policies, and its novel extension for learning stochastic policies. We evaluate our algorithms across various domains and compare our methods against the state-of-the-art MORL baselines. The empirical results show that our methods learn a set of fair policies that accommodate different user preferences.

---


### 182. [Ternary Mamba: Grouped Quantization-Aware Training of W1.58A16 State Space Models](https://arxiv.org/abs/2606.18114)

**<font color=#1a73e8>作者：</font>** Ramprasath Ganesaraja, Sahil Dilip Panse, Swathika N  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> State Space Models (SSMs) such as Mamba-2 offer linear-time inference but their memory footprint limits edge deployment. Prior ternary SSM work (Slender-Mamba) trains from scratch on 150B tokens; we show a pretrained checkpoint suffices, reducing the marginal token budget by 1,000x. Using grouped quantization-aware training (QAT) with knowledge distillation from a frozen FP16 teacher, we compress Mamba-2 1.3B to 3.61x (2,687 to 744 MB) and achieve 48.1% zero-shot accuracy (7-task average) in just 102M tokens (4 GPU-hours, single H100) -- approaching Bi-Mamba's 48.4% (within +/-0.9pp CI). This QAT-from-pretrained setting reveals zero-ratio collapse, a novel instability caused by learnable quantization scales that does not arise in from-scratch training. We further show that post-hoc correction strategies effective for Transformers fail for SSMs due to error accumulation through the recurrence. These results demonstrate that ternary SSMs do not require expensive from-scratch training: QAT from pretrained checkpoints with KD is a data-efficient alternative.

---


### 183. [First Proof Second Batch](https://arxiv.org/abs/2606.18119)

**<font color=#1a73e8>作者：</font>** Mohammed Abouzaid, Nikhil Srivastava, Rachel Ward 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> To assess the ability of current AI systems to correctly solve research-level mathematics problems, we tested several AI systems on a set of ten problems in a broad range of mathematical fields; these problems arose naturally in the research process of the contributors. This document includes the problems, our methodology, and the results of our testing. We provide links to supplementary documents including the human solutions, the AI-generated solutions, and the referee reports and logs for the AI-generated solutions.
The ten problems were contributed by the following mathematicians: (1) Dariusz Kalociński and Theodore A. Slaman, (2) Richard Schwartz, (3) Aleksa Milojevic and Benny Sudakov, (4) Larry Guth, (5) Oleg Butkovsky, Jonathan Mattingly, and Lorenzo Zambotti, (6) Joshua Evan Greene and Duncan McCoy, (7) Sucharit Sarkar, (8) Sam Payne and Jidong (Jayden) Wang, (9) Sylvie Corteel and John Lentfer, (10) Srivatsav Kunnawalkam Elayavalli.

---


### 184. [On the Reliability of Networks of AI Agents: Density Evolution, Stopping Sets, and Architecture Optimization](https://arxiv.org/abs/2606.18121)

**<font color=#1a73e8>作者：</font>** Ehsan Aghazadeh, Hossein Pishro-Nik  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Modern AI systems increasingly solve a task not with a single model call but with several imperfect agents working together: some propose pieces of a solution, others verify them, and the results are combined. These systems often outperform any single model, yet it is rarely clear why they succeed or when they will fail. We model such a system as message passing on a sparse graph, the structure that underlies low-density parity-check (LDPC) codes, and extend the density-evolution machinery of coding theory to this richer setting. In our model a task is a set of coupled binary subclaims, and an agent architecture is a sparse, role-typed factor graph whose check nodes are noisy Boolean verifier nodes, each computing a local Boolean function of the subclaims it touches. Three distinct failure modes, all modeled as erasures (an agent abstaining, a verifier returning no usable output, and a message lost between two agents), propagate as the agents exchange set-valued messages. The check agents combine these messages by a single logical-forcing rule that specializes to XOR, AND, OR, implication, and Horn constraints. This is more than a relabeling of LDPC theory: the verifier functions are nonlinear and value-asymmetric, and the three failure modes do not reduce to a single effective channel, so they require new threshold, finite-length, and converse results rather than a direct reuse of parity-check density evolution. We prove a density-evolution theorem that predicts the asymptotic fraction of unresolved subclaims on random role-typed architectures, with an extension to deterministic, locally tree-like graph sequences. The XOR case recovers the classical LDPC recursion on the binary erasure channel (BEC); the AND case exposes an asymmetry between positive and negative verifier certificates.

---


### 185. [Embedded Machine Learning for Microcontroller-Class Edge Devices: Data, Feature, Evaluation, and Deployment Pipelines](https://arxiv.org/abs/2606.18122)

**<font color=#1a73e8>作者：</font>** Mostafa Darvishi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Embedded machine learning moves inference from cloud services to resource-constrained devices that must acquire data, preprocess signals, run a model, and act within tight limits on memory, energy, and latency. This paper presents a systems-oriented synthesis of an embedded machine-learning workflow for microcontroller-class platforms. The emphasis is placed on engineering decisions that are often hidden in generic machine-learning introductions: sampling and buffering, feature extraction as dimensionality reduction, validation under class imbalance, model/runtime co-design, and streaming deployment. Two representative signal families are used throughout the paper. The first is inertial motion recognition, where a two-second, three-axis accelerometer window is transformed from raw samples into root-mean-square and spectral features before classification. The second is keyword spotting, where audio is sampled, anti-aliased, transformed into mel-frequency cepstral coefficients, and processed by a compact one-dimensional convolutional network. The paper concludes with practical design rules for robust on-device inference, including data curation, quantization, thresholding, scheduling, and field monitoring.

---


### 186. [Knowledge Reutilization in Meta-Reinforcement Learning](https://arxiv.org/abs/2606.18132)

**<font color=#1a73e8>作者：</font>** Yuan Meng, Bo Wang, Juan de los Rios Ruiz 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Meta-reinforcement learning enables fast adaptation by extracting shared structure from related tasks, but existing end-to-end methods often couple task inference with embodiment-specific control. This coupling can obscure non-parametric task semantics, reduce sample efficiency, and limit cross-agent reuse. We propose a meta-knowledge reutilization framework that learns task-level knowledge on a dynamics-simplified agent and transfers it to heterogeneous agents. The framework uses a Bayesian non-parametric prior to organize latent task modes and a high-level policy to generate task-level magnitude guidance. To bridge reusable task knowledge with different embodiments, we introduce a semantic-magnitude interface and a lightweight temporal adaptor, which convert frozen meta-knowledge into temporally aligned subgoals for embodiment-specific low-level controllers. Experiments on multiple locomotion agents show that our framework reduces final-step tracking error by 94.75% -- 99.79% compared with recent state-of-the-art baselines and achieves comparable deployment performance with about 23.8% of their interaction data.

---


### 187. [Memory as a Wasting Asset: Pricing Flash Endurance for Embodied Agents, and the Limits of Doing So](https://arxiv.org/abs/2606.18144)

**<font color=#1a73e8>作者：</font>** Josef Liyanjun Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A robot's flash endurance is a non-renewable stock: every persisted write spends one of a few thousand program/erase cycles and never refills, yet no fielded robot memory system prices which memories are worth an erase cycle. We treat embodied memory as depreciating capital and price that stock with a single endurance shadow price $\eta$, which makes cost-minimizing placement across a RAM / on-board NVM / cloud hierarchy a threshold in a wear-augmented per-byte index. The index is cost-optimal whatever the sign of the value-write association $\chi$; only when $\chi > 0$ does the optimum turn non-monotone, sending a robot's most valuable memories off its flash.
The pivot is thus empirical, and we measure $\chi$ on real robot logs at a pre-specified gate: its sign is a property of the deployment regime -- positive on recurrent long-horizon manipulation ($\hat{\chi} \approx +1.0 \times 10^{-3}$, replicated at full power), null on a shorter-horizon suite, and negative on non-recurrent teleoperation. Two boundaries scope the result. The endurance budget is dormant on premium 3,000-P/E TLC at datasheet prices and binding on the commodity QLC/eMMC ($\sim$1,000 P/E) that cheaper edge robots run. And where it binds, a learned wear-aware controller only ties price-based routing on task value, because realized value is tier-invariant across RAM, NVM, and cloud: the rent governs device lifetime and cost, not task performance. Whether wear-aware placement improves task value remains open -- $\chi$ is measured against a value proxy, and the non-monotone optimum, while proven, is not yet observed in data.

---


### 188. [Neural Tree Reconstruction for the Open Forest Observatory](https://arxiv.org/abs/2606.18153)

**<font color=#1a73e8>作者：</font>** Marissa Ramirez de Chanlatte, Arjun Rewari, Trevor Darrell 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The Open Forest Observatory (OFO) is a collaboration across universities and other partners to make low-cost forest mapping accessible to ecologists, land managers, and the general public. The OFO is building both a database of geospatial forest data as well as open-source methods and tools for forest mapping by uncrewed aerial vehicle. Such data are useful for a variety of climate applications including prioritizing reforestation efforts, informing wildfire hazard reduction, and monitoring carbon sequestration. In the current iteration of the OFO's forest map database, 3D tree maps are created using classical structure-from-motion techniques. This approach is prone to artifacts, lacks detail, and has particular difficulty on the forest floor where the input data (overhead imagery) has limited visibility. These reconstruction errors can potentially propagate to the downstream scientific tasks (e.g. a wildfire simulation.) Advances in 3D reconstruction, including methods like Neural Radiance Fields (NeRF), produce higher quality results that are more robust to sparse views and support data-driven priors. We explore ways to incorporate NeRFs into the OFO dataset, outline future work to support even more state-of-the-art 3D vision models, and describe the importance of high-quality 3D reconstructions for forestry applications.

---


### 189. [ReAge3D: Re-Aging 3D Faces with View Consistency](https://arxiv.org/abs/2606.18156)

**<font color=#1a73e8>作者：</font>** Libing Zeng, Li Ma, Mingming He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a novel framework for realistic and controllable 3D face re-aging which produces highly detailed, identity-preserving results. Existing 3D editing methods, while effective for coarse semantic changes, are not well suited for re-aging, as even small inconsistencies across re-aged 2D views can lead to over-smoothing of subtle but perceptually important age-related details. To address this challenge, we first introduce a 2D diffusion-based re-aging model, DiffReaging, trained on synthetically generated image pairs. We further propose a center-out editing propagation strategy that leverages this re-aging model to reconstruct multi-view-consistent re-aged images. Specifically, starting from a re-aged frontal pivot view, we reconstruct the remaining views through warping and our proposed Masked-DiffReaging process. By injecting existing content at every step of the diffusion process, Masked-DiffReaging ensures that the reconstructed regions remain coherent with existing pixels. The resulting consistent set of re-aged views supervises the optimization of the re-aged 3D representation. Our method outperforms existing 3D editing techniques both visually and quantitatively, enabling smooth, fine-grained control over age transformations in 3D face models.

---


### 190. [Kolmogorov Regression for Robust Diffusion Policies](https://arxiv.org/abs/2606.18186)

**<font color=#1a73e8>作者：</font>** Lekan Molu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Finite-dimensional (FD) diffusion policies exhibit temporal drift owing to discretization artifacts that degrade long-horizon performance (when deployed on physical systems). We introduce a backward Kolmogorov equation that lifts diffusion policies to a Cameron-Martin space -- a subset of the Hilbert space. Essentially, replacing stochastic score matching with a deterministic boundary-value PDE problem. Our core innovation thrives on Gaussian measure theory whereupon the diffusion noise covariance operator is realized from a colored noise distribution which prescribes a notion of regularity on samples from the model at inference time. We train the diffusion model with a derived precision-weighted Cameron- Martin loss and a Kolmogorov residual is introduced as a PDE diagnostic during inference. These substitutions yield (i) convergence guarantees where the bound's constants depend on the effective rank of the kernel rather than action dimension, (ii) improved trajectory regularity via spectral weighting, and (iii) a deterministic failure detector without reward signals. Validation across two application domains demonstrates substantial improvements: on the PushT manipulation benchmark, the Cameron-Martin loss achieves a 17% improvement in maximum episode reward (0.95 vs. 0.78 for MSE) and 67.6% reduction in inter-step drifts during inference via the introduced residual magnitude. Similarly, on a 6-station manufacturing line with constant work-in-process (CONWIP) flow control, we achieve 28.4% lower RMSE than classical LSTM baselines; a high starvation-event recall (1.0 in test cycles), and effective bottleneck identification (Precision@1 = 1.0 in test set, 13x signal-to-noise ratio). We then certify the dispatch policies with Hamilton-Jacobi reachability theory which reduces deadlock events by 96% compared to uncontrolled dispatch over 100 simulated runs (351 events prevented).

---


### 191. [DRFLOW: A Deep Research Benchmark for Personalized Workflow Prediction](https://arxiv.org/abs/2606.18191)

**<font color=#1a73e8>作者：</font>** Md Tawkat Islam Khondaker, Raymond Li, Muhammad Abdul-Mageed 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep research (DR) systems are increasingly used for complex information-seeking tasks, but existing works mainly focus on generating reports and summaries. In contrast, many enterprise tasks instead require an agent to identify concrete workflows which is a sequence of action-steps. For example, rather than summarizing budgeting policies, an agent should be able to determine the steps needed to answer a question such as: "How do I request new headcount given a fixed budget?". Therefore, we introduce DRFLOW, a benchmark for evaluating personalized workflows predicted by agents from heterogeneous sources. Each task requires the agent to identify relevant evidence from scattered sources, then use that evidence to predict the correct action-step sequence for the user's task. DRFLOW contains 100 tasks across five domains, with 1,246 reference workflow steps grounded in more than 3,900 sources. We define seven diagnostic metrics covering factual grounding, step recovery, structural ordering, condition resolution, and personalization. We further present DRFLOW-Agent (DRFA), a workflow-oriented reference agent to predict personalized workflow. We show that although DRFA improves over strong baseline agents (upto 10.02% average F1 score), there is substantial room for improvement remains across these workflow metrics, indicating that predicting complete and correct personalized workflows remains a challenging frontier for deep research.

---


### 192. [The Stanford EDGAR Filings Dataset: Reconstructing U.S. Corporate and Financial Disclosures into Layout-Faithful and Token-Efficient Pretraining Data](https://arxiv.org/abs/2606.18192)

**<font color=#1a73e8>作者：</font>** Nick Bettencourt, Xiaowei Ding, Kay Giesecke  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As high-quality public web corpora become increasingly exhausted, clean long-context documents have become a scarce and expensive source of training data for large language models (LLMs). Existing long-context corpora are often proprietary and costly to acquire, synthetically generated, or concentrated in narrow domains such as programming. We introduce the Stanford EDGAR Filings Dataset (SEFD), an open reconstruction of SEC filings into layout-faithful MultiMarkdown for financial language modeling and evaluation. SEFD makes audited financial statements, risk disclosures, ownership reports, accounting notes, and market-moving event filings usable as long-context pretraining data and as a basis for financial reasoning, forecasting, compliance, and document understanding. The resulting corpus is token-efficient, model-ready, and has less than 0.1% overlap with Common Crawl-derived corpora. We release SEFD-v1, a 152B-token initial public snapshot, and provide corpus-level analyses of a larger 18.5M-filing archive estimated at 550B tokens. We further introduce two SEFD-derived benchmarks: EDGAR-Forecast, which evaluates filing-grounded numerical forecasting after model knowledge cutoffs, and EDGAR-OCR, which evaluates transcription of complex financial tables.

---


### 193. [A Red-Team Study of Anthropic Fable 5 & Opus 4.8 Models](https://arxiv.org/abs/2606.18193)

**<font color=#1a73e8>作者：</font>** Nicola Franco  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We evaluate the adversarial robustness of two frontier large language models (LLMs) developed by Anthropic, Fable 5 and Opus 4.8, against four families of automated jailbreak attack across 7 826 harmful intents spanning a ten-category harm taxonomy. Using the HackAgent red-teaming framework, hundreds of thousands of adversarial attempts were generated and every apparent success was independently re-adjudicated by a panel of three judge models (majority vote). Both models resist the majority of attacks, but the residual surface is larger than aggregate framing suggests: it is dominated by adaptive iterative attacks, while static obfuscation is near-fully neutralised. The strongest adaptive search (tree-of-attacks) breaks Opus 4.8 on 11.5% of intents overall, whereas Fable 5 stays in the single digits (6.1% worst-case). Aggregate rates therefore should not be read as reassurance. Even in these hardened configurations, the two models produced 1 620 (Opus 4.8) and 702 (Fable 5) panel-confirmed harmful completions spanning every harm category, located automatically, cheaply, and within the first one or two refinement steps by an attacker model with no human expert in the loop. The reasonable conclusion is that even the best, most-tested frontier models remain reliably breakable under sustained automated pressure.

---


### 194. [Analyzing and Encoding the Al-Mawrid Arabic-English Dictionary with the ISO Language Markup Framework and TEI Lex-0](https://arxiv.org/abs/2606.18205)

**<font color=#1a73e8>作者：</font>** Diaa Fayed, Laurent Romary  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents a robust methodology for the systematic digitization and encoding of the Al-Mawrid Arabic-English dictionary, transforming it from a legacy print resource into a standardized computational lexicon. Addressing a significant gap in Arabic lexical infrastructure, the study adopts a dual-standard framing that aligns the ISO Lexical Markup Framework (LMF) with the Text Encoding Initiative TEI Lex-0 guidelines. By applying an editorial view to the dictionary's macro- and microstructure, the research resolves the structural ambiguities and punctuation inconsistencies typical of 20th-century bilingual dictionaries. The methodology is grounded in an empirical analysis of the dictionary's lexical knowledge density. Drawing on a representative sample (the letter Ayn, comprising 4.6% of the total volume), the study provides scientific weight to the encoding process, demonstrating a structural parsing accuracy of 91%. Quantitative evaluation of the information extraction rules reveals high performance, with 85% precision and 98% recall for synonyms, and 88% precision for other morpho-semantic features. Beyond technical description, the paper provides a critical comparison with existing Arabic lexical resources and discusses the limitations of TEI Lex-0 when modelling specific Arabic phenomena, such as implicit "open set" semantic relations and scattered morphological cues. Furthermore, the study explores the potential for Linguistic Linked Open Data (LLOD) integration by establishing a scalable prefix-based referencing system that facilitates the resource's inclusion in the semantic web. The result is an interoperable, machine-tractable resource that provides a reproducible workflow for the retro-digitization of complex legacy bilingual lexicons within the Arabic NLP and Digital Humanities communities.

---


### 195. [Fixed-Point Reasoners: Stable and Adaptive Deep Looped Transformers](https://arxiv.org/abs/2606.18206)

**<font color=#1a73e8>作者：</font>** Sajad Movahedi, Vera Milovanović, Shlomo Libo Feigin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Looped architectures provide an inductive bias toward learning step-by-step procedures for tasks that require compositional reasoning. The number of effective layers reached by looping determines the quality of the solution these models find. Like deep architectures, looped architectures are prone to a signal propagation problem induced by depth as the halting decision is postponed. In this paper, we address this signal propagation issue using pre-norm layers and residual scaling. Building on these architectural modifications, we propose FPRM, a Transformer-based Fixed-Point Reasoning Model that uses fixed-point convergence as an end-to-end halting mechanism in a looped architecture. We show that fixed-point halting allows FPRM to adapt its compute to task difficulty. FPRM is effective on common reasoning benchmarks, namely Sudoku, Maze, state-tracking, and ARC-AGI.

---


### 196. [Rethinking Dataset Distillation for Classification: Do Distilled Sets Outperform Coresets?](https://arxiv.org/abs/2606.18209)

**<font color=#1a73e8>作者：</font>** Trisha Mittal, Akshay Mehra, Joshua Kimball  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dataset distillation (DD) has emerged as a prominent approach in data centric machine learning, aiming to synthesize compact training sets for efficient training by compressing the information in large datasets into a small number of synthetic samples. However, DD methods are often evaluated under inconsistent evaluation protocols, ranging from standard ERM to single/multi-teacher supervision, making it difficult to isolate the effectiveness of distilled data from evaluation. Moreover, many prior methods claim that DD outperforms data pruning approaches such as coreset selection (CS), based on the assumption that restricting condensed datasets to subsets of real samples fundamentally limits their expressiveness. In this work, we critically evaluate DD methods through large-scale experiments using standardized datasets and evaluation protocols to assess their intrinsic effectiveness. We benchmark seven state-of-the-art (SOTA) DD methods on ImageNet-1K, ImageNet100, and ImageNette, using three widely adopted training protocols against three CS strategies. Our results show that while some DD methods fail to outperform even simple random subsets, the SOTA DD approaches are comparable to or worse than coresets on large-scale datasets and incur a substantially higher cost for construction. Beyond accuracy, we also evaluate the representativeness, diversity, and quality of condensed sets, and find that coresets consistently achieve better coverage of the original data distribution. These findings highlight the limited practical advantages of current DD methods and show that coresets remain competitive and are often a more computationally efficient alternative for data-centric learning.

---


### 197. [Gatling: Rapid-Fire Consensus from Parallel Composition](https://arxiv.org/abs/2606.18220)

**<font color=#1a73e8>作者：</font>** Giulia Scaffino, Max Resnick, Joachim Neu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Consensus protocols form the core of blockchains and other replicated state machines, ensuring that all correct nodes process the same totally ordered log of input transactions. In fault-free executions, performance is driven by the good-case transaction latency -- the time between a transaction becoming known to all nodes and its confirmation by the consensus protocol -- which depends on both how frequently proposals are made and, once made, how quickly they are confirmed. While prior work has established tight lower bounds on confirmation latency that modern protocols already achieve, it remains open whether the inter-proposal time can be further reduced below the state-of-the-art of one network delay.
We introduce Gatling, an atomic broadcast protocol that achieves arbitrarily small inter-proposal times under rotating leader schedules; in particular, smaller than the network delay. Gatling runs multiple parallel instances of a black-box atomic broadcast protocol and staggers their proposal schedules to generate proposals in faster succession than state-of-the-art protocols. A deterministic interleaving rule merges the outputs of these instances into a single global log. We analyze the effects of head-of-line blocking caused by crashed leaders, and derive Gatling's optimal number of parallel instances. We further study the impact of Gatling on predictable validity and present two variants that retain this property. Finally, our experiments confirm that Gatling can be used with off-the-shelf component protocols to achieve low latency without fine-tuning the component protocol for minimum latency.

---


### 198. [Darshana Graph: A Parallel Commentary Corpus for Comparative Indian Philosophy, with Stylometric and Exploratory Graph Analyses](https://arxiv.org/abs/2606.18222)

**<font color=#1a73e8>作者：</font>** Joy Bose  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Darshana Graph, a corpus of over 125,000 text records spanning classical Hindu, Buddhist, and Jain philosophical traditions, drawn from public-domain and openly licensed translations of sources including the Bhagavad Gita, Brahma Sutras, principal Upanishads, the Pali Canon, and core Jain texts. Its distinctive contribution lies in a structurally unique subset of roughly 8,500 Hindu and Jain records in which the same root verse or sutra is aligned across eighteen historical commentators representing five schools of Vedanta and other darshanas, enabling direct comparison of how independent interpretive traditions read identical source material. To our knowledge, no publicly available resource provides comparable cross-commentator alignment at this scale. We present two analyses built on this corpus. First, a transparent stylometric comparison requiring no machine learning measures argumentative style through scriptural citation density, explicit refutation rate, and sentence complexity. It finds a moderate negative correlation between citation density and refutation rate, a marked increase in refutation rate across three commentators in a related doctrinal lineage, and measurable genre-level differences within the Pali Canon itself. Second, we describe a constrained large language model pipeline that extracts typed philosophical relationships between concepts using a predefined relation vocabulary and deterministic post-hoc validation. The resulting graph surfaces cross-school disagreement patterns while also revealing important extraction limitations, including cases where an independent embedding-based analysis disagrees with the graph-derived findings. We release the full corpus, extracted relationship graph, and all source code.

---


### 199. [Learning Red Agent Policy from Observations for Neurosymbolic Autonomous Cyber Agents](https://arxiv.org/abs/2606.18223)

**<font color=#1a73e8>作者：</font>** Ankita Samaddar, Sandeep Neema, Daniel Balasubramanian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With sophisticated cyber-attacks becoming increasingly prevalent, modern networks require intelligent autonomous cyber-defense agents trained via Reinforcement Learning (RL). These agents employ neurosymbolic approaches such as behavior trees with learning-enabled components (LECs) to learn, reason, adapt, and implement security rules while maintaining critical operations. However, these autonomous networks are partially observable systems, i.e., the cyber-attacker's (red agent's) actions are not observable, making it difficult for the defender to predict red actions, learn red policies, or assess the attacker's intrusion levels. To address this, we propose a Policy Learning Technique using imitation learning to learn policies for partially observable RL agents with discrete states and discrete actions. We apply this technique in an autonomous cyber environment to predict red agent's actions from network observations and defender actions. Integrated with a neurosymbolic cyber-defense agent, our method effectively handles different red policies and achieves high prediction accuracy across diverse simulated scenarios.

---


### 200. [Adaptive Volumetric Mechanical Property Fields Invariant to Resolution](https://arxiv.org/abs/2606.18231)

**<font color=#1a73e8>作者：</font>** Rishit Dagli, Donglai Xiang, Vismay Modi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate mechanical properties (or materials) Young's modulus ($E$), Poisson's ratio ($\nu$) and density ($\rho$) are essential for reliable physics simulation of digital worlds, but most 3D assets lack this information. We propose AdaVoMP, a method for predicting accurate dense spatially-varying ($E$, $\nu$, $\rho$) for input 3D objects across representations, improving the resolution, accuracy, and memory efficiency over the state-of-the-art. The foundation of our technique is a sparse and adaptive voxel structure SAV that efficiently represents both the input 3D shape and the material field output. We replace the fixed-voxel model of the most accurate prior method, VoMP, with a novel sparse transformer encoder-decoder model that learns to generate a unique SAV autoregressively for every input shape to represent its materials, achieving a resolution $16^3\times$ higher than prior art. Experiments show that AdaVoMP estimates more accurate volumetric properties, even with lesser test-time compute than all prior art. This allows us to convert high-resolution complex 3D objects into simulation-ready assets, resulting in realistic deformable simulations.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-205](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
