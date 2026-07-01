# 📦 其他研究 | 2026年07月02日

> 本类共 **274** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-274](./part-06.md)

---

### 151. [RCL-Mamba: A Dual-domain State Space Model for Measurement-oriented Image Restoration in Rotational Sparse-View Scanning Computed Laminography](https://arxiv.org/abs/2606.31353)

**<font color=#1a73e8>作者：</font>** Xuyang Duan, Genyuan Zhang, Zhenjiang Dong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rotational Scanning Computed Laminography (RCL) is widely utilized for the Non-Destructive Testing(NDT) of large planar components. However, to facilitate rapid inspection, continuous sparse-view scanning is often employed, where the angular integration effect during exposure induces rotational blur in the projection domain. Furthermore, the data incompleteness inherent in sparse sampling manifests as sparse artifacts in the reconstructed image domain. To address these cross-domain degradations, this paper proposes RCL-Mamba, a measurement-oriented dual-domain State Space Model (SSM)-based image restoration network. The framework adopts a cascaded joint processing strategy: it first corrects the rotational blur in the projection domain and subsequently suppresses the sparse artifacts in the image domain. Additionally, we design a Mamba-CNN dual-branch module to adaptively balance large-scale blur correction with local detail recovery. Evaluations on both simulated datasets and real-world Printed Circuit Board (PCB) scans demonstrate that RCL-Mamba outperforms existing baselines in blur removal, artifact suppression, and structural preservation. Line-profile-based structural measurement further verifies that the proposed method better preserves via/pad boundaries and slender trace profiles. Crucially, by reducing the required scanning views from 512 to 64, our method enhances inspection efficiency by approximately 8-fold without compromising reconstruction quality, offering a robust measurement-oriented restoration solution for high-throughput RCL inspection with improved structural measurement fidelity.

---


### 152. [Language-Assisted Super-Resolution from Real-World Low-Resolution Patches](https://arxiv.org/abs/2606.31363)

**<font color=#1a73e8>作者：</font>** Joonkyu Park, Kyoung Mu Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single image super-resolution aims to reconstruct high-resolution (HR) images from low-resolution (LR) inputs. Training SR models typically requires paired HR-LR data, which is difficult to obtain in reality. As a result, most methods synthesize LR images by artificially degrading HR images with handcrafted kernels or camera ISP adjustments. However, these synthetic degradations fail to capture the complexity of real LR images, leading to poor generalization in practice. To address this, we observe that even within a single high-quality image, regions at different depths exhibit varying resolutions, where distant regions act as LR patches and closer ones as HR patches. This allows the extraction of real, degradation-induced LR patches from real images. Since these LR patches lack paired HR counterparts, we propose LA-SR (Language Assistant for SR), a novel framework for unpaired SR. The key idea of LA-SR is to redefine unpaired SR in the language space, using vision-language models to bridge the LR-HR gap. LA-SR projects images into a semantically rich space representing both content and quality, and applies two language-guided losses: linguistic content loss to preserve semantic fidelity, and linguistic quality loss to enhance perceptual realism. With this alignment, LA-SR effectively super-resolves real LR inputs, producing realistic outputs that overcome the limitations of synthetic-data-trained methods.

---


### 153. [Witness Complexity of Short Descriptions: A Cryptographic Perspective](https://arxiv.org/abs/2606.31370)

**<font color=#1a73e8>作者：</font>** Fabio F.G. Buono  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In cryptographic practice, where protocols impose strict time bounds, implementations demand predictable resource usage, and real-world systems require immediate verification for security and usability, a short key or certificate is useful only if it can be expanded or verified within a bounded time; otherwise a compact representation that requires superpolynomial work to expand offers no operational guarantee within a bounded-time protocol. This paper formalises that gap by introducing \emph{witness complexity} \(\gam(x)\), the minimum running time over near-shortest descriptions of a string on a universal Turing machine. \(\gam\) differs from Shannon entropy and Kolmogorov complexity \(\KC\): low \(\KC\) can coexist with high \(\gam\). We prove invariance up to polynomial factors; a conditional separation (assuming \(\PneqNP\)). An unconditional lower bound from incomputability of \(\KC\); a biconditional characterisation of \(\PeqNP\) via the class-relative variant \(\gP\); and polynomial-time tractability for structured \(\classNP\) families. Part II develops companion measures and shows an unconditional gap between grammar size and derivation cost, positioning \(\gam\) as a metric for the usability of keys and certificates.

---


### 154. [Domain Adaptive Object Detection via Dual-Stream Bilevel-Cycle Optimization](https://arxiv.org/abs/2606.31373)

**<font color=#1a73e8>作者：</font>** Yannan Chen, Wei Wang, Wenqiang Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cycle self-training (CST) breaks the shared classifier assumption of the standard self-training framework, which is effective for unsupervised domain adaptation and exploits unlabeled target data by training with target pseudo-labels. CST introduces a target classifier and employs an inner-outer loop updating strategy, addressing the issue of unreliable pseudo-labels and enabling pseudo-labels to generalize across domains. Despite its success in image classification, extending CST to object detection faces three main challenges. First, the upper bound of CST in object detection is constrained by three types of unreliable pseudo-labels, such as classification error alone, localization error alone, and their combination. Second, since object detection involves detecting multiple target objects, directly applying CST leads to training insta bility. Third, a wider numerical range of regression coordinates leads to exploding losses. To this end, we apply CST to both classification and regression and propose the Dual-Stream Bilevel-Cycle Optimization framework. Specifically, we construct CST upon Mean Teacher to prevent training instability and use extra normalization to map the regression bounding box into a standardized space, effectively addressing exploding losses. Also, we provide a theoretical derivation of the regression bound. Extensive experiments across four cross domain standard scenarios demonstrate that our framework achieves considerable results.

---


### 155. [MAPE: Defending Against Transferable Adversarial Attacks Using Multi-Source Adversarial Perturbations Elimination](https://arxiv.org/abs/2606.31378)

**<font color=#1a73e8>作者：</font>** Xinlei Liu, Jichao Xie, Tao Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neural networks are vulnerable to meticulously crafted adversarial examples, leading to high-confidence misclassifications in image classification tasks. Due to their consistency with regular input patterns and the absence of reliance on the target model and its output information, transferable adversarial attacks exhibit a notably high stealthiness and detection difficulty, making them a significant focus of defense. In this work, we propose a deep learning defense known as multi-source adversarial perturbations elimination (MAPE) to counter diverse transferable attacks. MAPE comprises the single-source adversarial perturbation elimination (SAPE) mechanism and the pre-trained models probabilistic scheduling algorithm (PPSA). SAPE utilizes a thoughtfully designed channel-attention U-Net as the defense model and employs adversarial examples generated by a pre-trained model (e.g., ResNet) for its training, thereby enabling the elimination of known adversarial perturbations. PPSA introduces model difference quantification and negative momentum to strategically schedule multiple pre-trained models, thereby maximizing the differences among adversarial examples during the defense model's training and enhancing its robustness in eliminating adversarial perturbations. MAPE effectively eliminates adversarial perturbations in various adversarial examples, providing a robust defense against attacks from different substitute models. In a black-box attack scenario utilizing ResNet-34 as the target model, our approach achieves average defense rates of over 95.1\% on CIFAR-10 and over 71.5\% on Mini-ImageNet, demonstrating state-of-the-art performance.

---


### 156. [One Video, One World: Turning Monocular Video into Physical 4D Scenes](https://arxiv.org/abs/2606.31388)

**<font color=#1a73e8>作者：</font>** Junhao Chen, Boran Zhang, Mingjin Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce \textbf{OVOW}, the first training-free system that reconstructs \emph{instance-level, simulation-ready} 4D mesh scenes from a single monocular video. Recent 4D reconstruction achieves impressive rendering quality, but its outputs (\eg, implicit fields, Gaussian primitives, or point clouds) lack the watertight topology, instance separation, and standardized physical interfaces required by physics simulators and embodied AI. OVOW closes this gap with a four-stage pipeline: a vision-language model discovers, labels, and motion-classifies all instances; category-aware reconstruction yields per-instance meshes for rigid objects and topology-consistent mesh sequences for deformable ones; an iterative render-match-optimize procedure recovers metric scale and 6-DoF pose trajectories; and physics-grounded assembly enforces ground contact and inter-object support. Crucially, we model all motion, rigid and non-rigid, through direct vertex deformation without category-specific priors or skeleton rigging, producing watertight mesh scenes ready for downstream physics simulation and editing. We further establish the first benchmark for \emph{structured Video-to-4D} evaluation, with metrics for geometric correctness, instance separation, and physical plausibility beyond visual fidelity; the same pipeline doubles as a scalable engine for \emph{synthesizing} paired video-to-4D simulation data for future 4D world models and embodied AI. Across two synthetic benchmarks (static and 4D), OVOW attains the best overall layout and geometry accuracy and the lowest photometric and semantic error among all baselines, and on monocular video runs one to two orders of magnitude faster than the baselines, while downstream physics simulation confirms its physical stability.

