# 📦 其他研究 | 2026年10月15日

> 本类共 **810** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**751-800**（第 16/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | **751-800** | [801-810](./part-17.md)

---

### 751. [Retrieval Disagreement as a Signal: Diagnosing and Steering Multilingual Dense Embedders](https://arxiv.org/abs/2610.18526)

**<font color=#1a73e8>作者：</font>** Faeze Ghorbanpour, Shaghayegh Kolli, Jana Diesner 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual dense retrievers place all languages in one shared space so that a question finds relevant documents, regardless of which language they are written in. We show that the same question, asked in different languages, retrieves substantially different documents, and this disagreement is not because of weak language understanding. Each language performs well on its own and ranks candidates consistently with the other languages; divergence appears only when languages share an index. We trace the mechanism: each language keeps its own ranking, but in the shared index, its correct answers are pushed far down, buried under non-relevant documents that are either in the query's own language or in English, depending on the model. We introduce disagreement-guided steering: for each language, we contrast the documents that other languages agree on for a question against those that language retrieves idiosyncratically, and take the difference of their representations as a language-specific direction, added to that language's queries at inference. Against baselines of language-mean removal, subspace removal, and per-language rotation, it most strongly reduces same-language crowding while remaining competitive on recall, trading off against mean removal, which better preserves ranking quality.

---


### 752. [Euclidean Distance-Based Flow Matching](https://arxiv.org/abs/2610.18534)

**<font color=#1a73e8>作者：</font>** Paul-Henrik Heilmann, Peter Ochs  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow Matching has recently become popular as a technique for generative modeling with applications in many domains. In the standard Flow Matching formulation, we interpret the vector field as the solution of a least-squares regression problem, which is known to be sensitive to contamination. Therefore we leverage the viewpoint of robust statistics and replace the squared Euclidean distance with the Euclidean distance as a regression objective. This seemingly minor change strongly affects the properties of Flow Matching. We provide a probabilistic interpretation of the new regression target as a conditional geometric median and use this characterization to study distributional robustness of the Euclidean Distance-based Flow Matching. We analyze the mathematical properties of this changed objective and the effect of a contaminated target distribution on the involved conditional velocity distributions. We discuss the challenge of directly characterizing the distribution that our method induces. In specific contamination settings we show theoretically that our method yields an improvement for severe contamination. Finally, we present numerical experiments conducted on the CIFAR-10 image dataset where a proportion of the samples has been contaminated. Our Euclidean distance-based Flow Matching shows a clear advantage in scenarios of severe contamination of the target distribution.

---


### 753. [On Symmetry for Characterizing Agent Heterogeneity in Multi-Agent Systems](https://arxiv.org/abs/2610.18538)

**<font color=#1a73e8>作者：</font>** Jianhong Wang, Jonathan Lawry  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Understanding agent heterogeneity can inform the design of shared and agent-specific policy representations, however existing criteria provide no unified structural test. We study finite-horizon POSGs and define a type-compatible transformation as a policy-evaluation symmetry when complete policy evaluation commutes with it for every decentralized behavioral policy. Policy-evaluation symmetries form a group for which agent orbits define structural agent types. This classification does not depend on the particular policy chosen or the distribution of initial states. We prove that every componentwise environment automorphism is a policy-evaluation symmetry, but that the converse does not hold. Applying the framework to cooperative Dec-POMDPs shows that agents can belong to different structural types even when they share a common reward. For prescribed weighted reward aggregation, we derive an exact value identity and sufficient conditions for the resulting Dec-POMDP to inherit the policy-evaluation symmetries of the source POSG. Finally, we give sufficient conditions under which repeated model factorizations induce policy-evaluation symmetry, and show that preserving an optimal Boltzmann policy set neither implies nor follows from this symmetry in general.

---


### 754. [From Mind Mapping to Dream Interpretation: Understanding Muslim Users' Engagement with GenAI Tools in Religious Context](https://arxiv.org/abs/2610.18549)

**<font color=#1a73e8>作者：</font>** Ishrat Jahan, Soomanib Kamruzzaman, K M Nazib Hossen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative Artificial Intelligence (GenAI) tools are increasingly integrated into everyday life, including sensitive domains such as religion. Prior works examined alignment with religious values and discussed the potential risks. However, to gain empirical insights into the adoption of these tools in users' religious lives, in this study, we conducted an online survey with 178 Muslim participants in Bangladesh and collected 726 prompts on religious use cases, along with open-ended responses about using these tools in religious contexts. Using reflexive thematic analysis, we identify three key roles these tools play in users' religious lives: (1) religious assistants, (2) perceived religious scholars, and (3) faith counselors. However, participants expressed concerns about misguidance, overreliance, and violations of Islamic tradition, and reported adopting protective strategies to avoid these pitfalls. Based on these, we propose a set of design guidelines for faith-sensitive GenAI systems that would preserve religious boundaries while supporting religious practices.

---


### 755. [Unbalanced W-Flow: Unbalanced Wasserstein Drifting under Finite-Batch Marginal Fluctuations](https://arxiv.org/abs/2610.18552)

**<font color=#1a73e8>作者：</font>** Jongwook Jeon, Mingue Park, Jiwon Choi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Teacher-free one-step generative models such as W-Flow learn directly from distributional objectives, with the Sinkhorn divergence providing the strongest empirical performance among the energies studied in W-Flow. However, Sinkhorn divergence is based on balanced optimal transport, whose exact marginal constraints can induce undesirable transport under finite minibatch fluctuations. We introduce UW-Flow, which replaces the balanced Sinkhorn energy with a debiased unbalanced Sinkhorn divergence and derives the corresponding Wasserstein velocity. The resulting dynamics retain W-Flow's cross-minus-self structure, recover the balanced limit, and preserve target identifiability under suitable assumptions. We further characterize the finite-batch velocity error of balanced and unbalanced transport by comparing each minibatch field with its population counterpart. Our analysis identifies conditions under which marginal relaxation yields smaller minibatch-to-population velocity error, and shows that for separated matched modes, balanced sensitivity grows with inter-mode separation while the corresponding Unbalanced Optimal Transport (UOT) sensitivity remains controlled by local transport geometry. Controlled experiments on fixed-support and continuous two-mode distributions support these predictions. On MNIST, CIFAR-10, and ImageNet-100, UW-Flow improves generation under matched training budgets, with the largest gains in unconditional generation and consistent improvements in the class-conditional setting.

---


### 756. [Last-Iterate Convergence of Clipped SGD with Linear Decay](https://arxiv.org/abs/2610.18555)

**<font color=#1a73e8>作者：</font>** Wei Jiang, Haomin Bai, Zechao Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we study the last-iterate convergence of clipped stochastic gradient descent under heavy-tailed noise. We assume that the stochastic gradients are unbiased and that the noise has a bounded central $p$-th moment, where $1<p\le2$. For smooth convex objectives, a linearly decreasing learning rate gives a high-probability error bound of order $O(LR^2\log(1/\delta)/T+\sigma R(\log(1/\delta)/T)^{(p-1)/p})$. We further establish last-iterate guarantees for nonsmooth composite objectives and smooth composite objectives with proximal updates. In addition, when a causal adversary replaces at most $q$ gradients, the same clipped update achieves a bound with $\log(1/\delta)$ replaced by $\log(1/\delta)+q$. The corresponding lower bounds for the clean and corrupted oracle models are also provided.

---


### 757. [Denoise X: Self-Supervised U-Net for Quantum Mottle Suppression in Chest Radiography](https://arxiv.org/abs/2610.18556)

**<font color=#1a73e8>作者：</font>** Parth Giramkar, Aryan Patle, Vanita Kshirsagar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning for medical image restoration is often constrained by the need for paired training data. Acquiring perfectly registered clean-noisy radiographs in vivo is impractical due to patient motion and radiation-dose limits. To address this, we employ a self-supervised Noise2Noise paradigm that trains on independently corrupted observations without paired clean images. We propose Denoise X, a lightweight self-supervised U-Net model (7.79M parameters) for suppressing quantum mottle and electronic readout noise in low-dose chest radiographs. It is trained on the NIH ChestX-ray14 dataset (112,120 images) using a stochastic Poisson-Gaussian noise simulator. Zero-shot evaluation on the unseen Montgomery County dataset achieved a PSNR of 36.09 dB and SSIM of 0.8806, outperforming the Bilateral filter while preserving high-frequency anatomical details. Using patch-wise inference, Denoise X processes native-resolution chest radiographs in ~2.2 s per image on a Tesla P100 GPU. Cross-domain evaluation on the Shenzhen dataset achieved 36.44 dB PSNR and 0.9099 SSIM, showing strong generalization. For resource-constrained deployment, the model was converted into a 31.16 MB ONNX model for efficient CPU inference on non-DICOM images.

