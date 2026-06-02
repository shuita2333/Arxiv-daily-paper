# 📦 其他研究 | 2026年06月03日

> 本类共 **651** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**451-500**（第 10/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-651](./part-14.md)

---

### 451. [Stochastic convergence of parallel asynchronous adaptive first-order methods](https://arxiv.org/abs/2606.01787)

**<font color=#1a73e8>作者：</font>** Serge Gratton, Philippe L. Toint  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A new class of asynchronous adaptive first-order optimization methods is introduced, comprising asynchronous variants of several popular algorithms. Versions of these methods using momentum and/or inexact normalization are also considered. The convergence of methods in the class on non-convex functions is analyzed in a fully stochastic setting, and is shown to be (up to logarithmic factors) of order O(1/sqrt{t}) under reasonable assumptions. Numerical experiments suggest that such asynchronous adaptive algorithms are very relevant in heterogeneous large-scale machine learning systems.

---


### 452. [PlatonicNav: Unveiling Semantic Correspondence in Navigation with Platonic Topological Maps](https://arxiv.org/abs/2606.01788)

**<font color=#1a73e8>作者：</font>** Junlin Long, Zeyu Zhang, Xu Deng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embodied visual navigation, where an agent perceives a complex environment and acts to reach a goal from raw sensory input, underpins a wide range of applications such as household service robotics, assistive robotics, and large-scale autonomous exploration. However, recent attempts to unify vision-and-language navigation (VLN) and object goal navigation (ObjNav) remain at the level of architectural fusion, mixed-task training, and large vision-language pretraining, without examining whether independently trained vision and language encoders may already share a common semantic structure. Moreover, even object-centric topological maps still ground language goals through explicit cross-modal supervision such as CLIP or large vision-language models, leaving open whether such grounding is possible from a purely vision-built map. To address these challenges, we extend the Platonic Representation Hypothesis to embodied navigation and recast vision-only ObjNav, cross-modal ObjNav, and VLN as three different interfaces to the same object-centric semantic manifold. We further introduce PlatonicNav, a training-free framework whose Platonic Topological Map fuses geometric and semantic node distances from a self-supervised visual encoder, and grounds language goals via blind matching without any paired vision-language data. Extensive experiments on simulation benchmarks including HM3D-IIN, OVON, and R2R-CE on MP3D, together with deployment on Unitree Go2, demonstrate that PlatonicNav generalizes across tasks, modalities, and embodiments without explicit cross-modal training. Code: this https URL. Website: this https URL.

---


### 453. [Consistency evaluation of benchmarks used for causal discovery](https://arxiv.org/abs/2606.01789)

**<font color=#1a73e8>作者：</font>** Yuzhe Zhang, Chihui Chen, Lina Yao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In graphical causal model, causal discovery aims to construct a causal graph based on numerical data and domain knowledge in plain text. However, the evaluation of causal discovery methods remains a challenge in the area as the progress of domain researches often makes benchmark causal graphs contain mis-aligned knowledge. This problem especially affects the evaluation of large language model (LLM) based causal discovery methods as they are sensitive to the new discoveries in the literature. This work is the first to systematically study the quality of benchmark causal graphs. Specifically, we design a pipeline that automatically retrieves relevant research papers from scientific databases, and prompts LLMs to check the consistency between the benchmark causal graphs and domain research papers. We evaluate 11 popular real-world benchmarks, for which our pipeline in total proceeds 38,081 domain papers. Our results show that popular benchmarks vary significantly in their consistency with domain research, with clear implications for causal discovery research.

---


### 454. [Tridirectional Discriminating-Power Formal Verification of Smart Contract Reentrancy Defense Against Production-Deployed Solidity Source](https://arxiv.org/abs/2606.01794)

**<font color=#1a73e8>作者：</font>** Ray Iskander  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present the first machine-checked correctness proof of the OpenZeppelin reentrancy-guard pattern against a Lean 4 state-machine model of production-deployed Solidity source. All thirteen theorems are machine-checked with zero sorry, zero user-introduced axioms, and an axiom footprint bounded by [propext] (a standard mathlib4 axiom), gated under continuous integration.
Smart contract reentrancy has caused over US$500M in documented losses since 2016, with the DAO 2016 attack draining ~3.6M ETH and forcing the hard fork that split Ethereum. The OpenZeppelin ReentrancyGuard pattern is the de facto defense across production DeFi, yet no prior work has established its discriminating power: that the guard blocks attacks on vulnerable instances, preserves correct execution for non-attacking transactions, and distinguishes adjacent safe and vulnerable variants. Prior efforts formalized either guard correctness on toy contracts or attack feasibility on isolated instances - not both directions plus boundary cases against production source.
We verify three production instantiations - DAO 2016, Compound v2, and Aave V3 flashLoan - plus a minimal-diff mutant of Aave V3's flashLoan (flashLoanVulnerable) isolating one security-critical difference, via mutation testing. The tridirectional structure pairs (a) attack reproduction of the DAO 2016 pattern, (b) a correctness proof for Compound v2, and (c) a boundary-case proof distinguishing Aave V3's CEI-correct flashLoan from the mutant. A capstone meta-theorem composes the three under a no-retrofit discipline, demonstrated at the first cross-protocol stress test (Compound v2 to Aave V3); broader-family portability is future work.
Full Lean 4 source, CI config and reproduction commands are at this https URL, reproducible at v1.6-phase7-closure (substrate: v1.3-layer6-closure).

---


### 455. [Tree-Guided Identify-Then-Exploit: A Unified Framework of Best Arm Identification and Regret Minimization for Dueling Bandits](https://arxiv.org/abs/2606.01799)

**<font color=#1a73e8>作者：</font>** Pu Wang, Yao-Xiang Ding  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study $N$-armed stochastic dueling bandits under the Condorcet-winner assumption, where three widely adopted objectives are considered: best-arm identification (BAI), weak regret, and strong regret. We propose Tree-Guided Identify-Then-Exploit (TG-ITE), the first unified framework to tackle all these objectives to our knowledge. Without requiring stronger assumptions, we propose a shared tree-guided identification approach to find a high-confidence incumbent within $O(N)$ comparisons. We further propose varied exploitation strategies to utilize this warm-start stage to optimize the specific objectives at hand. This methodology enables our approach to (1) achieve $O(N)$ sample complexity in BAI without commonly adopted stronger assumptions; (2) build the first winner-stays-style algorithm to achieve $O(N)$ weak regret; (3) enjoy the same $O(N \log T)$ guarantee as specialized strong-regret approaches; (4) realize the joint optimization of BAI and weak regret with $O(N)$ guarantees for both, eliminating the sub-optimal gap of $O(\log N)$ in the existing approach. Our results provide evidence that the trade-off between BAI and regret minimization is relatively benign in dueling bandits.

---


### 456. [Personalized 3D Myocardial Infarct Geometry Reconstruction from Cine MRI for Cardiac Digital Twins](https://arxiv.org/abs/2606.01808)

**<font color=#1a73e8>作者：</font>** Yilin Lyu, Mark YY Chan, Ching-Hui Sia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate 3D geometric characterization of myocardial infarction (MI) is essential for building cardiac digital twins (CDTs) to precisely simulate infarct-related electrophysiology. Late gadolinium enhancement magnetic resonance imaging (LGE MRI) is the clinical reference for locating MI, yet its reliance on contrast agents restricts use in renally impaired patients and limits longitudinal follow-ups. As an alternative, contrast-free cine MRI visualizes abnormal ventricular wall motion, which is highly indicative of the infarcted area. In this study, we propose a novel explicit geometry-motion embedded model to fully automatically reconstruct personalized, simulation-ready 3D MI geometries directly from multi-view cine MRIs. Specifically, we construct a 4D (3D + t) biventricular mesh to explicitly extract and decouple geometry-aware and motion-aware features. We further design a dual-branch module for adaptive geometry-motion fusion to capture spatiotemporal dependencies for mapping infarcted region. Furthermore, we introduce multi-scale supervision utilizing an AHA-17 segment-guided cross-attention mechanism to steer the prediction, ensuring biophysically consistent reconstruction. Experimental results on 225 cine MRIs demonstrated that the proposed 3D MI reconstruction achieved high performance with an average Dice score of 0.678 $\pm$ 0.011. In the downstream in-silico electrophysiological simulation evaluations, the results were highly consistent with the LGE-derived ground truth, highlighting the great potential of the proposed model for contrast-free scar characterization and seamless integration into CDT modeling. The code will be released publicly upon acceptance of the manuscript for publication.

---