---


### 157. [Resolving superposition in AI for interpretability and cross-modal alignment in patient-neuronal images](https://arxiv.org/abs/2606.31394)

**<font color=#1a73e8>作者：</font>** Jisung Park, Seohyeon Kang, Daeun Yoo 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence is transforming our capability to solve biological challenges. In dimensionality bottleneck regimes exacerbated by high-dimensional biological data, Neural networks force distinct concepts into the lower dimensions known as superposition. Although this superposition is widely known to hinder interpretability, its impact on corrupting the geometry of latent spaces remains critically overlooked. Here, we utilized sparse autoencoders (SAEs) trained on over 100,000 multiplexed images of patient-derived Parkinson's disease and healthy neurons to resolve superposition. This approach bypasses the mathematical non-uniqueness of feature attribution by shifting to interpretable latent representation analysis. We theoretically and empirically demonstrate that superposition contaminates representational metric spaces, and thereby SAEs successfully recover geometric fidelity. By treating these geometrically purified representations as single-cell state vectors, we adapted single-cell RNA sequencing (scRNA-seq) data analysis methodologies directly to the image domain. Finally, we introduce GW-map, utilizing Gromov-Wasserstein optimal transport to align these image representations with authentic scRNA-seq data \emph{de novo}. This coupling reconstructs hierarchical neuronal pathology pathways such as Calcium-AIS scaffold, without reference spatial transcriptomics, establishing a scalable foundation for spatial biology. Code is available at this https URL

---


### 158. [World-Model Collapse as a Phase Transition](https://arxiv.org/abs/2606.31399)

**<font color=#1a73e8>作者：</font>** Xinyuan Song, Zekun Cai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Water looks unchanged as it warms, then at a critical point it boils. We ask whether long-horizon language agents show an analogous transition in their implicit world models. In some parameter settings, changing state load by a small amount, or adding a single step of horizon, leaves behavior nearly unchanged; near a critical boundary, the same small change causes a sudden world collapse. We study this effect in a deterministic task family with exact per-step gold state. A large grid search over state cardinality, dependency density, horizon, branching, observation mode, and mutation rate reveals a phase diagram: a solved plateau, a narrow transition band, and a collapse floor. Per-step traces show the mechanism: world-state fidelity fails before action validity, so the agent is not merely choosing a bad action; it is acting from a corrupted world. Stronger models translate the critical boundary but do not remove the qualitative transition. These results make world-model collapse a measurable bottleneck for long-horizon agents.

---


### 159. [Linguistic Bias Mitigation for Spoofing Detection via Gradient Reversal and A Variational Information Bottleneck](https://arxiv.org/abs/2606.31411)

**<font color=#1a73e8>作者：</font>** Anh-Tuan Dao, Driss Matrouf, Mickael Rouvier 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rapid advancements in generative speech technology have compromised the reliability of voice biometrics. While current spoofing detectors excel when assessed under in-domain conditions, generalisation to out-of-domain settings is often poor. We show that this can be due to linguistic bias. A reliance on linguistic cues observed in training data can then compromise robustness to cross-data. We propose a linguistic-invariant spoofing detection framework utilizing teacher-student adversarial learning. The linguistic-aware teacher model, pre-trained on linguistic content of an external dataset, guides the student detector via gradient reversal to minimize the linguistic information. To prevent the inadvertent removal of non-linguistic cues, we incorporate a Variational Information Bottleneck to enable suppression of principal cues. Across nine DF Arena datasets, our method achieves up to a 36.2% relative reduction in the EER compare to the baseline.

---


### 160. [Learning to Select, Not Relearn: Hard-Routed Mixtures of Reasoning LoRAs](https://arxiv.org/abs/2606.31413)

**<font color=#1a73e8>作者：</font>** Seyed Alireza Molavi, Zhan Su, Yan Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Composing independently trained LoRA adapters into a single large language model is useful for multi-domain adaptation, especially when the original training data cannot be shared. A common approach is to use MoE-style routing over LoRA experts, but for frozen pretrained adapters, soft weighted combinations can change the unit-scale additive update under which each LoRA module was originally trained. We propose \textbf{Hard-Routed MoR-LoRA}, a two-stage framework for composing frozen reasoning LoRA experts through unit-scale hard selection. First, domain-specific LoRA adapters are trained independently using reinforcement learning from verifiable feedback to obtain reasoning experts. Then, all experts are frozen, reasoning traces are distilled from them, and only a lightweight shared router together with a small attention LoRA is trained for integration. The router selects exactly one expert per token using hard top-1 routing, while a straight-through estimator enables gradient-based training. Experiments across five benchmarks, multiple model scales, and additional model families show that Hard-Routed MoR-LoRA preserves expert behavior while requiring substantially fewer trainable parameters than soft-routing mixture baselines. Our analysis further shows that normalized soft mixtures often concentrate most routing mass on a single expert, suggesting that hard unit-scale routing provides a simple and efficient abstraction for frozen LoRA expert composition.

---


### 161. [BP-TTA: Balanced and Prototype-Guided Test-Time Adaptation in Dynamic Scenarios](https://arxiv.org/abs/2606.31420)

**<font color=#1a73e8>作者：</font>** Shaoyang Huang, Yashi Zhu, Yichen Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Test-Time Adaptation (TTA) enables models trained on a source domain to adapt online to unlabeled test data under distribution shifts. While recent TTA methods have moved beyond static settings and begun to consider continual domain shifts, they primarily address distribution drift and fail to account for class imbalance in dynamic scenarios. In real-world test-time streams, class imbalance and continual domain shifts often occur at the same time and interact with each other. In this paper, we propose a novel Balanced and Prototype-Guided Test-Time Adaptation (BP-TTA) method, which combines batch-balanced sampling with prototype-guided adaptation to handle the class imbalance and continual domain shift problems. BP-TTA constructs balanced adaptation batches by integrating current samples with high-confidence historical instances, effectively mitigating bias toward dominant classes and stabilizing online updates. Meanwhile, BP-TTA maintains evolving class prototypes during inference and leverages prototype similarity as a constraint for model adaptation, thereby improving the reliability of pseudo-labels and enhancing the stability of online updates under persistent domain shifts. Extensive experiments demonstrate that BP-TTA consistently outperforms state-of-the-art TTA methods in dynamic test-time streaming settings.

---


### 162. [Temporal Preservation over Processing: Diagnosing and Designing Spatiotemporal Single-Stage Video Detectors](https://arxiv.org/abs/2606.31421)

**<font color=#1a73e8>作者：</font>** Karam Tomotaki-Dawoud, Anna Hilsmann, Peter Eisert 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-stage video object detectors are increasingly deployed in time-critical applications, yet it remains unclear whether these models genuinely reason over temporal context or merely exploit a single informative frame-a gap hidden by standard metrics, which reward correct predictions regardless of how they are reached. We address this from two complementary directions: first, we propose TemporalLens, a model-agnostic diagnostic framework probing temporal dependence through controlled perturbations, structured occlusions, temporal shuffling, redundancy injection, and resolution degradation, revealing whether a detector actually uses information across time. Applied to stacked-frame 2D detectors and our YOLO-3D architecture, it exposes behavioural differences invisible to mAP: stacked 2D models collapse when the target frame is removed, while spatiotemporal models recover predictions from earlier frames, a signature of real temporal reliance. Second, we detail YOLO-3D, a modular real-time spatiotemporal detector built on YOLOv8, and show that simply preserving temporal depth through the backbone is the dominant performance driver (+3.7 pp mAP@50 at 32 frames averaged across scales). Together, the diagnostics and architecture turn "does this detector reason over time?" into a measurable, actionable question.

---


### 163. [Ask the World Before Acting: Budgeted Environment Probing for World-Model Calibration](https://arxiv.org/abs/2606.31422)