---


### 758. [Prompt-Segmentation Meets ROI Encryption: Fine-Grained Video Protection Based on Diffusion Isolation](https://arxiv.org/abs/2610.18558)

**<font color=#1a73e8>作者：</font>** Xiang Zhang, Haoyan Lu, Ziqiang Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Region-of-interest (ROI) selective encryption in H.265/HEVC aims to protect sensitive content while preserving the utility of non-ROI regions. Existing coding-unit (CU)-level approaches still suffer from substantial encryption redundancy for two reasons. First, existing approaches map object-detection bounding boxes to CUs, producing regular rectangular regions, which poorly match the shape of irregular ROI boundaries, such as facial contours. Second, their coding-tree-unit (CTU)-based diffusion isolation expands the protected footprint in fixed $64\times64$ blocks, causing encryption-induced distortion to spread over a large number of non-ROI pixels. To address the aforementioned shortcomings, we propose a prompt segmentation-guided CU-level ROI encryption algorithm, which mainly consists of two core components. The first component is a prompt segmentation-guided fine-grained ROI encryption pipeline. It maps pixel-level ROI masks to CUs according to an ROI-overlap threshold, refines boundary CUs to $8\times8$ granularity, and applies format-compliant encryption to multiple syntax elements in the mapped ROI CUs. The second is a dual diffusion isolation strategy to address the encryption diffusion problem. For spatial isolation, the encoder refines non-ROI boundary regions into $8\times8$ CUs and uses PCM mode to bypass intra-frame prediction. For temporal isolation, it removes motion-vector candidates whose reference blocks overlap ROI CUs. Experimental results demonstrate that the proposed method generates encryption regions that more closely match irregular ROI boundaries, effectively confines distortion to the ROI.

---


### 759. [Observation Quality in DSM-Assisted Aerial Localization: A Benchmark and Base-Anchored Uncertainty Calibration](https://arxiv.org/abs/2610.18564)

**<font color=#1a73e8>作者：</font>** Pengyu Yin, Junxiang Tan, Jie Pan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aerial map matching provides position observations for navigation, but a position error alone does not determine how an observation should be weighted. We define five benchmark tasks: position availability and agreement, grouped error structure, predictive uncertainty, controlled updates, and temporal accumulation. A case study in digital-surface-model-assisted localization evaluates base-anchored uncertainty calibration within this framework. The method combines propagated image and map sensitivities with the second moment of a compact configuration subset relative to the reported position. The reported position remains unchanged, and scale is fitted using separate position references without local surface-height ground truth. Thirteen covariance models are evaluated on two held-out query sets from locations represented in the calibration data. Relative to a constant full-matrix baseline, the method reduces equal-location normalized position-update risk by 7.70% on 728 conditions and 5.46% on a separate 142 conditions under an independent prior, with all localization failures included. On the primary set, equal-location negative log likelihood improves by 2.571 nat. These results show improved reference-based weighting at seen locations. Exploratory base-quality and conditional-addition controls leave the incremental update benefit of configuration disagreement unresolved. Navigation benefit and real temporal accumulation remain untested.

---


### 760. [Order-Consistent Latent Geometry for Reliable Short-Horizon Planning in World Models](https://arxiv.org/abs/2610.18570)

**<font color=#1a73e8>作者：</font>** Junlin Wu, Wen Fan, Dandan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Latent planners often rank candidate action sequences by terminal Euclidean distance to a goal latent. Exact agreement with transition distance would make this score ideal, but is stronger than planning requires: along a transition-shortest rollout, the essential requirement is that latent distance does not reverse true transition progress. We show that this pathwise no-reversal requirement is precisely the classical self-approaching condition. To the best of our knowledge, we are the first to identify self-approachingness as a planner-facing compatibility condition for terminal Euclidean latent planning and to connect its violation to an exact finite-horizon candidate-order reversal. Because visual world models predict discrete latent sequences, we analyze their polygonal interpolation. We prove that an acute bend creates a nonempty region in which terminal Euclidean distance ranks a transition-worse candidate ahead of one that makes genuine progress, even under exact rollouts. We further interpret latent dimension as angular capacity through a classical spherical-code bound. A controlled six-branch experiment, including a zero-padded three-dimensional baseline, validates the predicted ordering failure and separates angular arrangement from ambient dimensionality.

---


### 761. [Parameter-Efficient Multimodal Brain Tumor Segmentation With Stage-Wise Shared Adapters](https://arxiv.org/abs/2610.18571)

**<font color=#1a73e8>作者：</font>** Milad Rostamian, Mohammadreza Mohammadi, Ender Konukoglu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Different MRI modalities reveal different parts of a brain tumor. Segmentation models combine information from these modalities to outline tumor regions. Many models use a separate encoder for each modality. However, exchanging features among these encoders at several stages can increase model complexity. We introduce the Block-Wise Shared Adapter (BWSA), which combines compressed features from the modality encoders in a shared path and returns adapted features to each stream. In its fixed-blending form, BWSA adds the adapted features to the original features. Its trainable-gated variant (TG-BWSA) instead learns separate weights for the original and adapted features at each modality and encoder stage. We evaluate both variants on BraTS 2020 and BraTS 2023 with four segmentation backbones. On the official BraTS 2023 online validation set, BWSA increases average region-wise Dice by 1.3--7.6 percentage points relative to the corresponding unmodified backbones. TG-BWSA increases it by 2.8--7.7 points. Both variants add approximately 0.85--3.73% parameters and reduce average HD95 relative to the unmodified backbones.

---


### 762. [Detecting Unreliable Classifications from Quantized Models](https://arxiv.org/abs/2610.18575)

**<font color=#1a73e8>作者：</font>** Ananya Kotla, Jorge T. Gomez  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Post-training INT8 quantization is typically validated by checking accuracy retention, which requires ground-truth labels often unavailable in low-resource clinical settings. We show a label-free alternative: comparing a model's own output before and after quantization. We compute cosine similarity between the FP32 and INT8 models' output probability vectors for each prediction, which requires only a single forward pass. This output-agreement similarity separates lower-accuracy predictions across four evaluated architectures (ResNet-50, VGG-16-BN, Wide ResNet-50, and ViT-B/16) under fixed-percentile splits, outperforming a confidence-only baseline for all four. These results show that quantized models can be compared to their baselines to assess their drift and determine whether they are well suited for clinical deployment.

---


### 763. [When More Objectives Make Identification Easier: The Role of Preferences and Feedback](https://arxiv.org/abs/2610.18577)

**<font color=#1a73e8>作者：</font>** Bo Xue, Ji Cheng, Yuanyu Wan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Best-arm identification (BAI) aims to identify the optimal arm using as few samples as possible. While most existing work focuses on a single objective, many real-world applications involve multiple criteria, which motivates the study of BAI in multi-objective bandits. Intuitively, multi-objective identification seems harder, since the learner must identify optimal arms in a higher-dimensional reward space; however, the additional objectives also provide richer feedback that can reduce the required exploration. In this paper, we characterize when and why multiple objectives can make BAI easier. For Gaussian bandits, we establish a characteristic-time lower bound for fixed-confidence identification that holds uniformly across preference orders. Through explicit comparisons under Pareto, linear, and lexicographic preferences, we reveal three phenomena: (i) identifying a larger optimal set can require fewer samples than identifying a unique optimum; (ii) the advantage of vector feedback over coordinate feedback depends fundamentally on the preference order; and (iii) multi-objective identification can require fewer samples than even the easiest corresponding single-objective problem. Finally, we propose Order-Aware Track-and-Stop (OATS), an algorithm that is correct at any prescribed confidence level and asymptotically matches the lower bound.

---


### 764. [X.js: A Live Benchmark for Node.js Taint-Style Vulnerabilities](https://arxiv.org/abs/2610.18585)