### 457. [Token Predictors Are Not Planners: Building Physically Grounded Causal Reasoners](https://arxiv.org/abs/2606.01810)

**<font color=#1a73e8>作者：</font>** Zheng Lu, Mingqi Gao, Qinlei Xie 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current benchmarks for embodied vision-language planning often favor linguistic next-token prediction over physically grounded next-state reasoning. This rewards models that mimic statistical language priors rather than track causal dependencies, reducing physical planning to shallow sequence modeling. We argue that reliable physical autonomy requires a shift from linguistically grounded token prediction toward physically grounded causal reasoning. To this end, we introduce Causal-Plan-Bench, a high-fidelity diagnostic suite curated through multi-stage verification to evaluate embodied planning across four causal dimensions. We also construct Causal-Plan-1M, a million-scale corpus of explicit reasoning traces produced by a four-stage annotation pipeline over egocentric videos. Extensive evaluation shows that leading models still struggle to demonstrate genuine physical agency, with Gemini 3 Pro reaching only 38.18 on our benchmark. In contrast, our training recipe enables Causal Planner, built on Qwen3-VL-8B, to internalize physical logic for more accurate next-state estimation. The model achieves strong in-domain performance and cross-benchmark generalization, and reveals a Causal Scaling Law: scaling causal training data to one million instances yields a 36.3% relative gain, from 33.22 to 45.28. Overall, our work provides a concrete step toward turning agents from superficial token predictors into physically grounded causal reasoners.

---


### 458. [Cost-Aware Diffusion Draft Trees for Speculative Decoding](https://arxiv.org/abs/2606.01813)

**<font color=#1a73e8>作者：</font>** Shuai Zhang, Huachuan Qiu, Hongliang He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates inference by having a lightweight drafter propose tokens verified in parallel by the target language model. Block diffusion drafters such as DFlash generate an entire draft block in one pass, yielding per-position marginals; DDTree uses these to build a candidate tree that maximizes expected acceptance length under a fixed node budget. We observe, however, that acceptance length is non-decreasing in budget: it always favors larger trees regardless of verification cost, offering no principled basis for budget selection. We introduce \textbf{CaDDTree} (Cost-aware Diffusion Draft Tree), a method that directly optimizes token throughput (expected tokens generated per unit time) by jointly selecting the tree structure and node budget. We model draft and verification latencies explicitly, show that the throughput objective decomposes into a per-round one-dimensional search over the budget, and prove that under a convex verification cost the throughput function is \emph{unimodal}, enabling an efficient greedy stopping rule. CaDDTree requires no offline budget search, adapting the budget each round from the current per-position distributions and verification cost. Experiments on Qwen3-4B and Qwen3-8B across eight benchmarks spanning reasoning, coding, and instruction-following tasks show that \caDDTree{} matches or surpasses DDTree with oracle budget selection on nearly all tasks.

---


### 459. [Unsupervised Collaborative Domain Adaptation for Driving Scene Parsing](https://arxiv.org/abs/2606.01818)

**<font color=#1a73e8>作者：</font>** Jiahe Fan, Shaolong Shu, Mingjian Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable driving scene parsing is a fundamental capability for autonomous vehicles operating in open and dynamic driving environments. However, adapting perception models to new deployment domains remains challenging because pixel-level annotations are expensive to obtain, while source-domain data are often inaccessible due to privacy, security, or ownership constraints. Existing source-free unsupervised domain adaptation methods typically rely on a single pre-trained source model, which makes the adapted perception system vulnerable to source-specific biases and limits its robustness under diverse road layouts, illumination conditions, weather patterns, and traffic conditions. This article presents an unsupervised collaborative domain adaptation (UCDA) framework for driving scene parsing in a source-free setting, which transfers complementary knowledge from multiple pre-trained source models to a unified target model without accessing any original source samples. To compare predictions from independently trained models, UCDA constructs a class-level prototype memory bank and estimates cross-model prediction reliability through prototype similarity, reducing the effect of inconsistent confidence scales across source models. Based on the resulting complementary supervision, UCDA adopts a two-stage transfer strategy: multiple source models are first refined on unlabeled target-domain driving data through collaborative optimization with positive and negative consistency constraints, and their validated expertise is then distilled into a single deployable target model. Comprehensive evaluations on public driving-scene datasets and real-world data collected from an autonomous vehicle platform demonstrate that UCDA effectively consolidates complementary multi-source knowledge, improving target-domain scene parsing reliability and generalization across diverse driving environments.

---


### 460. [Hist2Style: Histogram-Guided Stylization with Bilateral Grids](https://arxiv.org/abs/2606.01819)

**<font color=#1a73e8>作者：</font>** Dekel Galor, Adam Pikielny, Zhoutong Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Photorealistic style transfer aims to match the color and tone of an input image to that of a style target while preserving the content and details of the original scene. Although existing large image models can facilitate these kinds of appearance edits, their high computational demands, potential for hallucinations, and limited user control make them unsuitable for high-resolution, real-time workflows. We introduce Hist2Style, a bilateral-grid formulation for fast, edge-aware stylization that preserves visual fidelity by constraining operations to locally affine transforms in bilateral space. Our model distills a large image editing model into a lightweight network by training on a large supervised corpus generated with language and vision-language models, targeting spatially varying color edits. The network conditions on a histogram-based embedding of the style target to provide an interpretable interface for adjusting the output style by modifying the target color distribution. Overall, Hist2Style maintains content structure by construction, avoids hallucinations, and supports real-time, high-resolution photorealistic stylization with interactive user-controllable color and tone adjustments.

---


### 461. [TalkTag: Fine-Grained Morphosyntactic Error Annotation for Transcribed Speech](https://arxiv.org/abs/2606.01820)

**<font color=#1a73e8>作者：</font>** Shamira Venturini, Oliver Hennhöfer, Steffen Kinkel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fine-grained morphosyntactic error annotation is important in clinical and developmental language research, yet it is labour-intensive, expert-dependent, and difficult to scale. We present TalkTag, an LLM-based lightweight tool fine-tuned to automate CHAT-style error annotation in spoken-language transcripts. Developed under conditions of extreme data scarcity using children's narrative data, the system shows the feasibility of linguistic analysis in low-resource settings. Our evaluation demonstrates that TalkTag produces encouragingly precise annotation while effectively identifying instances where linguistic ambiguity makes automated tagging genuinely complex. In summary, with TalkTag, we provide a scalable alternative to manual error annotation and practically viable support for morphosyntactic error annotation.

---


### 462. [Hierarchically Decoupled Mixture-of-Experts for Robust Traffic Sign Recognition in Complex Driving Scenarios](https://arxiv.org/abs/2606.01822)

**<font color=#1a73e8>作者：</font>** Mingxiao Wang, Xiaozhen Qu, Bolin Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traffic sign detection is a fundamental component of environmental perception in autonomous driving and intelligent transportation systems. However, most existing detectors rely on static inference with globally shared parameters, limiting their ability to adapt to diverse and unstructured traffic scenarios. As a result, a single static model often struggles to simultaneously handle both clear near-range samples and challenging conditions such as distant small targets or adverse weather environments. To address this limitation, we propose CBDES MoE TSR, a hierarchically decoupled heterogeneous mixture-of-experts(MoE) framework for traffic sign recognition. The proposed framework departs from the conventional globally shared parameter paradigm by introducing a heterogeneous You Only Look Once (YOLO) expert pool together with a lightweight gating network, enabling an image-level dynamic routing mechanism. Based on the semantic characteristics of the input image, the gating module selectively activates the most suitable expert model from the expert pool, enabling a shift from fixed parameter fitting to on-demand dynamic representation. This design enhances feature extraction capability for specific scenarios while maintaining controlled inference overhead. Experimental results demonstrate that the proposed method achieves a remarkable balance between detection accuracy and efficiency on the composite traffic sign dataset. Specifically, our method attains an mAP50-95 of 76.8%, yielding a 2.3% improvement over the baseline method (74.5%) while simultaneously reducing computational overhead by approximately 39.4%. These findings robustly validate the effectiveness of the proposed approach.

---


### 463. [CAPF: Guiding Search-Agent Rollouts with Credit-Attenuated Privileged Feedback](https://arxiv.org/abs/2606.01830)