**<font color=#1a73e8>作者：</font>** Xinyuan Song, Zekun Cai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon language agents do not only choose actions; they carry a private model of the world from one decision to the next. When that model drifts, a later failure can be decided before the failing action is ever taken. We study a direct repair mechanism: before committing to the next task action, an agent may ask the environment about one belief field and write the answer back into its world model. This makes environment interaction a scarce calibration resource, not merely a way to advance the task. We introduce \method, a budgeted probing operator for structured belief tables. The useful probes are not the same everywhere. Procedural beliefs, such as tool dependencies, can often be repaired by targeted checks, but those checks spend steps that the task may need. Spatial beliefs, such as object locations and graph edges, rely more on structural cues; the agent's own confidence can be a poor guide when the world changes off-screen. A type-stratified analysis formalizes this probe-action frontier, and controlled experiments show that mid-planning environment evidence reduces terminal world-model error when the probe policy follows the structure of the task.

---


### 164. [No Prompt, No Leaks: A Robust Generative Steganography Framework via Prompt-Free Diffusion](https://arxiv.org/abs/2606.31427)

**<font color=#1a73e8>作者：</font>** Jingwen Cai, Fen Xiao, Shuhua Deng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative image steganography synthesizes stego images directly from secret information to achieve inherent security advantages. Latent Diffusion Models (LDMs) have recently emerged as a fundamental image steganography framework that modulates secret latent representations with text prompts. Limited by the inflexibility of text prompts, these methods still struggle to generate high-quality stego images and accurately recover secret images. In this work, we propose a prompt-free diffusion image steganography framework that integrates style semantic priors to control more robust and reliable stego image generation. Specifically, a Cascaded Affine Coupling Module (CACM) establishes a bijective, deterministic mapping between a secret image and its latent representation. Then, style semantics are integrated into the diffusion process to control latent representation and ensure visual imperceptibility in the generated stego images. To mitigate trajectory deviations stemming from the unconditioned reverse process, a predictor-corrector mechanism is introduced to iteratively refine the generation trajectory via feedback from the current and predicted next states. Extensive experimental results show that the proposed method achieves competitive performance compared to state-of-the-art methods in terms of security, secret image reconstruction accuracy and controllability.

---


### 165. [Clinically Structured Rank-Gated LoRA for Cross-Benchmark Medical Question Answering](https://arxiv.org/abs/2606.31432)

**<font color=#1a73e8>作者：</font>** Yining Huang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medical multiple-choice question answering requires parameter-efficient adaptation across heterogeneous knowledge domains and reasoning operations. A medication question, a diagnostic decision, a public-health item, and a nursing-action item may require different low-rank updates, while some recall items should preserve the base model's representation with only mild adapter intervention. We propose BiRG-LoRA, a single-adapter rank-gated LoRA method for medical question answering. BiRG-LoRA keeps one LoRA module per target layer but makes its rank dimension input-conditioned: for each question, a biaxial gate combines hidden semantic evidence with specialty/profession priors, clinical-operation priors, and their interaction to select a sparse top-$k$ subset of rank atoms. A scalar injection coefficient further controls the strength of the selected adapter update. Under a matched Qwen3-8B CMB-source protocol, BiRG-LoRA achieves the highest four-benchmark macro-average accuracy among trainable PEFT baselines and matched routing controls: 69.31% averaged over CMB, CMExam, MedQA, and MedMCQA. It improves over MoELoRA by 0.89 percentage points while using 28.1% fewer trainable parameters; a paired, benchmark-stratified bootstrap over final predictions gives a 95% confidence interval of [0.42, 1.37] for this macro-average gain. Basic controls show that BiRG-LoRA also improves over vanilla LoRA r16 and active-rank-matched LoRA r4 by 0.83 macro points, and an evaluation-time weak-axis perturbation check suggests that performance is not brittle to moderate tag noise. The results support a bounded claim: clinically structured rank allocation improves cross-benchmark medical QA under a matched single-seed protocol, while training-seed variance remains future work.

---


### 166. [CDR-Bench: Evaluating Faithful Execution of Compositional, Order-Sensitive Data Refinement Recipes](https://arxiv.org/abs/2606.31435)

**<font color=#1a73e8>作者：</font>** Yuchen Huang, Xiang Li, Zhenqing Ling 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Data refinement involves executing multi-step recipes over evolving text states, where both composition and execution order of processing operators determine the outcome. While existing benchmarks either isolate text editing or entangle it with code and tool execution, it remains unclear whether LLMs can directly and faithfully execute these compositional, order-sensitive data refinement recipes. To fill this gap, we introduce CDR-Bench, a comprehensive benchmark featuring 3,462 high-quality tasks spanning four real-world data refinement domains and 29 distinct operators. Our benchmark evaluates models across atomic, order-agnostic, and order-sensitive settings, leveraging deterministic reference outputs to enable exact evaluation. Experiments on 10+ state-of-the-art LLMs reveal consistent failure patterns: performance degrades sharply in compositional settings, and order-sensitive recipe success collapses. These findings underline that current LLMs lack the procedural faithfulness required for reliable compositional data refinement.

---


### 167. [Who Determines the Meaning of an Emotion? Affective Sovereignty as an Epistemic Consequence of Measurement Limits](https://arxiv.org/abs/2606.31442)

**<font color=#1a73e8>作者：</font>** Keito Inoshita  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Emotion-sensing AI is rapidly becoming embedded in vehicles, home appliances, dialogue agents, and social infrastructure, giving rise to a sphere in which emotion is no longer confined to individual experience but is instead observed and computed at a societal scale, a domain we term the Affectosphere. Yet a central normative question in this domain has remained underexplored: who has the final authority to determine the meaning of one's own emotion? This study addresses the question from the epistemological side of measurement's structural limits. We define a meaning distribution as the distribution of labels assigned by annotators drawn from a population under a fixed annotation protocol, and decompose its uncertainty into reducible and irreducible components. We then demonstrate that, while emotion AI can assign high-confidence point labels and discriminate real differences at an aggregate level, the irreducible component of the meaning distribution for individual instances cannot be estimated with adequate coverage under realistic annotator counts, a systematic divergence we term the epistemic gap. The key finding is that high device confidence does not constitute evidence that irrecoverable meaning has been recovered. From this epistemic gap, together with an explicitly stated normative premise, namely that the output of a system which cannot recover a quantity in principle must not be treated as its authoritative determination, we derive the norm that the final interpretive authority over the meaning of one's emotion is procedurally reserved for the experiencing subject, the norm of affective sovereignty. These results suggest that the design, evaluation, and regulation of emotion AI should place explicit allocation of interpretive authority, rather than accuracy maximisation, at their core.

---


### 168. [Temporal Training Strategies for Left Atrium and Left Atrial Appendage Segmentation in Dynamic Contrast 4DCT](https://arxiv.org/abs/2606.31444)

**<font color=#1a73e8>作者：</font>** David Montalvo-García, Lauren Severance, Elliot R. McVeigh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic contrast-enhanced cardiac CT enables time-resolved analysis of contrast filling and washout in the left atrium (LA) and left atrial appendage (LAA), with potential applications for assessing blood stasis in atrial fibrillation (AF). Accurate segmentation across all frames is required for such analysis but is challenging due to large temporal contrast variations and the use of a single annotation per registered sequence. This creates a trade-off between training for robustness and limiting label noise. In this study, we investigate how temporal training-set design affects nnUNet-based segmentation of the LA and LAA in dynamic 4DCT. We compare training using a minimal two-frame dataset reflecting standard clinical practice, a physiologically selected subset of frames, and the full 27-frame sequence. We further evaluate the impact of foreground-based normalization. Training with all frames yielded the best performance in early low-contrast phases. However, the physiologically selected subset achieved comparable performance from the filling phase onward. Applying normalization parameters derived from the full dataset improved performance of reduced datasets in low-contrast frames, but did not fully close the gap. These findings highlight the importance of temporal diversity in training data for robust segmentation in dynamic CT, while indicating that carefully selected frame subsets may provide an effective trade-off between performance and efficiency for downstream applications.

---


### 169. [Revising RVL-CDIP: Quantifying Errors and Test-Train Overlap](https://arxiv.org/abs/2606.31446)

