# 📦 其他研究 | 2026年10月23日

> 本类共 **232** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-232](./part-05.md)

---

### 151. [Block Diffusion for Longitudinal EHR: Accuracy, Efficiency, and Representation Trade-offs](https://arxiv.org/abs/2610.29533)

**<font color=#1a73e8>作者：</font>** Ashvin Gupta, Joshua Placidi, Brendan Delaney 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoregressive (AR) models have proved effective for zero-shot prediction from longitudinal electronic health records, but impose strictly sequential generation on trajectories containing temporally clustered and interdependent clinical events. We investigate block-based masked diffusion (BD) as an alternative on MIMIC-IV under matched tokenisation, context length, model capacity, and evaluation conditions. Across block sizes, BD exhibits a clear quality--efficiency trade-off, with small-block configurations retaining much of the predictive performance of AR while enabling substantially faster inference. A representative $B{=}8$ configuration achieves approximately $1.43\times$ faster evaluation. Although generative rollout remains below AR in most settings, frozen linear probes on BD and AR representations achieve near-identical performance across clinical prediction tasks, indicating that BD learns comparably informative clinical representations. Increasing the denoising budget yields diminishing returns, while alternative decoding strategies provide limited gains. Overall, our results show that block diffusion is a viable and computationally attractive approach to longitudinal EHR modelling, with further improvements in iterative decoding offering a promising route toward closing the remaining generative performance gap.

---


### 152. [Stochastic Pruning of the DPO Computation Graph: 1.4x Faster Training and Lower Peak Memory](https://arxiv.org/abs/2610.29538)

**<font color=#1a73e8>作者：</font>** Yubing Wu, Wei Chen, Junmei Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Direct preference optimization (DPO) incurs training costs in output scoring, sequence execution, and backpropagation, so reducing supervision alone does not necessarily save computation. We introduce a unified framework for stochastic pruning of the DPO computation graph that independently samples response positions for scoring, response prefixes for execution, and preference branches for backpropagation. By making these selections before the corresponding operations, the framework omits computation at each stage of a training step. Our analysis characterizes the objective changes induced by position and sequence pruning and uses inverse-probability weighting to obtain a conditionally unbiased single-branch gradient estimator for the sampled objective. Controlled measurements show that position and sequence pruning primarily reduce peak memory, with most output-memory savings attributable to an implementation that retains full response supervision. Branch pruning yields a $1.426\times$ step-time speedup over a concatenated DPO baseline and reduces training time by about 30\% relative to stock DPO across two model families, with slightly lower mean accuracy and benchmark-dependent changes in open-ended scores. These findings relate the resource benefits of stochastic graph pruning to the computation omitted and the resulting changes in the training objective.

---


### 153. [Hyperspherical Simplex Representations for Backward-Compatible Retrieval](https://arxiv.org/abs/2610.29550)

**<font color=#1a73e8>作者：</font>** Simone Ricci, Niccolò Biondi, Federico Pernici 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training modern AI models has become increasingly expensive, and updating deployed models can alter their internal feature representations, affecting applications built upon them. In retrieval systems, such updates often require complete gallery re-indexing, a computationally expensive process at scale. Existing backward-compatibility methods enable direct comparison of representations from updated and earlier models, avoiding re-indexing. However, they typically require compatibility-specific training, learned mapping functions, or architectural modifications, and often depend explicitly on the previous model. We propose hyperspherical simplex representations derived from softmax outputs and logits for backward-compatible retrieval across independently trained models. They leverage the simplex structure induced by softmax cross-entropy training with one-hot labels as a common geometric reference across model updates. Since this reference depends on the number of classes, adding new ones expands the simplex, misaligning existing class prototypes with their earlier counterparts. We therefore derive a deterministic linear transformation to restore their alignment. Our theoretical analysis of the formal backward-compatibility definition identifies two geometric conditions under which its inequalities hold in expectation, assuming von Mises--Fisher class distributions with increasing concentration across updates. Aligned regular-simplex representations satisfy these conditions, providing a theoretical basis for the proposed representations under the stated assumptions. Without using additional compatibility-specific losses, learned mappings, or architectural modifications, the proposed representations achieve competitive results on standard compatibility benchmarks, including expanded class sets, more expressive architectures, and independently trained models from public repositories.

---


### 154. [SOAR: Social and Opinion-Aware Recommendations](https://arxiv.org/abs/2610.29556)

**<font color=#1a73e8>作者：</font>** Giannis Christoforidis, Apostolos N. Papadopoulos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> One of the enduring challenges in online platforms is recommendation. Both communities and advertisers face difficulties in analyzing complex user behavior, identifying habits and evolving preferences, and providing timely recommendations that are relevant to user interests. In particular, point of interest recommendation poses the additional challenge of identifying the factors that influence user behavior, capturing user tendencies, and generating accurate, personalized recommendations for each individual. In this work, we propose SOAR, a Social and Opinion Aware Recommendation model that incorporates both the user's friendship network and textual reviews to assess whether a location is suitable for a specific user, with a particular emphasis on the sentiment of shared reviews. Experimental results in real-world datasets demonstrate that incorporating reviews into the recommendation process improves the precision of the recommendation.

---


### 155. [VMSpec: A Decompiler-based Approach against Virtual Machine Obfuscation](https://arxiv.org/abs/2610.29566)

**<font color=#1a73e8>作者：</font>** Fabian Kilger, Leonard Auer, Manuel Andreas  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Malicious actors frequently obfuscate their code to hinder investigative reverse engineering efforts. Among the most formidable techniques is virtual machine (VM) obfuscation: programs are translated into bytecode for a custom VM, often with a randomized virtual instruction set and distributed alongside a corresponding interpreter. Manual analysis and deobfuscation scale poorly due to the complexity of VM obfuscation and the diversification techniques that render each VM and interpreter unique. Existing methods primarily focus on simplifying execution traces and identifying virtual execution boundaries. However, comparatively little attention has been given to recovering higher-level program semantics from VM-obfuscated code. To address this gap, we propose VMSpec, a novel decompiler-based approach that automates the construction of VM processor specifications, enabling existing, well-known decompilers to analyze the VM-obfuscated code. We evaluate our prototype of VMSpec on 147 programs from an established obfuscation benchmark, comprising hash functions, standard algorithms, and randomized functions, obfuscated with different configurations of the Tigress and Code Virtualizer obfuscators. To demonstrate real-world applicability, we additionally include six domain generation algorithms stemming from real-world malware. VMSpec completely strips VM-obfuscation from nearly all obfuscated samples, producing output comparable to Ghidra's decompilation of the original code. Furthermore, it is the first method capable of reconstructing the complete program behavior of VM-obfuscated programs with infinite, input-dependent paths and recursive calls.

---


### 156. [Rethinking Underwater Image Enhancement: Learning through Text-Guided Degradation Curriculum](https://arxiv.org/abs/2610.29569)

**<font color=#1a73e8>作者：</font>** Hongri Tian, Wenxue Li, Tian Ye 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing paired clean-degraded datasets have advanced learning-based underwater image enhancement, but they remain either limited in scale or difficult to acquire, and still fail to adequately cover the diverse degradations encountered in real-world underwater environments. Such scarce and insufficient data ultimately restrict the generalization of underwater image enhancement models, highlighting the need for realistic and controllable degradation modeling to better capture real underwater conditions and improve enhancement robustness. To this end, we propose a unified degradation-aware training framework for the underwater image enhancement task. A Text-Conditioned Degradation Augmentation Pipeline uses a text-guided diffusion model to synthesize diverse and semantically consistent degraded samples, providing paired data to support the subsequent curriculum learning strategy. The proposed Progressive Degradation Curriculum organizes training across multiple attributes and difficulty levels to promote balanced learning, and a Transmission-Guided One-Step Diffusion Model leverages this progressive process to better address the wide range of degradation severity and restoration ambiguity in underwater images. Extensive experiments on multiple underwater benchmarks demonstrate that our proposed method achieves superior performance. Our code and models will be released upon the publication of this work.

---


### 157. [Implicit Feature Reweighting for Label-Free Graph Generalization](https://arxiv.org/abs/2610.29571)