**<font color=#1a73e8>作者：</font>** Bin Chen, Xinye Liao, Yiming Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent LLM search agents use reinforcement learning with verifiable rewards (RLVR) to learn search-augmented reasoning from outcome rewards. On hard problems, these agents rarely sample end-to-end successful rollouts, leaving outcome-only RLVR with few positive-reward trajectories. We argue that improving learning on such problems requires additional guidance during training, and RLVR already contains verifier-side information that can provide it. This information can identify errors or omissions in the agent's submitted answer and guide revision within the rollout. We propose a training-time mechanism called \textbf{Credit-Attenuated Privileged Feedback} (CAPF), which makes this verifier-side information available through a Privileged Feedback call during training. CAPF lets the policy revise zero-reward attempts into positive-reward repair trajectories and attenuates credit for the feedback call and earlier actions to accommodate deployment without this call. Empirical research demonstrates that CAPF improves Qwen3-4B's average exact-match score from 44.7% under outcome-only RLVR to 48.5% on seven open-domain QA benchmarks.

---


### 464. [Learning Implicit Bias in Generative Spaces for Accelerating Protein Dynamics Emulation](https://arxiv.org/abs/2606.01833)

**<font color=#1a73e8>作者：</font>** Kaihui Cheng, Zhiqiang Cai, Wenkai Xiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative emulators of protein dynamics produce plausible trajectories at a fraction of the cost of molecular dynamics, but they inherit their training distribution and tend to revisit known states rather than reach rare ones under long-horizon extrapolation. Inspired by classical enhanced sampling, we introduce an implicit, history-dependent bias in the generative space of a pretrained emulator. Specifically, a history-aware score estimator augments the frozen emulator with a distance-weighted bias that steers reverse-time sampling away from previously generated structures, regularized by an environment-support term. To preserve structural validity at long horizons, a score-based refinement step re-projects drifted samples onto the data manifold using the frozen emulator. Our experiments demonstrate that the method (i) raises diversity by $35\%$ on DynamicPDB-80; (ii) on $12$ zero-shot Fast-Folding proteins, the learned bias alone reaches the unbiased emulator's coverage up to ${\sim}15\times$ faster, and pairing it with refinement reaches the coverage up to ${\sim}37\times$ faster while covering ${\sim}3\times$ as many low-energy states. Code will be released soon.

---


### 465. [Physics-Guided Attention in a Lightweight TCN for Efficient WiFi CSI-Based Human Activity Recognition](https://arxiv.org/abs/2606.01834)

**<font color=#1a73e8>作者：</font>** Chinthaka Ranasingha, Tharindu Fernando, Sridha Sridharan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human Action Recognition (HAR) using WiFi Channel State Information (CSI) has gained increasing attention due to its non-contact, low-cost, and privacy-preserving nature. However, existing learning-based approaches largely rely on deep, computationally intensive architectures to implicitly capture motion dynamics from CSI measurements, thereby increasing model complexity and reducing efficiency. Instead, we argue that incorporating appropriate inductive biases tailored to the physical characteristics of CSI signals enables more efficient and effective learning. In this work, we propose a compact temporal convolutional network (TCN)-based framework that explicitly incorporates motion-aware inductive biases into feature learning. Specifically, we introduce a Doppler-energy-guided temporal attention mechanism in feature space to emphasize motion-salient time segments, and a variance-driven channel attention module to weight informative subcarriers based on temporal motion statistics adaptively. By integrating these domain-specific priors, the proposed model effectively captures motion dynamics without increasing architectural depth. Extensive experiments on multiple benchmark datasets demonstrate that our approach achieves superior performance compared to deeper baselines, while significantly reducing parameter count and computational cost.

---


### 466. [Evaluation of Baseline Methods for IDD-based SSD External Memory Search](https://arxiv.org/abs/2606.01840)

**<font color=#1a73e8>作者：</font>** Yuki Suzuki, Alex Fukunaga  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many difficult search problems cannot be solved by algorithms such as A* using only RAM. Search algorithms which use external memory such as SSDs and HDDs with much higher capacity than RAM have been proposed in previous work, but previous work has focused on delayed duplicate detection approaches, as well as complex immediate duplicate detection (IDD) methods, and relatively simple methods for IDD have not been systematically studied. In addition, the effect of OS-level mechanisms for managing and speeding up accesses to external memory, such as page caches, has not been studied. This paper addresses these gaps in the literature by evaluating and analyzing the performance of simple baseline approaches for IDD-based A*.

---


### 467. [Suppressing Forgery-Specific Shortcuts for Generalizable Deepfake Detection](https://arxiv.org/abs/2606.01843)

**<font color=#1a73e8>作者：</font>** Yihui Wang, Yonghui Yang, Jilong Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deepfake detection suffers from poor generalization across forgery methods, as existing models tend to rely on spurious method-specific shortcuts that fail to transfer to unseen manipulations. While recent approaches attempt to improve generalization, they lack an explicit mechanism to identify and suppress such shortcuts in learned representations. In this work, we propose Shortcut Subspace Suppression (S^3) framework that explicitly characterizes and suppresses method-specific shortcuts via subspace modeling. Our key insight is that variations distinguishing different forgery methods capture method-specific artifacts and thus serve as an effective proxy for method-specific shortcuts. To this end, we train a lightweight linear probe for forgery method classification and perform Singular Value Decomposition (SVD) to extract the dominant shortcut subspace. Building on this formulation, we develop two complementary strategies to reduce shortcut reliance. During training, we softly suppress the shortcut subspace in feature representations, encouraging the model to rely on more generalizable cues for real/fake discrimination. At inference time, we introduce a training-free counterpart that attenuates neurons aligned with the identified shortcut directions, enabling plug-and-play generalization enhancement with improved interpretability. Extensive experiments on multiple benchmarks demonstrate that our method significantly improves cross-method generalization while maintaining strong in-domain performance. The code will be released upon acceptance of the submission.

---


### 468. [Mos-Gen: A Generative Molecular Framework for Mosquito Insecticide Design](https://arxiv.org/abs/2606.01846)

**<font color=#1a73e8>作者：</font>** Lina Wang, Yaning Cui  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mosquito-borne infectious diseases cause more than 700000 deaths worldwide each year. The long-term use of conventional chemical insecticides has induced serious resistance problems, creating an urgent need to develop novel, highly effective, and ecologically sustainable alternatives. While existing artificial intelligence approaches in this domain have focused primarily on activity prediction and classification, they leave a critical gap in the de~novo generation of novel molecular scaffolds. In this study, we propose Mos-Gen, a motif-aware generative collaborative framework that couples the pretrained molecular representation model Uni-Mol with a variational autoencoder (VAE), specifically tailored for the design of disulfide-containing allicin derivatives as mosquito insecticides. Among the generated candidates, fourteen compounds -- comprising nine predicted positives and five predicted negatives -- were selected for chemical synthesis and experimental validation. The hit rate among the predicted positives reached 78%, whereas none of the predicted negatives exhibited mosquitocidal activity. These experimental results fully validated the high-precision screening capability of the Mos-Gen framework.

---


### 469. [RescueBench: Can Embodied Agents Save Lives in the Wild ?](https://arxiv.org/abs/2606.01848)

**<font color=#1a73e8>作者：</font>** Kui Wu, Beiyu Guo, Hao Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Search-and-rescue (SAR) requires embodied agents to explore unfamiliar environments under multimodal uncertainty, perform multi-stage interactions, and retrieve spatial memory over long horizons. Existing benchmarks typically evaluate these capabilities in isolation, leaving unclear how failures compound when they must be composed in realistic workflows. We introduce RescueBench, a photo-realistic diagnostic benchmark that instantiates SAR as a four-stage pipeline: multimodal exploration, target rescue, memory-guided return, and final handoff. By combining sequential task composition with stage-level evaluation, RescueBench enables analysis of how exploration and memory failures propagate through embodied rescue workflows. It contains five progressive difficulty levels that vary in environmental complexity, clue ambiguity, and spatial hierarchy, along with an automatic episode generation and annotation pipeline for scalable evaluation and training. We evaluate seven baselines, an oracle reference, and human players, showing that no baselines complete the full task at the greatest difficulty. Stage-level diagnosis identifies autonomous exploration as the dominant failure mode and spatial memory as a second, independent bottleneck, suggesting that these limitations are not resolved by current topological visual-language navigation or map-based methods. Code is available in this https URL

---


### 470. [ContinuousBench: Can Differentially Private Synthetic Text Improve Capabilities?](https://arxiv.org/abs/2606.01849)