**<font color=#1a73e8>作者：</font>** Stefan Larson, Attila Nagy, Sam Desai 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> RVL-CDIP is a popular dataset for benchmarking document classifiers. However, the dataset contains ample amounts of label errors as well as non-trivial amounts of test-train overlap, both of which may impact model performance metrics. In this paper, we address these two problems by (1) finding and fixing label errors, and (2) detecting and addressing test-train overlap. We produce several variations of RVL-CDIP with label error and test-train overlap fixes, and benchmark document classification performance on these new RVL-CDIP variations. Our rigorous analysis of RVL-CDIP finds that the corpus contains 12\% label error and approximately 35% test-train duplication. Remediation sees improvements in classification accuracy when errors are removed, but sees decreases in accuracy when duplicates are removed. We additionally evaluate models on RVL-CDIP-N, an out-of-distribution benchmark, finding that training on error-corrected data substantially improves OOD generalization, with supervised models gaining an average of 8.1 percentage points in accuracy and improvements as large as 14 percentage points.

---


### 170. [Contextual Slate GLM Bandits with Limited Adaptivity](https://arxiv.org/abs/2606.31449)

**<font color=#1a73e8>作者：</font>** Tanmay Goyal, Sukruta Prakash Midigeshi, Gaurav Sinha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate the contextual slate bandit problem with generalized linear rewards under limited adaptivity. At each round, the learner is presented with $N$ sets of items, where each item is represented by a $d$-dimensional feature vector. The learner then constructs a slate by selecting one item per set; the resulting slate yields a scalar reward sampled from a Generalized Linear Model (GLM). We propose algorithms under two limited-adaptivity settings: (a) Batched and (b) Rarely-Switching. For the batched setting, we introduce B-SlateGLinCB, which partitions the time horizon into $\mathcal{O}(\log\log T)$ batches such that each batch's policy relies only on data from previous batches. For the rarely-switching setting, we propose RS-SlateGLinCB, which adaptively performs only $\mathcal{O}(Nd\log T)$ parameter updates. Under a diversity assumption on the item sequences, we prove that B-SlateGLinCB and RS-SlateGLinCB achieve regret bounds of $\mathcal{O}(Nd^{3/2}\sqrt{T})$ and $\mathcal{O}(Nd\sqrt{T})$, respectively. Notably, both bounds are independent of the non-linearity parameter $\kappa$ that is typically found to scale the regret of GLM bandit algorithms. Our algorithms are computationally efficient, requiring only $\text{poly}(N)$ time per round despite $2^{\Omega(N)}$ possible slates. Simulations show our algorithms outperform existing baselines with limited adaptivity and remain competitive with Slate-GLM-OFU, a fully adaptive state-of-the-art algorithm. Notably, a slightly modified B-SlateGLinCB empirically matches this baseline. Finally, we demonstrate strong performance in a practical in-context example selection task for language models.

---


### 171. [Towards a foundational model for recognising diastematic Gregorian notation](https://arxiv.org/abs/2606.31454)

**<font color=#1a73e8>作者：</font>** Daniel Kurek, Jan Hajič jr  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical recognition of Gregorian notation has recently been attempted with end-to-end methods, with four datasets introduced. However, each of these datasets is in a different encoding. We design a common encoding based on the S-GABC proposal, convert all four datasets to this common encoding, and train a shared end-to-end foundational model for diastematic Gregorian notation that establishes a new state of the art across all four datasets.

---


### 172. [Zero-Shot Quantization for Object Detectors using Off-the-Shelf Generative Models](https://arxiv.org/abs/2606.31456)

**<font color=#1a73e8>作者：</font>** Hyunho Lee, Kyomin Hwang, Hyeonjin Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With an increasing number of Object Detection (OD) models being deployed on edge devices, Zero-Shot Quantization for OD (ZSQ-OD) aims to quantize these models when access to the original training data is prohibited. Existing research on Zero-Shot Quantization-Aware Training (QAT) for OD synthesizes training sets through noise optimization. However, this approach struggles to maintain performance in low-bit regions. In this paper, we introduce GoodQ (Generative off-the-shelf models for object detector Quantization), a QAT pipeline that utilizes off-the-shelf generative models to construct a training set. We first identify three challenges that arise when introducing a generative model to the ZSQ-OD task: 1) each image contains dense information with multiple instances, 2) the class-wise distribution in the original dataset is imbalanced, and 3) the pseudo-labels assigned to the generated images can potentially act as noisy signals during QAT. GoodQ addresses these challenges by 1) introducing an Information-Dense Prompting strategy to generate multi-instance images, 2) applying Intrinsic Distribution-Aware Selection to match the pretrained class distribution, and 3) employing Teacher-guided Adaptive Noise Reduction to mitigate noise arising from the QAT process. Our framework achieves state-of-the-art performance in low-bit ZSQ (W4A4) and extends quantization to extreme bit-widths (W3A3). Furthermore, we conduct an extensive analysis to uncover the underlying factors contributing to the efficacy of GoodQ.

---


### 173. [CSTrader: A Testbed for Language-Grounded Trading in a Community-Driven Virtual Asset Market](https://arxiv.org/abs/2606.31461)

**<font color=#1a73e8>作者：</font>** Yao Shi, Kingfung Luo, Nan Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Niche asset markets, such as Counter-Strike 2 (CS2) weapon skins, are small, volatile, and heavily driven by community discussions and platform rules. These properties make them hard for traditional quantitative models, but provide an ideal testbed for studying how large language models (LLMs) turn unstructured text into trading actions. We present CSTrader, a multi-agent framework for language-grounded trading in the CS2 skin market. The system first integrates heterogeneous signals from various sources, then uses specialized agents for technical analysis, liquidity, events, and (reversed) sentiment, and finally applies risk control, transaction friction, and portfolio management agents to produce buy, sell, or hold decisions under realistic trading frictions. We build a live-like evaluation environment with real CS2 data from a highly volatile period and evaluate several recent LLM backbones. Across models, CSTrader consistently outperforms both a falling market index (-15.62%) and simple single-prompt LLM baselines, achieving up to a 7.58% cumulative return with controlled risk. Ablation studies show that liquidity, reversed sentiment, and transaction friction agents are crucial for turning noisy language signals into stable profits, suggesting that niche, language-driven markets are a useful benchmark for future language-to-action research. Code is available at: this https URL

---


### 174. [A forgery attack on the Block.co blockchain-based digital credential certification system](https://arxiv.org/abs/2606.31462)

**<font color=#1a73e8>作者：</font>** Giacomo Zonneveld, Giulia Rafaiani, Marco Baldi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Certification of digital documents, such as academic credentials, seems a particularly suitable application for the use of blockchain and distributed ledger technologies. Indeed, these technologies enable decentralized certification systems that rely on the immutability and persistence of their distributed ledgers. However, in the absence of a central trusted authority, it is not easy to guarantee the authenticity of the connection between the real identity of an academic institution and the digital identity of the certificate issuer. In this paper, we demonstrate that one of such systems, known as this http URL, has a vulnerability that allows the production of forged certificates that are recognized as valid by the system. Since this is an inherent limitation of the approach used for blockchain-based certification, our attack is likely to be extendable to other systems adopting the same approach.

---


### 175. [Think While You Map: Asynchronous Vision-Language Agents for Incremental 3D Scene Graphs](https://arxiv.org/abs/2606.31471)

**<font color=#1a73e8>作者：</font>** Deniz Bickici, Michael Pabst, Shohei Mori 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary 3D scene graph methods typically operate in two stages: first reconstruct, then enrich with vision-language models, leaving the graph unqueryable during exploration. We argue that this sequential coupling is unnecessary and propose an asynchronous architecture in which lightweight online mapping runs concurrently with heavyweight semantic refinement. A probabilistic voxel-based backbone maintains stable object identities incrementally, while background VLM agents progressively enrich the graph. This framework resolves duplicate object tracks through semantic loop closure, attaches fine-grained visual attributes and derives spatial relations between objects. A multi-target frame scheduler amortizes VLM cost by selecting a small set of informative frames that jointly cover multiple targets. The resulting scene graph is queryable during exploration and grows in semantic richness over time. Our method matches or outperforms existing open-vocabulary 3D scene graph methods on semantic segmentation (ScanNet, Replica) and surpasses the prior state-of-the-art across three visual grounding benchmarks (Sr3D+, Nr3D, ScanRefer) by 15.3 to 18.8 A@0.25. Project page: this https URL

---


### 176. [One Reflection Is Not Enough: Self-Correcting Autonomous Research via Multi-Hypothesis Failure Attribution](https://arxiv.org/abs/2606.31478)

