# 📦 其他研究 | 2026年08月26日

> 本类共 **361** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-361](./part-08.md)

---

### 251. [SiZeUp: Fast 3D Proxy from Aerial Images via Depth Ordinal Loss](https://arxiv.org/abs/2608.22821)

**<font color=#1a73e8>作者：</font>** Wenjun Zhou, Yunshan Li, Qiaoyu Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present SiZeUp, a fast and scalable approach for constructing large-scale 3D urban proxy models directly from calibrated oblique aerial imagery. Our method adopts a height-from-footprint representation, reducing 3D building abstraction to a low-dimensional optimization problem in which building footprints are extruded by a single height parameter. To enable efficient and robust height estimation, we introduce an ordinal depth consistency loss that enforces agreement between the relative depth ordering of rendered proxies and depth priors predicted by a monocular depth model. This is realized through a differentiable renderer that maps parametric building proxies into multi-view depth images, allowing gradients to be propagated from depth supervision to building heights. Our ordinal formulation produces stable optimization in practice and avoids explicit feature matching or dense point cloud reconstruction. Rather than relying on metric depth, which can be unreliable under monocular scale ambiguity, our ordinal depth consistency loss operates on relative depths, providing a more reliable signal across views. Combined with an efficient dynamic view selection, our approach achieves a 23-52$\times$ speedup over state-of-the-art proxy reconstruction pipelines while maintaining comparable proxy-level coverage and volume consistency, making it well suited for large-scale urban modeling tasks.

---


### 252. [DIME: Query-Efficient Framework for Membership Inference on Diffusion Models](https://arxiv.org/abs/2608.22824)

**<font color=#1a73e8>作者：</font>** Tue Do, Daniel Alabi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Membership inference attacks expose whether individual records were used to train a model, yet existing attacks on diffusion models are largely heuristic and can require substantial query budgets. We introduce DIME (Denoiser Ideal Membership Error), a theoretically grounded and query-efficient framework for membership inference on diffusion models. Our starting point is an exact characterization of the optimal diffusion denoiser for a finite training set, which reveals that membership leakage is governed by the denoiser's implicit reconstruction error. This error decomposes into two complementary signals: a bias term, capturing reconstruction accuracy, and a previously unexplored local crowding term, capturing the geometry of nearby training examples. Both admit efficient estimators using only model queries, yielding a practical attack with as few as two queries. Across CIFAR-10/100, STL10-U, CelebA, and ImageNet, DIME consistently outperforms prior attacks at comparable or substantially lower query cost, improving TPR at 1% FPR by up to $3\times$; remarkably, its two-query variant can outperform existing 30-query baselines. Finally, we suggest, discuss, and evaluate specific defenses to counteract such powerful membership tests.

---


### 253. [VeCAS: Vessel-Focused Contrast-Free Angiogram Synthesis for Vascular Interventions](https://arxiv.org/abs/2608.22828)

**<font color=#1a73e8>作者：</font>** De-Xing Huang, Chen-Yu Wang, Hao Liang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> X-ray angiography relies on iodinated contrast agents to visualize vascular structures during image-guided interventions. However, contrast administration carries risks of adverse events, motivating the development of contrast-free alternatives. Generating X-ray angiograms directly from non-contrast X-ray images offers a potential solution, but existing approaches remain limited by (i) insufficient control over vascular localization and (ii) inefficient modeling of redundant background content. To address these challenges, we propose VeCAS, a two-stage vessel-focused contrast-free angiogram synthesis framework that separates vascular structure localization from angiographic appearance synthesis. In Stage I, a discriminative model localizes vascular structures in non-contrast X-ray images, while cross-modality latent distillation transfers vessel-sensitive knowledge from X-ray angiograms during training. In Stage II, a vessel-focused inpainting model synthesizes angiographic appearance within the localized vascular regions while preserving the non-vascular background. Experiments on an in-house lower-limb vascular intervention dataset show that VeCAS outperforms the comparison methods in terms of vascular structural fidelity and image quality. Visual Turing tests and physician assessments indicate the perceptual realism of the synthesized angiograms. In addition, robotic guidewire navigation experiments in vascular phantoms show that VeCAS guidance reduces the time to target by 41.4% and the number of operation steps by 40.7% compared with non-contrast guidance. Together, these results suggest the potential of VeCAS to serve as ``meta contrast agent'' for vascular interventions.

---


### 254. [Let the Bullets Fly: Multimodal Fake News Detection with Temporal-Aligned Generative Danmaku](https://arxiv.org/abs/2608.22832)

**<font color=#1a73e8>作者：</font>** Xiansheng Luo, Chaowei Zhang, Zewei Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The social interactions among crowds via \textit{Danmaku} (a.k.a., bullet comments) on modern multimedia platforms can facilitate both viewpoint conflicts and consensus, providing fine-grained discriminative social signals that can benefit fake news detection. However, the inherent accumulation latency of \textit{Danmaku} in real-world scenarios violates the real-time necessity of fake news detection, making the studies of \textit{Danmaku}-related fake news detection underexplored. To break this violation, we simulate this temporal-aware user interactive process by proposing a novel temporal \textbf{Gen}erative \textbf{da}nmaku framework, called \textbf{Genda}, which consists of: (1) a \textit{Danmaku} Trigger for predicting the timing and intensity of user reactions; and (2) a \textit{Danmaku} Generator for synthesizing corresponding semantic and emotional expressions, thereby mutually constructing a temporally aligned and human-like pseudo \textit{Danmaku} streams. To make the generated \textit{Danmaku} useful for identifying fake news videos, we further design a \textit{Danmaku}-guided Temporal Multimodal fake news detection model - \textbf{DM-FEND}, which enables fine-grained multimodal interactions among video, audio, text, and \textit{Danmaku}, enhancing dynamic modalities alignment and semantic noise inhibition. The experimental results demonstrate that \emph{DM-FEND} consistently outperforms state-of-the-art baselines across both Chinese (FakeSV) and English (FakeTT) benchmarks. Further ablations validate the crucial role of temporal \textit{Danmaku} modeling in enhancing robustness and discriminative capability. Finally, this study offers a bright and robust solution for multimodal fake news detection in modern social interactive fashions by bridging the temporal inconsistency between news and user behaviors.

---


### 255. [Mapping the Concept Landscape: Structural Perception of Global Distributions for Transparent Data Pruning](https://arxiv.org/abs/2608.22858)

**<font color=#1a73e8>作者：</font>** Dongyue Wu, Tao Ma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing data pruning methods predominantly rely on high-dimensional feature embeddings to measure sample importance. However, these compressed vectors often obscure fine-grained semantic interactions, leading to suboptimal coverage of rare semantic concepts in the pruned subsets. In this paper, we propose Mapping the Concept Landscape (MCL), a novel structural perception framework for transparent data pruning. Instead of abstract embeddings, we represent each image-caption pair as an explicit sample-level graph comprising entities, events, and attributes. By integrating these individual graphs into a comprehensive dataset-level graph, we characterize the global distribution of semantic concepts and quantify their rarity across the entire corpus. Based on this structured perception, we develop a greedy concept-coverage maximization algorithm that iteratively selects samples to maximize the marginal gain of high-value, under-represented concepts. Experimental results on various benchmarks demonstrate that our method not only achieves superior pruning efficiency compared to state-of-the-art methods but also provides a transparent and interpretable audit trail for the selection process.

---


### 256. [Following Motion for Sequential Modeling in Video Frame Interpolation](https://arxiv.org/abs/2608.22861)

**<font color=#1a73e8>作者：</font>** Jaehyun Park, Nam Ik Cho  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> State Space Models (SSMs) have surfaced as a promising architecture in Video Frame Interpolation (VFI), as they can capture long-range dependencies with linear computational complexity. However, their predefined scanning order limits their effectiveness in modeling the dynamic motion trajectories inherent in VFI problems. To tackle this challenge, we propose Motion-Guided Mamba for Video Frame Interpolation (MGMVFI), an adaptation of the selective state space model tailored explicitly for VFI. MGMVFI introduces Motion-Guided Serialization (MGS), which leverages optical flow to define a motion-adaptive 1D input order for the SSM. This aligns the causal state updates with semantically related tokens, enabling motion-consistent feature propagation, particularly for large and dynamic motions. Additionally, to mitigate the unreliable feature representations caused by inaccurate optical flow estimates, we introduce contextual synthesis that utilizes the surrounding spatial context for robust inter-frame feature synthesis. These components are seamlessly integrated within our tailored Mamba architecture, which also employs a lightweight refinement block to enhance local detail reconstruction at a reduced computational cost. Extensive experiments on standard VFI benchmarks demonstrate that MGMVFI achievesstate-of-the-artperformance,particularly on complex and dynamic motions, thereby establishing a new direction for sequence modeling in video interpolation.