**<font color=#1a73e8>作者：</font>** José Afonso, João Madeira Pereira, Ronghao Ni 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> JavaScript vulnerabilities in npm packages pose a significant risk to the this http URL ecosystem, and a growing body of work aims to detect, exploit, and mitigate them. Studying and evaluating this work requires up-to-date collections of real vulnerabilities, yet the most commonly used datasets stop recording vulnerabilities in 2022. We present this http URL, a live benchmark of real-world this http URL taint-style vulnerabilities covering code and command injection, prototype pollution, and path traversal. Built from 1,738 advisories collected through mid-2026, primarily from the GitHub Advisory Database, this http URL pairs each vulnerability with precise source and sink locations, a validated executable exploit and its execution trace, and, when available, a patched version of the package. this http URL supports long-term reproducibility and growth: dependencies are mirrored in a self-hosted registry to guard against package removal from the ecosystem, and dedicated infrastructure generates and validates exploits for newly reported vulnerabilities. The current release contains 1,159 validated exploits for 965 packages. Using this http URL, we characterize how the frequency, structure, and complexity of this http URL taint-style vulnerabilities have evolved over time. We find that these vulnerabilities are increasingly reported in large packages: the median vulnerable package grew from roughly 250 LoC in 2021--2022 to 6,100 LoC in 2026.

---


### 765. [Fairness under Prediction Error in Predict-then-Optimize Pipelines](https://arxiv.org/abs/2610.18593)

**<font color=#1a73e8>作者：</font>** Hilda Adwubi Osei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fairness constraints in predict-then-optimize pipelines are necessarily enforced on predicted outcomes $\hat{y}$, since true outcomes $y$ are unobserved at decision time. We study whether a demographic parity constraint enforced this way continues to hold against $y$, and how the resulting violation scales with prediction error. Using a budget-constrained allocation problem solved as a linear program, we show empirically that the true-outcome fairness gap grows with prediction error $\sigma$ and saturates, well fit by $c(1 - e^{-\sigma/\tau})$ with $c = 0.1545 \pm 0.0103$ and $\tau = 3.9045 \pm 0.3745$; its mean is invariant to sample size while its variance decays at the standard $O(1/\sqrt{n})$ rate. We derive a two-part theoretical bound: a closed-form local sensitivity result showing the gap's first-order response to prediction error depends on only two individuals per group, validated against the solver to within three significant figures; and a universal, error-independent ceiling following from the boundedness of the decision variable, confirmed consistent with but looser than the empirical saturation level. On US Census income data, enforcing demographic parity on a trained predictor's output reduces an unconstrained disparity in true income to roughly one-third of its original size, leaving 34.4% $\pm$ 3.3% (California) and 35.7% $\pm$ 1.8% (Texas) of the disparity intact and undetectable from the predictions alone -- consistent not only in mechanism but in approximate magnitude across two states with different demographics and income distributions, and stable across ten independent train/test splits in each. A fairness constraint that appears fully satisfied at decision time can mask a substantial, systematic violation of the outcome it was meant to protect.

---


### 766. [Autonomous Cyber Operations Gym for Training and Evaluating AI Models for Defence](https://arxiv.org/abs/2610.18594)

**<font color=#1a73e8>作者：</font>** Tobias Hürten, Johannes F. Loevenich, Florian Spelter 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper proposes an Autonomous Cyber Operations (ACO) gym, a unified framework integrating high-fidelity network emulation, realistic user behaviour modelling for benign network traffic and adversarial profiles, and the generation of cybersecurity scenarios through open toolkits. By supporting live and deferred feature extraction at the packet and flow levels, the gym facilitates the creation of labelled synthetic datasets for training Deep Neural Network (DNN)-based Intrusion Detection Systems (IDSs), as well as developing and evaluating modular components for autonomous defence agents through emulated interactions. While evaluation of a DNN classifier within the gym shows high in-domain performance, achieving near-perfect recall on adversarial network flows, our experiments reveal a significant sensitivity to domain shift, showing that even minor changes in network composition, such as variations in traffic protocol distribution, can lead to a catastrophic collapse in model transferability and detection performance.

---


### 767. [Recasting DiT for Extreme Image Compression with Hierarchical Visual Priors](https://arxiv.org/abs/2610.18607)

**<font color=#1a73e8>作者：</font>** Yunuo Chen, Jingnan Gao, Bing He 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained diffusion models provide powerful generative priors for extreme image compression, but their stochastic, iterative generation processes are not designed to decode compressed representations directly. We present PrismCodec, which recasts a pretrained Diffusion Transformer (DiT) as a bitstream-grounded one-step generative decoder. PrismCodec uses the decoded representation in two complementary roles: a projected codec state defines the starting state for generation, while hierarchical visual priors derived from the same decoded latent provide semantic and structural guidance. To bridge the gap between stochastic, iterative generation and deterministic one-step decoding, we develop a progressive adaptation strategy. We first learn codec-conditioned transport from a noisy neighborhood centered on the codec state, distill it into a one-step mapping, and finally anneal the source perturbation to zero during end-to-end optimization. The resulting decoder reconstructs deterministically from the received representation without additional conditioning bits. Across Kodak, CLIC, and DIV2K, PrismCodec consistently improves rate-perception performance over prior generative codecs, achieving BD-rate reductions of 70-75% in LPIPS and 75-81% in DISTS over StableCodec. Code will be released upon acceptance.

---


### 768. [Nudge the Judge: Uncovering Program Decision Hijacking in Real-World Jev Applications](https://arxiv.org/abs/2610.18612)

**<font color=#1a73e8>作者：</font>** Yang Luo, Tiantian Ji, Zifeng Kang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> System One models such as Jev change how software makes decisions by mapping open-ended semantic contexts into structured judgments that directly drive program execution. However, this paradigm introduces a new security risk, which we term Jev Program Decision Hijacking (JPDH): attacker-controlled contexts can redirect program decisions through schema-valid Jev judgments. Existing evaluations focus primarily on model-level attacks or predefined injection channels, leaving attack reachability and downstream security consequences in real-world Jev applications underexplored.
In this paper, we present JevProbe, the first automated framework to evaluate JPDH by tracing adversarial influence from reachable context surfaces through program-consumed decisions to downstream security consequences in real-world Jev applications. Our key insight is that application logic maps diverse Jev judgments to observable decisions, enabling systematic, program-grounded attack evaluation. Across 228 popular real-world Jev applications and 2,273 test cases, 81.5% exhibit decision flips, of which 98.6% lead to potential downstream security impacts. Compared with the strongest adapted baseline, JevProbe improves macro-average Decision Flip Rate (DFR) by 50.4 percentage points, while existing defenses offer limited protection. We further construct JevProbeBench to support systematic evaluation of JPDH in real-world Jev applications. We have responsibly disclosed our findings to Jev application maintainers, pending their responses. The source code of JevProbe and the JevProbeBench dataset are publicly available on GitHub (this https URL).

---


### 769. [Two Routes to Interoceptive Prioritisation: Dissociating Likelihood Precision and Preference Reweighting in Active Inference](https://arxiv.org/abs/2610.18617)

**<font color=#1a73e8>作者：</font>** St John Grimbly, Nicolas Kuske, Evert A. Boonstra 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An embodied agent must prioritise among competing bodily needs. In active inference, it can respond to an urgent need by increasing the precision of information about that need or by increasing its preference for outcomes that relieve it. We compare these two interventions, separately and together, in a foraging gridworld with three lethal needs, and ask how each changes survival, perception and the body model the agent learns. Precision sharpens interoceptive posteriors and improves survival. Preference reweighting keeps bodily states further from their lethal boundaries and changes the states from which the agent learns, so its learned model covers fewer need levels, with lower quality across all levels but slightly higher quality on the levels it visits. An experiment on 72 further layouts does not establish the predicted preference benefit on difficult layouts, but both interventions improve average survival there and their interaction is positive. Survival alone therefore gives an incomplete account of how a model prioritises needs and learns about its body.

---


### 770. [Deterministic Prediction as Global Velocity: Flow Matching for Probabilistic Time-Series Forecast](https://arxiv.org/abs/2610.18621)

**<font color=#1a73e8>作者：</font>** Jiajing Hu, Xu Han, Li-Ping Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate uncertainty quantification is critical for many time series forecasting applications, and recent studies have increasingly adopted generative models to capture predictive uncertainty. Existing approaches often combine deterministic forecasting with generative modeling to improve predictive performance. However, their joint training is typically unstable because the deterministic model is embedded within the generative process, resulting in deep computational graphs and changing the probability transport path. In this work, we propose DV-Flow, a unified flow-matching formulation that incorporates the deterministic predictor as a parallel velocity component rather than as the endpoint of the transport path. This design enables stable end-to-end optimization while subsuming several existing formulations as special cases, allowing direct comparisons among them. Extensive experiments on six real-world datasets demonstrate that DV-Flow consistently improves probabilistic forecasting performance over strong baselines. Our code is available at this https URL.