**<font color=#1a73e8>作者：</font>** Jie Ma, Binfei Chu, Jie Gao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous research agents can now draft hypotheses, write code, run experiments, and produce papers, but they remain brittle when experiments fail. Under the prevailing paradigm, failure recovery is usually delegated to a single free-form reflection: a rich trajectory of metrics, logs, and design choices is compressed into one verbal critique, which often leads either to localized trial-and-error or to hard pivots that discard useful context. We propose SAGE, a Self-correcting, Autonomous, Grounded Experimenter, to tackle this failure-recovery bottleneck. Its core mechanism, Multi-Hypothesis Failure Attribution (MHFA), treats recovery as a structured causal diagnosis. By analyzing dynamic trajectory features, MHFA systematically generates multiple evidence-grounded explanations for a failure, independently evaluates their severity, and deterministically routes the verified root cause to the correct intervention level (hypothesis, experimental design, or implementation). To guarantee scientific honesty, SAGE further employs a grounded reporting mechanism that explicitly constrains drafted results to actual measured values, redacting hallucinated numbers. On a 12-topic, 5-domain benchmark, SAGE increases metrics-bearing outputs from 42% to 92% over a reflection baseline, improves artifact quality from 5.00 to 6.75/10, and blindly outscores AI-Scientist-v2 (52.0 vs. 48.2), with gains concentrated in code development and execution. While fully autonomous scientific writing and generating conference-ready papers remain notoriously difficult open problems for the entire field, SAGE successfully produces significantly more reliable and higher-quality scientific artifacts. Ultimately, by coupling structured recovery with explicit grounding constraints, SAGE significantly outperforms monolithic reflection paradigms, establishing a highly trustworthy foundation for future autonomous research.

---


### 177. [Constrained Online Convex Optimization without Slater's Condition](https://arxiv.org/abs/2606.31480)

**<font color=#1a73e8>作者：</font>** Kihyun Yu, Junehee Lee, Dabeen Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study constrained online convex optimization with adversarial losses and stochastic or adversarial constraints. For stochastic constraints, existing algorithms that achieve nearly optimal regret and constraint violation bounds typically rely on regularity assumptions such as Slater's condition, while adversarial-constraint algorithms avoid these assumptions by using a rather restrictive round-wise feasible comparator. We bridge this gap with an anytime primal-dual framework that incorporates an adaptive regularizer into the dual update. The regularizer stabilizes the dual process without relying on the negative drift induced by Slater's condition. For stochastic constraints and convex losses, our algorithm achieves $O(\sqrt{T})$ expected regret and $O(\sqrt{T}\log T)$ expected cumulative constraint violation. Furthermore, we show that our algorithm also admits high-probability bounds of the same order on regret and constraint violation. For strongly convex losses, the regret bound improves to $O(\log T)$ with a violation bound of the same order. With a minor modification, the framework also applies to adversarial constraints and provides guarantees for hard constraint violation.

---


### 178. [Fork-Think with Confidence](https://arxiv.org/abs/2606.31484)

**<font color=#1a73e8>作者：</font>** Zena Al-Khalili, Rafi Hakim, Dietrich Klakow 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parallel thinking has enjoyed great success for boosting LLM performance on reasoning tasks without the need for any re-training. However, existing methods follow a think-first-then-decide paradigm, i.e., they first sample multiple reasoning paths, which inevitably leads to overgeneration, then prune or stop unnecessary paths to compensate. In contrast, decide-first-then-think, i.e., first identifying points that are likely to lead to desirable generations, has been underexplored so far. Following this paradigm, we propose Fork-think with confidence, that first identifies forking points using model confidence in a single seeding path, then triggers thinking, sampling multiple continuations and aggregating them for the final response. Our experiments across three models and three reasoning benchmarks show that Fork-think reduces the token consumption by up to 30% and run-time by up to 57%, while performing comparable to or better than parallel thinking. Our analysis reveals that Fork-think is able to identify forking points that are meaningful with respect to the downstream task and that sampling at later positions can lead to substantially better generations. Finally, we demonstrate how combining Fork-think with existing mechanisms such as early stopping and weighted voting can further boost the performance and perform comparably to existing state-of-the-art methods, without requiring any warm-up or offline training. Our results establish pre-determined forking as a promising research direction for efficient LLM reasoning.

---


### 179. [DrivingDepth: Sparse-Prompted Pixel-wise Scale Correction for Driving Depth Estimation](https://arxiv.org/abs/2606.31488)

**<font color=#1a73e8>作者：</font>** Chi Huang, Wenhao Zhang, Hang Yin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dense depth estimation for autonomous driving faces a geometry-scale conflict: depth foundation models deliver pixel-aligned dense visual geometry without reliable metric scale, while projected LiDAR provides metric anchors that are sparse, noisy, and misaligned with image structures. Existing sparse-prompted methods incorporate LiDAR by regenerating depth from scratch, overriding the foundation model's coherent geometry and producing structural artifacts on visually continuous surfaces. Our key insight is that foundation models already capture geometrically coherent relative depth; no additional surface structure learning is required-only a per-pixel scale factor mapping relative geometry to metric coordinates. Based on this, we propose DrivingDepth, which treats sparse LiDAR as geometric prompts that locally calibrate a frozen foundation prior through residual pixel-wise scale correction, preserving dense visual geometry by construction. On nuScenes with 4-frame surround-view input, DrivingDepth achieves an AbsRel of 11.19 and an EdgeCR of 5.741, outperforming MapAnything (11.99/1.914) by simultaneously delivering SOTA metric accuracy and geometric consistency.

---


### 180. [Surprise as a Signal for Plasticity and Metacognition](https://arxiv.org/abs/2606.31495)

**<font color=#1a73e8>作者：</font>** Louis Mouchon  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study a single idea across two settings: that a prediction-error signal, computed by a small predictor over the latent space of a frozen encoder, can serve both as a gate on plasticity and as a substrate for metacognition. In the first system, a non-parametric episodic memory writes a new concept only when this surprise is high, and a periodic offline replay phase consolidates recent traces into a slow linear readout. On a continual stream of 1000 ImageNet classes with a frozen DINOv2 or I-JEPA backbone, the consolidation phase recovers 17.7 points of retention on the oldest classes for DINOv2 and 51.3 points for I-JEPA (single-seed runs), and an ablation shows that replaying only a recent window is worse than no replay at all. In few-shot evaluation the same memory reaches 91.6% on 5-way 1-shot mini-ImageNet, above a task-specific baseline, while a harder 500-way regime exposes the true difficulty. In the second system, the same surprise signal, computed in a shared text-image space, modulates the behaviour of a vision-language model: it answers assertively when a concept is known, hedges when it is partially familiar, and refuses to identify the object and asks for an explanation when it is novel, learning the concept from a single user utterance. The external detector separates known from novel concepts at an AUROC of 0.966 (95% CI +/-0.024), far above the model's own verbalised confidence (0.618), while its token-level confidence sits below chance under greedy decoding; after a sleep phase that empties the fast store, the system recalls 99.2% of fifty taught facts from the consolidated store while a base model recovers none. We report both systems as proof-of-concept, with explicit limitations, and position the second against recent episodic-memory and personalised-VLM work.

---


### 181. [HVPNet: A Bio-Inspired Network for General Salient and Camouflaged Object Detection](https://arxiv.org/abs/2606.31496)

**<font color=#1a73e8>作者：</font>** Jiawei Xu, Qiangqiang Zhou, Zhouping Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In recent years, most research on multimodal salient object detection (SOD) and camouflaged object detection (COD) typically aims to improve performance through complex cross-modal feature fusion and decoding structures. However, this approach leads to an excessively large model parameter scale and often fails to deliver satisfactory detection performance due to structural redundancy. In contrast, the human visual process is able to efficiently perform salient and camouflaged object identification without such complex structures. This contrast raises an important question: Can we draw conceptual inspiration from the human visual process to achieve a simpler modeling strategy, and still realize accurate and efficient object detection? To answer this question, we propose HVPNet, a simple yet general bio-inspired computational architecture. Drawing on the multi-layered information integration of the retina as a conceptual metaphor, we designed a Retinal Integration Module (RIM), which effectively integrates multimodal features through a level-specific multi-stage integration strategy. To fully exploit these features, we further design a cortical decoder (CD) that breaks down the decoding process into low- and high-level visual stages, abstracting the hierarchical processing in the human visual cortex. Benefiting from these designs, HVPNet can readily extend to seven tasks across four modalities. Without bells and whistles, it establishes an excellent accuracy-efficiency trade-off across 22 datasets spanning these seven tasks. Our code is available at this https URL.

---


### 182. [Governance Gaps in Agent Interoperability Protocols: What MCP, A2A, and ACP Cannot Express](https://arxiv.org/abs/2606.31498)