**<font color=#1a73e8>作者：</font>** Peihan Liu, Lucas Rosenblatt, Weiwei Kong 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Differentially private (DP) text synthesis promises to unlock sensitive corpora for model training, but it remains unclear whether DP synthetic data transmits genuinely new knowledge and capabilities present only in those corpora. This is because existing evaluations rely on tasks that are nearly solvable without training, so strong benchmark performance does not establish that DP synthesis can substitute original data access. Thus, we introduce ContinuousBench, a continuously and automatically-regenerated benchmark that measures capability gain from DP synthetic text. Each quarter, a new release pairs a never-before-seen training corpus with a derived QA set, constructed to be: (1) unsolvable sans-corpus; and (2) learnable under DP, as the tested knowledge is supported by hundreds of independent records. Researchers produce DP synthetic data from the training corpus and run our standardized training and evaluation harness on their synthetic data to measure gains. We instantiate two tracks: Geminon, a procedurally-generated dataset about fictional creatures; and News, a stream of newly crawled public news articles. Although standard benchmarks are nearly saturated, on ContinuousBench we find that non-private synthesis transfers substantial knowledge from the original corpus, while state-of-the-art DP synthesis methods generally fail to do so, even at $\varepsilon=100$.

---


### 471. [From Global Policies to Local Strategies: Multi-Objective Optimization of Resource-Specific Handover Policies](https://arxiv.org/abs/2606.01857)

**<font color=#1a73e8>作者：</font>** Lukas Kirchdorfer, Artemis Doumeni, Han van der Aa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Efficient resource allocation is a key challenge in business process management, with direct implications for cost, throughput time, and utilization. While recent Reinforcement Learning (RL) approaches have shown promise in deriving adaptive allocation policies, they typically neglect inter-resource collaboration patterns that can strongly influence real-world task handovers. Recognizing this, this paper introduces the first approach for multi-objective optimization of resource-level decision-making, enabling the recommendation of person-specific handover policies. To achieve this, our work combines an existing Multi-Agent System-based process simulator with a multi-objective evolutionary algorithm. The resulting approach produces Pareto-optimal, resource-specific policies that optimize the process across multiple objectives. Experimental results on synthetic and real-world datasets show that our approach reduces costs by an average of 37% and waiting time by 58%, consistently outperforming heuristic baselines and demonstrating the potential of leveraging collaboration-aware optimization to improve process performance.

---


### 472. [Polaris: Scaling Up Instruction-Guided Image Generation Towards Millions of Personalized Style Needs](https://arxiv.org/abs/2606.01858)

**<font color=#1a73e8>作者：</font>** Zhi-Kai Chen, Jun-Peng Jiang, Jun-Jie Tao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Users increasingly expect image generation models to quickly adapt to highly diverse and personalized requirements, such as producing images with distinctive styles or characteristics. Traditional approaches rely on fine-tuning, which is costly and difficult to scale. To cope with these limitations, the community has accumulated a growing library of fine-tuned modules and adapters, where each component targets specific generation needs and collectively serves as a foundation for handling new demands. This naturally raises a question: instead of repeatedly training new models, can we systematically exploit this expanding ecosystem to better fulfill user instructions? To this end, we present Polaris, an intelligent retrieval framework that automatically selects and integrates suitable models from the model library based on a user's instructions. The key insight is that harnessing such a massive and heterogeneous pool requires not only finding the most relevant modules among thousands of candidates, but also aligning them effectively for instruction-driven generation and editing. Polaris addresses this challenge by indexing over 6,500 checkpoints and 75,000 adapters, and retrieving the most relevant components given a user's input and instruction. In doing so, it delivers scalable, controllable, and well-aligned generation -- without any additional training.

---


### 473. [A Theoretical Framework for Self-Play Theorem Proving Algorithms](https://arxiv.org/abs/2606.01861)

**<font color=#1a73e8>作者：</font>** Thomas Chen, Zhiyuan Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-play, a type of training algorithm that enables a model to self-improve, has recently shown promising empirical results in the context of formal theorem proving using Large Language Models (LLMs). (Dong & Ma, 2025) instantiate self-play with two cooperating agents: a prover, which proves theorems, and a conjecturer, which generates new theorems as a curriculum to the prover. In this paper, we provide a theoretical framework for understanding the self-improvement capabilities of self-play algorithms for theorem proving. First, we formalize the set of theorems as a graph, with nodes as theorems and edges between pairs of theorems with similar semantics. We introduce a set of primitive assumptions that characterize the guarantees of a trained prover and how a conjecturer can access the structure of the graph. Second, we show that if the underlying graph of theorems is well-connected, then a prover-conjecturer system, where the conjecturing algorithm is based on a reversible random walk, is sufficient to grow the set of proved theorems exponentially. Third, motivated by an issue encountered empirically by self-play algorithms, where the conjecturer tends to generate artificially complex and non-fundamental theorems, we propose a diversity measure for a training distribution of theorems generated by a conjecturer and an improved conjecturing algorithm that locally maximizes this diversity measure, by computing the diffusion similarity between neighboring theorems in the theorem graph. Finally, we describe a method to compute the diffusion similarity by using contrastive learning to embed nodes into Euclidean space and then computing the inner-product between embeddings.

---


### 474. [RadioMaster: Multi-Agent System for Autonomous Radio Signal Generation](https://arxiv.org/abs/2606.01862)

**<font color=#1a73e8>作者：</font>** Jiazhen Lei, Tianze Cao, Yuxin Sha 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Translating user intents into physical radio signals represents the critical yet notoriously tedious final step in wireless prototyping, as it requires intricate knowledge of physical layer details and presents immense implementation challenges. Large Language Models (LLMs) and multi-agent systems have revolutionized conventional software engineering, raising the compelling question of whether they can resolve these formidable difficulties. However, our investigations reveal that current models experience significant limitations and fail to accomplish this task when applied to radio signal generation. This performance degradation primarily stems from severe domain ignorance and a fundamental insensitivity to physical hardware constraints. To bridge this gap, we introduce RadioMaster, a fully autonomous multi-agent framework designed to seamlessly translate user input into real-world wireless emissions. RadioMaster operates on three synergistic pillars: RadioWiki for domain-specific knowledge retrieval, RadioAgent for collaborative I/Q sample generation alongside hardware configuration, and RadioEmulator for closed-loop physical layer verification. Furthermore, we construct RadioBench, the first comprehensive benchmark tailored specifically for the radio signal generation domain. Extensive real-world evaluations demonstrate that RadioMaster significantly outperforms state-of-the-art (SOTA) baselines regarding configuration viability and signal fidelity.

---


### 475. [Continual Learning as a Multiphase Moving-Boundary Problem](https://arxiv.org/abs/2606.01863)

**<font color=#1a73e8>作者：</font>** Snigdha Chandan Khilar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning struggles to balance retaining past knowledge with absorbing new tasks. Stefan-CL elegantly resolves this stability-plasticity dilemma through the physics of melting. It frames consolidated knowledge as a protected "solid" and unused capacity as an adaptable "liquid." As the network learns, this boundary expands, governed by a "latent heat" tuning dial. By mathematically freezing the learned interior, Stefan-CL cuts forgetting to near zero, matching memory-heavy baselines without storing raw data, forging a beautiful, physics-grounded path for AI.

---


### 476. [Task-Induced Representational Invariances Depend on Learning Objective in Deep RL](https://arxiv.org/abs/2606.01868)

**<font color=#1a73e8>作者：</font>** Manu Srinath Halvagal, Sebastian Lee, SueYeon Chung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) has long served as a model for goal-directed animal behavior in neuroscience. Modern deep RL has shown remarkable success across many domains, further strengthening this connection. The ability to learn abstract representations of high-dimensional state spaces underlies much of this success. However, theoretical understanding of these learned representations remains limited, hindering direct comparisons between models and animal learning. We address this gap by analyzing deep RL representations through the lens of MDP reduction theory. Investigating canonical RL algorithms in a navigation task, we find that even when performance is comparable, the value-based method (DQN) learns representations that are invariant to MDP homomorphism symmetries, while the policy-gradient method (PPO) learns representations invariant to action symmetries. These differences emerge consistently across domains, have downstream consequences for transfer learning, and appear in LLMs in a prompt-dependent manner. Our findings provide a principled approach to comparing learned representations across RL algorithms, with demonstrated practical implications and possible insights for neural coding in the brain.

---


### 477. [Deep Learning for Generating Computational PIN-4 Immunohistochemistry Staining from Prostate Biopsy H&E Images](https://arxiv.org/abs/2606.01871)