---


### 257. [Toward Sub-1 kB Identity-Preserving Face Compression: A Benchmark of Codecs, a Custom Learned Codec, and Studies of Resolution, Demographic Fairness, Recompression, and Adversarial Robustness](https://arxiv.org/abs/2608.22866)

**<font color=#1a73e8>作者：</font>** Petr Hurtik, Jakub Sochor  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Storing face images under a hard sub-kilobyte budget, as required for identity documents, smart-card biometrics and bandwidth-constrained verification, forces a codec to discard most of the signal while keeping what a face matcher actually reads: identity. Generic codecs optimize pixel fidelity, not the embedding distances that drive verification, so which codec, resolution and setting best preserve identity at 1024 bytes or less, and how that degrades at 512, is unclear.
We benchmark ten general and face-specific codecs across resolutions, byte budgets, two datasets (controlled Color FERET, in-the-wild AI-Solutions-KK) and four anchor face matchers, with a fourteen-model ViT and CNN roster confirming the ranking is backbone-invariant. We then train a custom identity-preserving codec that hits the byte budget exactly via binary search over a frozen gain table, and run four studies: resolution, demographic fairness, recompression, and no-box adversarial robustness.
Sub-kilobyte identity preservation is feasible, but which codec to deploy depends entirely on the budget. At 1024 bytes and the 112 px working resolution the problem is close to solved: modern codecs hold Color FERET equal-error rate under 0.35 percent on the ArcFace anchor. At 512 bytes the field re-sorts: AVIF, HEIF, JPEG XL and legacy JPEG collapse to 28 to 98 percent false-non-match rate at FMR 1e-4, while WebP, JPEG-AI and our byte-budgeted learned codecs stay out of that band, with 24.3 percent for WebP against 6.9 percent for our accurate variant in the wild. That re-sort, not the 1024-byte ranking, is the operational result: a codec chosen at 1 kB is not the codec to deploy at half that.

---


### 258. [Stochastic Separability of Embedding Manifolds](https://arxiv.org/abs/2608.22874)

**<font color=#1a73e8>作者：</font>** Liqing Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neurobiological studies and representation learning have observed that representations of objects belonging to the same category in high-dimensional neural spaces exhibit low-dimensional object manifold characteristics, and different object manifolds are linearly separable in these neural spaces. However, these experimentally observed phenomena lack rigorous theoretical validation to date.
This paper proposes a new stochastic separability theorem for embedding manifolds of two different object categories. First, we establish a projection measure concentration theorem for embedding manifolds under general conditions. We develop a new two-layer measure concentration analysis technique, which unifies two estimation bounds via the law of total expectation to derive measure concentration inequalities.
Based on the measure concentration theorem, we further prove a stochastic separability theorem for embedding manifolds of two different object categories. If two datasets have distinct means and bounded total variances, their samples become linearly separable with high probability, provided that the projection direction satisfies a non-singularity condition.
The main contributions of this paper are twofold:
1. We prove the projection concentration properties of embedding manifolds in high-dimensional spaces by using two-lawyer tail-bound inequalities.
2. We identify a non-singularity condition for the stochastic separability between embedding manifolds, and rigorously prove the stochastic projection separability theorem.
The theorem not only uncovers geometric and statistical properties of the object embedding manifolds, but also provides a novel mechanism for representation learning in deep networks.

---


### 259. [Large-Small Model Collaboration for Zero-Shot Surgical Phase Recognition](https://arxiv.org/abs/2608.22879)

**<font color=#1a73e8>作者：</font>** Yiyi Zhang, Ying Zheng, Wenxin Fan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Task-specific lightweight models for surgical phase recognition excel at capturing temporal dynamics but generalize poorly under domain shift. Conversely, surgical foundation models (FMs) offer superior transferability via large-scale pretraining, yet their lack of explicit temporal modeling often yields temporally inconsistent predictions, leading to degraded performance. To exploit the complementary strengths of both paradigms, we propose \textbf{La}rge-\textbf{S}mall \textbf{T}emporal adaptation (\textbf{LaST}), a novel large-small collaborative framework that enables zero-shot adaptation to unseen clinical domains. In LaST, the FM initiates the pipeline by generating frame-level phase priors that serve as initial weak supervision. To effectively utilize these noisy phase priors, we introduce an iterative temporal refinement scheme that integrates dynamic quality control to filter reliable predictions and dual-model cross-learning to mitigate confirmation bias. Simultaneously, the lightweight model leverages its intrinsic temporal modeling ability to progressively correct inconsistent predictions and enhance overall accuracy across iterations. At the end, a cycle replay strategy is employed to close the loop: the refined, more accurate predictions are utilized as upgraded supervision signals for the subsequent iterations, fostering a self-reinforcing evolution of both label quality and model capability. Extensive experiments demonstrate that LaST achieves robust adaptation to unseen domains for zero-shot surgical phase recognition, outperforming the baseline (PeskaVLP) by 24.85\%-43.17\% in accuracy and even surpassing fully supervised linear probing and several state-of-the-art few-shot approaches. Codes will be released at this https URL.

---


### 260. [NemoSplat: Feed-Forward 4D Gaussian Splatting for Media-Aware Underwater Reconstruction](https://arxiv.org/abs/2608.22888)

**<font color=#1a73e8>作者：</font>** Xiaopeng Guo, Wai Chung Tse, Yipeng Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing photorealistic scenes in unconstrained underwater environments remains challenging due to severe media-induced light scattering and unpredictable dynamic objects. Recent feed-forward visual foundation models have demonstrated remarkable capabilities in generalized novel view synthesis and tracking. However, when directly applied to aquatic videos, optical attenuation and motion interference fatally corrupt their feature aggregation, leading to severe tracking and reconstruction failures. To overcome these limitations, we present NemoSplat, the first feed-forward 4D Gaussian Splatting framework tailored for media-aware dynamic reconstruction directly from uncalibrated marine videos. Beyond providing robust estimations of camera poses and dense scene depth, we devise a Promptable Dynamic Disentangler that utilizes a confidence-aware fusion strategy of learned dynamic probabilities and optional semantic text priors, effectively isolating massive transient entities. Furthermore, to counteract visual degradation, a Media-Aware Gaussian Predictor is formulated to jointly estimate intrinsic 3D Gaussian attributes alongside physical media parameters, rendering pristine scene appearance in a single forward pass. Additionally, we introduce a large-scale underwater dataset with massive dynamic elements to facilitate training and evaluation. Extensive experiments on our dataset demonstrate that NemoSplat achieves state-of-the-art tracking accuracy and high-fidelity rendering.

---


### 261. [CDEG: Learning Decision-Critical Evidence for Long-Horizon Diagnostic Agents](https://arxiv.org/abs/2608.22899)

**<font color=#1a73e8>作者：</font>** Xiwei Dai, Zijie Meng, Zhiting Fan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Unlike static medical question answering, long-horizon diagnosis captures the sequential nature of clinical practice: evidence is progressively acquired, integrated, and evaluated over multiple rounds of interaction before reaching a final diagnosis. However, existing doctor agents often fail when critical evidence is either not acquired or not adequately incorporated into diagnostic reasoning. Recent agentic approaches attempt to address these failures by reusing historical trajectories or distilled memories. But their diagnostic gains remain constrained because such experience may contain noisy or incidental information and is typically reused without validating which evidence actually drives diagnostic decisions. To address this limitation, we introduce CDEG, a graph-based framework that learns reusable decision-critical evidence from historical diagnostic trajectories. CDEG contrasts successful and failed trajectories from the same case to identify candidate evidence, validates their diagnostic impact through controlled counterfactual interventions, and organizes the resulting diagnosis--evidence--action relations into a structured graph. During inference, CDEG tracks the evolving patient evidence state to retrieve relevant diagnostic relations and selectively guide missing evidence acquisition or overlooked evidence reappraisal. Across in-domain and out-of-distribution benchmarks with multiple doctor agent backbones, CDEG consistently improves diagnostic performance, achieving up to an 11.5% accuracy gain over vanilla agents. These results demonstrate that reliable long-horizon diagnosis requires moving beyond trajectory-level experience reuse toward evidence-level learning of the factors that truly shape clinical decisions.

---


### 262. [Black Box Cryptanalysis of AES128](https://arxiv.org/abs/2608.22904)