**<font color=#1a73e8>作者：</font>** Tianjun Yao, Chen Xi, Xinyang Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph-level out-of-distribution (OOD) generalization is critical for deploying graph neural networks in real-world applications where distribution shifts are inevitable. Existing approaches typically require class labels during representation learning to decide which substructures are predictive, limiting their applicability. We propose SCARCE, a label-free representation-learning framework that yields distribution-shift-robust graph representations from an environment partition of the training graphs alone, whether that partition comes from dataset metadata or, when none is available, from clustering a self-supervised embedding. Our method operates in two stages: (1) a variational graph autoencoder is warm-started for graph reconstruction; and (2) an adversarial confusion mechanism forces the encoder to produce representations from which a discriminator cannot distinguish environments, while preserving graph-reconstruction fidelity. We provide theoretical analysis showing that environment confusion contracts environment-discriminative directions in the representation space, which, under regularized downstream classifiers, is equivalent to imposing a stronger directional penalty on environment-associated features. This feature-reweighting mechanism reduces reliance on spurious correlations without erasing information, offering a label-free, continuous relaxation of last-layer reweighting methods. Experiments on a controlled synthetic datasets and the DrugOOD datasets show that SCARCE achieves state-of-the-art OOD generalization among label-free methods, using no class labels during representation learning.

---


### 158. [Private Online Prediction from Experts with Small Losses](https://arxiv.org/abs/2610.29575)

**<font color=#1a73e8>作者：</font>** Bo Li, Peng Ye  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider online prediction from experts, a fundamental problem in machine learning, under differential privacy constraints. Existing private algorithms achieve near-optimal regret $\tilde{O}(\sqrt{T})$, where $T$ is the time horizon. However, this bound becomes suboptimal when $L^\star$, the cumulative loss of the best expert, is significantly less than $T$. In this work, we present the first differentially private algorithm with regret $\tilde{O}(\sqrt{L^\star})$, offering a substantial improvement in the low-loss regime. Our regret bound matches the non-private lower bound up to poly-logarithmic factors for constant privacy parameters, demonstrating that privacy incurs only a small cost in this setting. Our result assumes that the input sequence is oblivious, i.e., it is fixed in advance and independent of the algorithm's outputs. We also prove that an $\tilde{\Omega}(\sqrt{T})$ regret is inevitable for adaptively generated inputs, even when $L^\star = 0$.

---


### 159. [The Reflexivity Threshold: A Phase Transition for Multi-Agent Performative Prediction](https://arxiv.org/abs/2610.29577)

**<font color=#1a73e8>作者：</font>** Ahmed Mahrous, Roberto Di Pietro  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many learning systems are performative: once deployed, their predictions change the data distribution on which future models are trained. In multi-agent settings, this feedback is routed through a network of interacting learners, so stability depends not only on the strength of performativity but also on who affects whom. We study repeated retraining in multi-agent performative prediction and identify a spectral threshold that separates stable learning from worst-case learning obstruction. Prior work often collapses cross-agent feedback into a scalar contraction constant, missing this network structure. We instead introduce the reflexivity matrix $\Gamma$, which records how strongly one agent's deployment can move another agent's best response, defined from per-agent gradient sensitivities and curvature parameters. The threshold occurs when the spectral radius of this matrix crosses one. Below the threshold, repeated retraining converges geometrically to a unique performatively stable equilibrium, with cumulative excess loss bounded uniformly in the time horizon. Above the threshold, we construct noisy supercritical instances in which every local-information learner incurs expected cumulative excess loss growing linearly for horizons up to order $1/(\rho(\Gamma)-1)$. Together, these results characterize the threshold behavior through upper and lower bounds and recover the single-agent scalar threshold from prior work as a special case.

---


### 160. [Fast Bayesian Optimization Through Linear Models](https://arxiv.org/abs/2610.29580)

**<font color=#1a73e8>作者：</font>** Colin Doumont, Henry Moss, Philipp Hennig  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian optimization (BO) is typically used only for problems where the underlying function is deemed "expensive" (e.g. in time or money), with the speed of the BO algorithm being of little importance. In the real world, however, problems span a continuous range of values, going from cheap to expensive. In this paper, we present BO algorithms through the lens of a speed-performance Pareto frontier: we compare BO against faster algorithms like CMA-ES, and highlight how certain regions of the Pareto frontier are currently empty. As a solution, we propose a new set of fast BO methods that exploit the linear structure in existing BO algorithms, for both continuous and combinatorial inputs (from ~10 to 6000+ dimensions). Our methods achieve performance similar to state-of-the-art BO, while being more than $10^2\times$ to $10^3\times$ faster, opening the field of BO to an entirely new class of problems.

---


### 161. [Fragment-Level Graph Encoding for Interpretable Molecular Property Prediction](https://arxiv.org/abs/2610.29589)

**<font color=#1a73e8>作者：</font>** Rafael Lopes Almeida, Ina Pöhner  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks (GNNs) are among the standard tools for molecular property prediction, but the atom-level explanations of their predictions are hard for medicinal chemists to act on. We propose a change of input representation rather than a new model: molecules are encoded as fragment-level graphs from BRICS decomposition, where each node is a synthetically meaningful fragment whose features are the element-wise sum of its atoms' features. Because only the representation changes, any message-passing GNN and any post-hoc attribution method produces explanations at the resolution of functional groups instead of single atoms. Across four architectures, four prediction tasks, and two explainers under scaffold splits, fragment-level encoding matches atom-level test accuracy on roughly five-fold smaller graphs. Integrated-Gradients attributions recover known pharmacophores above chance on two enzyme targets, namely BACE at 1.5 times the chance rate, and PTR1 at 3.2 times. A like-for-like comparison against an aggregated atom-level baseline shows that post-hoc aggregation is not a stable substitute: its BACE hit rate range both exceeds and falls below the fragment model's hit rate depending on two arbitrary aggregation choices, whereas fragment-level training yields a single convention-free attribution at no predictive cost. The code is available at: this https URL

---


### 162. [A Transfer Learning-Driven Methodology for Efficient and Sustainable Indoor Localization Using VLC](https://arxiv.org/abs/2610.29594)

**<font color=#1a73e8>作者：</font>** Masood Jan, Wafa Njima, Xun Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid expansion of the Internet of Things enables seamless collaboration among connected devices, making indoor localization a critical component of industrial automation. However, conventional localization techniques struggle in dynamic environments. These methods depend on extensive, frequent data collection and environment-specific calibration, limiting scalability, interoperability, and effective use of prior research while imposing significant energy penalties that hinder practical deployment. To address these challenges, we propose an energy-efficient transfer learning (TL) based approach for visible light communication based indoor localization. Our method leverages TL to tackle environmental variability, including lighting fluctuations and physical obstacles that typically degrade localization performance, while simultaneously reducing computational overhead and energy consumption compared to conventional approaches. We also introduce a novel model efficiency (ME) metric, designed to integrate localization accuracy, energy efficiency, data efficiency, and transfer gain into a single evaluative measure for comprehensive optimization. Evaluations on a real-world dataset collected from a BOSCH factory demonstrate that our model achieves a 47% improvement in localization accuracy compared to a conventional model that does not utilize TL, and achieves up to 67.5% ME with TL models, compared to only 10.4% in conventional models under high-noise conditions. These results underscore the potential of our approach to deliver a highly efficient and scalable indoor localization system suitable for energy-constrained industrial applications.

---


### 163. [Local and Global Recursive Ridge Regression for Online Residual Correction of Frozen Multivariate Forecasters under Label Delay](https://arxiv.org/abs/2610.29604)

**<font color=#1a73e8>作者：</font>** Takumi Fujimoto, Hiroaki Nishi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A frozen multi-horizon forecaster can be corrected online from its own residuals. However, under label delay the target of a block arrives only after the whole horizon has passed, and the corrector's retained state grows with the number of channels. Aiming to combine a small retained state with a large error reduction, we propose DRiC (DCT Ridge Corrector), which fits a ridge regression of the leading discrete cosine transform (DCT) coefficients of the next residual block on those of the frozen forecast and of the latest input block, with sufficient statistics updated recursively. Its local variant, DRiC-L, keeps one such regression per channel; its global variant, DRiC-G, pools all channels into one regression, whose statistics do not depend on the channel count. A guard tracks a running scale of the frozen forecast's residual for each channel; it skips updates on blocks far outside that scale and clips the issued correction. We evaluate on seven datasets (four ETT series, Weather with its missing-value codes filled, Electricity, and Traffic) with DLinear, PatchTST, and iTransformer backbones, against 10 naive, gradient-trained, and closed-form methods. DRiC-L with eight DCT coefficients (DRiC-L8) reduces the mean squared error (MSE) by 14.55% on average over 126 conditions, against 12.98% for ELF, the most accurate comparator, while retaining 15-17 times less state, although ELF is more accurate on Traffic. DRiC-G retains 14.6 kB on the 321-channel Electricity data and 18.9 kB on the 862-channel Traffic data and is the most accurate method at or below its state on both. However, 5 to 7 of the 10 comparators, all with at least 10 times its state, are more accurate there. On the unfilled Weather file, DRiC-L8 without the guard has on average 8.0 times the frozen forecast's MSE, whereas with the guard it reduces the MSE by 7.94%. Code: this https URL.