**<font color=#1a73e8>作者：</font>** Vietbao Tran, Pratik Shah  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Immunohistochemistry (IHC)is frequently used to resolve diagnostically ambiguous prostate cancer biopsy findings on hematoxylin and eosin (H&E)-stained tissue. However, PIN-4 IHC staining is typically performed on adjacent tissue sections, limiting direct spatial comparison between the H&E morphology and the corresponding immunophenotypic signal. A paired, registered H&E/PIN-4 dataset was constructed from routine clinical prostate biopsy whole-slide images (WSIs), and a conditional generative adversarial network (cGAN) was trained to synthesize PIN-4 staining patterns directly from native H&E image patches. The final dataset comprised 172 paired WSIs from 93 patients and 27,298 registered 1024x1024 patch pairs, spanning adenocarcinoma-positive and benign cases with representation across age, race, and ethnicity groups. The model was evaluated on a held-out test set of 1,814 patch pairs from 17 WSIs, achieving a mean peak signal-to-noise ratio (PSNR) of 21.88 dB, structural similarity index measure (SSIM) of 0.667, Pearson correlation coefficient (PCC) of 0.684, and learned perceptual image patch similarity (LPIPS) of 0.417. Qualitative review by a board-certified pathologist showed that generated images captured diagnostically relevant PIN-4 staining patterns, including AMACR/racemase expression and basal-cell-associated staining, while preserving spatial correspondence with the source H&E morphology. Accuracy of synthesis varied across morphologically complex regions, including high-grade carcinoma and intraductal carcinoma. These results support the feasibility of supervised PIN-4 synthesis from routinely acquired brightfield H&E prostate biopsy images. The approach enables direct interpretation of predicted PIN-4 marker patterns in the context of the source prostate H&E architecture, addressing a current spatial limitation of conventional adjacent-section IHC.

---


### 478. [Beyond the Simplex: Balanced Prototype Geometry for Scorer-Agnostic Open-Set Recognition](https://arxiv.org/abs/2606.01883)

**<font color=#1a73e8>作者：</font>** Mayank Sharma, Rohit Kumar Mourya  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Open-set recognition (OSR) requires a classifier to reject inputs from unseen classes which is essential in safety-critical settings such as medical imaging. Simplex based methods, which fix class prototypes at the vertices of a regular simplex and then reject via a distance-ratio score, perform well empirically but lack theoretical justification, and existing analysis applies only when the embedding dimension d is at least C-1, which is the regime in which a regular simplex exists.
We give a theoretical account of simplex-ratio OSR that holds in every embedding dimension, including d < C-1. Our analysis centers on balanced equal-norm codes: prototype configurations with equal lengths and zero sum, which exist for all d >= 2 and include the regular simplex as a special case. For these codes we show that an auxiliary squared ratio score has sublevel sets that are exact unions of Euclidean balls, which in turn bracket the acceptance region of the operational score; and we prove a sharp dichotomy: the prototypes attain one-distance symmetry, behaving like a regular simplex, if and only if d >= C-1, with controlled degradation governed by an explicit defect parameter below that threshold. We further show the false-acceptance rate decays exponentially in d under natural isotropy assumptions, and that the operational score is globally Lipschitz with compact acceptance regions.
Empirically, we study balanced prototype geometry as both an analytic tool and a representation-learning prior, rather than as a stand-alone state-of-the-art detector. Across CIFAR and MedMNIST open-set splits, the geometry provides useful structure, but OSR performance remains strongly dependent on the scoring rule: raw ratio scores typically underperform nearest-neighbor and logit-based alternatives.

---


### 479. [EVA-Net: Subject-Independent EEG Motor Decoding with Video-Derived Motor Priors](https://arxiv.org/abs/2606.01884)

**<font color=#1a73e8>作者：</font>** Ziyuan Li, Yueyu Sun, Yimeng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Practical non-invasive Brain-Computer Interface (BCI) systems require EEG decoders with strong cross-subject generalization and minimal calibration. However, inter-subject variability and signal non-stationarity often entangle motor semantics with subject-specific noise, limiting subject-independent decoding. Recent multimodal approaches use text as a semantic anchor, yet text provides sparse and static supervision for inherently dynamic motor processes. To address this issue, we propose EVA-Net, a two-stage framework that uses action videos as semantic priors for subject-independent EEG motor decoding. In the first stage, EEG and video features are aligned in a shared space using cross-modal and supervised contrastive objectives to reduce subject-specific variation. In the second stage, video category prototypes and knowledge distillation transfer video-derived priors to an EEG-only classifier without adding inference overhead. Experiments on two public datasets show that EVA-Net achieves strong subject-independent decoding performance, including an 8.66% LOSO accuracy gain on EEGMMI. Ablation results further suggest that video provides a more effective semantic anchor than the text baseline considered in this work.

---


### 480. [Divide and Conquer: Reliable Multi-View Evidential Learning for Deepfake Detection](https://arxiv.org/abs/2606.01885)

**<font color=#1a73e8>作者：</font>** Xiaolu Kang, Zhongyuan Wang, Jikang Cheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the evolution of generative models, deepfakes have achieved near-perfect semantic realism, leaving forensic traces only in subtle structural anomalies. However, existing single-view paradigms often fail to generalize, as dominant semantic features overwhelm subtle artifact cues within entangled representations. This imbalance leads to overconfident yet brittle predictions -- a phenomenon we term the Semantic Masking Effect. To address this challenge, we propose a reliable framework called Divide-and-Conquer Multi-View Evidential Learning (DiCoME) for Deepfake Detection. In the "Divide" phase, we employ Geometric View Purification to decompose the entangled representation space through principled geometric projection. This process suppresses semantic interference within artifact-sensitive representations, forming the foundation for decorrelated yet complementary semantic and artifact views. In the "Conquer" phase, we leverage Uncertainty-Aware Evidential Learning to synthesize these distinct views. By explicitly modeling the "epistemic conflict" between semantic and artifact cues, this mechanism provides calibrated uncertainty estimates instead of forcing rigid deterministic decisions. Extensive experiments across multiple benchmarks demonstrate that our method consistently outperforms existing approaches in generalization performance, while providing reliable uncertainty estimation for trustworthy deepfake detection. Code is available at this https URL.

---


### 481. [Adversarial Attacks on Robot Localization Systems via Deep Feature Perturbation](https://arxiv.org/abs/2606.01892)

**<font color=#1a73e8>作者：</font>** Zhenyu Li, Tianyi Shang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robot localization systems are critical for autonomous navigation and safety. Adversarial perturbations can mislead these systems, resulting in mislocalization, navigation errors, or unsafe interactions, especially in mission-critical scenarios. This paper investigates the vulnerability of deep learning based localization pipelines to adversarial attacks. We propose a novel framework for generating adversarial queries that specifically target Product Quantization (PQ) in visual localization systems. Our method employs a Lightweight Product Quantization Network (LPQN) to perturb query feature encodings, misleading the retrieval process by returning semantically irrelevant database entries. Adversarial queries are generated via a two-phase procedure: a forward pass that perturbs feature distributions and a backward pass that refines the perturbation through optimization. The lightweight design of LPQN allows the creation of subtle yet highly effective perturbations with minimal computational overhead. Extensive experiments in both controlled and real-world robotic environments demonstrate that our approach substantially degrades PQN performance, exposing critical vulnerabilities in practical applications.

---


### 482. [Physically-Constrained Mamba-SDE for Remaining Useful Life Prediction under Irregular Observations](https://arxiv.org/abs/2606.01894)

**<font color=#1a73e8>作者：</font>** Deyu Zhuang, Peiliang Gong, Yang Shao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate Remaining Useful Life prediction is critical for industrial predictive maintenance. However, real-world deployment is challenging due to the irregular nature of sensor observations, characterized by asynchronous sampling, burst missingness, and temporal jitter. Compounding this issue, purely data-driven models often generate physically implausible degradation trajectories that violate the irreversible nature of damage accumulation. To address this, we propose PC-MambaSDE, a unified continuous-time framework for robust RUL prediction under irregular observations. Specifically, we design a Mask-Aware Continuous Mamba Encoder that explicitly leverages observation masks to extract context-rich control signals. Furthermore, we introduce a Physics-Guided Latent SDE with parametrically rectified hybrid drift, superimposing a global physical bias to enforce monotonic degradation even amid severe observation gaps. Additionally, we formulate RUL prediction as a boundary value problem via a Terminal Degradation Penalty, which decouples a Health Index dimension and applies a penalty loss to guide trajectories toward the failure state. Theoretically, we prove that our variational objective is mathematically equivalent to minimizing the KL divergence via Girsanov's theorem, and we guarantee the global asymptotic stability of the learned dynamics through Lyapunov analysis. To enable rigorous evaluation, we develop a Hybrid Irregularity Generation Scheme that simulates realistic industrial imperfections. Extensive experiments on public benchmarks demonstrate that PC-MambaSDE significantly outperforms state-of-the-art methods, particularly under extreme observation scarcity, validating the efficacy of embedding physical priors into continuous-time latent dynamics.