**<font color=#1a73e8>作者：</font>** Virendra Sule, Kunal Telangi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper presents computational results of cryptanalysis of AES using the Local Inversion by Black Box computations of the forward encryption and utilizes these results to develop a practically feasible approach for the key recovery of the full scale AES128 under Known Plaintext Attack (KPA). It is shown that complete recovery of unknown key bits is possible upto $80$ bits in a practically feasible time and memory in random KPA situation by sequential computation when remaining $48$ bits are known. The results of key recovery in $64$, $72$ and $80$ bit unknown cases are extrapolated to predict the period of the iterative sequence generated in the local inversion approach for the full $128$ bit unknown key case and a strategy is proposed to search the actual period by brute force parallel search of the sequence period with $10$ free bits defining the search space. Then it is shown that the actual key can be verified in polynomial time by fast powering of the forward encryption map. Hence this strategy shows that the key recovery problem for AES128 under KPA has a high chance of success in practically feasible time. Local inversion approach to cryptanalysis using black box computations is a universal method applicable to a vast variety of key recovery and map inversion problems. Hence the results presented in this paper are representative of estimates of cryptanalysis of other ciphers which can be considered almost as strong as AES128 as encryption functions.

---


### 263. [AquaFlow: A Monocular Gaussian Splatting SLAM for Underwater Streaming Reconstruction](https://arxiv.org/abs/2608.22906)

**<font color=#1a73e8>作者：</font>** Yingxiang Xu, Kerui Ren, Wenqi Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent monocular 3D Gaussian Splatting (3DGS) streaming reconstruction methods have achieved impressive performance by balancing reconstruction quality and efficiency. However, extending these frameworks to underwater scenes remains challenging due to severe visual degradation, such as light attenuation and scattering, which degrades camera pose tracking and distorts scene geometry. To address these challenges, we propose AquaFlow, a monocular Gaussian Splatting streaming reconstruction framework for efficient and high-fidelity underwater reconstruction. Specifically, AquaFlow fine-tunes a 3D vision foundation model on large-scale underwater data for robust pose and pointmap estimation, and introduces a medium-guided incremental Gaussian initialization strategy for streaming mapping. Furthermore, we develop a streaming-compatible hybrid scene representation that integrates structured, distance-conditioned neural Gaussians with a physics-inspired optical model to compensate for underwater image formation effects, enabling accurate scene reconstruction. We evaluate AquaFlow on a comprehensive dataset of 62 diverse underwater trajectories, collected from both public benchmarks and in-the-wild web videos across various scales. Extensive experiments demonstrate that AquaFlow achieves state-of-the-art tracking and rendering performance, reducing average localization error by 13.2% and improving PSNR by 4.74 dB compared to WaterSplat-SLAM.

---


### 264. [Exploring Dowker Homology for Sentence Similarity](https://arxiv.org/abs/2608.22909)

**<font color=#1a73e8>作者：</font>** Marius Huber, Juri Opitz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dowker homology is a topological tool that may be used to analyze the relative position of two point clouds living in a common space. We investigate whether Dowker homology captures sentence similarity information by treating the embeddings of the tokens that constitute a sentence pair as a pair of point clouds in the latent space of a transformer model, using both models that have and have not been fine-tuned for sentence similarity. We find that Dowker homology captures sentence similarity information, as measured by regressing Dowker homology features onto ground-truth similarity scores, and that it can be used for visual inspection of similarity data and models. In an attempt to make Dowker homology readily applicable, we derive from it single-number summaries that we expect to capture sentence similarity directly. These turn out to work reasonably well, but without outperforming standard sentence similarity measures based on established pooling methods.

---


### 265. [Results of the 1st Asynchronous CASTLE Challenge at the Joint Egocentric Vision Workshop in Conjunction with CVPR 2026](https://arxiv.org/abs/2608.22914)

**<font color=#1a73e8>作者：</font>** Luca Rossetto, Werner Bailer, Cathal Gurrin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This report summarizes the contributions and results of the 1st Asynchronous CASTLE Challenge at the Joint Egocentric Vision Workshop in conjunction with CVPR 2026.

---


### 266. [Beyond Observed Auxiliary Relations: Environment-Conditioned Modeling for Multi-Behavior Recommendation](https://arxiv.org/abs/2608.22920)

**<font color=#1a73e8>作者：</font>** Seunghan Lee, Hyunsik Yoo, Jian Kang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-behavior recommendation (MBR) leverages auxiliary behavioral signals, such as clicks and add-to-cart, to enhance target behavior prediction like purchases. While recent graph neural network-based approaches have achieved strong performance by systematically propagating auxiliary behavior signals, they still suffer from two fundamental challenges inherent to auxiliary behaviors: (1) missing auxiliary signals, which hinder generalization to items without auxiliary observations, and (2) unreliable auxiliary signals, which amplify noise misaligned with the target behavior. To address these challenges in a unified manner, we propose BOAR, an environment-conditioned MBR framework that addresses missing and unreliable auxiliary signals through two complementary modules conditioned on auxiliary observability. Extensive experiments demonstrate that BOAR consistently outperforms state-of-the-art baselines, achieving up to 7.82% gains in HR@10 overall and up to 44.2% gains for target items without auxiliary observations, highlighting its ability to capture hidden preferences beyond observed auxiliary relations. Our code is available at: this https URL.

---


### 267. [Cryptocurrencies in the Quantum Age: Migration Paths to PQC](https://arxiv.org/abs/2608.22924)

**<font color=#1a73e8>作者：</font>** Aleksei Kodukhov  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Quantum computers pose a fundamental threat to blockchain systems that rely on elliptic-curve cryptography. This work reviews the quantum vulnerabilities and associated economic risks of major blockchain platforms, with a focus on Bitcoin, Ethereum, and Solana. We distinguish between at-rest, on-spend, and on-setup attacks and identify the blockchain components most exposed to quantum adversaries. We further review practical migration strategies toward post-quantum security, including NIST-standardized digital signatures and emerging solutions for Solana, Algorand, and Ethereum.

---


### 268. [Quality Inspection of Printed Circuit Board Pin Insertion via Semantic Segmentation and Board-Level Feature Extraction](https://arxiv.org/abs/2608.22937)

**<font color=#1a73e8>作者：</font>** Nils Rabeneck, André Kiunke, Nicole Hoess 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Quality control during printed circuit board (PCB) assembly is a critical step in ensuring reliable electronic products. Detecting misaligned pins during or after pin insertion remains a particularly challenging inspection task. This paper presents an automated defect detection method for identifying incorrectly inserted pins on PCBs. The proposed pipeline combines semantic segmentation using a U-Net architecture with contour-based feature extraction and logistic regression for board-level pass/fail classification. Segmentation masks are used to derive contour representations of individual pins, from which board-level features -such as average contour size- are extracted and used to train a logistic regression classifier. We evaluate the method on two datasets: an industrial collection of real-world PCB images, and a publicly available PCB pin-inspection dataset with substantially different visual characteristics. To assess the effectiveness of the proposed approach, a comparison against PatchCore, an anomaly detection technique new to be applied to pin inspection, as well as instance segmentation-based pin detection is made. The developed method achieved Area Under the Receiver Operating Characteristic Curve (ROC-AUC) values of 0.990 on a random test set split from the industrial data and 1.000 on the public dataset indicating strong separation between pass and fail boards. The results indicate that the proposed approach is a promising candidate for automated pin inspection in industrial environments and achieves strong performance on datasets with substantially different visual characteristics after dataset-specific training.

---


### 269. [What's Your NIC Whispering? Network Threat Behavior Recognition via NIC Electromagnetic Side-Channel Leakage](https://arxiv.org/abs/2608.22941)

**<font color=#1a73e8>作者：</font>** Hongchao Wang, Linrui Li, Yunkai Zou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Conventional network threat detection primarily relies on packet-level, flow-level, or host-level telemetry. This paper investigates a different observation surface: unintended electromagnetic(EM) emissions generated by network interface card(NIC) activity, and asks whether such physical leakage contains sufficiently structured information for network threat-behavior recognition. We present NICWhisper, which externally captures NIC EM emissions, transforms raw measurements into time-frequency representations, and recognizes network behaviors without inspecting packet contents or host-side runtime states. Rather than competing with traffic-based detection, NICWhisper exploits the physical manifestation of traffic-driven NIC activity, whose timing, rate, concurrency, and burst organization naturally shape the measured EM leakage. We construct a NIC EM dataset covering active benign workloads and seven representative threat behaviors under diverse execution conditions, and systematically evaluate signal dependence, execution variation, measurement perturbation, and cross-device transfer. NICWhisper achieves 80.67\% Macro-F1 across eight behavior classes, while further experiments show that the observed behavior-related information extends beyond simple signal magnitude and remains partially transferable across execution conditions and NIC hardware. These results establish NIC EM leakage as a complementary physical observation source for network security monitoring when direct access to conventional traffic or host telemetry is limited or undesirable.