---


### 164. [Improved Training of Strong Stochastic Flow Maps](https://arxiv.org/abs/2610.29605)

**<font color=#1a73e8>作者：</font>** Zander W. Blasingame, Antonio Franca, Raul Minan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stochastic flow maps promise few-step sampling of stochastic differential equations (SDEs) by learning to directly jump between times along the solution path, yet training these models to learn this solution map remains difficult. The primary obstacle is the Brownian path itself: it is an infinite-dimensional object which needs to be passed to the neural network and is nowhere differentiable, which makes the implementation of derivative-based losses that power the state-of-the-art deterministic flow maps just out of reach. We identify two core design principles which address these issues: a) represent the Brownian path with a basis which carries higher-order local information, and b) train with an objective that forces the network to use the full representation of the path, not just the first order. To address this, we leverage the shifted Legendre polynomial expansion with a Wong-Zakai styled objective, unlocking derivative-based losses. Finally, we propose a recipe for fine-tuning large pre-trained flow models into strong stochastic flow maps. We ablate through this design space on several toy problems and use our findings to transform a large flow model into a strong stochastic flow map on ImageNet, achieving roughly a three-fold improvement in FD-DINOv2 over SSFM at four NFE.

---


### 165. [No Frames, Just Frequencies: Bandwidth-Efficient Deployment-Time Adaptation for Smart Glasses](https://arxiv.org/abs/2610.29607)

**<font color=#1a73e8>作者：</font>** Francesco Corti, Moritz Becker, Olga Saukh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep neural networks deployed on smart glasses must adapt to changes in the distribution of incoming data while adhering to strict privacy and device constraints. We present No Frames, Just Frequencies, a bandwidth-efficient source-assisted adaptation framework that characterizes distribution shifts using compact frequency descriptors computed on-device. Rather than transmitting camera frames, the glasses compute and send frequency descriptors to a host device that contains a replica of the model. The host device maps the received frequency descriptor to a distribution shift operator that synthesizes out-of-distribution data and adapts a model replica using a pre-defined adaptation protocol. We evaluate the framework on mixtures of ImageNet-C corruptions using convolution-based (ConvNeXtV2-Femto), self-attention-based (DeiT-Tiny), and hybrid (TinyViT-5M) vision models, on person classification (Visual Wake Words), and on object detection (MS-COCO). Our results reveal that adaptation driven solely by the transmitted descriptors recovers $93-95\%$ of the supervised oracle adaptation gain on all three architectures, $82\%$ on Visual Wake Words and $94$--$98\%$ on MS-COCO. Notably, adaptation quality degrades gracefully as the descriptor resolution decreases from $224 $ to $28$ pixels, consistently across architectures, enabling bandwidth reductions from $213\times$ to $784\times$ across the frequency descriptors.

---


### 166. [Diff-IrisPAD: Modeling Bona Fide Iris Distributions for Unsupervised Presentation Attack Detection](https://arxiv.org/abs/2610.29611)

**<font color=#1a73e8>作者：</font>** Geetanjali Sharma, Harsh Yadav, Tanmay Deshpande 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Iris recognition systems are vulnerable to presentation attacks (PAs), including textured contact lenses, print replays, and synthetic irises. Existing PAD methods rely on supervised learning with attack data, limiting generalization to unseen attacks and new sensors. We propose Diff-IrisPAD, an unsupervised framework based on Brownian Bridge Diffusion that models bona fide iris distributions without using attack samples. The method reconstructs clean iris textures from degraded inputs and detects attacks via reconstruction inconsistency using ViT scoring and pixel-level measures. Experiments on a large-scale multi-sensor dataset (125K+ images, NIR and VIS, 8 attack types) show that Diff-IrisPAD achieves an overall ACER of 30.52, significantly outperforming diffusion-based baselines while demonstrating strong generalization to unseen attacks. These results highlight the effectiveness of diffusion-based bona fide modeling for robust and scalable iris PAD.

---


### 167. [An interpretable deep learning method for early hepatocellular carcinoma diagnosis on multiphase CT](https://arxiv.org/abs/2610.29616)

**<font color=#1a73e8>作者：</font>** Emma Sarfati, Alexandre Bône, Pietro Gori 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Early diagnosis of hepatocellular carcinoma is critical to preserve access to curative treatment options. The Liver Imaging Reporting and Data System (LI-RADS) provides a standardized framework for non-invasive diagnosis on multiphase computed tomography, based on major visual imaging features. However, these features may be difficult to assess consistently, particularly in small liver lesions. We developed dLI-RADS, an interpretable artificial intelligence method designed to estimate the probability of hepatocellular carcinoma from multiphase computed tomography images of manually segmented liver lesions, while remaining aligned with LI-RADS-related imaging concepts. dLI-RADS combines neural network-derived predictions with handcrafted quantitative imaging measurements reflecting LI-RADS major features and integrates these inputs using logistic regression. In this multicenter retrospective study, patients with multiphase computed tomography and at least one liver lesion were included, while lesions larger than 40 mm were excluded. Histology served as the reference standard for hepatocellular carcinoma, and a composite reference standard was used for non-hepatocellular carcinoma lesions. The lesion-level accuracy of dLI-RADS and LI-RADS were compared on the internal evaluation set using 10,000-repetition bootstrap non-inferiority tests, with 5% margins and significance levels. On the external test set, sensitivities were similarly compared. dLI-RADS was non-inferior to LI-RADS for lesion-level accuracy in the internal evaluation set, achieving 80% accuracy compared with 74% for LI-RADS (p = 0.04)...

---


### 168. [FogTTA: Online Test-Time Adaptation for Robust Transformer-based Object Detection in Foggy Weather](https://arxiv.org/abs/2610.29618)

**<font color=#1a73e8>作者：</font>** Ali Abedi, Q. M. Jonathan Wu, Ning Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object detection models for autonomous driving commonly experience substantial performance drops when deployed under adverse weather due to the domain shift between training data and real-world operating conditions. This degradation is especially evident when models trained on clear-weather images encounter foggy environments with reduced visibility and contrast. To address this challenge, we introduce FogTTA, an online test-time adaptation framework designed to improve the robustness of Transformer-based object detectors in fog. Using RF-DETR as the underlying object detector, FogTTA enables real-time adaptation to the streaming target domain without requiring source data or retraining. The framework follows a teacher-student design, where the deployed model serves as the teacher and generates pseudo labels from weakly augmented target inputs. These predictions are subsequently refined through non-maximum suppression and confidence filtering. The student model then learns from strongly augmented target sample using the Varifocal loss to mitigate pseudo-label noise. The teacher is updated via exponential moving averaging to ensure stable and continuous adaptation. Experiments show that FogTTA outperforms prior baselines, delivering improved detection accuracy and stability while maintaining real-time performance.

---


### 169. [Reliability-Aware Probabilistic Fusion for Multimodal Learning with Incomplete Evidence](https://arxiv.org/abs/2610.29621)

**<font color=#1a73e8>作者：</font>** Patitapaban Palo, Abhisek Tiwari, Mattia Carletti 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal inputs may be missing or degraded, raising distinct questions of evidence availability and trust. We introduce a reliability-aware Gaussian Product-of-Experts (PoE) in which an input-dependent reliability weight tempers each modality's latent precision, while missing experts are omitted. We characterize how reliability and availability affect posterior information and expert influence. Across two clinical multimodal tasks, the full framework remains competitive with complete inputs and achieves its clearest mean-AUROC advantage under modality absence, particularly on HAIM-MIMIC-MM. Ablations show a substantial gain from missing-aware training and an additional HAIM improvement from reliability weighting under matched PoE, missing-aware, and consistency training. Unseen test-time corruptions are used diagnostically and reveal modality-dependent reliability-weight and latent-uncertainty responses, including failure under severe degradation. Thus, reliability weighting provides an explicit evidence-control mechanism, while learning dependable quality signals remains an open challenge.

---


### 170. [Cross-Area Transfer Learning for VLC-based Indoor Localization with a Transfer Efficiency Score](https://arxiv.org/abs/2610.29638)