---


### 483. [Collaborative Space Object Detection with Multi-Satellite Viewpoints in LEO Constellations](https://arxiv.org/abs/2606.01895)

**<font color=#1a73e8>作者：</font>** Xingyu Qu, Wenxuan Zhang, Peng Hu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the growing number of satellites in low Earth orbit (LEO) constellations, the near-Earth space environment has become increasingly congested, making space object detection (SOD) a pressing challenge for space safety and sustainability. To mitigate collision risks and ensure the continuity of space operations, SOD systems must deliver fast and accurate detection under stringent onboard constraints. In this paper, we investigate the potential of multi-viewpoint observation fusion within a deep learning (DL) framework to enhance SOD performance. We design a practical multi-view pipeline and several input representations for feeding multi-view data into YOLO-based detectors. Our experiments show that using multi-view inputs is feasible in most cases and typically produces better results for mAP50 and mAP50-95. For example, in model YOLOv9-m, single-view compared to a three-view fused RGB setting, mAP50 increases from 0.638 to 0.732, while mAP50-95 improves from 0.227 to 0.276. Compared with the single-view setting, the best three-view grayscale configuration improves mAP50 by 36.3% and mAP50-95 by 46.5%. These findings establish multi-view fusion as a viable and effective strategy for SOD, with broad implications for space situational awareness in LEO constellation deployments.

---


### 484. [Train, Test, Re-evaluate: Schedule-Sensitive Evaluation of Generative Data for Hand Detection](https://arxiv.org/abs/2606.01896)

**<font color=#1a73e8>作者：</font>** Atmika Bhardwaj, Silvia Vock, Nico Steckhan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generated (or synthetic) image data is increasingly used to augment or replace real training datasets when target imagery is scarce, expensive, or biased. For hand detection, particularly in occupational safety settings, public datasets mostly contain bare hands. This under-represents the variation in hand appearance introduced by gloves, tattoos, jewelry, and other personal protective equipment, creating a distribution shift that safety-critical applications encounter at deployment. We test whether generative inpainting, editing only the hand region of a real photograph to introduce accessories, can close this shift gap. On a paired dataset of real images and their synthetic counterparts, we train YOLOv8n hand detectors under six training-and-scheduling regimes (Experiments A-F, three random seeds each), evaluate every detector on a real test set and on a real-gloves-only test split, and report the mean average precision (mAP) at two overlap thresholds (mAP@0.5 and mAP@0.5:0.95) along with paired statistical tests. A two-stage experiment: train on real U synthetic data, then fine-tune the resulting weights on real-only at a lower learning rate, increases mAP@0.5 compared to the real-only baseline model on the standard real test set, and improves the real-gloves out-of-distribution gap. Another three-stage experiment preserves box-tightness best, reaching the highest mAP@0.5:0.95 of any other experiment in the study. The synthetic-data utility for safety-critical hand detection is determined by the training procedure, and simple multi-stage experiments extract substantial real-deployment benefit from inpainted accessory data.

---


### 485. [Community-Aware Assessment of Social Textual Engagement and Resonance: A Human-Centric Perspective on User-Generated Content Evaluation](https://arxiv.org/abs/2606.01897)

**<font color=#1a73e8>作者：</font>** Tianjiao Li, Kai Zhao, Xiang Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Traditional Video Quality Assessment (VQA) focuses narrowly on aesthetic fidelity, overlooking the complex social dynamics that define quality in User-Generated Content (UGC). In this work, we propose a paradigm shift from signal-centric metrics to human-centric resonance assessment. We introduce CASTER (Community-Aware Assessment of Social Textual Engagement and Resonance), a new task that evaluates whether a UGC item achieves positive community resonance based on its multimodal attributes rather than visual quality alone. To address this, we present MEDEA (Multimodal Engagement-Driven Evaluation Architecture), which introduces a novel Social Chain-of-Thought (Social-CoT) mechanism. Unlike traditional logical CoT, Social-CoT performs multimodal perspective-taking, instantiating diverse viewer personas to simulate collective cognitive and emotional reactions (i.e., the "community mind") before deriving a quality judgment. MEDEA is trained via a two-stage approach involving supervised fine-tuning and process-supervised reinforcement learning with Social Alignment Reward to ensure reasoning paths are grounded in authentic human social cognition. To support this task, we release CASTER-Bench, a comprehensive human-annotated benchmark covering diverse UGC categories. Experiments demonstrate that MEDEA significantly outperforms state-of-the-art baselines on CASTER-Bench while providing interpretable and empathetic reasoning paths that align with real community feedback.

---


### 486. [KliniskVestBERT: BERT Model Specialised to Norwegian Clinical Texts](https://arxiv.org/abs/2606.01904)

**<font color=#1a73e8>作者：</font>** Christian Autenried, Cosimo Persia  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The increasing application of Natural Language Processing (NLP) in healthcare demands language models specifically attuned to the complexities of clinical language. This work introduces KliniskVestBERT, a suite of three BERT-based encoder models pre-trained on a substantial corpus of real-world, de-identified Norwegian clinical texts from Helse Vest. We continue pretraining existing language models Nb-BERT-large, NorBERT3-large, and ModernBERT on our specialized clinical dataset. This dataset is based on a representative population of Helse Vest patients. The included document types are carefully curated to encompass a broad clinical spectrum in bokmål and nynorsk including discharge summaries, surgical reports, nursing notes etc. ensuring comprehensive representation of the linguistic landscape within Norwegian healthcare settings. Evaluation on three synthtetic Norwegian clinical benchmark datasets and two real-world problems demonstrates that each of our clinically specialized models consistently outperforms their baseline counterparts, highlighting the significant benefit of domain-specific pre-training for NLP tasks within the clinical domain. The project was a joint effort by all Helse Vest entities (Helse Bergen, Helse Fonna, Helse Førde and Helse Stavanger) with DIPS under the project lead of Helse Vest ICT.

---


### 487. [Bayesian Spectral Emotion Transition Discovery from Multi-Annotator Disagreement](https://arxiv.org/abs/2606.01906)

**<font color=#1a73e8>作者：</font>** Keito Inoshita, Takato Ueno  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Emotions evolve through the dynamics of conversation, and understanding their transition structure is foundational to applications ranging from mental-health screening to dialogue systems. However, existing studies typically compress multi-rater judgments into a single hard label by majority voting, discarding the uncertainty signal needed to understand turn-to-turn transitions. In this article, we propose Bayesian Spectral Emotion Transition Discovery (BSETD), a two-stage framework that discovers emotion-transition structure from multi-rater soft labels. In the first stage, a hierarchical Dirichlet-Multinomial posterior is constructed through the outer product of soft labels, equipping each cell of the K x K transition matrix with a credible interval and Benjamini-Hochberg (BH) false discovery rate (FDR)-controlled significance. In the second stage, the symmetrized graph Laplacian is spectrally decomposed to separate a low-frequency (inertia) component from a high-frequency (contagion) component. On EmotionLines, BSETD simultaneously recovers the signatures of two distinct affective spaces: the Plutchik-adjacent transitions disgust to anger (log2 lift +0.94) and anger to disgust (+0.86) are over-represented, while the Russell-valence-reversed transitions joy to anger (-0.90) and anger to joy (-0.89) are under-represented. A five-source cross-corpus validation yields pairwise Pearson correlations in 0.91-0.98 within English, 0.79-0.85 against Chinese M3ED, and 0.979 between the human hard labels and the LLM virtual soft labels on the same utterance set, demonstrating that a pipeline preserving annotator uncertainty bridges the computational study of emotion dynamics with established psychological theory.

---


### 488. [Private and Stable Test-Time Adaptation with Differential Privacy](https://arxiv.org/abs/2606.01908)

**<font color=#1a73e8>作者：</font>** Zefeng Li, Qiaoyue Tang, Mathias Lecuyer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time adaptation (TTA) can reduce error on new and different data by updating the model on these inputs during inference. However, these updates raise the issue of privacy w.r.t. the testing data, because the model parameters now depend on all past inputs. To control this privacy risk, we cast multiple popular TTA methods (Tent, EATA, SAR, DeYO, and COME) into differential privacy (DP) forms that apply per-sample gradient clipping and Gaussian noise for all updates. On ImageNet-C, our DP-TTA methods provide adequate privacy at small cost to accuracy, and in the low-privacy regime the clipping mechanism of DP can even improve the accuracy and stability of adaptation in the continual setting. These improvements to privacy and accuracy come at only modest computational overhead. These first results on private TTA raise awareness of the issue, inform the development of more private test-time updates, and identify per-sample clipping as an effective technique for improving the accuracy and stability of adaptation.