---


### 270. [A Momentum-Based Variance-Reduced Algorithm for Federated Multiobjective Optimization](https://arxiv.org/abs/2608.22945)

**<font color=#1a73e8>作者：</font>** Yong Zhao, Chunlin You, Minh N. Dao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning has traditionally been formulated as a single-objective optimization problem, primarily focused on maximizing model utility. In real-world applications, however, machine learning models often need to optimize multiple and potentially conflicting objectives simultaneously. This motivates federated multiobjective optimization (FMOO), which provides a natural framework for jointly handling multiple task-specific objectives in federated learning. In this paper, we propose a momentum-based variance-reduced algorithm for federated multiobjective optimization. The method incorporates a momentum-driven gradient estimator into the local updates to reduce the variance of stochastic updates, leading to an improved convergence rate. We establish theoretical guarantees showing that the expected Pareto stationarity measure of a randomly selected output iterate decays at a rate of $\mathcal{O}(T^{-2/3})$, improving upon the $\mathcal{O}(T^{-1/2})$ rates established for existing methods such as FSMGDA and FedCMOO. Numerical experiments on federated multiobjective optimization benchmarks demonstrate the effectiveness and competitive performance of the proposed algorithm.

---


### 271. [Stochastic gradient descent with initial regularization](https://arxiv.org/abs/2608.22953)

**<font color=#1a73e8>作者：</font>** Nabil Kahalé  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We analyze a variant of stochastic gradient descent with initial regularization (SGDIR) and derive dimension-free upper bounds on its expected excess risk for the squared loss. In the noiseless case, we obtain new bounds for both averaged and non-averaged SGDIR under moment, source, and capacity assumptions. For a particular value of the source parameter, these bounds are of order $m^{-2}\log^{2}m$, where the number of training samples is of order $m$. For another value of the source parameter, we obtain, for any $\epsilon>0$, bounds of order $m^{-3+\epsilon}$, provided that the capacity parameter exceeds $\epsilon^{-1}$. We also establish a lower bound that matches our upper bounds in certain regimes up to a polylogarithmic factor. In the noisy case, we provide an instance-based comparison between SGDIR and ridge regression. Under general assumptions and a mild lower bound on the regularization parameter, we show that the expected excess risk of SGDIR is no larger than that of ridge regression, up to a polylogarithmic factor. Numerical experiments on synthetic and real data are consistent with our theoretical findings.

---


### 272. [Rational Dolev--Yao Attackers: Decidable Incentive-Aware Verification of Security Protocols in Strategic Logic](https://arxiv.org/abs/2608.22954)

**<font color=#1a73e8>作者：</font>** Ioana Boureanu, R. Ramanujam  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Symbolic protocol verification models the network attacker as a Dolev--Yao (DY) intruder, which does everything its knowledge permits, whether or not it serves any purpose; real adversaries instead maximise utility, attacking only when the payoff is positive. We introduce a rational Dolev--Yao attacker, a DY intruder whose actions carry costs and whose security-violating goals carry rewards, and call a protocol rationally secure when no intruder strategy achieves a violation with strictly positive utility, expressed in a weighted fragment of ATL (WATL). We prove this decidable for a bounded rational DY intruder over a finite cost-annotated concurrent game structure, characterise its complexity, and show it strictly refines DY security: some protocols are DY-insecure yet rationally secure, separated by a computable threshold. We illustrate the framework on two contrasting use-cases: an authenticated payment under session uncertainty, where a rational intruder must strategise across indistinguishable sessions and its imperfect information strictly raises the attack cost a designer must price against; and ThreeBallot, a cryptography-free scheme where we pinpoint the bribe-to-benefit ratio below which no rational coercer attacks.

---


### 273. [The Illusion of Control: Why Bare Classifier Inversion Silently Fails in Concept-Bottleneck Text Generation](https://arxiv.org/abs/2608.22956)

**<font color=#1a73e8>作者：</font>** Qi Bing, Xiaowei Shao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Concept-bottleneck controllable generation routes multi-attribute control through a low-dimensional concept code that, at deployment, must be synthesised from a target attribute configuration. We study this problem in concept-bottleneck text generation under multi-axis compositional generalisation, comparing three ways to obtain the inference-time code: classifier inversion against the encoder heads, reference-text encoding, and a post-hoc label-conditioned prior. Since a concept code admits no direct LM-fluency term, regularising inversion must instead constrain the code toward the encoder's training distribution. We therefore test bare inversion and three regularised variants: label-agnostic and label-conditioned Mahalanobis penalties, and a conditional normalising-flow density baseline. Every inversion variant we test underperforms a simple post-hoc prior fitted to per-combination encoder means on the same checkpoints, across three backbone families spanning $124$M to $8$B parameters. The bare form of classifier inversion also silently collapses to chance, traceable to a directly measured off-manifold code. We validate this diagnosis on real-world benchmarks and under external evaluators, enabling fair comparison with published baselines.

---


### 274. [Simplified Cross-Modal Calibration for Heterogeneous Event-RGB Stereo Systems](https://arxiv.org/abs/2608.22965)

**<font color=#1a73e8>作者：</font>** Nico Hessenthaler, Adam T. Müller, Nicolaj C. Stache  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate extrinsic calibration between event-based and frame-based cameras remains a practical bottleneck for heterogeneous stereo systems. Existing approaches often require sensor or target motion, precise synchronization, or computationally expensive event-to-image reconstruction. We propose a simple, motion-free cross-modal calibration framework that uses a temporally modulated, blended ChArUco target presented on standard consumer displays. By alternating between the original pattern and a partially blended version, the target reliably triggers events while remaining continuously observable to a frame-based camera, avoiding blank frames and reducing synchronization constraints to a coarse, trigger-based alignment. We discretize events into frames coarsely aligned with the RGB images, apply lightweight denoising, and perform ChArUco-based intrinsic and stereo extrinsic calibration. Extensive experiments assess robustness to blending opacity, display brightness, external illumination, viewing angle, and handheld acquisition. Compared to the strongest motion-based reference (E2Calib + Kalibr) and a non-motion-based reference (Plasberg et al.), our approach reduces the mean reprojection error by $44\%$ and $6\%$, respectively, while substantially simplifying the calibration procedure. Finally, we demonstrate practical utility in a robotic eye-to-hand calibration case study, showing consistent transformations and stable downstream geometric measurements even under partial occlusions. Code is publicly available at this https URL.

---


### 275. [Budget-Constrained Embodied Perception: Four Resource Walls and a Pre-Registered Evaluation of Access-Structured Perception on Open Models at less than 31B](https://arxiv.org/abs/2608.22975)

**<font color=#1a73e8>作者：</font>** Defu Lin, Wenhui Chen, Ziyao Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Embodied multimodal agents must answer from growing observation streams under a fixed per-decision token budget. We formalize this constraint through four resource walls: a perceptual Shannon wall for bounded state, a horizon wall for query-independent frame selection, a round wall for non-adaptive retrieval, and a conditional composition wall for fixed-depth inference. We introduce ASP, a training-free wrapper for frozen multimodal models that combines a capped structured state, a verbatim episodic index, and query-conditioned budget allocation with iterative access. Following a pre-registered protocol, we evaluate seven open-weight models from 3B to 31B on SEW-Bench, a license-free synthetic long-horizon walkthrough benchmark constructed to instantiate these walls. The registered natural-video benchmarks were not run because their frames require dataset agreements; our evidence therefore concerns access mechanisms, not natural-scene perception. Under a 4,096-token decision budget, ASP reaches 75 to 94% episodic retrieval accuracy, compared with 3 to 19% for equal-budget query-independent sampling, and budget reallocation outperforms quadrupling the sampling budget on every backbone. However, the full three-component architecture does not validate channel duality: removing the compressive state raises the flagship mean from 35.4 to 58.0, ASP does not outperform the verbatim-only baseline on any backbone, and two of four pre-registered falsification criteria fire. These results show that query-conditioned access, rather than parameter count or context growth alone, is decisive under a fixed budget, while prompted online compression does not earn its cost in this setting.

---