**<font color=#1a73e8>作者：</font>** Masood Jan, Wafa Njima, Xun Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Indoor localization systems are critical for Industry-4.0 applications. Visible Light Communication (VLC)-based systems offer advantages such as immunity to electromagnetic interference, high accuracy, and energy efficiency, but their performance is hindered by environmental variability across deployment areas. This paper presents a transfer learning (TL) framework for VLC-based indoor localization that enhances cross-area robustness while reducing data requirements. Using real-world measurements from four distinct areas of a Bosch manufacturing facility, we show that fine-tuning a deep neural network (DNN) pre-trained on source area data with only 40% of target-area measurements recovers 97% of full-data performance, thereby reducing the amount of target data needed. We further introduce the Transfer Efficiency Score (TES), a composite metric that identifies the most effective source models for transfer without exhaustive evaluation. Guided by TES, the framework selects the best source model, yielding localization errors as low as 40.9 cm with success rates above 86%. Validation on an unseen area confirms its generalization capability, with a 3.28 cm mean error achieved using the TES-selected source model. Overall, the proposed framework provides a scalable and data-efficient pathway for industrial VLC localization, substantially reducing deployment costs and computational burden while maintaining high accuracy in diverse and dynamic environments.

---


### 171. [OpenEarth-OVS44: A Multimodal Remote Sensing Dataset for Open-Vocabulary Segmentation](https://arxiv.org/abs/2610.29642)

**<font color=#1a73e8>作者：</font>** Yimin Wei, Hongruixuan Chen, Hao Zheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In remote sensing, open-vocabulary segmentation is particularly important for flexible and scalable land-cover understanding across diverse regions, as it improves generalization to novel categories without requiring exhaustive pixel-level annotations. Despite its great promise, progress in this area remains largely constrained by existing datasets with limited category coverage and overly coarse taxonomies, and therefore struggles to support fine-grained semantic understanding required in real-world applications such as urban functional zoning, carbon accounting, and post-disaster assessment. To address these challenges, we present OpenEarth-OVS44, a multimodal benchmark with 290,587 expert-verified segments from 2,832 RGB images and 1,341 strictly registered RGB-SAR pairs at sub-meter spatial resolution, covering 40 cities across France, Japan, and the United States under a unified 44-class taxonomy organized into 9 base categories. Three evaluation tracks are provided: an RGB-only fine-grained benchmark, a multimodal track with diverse synthetic cloudy conditions for weather-robust evaluation, and a held-out cross-region track. Extensive experiments on representative open-vocabulary segmentation models demonstrate that training on OpenEarth-OVS44 substantially improves fine-grained segmentation performance over the strongest training-free baseline, with improvements of up to 7.1 mIoU points on unseen categories and 27.6 mIoU points on seen categories. The dataset and code will be released.

---


### 172. [Joint Semantic-Channel Coding and Modulation for Generative Image Transmission](https://arxiv.org/abs/2610.29643)

**<font color=#1a73e8>作者：</font>** Hao Cao, Jingkai Ying, Yinhuan Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Digital image transmission typically optimizes source coding, channel coding, and modulation separately, limiting how source representations adapt to channel impairments. We propose SemQAM, a joint semantic-channel coding and modulation scheme for generative image transmission converting source to modulated symbols, such as standard QAM symbols. Channel impairments create two challenges: they can corrupt the latent representation at the receiver, and this corruption can compound through autoregressive coding, degrading reconstruction quality. First, SemQAM represents latent features with vector quantization (VQ), maps each VQ index to a QAM symbol, and updates the codeword corresponding to the detected symbol so that channel impairments directly affect codebook learning. Moreover, SemQAM uses the conditional expectation of received codewords to approximate the receiver reconstruction and reduce error propagation during autoregressive coding. SemQAM supports multiple SNRs and CBRs in a unified model, while also supporting conventional source coding through SemQAM-C. Experiments show that (i) under the same LDPC and QAM settings, SemQAM-C outperforms OneDC in LPIPS and DISTS with substantially lower complexity, showing that the unified model retains competitive capability for source coding. (ii) Compared with this separated counterpart, SemQAM reduces channel uses by 18.57% at matched LPIPS and outperforms the compared JSCC methods, demonstrating the benefit of joint coding.

---


### 173. [MS2CAST: A Video Anomaly Detection Framework via Multi-Scale Spatial Cross-Attention and Efficient Spatiotemporal Networks](https://arxiv.org/abs/2610.29649)

**<font color=#1a73e8>作者：</font>** Ali Safaei, Mohammad Kazemi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video anomaly detection (VAD) is a challenging task for surveillance systems due to the scarcity and diversity of anomalous events. While semi-supervised VAD approaches have advanced the field, many rely on computationally intensive optical flow networks to capture motion dynamics. Convolutional neural networks (CNNs) are also widely used for spatial encoding, but their effective receptive field is highly local. To address these limitations, we introduce MS2CAST, an end-to-end semi-supervised predictive VAD framework. For spatial encoding, we employ a multi-scale cross-attention encoder that fuses the hierarchical feature representations from a vision transformer (MViTv2-S) and a CNN (ConvNeXt-T) to exploit their distinct receptive fields. To model spatiotemporal dynamics without optical flow estimation, we integrate two interchangeable spatiotemporal modules in the latent space. One module (SwinLSTM) incorporates a Swin Transformer, while the other (VMRNN) integrates Vision Mamba blocks. Our objective function combines L1 loss, Gradient Difference Loss (GDL), and Multi-Scale Structural Similarity Index Measure (MS-SSIM) to ensure pixel-wise accuracy, sharpness, and structural integrity. Evaluations across the UCSD Ped2, CUHK Avenue, and ShanghaiTech datasets demonstrate frame-level Receiver Operating Characteristic (ROC) Area Under the Curve (AUC) scores that are competitive with top-tier techniques while maintaining a peak GPU memory usage of under 1 GB.

---


### 174. [Spatially Gated Demographic Steering for Debiasing Multi-Person Text-to-Image Generation](https://arxiv.org/abs/2610.29651)

**<font color=#1a73e8>作者：</font>** Venkatesh Thirugnana Sambandham, Torsten Schon  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-Image models reproduce societal stereotypes, and existing mitigation applies one demographic correction to the whole scene. In multi-person scene generation this creates a trade-off: global steering improves aggregate balance only by homogenizing the people within an image. Steering-based methods like Embedding Arithmetic drive the intra-image diversity below the unsteered baseline. Text- and latent-projection approaches shift the aggregate skew with only marginal gains in intra-image diversity. We present Spatially Gated Steering (SGS), which steers the demographics of each person independently by extracting per-person masks from the Diffusion Transformer's (DiT) internal attention maps at a critical denoising timestep and applying a distinct demographic vector within each mask for the remaining steps. SGS needs no fine-tuning, inversion or layout specifications, and uses a lightweight segmentor over frozen DiT attention features to localize subjects at early timesteps. On skewed occupational prompts, SGS reaches high intra-image racial and gender diversity while keeping aggregate balance competitive and image quality near baseline, a result we validate on two architecturally distinct diffusion transformers, FLUX.1-Dev and SD3.5-Large. Codebase and model weights are available at this https URL

---


### 175. [Probabilistic Machine Learning for Short-Term Atmospheric Seeing Forecasting](https://arxiv.org/abs/2610.29654)

**<font color=#1a73e8>作者：</font>** Mary-Joe Medlej, Rahul Srinivasan, Simon Prunet 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate short-term forecasting of atmospheric seeing is of significant interest for astronomical observations and free-space optical communication systems, where rapid variations in optical turbulence can affect system performance and operational planning. In this work, we benchmark machine learning models for predicting atmospheric seeing up to two hours in advance, with a particular focus on probabilistic forecasting and uncertainty quantification. We compare two probabilistic approaches, Gaussian Processes (GPs) and a normalizing-flow- based model (FloTS), against deterministic recurrent neural network (RNN) and long short-term memory (LSTM) baselines. All models are trained and evaluated on seeing measurements from the Maunakea summit. We assess the models using both deterministic metrics, including the root mean square error and the Pearson correlation coefficient, and probabilistic metrics that evaluate the quality and calibration of predictive uncertainty estimates. The results show that deep learning approaches outperform standard recurrent networks for short-term forecasting, with LSTM and FloTS achieving the best overall predictive accuracy. While Gaussian Processes provide a useful probabilistic baseline, their predictive distributions are limited by the Gaussian assumption. FloTS combines competitive forecasting accuracy with flexible uncertainty quantification and produces the most informative probabilistic forecasts.

---


### 176. [Learning to Reason Like a Cytopathologist:Clinically Grounded Multiscale Evidential Learning for Cervical Cytology](https://arxiv.org/abs/2610.29665)