---


### 489. [Residual Decoder Adapter: ID-Preserving Tokenizer Adaption for Autoregressive Text Rendering](https://arxiv.org/abs/2606.01911)

**<font color=#1a73e8>作者：</font>** Dongxing Mao, Jinpeng Wang, Jiahao Tang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual Autoregressive (AR) models generate images by predicting discrete tokens that are decoded by a visual tokenizer. Despite demonstrating strong overall image generation ability, they still underperform on text rendering with blur strokes and disrupt letter shapes. In this work, we trace this limitation to the visual tokenizer, which struggles to reconstruct fine-grained detail. Improving the tokenizer is straightforward but expensive, as it necessitates retraining both the tokenizer and the AR model. Can we improve text rendering performance of AR models without retraining the existing tokenizer and AR model? To achieve this, we propose the Residual Decoder Adapter(RDA) that upgrades an existing tokenizer post-hoc without changing its token space. Specifically, it refines the decoder output of the visual tokenizer by introducing two novel components: (i) a paired codebook that shares the token distribution with the original one; (ii) a parallel branch to learn the tiny differences (residual) between the reconstructed image and the ground-truth images in the pixel space. This residual design allows us to enhance the tokenizer non-invasively while preserving compatibility with prior AR models. RDA substantially improves text rendering significantly by a large margin. For instance, we boost finetuned Janus-Pro OCR accuracy rises from 24.52% to 58.26% (TextVisionBlend), from 12.75% to 36.81% (StyledTextSynth) on competitive TextAtlas benchmark. The code is available at this https URL

---


### 490. [Pool-Select-Refine: Allocation-Aware Generative Dataset Distillation with Soft-Label-Guided Latent Refinement](https://arxiv.org/abs/2606.01920)

**<font color=#1a73e8>作者：</font>** Wenmin Li, Shunsuke Sakai, Zhongkai Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based dataset distillation has recently emerged as a promising paradigm for condensing large-scale datasets into compact synthetic sets. By leveraging pretrained generative priors, these methods can produce realistic class-conditional samples more efficiently than traditional matching-based approaches. However, most existing diffusion-based methods still adopt a rigid ``Generate-and-Use'' strategy, where the generated samples are directly treated as the final distilled set under a fixed images-per-class budget. Such a design tightly couples candidate generation with final budget allocation, which may result in redundant waste of the limited budget or insufficiently informative samples. In this paper, we propose ``Pool-Select-Refine'', a two-stage framework for allocation-aware generative dataset distillation. First, instead of directly using a fixed number of generated samples, we construct an over-complete candidate pool and select a compact subset under the target budget. Second, we refine the selected samples in latent space using soft-label supervision derived from the teacher model, improving semantic alignment while preserving the generative prior. This design explicitly decouples generation, selection, and refinement, enabling more effective use of the distillation budget. Experiments on large-scale and fine-grained image classification benchmarks show that the proposed framework delivers consistent gains over diffusion-based baselines. The results suggest that introducing a curation stage before refinement is a simple yet effective way to improve diffusion-based dataset distillation.

---


### 491. [VET: A Framework for Analyzing AI Discourse](https://arxiv.org/abs/2606.01929)

**<font color=#1a73e8>作者：</font>** Meredith Ringel Morris  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Public discourse on AI has become polarized; exaggerated positions on AI in traditional and social media threaten the development of AI Literacy among the general public. In this article, I introduce the VET Framework, a method for categorizing AI discourse along the dimensions of valence, effectiveness, and trajectory. I show how this framework can be used to identify, compare, and critique prevalent narratives of AI Hype, AI Doom, AI Denial, and AI Normalcy. Using VET, I analyze how each of these four stances exaggerates some aspects of the current state and/or likely evolution of AI, and illustrate how the VET framework can serve as an AI Literacy tool by supporting the ``vetting'' of polarized AI discourse.

---


### 492. [SAVMap: Structure-Aided Visual Mapping of Large-Scale 2.5D Manhattan Wireframes from Panoramic Video](https://arxiv.org/abs/2606.01939)

**<font color=#1a73e8>作者：</font>** Howard Huang, Bharath Surianarayanan, Keifer Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Precise 3D representations of industrial environments enable tasks such as robot localization and digital twin generation. We propose SAVMap, a method for generating a semantic wireframe map of warehouse shelf and light structures using only a panoramic video camera as the sensor input. Sequences of rectified images with shelf and ceiling-facing views are extracted from a panoramic video captured along the warehouse aisles. Using a semantic segmentation network front end, a set of sparse, semantic structure feature points (e.g., corners of shelf structures, centers of lights) are extracted from each image and tracked across the sequences. By accounting for real-world geometric relationships among the points such as Manhattan grids, a constrained structure-from-motion algorithm yields the 3D points that form a wireframe map. We demonstrate the scalability and accuracy of our proposal in a warehouse with 46 shelving rows, each with faces spanning 55\,m by 7\,m. From an hour of panoramic video content, we create wireframe maps for over 5000 shelf elements across the rows, achieving an aggregate mean absolute error of 4.8\,cm with respect to ground-truth.

---


### 493. [SCAPO: Self-Supervised Category-Level Articulated Pose Estimation from a Single 3D Observation](https://arxiv.org/abs/2606.01940)

**<font color=#1a73e8>作者：</font>** Can Zhang, Gim Hee Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing methods for category-level object articulation from a single 3D observation often rely on dense supervision, multi-frame inputs, or CAD templates, and still struggle to disentangle geometry from articulation or to recover explicit joint parameters. We propose SCAPO, a self-supervised framework that estimates canonical geometry, rigid part segmentation, and joint pivots, axes, and articulation states from a single RGB-D observation without ground-truth labels or category-specific models. Our SCAPO first uses an SE(3)-equivariant vector-neuron autoencoder to factor out global pose and align diverse instances into a shared canonical space. On this aligned shape, a joint-aware blend-skinning module is then designed to model part motion. We learn this representation through cycle reconstruction between observed and canonical shapes and cross-space alignment with a learnable canonical template that decouples shared category geometry from instance-specific residual shape. Experiments on synthetic and real articulated-object datasets show that our SCAPO recovers consistent part structure and accurate articulation parameters and outperforms all self-supervised baselines.

---


### 494. [Beyond Low-Rank: Low-Rank Sparse Prompting via Spiking Neural Network and Prompt Factorization](https://arxiv.org/abs/2606.01945)

**<font color=#1a73e8>作者：</font>** Yumiao Zhao, Bo Jiang, Beibei Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual Prompting (VP) has emerged as an efficient paradigm for adapting large-scale pre-trained vision models to downstream tasks by incorporating learnable prompts at the input level. However, existing VP methods typically employ dense pixel-level prompts, which often suffer from redundant perturbations, limited generalization and energy inefficiency. To overcome these limitations, we propose to integrate brain-inspired spiking learning into visual prompt learning tasks. As we know that spiking neuron can perform inexpensive information processing by transmitting the input data into discrete spike trains and return sparse outputs. Inspired by this, we propose \textbf{Lo}w-\textbf{R}ank visual \textbf{S}pike \textbf{P}rompting (LoRSP), a novel framework that learns dynamic low-rank sparse visual prompts naturally via a Spiking neuron learning mechanism. The core idea of LoRSP is to exploit the brain-inspired sparse firing mechanism of spiking neurons to generate pixel-level sparse prompt for each instance. To be specific, we first construct a series of prompt factors via low-rank factorization to capture distinct prompt subspaces. These prompt factors are then fed into an SNN architecture, which performs the integrate-and-fire process to emit spikes. As a result, our LoRSP generates a \emph{sparse} visual prompt while maintaining the low-rank constraint. This design enables instance-specific selective prompting, leading to more compact and robust adaptation across diverse downstream tasks. Extensive experiments on five heterogeneous vision backbones and multiple benchmarks demonstrate that LoRSP achieves competitive performance while requiring fewer tunable parameters compared to existing VP methods.

---


### 495. [Randomized Least Squares Value Iteration itself is Joint Differentially Private](https://arxiv.org/abs/2606.01952)