### 276. [SA-RSQ: A Versatile Sparse Representation Framework for Multi-modal Recommender Systems](https://arxiv.org/abs/2608.22979)

**<font color=#1a73e8>作者：</font>** Xiang Wang, Shigang Quan, Tingzhen Chang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deploying high-dimensional multimodal features in industrial recommender systems incurs substantial storage and latency overhead. Hard quantization is compact but introduces boundary distortion, whereas dense soft quantization couples representation quality to the limited storage budget. We propose Sparse Activation-based Residual Soft Quantization (SA-RSQ), which uses Top-K sparse routing and softmax weights to store compact (Index, Probability) tuples. The stored tuples decouple per-item storage from codebook dimensionality; for a fixed selected support, gradients propagate through the routing weights and weighted reconstruction without relying on a straight-through estimator. Experiments on a proprietary food-delivery advertising dataset show favorable reconstruction-performance and CTR trade-offs across storage budgets of 8-48 bytes per item. A preliminary Next-Distribution Prediction study and a one-week online A/B test further demonstrate the practical potential of SA-RSQ, with relative lifts of +2.51% in CTR and +3.66% in CPM.

---


### 277. [Hierarchy-Aware Semantic Losses for Knowledge Graph Link Prediction](https://arxiv.org/abs/2608.22981)

**<font color=#1a73e8>作者：</font>** Filip Kronström, Ross D. King  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge graphs are often accompanied by ontological class hierarchies that encode valuable semantic information, yet many link prediction methods either ignore such hierarchies or incorporate them indirectly through additional graph edges. Recent work introduced hierarchy-aware graph neural networks (GNNs), which use semantic losses derived from box embeddings to encourage satisfaction of subclass relationships during GNN-based representation learning. While this approach has shown promise for biological regression tasks, its effectiveness for knowledge graph link prediction has not been investigated.
In this paper we evaluate hierarchy-aware semantic losses on link prediction across three benchmark datasets: AIFB, CoDEx, and BioKG. We combine graph neural network encoders with box-embedding-based semantic losses that encourage learned representations to better satisfy ontology-derived class hierarchies, and compare this approach to both standard link prediction models and models incorporating subclass relations as graph edges. Across all datasets, hierarchy-aware semantic losses significantly improve mean reciprocal rank (MRR) and consistently outperform models that incorporate hierarchy information through additional subclass edges. Relative to the baseline GNN models, MRR improved by 7.6%, 2.4%, and 15.5% on AIFB, CoDEx, and BioKG, respectively. Furthermore, semantic losses consistently outperform the alternative of augmenting the graph with subclass edges.
These results are consistent with ontology-derived class hierarchies providing complementary information to graph structure, and suggest that encouraging hierarchical consistency through semantic losses is an effective and comparatively parameter-efficient mechanism for improving knowledge graph link prediction.

---


### 278. [What Does Activation Steering Control? Attribution Across Answer Encodings and Output-Sensitive Subspaces](https://arxiv.org/abs/2608.22985)

**<font color=#1a73e8>作者：</font>** Zhiwei Gao, Shaowen Peng, Shoko Wakamiya 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Activation steering is often evaluated under the answer encoding used to construct the direction. A reported gain may reflect the intended judgment or compatibility with answer identifiers seen during construction. We introduce Cross-Encoding Steering Evaluation, which freezes an intervention while re-encoding answers to the same held-out items. On NormBank, after A/B/C identifiers are reassigned, contrastive activation addition (CAA) induces larger target-versus-source score changes for the extraction indices than for the semantic labels under the new mapping. We call this extraction-index following. Varying identifier vocabulary (A/B/C, X/Y/Z, or 1/2/3) and row order shows that the effect tracks extraction index rather than row position. After matching direction norms across layers, extraction-index following emerges mainly at later depths. A low-rank output-sensitive component containing 15.4% of the direction's squared norm retains 96.3% of this effect. An Inference-Time Intervention (ITI)-style method also favors extraction-index over semantic-label following on NormBank in three models. In aggregate, MNLI favors extraction-index following, whereas Social Chemistry 101 (SC101) favors semantic-label following. Multiple-choice and open-ended evaluations can yield different behavioral conclusions. Thus, a steering gain under one answer encoding does not by itself identify what the intervention controls.

---


### 279. [The Anonymity Gap: Understanding Real Privacy in Shielded UTXO-based Protocols for DeFi](https://arxiv.org/abs/2608.22987)

**<font color=#1a73e8>作者：</font>** Hanze Guo, Stefanos Chaliasos, Yebo Feng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Shielded UTXO-based protocols are becoming a core form of privacy infrastructure for DeFi. Unlike mixers that organize privacy mainly around deposits and withdrawals, these protocols allow assets, once inside the shielded pool, to continue moving and being re-spent within the hidden state, and to become public only when users withdraw or interact with public DeFi protocols. Their anonymity is therefore no longer a flat pool-size problem, but a provenance problem that propagates across the note/UTXO, proof, and transaction layers. Yet, a unified analysis framework for this setting is still missing. We propose a layered system model and an analysis pipeline that uses prior history as the temporal baseline, applies cumulative pruning and cross-proof propagation to each proof's Commitment Set, and recursively traces the survivors through historical hidden-state transitions to derive the final transaction-level Anonymity Set Size.
We evaluate our methodology on the complete on-chain histories of all four Railgun production deployments and five independent Hinkal pools across six EVM chains, analyzing 186,356 unshielding spend transactions. Using only public protocol traces and constraints, our non-heuristic analysis yields mean Anonymity Set Size reductions of 40.1%-59.0% relative to each deployment's temporal baseline; 3,679 transactions retain at most 10 addresses, including 1,228 singletons. Public token constraints are the strongest and most stable source of pruning in both protocols, while the effects of tree number, proof roots, and value constraints vary with protocol design and historical state. Together with representative cases, these results reveal interpretable anonymity-loss patterns and implications for user behavior and future protocol design.

---


### 280. [PatchWrite: One Line, Not One Section -- Compile-Gated, Validity-Preserving Editing for AI-Drafted Manuscripts](https://arxiv.org/abs/2608.23001)

**<font color=#1a73e8>作者：</font>** Weiwei Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated manuscript pipelines often regenerate an entire section to repair a local defect, allowing unrelated metrics and citations to change even when the resulting PDF still builds. PatchWrite instead constrains how candidate edits become committed manuscript states: it reuses bounded EDIT N M editing and rollback, but tightens compilation acceptance with fatal-log checks and adds evidence locks that require every cited key and experimental numeric token to be attested by a reference registry or experimental log. Candidates that fail either check are rejected and the previous HEAD is retained. On a 24-manuscript x 8-fault oracle stress test (768 jobs, evenly split between compile-breaking and content-only faults), whole-slot rewriting mutated an unrelated "12-layer" line in every case (0/192 preserved; numeric Jaccard 0.6667), whereas PatchWrite preserved it in 192/192 cases. Removing the compile gate reduced acceptance to 0, while removing the evidence gate allowed a hallucinated citation to pass. The same pattern held across all eight faults. To test the protocol with generation rather than oracle edits, we reran the 192 jobs with the writer model proposing the edits. The model's candidates were accepted in 75% of cases; nearly all rejections came from one reproducible failure mode in which the model attempted to delete a line using an empty replacement unsupported by the current grammar. Every accepted candidate passed both gates, and 93.75% fixed the injected fault; the remaining cases involved a technically valid but sentence-inappropriate citation and one markup-changing near-miss. In a blind evaluation of sixteen PDF pairs, both raters preferred PatchWrite for preserving lab-grounded facts (C1 Likert 5.0 vs. 2.0), while rating prose quality nearly identically. Logs from 193 in-product drafting tasks show the same classes of failures occurring in practice.

---


### 281. [Misanthrope: A Privacy-Preserving Keypoint Detector](https://arxiv.org/abs/2608.23012)

**<font color=#1a73e8>作者：</font>** Francesco Vultaggio, Predrag Djindjic, Markus Gerke 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image matching is a core component of applications such as Simultaneous Localization and Mapping (SLAM), Visual Localization, and Structure from Motion (SfM). However, the local image features central to this task are vulnerable to inversion attacks, which enable adversaries to reconstruct privacy-sensitive scene content from local features. These attacks pose a particular threat in distributed computing scenarios where the pre-computed features leave edge devices to be processed by remote servers. In this work, we introduce Misanthrope, a novel privacy-preserving keypoint detector trained through self-distillation to avoid detecting keypoints on people---a predominant source of privacy-sensitive content in most localization scenarios---thus mitigating inversion attacks at the source rather than through post-hoc obfuscation. We demonstrate how inverted images from traditional feature detection pipelines can be used to detect and re-identify people in the scene, while Misanthrope is able to mitigate these attacks. Furthermore, Misanthrope maintains image matching performance on par with the state of the art and even surpasses it in challenging settings where people act as distractors, such as phototourism and in-the-wild odometry. On the Image Matching Challenge 2021 Phototourism test set, Misanthrope is the top-performing sparse feature extractor in 7 out of 9 scenes. We make our model and its evaluation script available here: this https URL