---


### 771. [Breakdown of Conversational Involvement: A Joint Multi-Modal Analysis of Conversation Floors and F-formation Detection with Multiple Features](https://arxiv.org/abs/2610.18627)

**<font color=#1a73e8>作者：</font>** Zonghuan Li, Chirag Raman, Hayley Hung  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Interactions happen universally and spontaneously in daily lives. Studying involvement in interactions helps us analyze who can influence who and has a wide potential in applications. Specifically, we consider conversational involvement in free-standing conversations. We study two operationalizations of an FCG: F-formations and conversation floors, and propose that current assumption that F-formations capture single conversations is insufficient. To illustrate how different implementations could impact the detected F-formations, we employ three analyses. First, we propose that speaking status can be used for estimating conversation floors, and leveraged it to analyze floors within F-formations. Second, we analyze spatial characteristics of the detection results by applying different feature sets on chosen baselines, and find that groups resulting from head features are more likely to be subsumed by groups detected using other features. Finally, we do a joint analysis which combines the spatial features and floor patterns in the conversation. We observe that certain pipelines can detect groups with single floors from upper body features, while retaining F-formations with lower body features. We conclude that a more detailed theory and framework is needed to holistically demonstrate conversational involvement within interactions.

---


### 772. [ST-GRU PredRNN-V2: A GRU-Based Reformulation of PredRNN-V2 for Video Prediction](https://arxiv.org/abs/2610.18645)

**<font color=#1a73e8>作者：</font>** Augusta van Haren, Hanna Hoogen, Luca Pattavina 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video prediction requires models to capture complex spatiotemporal dependencies and to retain relevant information over long sequences. PredRNN and its successor PredRNN-V2 address this challenge with spatiotemporal Long Short-Term Memory (ST-LSTM) units that maintain two separate memory states, at the cost of a relatively complex recurrent building block. In this work, we investigate whether the simpler gating of Gated Recurrent Units (GRUs) can be transferred to spatiotemporal predictive learning. To this end, we develop a spatiotemporal GRU (ST-GRU) unit as a GRU-based alternative to the ST-LSTM. The ST-GRU replaces the ST-LSTM's three gates per memory state with two GRU-style gates (update and reset), and merges the temporal memory state into the hidden state, which reduces the number of parameters by about 5%. We incorporate the ST-GRU into PredRNN-V2 and evaluate the resulting model on the Moving MNIST video prediction benchmark, following the original experimental protocol. Averaged over ten predicted frames, the ST-GRU-based PredRNN-V2 achieves an MSE of 55.1, an SSIM of 0.883, an LPIPS of 0.065 and a PSNR of 19.53dB. It does not surpass the original ST-LSTM-based PredRNN-V2 on MSE, SSIM or PSNR, but it achieves a lower LPIPS and performs on par with the earlier ST-LSTM-based PredRNN, while using a simpler recurrent cell. These results suggest that ST-GRUs are a promising building block for spatiotemporal predictive learning and motivate further work on their design and integration.

---


### 773. [Tiny Recursive Message Passing](https://arxiv.org/abs/2610.18649)

**<font color=#1a73e8>作者：</font>** Tommaso Salvatori, Matteo Forasassi, Alexis Toumi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Message passing neural networks have shown remarkable performance in algorithmic and constraint reasoning, due to their ability to encode the structure of the task directly in the architecture. Recent work has shown that better results can be achieved using recursive transformers trained with deep supervision and truncated recursions, which make extremely deep loops stable to train, and equipped with test-time procedures such as discrete deduction lattices. In this work, we apply the same procedures to message passing networks, and show that the two ingredients are complementary, and lead to parameter efficient models: we obtain about $99\%$ test accuracy on Sudoku-Extreme with a model of $16$k parameters that trains in about $10$ minutes on an H100, or in $9$ hours on a CPU. We further show that the cost of truncating gradients grows with the number of rounds information needs to cross the graph, making the choice of wiring a trade-off between robustness to truncation and transfer across problem sizes. We conclude by showing that our models transfer zero-shot to larger instances than those seen during training, outperforming popular neural baselines on N-queens and Boolean satisfiability with a fraction of their parameters.

---


### 774. [Texture Interpolation as Texton Matching](https://arxiv.org/abs/2610.18655)

**<font color=#1a73e8>作者：</font>** Ido Madar, Gal Oren, Shai Avidan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Texture interpolation asks what should lie between two textures. Standard methods typically blend pixels or features at corresponding spatial locations, implicitly assuming that co-located elements should be mixed. For unrelated textures, however, this correspondence is arbitrary: a crack at one location has no particular relationship to a fiber at the same location in another image. We study whether this hidden pairing choice is itself a major determinant of interpolation quality. We represent textures as collections of local appearance vectors, or textons, and replace positional pairing with appearance-aware matching while keeping the encoder, representation, and decoder fixed. This isolates the effect of correspondence from changes in model capacity or training. Across texture pairs, appearance-aware matching consistently improves the distributional quality of interpolated midpoints over positional feature blending. Soft matching produces the strongest midpoint statistics, whereas one-to-one assignments yield more balanced transitions and closer agreement with the target endpoint. The same intervention also improves a second pretrained texture interpolator without retraining. These results identify correspondence as a first-class design choice in texture interpolation: meaningful transitions depend not only on how strongly two textures are mixed, but also on which local appearances are mixed with one another.

---


### 775. [BridgeTwist: Twisting Schrödinger Bridges for Training-Free Conditional Sampling](https://arxiv.org/abs/2610.18658)

**<font color=#1a73e8>作者：</font>** Mengyu Li, Qianqian Qu, Jun S. Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models are often required to serve many downstream conditional tasks. In the training-free setting, a pretrained unconditional model is reused as a prior and combined with a task-specific likelihood to sample from the corresponding posterior. While such training-free samplers have been developed for diffusion and flow models, their counterpart for Schrödinger bridge (SB) models remains unexplored, despite the growing appeal of SBs as flexible stochastic transport models between general source and target distributions. We propose BridgeTwist, a training-free conditional sampler for pretrained SB generative models, formulated as a tempered twisted sequential Monte Carlo scheme. Its twist is a closed-form plug-in surrogate, obtained by combining the velocity and score fields exposed by SB pretraining into an endpoint predictor and evaluating the likelihood there. Since this surrogate is less reliable near the source, we temper the twist with a time-varying exponent, downweighting its influence at early steps. We further introduce a bridge-shaped inference-time diffusion schedule that concentrates the proposal noise in the interior of the path. Telescoping importance weights then cancel all intermediate twist factors, yielding an asymptotically exact sampler for the posterior. Empirically, BridgeTwist outperforms training-free baselines on class-conditional and text-prompted image generation, and is competitive with specialized inverse problem solvers on inpainting, deblurring, and super-resolution.

---


### 776. [ARACDE: Retrofitting Databases with ABAC using External Authorization Engines](https://arxiv.org/abs/2610.18660)

**<font color=#1a73e8>作者：</font>** Karthikeya S M Yelisetty, Shamik Sural, Santosh Nagarakatte  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper proposes a methodology for decoupling the authorization logic of a relational database from its core data management engine, enabling specification of advanced access control policies with minimal changes to the code base. Our decoupled authorization architecture, which we call ARCADE, externalizes access request resolution to a formally verifiable policy engine (e.g., Cedar), while the database itself enforces those decisions. We showcase the capabilities of ARCADE on two widely popular open-source databases, namely MySQL and PostgreSQL. Purpose built lightweight plugins add an Attribute-based Access Control (ABAC) layer that augments the native discretionary and role-based access control capabilities of these databases. ARCADE supports highly expressive policies using attributes of subjects, objects, and the environment, and the use of Cedar enables easy auditing and verification of the specified policies. It follows a design principle that mitigates potential risks in segregating authorization from the database core through low footprint, network isolation, and a policy composition methodology that does not negate any native authorization. Experiments on TPC-C, TPC-B, and a custom workload show that ARCADE incurs negligible performance overhead, for instance, less than 3.9% throughput penalty for MySQL (1.3% for PostgreSQL) on industry standard TPC-C benchmark.