**<font color=#1a73e8>作者：</font>** Ajeet Kumar Singh, Nehal Mishra, Anurag Tripathi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cervical cytology presents a fundamentally ambiguous diagnostic landscape, where equivocal categories such as Atypical Squamous Cells of Undetermined Significance (ASC-US) occupy a morphological grey zone that is definitional. For clinical decision support, the goal extends beyond assigning a definitive label to every sample: cases must also be distinguished by whether the available evidence supports a confident decision or warrants further consideration, a distinction conventional classification models are not designed to explicitly represent. We propose a multiscale evidential framework that models cervical cytology along an ordinal disease continuum using clinically grounded soft anchors, representing progression from benign reactive changes to precancerous lesions and malignancy. Three biologically motivated spatial contexts--nuclear morphology, cytoplasmic characteristics, and neighbourhood cellular architecture--are independently encoded using a shared frozen DINOv2 backbone, preserving inter-scale disagreement that early fusion may obscure. Calibrated predictions are transformed into Dempster--Shafer belief masses and fused with reliability discounting, allowing conflicting evidence and insufficient support to remain explicitly uncommitted rather than forcing a decision. The fused belief state drives interpretable routing that separates confidently classified cases from those with irreducible evidential insufficiency, enabling clinically meaningful triage. Across two independent publicly available conventional cytology datasets, RIVA and CRIC Cervix, the framework generalises consistently, with uncertainty strongly associated with diagnostic difficulty: incorrect predictions carry 1.94x-4.13x higher uncertainty than correct ones.

---


### 177. [Characterizing Oblivious Common-Reward Multi-Player Bandits: Universal Stationarity, Coordination Traps, and Certified Global Rates](https://arxiv.org/abs/2610.29673)

**<font color=#1a73e8>作者：</font>** Mingxiao Li, Wenhai Lai, Hongyu Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper presents a theoretical analysis of the oblivious common-reward multi-player multi-armed bandit (OC-MPMAB), a minimal multi-player bandit model in which multiple players select arms simultaneously and observe only a shared reward. Crucially, the players are fully oblivious: they do not observe the actions of other players and do not even know whether any other players exist. The contributions of this work are threefold. First, we prove that the independent gradient-bandit updates applied by the players jointly form an unbiased stochastic gradient estimator of a hidden product-policy objective. This property then yields a universal finite-time first-order stationarity guarantee for every instance. Second, we show that stationarity cannot, in general, be strengthened to global optimality. To illustrate this, we identify a product-policy trap obstruction that rules out the guarantee of global optimality. Third, we show that global optimality can be recovered under structural assumptions on the reward table. To make global optimality achievable, we introduce finite-table certificates that separately characterize product-gradient dominance and self-bounding stochastic noise. We then establish certificate-conditioned bounds on the product-policy gap and pseudo-regret. Consequently, the standard $O(1/t)$ product-policy gap and $O(\log T)$ pseudo-regret rates hold when the certificates are uniform.

---


### 178. [DriveMLP: When Training Strategy Outperforms Model Complexity in Autonomous Driving](https://arxiv.org/abs/2610.29676)

**<font color=#1a73e8>作者：</font>** Alessandro Canevaro, Julian Schmidt, Hang Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning motion planning policies that remain reliable under closed-loop execution is a central challenge in Autonomous Driving (AD). Imitation Learning (IL) scales well to large AD datasets but suffers from distribution shift, causal confusion, and compounding errors under closed-loop execution. In contrast, Reinforcement Learning (RL) typically requires handcrafted rule-based rewards and massive simulation. We study a simple closed-loop IL framework that uses RL purely as an optimization tool, guided by a trajectory-distance reward derived from logged expert data. We refer to this training strategy as Expert-Guided RL (EGRL). Through a controlled empirical study we find evidence that the training procedure, rather than model size and complexity, accounts for a substantial part of the performance gains. We then introduce DriveMLP, a lightweight MLP policy trained with EGRL, as a simple instantiation of these findings. It achieves a score of 86.51 on the nuPlan Val14 Reactive benchmark, a +3.2 point improvement over the previous best IL planner (Flow Planner), with >15x faster inference. Code is available at: this https URL .

---


### 179. [Efficient Generative Image Compression with Quantized Latents Refinement](https://arxiv.org/abs/2610.29691)

**<font color=#1a73e8>作者：</font>** Hao Cao, Yinhuan Huang, Wenqi Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative image compression (GIC) delivers strong perceptual quality at low bitrates. However, GIC methods with strong perceptual quality often rely on pretrained diffusion models with high latency, while recent lightweight GIC methods reduce latency but deliver lower perceptual quality. We observe that, for lightweight GIC methods at low bitrates, coarse deterministic quantization can collapse nearby encoder latents corresponding to different fine details to the same point, making these details difficult to recover. Motivated by this, we propose GR-GIC, an efficient GIC that delivers competitive reconstruction performance with fast inference. For better performance, we introduce Guided Refinement (GR), which combines latent refinement guided by entropy context with adaptive perturbations for training regularization, jointly improving reconstruction at low bitrates. For fast inference, we introduce reorganized projected residual vector quantization (P-RVQ), which equivalently reorganizes residual updates into low-dimensional lookups to expose greater parallelism and reduce sequential computation. Experiments on Kodak show that for performance, compared with OneDC, GR-GIC achieves BD-rate savings of 23.19%, 37.71%, 22.30%, and 22.14% for LPIPS, DISTS, PSNR, and FID, respectively. For fast inference, the highly optimized implementation of GR-GIC encodes and decodes in 4.60 and 5.98 ms on an NVIDIA A100. Specifically, the reorganized P-RVQ implementation achieves a $3.14\times$ average speedup over the original implementation under the same FP32 setting. On an NVIDIA Jetson Orin NX, GR-GIC achieves latency comparable to lightweight GIC methods.

---


### 180. [Forward-Only Learning for Shared-Kernel Wavelet Neural Networks without Backpropagation](https://arxiv.org/abs/2610.29697)

**<font color=#1a73e8>作者：</font>** Yongfei Guo, Xuan Sun, Ang Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Backpropagation remains the dominant training paradigm, using backward gradients and local updates that can suffer from vanishing or exploding gradients in deep networks. Although the Forward-Forward algorithm avoids conventional backpropagation, it remains mainly local or layer-wise, motivating global whole-network learning using forward evaluations only. For shared-kernel wavelet neural networks, we therefore propose a CMA-ES-based global forward-only learning framework. We further introduce structure-aware parameter decomposition and channel-specific credit assignment, factorizing the search into three subspaces. On BSDS500, our method reduces test MSE from 4.1783 to 4.0130 and improves PSNR from 42.621 to 42.787~dB over Adam/BP without backward propagation. Beyond these gains, training requires only 6 training-set coverages, compared with 1500 epochs for BP. Ablations show that structural decomposition and aligned credit assignment are more important than increasing population size, demonstrating the feasibility of whole-network forward-only learning for compact reconstruction networks. These results suggest a potential route toward forward-only optimization of compact reconstruction models for resource-constrained imaging and edge or near-sensor systems.

---


### 181. [Beyond Policy Engines: Binding-Complete Execution Admission](https://arxiv.org/abs/2610.29701)

**<font color=#1a73e8>作者：</font>** Lin Wang, Mengting Wu, Yong Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Policy engines determine whether evaluated policies permit a request, but a correct ALLOW decision does not establish complete governance-source participation, exact context binding, or sufficient grounds for execution admission. This paper examines the gap between policy evaluation and execution admission. We introduce the Binding-Complete Execution Admission Contract (BCEAC), a governance-relative contract for independently determined source obligations, exact policy and contextual binding, and typed admission outcomes under explicit trust assumptions. We propose a conditionally engine-agnostic architecture in which participating backends must satisfy declared semantic profiles, adapter contracts, and contextual correspondence obligations; an Execution Boundary Language (EBL) authoring syntax remains optional. The architecture separates governance resolution, policy evaluation, independent admission verification, and downstream execution mediation. We investigate two distinct experimental tracks: a finite Governance Source Completeness study and an OPA/Cedar experiment with archived native-engine records examined by offline review. The OPA/Cedar archive comprises 72 scenarios and 144 strict case-engine records (120 native-invoked and 24 pre-native), with eight additional permissive controls outside the strict denominator. The offline review did not rerun the original native OPA/Cedar executables. The results provide bounded evidence while retaining historical failures and unresolved implementation defects. The work does not establish constitutional adequacy, general semantic refinement, authenticated currentness, machine-checked execution-safety theorems, or protected external effects. Its contribution is an explicit, falsifiable framework for determining what must be established between a policy decision and an execution-admission judgment.

---


### 182. [Structure-Aware Message Passing on Petri Nets through Directed Walks and Incidence Diffusion](https://arxiv.org/abs/2610.29725)