---


### 282. [AnaDiffusion: Anatomically CompositionalLatent Diffusion for Controllable 3D Brain MRI Generation](https://arxiv.org/abs/2608.23014)

**<font color=#1a73e8>作者：</font>** Huiwen Han, Lulin Liu, Bangya Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D brain MRI generation has made significant advances in medical imaging, simulation, and controllable anatomical analysis. However, existing generative models typically synthesize 3D volumes monolithically, often overlooking regional anatomical structures and limiting local controllability. To address these limitations, we introduce AnaDiffusion, an anatomically compositional latent diffusion framework that factorizes the generation process into distinct, anatomically meaningful regions, followed by part-to-whole assembly and global refinement. Our approach first trains part diffusion models to capture local structural priors. We then inject an assembled anatomical composite of the parts into the whole-brain latent representation and continue denoising. This mechanism enables the model to resolve global context while preserving the injected anatomy. As a result, AnaDiffusion produces both explicit part assets and a globally coherent volume, thereby enabling controllable part editing without requiring subject-specific dense segmentation maps at inference time while maintaining consistent part-to-whole brain structure. On the subject-disjoint ADNI test split, AnaDiffusion achieves the lowest FID across the whole brain, left and right hemispheres, cerebellar-brainstem complex, and seam regions. It also achieves the best cerebellar and second-best ventricular and brainstem absolute Cohen's d values among the evaluated methods. In localized editing experiments, paired MS-SSIM demonstrates high target transfer and off-target preservation, supporting controllable part replacement with minimal unintended anatomical alterations.

---


### 283. [When the Edit Changes the Patient: Measuring Identity Preservation in Counterfactual Retinal Images](https://arxiv.org/abs/2608.23024)

**<font color=#1a73e8>作者：</font>** Andrea Posada, Wenke Karbole, Bach Ngoc Doan 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Counterfactual medical image generation aims to modify an existing image to reflect a hypothetical scenario in which certain characteristics of the imaged subject are altered, while keeping their identity fixed. Most existing works repurpose established image editing methods, which do not directly supervise identity preservation. Instead, they assume that identity is implicitly preserved by anchoring generation to the source image. This assumption is rarely tested and may fail in domains where biometric cues are subtle, such as retinal optical coherence tomography (OCT). In this work, we explicitly measure identity preservation for three groups of text-conditioned editing methods - source-anchored, structured-prompt, and paired-training - using referee classifiers, embedding alignment scores, and a blind reader study. We find that all methods produce high-quality OCT images with comparable editing success, yet their identity preservation differs markedly. Source-anchored editing frequently alters the depicted subject, while paired-training preserves it best. We argue that future work on medical counterfactual generation must explicitly measure and report identity preservation alongside image realism and editing success.

---


### 284. [Artificial Empathy: Towards a Framework for Unsupervised Agency Detection and Policy Reconstruction](https://arxiv.org/abs/2608.23030)

**<font color=#1a73e8>作者：</font>** Peter Kuhn, Chris Pang, Sonakshi Chauhan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study how an AI system can identify and model other agents in its environment from observation alone, which is a capability necessary for cooperative behaviour in the real world. This problem is less constrained than inverse reinforcement learning and remains largely unexplored. We propose a framework that uses a reinforcement learning agent, trained on an independent task as a prior about agentic dynamics, to perform agency detection and policy reconstruction.

---


### 285. [FedCC: Towards Addressing Label Distribution Skews in Distillation-Based Federated Learning](https://arxiv.org/abs/2608.23031)

**<font color=#1a73e8>作者：</font>** Wenxuan Ye, Onur Ayan, Xueli An 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) enables distributed clients to collaboratively train models without sharing raw data, making it promising for leveraging massive devices in communication networks. In distillation-based FL, each client applies its local model on an unlabeled public dataset, and shares only prediction results with the server. While heterogeneous local data introduces label distribution skew, thus biasing client models toward majority classes and leading to potentially inaccurate predictions. The lack of ground-truth labels in the public dataset hampers the server's ability to calibrate predictions, which ultimately degrades overall performance. To address this, we propose FedCC, a simple and effective algorithm for mitigating client misclassification. Instead of being forced to classify and risking error propagation, clients are allowed to tag ambiguous samples as 'unknown'. This additional class, together with calibrated pseudo-labels on the public data, balances confidence in majority classes against uncertainty in under-represented ones. Extensive experiments demonstrate that FedCC significantly outperforms existing methods, especially under severe label skew. In the extreme scenario where each client holds samples from only one of ten classes, FedCC achieves 67.3% accuracy, while baselines collapse to near-random results.

---


### 286. [The Multilingual FrameNet Corpus](https://arxiv.org/abs/2608.23037)

**<font color=#1a73e8>作者：</font>** Beatrice Fiumanò, Nicolas Lazzari, Simone Paolo Ponzetto 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper introduces the Multilingual FrameNet Corpus (mFNC), a novel resource that extends the English Berkeley FrameNet corpus by collecting and harmonizing existing language-specific corpora across nine additional languages: Brazilian Portuguese, Chinese, Dutch, French, German, Italian, Korean, Latvian and Swedish. By training models that rely on different architectures on the mFNC, we consistently outperform existing state-of-the-art Frame Semantic Parsers in both multilingual and cross-lingual settings, underscoring the importance of multilingual training data. The mFNC and our trained FSP models are openly available at this https URL.

---


### 287. [Graph Representation Learning of Lightweight IoT Ciphers](https://arxiv.org/abs/2608.23054)

**<font color=#1a73e8>作者：</font>** Jonathan Cook, Sabih ur Rehman, M. Arif Khan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> SIMON and SIMECK belong to a family of Lightweight Cryptographic Algorithms (LCAs) based on the Feistel block cipher, designed for Internet of Things (IoT) devices. As with all Feistel ciphers, they are susceptible to differential cryptanalysis, necessitating rigorous resilience evaluations. While state-of-the-art techniques leverage heuristics and sampling to improve efficiency, little work has applied Machine Learning (ML) guided Graph Representation Learning (GRL) to efficiently identify and visualise high-probability differential clusters. We address this gap by introducing an efficient feature engineering strategy that extracts four differential attributes from a partial Difference Distribution Table (pDDT), revealing structural information concealed in raw differential data. Utilising the enriched features, we construct and compare three ML-guided directed graphs for SIMON$32$ and SIMECK$32$ using K-Nearest Neighbour (KNN), Decision Trees (DT), and Random Forests (RF). To the best of our knowledge, our framework produces the first graph-based visualisation of the differential clustering effect, in which high-probability single-bit differentials form geometrically close clusters in the learned embedding. All three models achieve a precision of $1.0$ in identifying high-probability differentials, confirming zero false positives. KNN achieves the strongest cluster separation, the highest F1 score and the lowest graph construction time of approximately $2.3$ seconds, while DT and RF produce optimal paths with near-perfect regression. The results are consistent across both LCAs, demonstrating the applicability of the framework to other AND-rotation LCA families.

---


### 288. [Macro-Action Topological Navigation under Noisy Localization using Reinforcement Learning](https://arxiv.org/abs/2608.23055)

**<font color=#1a73e8>作者：</font>** Simon Hakenes, Tobias Glasmachers  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Navigating large, photorealistic 3D apartments from raw pixels is widely considered infeasible for plain reinforcement learning. We build an agent that does it anyway, estimating its own pose from the camera alone. The agent has to reach several target objects in sequence, and their positions change between episodes, so it must explore to find them. It builds on our earlier object-centric topological controller, which still read the agent's true pose and its object detections from the simulator. Here we replace that true pose with an onboard, object-centric estimate. For each object we keep a bank of ORB features that, when the object is seen again, yield a rough pose measurement, which a minimal Extended Kalman Filter (EKF) fuses with a motion model. As on a real robot, the executed motions are noisy. The estimate drifts, but the agent and the nearby objects drift together, so a locally consistent pose is enough to follow each short edge and then home in visually on the target, which lets us replace full SLAM with a much smaller model, closer to how biological navigation appears to work. In the photorealistic Habitat simulator, the agent reaches its target objects from vision alone, with a pose that only needs to be locally consistent.