---


### 777. [PlanPath: Exploration-Guided Orchestration for Patient-Level Pathology Reasoning](https://arxiv.org/abs/2610.18664)

**<font color=#1a73e8>作者：</font>** Jiusong Ge, Mingzhao He, Qidong Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A patient's pathology case spans tens of slides from distinct specimens and anatomical sites, each carrying non-redundant, site-specific evidence. Forming a patient-level conclusion therefore requires locating the slides relevant to a given question and integrating complementary findings across them. However, existing pathology agents analyze one slide at a time and describe morphology rather than measure it, leaving evidence acquisition across a patient's specimens and patient-level quantification underexplored. To address this gap, we propose PlanPath, an agentic framework for patient-level pathology visual question answering (VQA). PlanPath turns the question into an exploration plan that specifies the evidence required, routes to the slides likely to carry it, and drives coarse-to-fine acquisition from tissue architecture down to individual cells. Tissue- and cell-level tools supply the counts, proportions, and extents, which PlanPath aggregates across slides into a traceable answer. To enable evaluation, we build two patient-level VQA datasets for renal and gastric cancer, averaging 15 WSIs per patient, with pathologist-verified question-answer pairs derived from diagnostic reports. Experimental results show that PlanPath outperforms the strongest baseline by 9.4% and 12.1% in overall accuracy on the two datasets and further improves existing slide-level agents when plugged into our framework. The dataset and code are available at: this https URL.

---


### 778. [Known-Voice Cloning and the Limits of Personality Transfer for Character Design](https://arxiv.org/abs/2610.18669)

**<font color=#1a73e8>作者：</font>** Johanna Magdalena Kuch, Maud van Lier, Daksitha Senel Withanage Don 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in zero-shot voice cloning systems make it possible to reproduce a recognizable voice from a short recording and attach it to arbitrary virtual characters. Prior work suggests that familiar vocal identity can carry over associated personality impressions to new targets such as robots or virtual characters. However, these works have mainly examined familiarity and personalization effects rather than directly testing whether a cloned familiar voice systematically transfers personality impressions to an embodied virtual character. Such transference raises the concern that cloned voices could be used to manipulate people into engaging with virtual characters as capable social actors. Across two studies, we investigated whether personality impressions transfer when a virtual character speaks with the cloned voice of a familiar person. Study 1 examined this question in a real-world university setting using the cloned voice of a lecturer familiar to the participating students. Study 2 examined the same question online using voices of social media content creators and members of their communities. Drawing on the concepts of identity activation, trait transfer, and person reconstruction, we show that evidence of personality transfer was limited in both studies. Observed effects were selective and did not generalize across traits or study contexts. In the online study in particular, recognizable voice identity cues activated expectations about the speaker but did not reconstruct the broader person impression. Qualitative responses further indicated that judgments were frequently shaped by perceived artificiality and by whether voice and appearance fit together. Our findings moderate common concerns that cloned voices straightforwardly manipulate people into perceiving artificial characters as capable social actors.

---


### 779. [Model-Based Online Decision Making via Generative Trajectory Planning](https://arxiv.org/abs/2610.18677)

**<font color=#1a73e8>作者：</font>** Haldun Balim, Yilun Du, Na Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online decision-making faces a tension between efficient inference and long-horizon reasoning. Value-based methods rely on short-horizon bootstrapping that limits the propagation of long-term information, while trajectory optimization methods plan explicitly but must solve a high-dimensional optimization problem at every decision step. We propose Generative Trajectory Planning (GTP), a model-based framework that addresses this tension by learning a generative model as a proposal distribution over action sequences. Instead of optimizing sequences from scratch, GTP samples candidate sequences from a diffusion prior and refines them using learned dynamics, reward, and value models, enabling efficient trajectory-level reasoning. Across continuous control and long-horizon manipulation tasks, GTP matches or exceeds state-of-the-art model-free, diffusion-policy, and model-based baselines, and remains stable in regimes where strong baselines degrade. Our results suggest that generative models are best understood not as policies, but as structured proposal distributions for planning, offering a new perspective on how to integrate generative modeling with model-based decision-making.

---


### 780. [Communicating Uncertainty in AI-Supported Nurse Scheduling: Expert Co-Design and Evaluation of an Explainable AI Prototype](https://arxiv.org/abs/2610.18679)

**<font color=#1a73e8>作者：</font>** Alice Rollwagen, Emily Schiller, Anton Hummel 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Nurse scheduling is a complex optimization problem in which nurses are assigned to shifts to meet staffing demands while complying with working-time limits, qualification requirements, and other operational and regulatory constraints. Artificial intelligence is increasingly being used to support this process by forecasting future staffing needs and providing advice on how to improve shift scheduling. Effective human-AI collaboration in nurse scheduling requires users to understand, interpret, and appropriately act on AI forecasts and advice. However, it remains insufficiently understood how healthcare professionals use transparency mechanisms like uncertainty communication and AI advice explanations when making staffing decisions. Applying a human-centered design approach, we iteratively developed a prototype decision support system for nurse scheduling and evaluated it through a mixed-methods user study with expert users. Using thematic analysis, questionnaire data, and eye tracking, we examine how healthcare professionals interact with the system and how uncertainty communication and explanations of AI advice influence understanding, decision confidence, trust, and usability. We found that the uncertainty communicated in AI forecasts was frequently misinterpreted and reduced decision confidence. Explanations were generally perceived positively, but did not significantly affect decision confidence or advice acceptance. We conclude with eight design implications derived from our findings, providing insights for the design of more transparent and effective AI-supported decision support tools in healthcare.

---


### 781. [RadarGSOcc: Doppler-Aware 3D Semantic Occupancy Prediction Using 4D Radar Tensor with Geometric-Semantic Feature Extraction](https://arxiv.org/abs/2610.18686)

**<font color=#1a73e8>作者：</font>** Christofel Rio Goenawan, Dong-Hee Paek, Seung-Hyun Kong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D semantic occupancy prediction is crucial for autonomous driving, but camera-based methods degrade in low-light conditions and LiDAR-based methods are sensitive to adverse weather. 4D radar is more robust, yet its sparsity and the high cost of radar tensor processing limit its use. We propose Radar Geometric-Semantic Occupancy Prediction (RadarGSOcc), an efficient framework that directly processes 4D radar tensors by separately extracting geometric and semantic features, including Doppler information, with a deformable attention-based geometric refinement module as its key component. We also introduce the K-Radar 3DSemOcc benchmark, the first large-scale benchmark for 3D semantic occupancy prediction using 4D radar tensors, built on the K-Radar dataset with refined LiDAR-based annotations. RadarGSOcc predicts 15 classes within a 51.2m range and achieves 38.2% IoU, 7.6% mIoU, and 25.5% weighted mIoU, outperforming RadarOcc by 17% relative (25.5 vs. 21.9) in weighted mIoU while using fewer parameters and lower computation. It substantially improves truck prediction while trading off car accuracy, outperforms camera-based approaches, and narrows the gap with LiDAR-based methods. To assess robustness without per-frame ground truth in adverse weather, we further propose a novel proxy metric, Environment-Based KL Divergence (EBKL), under which 4D radar proves a reliable and efficient modality for 3D semantic occupancy prediction. The dataset and code will be publicly available.

---


### 782. [Orientation Estimation of Cryo-EM Images for Molecules with Arbitrary Symmetry by Semidefinite Programming](https://arxiv.org/abs/2610.18691)

**<font color=#1a73e8>作者：</font>** Yunpeng Shi, Amit Singer, Jinxin Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper extends the non-unique games framework introduced in Bandeira et al. (2020) to address symmetric structures. Precisely, we consider the problem \[ \begin{aligned}
\underset{g_1,\ldots,g_n\in \mathcal{G}}{\operatorname{min}}\,\, \frac{1}{|S|}\sum_{i,j=1}^n \sum_{s\in S} f_{ij}(g_i s g_j^{-1}), \end{aligned} \] where $\mathcal{G}$ is a compact group, $S\subset \mathcal{G}$ is a finite subgroup of symmetry elements, and $f_{ij}:\mathcal{G}\rightarrow \mathbb{R}$ is a loss function. A notable example is common lines based orientation estimation of cryo-EM images for molecules with point group symmetry $S$, where $\mathcal{G}$ is the rotation group $\operatorname{SO}(3)$. With a semidefinite programming relaxation, we turn the problem into a convex program that is solved with the alternating direction method of multipliers. Unlike existing approaches which are tailored to specific symmetry groups, ours provides a unified computational framework for addressing all point group symmetries. We demonstrate the applicability of the proposed algorithm on the cryo-EM orientation estimation problem on both simulated and experimental datasets. In particular, our algorithm is effective in generating high-quality ab initio models from only a few class averages computed from experimental images.