**<font color=#1a73e8>作者：</font>** Geri Skenderi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A common application of the process mining discipline is to connect observed event data with Petri nets, which are bipartite, directed graphical process models with rich formal underpinnings. Recent work learns vector representations of Petri nets to retrieve process models and relate them to event logs, but leaves implicit two key aspects hidden within the net's structure: directed cycles (process loops) and invariants recorded by the net's incidence matrix. We expose both of these to message-passing graph neural networks, through a positional encoding built from return probabilities of directed place-transition walks (PNRWPE), and through same-type messages gated by diffusion kernels of the incidence matrix (DA-PNGNN). Our constructions raise macro balanced accuracy in predicting the generation factors of the 96 Process Discovery Contest 2023 models from 0.751 to 0.796 with PNRWPE, which nearly doubles accuracy on process loops, and to 0.830 with DA-PNGNN, which, without retuning, also improves net-to-tree retrieval top-1 accuracy on the self-supervised ProcRosetta benchmark by 4.1 to 5.9 points.

---


### 183. [Learning to Measure and Diagnose: A Clinical-Dictionary Radiomic Bottleneck Model for Thyroid Nodule Classification](https://arxiv.org/abs/2610.29738)

**<font color=#1a73e8>作者：</font>** Guibin Zhang, Weier Luo, Lei Cao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Thyroid ultrasound supports the assessment of nodule malignancy, but classification predictions often lack evidence linked to familiar clinical descriptions. Radiomics provides explicitly defined measurements that can support such explanations through a clinical dictionary. However, using these measurements as interpretable evidence requires reliable estimation from ultrasound images and preservation of measurement fidelity when optimizing classification performance. We propose a clinical-dictionary radiomic bottleneck model for thyroid nodule classification. Within this model, Family-Aware Radiomic Learning (FARL) estimates measurements with balanced supervision across feature families. Fidelity-Guided Bottleneck Modeling (FGBM) constructs a fixed bottleneck, followed by joint optimization of measurement estimation and classification under fidelity guidance. Decision evidence decomposition then traces feature contributions through a linear classifier and organizes them by clinical dictionary categories. Experiments on ThyroidXL and TN3K show competitive classification performance, while case studies illustrate feature contributions for benign and malignant nodules. These findings indicate interpretable classification with inspectable quantitative evidence informed by clinical knowledge. Code is available online.

---


### 184. [APED-CXR: Adaptive Privileged Evidence Distillation for Chest X-Ray Grounding with Image-Only Inference](https://arxiv.org/abs/2610.29740)

**<font color=#1a73e8>作者：</font>** Md Shihabul Islam Shovo, Nishi Kanta Paul, Jamil Fayyad  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Compact chest X-ray (CXR) models that localize findings suit deployment, but box annotations are limited and report-aware multimodal models are expensive at inference. We introduce APED-CXR, which distills report-informed spatial evidence from a frozen multimodal teacher into a student with 11.1M parameters that predicts diseases and boxes from shared evidence maps and requires the image alone at test time. During training, the teacher uses the radiograph, report, and queried class to evaluate regions proposed from the student's current evidence maps, and its support scores serve as training targets for the student's pooled evidence scores within these regions. Trained on PadChest and evaluated on held-out PadChest-GR, refreshing the student's proposals for teacher evaluation improves box-level localization F1 from 0.302 with fixed warm-up proposals to 0.338 (IoU >= 0.5; gain 0.036, 95% CI [0.022, 0.049]), while maintaining diagnostic AUC. This gain depends on the teacher checking current proposals: with equally many random boxes, a fixed dense box set, teacher-generated boxes, or report rules instead of the teacher, F1 stays near the fixed-proposal level, and proposals two refreshes old recover only part of the gain. On NIH ChestX-ray14, a secondary test set, box recall also rises from 0.423 to 0.447.

---


### 185. [LEAF-Mamba: Feature Adaptation and Fusion for Whole Slide Image Analysis](https://arxiv.org/abs/2610.29746)

**<font color=#1a73e8>作者：</font>** Lubin Gan, Jing Zhang, Mingjun Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Whole slide image (WSI) analysis enables computational diagnosis and prognosis, but gigapixel images and limited annotations make slide-level learning challenging. Multiple instance learning addresses this task by aggregating patch representations from frozen pretrained encoders. Recently, Mamba has enabled efficient modeling of long patch sequences. However, task supervision alone does not explicitly constrain information recovery during feature adaptation, while Mamba couples local processing with long-range propagation rather than retaining separate representations for fusion. Motivated by these challenges, we introduce LEAF-Mamba, a framework that jointly addresses latent evidence adaptation and fusion for frozen-feature WSI analysis. A reconstruction-regularized adapter learns compact, task-specific representations while reconstructing the input features. Parallel Mamba and convolutional streams then capture long-range dependencies and sequence-local interactions, with an input-dependent gate modulating their joint representation before slide-level pooling. Experiments across feature extractors demonstrate improved average performance over strong MIL baselines in both diagnostic classification and survival prediction. Component analyses further support the contributions of adaptation and fusion. These findings highlight the value of jointly designing feature transformation and contextual aggregation to translate pretrained representations into effective slide-level predictions.

---


### 186. [UniRAP: Towards Unified Part-level Physical Affordance Reasoning and Actionable Perception](https://arxiv.org/abs/2610.29768)

**<font color=#1a73e8>作者：</font>** Linfei Li, Ruining Hu, Lin Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language perception has achieved impressive progress in aligning natural language with visual observations, yet grounding high-level semantics into part-level physical interaction remains challenging. To address this gap, we propose UniRAP, a unified model for inferring part-level physical affordances and mapping language instructions to actionable geometric representations. UniRAP formulates this problem as a conditional multimodal generation task, integrating visual inputs, textual instructions, and optional prompts into a shared spatiotemporal representation space through a unified interface token mechanism. To predict executable contact geometry, we introduce a Unified Affordance Decoder (UAD), which jointly performs object detection, part-level affordance segmentation, and 4-DoF interaction pose estimation by leveraging intermediate segmentation features. In addition, we propose a curriculum-based transfer training strategy that progressively adapts the model from general visual parsing to interaction-aware perception, improving data efficiency under limited textual annotations. Experiments show that UniRAP achieves state-of-the-art performance on referring expression segmentation, affordance grounding, and interaction pose estimation, while maintaining strong spatiotemporal consistency in dynamic video scenarios. These results demonstrate the effectiveness of UniRAP as a unified perception framework for language-guided physical manipulation.

---


### 187. [Location-of-interest vs. Current-location Privacy in Multi-hop Communication](https://arxiv.org/abs/2610.29772)

**<font color=#1a73e8>作者：</font>** Ryan Vogt, Ioanis Nikolaidis, Mario A. Nascimento  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Consider a standard multi-hop wireless radio network in which nodes relay messages for one another. While the contents of messages may be sensitive and thus encrypted, the very fact that two radios communicated can leak sensitive information about both the physical location of the origin and the physical location of the destination. We investigate the trade-off between protecting the privacy of a user's current location and the privacy of their location of interest, and how the user should choose dummy destinations to obfuscate their queries.

---


### 188. [Key Findings for Small UAS for Post-Disaster Damage Assessment from the CURSE'26 Exercise](https://arxiv.org/abs/2610.29777)

**<font color=#1a73e8>作者：</font>** Thomas Manzini, Stephen Johnson, Priyankari Perali 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The CLARKE building and road damage assessment AI classifier was incorporated into the Catastrophic Unmanned Remote Sensing Exercise (CURSE) 2026, which trained 23 small uncrewed aerial systems (sUAS) teams from state and local agencies and non-governmental organizations in Florida and Missouri on how to collect imagery for an incident command Remote Sensing Cell. Although CLARKE has been operationally deployed to two hurricanes (Debby and Helene), CURSE'26 presented an opportunity to evaluate the machine learning model with a larger set of never-before-seen orthomosaics. The results show that building and road damage assessment together ran in 3.5 minutes on average, and that building damage assessment achieved a Micro F1 of 0.834 with no manual adjustments to correct spatial misalignment and delivered that performance in both Florida and Missouri, demonstrating good geographic transfer. It also showed that road damage assessment performed poorly due to sensitivity to misalignment between road maps and the images, and to lighting and environmental conditions in an urban setting. The analysis of CURSE'26 presents five other findings of value to the sUAS community: that the use of sUAS and machine learning is now operationally normalized and accepted, sUAS teams in the field can improve classification accuracy by timing their flights, exercises are good operational tests but their value for evaluating learning models is less clear, edge computing is needed to overcome the wireless upload barrier, and the application of sUAS and AI to disaster response has ethical and legal ramifications for pilots and data managers.

---


### 189. [JointLight: Human-Centric Video Relighting with Asynchronous RGB-Irradiance Joint Modeling](https://arxiv.org/abs/2610.29780)