---


### 289. [From Generation to Simulation: How Far Are World Models from Being True Simulators?](https://arxiv.org/abs/2608.23070)

**<font color=#1a73e8>作者：</font>** Tong Wang, Huan Deng, Mucheng Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With the rapid progress of diffusion models and large-scale video generation, generative world models are increasingly expected to replace traditional simulators, including physics engines, game engines, and reinforcement-learning environments. Yet the remaining distance from generation to simulation lacks a systematic assessment. We present a capability-based study using an external yardstick: eight capabilities of a traditional simulator, namely asset construction, physics engine, interaction, controllability, stability, state feedback, diversity, and evaluation metrics. We trace three main technical routes--latent dynamics, video generation, and joint-embedding prediction--and map exactly 200 representative works published from 2018 to June 2026 onto these capabilities. Our analysis shows that world models have achieved functional substitution in interaction and controllability for specific scenarios, but remain short of traditional simulators in formal guarantees of physical laws, structured state feedback, and reproducible long-horizon evolution. State feedback is the most neglected cross-route shortcoming: only 6 of 163 implementation papers expose a runtime interface for querying entity states or physical parameters. We identify six research directions: formalized physics, a unified action interface, first-class state feedback, long-horizon stability, downstream-utility evaluation, and cross-route hybridization. Project page: this https URL

---


### 290. [Loopy: Seamless Video Loop Generation via Anchored Looping Shift of Positional Embedding](https://arxiv.org/abs/2608.23090)

**<font color=#1a73e8>作者：</font>** Haotian Dong, Wenjing Wang, Chen Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Looping videos are essential for practical applications such as web graphics, game development, and social media. However, existing approaches typically fail to generate high-quality looping videos due to the neglect of how video generation models perceive temporal order and how this relates to the looping behavior. In this work, we are the first to reveal that position embedding at different attention layers within DiT exhibits varying levels of positional control, with the most pronounced layer acting as an anchor. We formulate this anchored layer as the reference point of the looping video, offering strong contextual priors for the remaining layers to facilitate the generation of seamless and coherent video content. Based on this insight, we propose an anchored position embedding shifting strategy that applies layer-specific shift lengths according to each layer's temporal control effect, effectively transforming DiT's temporal perception from a straight line to a circle. Leveraging this strategy, we develop a general framework, Loopy, for high-quality looping video generation, supporting both RGB and RGBA videos, while also enabling advanced AIGC features such as identity control and style transfer. Experiments demonstrate that our approach significantly improves temporal consistency and visual fidelity in generated looping videos. The released model is available on our website: this https URL.

---


### 291. [Jiuge-Tuiqiao: An Interpretable Human-AI System for Classical Chinese Poetry Refinement](https://arxiv.org/abs/2608.23098)

**<font color=#1a73e8>作者：</font>** Yufeng Han, Lifan Deng, Cunliang Kong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Classical Chinese poetry composition has long valued Tuiqiao, the iterative refinement of words, imagery, and prosody. However, many current AI poetry systems follow a one-shot generation paradigm, which reduces users to prompt providers and weakens their creative agency. We present Jiuge-Tuiqiao, an interactive human-AI collaborative system for classical Chinese poetry composition. The system is designed around a triadic model: user-driven control, ancient-guided evidence, and AI-assisted generation. Users can lock characters or lines, receive real-time prosody feedback, and obtain interpretable refinement suggestions grounded in high-frequency collocations, PPL-ranked classical lines, and structured knowledge extracted from classical encyclopedias. This design turns AI from an autonomous generator into a background assistant that supports the user's own process of poetic refinement. Preliminary experiments and user feedback suggest that Jiuge-Tuiqiao improves controllability, interpretability, and user engagement in classical poetry composition.

---


### 292. [PolyChirp: Multi-Species Birdsong Classification Using TinyML on Low-Power Acoustic Sensors](https://arxiv.org/abs/2608.23101)

**<font color=#1a73e8>作者：</font>** Nathan Duboisset, Zhaolan Huang, Felix Bießmann 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent progress in the field of TinyML has demonstrated that low-power hardware based on microcontrollers can achieve bird species monitoring in real time based on acoustic sensor data for an entire breeding period on a single battery charge. However, the state of the art on low-power microcontrollers was so far limited to binary classification of a single species. In contrast, real fauna monitoring deployments often target multiple species simultaneously. To address this challenge we develop PolyChirp, an approach combining biological domain expertise, automated dataset curation, neural architecture optimization and novel hardware to achieve multiclass bird species detection in the wild. PolyChirp is based on newly designed tiny multiclass models that leverage recent microcontrollers and hardware acceleration with a neural processing unit (NPU). We evaluate the predictive performance of these models, and we measure their computational performance -- memory footprint, latency, energy consumption -- on common microcontroller hardware. Our results demonstrate that PolyChirp not only outperforms state-of-the-art on single species binary classification, but also achieves robust classification of up to 10 species simultaneously, while still fitting with the resource envelope of a sensor that must remain operational in the field for a full season on a single battery charge.

---


### 293. [DeMixPert: Decomposed Response Modeling with Gaussian Mixtures for OOD Single-Cell Perturbation Prediction](https://arxiv.org/abs/2608.23114)

**<font color=#1a73e8>作者：</font>** Jiawen Liu, Xuechenxiao Cao, Yutong Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting transcriptome-wide responses to unseen genetic perturbations remains a major computational challenge because accurate prediction requires recovering both perturbation-specific transcriptional shifts and heterogeneous cellular responses. Existing methods often entangle deterministic response structure with stochastic population-level variation, causing dominant shared patterns to mask weaker perturbation-specific signals and impair distributional modeling. To address these challenges, we propose \textbf{DeMixPert}, an approach for Decomposed response Modeling with Gaussian Mixtures for Out-Of-Distribution (OOD) single-cell Perturbation prediction. DeMixPert decomposes perturbation-induced changes into a basal-state-dependent systematic response, a perturbation-specific response, and population-level variation. The systematic component is derived from the basal state encoded from control-cell expression, whereas the perturbation-specific component is inferred from pretrained target embeddings for unseen-target generalization. DeMixPert models population-level variation using a Gaussian prototype Invertible Network and adaptively combines reusable Gaussian prototypes according to the basal state and perturbation condition. The resulting mixture is mapped to a condition-specific variation distribution. Sampled variations are integrated with the systematic and perturbation-specific components, followed by joint decoding with the basal state to reconstruct perturbed-cell gene expression. Experimental results show that DeMixPert effectively captures heterogeneous single-cell perturbation responses and achieves superior performance across unseen-perturbation settings. The source code is made publicly available upon publication.

---


### 294. [Statistical Machine Translation Systems of English-Pnar Language Pair : Some Insights of the Emperical Study](https://arxiv.org/abs/2608.23120)

**<font color=#1a73e8>作者：</font>** Edawanbiang Dhar Surmila Thokchom, Thoudam Doren Singh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pnar, an Austroasiatic language spoken by approximately 0.4 million people in the Jaintia Hills of Meghalaya, lacks the digital corpora and natural language processing (NLP) resources. This paper presents the first machine translation study for the English and Pnar language pair. Using articles collected from the Wyrta newspaper, we built a parallel corpus comprising of 10,234 sentences and trained phrase-based statistical machine translation (SMT) systems the models using 9,563 parallel corpora under three configurations for each direction using Moses, GIZA++ , KenLM, varying lexicalized reordering and minimum error rate training (MERT) tuning. The models are evaluated on a held out test set of 371 sentences, the best performing system achieves a BLEU score of 14.97 (chrF2: 33.42, TER: 77.60) for Pnar to English and 11.16 (chrF2: 31.38, TER: 93.51) for English to Pnar, establishing the first quantitative benchmark for this language pair. Lexicalized reordering improves translation quality by 3.73 BLEU points for Pnar to English, reflecting the structural shift from the source language's SOV word order to the target language's SVO order, whereas MERT tuning degrades BLEU performance under low resource conditions. Finally, we analyze the remaining translation errors, including morphological out of vocabulary (OOV) words, long-distance reordering and Khasi code mixing and discuss future directions toward neural and multilingual machine translation for Pnar.

---


### 295. [LITERARYBIGFIVE: Author-Personalized Text Generation in a Unified Interpretable Space](https://arxiv.org/abs/2608.23124)