---


### 783. [CryoTracer: A Synthetic-to-Real System for Filament Instance Tracing in Cryo-EM](https://arxiv.org/abs/2610.18696)

**<font color=#1a73e8>作者：</font>** Radosław Kuczbański, Wojciech Kozłowski, Mateusz Grzesiuk 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Particle picking in cryo-electron microscopy is commonly formulated as an object-detection problem in which individual particles are represented by bounding boxes, a natural representation for globular particles but a poor match for filaments that can extend across an entire micrograph. Existing methods reconstruct filament trajectories by linking local predictions in a separate post-processing stage, decoupling detection from instance formation and creating potential ambiguities at gaps and crossings. Directly preserving filament identity is particularly useful for polymorphic specimens, where segments originating from the same filament should remain associated. However, learning such instance-level representations is challenging because expert centerline annotations are scarce and costly to obtain. We introduce CryoTracer, a synthetic-to-real framework that addresses this limitation through procedural micrograph generation, transformer-based polyline prediction, and specimen-specific fine-tuning. Procedural pretraining exposes the model to diverse filament geometries, intersections, and imaging conditions before adaptation using a limited number of fully annotated experimental micrographs. CryoTracer represents filaments as ordered centerline polylines and optimizes their geometry using an orientation-invariant discrete Fréchet objective, enabling consistent learning regardless of tracing direction. Evaluation on established and newly expert-annotated datasets shows that CryoTracer improves instance-level filament recovery over existing particle-detection approaches. These results establish end-to-end polyline prediction as a practical alternative to detection-and-linking pipelines for recovering complete filament instances with limited micrograph annotation budgets. Code and data are available at this https URL

---


### 784. [Learning Source Structure: Bayesian Prediction with Transformers](https://arxiv.org/abs/2610.18725)

**<font color=#1a73e8>作者：</font>** Meir Feder, Ruediger Urbanke  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A transformer trained on sequences whose source parameters are drawn afresh each time can learn only what the sequences share: the source family and its prior. The Bayesian predictor that knows both, which we call informed Bayes, is the unique minimizer of the training loss and is computable from the family alone; we use it as a quantitative, falsifiable reference. Where earlier work compared transformers with Bayes on sources whose contexts can be learned independently, we build Markov sources with up to 64 symbols in which observations in one context inform prediction in another: product sources with known or hidden encodings, transition rows sharing an unknown base law and depth, and a mixture of three families. Our main result is that informed Bayes predicts, from the family and prior alone, how a trained transformer behaves in four tests that go beyond the learning curve: the loss that remains under a source outside the training family (predicted 2.237 bits, measured 2.309), the doubling of the extra loss when two independent components change rather than one (0.345 predicted, 0.350 measured), the benefit of other contexts when a token appears for the first time, and the depth at which copying an earlier continuation starts to pay. On the learning curves themselves, small transformers match informed Bayes when the shared structure is visible in the tokens, and hidden structure needs more layers and training, with gaps below 0.01 bits per token for the largest models. We explain why the imitation is possible and where it must fail: informed Bayes decomposes into sufficient statistics that attention selects and accumulates and an estimator, fixed by the prior, that the feed-forward network learns; training pays the complexity of informed Bayes under the architecture's prior, and finite-memory universal prediction bounds how closely a bounded network can reach it.

---


### 785. [Learning When to Transfer: Reinforcement Learning for Carbon-Footprint Modeling in New Manufacturing Domains](https://arxiv.org/abs/2610.18730)

**<font color=#1a73e8>作者：</font>** Muhammad Umar Farooq, Daniel R. Cooper  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Manufacturers often need to characterize a new material, process, or product before enough operating data are available to train reliable predictive models for this new, target domain. Existing manufacturing operations contain potentially useful knowledge to accelerate this characterization, but indiscriminate reuse of data from existing source domains can cause negative transfer in learning of the new, target domain when the manufacturing domains differ sufficiently. This work proposes a reinforcement-learning method for selective knowledge transfer, where its reward scores each opportunity to transfer against supervised alternatives, so negative transfer is avoided and controlled during forward prediction instead of being diagnosed afterwards. Given limited data from a new target domain, the learned policy chooses among predictors based on individual source operations, subsets of the sources, or the supervised alternatives: fully pooled sources, or target data alone. A validation gate deploys the transferred prediction only when it improves upon the supervised alternatives. The method is designed for learning variables supporting carbon accounting, as well as performance and quality outcomes. We demonstrate the approach by quantifying the embodied greenhouse-gas emissions of parts produced via material-extrusion additive manufacturing, using data from 729 experiments spanning five materials: ABS, PETG, TPU, PLA, and recycled PLA. The response combines measured fabrication electricity with polymer-specific cradle-to-gate production factors, while 22 material, process, and toolpath features characterize each experiment. In leave-one-material-out evaluation, this method achieves a mean test RMSE of 5.2 g CO2e per part, 20.00% lower than target-only training (32.5% lower when only 5-10% of the target training data are available) and 10.30% lower than indiscriminate source-target pooling.

---


### 786. [Neural Block-wise Auto-exposure for Single-Shot High Dynamic Range Imaging](https://arxiv.org/abs/2610.18733)

**<font color=#1a73e8>作者：</font>** Zhengguo Li, Chaobing Zheng, Wei Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Block-wise varying exposures are effective for cap- turing appearance of a real-world high dynamic range (HDR) scene via a single-shot. However, brightness order reversal (BOR) artifacts, blocking artifacts and loss of details in highlight/shadow regions are possible issues for block-wise varying exposures. In this paper, a novel neural block-wise auto-exposure algorithm is proposed to address the issues. The proposed algorithm maps a temporary image and its exposure time to the exposure times of all non-overlapping 16 X 16 blocks. The temporary image can be either an sRGB or a raw image. Although the sRGB image is widely adopted in existing auto-exposure algorithms, exposure times of blocks in the highlight and shadow regions might not be accurately learned due to the limited radiance measurement capability of the sRGB image. This paper thus also explores the feasibility of temporary image as a raw image. Due to the better radiance measurement capability of the raw image, the exposure times of blocks are learned more accurately, and more details in the highlight/shadow regions of the real-world HDR scene are captured by the resultant HDR imaging system. Experiment results validate the proposed neural block-wise auto-exposure algorithm.

---


### 787. [Concealed Handgun Detection using WiFi Signals](https://arxiv.org/abs/2610.18736)

**<font color=#1a73e8>作者：</font>** Erik Persson, David Gustafsson, Tomas Wilkinson  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While conventional camera-based surveillance systems and metal detectors can provide a sufficient level of security when used appropriately, they have fundamental limitations that reduce their applicability. Camera-based systems are unable to detect occluded or concealed threats and metal detectors require each person to enter through a narrow opening one at a time, leading to congestion issues and limited use in large crowds. A WiFi-based security system has the potential to be a complementary modality that is able to handle occlusions or concealment and is not hindered by strict spatial configurations. In this paper, we propose use Channel State Information estimated from WiFi-signals to detect concealed handguns. To this end we collect a dataset of aligned WiFi signals and RGB images that we call the WiFire dataset. We also propose a deep learning model called WiFireNet tailored to detect concealed handguns in WiFi signals using vision-based supervision signals. Our results show that concealed handgun detection is possible in WiFi and has promise as a complementary modality to surveillance cameras and metal detectors. We release the dataset, model and code to facilitate the further research into WiFi-based handgun detection.

---


### 788. [A Rate Transfer Method: Convergence Rates in Stochastic Gradient Descent via Stochastic Calculus](https://arxiv.org/abs/2610.18739)

**<font color=#1a73e8>作者：</font>** Neil Walton  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop a rate-transfer method that converts finite-time Lyapunov estimates for an associated stochastic differential equation (SDE) into finite-time convergence bounds for stochastic gradient algorithms. Under generic moment and smoothness conditions, the convergence analysis of the stochastic gradient method reduces to a calculus argument verifying a Lyapunov generator inequality for the SDE. The method recovers established rates for classical stochastic gradient methods and provides a way to establish convergence rates for new optimization algorithms through calculus arguments applied to their associated SDEs.