**<font color=#1a73e8>作者：</font>** Richard Kang, Yudho Diponegoro  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Agent interoperability protocols (MCP, A2A, ACP, ANP, and ERC-8004) have rapidly matured to enable identity, capability discovery, tool access, and message exchange between autonomous agents. However, as enterprises deploy heterogeneous agent fleets that must make collective decisions under governance constraints, a question arises: can these protocols support governed agent communities, or only task-oriented coordination? We present a systematic gap analysis applying a six-dimension governance requirements taxonomy (membership, deliberation, voting, dissent preservation, human escalation, and audit/replay) derived from organizational theory, multi-agent systems literature, and enterprise governance standards. We analyze each protocol's specification against this taxonomy, classifying capabilities as Supported, Partial, or Absent. The resulting gap matrix reveals that voting and dissent preservation are universally absent across all five protocols, deliberation is absent or at most partial, and no protocol encodes the full set of primitives required for governed agent communities. We distinguish extensible gaps (addressable through protocol extension mechanisms) from structural gaps (requiring a new architectural layer) and assess time-sensitivity based on observed protocol evolution velocity. The analysis establishes that agent community governance constitutes a missing architectural layer above current interoperability standards, not a missing feature within them.

---


### 183. [Fully Automated High-Precision Segmentation of Retinal Atrophy and Ellipsoid Zone Thickness in OCT: A Reliable Tool for Real-World GA Monitoring](https://arxiv.org/abs/2606.31502)

**<font color=#1a73e8>作者：</font>** Wolf-Dieter Vogl, Hlynur Skulason, Oliver Leingang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geographic atrophy (GA) secondary to age-related macular degeneration (AMD) requires precise monitoring of relevant structural biomarkers to assess disease stage, progression, and treatment response. This paper presents a fully automated, deep learning-based framework for the high-precision, pixel-wise segmentation of key biomarkers in optical coherence tomography (OCT) imaging: retinal pigment epithelium (RPE) loss, ellipsoid zone (EZ) loss, and EZ thinning. The proposed pipeline uses three specialized semantic segmentation models to delineate RPE loss, EZ boundaries (including interruptions), and Bruch's membrane. To ensure robustness and generalizability, the models were developed on a diverse dataset of 298 SD-OCT volumes representing the full phenotypic spectrum of AMD (GA:222, intermediate AMD: 40, neovascular AMD: 17, healthy: 19) and validated on an independent external dataset (n=43). The comprehensive evaluation was further strengthened using additional datasets to assess repeatability, inter-reader reliability, the impact of B-scan density on measurement accuracy, and subgroup performance stratified by lesion size. Results demonstrated high segmentation accuracy (Dice RPE loss: 0.88, Dice EZ loss: 0.87, Pearson's r > 0.99). Total EZ thickness measurements exhibited a sub-pixel average deviation of 2.15 $\mu m$, and segmentation reliability was confirmed by a strong reproducibility score (ICC > 0.98). By accurately and consistently quantifying outer photoreceptor degeneration and RPE loss, this fully automated framework provides a highly reliable tool for GA assessment in both clinical trials and routine real-world ophthalmic care.

---


### 184. [Building an ASR Solution for Training and Assessing Children's Reading](https://arxiv.org/abs/2606.31508)

**<font color=#1a73e8>作者：</font>** Yacouba Diarra, Nouhoum Souleymane Coulibaly, Mamadou Dembele 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic speech recognition for children's reading remains underdeveloped for most African languages, including Bambara, despite its potential value for reproducible literacy assessment. We present an open-source system for assessing children's reading in Bambara, developed through an end-to-end process linking field data collection, benchmark construction, model adaptation, a reading application, and classroom validation. A mobile collection and assessment app was used to collect 55 hours of raw reading speech from 60 children, from which we construct a public benchmark for Bambara child-reading assessment. Fine-tuning experiments compare Soloni, a Bambara-adapted Fast-Conformer ASR framework with TDT and CTC decoders, with QuartzNet, a compact convolutional ASR architecture. The best Soloni model reduces WER from 0.42 to 0.22 and CER from 0.15 to 0.08, substantially outperforming QuartzNet on the isolated benchmark. The experiments further show that repeated readings of the same texts provide architecture-dependent benefits: they substantially improve QuartzNet but add only marginal gains for Soloni, while SpecAugment regulates training without exceeding the best unaugmented configuration. Disaggregated analysis identifies children under 10 as the main source of residual errors, motivating targeted collection from younger readers. Ten classroom trials supported continued use of the application.

---


### 185. [PRISM: Latent Composition Consistency for Single-Image Reflection Removal](https://arxiv.org/abs/2606.31513)

**<font color=#1a73e8>作者：</font>** Junseong Shin, Tae Hyun Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-image reflection removal (SIRR) seeks to recover the transmission layer from a mixture corrupted by reflections -- a severely ill-posed problem. Existing methods operate in pixel space, where the nonlinear sRGB formation model entangles the two layers and limits generalization. We observe that pretrained VAE latent spaces exhibit substantially lower coherence between image layers compared to pixel space, providing a more favorable working space for decomposition. Building on this finding, we propose \textbf{PRISM} (Pretrained-latent Reflection Image Separation Model), which reinterprets SIRR as a latent linear separation problem. Under an approximate additive formulation in latent space, PRISM learns a flow matching velocity field on a pretrained FLUX backbone that recovers both transmission and reflection in a single forward pass. To enforce robust disentanglement, we introduce a Latent Composition Consistency (LCC) strategy that constructs synthetic mixtures by swapping reflection latents across samples and enforces consistent decomposition via a cycle loss. We further propose a Layer Contrastive Separation (LCS) loss that promotes semantic separation between layers through patch-level contrastive learning, without requiring explicit reflection targets. Experiments on six benchmarks demonstrate that PRISM consistently outperforms state-of-the-art methods by significant margins, with strong generalization to in-the-wild images.

---


### 186. [FinPersona-Bench: A Benchmark for Longitudinal Psychometric Stability of Autonomous Financial Agents](https://arxiv.org/abs/2606.31522)

**<font color=#1a73e8>作者：</font>** Muhammad Usman Safder, Ayesha Gull, Rania Elbadry 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly deployed as autonomous financial agents initialized with explicit behavioral mandates such as "preserve capital" or "avoid speculative bets" that are meant to govern every decision throughout deployment. In practice, however, as market context accumulates over long horizons, these mandates gradually lose their behavioral influence, a phenomenon we formalize as Mandate Salience Decay (MSD). To measure MSD objectively, we introduce FinPersona-Bench, a simulation benchmark in which a synthetic market decouples observable price from hidden fundamental value, enabling falsifiable evaluation across three failure modes: trading without signal in calm markets, panic-selling during crashes, and ignoring fundamental value during speculative bubbles. Evaluating 18 leading frontier and open-source LLMs, each assigned one of three behavioral profiles ranging from strict capital preservation to aggressive growth, shows that MSD compounds over time and is model-dependent. In crash scenarios, the behavioral gap between static agents and those receiving periodic mandate re-grounding grows 4.4x from the first to the final quarter of the simulation. The effects of mandate re-grounding are not uniformly positive: it consistently helps conservative agents in low-signal markets but actively worsens behavior for aggressive agents in the same setting. These findings suggest that reliable long-horizon deployment requires selective, mandate-aware re-grounding based on agent profile and market regime.

---


### 187. [A time-series classification framework for individual-level absenteeism prediction under severe class imbalance](https://arxiv.org/abs/2606.31532)

**<font color=#1a73e8>作者：</font>** Kwong Ho Li, Matthew Roughan, Wathsala Karunarathne  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Staff absenteeism imposes substantial operational costs in high-demand work environments such as healthcare, emergency services, meat processing, construction, and courier and delivery services, where proactive workforce planning depends on reliable individual-level absence prediction. Existing regression and classification approaches share a structural limitation; they map features observed at time t to labels at the same time t, reproducing already-realised outcomes rather than predicting future events, and discard the sequential behavioural structure inherent in individual attendance histories. We propose a Time Series Classification (TSC) framework that separates historical attendance sequences from future absence labels, enabling genuinely proactive prediction. Due to the lack of public longitudinal attendance data, we construct a reproducible simulated dataset calibrated to the UCI dataset. We analyse Binary Focal Loss (BFL) and Geometric Mean (G-Mean) loss under severe class imbalance using only the imbalance ratio $\rho$. For BFL, the initial gradient ratio is $\rho\alpha/(1-\alpha)$, implying the balanced weight $\alpha = 1/(1+\rho) \approx 0.023$. Experiments show that performance is governed mainly by $\alpha$, with BFL achieving specificity 0.813 and balanced accuracy 0.888, comparable to G-Mean. Unlike BFL, G-Mean adapts automatically without parameter calibration. Among three deep learning architectures evaluated, Long Short-Term Memory (LSTM), Convolutional Neural Network (CNN), and the hybrid LSTM-Fully Convolutional Network (LSTM-FCN), the LSTM-FCN delivers strong precision and specificity. Stable performance is obtained with batch sizes >= 64 and window sizes between 40-80 days, yielding balanced accuracy of approximately 80% on held-out test data.