**<font color=#1a73e8>作者：</font>** Jinghui Zhang, Lang Gao, Ao Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Personalized text generation for authors and literary writing is essential for applications such as adaptive writing assistants, creative support tools, and computational literary analysis. However, existing approaches to author modeling and personalization often represent writing behavior as independent labels, requiring large-scale corpus collection or fine-tuning for each author or stylistic category. Such formulations are costly, difficult to interpret, and poorly suited for generalizing across authors. Inspired by the Big Five model's dimensional view of personality, we propose LiteraryBigFive, a framework that reframes authorial writing characteristics as coordinates within a unified and interpretable space. In this space, we derive each interpretable axis (e.g., Classicism, Emotionality) from activation-space contrasts between author-written and neutral passages, yielding distinct stylistic dimensions that allow texts or authors to be positioned within a five-dimensional system. Beyond localizing different authors, we further introduce an interpretable steering mechanism, which adaptively guides text generation toward target coordinates to perform author-personalized writing. Experimental results show that LiteraryBigFive improves authorial expressiveness while preserving semantic fidelity. The derived author per-axis scores strongly correlate with real-world literary consensus, offering transparent and interpretable explanations of author-specific generation behavior: this https URL.

---


### 296. [MIVIFI: Bridging Perspective and Fisheye Domains for Training Multi-View Fisheye Image Generation Models](https://arxiv.org/abs/2608.23140)

**<font color=#1a73e8>作者：</font>** Matthias Neuwirth-Trapp, Begüm Altunbas, Jiayi Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Achieving 360° coverage is critical for the visual perception systems of autonomous vehicles. Fisheye cameras offer a cost-effective solution by enabling full surround coverage with as few as two sensors. However, existing multi-view fisheye datasets are limited, and synthesizing rare corner cases typically requires computationally expensive 3D simulations, hindering the training. While generative models have achieved significant success in standard perspective imagery, their application to wide-angle distortion remains unexplored. In this work, we formally introduce the novel problem of multi-view fisheye image generation conditioned on volumetric semantic representations and present two distinct methods. We first propose SyntheOcc-FE, which adapts the SyntheOcc architecture to fisheye data. While effective, this method is constrained by the scarcity of fisheye datasets, which limits its generalization. To overcome these limitations, we propose our second method, MIVIFI (multi-view fisheye), which leverages cross-domain learning with Equirectangular Projections. By bridging the gap between dataset domains using KITTI-360 fisheye images alongside nuScenes multi-view standard images, our approach enables high-fidelity manipulation of scene content. This framework enables the structural modification of semantic occupancy inputs to introduce or eliminate specific actors and facilitates the rendering of diverse meteorological conditions and illumination scenarios absent in the limited fisheye datasets. Quantitative and qualitative experiments demonstrate that our methods achieve robust photorealistic multi-view fisheye image generation and highlight the specific advantages of our cross-domain strategy for handling data scarcity.

---


### 297. [How Merge-Tolerant Are Vision Transformers for Wheat Phenotyping?](https://arxiv.org/abs/2608.23142)

**<font color=#1a73e8>作者：</font>** Simon Ravé, Pejman Rasti, David Rousseau  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-based wheat phenotyping requires repeated measurements under deployment constraints, from growth-stage recognition to wheat-head counting and organ segmentation. Plain Vision Transformers (ViTs) provide a common architecture for these tasks, but quadratic attention limits high-throughput and edge inference. Training-free token merging is attractive because it can be inserted into trained models without retraining. We provide a systematic benchmark of ToMe and Mutual Pair Merging across growth-stage classification, wheat-head detection, and wheat-organ segmentation, measuring task quality, throughput, token count, and peak GPU memory, with additional Raspberry Pi 5 measurements. The benchmark reveals a clear hierarchy: classification is highly merge-tolerant, while detection and segmentation are constrained by repeated instances, thin organs, dense boundaries, reconstruction, and runtime overhead. Optimized attention backends can erase apparent speedups, so deployment value must be profiled on the target runtime rather than inferred from token count.

---


### 298. [Conformal Risk Minimization for Semi-Supervised Domain Adaptation via Optimal Transport](https://arxiv.org/abs/2608.23153)

**<font color=#1a73e8>作者：</font>** Manos Giannopoulos, Yi Shen, Michael M. Zavlanos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In high-stakes healthcare applications, machine learning models are frequently trained on data from one patient population and deployed on another, creating a distribution shift that degrades both accuracy and reliability. Semi-Supervised Domain Adaptation (SSDA) addresses this by leveraging labeled data from some source domain to improve model performance on a target domain where labels are scarce. However, existing SSDA methods optimize primarily for point-prediction accuracy and offer no principled uncertainty quantification --- a prerequisite for clinical trust. Conformal Prediction (CP) can address this limitation by providing prediction sets with rigorous, distribution-free coverage guarantees. However, applying CP post-hoc to a pre-trained model can yield prohibitively large prediction sets, as SSDA pre-training methods do not account for the nonconformity score geometry that determines conformal set size. Conformal Risk Minimization (CRM) has been used to resolve this issue in the fully supervised setting by integrating the CP objective directly into model training, but it requires a large labeled dataset to compute nonconformity thresholds during training, precisely the data that is scarce in the SSDA regime. We propose an end-to-end framework that integrates CRM into the SSDA training objective, enabling effective CRM in the limited-labeled-target-data regime. The key idea is to utilize Optimal Transport (OT) to generate pseudolabels for unlabeled target instances, providing the additional training signal needed by CRM to operate using only a small labeled target set. This results in a model jointly optimized for domain invariance and conformal efficiency, producing prediction sets that are compact, coverage-valid, and support domain-specific constraints such as excluding mutually contradictory diagnoses in skin lesion classification.

---


### 299. [When More Modalities Hurt: Modality Dropout for Heavy-Duty Vehicle Engine Diagnostics](https://arxiv.org/abs/2608.23161)

**<font color=#1a73e8>作者：</font>** Adeel Zafar, Slawomir Nowaczyk, Hamid Sarmadi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Heavy-duty vehicle diagnostics generate three disconnected data modalities: unstructured multi- lingual service complaints, high-dimensional sensor telemetry with over 80% missing values, and Diagnostic Trouble Codes (DTCs). We investigate whether fusing these modalities improves engine component classification on a proprietary dataset from a major truck manufacturer. Through 5-fold cross-validation across multiple model configurations spanning three model families on five engine component classes (885 samples, the full cross-database matched population for this manufacturer), we find that naive fusion provides modest gains over text alone (65.3%). However, modality dropout during training, which randomly disables entire modalities per batch, forces the network to exploit weaker inputs and achieves 68.8% accuracy on text+DTC fusion (weighted F1: 0.67), a 3.5-point improvement over text-only (65.3%, weighted F1: 0.64) and the best result across all methods including logistic regression and gradient-boosted trees. Per-class analysis shows that the dominant modality varies by fault type: text describes symptoms, DTCs encode structured fault signals, and sensors measure physical state. On intake/exhaust faults, sensors alone reach 93% where text achieves 80%. On fuel system faults, fusion with modality dropout nearly triples accuracy from 15% to 38% over text alone. To our knowledge, this is the first application of three-way modality fusion combining text, sensors, and fault codes in industrial vehicle diagnostics.

---


### 300. [Counterfactual Transition Graphs: Evaluating Cross-Class Transition Quality](https://arxiv.org/abs/2608.23164)

**<font color=#1a73e8>作者：</font>** Syed Muhammad Hamza Zaidi, Szymon Bobek, Grzegorz J. Nalepa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Counterfactual (CF) explanations for time-series classifiers are usually evaluated one example at a time: what minimal edit flips this single window's prediction? We argue that the more informative question for diagnostic interpretability is structural: how does the classifier connect its own classes to each other?
We propose a counterfactual transition graph (CGT) in which each node is a class and each edge weight is the CF reliability of the transition from one prototype to another under a proximity aware retrieval sweep. On a six-class hand-movement task, we induce a CGT that reveals a non-trivial topology, which is not predicted by the binary confusion matrix: it shows that counterfactual reachability does not align with classifier accuracy and even runs counter to it (Spearman $\rho=-0.37$ over the 15 pairs), i.e. the boundaries the classifier separates most confidently are among those an in-distribution edit can least often cross.
Our framework is method agnostic, i.e. any CF-explainers can be used. Presently, we use it to juxtapose replacement-based CFs with gradient-based CFs; gradient-based methods reach almost any class by stepping off the data manifold, while replacement-based methods stay on it and fail on precisely the rigid boundaries.

---


> [!TIP]
> 当前位于：**251-300**（第 6/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-361](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