---


### 789. [Context-aware Bayesian Fusion for Multimodal Object Detection](https://arxiv.org/abs/2610.18741)

**<font color=#1a73e8>作者：</font>** Arunachalam Venkatachalam, Mhafuzul Islam, Marwan Yusuf 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable detection of pedestrians and road users is essential for the safe operation of autonomous vehicles. However, this task becomes increasingly challenging under adverse environmental conditions, such as poor weather and low lighting, where the performance of state-of-the-art pre-trained object detectors and on-board sensors tends to degrade, which limits their effectiveness and reliability. Moreover, retraining models for each operating context imposes significant constraints due to high data requirements, computational resources, and time. Considering this, we propose a novel context-aware multimodal late fusion approach that integrates a lightweight gating network within our probabilistic calibration framework. The gating network extracts environmental context and dynamically modulates the detection outputs of pre-trained object detectors based on the inferred context, without retraining of the detectors. Our methodology is evaluated on a modified KITTI dataset, in which the camera images and lidar pointclouds are augmented for varying fog levels. Experimental results show that our approach yields an approximately 14% relative improvement over non-adaptive late fusion baselines, achieving a consistent average precision of 56% across different fog levels.

---


### 790. [Bio-Inspired Electrotactile Feedback: A Framework and Impacts of Multimodal Cues](https://arxiv.org/abs/2610.18746)

**<font color=#1a73e8>作者：</font>** Melika Emami, Amirhossein Bayat, Rahim Tafazolli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Electrotactile stimulation, as a haptic feedback method, often struggles to evoke high-quality natural sensations. Consequently, despite its practical advantages, it is generally less preferred in human-machine systems than mechanical approaches. In this paper, we propose a bio-inspired stimulation framework that generates signals modelled on afferent neural activity derived from a touch model. By producing more biologically plausible spiking patterns, the proposed approach aims to enhance the realism of perceived tactile sensations. To evaluate these stimulation patterns in a realistic task context and to quantify the influence of visual and movement cues, we conducted a series of subjective experiments under three conditions. The results indicate that bio-inspired modulation was effective: in particular, bio-inspired co-modulation of amplitude and frequency achieved a favourable pressure-irritation trade-off, increasing the probability of perceiving pressure while maintaining low irritation (pressure: 0.78; irritation: 0.24) relative to the other patterns. Visual cues and hand movement further improved feedback quality by significantly increasing the probability of reporting pressure (p$<$0.001) without a corresponding increase in irritation, and by increasing mean naturalness ratings. Overall, these findings demonstrate the potential of bio-inspired electrotactile patterns to improve haptic feedback quality, and highlight the importance of evaluating such methods under realistic, multimodal interaction scenarios.

---


### 791. [LayerCanvas: Infographic Generation in AI Learning Assistants via Hybrid Layer-Set Diffusion](https://arxiv.org/abs/2610.18763)

**<font color=#1a73e8>作者：</font>** Keshav Gupta, Jeremy Owen, Christopher Lloyd 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online learning platforms are increasingly deploying AI assistants to provide personalized, on-demand tutoring. These can leverage infographics to communicate complex information and improve the learning experience. However, automating effective infographic generation remains a challenging task, requiring a combination of visual richness with precise typography, structured layouts, and continued editability. Existing representation methods satisfy these goals only in part: Scalable Vector Graphics (SVG) representations preserve geometry, hierarchy, and text but provide limited aesthetic flexibility, while raster diffusion models produce richer appearances by flattening content and layout into a single image. Conditioning a diffusion model on a rasterized SVG does not resolve this conflict because the raster preserves approximate placement but discards element ownership, occlusion relationships, and the structure needed to modify and recompose the result. We introduce LayerCanvas, a hybrid approach that retains SVG as the semantic, structural, and typographic program while using diffusion to aestheticize non-text content. Rather than generating one flattened raster, LayerCanvas partitions SVG elements into z-ordered sets of mutually non-overlapping elements and processes them through communicating parallel RGB generation streams. The resulting layers are independently editable and deterministically recomposed, while text is rendered from preserved vector metadata. Our approach combines rich visual synthesis with accurate typography and localized editing. LayerCanvas substantially improves text fidelity over state-of-the-art raster image generators while achieving the highest overall aesthetic quality. We further demonstrate non-destructive content editing, localization, asset reuse, and animation.

---


### 792. [MIST: Multi-Scale Spatial Context for Gene Expression Prediction from Histology](https://arxiv.org/abs/2610.18769)

**<font color=#1a73e8>作者：</font>** Koushik Howlader, Tirtho Roy, Md Tauhidul Islam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Predicting spatial gene expression from standard H&E images could extend molecular analysis to tissues without spatial transcriptomic measurements. A standard Transformer applies self-attention over spots but ignores where each spot sits in the tissue, whereas a spot's molecular state depends on tissue context at multiple spatial scales. Building on this insight, we introduce MIST, a Multi-context Spatial Transformer that augments the self-attention backbone with two context pathways applied in every layer: a coordinate-invariant local pathway that attends over spatial k-nearest-neighbor spots, and a slide pathway that broadcasts a whole-slide summary to every spot; the model predicts all spots in a single forward pass. Because coordinates enter only through pairwise distances, the local pathway is invariant to translations, rotations, and reflections when image features are fixed. In intra-cohort evaluation across six human organ cohorts from HEST-1k, MIST improves mean Pearson correlation over the strongest evaluated baseline by 9.7%, 11.6%, and 11.4% for 10-, 50-, and 100-gene panels, respectively, with the lowest average MSE and MAE. MIST further improves leave-one-organ-out transfer by 6.0% over the next strongest baseline, attains the best expression-derived domain recovery (highest mean ARI and NMI at every clustering resolution, and higher NMI than the closest baseline on 84% of held-out slides), and reproduces spatial expression patterns of selected cancer-marker genes. Together, these results show that adding local and slide context to a vanilla Transformer backbone is an effective approach to spatial gene expression prediction from histology.

---


### 793. [The Federated Tumor Segmentation and Classification (FeTS++) Challenge](https://arxiv.org/abs/2610.18771)

**<font color=#1a73e8>作者：</font>** Wenyi Tang, Carla Pitarch-Abaigar, Siddhesh Thakur 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> International challenges have become the standard for developing and benchmarking biomedical image analysis methods using centralized multi-institutional data. Federated learning (FL) describes a paradigm-shift on multi-institutional collaborations, where models are trained across institutions while their data are always retained locally. The Federated Tumor Segmentation (FeTS) challenge, first held in 2021, was the first challenge dedicated to FL in medical imaging and editions in 2022 and 2024 pushed the frontiers of real-world method validation. FeTS++ 2027 returns after a two-year gap with a substantially larger and more diverse cohort, and with the two "pluses" that name the challenge: an official classification task alongside segmentation, and a move of the infrastructure to NVIDIA FLARE (NVFlare). Built on the clinically acquired, multi-institutional multi-parametric MRI data of the BraTS 2025 Lighthouse challenge, FeTS++ spans gliomas and meningiomas across patient cohorts from institutions in North America, Europe, Asia, and Africa, and focuses on ranking submitted methodological approaches according to their model utility and an efficiency-aware score. Task 1 asks participants to find the best strategy for aggregating knowledge from per-institution segmentation models, while Task 2 asks them to distinguish glioma from meningioma under the same federated protocol, in which the entity label is heavily confounded with the site of origin.

---


### 794. [Jeva: System One Models from First Principles](https://arxiv.org/abs/2610.18773)

**<font color=#1a73e8>作者：</font>** Qi Li, Xinchao Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> System one models enable direct, low-latency decision-making. Yet recent practice of predicting an answer from serialized text does not, by itself, respect the structure of a decision problem. We argue that current designs underemphasize four important structural requirements. (i) null-aware: Models should distinguish answer absence from uncertainty among candidates; (ii) permutation-invariant: Reordering alternatives should not change the decision; (iii) option-scalable: Growing candidate sets should not require redefining the output space; (iv) cacheable: Request-independent computation over recurring alternatives should be reusable across requests. We introduce Jeva, a decision-native architecture that addresses these requirements jointly. A shared encoder independently represents the request and each option, while a compact decision stack refines only the request state against immutable option memory. Symmetric aggregation yields permutation-equivariant probabilities; shared scoring accommodates variable-size candidate sets. A separate coverage estimate distinguishes answer absence from candidate competition, enabling explicit null outcomes. Request-independent option representations and layer projections support reuse across newly assembled sets. These mechanisms unify Choice, Noul, and Score outputs. Across evaluations, Jeva combines strong typed-decision performance with near-perfect null detection and no decision flips under any tested permutations. It scales to thousands of candidates and substantially reduces latency through cross-request reuse without changing decisions.