**<font color=#1a73e8>作者：</font>** Haiyang Lu, Pratik Gajane, Shaojie Bai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As reinforcement learning (RL) increasingly applies to sensitive domains, such as health care and recommendation systems, privacy-preserving techniques have become essential to protect users' sensitive information. We investigate privacy-preserving RL under an episodic setting, focusing on algorithms based on randomized exploration, such as Randomized Least Squares Value Iteration (RLSVI). The overall goal is to study how randomized exploration interacts with the injected noise required by privacy mechanisms. In this work, we show a new privacy analysis that characterizes how the noise in RLSVI set for exploration simultaneously provides privacy protection. Specifically, we prove that RLSVI is $(\varepsilon(\delta),\delta)$-joint differentially private in tabular MDP as is with $\varepsilon(\delta) = \frac{2AK}{H^2\log(2HSA)} + 2\sqrt{\frac{2AK\log(1/\delta)}{H^2\log(2HSA)}}$, where $S$ and $A$ are the number of states and actions respectively, $H$ is the length of an episode and $K$ is the number of episodes.

---


### 496. [Flow-Transformed Implicit Processes for Function-Space Variational Inference](https://arxiv.org/abs/2606.01954)

**<font color=#1a73e8>作者：</font>** Luis A. Ortega, Andrés R. Masegosa, Thomas D. Nielsen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Implicit-process priors define distributions over functions through flexible generative mechanisms, making them attractive for Bayesian function-space modelling. However, performing posterior inference with such priors is challenging because their induced function-space distributions are typically not available in closed form. One practical strategy is to approximate the prior using a finite collection of sampled functions, and then represent posterior functions as learned combinations of these samples. Existing approaches commonly place a Gaussian variational distribution over the combination weights. While tractable, this choice limits the shapes of posterior uncertainty that can be represented, especially when the true posterior is asymmetric, heavy-tailed, or multimodal. We propose Flow-Transformed Implicit Processes (FTIP), a variational inference method that makes this finite-dimensional function-space approximation more expressive. Instead of using a Gaussian distribution over the combination weights, FTIP uses a normalizing flow to define a richer variational distribution. This induces a flexible posterior distribution over functions while preserving tractable optimization. We train the model using a Black-Box {\alpha} objective, allowing us to compare mass-covering and mode-seeking variational behaviour. Experiments show that FTIP captures asymmetric and multimodal posterior structure in function space that Gaussian coefficient approximations tend to smooth or collapse.

---


### 497. [Contrastive Augmented Transformer with Domain-specific Enhancement for Robust Multi-scenario Metal Surface Defect Detection](https://arxiv.org/abs/2606.01962)

**<font color=#1a73e8>作者：</font>** Yiyao Liua, Wenxiao He, Liyuan Ren 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Metal surface defect detection is critical for maintaining product quality in industrial manufacturing. However, it faces significant challenges, including limited annotated data, difficulty in identifying subtle multi-scale defects, and poor generalization across diverse scenarios. To address these issues, this paper proposes a novel Contrastive Augmented Transformer (CAT) framework for robust defect detection. CAT employs a hierarchical Swin Transformer backbone and redesigns the feature pyramid network to effectively fuse low-level textures with high-level semantics, enabling precise modeling of subtle and multi-scale defect patterns. To enhance robustness under real-world noise conditions, we propose a domain-specific droplet augmentation algorithm. Furthermore, we incorporate a hard negative mining strategy into the contrastive loss to strengthen the model's discrimination ability in ambiguous defect regions. Experimental results on the KolektorSDD2 dataset demonstrate that CAT achieves a pixel-level AUROC of 99.54%, outperforming existing methods. In addition, CAT exhibits superior generalization and robustness on three unseen datasets, including KSDD1, MTD for tile defects, and MSDD for rail surface defects, demonstrating its potential for wide-scale industrial deployment.

---


### 498. [Eyettention II: A Dual-Sequence Architecture for Modeling Fixation Location, Within-Word Landing Position, and Fixation Duration in Reading](https://arxiv.org/abs/2606.01964)

**<font color=#1a73e8>作者：</font>** Shuwen Deng, Cui Ding, David R. Reich 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The way our eyes move while reading provides valuable insights into both the reader's cognitive processes and the properties of the text. In particular, eye-tracking-while-reading data has shown to be highly beneficial in various technological applications, such as enhancing and interpreting language models and inferring a reader's characteristics. However, these applications often rely on large-scale, data-driven models, which demand extensive eye-tracking datasets that are challenging to obtain due to the resource-intensive nature of data collection. To address the challenge of data scarcity, we develop Eyettention II, an end-to-end trained deep-learning model capable of generating realistic scanpaths consisting of a complete set of fixation attributes in chronological order, including fixation location, within-word landing position, and fixation duration. Our model is lightweight, efficiently trainable on limited GPU resources, and closely aligned with cognitive theories. We demonstrate that Eyettention II surpasses state-of-the-art models in scanpath prediction and mirrors human-like gaze behavior by capturing key psycholinguistic phenomena. With its robust performance, Eyettention II holds the potential to drive advancements in natural language processing, facilitate piloting the materials of psycholinguistic experiments, and uncover new insights beyond what is explicitly encoded in theoretical cognitive models.

---


### 499. [Implementation and Optimization of HQC Decoding on NPU-Integrated Devices](https://arxiv.org/abs/2606.01968)

**<font color=#1a73e8>作者：</font>** Vu Minh Chau, Nguyen Ngoc Kiet, Pham Quang Minh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hamming Quasi-Cyclic (HQC) has been selected by NIST for standardization as an additional code-based key-encapsulation mechanism, providing algorithmic diversity alongside lattice-based post-quantum cryptography. Efficient deployment of HQC on mobile and embedded platforms, however, requires careful optimization of its decoding procedure, whose Reed-Muller and Reed-Solomon components dominate the computational cost. This paper studies HQC decoding on Qualcomm Hexagon processors in NPU-integrated devices, focusing on the Hexagon Vector eXtensions (HVX) backend rather than a tensor-inference engine. We observe that HQC decoding naturally exposes vector-structured computation, including Reed-Muller reliability vectors, Hadamard-transform coefficients, Reed-Solomon syndrome vectors, finite-field products, and packed support-point evaluations. Based on this observation, we redesign the dominant decoding kernels around HVX-friendly data layouts and execution patterns, including a vectorized Reed-Muller Hadamard transform, scalar-equivalent peak selection, HVX-oriented finite-field arithmetic, vectorized syndrome computation, and shortened-support locator-root evaluation. We implement and evaluate the optimized decoder using both Hexagon simulator measurements and real-device experiments on a Snapdragon~8 Gen~2 hardware development kit. The results show that Hexagon/HVX-assisted decoding substantially reduces latency and energy consumption, improving energy efficiency by up to $18.13\times$ while significantly offloading host CPU work. These results indicate that NPU-integrated mobile platforms can serve as effective backends for structured post-quantum cryptographic decoding when the underlying kernels are reformulated around vector execution.

---


### 500. [A Closer Look at In-Distribution vs. Out-of-Distribution Accuracy for Open-Set Test-time Adaptation](https://arxiv.org/abs/2606.01973)

**<font color=#1a73e8>作者：</font>** Zefeng Li, Evan Shelhamer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Open-set test-time adaptation (TTA) updates models on new data in the presence of input shifts and unknown output classes. While recent methods have made progress on improving in-distribution (InD) accuracy for known classes, their ability to accurately detect out-of-distribution (OOD) unknown classes remains underexplored. We benchmark robust and open-set TTA methods (SAR, OSTTA, UniEnt, and SoTTA) on the standard corruption benchmarks of CIFAR-10-C at the small scale and ImageNet-C at the large scale. For CIFAR-10-C, we use OOD data from SVHN and CIFAR-100 in their respective corrupted forms of SVHN-C and CIFAR-100-C. For ImageNet-C, we use OOD data from ImageNet-O and Textures in their respective corrupted forms of ImageNet-O-C and Textures-C. ImageNet-O is nearer to ImageNet, as unknown but related object classes (like ''garlic bread'' vs. ''hot dog'' for food, or ''highway'' vs. ''dam'' for infrastructure), while Textures is farther from ImageNet, as non-object patterns (like ''cracked'' mud, ''porous'' sponge, ''veined'' leaves). We evaluate the accuracy and confidence of TTA methods for InD vs. OOD recognition on CIFAR-10-C and ImageNet-C. We verify the accuracy of each method's own OOD detection technique on CIFAR-10-C. We also evaluate on ImageNet-C and report both accuracy and standard OOD detection metrics. We further examine more realistic settings, in which the proportions and rates of OOD data can vary. To explore the trade-off between InD recognition and OOD rejection, we propose a new baseline that replaces softmax/multi-class output with sigmoid/multi-label output. Our analysis shows for the first time that current open-set TTA methods struggle to balance InD and OOD accuracy and that they only imperfectly filter OOD data for their own adaptation updates.

---


> [!TIP]
> 当前位于：**451-500**（第 10/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-651](./part-14.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