**<font color=#1a73e8>作者：</font>** Henglei Lv, Bailin Deng, Xiaoqiang Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding and modeling light transport in human-centric scenes is a longstanding challenge. While recent progress in diffusion models has boosted research in relighting, precise illumination control still lags, primarily due to the scarcity of diverse, high-quality, precisely labeled video relighting datasets. Existing end-to-end relighting approaches model light transport implicitly through neural networks, which substantially complicates controllability. In contrast, some works resort to path-traced irradiance cues as an explicit blueprint for light transport. However, such constructed irradiance cues are prone to artifacts and hinder generative quality when directly used as control signals. With the key observation that noise corruption removes high-frequency artifacts and preserves low-frequency light transport, we introduce an asynchronous joint-modeling paradigm that facilitates fine-grained illumination control. During two-stage training, we force the model to jointly denoise RGB and ground-truth irradiance frames with separate timesteps scheduling. A domain matching strategy is applied to the second stage to bridge the domain gap between irradiance cues and ground-truth irradiance maps. At inference time, we introduce an asynchronous hijacked generation pipeline that facilitates flexible illumination control. For training data, we develop a multi-illumination high-quality synthetic video dataset with paired irradiance maps using a powerful game engine. Trained exclusively on this dataset, our model exhibits robust generalization to real- world scenarios and outperforms prior approaches in both lighting fidelity and generative quality. The code and dataset will be publicly released.

---


### 190. [Open-Vocabulary Models and Label Propagation for Uncertainty-aware Pseudo-Labeling of Object Detection Datasets](https://arxiv.org/abs/2610.29788)

**<font color=#1a73e8>作者：</font>** Jonathan Klees, Timo Heller, Matthias Rottmann  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object detection models rely on large-scale annotated datasets that require substantial manual annotation effort. The labeling costs further increase when annotation uncertainty is captured through soft labels, as multiple annotations must be collected for each object. We address this challenge by introducing a semi-supervised framework for the uncertainty-aware annotation of object detection datasets. Our approach leverages open-vocabulary object detectors to generate region proposals and semantically meaningful object representations. Based on these representations, we construct an object-level similarity graph and propagate probabilistic label information. Our framework assigns soft labels to previously unlabeled objects, quantifying both aleatoric and epistemic uncertainty. We evaluate our method on four object detection benchmarks with soft-label annotations and demonstrate that high-quality annotations can be obtained with only a small fraction of manually labeled objects. Furthermore, we show that detectors trained on semi-automatically annotated data achieve performance comparable to models trained on fully manually annotated data. We achieve state-of-the-art downstream detection performance for the task of semi-supervised object detection on the COCO dataset, with 40.5% AP virtually matching the performance of the model trained on fully manually constructed data (40.9%) at only 1% of labeling costs. These results highlight the potential of open-vocabulary models and graph-based label propagation for efficient, accurate and uncertainty-aware pseudo-labeling.

---


### 191. [Asymmetric Likelihood-Free Hypothesis Testing](https://arxiv.org/abs/2610.29798)

**<font color=#1a73e8>作者：</font>** Gunjan Kumar, Yash Pote, Jonathan Scarlett  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In likelihood-free hypothesis testing (LFHT), given samples from two unknown distributions $P,Q$ on $[n]$ with $\mathrm{d_{TV}}(P,Q)\geq\varepsilon$, and from a third distribution $D\in\{P,Q\}$, the goal is to identify whether $D=P$ or $D=Q$. We study asymmetric likelihood-free hypothesis testing, where the sample budgets $s_P$ and $s_Q$ for $P$ and $Q$ may differ, and characterize the feasible triples $(s_P,s_Q,s_D)$ up to logarithmic factors. We establish that unequal reference budgets can give a polynomial saving. For instance, for constant separation, $n$ samples from $P$ and $n^{3/4}$ from $Q$ allow testing with $\widetilde O(n^{1/4})$ samples from $D$, whereas both existing baselines---symmetric LFHT and unequal-sample closeness testing---require $\Omega(\sqrt n)$ samples from $D$.
We further apply our results to non-adaptive distribution 2-clustering, where the sample allocation among $k$ distributions must be fixed before observing any data. We obtain matching upper and lower bounds for this problem up to logarithmic factors in terms of the domain size, number of distributions, smaller cluster size, and separation, both with one cluster distribution known and with both unknown. Comparing with known bounds for adaptive sample allocation gives a worst-case adaptivity gap of $\widetilde\Theta(k^{1/4})$.

---


### 192. [COMET: A coordinated multi-layer runtime monitoring framework for human-supervised AI-enabled safety systems](https://arxiv.org/abs/2610.29816)

**<font color=#1a73e8>作者：</font>** Niclas Flehmig, Mary Ann Lundteigen, Shen Yin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Incorporating AI systems into safety systems requires monitoring to avoid silent faults and ensure safe and reliable operation. Single monitors often do not provide actionable information for human supervisors, who act as the system's adaptive controller. We present COMET, a coordinated multi-layer runtime monitoring framework for human-supervised AI-enabled safety systems in which each monitor is anchored in a different fault mode. Monitor outputs are combined in a coordination layer and mapped by a communication layer to a traffic-light display. In this work, COMET consists of three monitoring layers: signal integrity, physics consistency, and the AI system's competence envelope. The framework is evaluated on an open dataset of compressed-air leaks, where an AI system detects leaks from acoustic emissions, with held-out conditions simulating covariate shift, semantic shift, and sensor faults, events expected during runtime but unknown in their exact appearance. All monitors are frozen after development and tested zero-shot, and the framework is compared against no-monitoring and single-monitor setups. The bare AI system fails silently and confidently under all three shift types, whereas COMET reduces the trusted-wrong-answer rate to zero on covariate-shifted no-leak data and on three of four sensor faults, at a nominal false-alarm rate of $\approx 1\%$. Single monitors come close in detection but cannot attribute the fault mode. COMET converts their anonymous detection flags into diagnoses. Residual silent misses under semantic shift define the boundary of passive monitoring. Runtime monitoring frameworks for AI-enabled safety systems must therefore combine quantitative fault detection and isolation with qualitative, human-oriented feedback.

---


### 193. [GuidedSAM-Plume: An Expert-Guided Segmentation Framework for Volcanic Plumes](https://arxiv.org/abs/2610.29825)

**<font color=#1a73e8>作者：</font>** Taddeo D'Adamo, Simon Thivet, Catherine Pothier 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Quantitative analysis of environmental phenomena increasingly relies on image-based measurements. In volcanology, the geometric characterization of volcanic plumes and clouds from RGB images remains hindered by the scarcity of dedicated segmentation solutions and partially handcrafted annotations remain widely prevalent. We present GuidedSAM-Plume, an open-source expert-guided framework tailored for the interactive segmentation of volcanic plumes and clouds. It leverages the zero-shot, spatial prompt-based capabilities of SAM2. The framework was thoroughly validated on a challenging dataset through dedicated segmentation metrics and field-relevant volcanological descriptors. From minimal user inputs, it is able to significantly increase performance compared to fully automatic dedicated solutions while preserving the reliability of derived volcanological parameters. The absence of retraining requirements lowers adoption barriers within the volcanological community, and the framework's demonstrated suitability for complex, diffuse plume-shaped phenomena extends its applicability to broader environmental science domains. The re-annotated dataset, produced under the guidance of expert volcanologists within the proposed framework, ultimately yields a more standardized release. The framework and accompanying dataset are made available at this https URL.

---


### 194. [Early versus Late RGB-Infrared Fusion for Counter-UAV Detection: A Comparative Study](https://arxiv.org/abs/2610.29828)

**<font color=#1a73e8>作者：</font>** Alberto De Zan, Denis Tavaris, Gian Luca Foresti 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents a novel strategy for UAV detection through visible (RGB) and infrared (IR) fusion, in order to improve accuracy and precision in harsh environments and weather conditions. In this research, two opposite approaches have been studied and implemented: the first concerns image-level (early) fusion, which merges two different spectra into a single image to which one detector is applied. On the other hand, the second approach, called decision-level (late) fusion, focuses on blending together the output bounding boxes of two different detection pipelines, aiming to create a common result that can be applied to both spectra simultaneously. Both strategies have been extensively tested in a dedicated environment, which included alternating low and high brightness scenes, different backgrounds (sky and ground), distances (5, 25 and 60 m), altitudes and zoom levels (1X, 2X and 4X). These tests allowed for the assessment of actual detection capabilities and system reliability in real-world applications. Furthermore, the two fusion strategies were evaluated and compared over a set of aligned images in order to highlight the better approach of the two. The results indicate that early fusion achieves better raw performance, since it incorporates the thermal information from the beginning of the training process. However, late fusion presents an innovative and useful detection workflow that can be applied in cases of sensor or frame misalignment. Both positive and negative aspects have also been pointed out and discussed, in order to give a more comprehensive overview. Finally, the paper outlines implementation considerations and practical recommendations based on operational priorities. Overall, the findings contribute to the research in RGB-IR fusion modalities, with the goal of enhancing UAV detection capabilities.