---


### 795. [GAD: Geometry Attention Distillation for Consistent Video Generation](https://arxiv.org/abs/2610.18779)

**<font color=#1a73e8>作者：</font>** Junfeng Ni, Ziyu Zhu, Fan Jiang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video diffusion models generate visually compelling short-term sequences but often struggle to preserve scene geometry and object structure over time. In this paper, we first demonstrate that current video attention cannot identify reliable correspondences across frames, with responses dispersed across multiple regions even after recognizable scene structure has emerged. We argue that reliable cross-frame associations are essential for information exchange as scene structure forms in video generation. Thus, we introduce Geometry Attention Distillation (GAD), which transfers correspondences from a frozen geometry model's attention to video attention. Extracted from clean videos, these correspondences link the same static surface or moving object across frames. Since structure formation begins in deeper layers at higher noise and shallower layers at lower noise, we apply attention distillation at a student layer selected according to the noise timestep. After training, video attention focuses more consistently on corresponding locations. Experiments across all three video backbones demonstrate improved long-range scene consistency and dynamic temporal consistency, with geometric gains across generation lengths. On Wan2.2 5B, GAD improves cross-frame matching accuracy by at least 30% over the Wan baseline on both long-range benchmarks. Notably, GAD achieves these gains without additional inference modules, offering a promising approach to efficient and consistent video-based world simulation. Project page: this https URL.

---


### 796. [Pack Light, CarryOn: Building Object-Oriented Context for Long-Horizon Agents](https://arxiv.org/abs/2610.18784)

**<font color=#1a73e8>作者：</font>** Yuchen Lu, Julian McAuley, Lei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon agents accumulate progress in persistent task state, yet repeatedly process interaction histories describing how that progress was achieved. This raises a natural question: can long-horizon context instead be organized around reusable progress rather than the history that produced it? In this paper, we introduce CarryOn, an object-oriented context runtime that organizes continuation around reusable task objects. Rather than treating compressed histories or reconstructed accounts of progress as the primary basis for continuation, CarryOn builds a context view from continuation carriers, complementary execution context, and a live tail of recent interactions. A core challenge is keeping this reusable basis valid after its surrounding history is retired: how can CarryOn update the basis without reconstructing the full representation at every fold? CarryOn maintains carrier records across folds, revising affected records against bound evidence and applicable environment checks while carrying forward unaffected records and jointly updating execution context. Experiments on OSWorld 2.0 and BrowseComp-Plus show improved gains of 5.8% and 7.0% while reducing total token usage by 51.9% and 22.9%, respectively. Project page: this https URL

---


### 797. [Bytes to Threats: Byte-Sequence Transformer For Malware Detection](https://arxiv.org/abs/2610.18787)

**<font color=#1a73e8>作者：</font>** Abdelrahman Yassin Eljamal, Abdeltawab Hendawi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Existing malware detection approaches heavily rely on handcrafted features derived from static or dynamic analysis of the executable files. These methods require specialized domain expertise, dedicated analysis tools, and time-consuming analysis, which limits their scalability and robustness in the face of the increasing complexity and diversity of modern malware. Consequently, there is a growing interest in approaches that operate directly on raw bytes, which contain rich semantic and structural information. However, capturing long-range dependencies within executable files remains challenging for conventional static and CNN-based methods. This paper presents MalwareFormer, a transformer-based, byte-level malware detection framework that operates directly on raw bytes, without requiring domain knowledge or feature extraction. MalwareFormer achieves an accuracy of 98.35%, a balanced accuracy of 98.32%, a macro-F1 of 98.32%, and a false positive rate of 1.94%, outperforming both baselines across all threshold-dependent classification metrics and demonstrating that transformers provide a powerful and scalable approach for byte-level malware detection.

---


### 798. [Trust Before Autonomy: Rethinking Agentic Remote Sensing for Crisis Response](https://arxiv.org/abs/2610.18789)

**<font color=#1a73e8>作者：</font>** Georgios Angelidis, Aggelos Psiris, Spyridon Evangelatos 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Agentic remote sensing is evaluated on how many questions it can answer, whereas crisis response depends on whether its answers can be relied on and how much of the decision can safely be handed to the agent. This paper argues that \emph{autonomy should be earned, not assumed}: An Earth-Observation (EO) agent should be granted autonomy in proportion to demonstrated reliability, epistemic honesty and verifiability. The position is supported by an evidential meta-analysis of twelve agentic RS/EO/GIS benchmark studies from peer-reviewed venues. Only one repeats runs, three contain unanswerable tasks and none measures calibration. Their own tables show that completed workflows are often not correct (task success exceeds tool-call correctness by up to 54pp on identical queries), that the gap to an expert trajectory widens overall with trajectory length (from 7 to 56pp), and that capability does not predict abstention (Spearman r from -0.25 to 0.50, all n.s.). The paper then contributes three EO-specific trust properties, an autonomy ladder for crisis EO tasks, and a readiness protocol that replays archived emergency activations before any live use. In this context, current evidence justifies assistive roles only.

---


### 799. [Registration is a Representation Problem: Solving Whole-Body PET/CT Registration](https://arxiv.org/abs/2610.18804)

**<font color=#1a73e8>作者：</font>** Neel Dey, Adrian V. Dalca  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Raw image intensities are a poor surrogate for similarity across images in correspondence problems. Further, while auxiliary segmentation labels can provide semantic identification and improve matching, they can assign only coarse identities to fine-grained anatomy and often cover only a subset of structures, particularly in whole-body settings. We present an approach that instead establishes correspondence using complementary representations of anatomy and demonstrate its utility for longitudinal whole-body PET/CT registration in the Learn2Reg 2026 PSMAReg Challenge. Our 3D foundation model, anatomix, is used to derive fine-grained, per-voxel semantic representations that are consistent across volumes, and we further employ off-the-shelf segmentation models to obtain coarse anatomical identities. Together, these representations drive a GPU-accelerated iterative registration solver (FireANTs) in a hybrid multistage framework: the first stage estimates alignment from dense multi-channel features, after which a second refines the deformation using both anatomix- and segmentation-based losses. Lastly, because registration should not introduce non-biological tumor volume changes across time, we develop lesion-specific component-wise volume preservation schemes. Without any task-specific training, our system won first place in the PSMAReg Challenge leaderboard. Code and interactive visualizations are available at this http URL.

---


### 800. [Optimizing Team Behavior via Extremum-seeking Control in Multi-agent Reinforcement Learning](https://arxiv.org/abs/2610.18808)

**<font color=#1a73e8>作者：</font>** Svar Rajankumar Patel, Kshitij Jerath  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In cooperative Multi-Agent Reinforcement Learning (MARL), agents must learn to coordinate their actions to achieve shared objectives. A key indicator of effective coordination is behavioral diversity, i.e., the agents' potential to enact distinct yet complementary control policies given the same set of observations. Although behavioral diversity can enable role specialization and richer joint behaviors, its appropriate level is highly context- and task-dependent and often costly to tune. We propose Adaptive Diversity Control (ADiCo), a two-timescale framework that adapts behavioral diversity online during training. On a fast timescale, Diversity Control (DiCo) regulates system diversity toward a target value. On a slower timescale, an Extremum Seeking Controller (ESC) adjusts this target using only mean episodic returns, without requiring an explicit model or analytical gradient of the diversity-performance landscape. We evaluate ADiCo on six configurations across two cooperative MARL tasks, where it maintains task-appropriate diversity levels: low diversity when homogeneous policies are beneficial and higher diversity when heterogeneous policies are required. Through this adaptation, ADiCo matches or exceeds the mean performance of DiCo (best grid-searched diversity target) and Unconstrained DiCo (diversity allowed to emerge without target regulation). These results demonstrate that incorporating classical feedback control into MARL training enables effective coordination by providing a systematic alternative to task-specific manual selection of the diversity target.

---


> [!TIP]
> 当前位于：**751-800**（第 16/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | **751-800** | [801-810](./part-17.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