---


### 188. [MV-GEL: Language-Driven Multi-View Geometric Entity Localization on Meshes](https://arxiv.org/abs/2606.31533)

**<font color=#1a73e8>作者：</font>** Kartik Bali, Roland Aydin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Identifying and grounding precise geometric entities, such as edges, planar regions, and curved surfaces within 3D objects, is foundational to computer-aided design (CAD), robotic manipulation, and scientific simulation. Although modern Vision Language Models (VLMs) have advanced referring segmentation (RIS) in the image domain, extending such language-driven localization to structured 3D geometry is substantially harder. The 3D object appearance is highly sensitive to viewpoints; a single perspective may render a target entity clearly observable, while another may suffer from severe occlusion or foreshortening. In this work, we attempt to solve these challenges with MV-GEL (Multi-View Geometric Entity Localization), a framework for localizing fine-grained geometric entities on polygon meshes from natural language queries. Our key insight is that reliable CAD entity (i.e., faces, edges or solids) localization depends on selecting views that make the queried entity maximally interpretable. We introduce GELviews, a prompt-conditioned ranking module that prioritizes viewpoints based on language prompted observability of geometric CAD entities. Selected views are processed by a VLM-based reasoning segmentation backbone, and predicted masks are lifted to the corresponding meshes via geometry-aware ray casting. Our framework is completely CAD agnostic and relies only on 3D meshes. Experiments show up to a 1.7X improvement in face-level IoU and over 4.5X gains in edge-level F1 compared to vanilla baselines, substantially outperforming CLIP-based and random view sampling, particularly for thin and view-sensitive this http URL dataset, code and trained checkpoints are available at this https URL.

---


### 189. [Beyond the Expressivity-Trainability Paradox: A Dynamical Lie Algebra Perspective on Navigating Barren Plateaus in Quantum Machine Learning](https://arxiv.org/abs/2606.31536)

**<font color=#1a73e8>作者：</font>** Kung-Ming Lan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As Quantum Machine Learning (QML) transitions toward practical implementation, the field faces a critical architectural bottleneck that challenges the fundamental assumptions of classical statistical learning theory. In classical deep learning, increasing model capacity typically risks overfitting. However, this study advances a counter-intuitive paradigm: unstructured contemporary QML architectures suffer from a profound state of quantum underfitting, driven by the "expressivity-trainability paradox." We demonstrate that the vast Hilbert space capacity of Parameterized Quantum Circuits (PQCs)-traditionally chased as the source of quantum advantage is the direct mathematical cause of Barren Plateaus (BPs), where gradient landscapes become exponentially flat. By synthesizing recent breakthroughs in Dynamical Lie Algebras (DLAs) and Geometric QML, we establish a comprehensive framework linking the algebraic dimension of circuit generators to their optimization dynamics. Furthermore, we empirically validate this framework on a non-linear binary classification task, illuminating a uniquely quantum manifestation of the bias-variance tradeoff: while unstructured architectures achieve near-perfect training accuracy via unscalable parameterization (quantum overfitting), embedding group-theoretic geometric priors acts as a structural regularizer. By restricting the DLA growth to a polynomial regime, our symmetry-preserving approach sacrifices raw memorization capacity to guarantee scalable, gradient-rich training landscapes, offering a robust roadmap for "Trainability-by-Design" in scalable quantum neural networks.

---


### 190. [DataEvolver: Self-Evolving Multi-Agent Data Construction for Text-Rich Image Generation](https://arxiv.org/abs/2606.31537)

**<font color=#1a73e8>作者：</font>** Siyu Yan, Yizhen Gao, Yilin Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-rich image generation is one of the most challenging settings in image generation, since models must simultaneously produce visually realistic images and render legible, semantically aligned, and layout-consistent text. Existing data pipelines usually follow a static crawl-filter-freeze paradigm. They collect candidate samples, filter them once, and freeze the accepted data for training. However, rejected samples are usually discarded, although they often contain useful failure signals such as OCR errors and semantic mismatches. As a result, later construction rounds may repeat the same failure modes. To address these limitations, we propose DataEvolver, a self-evolving multi-agent framework for text-rich image data construction. DataEvolver treats data construction as feedback-driven construction policy evolution. A Retriever collects candidate samples, a Verifier assigns quality scores and rejection causes, a Critic summarizes round-level feedback into semantic feedback, and a Generator completes under-covered regions through targeted synthesis. The updated feedback memory then guides the next construction round. Experiments on text-rich image generation benchmarks show that DataEvolver produces more useful training data than fixed-dataset baselines under matched data budgets. At the 0.75M scale on PixArt-alpha, DataEvolver improves OCR-F1 over the strongest baseline by 85.3 percent on TextScenesHQ and 35.3 percent on LongTextBench. The improvements are consistent across both evaluated benchmarks and also transfer to Show-o2, indicating that the benefit of DataEvolver is not tied to a single downstream generator. These results suggest that rejected samples can provide actionable feedback for improving text-rich image data construction.

---


### 191. [AugSplat: Radiance Field-Informed Gaussian Splatting for Sparse-View Settings](https://arxiv.org/abs/2606.31556)

**<font color=#1a73e8>作者：</font>** Lorenzo Lazzaroni, Riccardo Bollati, Daniel Barath 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating high-quality novel views at real-time frame rates remains a central challenge in 3D vision, particularly in sparse-view scenarios. Neural radiance fields have demonstrated robust reconstruction from limited observations, but their reliance on volumetric rendering leads to high computational cost and slow inference. In contrast, Gaussian Splatting methods achieve real-time rendering through rasterization, but their optimization is highly sensitive to the quality of the initial geometry. This sensitivity becomes especially problematic in sparse-view settings, where limited observations often lead to incomplete or noisy point-cloud reconstructions. In this work, we present AugSplat, a simple framework for improving Gaussian Splatting in sparse-view regimes using radiance-field-based view augmentation. We first train a radiance field on the sparse input views and use it to synthesize additional images from nearby novel viewpoints, increasing the effective view-space coverage available for supervision. These synthetic views are then used as auxiliary supervision during Gaussian Splatting optimization. We study two variants: Staged AugSplat, which uses synthetic views for an initial optimization phase before switching to real images, and Dual AugSplat, which jointly trains on real and synthetic views with a decaying synthetic loss weight. Experiments on sparse-view mip-NeRF 360 scenes show that AugSplat improves reconstruction quality over standard Gaussian Splatting. Staged AugSplat achieves the strongest average performance, while Dual AugSplat provides a closely performing formulation that keeps real-image supervision active throughout training, and both variants preserve real-time rendering at inference.

---


### 192. [CVE-TTP KG: Knowledge Graph Linking Software Vulnerabilities to Attack Behaviors](https://arxiv.org/abs/2606.31557)

**<font color=#1a73e8>作者：</font>** Basant Agarwal, Dincy R. Arikkat, Swati Yadav 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In the evolving threat landscape, adversaries exploit software vulnerabilities to launch sophisticated attacks, challenging traditional defenses. Although databases like CVE and NVD provide detailed technical information, they often lack links to attacker behaviors such as tactics and techniques, limiting effective threat interpretation and response. This work bridges this gap by connecting vulnerabilities with behavioral patterns from the MITRE ATT&CK framework. We construct a CVE-TTP Knowledge Graph that links CVEs to tactics and techniques using classification and relation extraction. Transformer-based models are developed for behavior identification, with CySecBERT achieving macro F1-scores of 87.71% (techniques) and 96.16% (tactics). Also, we created an annotated dataset with 24,820 entities and 43,608 relations for entity and relation extraction. The pipeline-based approach achieves macro F1-scores of 0.86 (entity extraction) and 0.99 (relation extraction), while a span-based joint model achieves 0.78. These outputs are integrated into a Neo4j-based Cyber Threat Knowledge Graph, enabling structured visualization of vulnerabilities.

---