---


### 195. [Revealing Hidden Failure Modes in Chest X-ray Classification via Spectral Domain Analysis](https://arxiv.org/abs/2610.29830)

**<font color=#1a73e8>作者：</font>** Samuel Halimi, Loic Themyr, Arnaud Abreu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning models for chest X-ray anomaly detection remain vulnerable to subtle distributional shifts (e.g., acquisition technique, patient-related factors, and preprocessing). Traditional error analysis often relies on semantic metadata or model embeddings, which can mask low-level signal variations that degrade performance. In this work, we propose a data-centric framework for automated failure mode discovery using spectral analysis. We project images into the frequency domain and extract a compact profile summarizing the distribution of signal energy across frequency bands. By performing unsupervised clustering on these spectral profiles, we demonstrate that model failures are not randomly distributed, but are strongly concentrated within specific spectral clusters. This method effectively isolates "blind spots", enabling the prediction of model reliability and the discovery of performance-degrading data slices without requiring ground-truth failure annotations.

---


### 196. [Linear Self-Symmetries of Inverse-Based S-boxes: Generic Rigidity and Applications](https://arxiv.org/abs/2610.29837)

**<font color=#1a73e8>作者：</font>** Zheng Zhang, Na Zhang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Finite-field inversion is a basic nonlinear building block in the design of S-boxes for symmetric cryptography. In inverse-based S-boxes, finite-field inversion is often combined with linear or affine layers that may preserve or destroy algebraic symmetries of the inverse function. We study how often nontrivial linear self-symmetries remain as the outer invertible linear transformation varies over \(GL_n(\mathbb F_2)\). Using the classification of two-sided linear equivalences of inversion, we reduce the problem to semilinear conjugacy and centralizer estimates. We obtain matching upper and lower bounds for the probability that a nontrivial linear self-symmetry remains, and these bounds determine its leading quadratic exponent. This exponent is governed by the smallest prime divisor of the extension degree. Thus the decay rate depends on the arithmetic of the field extension and not only on its dimension. As cryptographic applications, we provide a practical rigidity criterion, prove that the full AES S-box has no nontrivial linear self-symmetry, and illustrate the broader relevance of the framework through ARIA and Vision.

---


### 197. [How Do DiTs Denoise? An Aggregator-Predictor View of Attention and MLPs](https://arxiv.org/abs/2610.29854)

**<font color=#1a73e8>作者：</font>** Gyeonghun Kang, William Xingxu Chen, Xiang Cheng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> How do diffusion transformers (DiTs) represent image content and learn rules for reusing it to generalize? We develop an aggregator--predictor view of DiTs as input-adaptive local denoisers, in which context aggregation and patch prediction provide functional roles for interpreting attention and MLPs. We first establish that, for Gaussian Markov random field (GMRF) priors, the global Bayes denoiser can be approximated using only a subset of context patches, with error decaying exponentially in context radius. We further show that patchwise linear denoisers, often invoked to explain diffusion generalization, recover the empirical local denoiser with sufficiently informative aggregation. Within this view, AdaLN-modulated attention naturally parameterizes an input- and noise-dependent aggregator, while the MLP admits a learned key--value representation for tokenwise patch prediction. Our experiments support this view. DiTs trained on real images exhibit noise-dependent denoising contexts resembling those in the analytic GMRF setting, while attention mass exhibits a qualitatively corresponding broadening pattern. In a controlled CelebA64 study, shared-memory patch predictors used in place of DiT MLPs achieve competitive denoising and generative performance. Finally, cross-dataset component transplantation reveals compatibility patterns consistent with the proposed roles of QK in spatial weighting, VO in feature transport, and MLPs in patch prediction. Together, these results provide a component-level account of DiT denoising and motivate architecture-specific fine-tuning and controlled intervention.

---


### 198. [Stochastic Nonlinearities Improve Uncertainty Estimation](https://arxiv.org/abs/2610.29875)

**<font color=#1a73e8>作者：</font>** Mohammad Sarhangzadeh, Amirreza M. Shebly, Doruk Oner  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable uncertainty estimation is important across visual recognition tasks, providing information about the confidence and reliability of model predictions. Many uncertainty estimation methods obtain predictive diversity through mechanisms that can suppress intermediate features, perturb the input, or require substantial additional computation. Stochastic activation functions, where network units randomly select between multiple nonlinearities during a forward pass, have previously been used to improve optimization behavior, mitigate limitations of fixed ReLU activations, and increase output diversity. In this work, we reframe stochastic activation switching as a lightweight mechanism for uncertainty estimation. The proposed method samples between nonlinear activation functions, inducing predictive diversity while keeping intermediate feature pathways active. This enables uncertainty estimation from a single trained model without the training cost of ensembles, task-specific uncertainty heads, or architectural redesign. We evaluate the proposed approach across classification, semantic segmentation, and out-of-distribution detection using convolutional and transformer-based architectures on diverse datasets. Across these settings, stochastic activation switching improves uncertainty quality while preserving competitive primary-task performance, showing that stochastic nonlinearities provide an effective and information-preserving source of predictive variation for visual recognition.

---


### 199. [Expandable Modality Experts for Medical Vision-Language Learning](https://arxiv.org/abs/2610.29881)

**<font color=#1a73e8>作者：</font>** DM BAPPY, Eunsu Kim, Hanjoo Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning across medical imaging modalities requires making use of images without paired text and accommodating new domains while retaining existing representations. We propose a medical vision-language technique built around an expandable bank of modality experts. Its Multiway Transformer combines shared visual computation with deterministically routed feed-forward experts and a separate text pathway. A modality-aware visual tokenizer supplies targets for masked pretraining on 19.4 million unpaired image rows across seven modalities; contrastive alignment then uses 3.23 million image-text pairs. Additional fundus and optical coherence tomography experts learn from paired data while the original image and text embedding paths remain frozen. With a ViT-Large backbone, the proposed technique achieves the best or tied-best result in 24 of 25 benchmark settings across nine modalities: 10 of 11 zero-shot classification benchmarks, all 10 linear probes, and all four retrieval benchmarks. Mean balanced accuracy is 0.674 for zero-shot classification and 0.856 for linear probing, and mean bidirectional retrieval recall is 20.70%. A separate three-seed sequential experiment with matched adaptation data yields fundus and OCT retrieval gains of 14.95 and 9.31 percentage points, with no measured loss on preceding fundus or pathology tasks. The preservation argument requires unchanged existing computation paths and inference conditions, and feature-identity checks verify retention on evaluated inputs. The proposed technique provides a modular approach to learning and expanding medical vision-language representations.

---


### 200. [A Sharp Dynamic Haussler Lemma](https://arxiv.org/abs/2610.29898)

**<font color=#1a73e8>作者：</font>** Shihao Shao, Dacheng Tao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Haussler's covering lemma (JCTA 1995) gives the sharp $(C/\delta)^d$ metric-entropy bound for binary VC classes under normalized $\ell_1$ distance. We prove a sharp global dynamic analogue for bounded real-valued classes in normalized $\ell_p$, for every $1\le p<\infty$. Writing $d=\operatorname{sfat}_{\varepsilon/32}(\mathcal F)$, we obtain a global dynamic cover of size at most $(C/\varepsilon^p)^d$ for every horizon and $0<\varepsilon<1/2$. Here a single family of deterministic causal experts, fixed independently of the instance sequence, covers every target on every sequence. For $0<\varepsilon<1/4$, a matching worst-case lower bound $(c/\varepsilon)^{pd}$ holds already for binary classes on one fixed sequence, even with real-valued experts. The constants are universal, independent of $p$.
For $p=2$, this resolves the horizon-independent sequential $\ell_2$ covering problem of Rakhlin, Sridharan, and Tewari (PTRF 2015) in a stronger global form. For $p=1$, it gives the sharp $(C/\delta)^{\operatorname{Ldim}(\mathcal H)}$ global dynamic covering bound for binary classes, resolving questions of Alon, Ben-Eliezer, Dagan, Moran, Naor, and Yogev (STOC 2021) and Malliaris and Moran (Trans. AMS 2024). Our proof combines rank-decreasing correction schedules and accurate sampled prefixes with exact continuations after target identification. Shared-parent routing distributes these continuations among eligible prefixes, eliminating the logarithmic overhead.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-232](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