### 193. [Mitigating Positional Leakage in 3D Masked Autoencoders for Robust Representation Learning](https://arxiv.org/abs/2606.31570)

**<font color=#1a73e8>作者：</font>** Xu Yan, Huiqun Wang, Chen Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Masked autoencoding has emerged as a prominent paradigm for self-supervised learning on 3D point clouds, achieving competitive performance across downstream tasks. Unlike its 2D counterpart, 3D masked autoencoding directly reconstructs spatial coordinates, making it inherently susceptible to positional leakage. In this work, we identify that the decoder in existing 3D MAE frameworks tends to over-rely on positional information, which weakens semantic representation learning and leads to suboptimal feature quality. To address this issue, we propose MPL-MAE, a masked point learning framework that mitigates positional over-reliance while enhancing the utilization of encoder features. Specifically, we introduce a recalibrated positional embedding module that suppresses metric-dominant coordinate signals while preserving geometric topology, together with a gated positional interface module that dynamically regulates positional injection during reconstruction. These designs promote a more balanced interaction between spatial priors and semantic features, yielding robust and informative representations. Extensive experiments across downstream tasks demonstrate that MPL-MAE consistently achieves competitive performance, validating its effectiveness. Code is available at this https URL.

---


### 194. [Temperature Field Reconstruction of Tungsten Monoblock Divertor on EAST using Physics-aware Neural Operator Transformer](https://arxiv.org/abs/2606.31574)

**<font color=#1a73e8>作者：</font>** Zikang Yan, Xiao Wang, Qingquan Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate modeling of the divertor temperature field is essential for preventing material melting and damage and for extending the service life of fusion devices. However, conventional numerical methods, such as the Finite Element Method (FEM), are computationally expensive and therefore unsuitable for real-time applications. Therefore, a fast and generalizable method is required for real-time reconstruction of the divertor temperature field and subsequent real-time control. To address the above issue, we propose a Physics-aware Neural Operator Transformer (PNOT) to characterize the spatiotemporal evolution of the divertor temperature field. It models boundary heat-flux relations as a structured graph and employs graph attention to explicitly capture spatial physical dependencies. Inspired by physics-aware attention, we further develop a physics-aware neural operator module to aggregate query points with similar physical conditions via slicing and model heat diffusion, while a gradient-constrained Sobolev regularization loss enforces consistency between function values and their derivatives. Experimental results show that these physical constraints improve prediction accuracy while preserving physical consistency. The source code of this paper will be released on this https URL

---


### 195. [Introduction to Stochastic Differential Equations for Generative Machine Learning: A Variational Perspective](https://arxiv.org/abs/2606.31576)

**<font color=#1a73e8>作者：</font>** Ole Winther, Paul Jeha, Sander Dieleman 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The use of ordinary and stochastic differential equations has led to substantial progress in generative machine learning with applications to, for example, image, video and biomolecule generation. This paper provides a self-contained and informal introduction to the differential equations, the probabilistic framework for using them in generative modeling and the Fokker--Planck equation that governs the temporal evolution of the marginal distribution of the stochastic variables of the differential equations. The variational lower bound on the log-likelihood (the evidence lower bound, ELBO) is derived and used as a general starting point for a discussion of diffusion models, score matching, and flow matching. All of these approaches may be viewed as specific parameterizations of the most general variational approach. A one-dimensional density modeling problem is used as a simple example to compare different parameterizations.

---


### 196. [Holonic Active Distillation for Scalable Multi-Agent Learning in Multi-Sensor Systems](https://arxiv.org/abs/2606.31578)

**<font color=#1a73e8>作者：</font>** Dani Manjah, Tim Bary, Benoît Macq 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The rapid expansion of sensor-based networks introduces major challenges in scalability, adaptability, and knowledge transfer, especially in open environments where new subsystems can dynamically join or leave. In this work, we propose a Holonic Active Distillation architecture within a Holonic Multi-Agent System (HMAS) to address these issues. Our approach integrates Clustered Stream-Based Active Distillation (CSBAD), a framework in which specialized student models collect local data, query pseudo-labels from teacher models, and cluster into groups of similar sensors.
Results show that the holonic organization balances local specialization with global generalization, while efficiently adapting to sensor departures and re-integrations. We also analyzed trade-offs among incremental model updates, system reorganization, and scalability limits.
Our findings highlight the advantages of holonic learning for multi-sensor systems while identifying key challenges related to model drift and long-term adaptation.

---


### 197. [Robustness of neural networks to random noise perturbations of their inputs](https://arxiv.org/abs/2606.31581)

**<font color=#1a73e8>作者：</font>** Mark Levene, Martyn Harris  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate the problem of the robustness of a trained neural network to the perturbation of its input values. More specifically, we examine the interplay between the accuracy of the network, as measured by the mean squared error, and robustness. Accordingly, we present a robustness measure, which, with high probability, suggests an upper bound on the mean squared error of the network, with respect to an input data set, for a given perturbation of the input values of the network. The measure we propose is both simple and efficient to compute, treating the neural network as a black box. We provide experimental results on several real-world data sets showing the efficacy of the proposed method. We also introduce the concept of robustness curves, which allows us to further analyse robustness within and between data sets.

---


### 198. [DPPE: Rethinking Camera-Based Positional Encoding for Scaling Multi-View Transformers](https://arxiv.org/abs/2606.31585)

**<font color=#1a73e8>作者：</font>** Shun Kenney, Teppei Suzuki  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The remarkable scalability of Transformers has expanded their application to 3D computer vision, where camera-aware positional encoding is crucial for providing spatial cues in multi-view geometry. Recent advancements have established the practice of using camera parameters -- such as extrinsics or projection matrices -- as relative positional encoding into the query, key, and value vectors of the attention mechanism. However, when scaling up the training recipe of novel view synthesis (NVS) models with the camera-based positional encoding, we observe a significant issue: model performance stagnates in the late stages of training.
In this paper, we investigate the cause of the performance bottleneck when scaling up and demonstrate that storing rotation and translation given by the positional encoding in the same dimensions of the value vector causes indeterminacy in their independent identification, hindering training scalability. To address this, we propose Decoupled Pose Positional Encoding (DPPE), a novel camera-based positional encoding that explicitly decouples rotation and translation. Extensive evaluations on NVS tasks demonstrate that DPPE enables stable long-term training even in scaled-up training setup. Furthermore, it exhibits superior generalization performance in extrapolation settings, such as handling an increased number of viewpoints and zoom-in scenarios.

---


### 199. [Comparative Analysis of Machine Learning based Intrusion Detection in Realistic IoT Networks](https://arxiv.org/abs/2606.31594)

**<font color=#1a73e8>作者：</font>** Rana Alharbi, Chuadhry Mujeeb Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Internet of Things (IoT) is rapidly growing and expanding into various sectors, such as healthcare, transportation, smart homes, and more. Despite the benefits of using IoT devices, they present several challenges. Given the significant role these devices play in our lives, it is crucial to address issues related to their security and privacy. These devices are limited in resources, which complicates their security and the protection of the data that they manage. The paper aims to examine intrusion detection systems using the Gotham2025 dataset, generated through the Gotham testbed, which consists of 78 emulated IoT devices utilising various protocols, including MQTT, CoAP, and RTSP, to assist in safeguarding IoT networks from attacks. We conduct a comparative analysis between five machine learning algorithms, including Random Forest, XGBoost, Logistic Regression, Naive Bayes, and Deep Neural Network. We demonstrate that the Random Forest Classifier was the top-performing model, achieving an F1-score of 0.99 in classifying attacks.

---


### 200. [Digital signature schemes based on code equivalence and syndrome decoding from restricted errors](https://arxiv.org/abs/2606.31601)

**<font color=#1a73e8>作者：</font>** Sarah Arpin, Jason T. LeGrow, Hiram H. López 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Digital signature schemes are an important cryptographic tool to ensure data authenticity and integrity in many applications that must be resilient to attacks, including those facilitated by quantum computers. We consider the two digital signature schemes based on error-correcting codes that are second-round candidates in NIST's call for Additional Signature Schemes, which is part of the Post-Quantum Cryptography Standardization Process. Specifically, we provide an overview of the Codes and Restricted Objects Signature Scheme (CROSS) and the Linear Equivalence Signature Scheme (LESS). We describe their underlying problems of syndrome decoding from restricted errors and code equivalence. We review sigma protocols and how they can be transformed into digital signature schemes via the Fiat-Shamir transform. Finally, we explain how this procedure yields code-based digital signatures believed to be post-quantum secure.

---


> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-274](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
