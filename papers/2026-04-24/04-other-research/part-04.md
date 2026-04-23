# 📦 其他研究 | 2026年04月24日

> 本类共 **220** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-220](./part-05.md)

---

### 151. [Surrogate Functionals for Machine-Learned Orbital-Free Density Functional Theory](https://arxiv.org/abs/2604.20458)

**<font color=#1a73e8>作者：</font>** Roman Remme, Fred A. Hamprecht  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce surrogate functionals: machine-learned energy functionals for orbital-free density functional theory (OF-DFT) which are defined not by universal fidelity to a physical reference, but merely by the requirement that density optimization with a fixed procedure yields the true ground-state density. Helpfully, training surrogate functionals requires only ground-state densities, no energies or gradients away from the ground state. We here propose a gradient-descent-improvement loss that guarantees exponential convergence of the density to the ground state, and combine it with an adaptive sampling scheme that concentrates learning around the optimization trajectories actually visited during inference. On the QM9 and QMugs benchmarks, surrogate functionals achieve density errors competitive with or improving upon the state of the art for fully supervised machine-learned OF-DFT, while eliminating the need for the $O(N^3)$ orthononormalization step required by prior work, yielding improved runtime scaling for larger systems.

---


### 152. [DynamicRad: Content-Adaptive Sparse Attention for Long Video Diffusion](https://arxiv.org/abs/2604.20470)

**<font color=#1a73e8>作者：</font>** Yongji Long, Shijun Liang, Jintao Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Leveraging the natural spatiotemporal energy decay in video diffusion offers a path to efficiency, yet relying solely on rigid static masks risks losing critical long-range information in complex dynamics. To address this issue, we propose \textbf{DynamicRad}, a unified sparse-attention paradigm that grounds adaptive selection within a radial locality prior. DynamicRad introduces a \textbf{dual-mode} strategy: \textit{static-ratio} for speed-optimized execution and \textit{dynamic-threshold} for quality-first filtering. To ensure robustness without online search overhead, we integrate an offline Bayesian Optimization (BO) pipeline coupled with a \textbf{semantic motion router}. This lightweight projection module maps prompt embeddings to optimal sparsity regimes with \textbf{minimal runtime overhead}. Unlike online profiling methods, our offline BO optimizes attention reconstruction error (MSE) on a physics-based proxy task, ensuring rapid convergence. Experiments on HunyuanVideo and Wan2.1-14B demonstrate that DynamicRad pushes the efficiency--quality Pareto frontier, achieving \textbf{1.7$\times$--2.5$\times$ inference speedups} with \textbf{over 80\% effective sparsity}. In some long-sequence settings, the dynamic mode even matches or exceeds the dense baseline, while mask-aware LoRA further improves long-horizon coherence. Code is available at this https URL.

---


### 153. [Random Walk on Point Clouds for Feature Detection](https://arxiv.org/abs/2604.20474)

**<font color=#1a73e8>作者：</font>** Yuhe Zhang, Zhikun Tu, Zhi Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The points on the point clouds that can entirely outline the shape of the model are of critical importance, as they serve as the foundation for numerous point cloud processing tasks and are widely utilized in computer graphics and computer-aided design. This study introduces a novel method, RWoDSN, for extracting such feature points, incorporating considerations of sharp-to-smooth transitions, large-to-small scales, and textural-to-detailed features. We approach feature extraction as a two-stage context-dependent analysis problem. In the first stage, we propose a novel neighborhood descriptor, termed the Disk Sampling Neighborhood (DSN), which, unlike traditional spatially and geometrically invariant approaches, preserves a matrix structure while maintaining normal neighborhood relationships. In the second stage, a random walk is performed on the DSN (RWoDSN), yielding a graph-based DSN that simultaneously accounts for the spatial distribution, topological properties, and geometric characteristics of the local surface surrounding each point. This enables the effective extraction of feature points. Experimental results demonstrate that the proposed RWoDSN method achieves a recall of 0.769-22% higher than the current state-of-the-art-alongside a precision of 0.784. Furthermore, it significantly outperforms several traditional and deep-learning techniques across eight evaluation metrics.

---


### 154. [Towards Certified Malware Detection: Provable Guarantees Against Evasion Attacks](https://arxiv.org/abs/2604.20495)

**<font color=#1a73e8>作者：</font>** Nandakrishna Giri, Asmitha K. A., Serena Nicolazzo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine learning-based static malware detectors remain vulnerable to adversarial evasion techniques, such as metamorphic engine mutations. To address this vulnerability, we propose a certifiably robust malware detection framework based on randomized smoothing through feature ablation and targeted noise injection. During evaluation, our system analyzes an executable by generating multiple ablated variants, classifies them by using a smoothed classifier, and identifies the final label based on the majority vote. By analyzing the top-class voting distribution and the Wilson score interval, we derive a formal certificate that guarantees robustness within a specific radius against feature-space perturbations. We evaluate our approach by comparing the performance of the base classifier and the smoothed classifier on both clean executables and ablated variants generated using PyMetaEngine. Our results demonstrate that the proposed smoothed classifier successfully provides certifiable robustness against metamorphic evasion attacks without requiring modifications to the underlying machine learning architecture.

---


### 155. [Mythos and the Unverified Cage: Z3-Based Pre-Deployment Verification for Frontier-Model Sandbox Infrastructure](https://arxiv.org/abs/2604.20496)

**<font color=#1a73e8>作者：</font>** Dominik Blain  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The April 2026 Claude Mythos sandbox escape exposed a critical weakness in frontier AI containment: the infrastructure surrounding advanced models remains susceptible to formally characterizable arithmetic vulnerabilities. Anthropic has not publicly characterized the escape vector; some secondary accounts hypothesize a CWE-190 arithmetic vulnerability in sandbox networking code. We treat this as unverified and analyze the vulnerability class rather than the specific escape. This paper presents COBALT, a Z3 SMT-based formal verification engine for identifying CWE-190/191/195 arithmetic vulnerability patterns in C/C++ infrastructure prior to deployment.
We distinguish two classes of contribution. Validated: COBALT detects arithmetic vulnerability patterns in production codebases, producing SAT verdicts with concrete witnesses and UNSAT guarantees under explicit safety bounds. We demonstrate this on four production case studies: NASA cFE, wolfSSL, Eclipse Mosquitto, and NASA F Prime, with reproducible encodings, verified solver output, and acknowledged security outcomes. Proposed: a four-layer containment framework consisting of COBALT, VERDICT, DIRECTIVE-4, and SENTINEL, mapping pre-deployment verification, pre-execution constraints, output control, and runtime monitoring to the failure modes exposed by the Mythos incident.
Under explicit assumptions, we further argue that the publicly reported Mythos escape class is consistent with a Z3-expressible CWE-190 arithmetic formulation and that pre-deployment formal analysis would have been capable of surfacing the relevant pattern. The broader claim is infrastructural: frontier-model safety cannot depend on behavioral safeguards alone; the containment stack itself must be subjected to formal verification.

---


### 156. [Efficient Test-Time Inference via Deterministic Exploration of Truncated Decoding Trees](https://arxiv.org/abs/2604.20500)

**<font color=#1a73e8>作者：</font>** Xueyan Li, Johannes Zenn, Ekaterina Fadeeva 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-consistency boosts inference-time performance by sampling multiple reasoning traces in parallel and voting. However, in constrained domains like math and code, this strategy is compute-inefficient because it samples with replacement, repeatedly revisiting the same high-probability prefixes and duplicate completions. We propose Distinct Leaf Enumeration (DLE), a deterministic decoding method that treats truncated sampling as traversal of a pruned decoding tree and systematically enumerates distinct leaves instead of sampling with replacement. This strategy improves inference efficiency in two ways. Algorithmically, it increases coverage of the truncated search space under a fixed budget by exploring previously unvisited high-probability branches. Systemically, it reuses shared prefixes and reduces redundant token generation. Empirically, DLE explores higher-quality reasoning traces than stochastic self-consistency, yielding better performance on math, coding, and general reasoning tasks.

---


### 157. [Explicit Dropout: Deterministic Regularization for Transformer Architectures](https://arxiv.org/abs/2604.20505)

**<font color=#1a73e8>作者：</font>** Vidhi Agrawal, Illia Oleksiienko, Alexandros Iosifidis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dropout is a widely used regularization technique in deep learning, but its effects are typically realized through stochastic masking rather than explicit optimization objectives. We propose a deterministic formulation that expresses dropout as an additive regularizer directly incorporated into the training loss. The framework derives explicit regularization terms for Transformer architectures, covering attention query, key, value, and feed-forward components with independently controllable strengths. This formulation removes reliance on stochastic perturbations while providing clearer and fine-grained control over regularization strength. Experiments across image classification, temporal action detection, and audio classification show that explicit dropout matches or outperforms conventional implicit methods, with consistent gains when applied to attention and feed-forward network layers. Ablation studies demonstrate stable performance and controllable regularization through regularization coefficients and dropout rates. Overall, explicit dropout offers a practical and interpretable alternative to stochastic regularization while maintaining architectural flexibility across diverse tasks.

---


### 158. [Effects of Cross-lingual Evidence in Multilingual Medical Question Answering](https://arxiv.org/abs/2604.20531)

**<font color=#1a73e8>作者：</font>** Anar Yeginbergen, Maite Oronoz, Rodrigo Agerri  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper investigates Multilingual Medical Question Answering across high-resource (English, Spanish, French, Italian) and low-resource (Basque, Kazakh) languages. We evaluate three types of external evidence sources across models of varying size: curated repositories of specialized medical knowledge, web-retrieved content, and explanations from LLM's parametric knowledge. Moreover, we conduct experiments with multilingual, monolingual and cross-lingual retrieval. Our results demonstrate that larger models consistently achieve superior performance in English across baseline evaluations. When incorporating external knowledge, web-retrieved data in English proves most beneficial for high-resource languages. Conversely, for low-resource languages, the most effective strategy combines retrieval in both English and the target language, achieving comparable accuracy to high-resource language results. These findings challenge the assumption that external knowledge systematically improves performance and reveal that effective strategies depend on both the source of language resources and on model scale. Furthermore, specialized medical knowledge sources such as PubMed are limited: while they provide authoritative expert knowledge, they lack adequate multilingual coverage

---


### 159. [Aligning Stuttered-Speech Research with End-User Needs: Scoping Review, Survey, and Guidelines](https://arxiv.org/abs/2604.20535)

**<font color=#1a73e8>作者：</font>** Hawau Olamide Toyin, Mutiah Apampa, Toluwani Aremu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Atypical speech is receiving greater attention in speech technology research, but much of this work unfolds with limited interdisciplinary dialogue. For stuttered speech in particular, it is widely recognised that current speech recognition systems fall short in practice, and current evaluation methods and research priorities are not systematically grounded in end-user experiences and needs. In this work, we analyse these gaps through 1) a scoping review of papers that deal with stuttered speech and 2) a survey of 70 stakeholders, including adults who stutter and speech-language pathologists. By analysing these two perspectives, we propose a taxonomy of stuttered-speech research, identify where current research directions diverge from the needs articulated by stakeholders, and conclude by outlining concrete guidelines and directions towards addressing the real needs of the stuttering community.

---


### 160. [RefAerial: A Benchmark and Approach for Referring Detection in Aerial Images](https://arxiv.org/abs/2604.20543)

**<font color=#1a73e8>作者：</font>** Guyue Hu, Hao Song, Yuxing Tong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Referring detection refers to locate the target referred by natural languages, which has recently attracted growing research interests. However, existing datasets are limited to ground images with large object centered in relative small scenes. This paper introduces a large-scale challenging dataset for referring detection in aerial images, termed as RefAerial. It distinguishes from conventional ground referring detection datasets by 4 characteristics: (1) low but diverse object-to-scene ratios, (2) numerous targets and distractors, (3)complex and fine-grained referring descriptions, (4) diverse and broad scenes in the aerial view. We also develop a human-in-the-loop referring expansion and annotation engine (REA-Engine) for efficient semi-automated referring pair annotation. Besides, we observe that existing ground referring detection approaches exhibiting serious performance degradation on our aerial dataset since the intrinsic scale variety issue within or across aerial images. Therefore, we further propose a novel scale-comprehensive and sensitive (SCS) framework for referring detection in aerial images. It consists of a mixture-of-granularity (MoG) attention and a two-stage comprehensive-to-sensitive (CtS) decoding strategy. Specifically, the mixture-of-granularity attention is developed for scale-comprehensive target understanding. In addition, the two-stage comprehensive-to-sensitive decoding strategy is designed for coarse-to-fine referring target decoding. Eventually, the proposed SCS framework achieves remarkable performance on our aerial referring detection dataset and even promising performance boost on conventional ground referring detection datasets.

---


### 161. [Evian: Towards Explainable Visual Instruction-tuning Data Auditing](https://arxiv.org/abs/2604.20544)

**<font color=#1a73e8>作者：</font>** Zimu Jia, Mingjie Xu, Andrew Estornell 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The efficacy of Large Vision-Language Models (LVLMs) is critically dependent on the quality of their training data, requiring a precise balance between visual fidelity and instruction-following capability. Existing datasets, however, are plagued by inconsistent quality, and current data filtering methods rely on coarse-grained scores that lack the granularity to identify nuanced semantic flaws like logical fallacies or factual errors. This creates a fundamental bottleneck in developing more reliable models. To address this, we make three core contributions. First, we construct a large-scale, 300K-sample benchmark by systematically injecting diverse, subtle defects to provide a challenging testbed for data auditing. Second, we introduce a novel "Decomposition-then-Evaluation" paradigm that breaks model responses into constituent cognitive components: visual description, subjective inference, and factual claim, enabling targeted analysis. Third, we instantiate this paradigm via EVIAN (Explainable Visual Instruction-tuning Data AuditiNg), an automated framework that evaluates these components along the orthogonal axes of Image-Text Consistency, Logical Coherence, and Factual Accuracy. Our empirical findings challenge the prevailing scale-centric paradigm: a model fine-tuned on a compact, high-quality subset curated by EVIAN consistently surpassed models trained on orders-of-magnitude larger datasets. We also reveal that dividing complex auditing into verifiable subtasks enables robust curation, and that Logical Coherence is the most critical factor in data quality evaluation.

---


### 162. [Measuring the Machine: Evaluating Generative AI as Pluralist Sociotechical Systems](https://arxiv.org/abs/2604.20545)

**<font color=#1a73e8>作者：</font>** Rebecca L. Johnson  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In measurement theory, instruments do not simply record reality; they help constitute what is observed. The same holds for generative AI evaluation: benchmarks do not just measure, they shape what models appear to be. Functionalist benchmarks treat models as isolated predictors, while prescriptive approaches assess what systems ought to be. Both obscure the sociotechnical processes through which meaning and values are enacted, risking the reification of narrow cultural perspectives in pluralist contexts.
This thesis advances a descriptive alternative. It argues that generative AI must be evaluated as a pluralist sociotechnical system and develops Machine-Society-Human (MaSH) Loops, a framework for tracing how models, users, and institutions recursively co-construct meaning and values. Evaluation shifts from judging outputs to examining how values are enacted in interaction.
Three contributions follow. Conceptually, MaSH Loops reframes evaluation as recursive, enactive process. Methodologically, the World Values Benchmark introduces a distributional approach grounded in World Values Survey data, structured prompt sets, and anchor-aware scoring. Empirically, the thesis demonstrates these through two cases: value drift in early GPT-3 and sociotechnical evaluation in real estate. A final chapter draws on participatory realism to argue that prompting and evaluation are constitutive interventions, not neutral observations.
The thesis argues that static benchmarks are insufficient for generative AI. Responsible evaluation requires pluralist, process-oriented frameworks that make visible whose values are enacted. Evaluation is therefore a site of governance, shaping how AI systems are understood, deployed, and trusted.

---


### 163. [Enhancing Research Idea Generation through Combinatorial Innovation and Multi-Agent Iterative Search Strategies](https://arxiv.org/abs/2604.20548)

**<font color=#1a73e8>作者：</font>** Shuai Chen, Chengzhi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific progress depends on the continual generation of innovative re-search ideas. However, the rapid growth of scientific literature has greatly increased the cost of knowledge filtering, making it harder for researchers to identify novel directions. Although existing large language model (LLM)-based methods show promise in research idea generation, the ideas they produce are often repetitive and lack depth. To address this issue, this study proposes a multi-agent iterative planning search strategy inspired by com-binatorial innovation theory. The framework combines iterative knowledge search with an LLM-based multi-agent system to generate, evaluate, and re-fine research ideas through repeated interaction, with the goal of improving idea diversity and novelty. Experiments in the natural language processing domain show that the proposed method outperforms state-of-the-art base-lines in both diversity and novelty. Further comparison with ideas derived from top-tier machine learning conference papers indicates that the quality of the generated ideas falls between that of accepted and rejected papers. These results suggest that the proposed framework is a promising approach for supporting high-quality research idea generation. The source code and dataset used in this paper are publicly available on Github repository: this https URL. The demo is available at this https URL.

---


### 164. [Amortized Vine Copulas for High-Dimensional Density and Information Estimation](https://arxiv.org/abs/2604.20568)

**<font color=#1a73e8>作者：</font>** Houman Safaai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modeling high-dimensional dependencies while keeping likelihoods tractable remains challenging. Classical vine-copula pipelines are interpretable but can be expensive, while many neural estimators are flexible but less structured. In this work, we propose Vine Denoising Copula (VDC), an amortized vine-copula pipeline that trains a single bivariate denoising model and reuses it across all vine edges. For each edge, given pseudo-observations, the model predicts a density grid. We then apply an IPFP/Sinkhorn projection that enforces non-negativity, unit mass, and uniform marginals. This keeps the exact vine likelihood and preserves the usual copula interpretation while replacing repeated per-edge optimization with GPU inference. Across synthetic and real-data benchmarks, VDC delivers strong bivariate density accuracy, competitive MI/TC estimation, and substantial speedups for high-dimensional vine fitting. In practice, these gains make explicit information estimation and dependence decomposition feasible at scales where repeated vine fitting would otherwise be costly, although conditional downstream inference remains mixed.

---


### 165. [Ask Only When Needed: Proactive Retrieval from Memory and Skills for Experience-Driven Lifelong Agents](https://arxiv.org/abs/2604.20572)

**<font color=#1a73e8>作者：</font>** Yuxuan Cai, Jie Zhou, Qin Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Online lifelong learning enables agents to accumulate experience across interactions and continually improve on long-horizon tasks. However, existing methods typically treat retrieval from past experience as a passive operation, triggering it only at task initialization or after completing a step. Consequently, agents often fail to identify knowledge gaps during interaction and proactively retrieve the most useful experience for the current decision. To address this limitation, we present ProactAgent, an experience-driven lifelong learning framework for proactive retrieval over a structured experience base. We first introduce Experience-Enhanced Online Evolution (ExpOnEvo), which enables continual improvement through both policy updates and memory refinement. The experience base organizes historical interactions into typed repositories, including factual memory, episodic memory, and behavioral skills, so that retrieval can provide both relevant evidence and actionable guidance. On top of this, we propose Proactive Reinforcement Learning-based Retrieval (ProactRL), which models retrieval as an explicit policy action and learns when and what to retrieve via paired-branch process rewards. By comparing continuations from identical interaction prefixes with and without retrieval, ProactRL provides step-level supervision for retrieval decisions, encouraging retrieval only when it leads to better task outcomes or higher efficiency. Experiments on SciWorld, AlfWorld, and StuLife show that ProactAgent consistently improves lifelong agent performance, achieving success rates of 73.50\% on SciWorld and 71.28\% on AlfWorld while substantially reducing retrieval overhead, and attains performance competitive with proprietary models on StuLife.

---


### 166. [Where are they looking in the operating room?](https://arxiv.org/abs/2604.20574)

**<font color=#1a73e8>作者：</font>** Keqi Chen, Séraphin Baributsa, Lilien Schewski 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Purpose: Gaze-following, the task of inferring where individuals are looking, has been widely studied in computer vision, advancing research in visual attention modeling, social scene understanding, and human-robot interaction. However, gaze-following has never been explored in the operating room (OR), a complex, high-stakes environment where visual attention plays an important role in surgical workflow analysis. In this work, we introduce the concept of gaze-following to the surgical domain, and demonstrate its great potential for understanding clinical roles, surgical phases, and team communications in the OR. Methods: We extend the 4D-OR dataset with gaze-following annotations, and extend the Team-OR dataset with gaze-following and a new team communication activity annotations. Then, we propose novel approaches to address clinical role prediction, surgical phase recognition, and team communication detection using a gaze-following model. For role and phase recognition, we propose a gaze heatmap-based approach that uses gaze predictions solely; for team communication detection, we train a spatial-temporal model in a self-supervised way that encodes gaze-based clip features, and then feed the features into a temporal activity detection model. Results: Experimental results on the 4D-OR and Team-OR datasets demonstrate that our approach achieves state-of-the-art performance on all downstream tasks. Quantitatively, our approach obtains F1 scores of 0.92 for clinical role prediction and 0.95 for surgical phase recognition. Furthermore, it significantly outperforms existing baselines in team communication detection, improving previous best performances by over 30%. Conclusion: We introduce gaze-following in the OR as a novel research direction in surgical data science, highlighting its great potential to advance surgical workflow analysis in computer-assisted interventions.

---


### 167. [PVAC: A RowHammer Mitigation Architecture Exploiting Per-victim-row Counting](https://arxiv.org/abs/2604.20576)

**<font color=#1a73e8>作者：</font>** Jumin Kim, Seungmin Baek, Hwayong Nam 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As DRAM scaling exacerbates RowHammer, DDR5 introduces per-row activation counting (PRAC) to track aggressor activity. However, PRAC indiscriminately increments counters on every activation -- including benign refreshes -- while relying solely on explicit RFM operations for resets. Consequently, counters saturate even in an idle bank, triggering cascading mitigations and degrading performance. This vulnerability arises from a fundamental mismatch: PRAC tracks the aggressor but aims to protect the victim.
We present Per-Victim-row hAmmered Counting (PVAC), a victim-based counting mechanism that aligns the counter semantics with the physical disturbance mechanism of RowHammer. PVAC increments the counters of victim rows, resets the activated row, and naturally bounds counter values under normal refresh. To enable efficient victim-based updates, PVAC employs a dedicated counter subarray (CSA) that performs all counter resets and increments concurrently with normal accesses, without timing overhead. We further devise an energy-efficient CSA layout that minimizes refresh-induced counter accesses. Through victim-based counting, PVAC supports higher hammering tolerance than PRAC while maintaining the same worst-case safety guarantee. Across benign workloads and adversarial attack patterns, PVAC avoids spurious Alerts, eliminates PRAC timing penalties, and achieves higher performance and lower energy consumption than prior PRAC-based defenses.

---


### 168. [On the Impact of Face Segmentation-Based Background Removal on Recognition and Morphing Attack Detection](https://arxiv.org/abs/2604.20585)

**<font color=#1a73e8>作者：</font>** Eduarda Caldeira, Guray Ozgur, Fadi Boutros 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This study investigates the impact of face image background correction through segmentation on face recognition and morphing attack detection performance in realistic, unconstrained image capture scenarios. The motivation is driven by operational biometric systems such as the European Entry/Exit System (EES), which require facial enrolment at airports and other border crossing points where controlled backgrounds usually required for such captures cannot always be guaranteed, as well as by accessibility needs that may necessitate image capture outside traditional office environments. By analyzing how such preprocessing steps influence both recognition accuracy and security mechanisms, this work addresses a critical gap between usability-driven image normalization and the reliability requirements of large-scale biometric identification systems. Our study evaluates a comprehensive range of segmentation techniques, three families of morphing attack detection methods, and four distinct face recognition models, using databases that include both controlled and in-the-wild image captures. The results reveal consistent patterns linking segmentation to both recognition performance and face image quality. Additionally, segmentation is shown to systematically influence morphing attack detection performance. These findings highlight the need for careful consideration when deploying such preprocessing techniques in operational biometric systems.

---


### 169. [A Hierarchical MARL-Based Approach for Coordinated Retail P2P Trading and Wholesale Market Participation of DERs](https://arxiv.org/abs/2604.20586)

**<font color=#1a73e8>作者：</font>** Patrick Wilk, Ethan Cantor, Yikui Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The ongoing shift towards decentralization of the electric energy sector, driven by the growing electrification across end-use sectors, and widespread adoption of distributed energy resources (DERs), necessitates their active participation in the electricity markets to support grid operations. Furthermore, with bi-directional energy and communication flows becoming standard, intelligent, easy-to-deploy, resource-conservative demand-side participation is expected to play a critical role in securing power grid operational flexibility and market efficiency. This work proposes a market engagement framework that leverages a hierarchical multi-agent deep reinforcement learning (MARL) approach to enable individual prosumers to participate in peer-to-peer retail auctions and further aggregate these intelligent prosumers to facilitate effective DER participation in wholesale markets. Ultimately, a Stackelberg game is proposed to coordinate this hierarchical MARL-based DER market participation framework toward enhanced market performance.

---


### 170. [Structure-Augmented Standard Plane Detection with Temporal Aggregation in Blind-Sweep Fetal Ultrasound](https://arxiv.org/abs/2604.20591)

**<font color=#1a73e8>作者：</font>** Keli Niu, He Zhao, Qianhui Men  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In low-resource settings, blind-sweep ultrasound provides a practical and accessible method for identifying fetal growth restriction. However, unlike freehand ultrasound which is subjectively controlled, detection of biometry plane in blind-sweep ultrasound is more challenging due to the uncontrolled fetal structure to be observed and the variaties of oblique planes in the scan. In this work, we propose a structure-augmented system to detect fetal abdomen plane, where the abdominal structure is highlighted using a segmentation prior. Since standard planes are emerging gradually, the decision boundary of the keyframes is unstable to predict. We thus aggregated the structure-augmented planes with a temporal sliding window to help stabilise keyframe localisation. Extensive results indicate that the structure-augmented temporal sliding strategy significantly improves and stabilises the detection of anatomically meaningful planes, which enables more reliable biometric measurements in blind-sweep ultrasound.

---


### 171. [Physics-Informed Conditional Diffusion for Motion-Robust Retinal Temporal Laser Speckle Contrast Imaging](https://arxiv.org/abs/2604.20594)

**<font color=#1a73e8>作者：</font>** Qian Chen, Yuehao Chen, Qiang Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Retinal laser speckle contrast imaging (LSCI) is a noninvasive optical modality for monitoring retinal blood flow dynamics. However, conventional temporal LSCI (tLSCI) reconstruction relies on sufficiently long speckle sequences to obtain stable temporal statistics, which makes it vulnerable to acquisition disturbances and limits effective temporal resolution. A physically informed reconstruction framework, termed RetinaDiff (Retinal Diffusion Model), is proposed for retinal tLSCI that is robust to motion and requires only a few frames. In RetinaDiff, registration based on phase correlation is first applied to stabilize the raw speckle sequence before contrast computation, reducing interframe misalignment so that fluctuations at each pixel primarily reflect true flow dynamics. This step provides a physics prior corrected for motion and a high quality multiframe tLSCI reference. Next, guided by the physics prior, a conditional diffusion model performs inverse reconstruction by jointly conditioning on the registered speckle sequence and the corrected prior. Experiments on data acquired with a retinal LSCI system developed in house show improved structural continuity and statistical stability compared with direct reconstruction from few frames and representative baselines. The framework also remains effective in a small number of extremely challenging cases, where both the direct 5-frame input and the conventional multiframe reconstruction are severely degraded. Overall, this work provides a practical and physically grounded route for reliable retinal tLSCI reconstruction from extremely limited frames. The source code and model weights will be publicly available at this https URL.

---


### 172. [Differentially Private Clustered Federated Learning with Privacy-Preserving Initialization and Normality-Driven Aggregation](https://arxiv.org/abs/2604.20596)

**<font color=#1a73e8>作者：</font>** Jie Xu, Haaris Mehmood, Rogier Van Dalen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) enables training of a global model while keeping raw data on end-devices. Despite this, FL has shown to leak private user information and thus in practice, it is often coupled with methods such as differential privacy (DP) and secure vector sum to provide formal privacy guarantees to its participants. In realistic cross-device deployments, the data are highly heterogeneous, so vanilla federated learning converges slowly and generalizes poorly. Clustered federated learning (CFL) mitigates this by segregating users into clusters, leading to lower intra-cluster data heterogeneity. Nevertheless, coupling CFL with DP remains challenging: the injected DP noise makes individual client updates excessively noisy, and the server is unable to initialize cluster centroids with the less noisy aggregated updates. To address this challenge, we propose PINA, a two-stage framework that first lets each client fine-tune a lightweight low-rank adaptation (LoRA) adapter and privately share a compressed sketch of the update. The server leverages these sketches to construct robust cluster centroids. In the second stage, PINA introduces a normality-driven aggregation mechanism that improves convergence and robustness. Our method retains the benefits of clustered FL while providing formal privacy guarantees against an untrusted server. Extensive evaluations show that our proposed method outperforms state-of-the-art DP-FL algorithms by an average of 2.9% in accuracy for privacy budgets (epsilon in {2, 8}).

---


### 173. [Self-Guided Plan Extraction for Instruction-Following Tasks with Goal-Conditional Reinforcement Learning](https://arxiv.org/abs/2604.20601)

**<font color=#1a73e8>作者：</font>** Zoya Volovikova, Nikita Sorokin, Dmitriy Lukashevskiy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce SuperIgor, a framework for instruction-following tasks. Unlike prior methods that rely on predefined subtasks, SuperIgor enables a language model to generate and refine high-level plans through a self-learning mechanism, reducing the need for manual dataset annotation. Our approach involves iterative co-training: an RL agent is trained to follow the generated plans, while the language model adapts and modifies these plans based on RL feedback and preferences. This creates a feedback loop where both the agent and the planner improve jointly. We validate our framework in environments with rich dynamics and stochasticity. Results show that SuperIgor agents adhere to instructions more strictly than baseline methods, while also demonstrating strong generalization to previously unseen instructions.

---


### 174. [Beyond ZOH: Advanced Discretization Strategies for Vision Mamba](https://arxiv.org/abs/2604.20606)

**<font color=#1a73e8>作者：</font>** Fady Ibrahim, Guangjun Liu, Guanghui Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Mamba, as a state space model (SSM), employs a zero-order hold (ZOH) discretization, which assumes that input signals remain constant between sampling instants. This assumption degrades temporal fidelity in dynamic visual environments and constrains the attainable accuracy of modern SSM-based vision models. In this paper, we present a systematic and controlled comparison of six discretization schemes instantiated within the Vision Mamba framework: ZOH, first-order hold (FOH), bilinear/Tustin transform (BIL), polynomial interpolation (POL), higher-order hold (HOH), and the fourth-order Runge-Kutta method (RK4). We evaluate each method on standard visual benchmarks to quantify its influence in image classification, semantic segmentation, and object detection. Our results demonstrate that POL and HOH yield the largest gains in accuracy at the cost of higher training-time computation. In contrast, the BIL provides consistent improvements over ZOH with modest additional overhead, offering the most favorable trade-off between precision and efficiency. These findings elucidate the pivotal role of discretization in SSM-based vision architectures and furnish empirically grounded justification for adopting BIL as the default discretization baseline for state-of-the-art SSM models.

---


### 175. [Too Sharp, Too Sure: When Calibration Follows Curvature](https://arxiv.org/abs/2604.20614)

**<font color=#1a73e8>作者：</font>** Alessandro Morosini, Matea Gjika, Tomaso Poggio 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern neural networks can achieve high accuracy while remaining poorly calibrated, producing confidence estimates that do not match empirical correctness. Yet calibration is often treated as a post-hoc attribute. We take a different perspective: we study calibration as a training-time phenomenon on small vision tasks, and ask whether calibrated solutions can be obtained reliably by intervening on the training procedure. We identify a tight coupling between calibration, curvature, and margins during training of deep networks under multiple gradient-based methods. Empirically, Expected Calibration Error (ECE) closely tracks curvature-based sharpness throughout optimization. Mathematically, we show that both ECE and Gauss--Newton curvature are controlled, up to problem-specific constants, by the same margin-dependent exponential tail functional along the trajectory. Guided by this mechanism, we introduce a margin-aware training objective that explicitly targets robust-margin tails and local smoothness, yielding improved out-of-sample calibration across optimizers without sacrificing accuracy.

---


### 176. [SoK: The Next Frontier in AV Security: Systematizing Perception Attacks and the Emerging Threat of Multi-Sensor Fusion](https://arxiv.org/abs/2604.20621)

**<font color=#1a73e8>作者：</font>** Shahriar Rahman Khan, Tariqul Islam, Raiful Hasan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous vehicles (AVs) increasingly rely on multi-sensor perception pipelines that combine data from cameras, lidar, radar, and other modalities to interpret the environment. This SoK systematizes 48 peer-reviewed studies on perception-layer attacks against AVs, tracking the field's evolution from single-sensor exploits to complex cross-modal threats that compromise multi-sensor fusion (MSF). We develop a unified taxonomy of 20 attack vectors organized by sensor type, attack stage, medium, and perception module, revealing patterns that expose underexplored vulnerabilities in fusion logic and cross-sensor dependencies. Our analysis identifies key research gaps, including limited real-world testing, short-term evaluation bias, and the absence of defenses that account for inter-sensor consistency. To illustrate one such gap, we validate a fusion-level vulnerability through a proof-of-concept simulation combining infrared and lidar spoofing. The findings highlight a fundamental shift in AV security: as systems fuse more sensors for robustness, attackers exploit the very redundancy meant to ensure safety. We conclude with directions for fusion-aware defense design and a research agenda for trustworthy perception in autonomous systems.

---


### 177. [pAI/MSc: ML Theory Research with Humans on the Loop](https://arxiv.org/abs/2604.20622)

**<font color=#1a73e8>作者：</font>** Mahmoud Abdelmoneum, Pierfrancesco Beneventano, Tomaso Poggio  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present pAI/MSc, an open-source, customizable, modular multi-agent system for academic research workflows. Our goal is not autonomous scientific ideation, nor fully automated research. It is narrower and more practical: to reduce by orders of magnitude the human steering required to turn a specified hypothesis into a literature-grounded, mathematically established, experimentally supported, submission-oriented manuscript draft. pAI/MSc is built with a current emphasis on machine learning theory and adjacent quantitative fields.

---


### 178. [RSRCC: A Remote Sensing Regional Change Comprehension Benchmark Constructed via Retrieval-Augmented Best-of-N Ranking](https://arxiv.org/abs/2604.20623)

**<font color=#1a73e8>作者：</font>** Roie Kazoom, Yotam Gigi, George Leifman 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traditional change detection identifies where changes occur, but does not explain what changed in natural language. Existing remote sensing change captioning datasets typically describe overall image-level differences, leaving fine-grained localized semantic reasoning largely unexplored. To close this gap, we present RSRCC, a new benchmark for remote sensing change question-answering containing 126k questions, split into 87k training, 17.1k validation, and 22k test instances. Unlike prior datasets, RSRCC is built around localized, change-specific questions that require reasoning about a particular semantic change. To the best of our knowledge, this is the first remote sensing change question-answering benchmark designed explicitly for such fine-grained reasoning-based supervision. To construct RSRCC, we introduce a hierarchical semi-supervised curation pipeline that uses Best-of-N ranking as a critical final ambiguity-resolution stage. First, candidate change regions are extracted from semantic segmentation masks, then initially screened using an image-text embedding model, and finally validated through retrieval-augmented vision-language curation with Best-of-N ranking. This process enables scalable filtering of noisy and ambiguous candidates while preserving semantically meaningful changes. The dataset is available at this https URL.

---


### 179. [Occupancy Reward Shaping: Improving Credit Assignment for Offline Goal-Conditioned Reinforcement Learning](https://arxiv.org/abs/2604.20627)

**<font color=#1a73e8>作者：</font>** Aravind Venugopal, Jiayu Chen, Xudong Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The temporal lag between actions and their long-term consequences makes credit assignment a challenge when learning goal-directed behaviors from data. Generative world models capture the distribution of future states an agent may visit, indicating that they have captured temporal information. How can that temporal information be extracted to perform credit assignment? In this paper, we formalize how the temporal information stored in world models encodes the underlying geometry of the world. Leveraging optimal transport, we extract this geometry from a learned model of the occupancy measure into a reward function that captures goal-reaching information. Our resulting method, Occupancy Reward Shaping, largely mitigates the problem of credit assignment in sparse reward settings. ORS provably does not alter the optimal policy, yet empirically improves performance by 2.2x across 13 diverse long-horizon locomotion and manipulation tasks. Moreover, we demonstrate the effectiveness of ORS in the real world for controlling nuclear fusion on 3 Tokamak control tasks.
Code: this https URL Website: this https URL

---


### 180. [MAPRPose: Mask-Aware Proposal and Amodal Refinement for Multi-Object 6D Pose Estimation](https://arxiv.org/abs/2604.20650)

**<font color=#1a73e8>作者：</font>** Yang Luo, Yan Gong, Yongsheng Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 6D object pose estimation in cluttered scenes remains challenging due to severe occlusion and sensor noise. We propose MAPRPose, a two-stage framework that leverages mask-aware correspondences for pose proposal and amodal-driven Region-of-Interest (ROI) prediction for robust refinement. In the Mask-Aware Pose Proposal (MAPP) stage, we lift 2D correspondences into 3D space to establish reliable keypoint matches and generate geometrically consistent pose hypotheses based on correspondence-level scoring, from which the top-$K$ candidates are selected. In the refinement stage, we introduce a tensorized render-and-compare pipeline integrated with an Amodal Mask Prediction and ROI Re-Alignment (AMPR) module. By reconstructing complete object geometry and dynamically adjusting the ROI, AMPR mitigates localization errors and spatial misalignment under heavy occlusion. Furthermore, our GPU-accelerated RGB-XYZ reprojection enables simultaneous refinement of all $N \times B$ pose hypotheses in a single forward pass. Evaluated on the BOP benchmark, MAPRPose achieves a state-of-the-art Average Recall (AR) of 76.5%, outperforming FoundationPose by 3.1% AR while delivering a 43x speedup in multi-object inference.

---


### 181. [Short-time, Wavelet-inspired Mouse Submovement Detection](https://arxiv.org/abs/2604.20673)

**<font color=#1a73e8>作者：</font>** Auejin Ham, Ben Boudaoud  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Submovements are ballistic components of human motion constituting a large part of motor interaction and arising from the cyclical and overlapping cognitive processes of perception, motor planning, and motor execution. Extracting submovements is challenging as the motions tend to overlap, or start before the previous ends. We propose and evaluate use of a wavelet-inspired technique to accurately locate and parameterize submovements from one-dimensional speed time series. Our method employs a self-weighted loss refinement step to identify and improve regions of poor quality of fit, a challenge for simpler wavelet transforms. We demonstrate the accuracy of our method by presenting analysis of ~6,400 1-2s trials of synthetic egocentric camera (first-person shooter) aim data for which we know ground truth, modeled from a similarly sized real data set of 13 users. We compare our method to dual-threshold and the persistence 1D segmentation techniques and note challenges and opportunities for future improvements.

---


### 182. [Improving clinical interpretability of linear neuroimaging models through feature whitening](https://arxiv.org/abs/2604.20675)

**<font color=#1a73e8>作者：</font>** Sara Petiton, Antoine Grigis, Raphaël Vock 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear models are widely used in computational neuroimaging to identify biomarkers associated with brain pathologies. However, interpreting the learned weights remains challenging, as they do not always yield clinically meaningful insights. This difficulty arises in part from the inherent correlation between brain regions, which causes linear weights to reflect shared rather than region-specific contributions. In particular, some groups of regions, including homologous structures in the left and right hemispheres, are known to exhibit strong anatomical correlations. In this work, we leverage this prior neuroanatomical knowledge to introduce a whitening approach applied to groups of regions with known shared variance, designed to disentangle overlapping information across correlated brain measures. We additionally propose a regularized variant that allows controlled tuning of the degree of decorrelation. We evaluate this method using region-of-interest features in two psychiatric classification tasks, distinguishing individuals with bipolar disorder or schizophrenia from healthy controls. Importantly, unlike PCA or ICA which use whitening as a dimensionality reduction step, our approach decorrelates anatomically informed pairs of neuroanatomical regions while retaining the full input signal, making it specifically suited for feature interpretation rather than feature selection. Our findings demonstrate that whitening improves the interpretability of model weights while preserving predictive performance, providing a robust framework for linking linear model outputs to neurobiological mechanisms.

---


### 183. [Variance Is Not Importance: Structural Analysis of Transformer Compressibility Across Model Scales](https://arxiv.org/abs/2604.20682)

**<font color=#1a73e8>作者：</font>** Samuel Salfati  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a systematic empirical study of transformer compression through over 40 experiments on GPT-2 (124M parameters) and Mistral 7B (7.24B parameters). Our analysis covers spectral compression, block-level function replacement, rotation-based quantization, activation geometry, and adaptive early exit.
We identify five structural properties relevant to compression. (1) Variance is not importance: high-variance activation directions are approximately 96 percent uncorrelated with predictive directions (measured via CCA), and projecting onto these subspaces preserves over 90 percent of variance while degrading perplexity. (2) Block linearity is conditional: transformer blocks are approximately linear (R^2 ~ 0.95 on GPT-2, 0.93 on Mistral block 31) only under the correct upstream distribution; modifying earlier blocks induces distribution shift that degrades downstream approximations. (3) The reconstruction wall: approaches that factor weights into quantized components amplify errors through cross-terms, making direct quantization strictly superior. (4) Linearity increases with depth: Mistral 7B exhibits a progression from R^2 = 0.17 (block 0) to R^2 = 0.93 (block 31), indicating a division between nonlinear feature construction and linear refinement. (5) Approximately 30 percent of tokens are computationally easy, confirmed via exit heads and KL divergence sensitivity.
We demonstrate that single-block linear replacement achieves 34x compression with a 1.71 perplexity increase on the final block of Mistral 7B, while multi-block replacement fails due to residual error accumulation and distribution shift. These findings suggest fundamental limits to static post-training compression and motivate adaptive, per-token computation as a more effective direction.

---


### 184. [Storm Surge Modeling, Bias Correction, Graph Neural Networks, Graph Convolution Networks](https://arxiv.org/abs/2604.20688)

**<font color=#1a73e8>作者：</font>** Noujoud Nader, Stefanos Giaremis, Clint Dawson 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Storm surge forecasting remains a critical challenge in mitigating the impacts of tropical cyclones on coastal regions, particularly given recent trends of rapid intensification and increasing nearshore storm activity. Traditional high fidelity numerical models such as ADCIRC, while robust, are often hindered by inevitable uncertainties arising from various sources. To address these challenges, this study introduces StormNet, a spatio-temporal graph neural network (GNN) designed for bias correction of storm surge forecasts. StormNet integrates graph convolutional (GCN) and graph attention (GAT) mechanisms with long short-term memory (LSTM) components to capture complex spatial and temporal dependencies among water-level gauge stations. The model was trained using historical hurricane data from the U.S. Gulf Coast and evaluated on Hurricane Idalia (2023). Results demonstrate that StormNet can effectively reduce the root mean square error (RMSE) in water-level predictions by more than 70\% for 48-hour forecasts and above 50\% for 72-hour forecasts, as well as outperform a sequential LSTM baseline, particularly for longer prediction horizons. The model also exhibits low training time, enhancing its applicability in real-time operational forecasting systems. Overall, StormNet provides a computationally efficient and physically meaningful framework for improving storm surge prediction accuracy and reliability during extreme weather events.

---


### 185. [Auto-ART: Structured Literature Synthesis and Automated Adversarial Robustness Testing](https://arxiv.org/abs/2604.20704)

**<font color=#1a73e8>作者：</font>** Abhijit Talluri  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Adversarial robustness evaluation underpins every claim of trustworthy ML deployment, yet the field suffers from fragmented protocols and undetected gradient masking. We make two contributions. (1) Structured synthesis. We analyze nine peer-reviewed corpus sources (2020--2026) through seven complementary protocols, producing the first end-to-end structured analysis of the field's consensus and unresolved challenges. (2) Auto-ART framework. We introduce Auto-ART, an open-source framework that operationalizes identified gaps: 50+ attacks, 28 defense modules, the Robustness Diagnostic Index (RDI), and gradient-masking detection. It supports multi-norm evaluation (l1/l2/linf/semantic/spatial) and compliance mapping to NIST AI RMF, OWASP LLM Top 10, and the EU AI Act. Empirical validation on RobustBench demonstrates that Auto-ART's pre-screening identifies gradient masking in 92% of flagged cases, and RDI rankings correlate highly with full AutoAttack. Multi-norm evaluation exposes a 23.5 pp gap between average and worst-case robustness on state-of-the-art models. No prior work combines such structured meta-scientific analysis with an executable evaluation framework bridging literature gaps into engineering.

---


### 186. [Generative Flow Networks for Model Adaptation in Digital Twins of Natural Systems](https://arxiv.org/abs/2604.20707)

**<font color=#1a73e8>作者：</font>** Pascal Archambault, Houari Sahraoui, Eugene Syriani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Digital twins of natural systems must remain aligned with physical systems that evolve over time, are only partially observed, and are typically modeled by mechanistic simulators whose parameters cannot be measured directly. In such settings, model adaptation is naturally posed as a simulation-based inference problem. However, sparse and indirect observations often fail to identify a unique and optimal calibration, leaving several simulator parameterizations compatible with the available evidence. This article presents a GFlowNet-based approach to model adaptation for digital twins of natural systems. We formulate adaptation as a generative modeling problem over complete simulator configurations, so that plausible parameterizations can be sampled with probability proportional to a reward derived from agreement between simulated and observed behavior. Using a controlled environment agriculture case study based on a mechanistic tomato model, we show that the learned policy recovers dominant regions of the adaptation landscape, retrieves strong calibration hypotheses, and preserves multiple plausible configurations under uncertainty.

---


### 187. [Participatory provenance as representational auditing for AI-mediated public consultation](https://arxiv.org/abs/2604.20711)

**<font color=#1a73e8>作者：</font>** Sachit Mahajan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence is increasingly deployed to synthesize large-scale public input in policy consultations and participatory processes. Yet no formal framework exists for auditing whether these summaries faithfully represent the source population, an accountability gap that existing approaches to AI explainability, grounding and hallucination detection do not address because they focus on output quality rather than input fidelity. Here, participatory provenance is introduced: a measurement framework grounded in optimal transport theory, causal inference and semantic analysis that tracks how individual public submissions are transformed, filtered or lost through AI-mediated summarization. Applied to Canada's 2025-2026 national AI Strategy consultation ($n = 5{,}253$ respondents across two independent policy topics), the framework reveals that both official government summaries underperform a random-participant baseline ($-9.1\%$ and $-8.0\%$ coverage degradation), with $16.9\%$ and $15.3\%$ of participants effectively excluded. Exclusion concentrates in clusters expressing dissent, scepticism and critique of AI ($33$-$88\%$ exclusion rates). Brevity, semantic isolation and rhetorical register independently predict representational outcome. An accompanying open-source interactive tool, the Co-creation Provenance Lab, enables policymakers to audit and iteratively improve summaries, establishing genuine human-in-the-loop oversight at scale.

---


### 188. [Learning to Evolve: A Self-Improving Framework for Multi-Agent Systems via Textual Parameter Graph Optimization](https://arxiv.org/abs/2604.20714)

**<font color=#1a73e8>作者：</font>** Shan He, Runze Wang, Zhuoyun Du 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Designing and optimizing multi-agent systems (MAS) is a complex, labor-intensive process of "Agent Engineering." Existing automatic optimization methods, primarily focused on flat prompt tuning, lack the structural awareness to debug the intricate web of interactions in MAS. More critically, these optimizers are static; they do not learn from experience to improve their own optimization strategies. To address these gaps, we introduce Textual Parameter Graph Optimization (TPGO), a framework that enables a multi-agent system to learn to evolve. TPGO first models the MAS as a Textual Parameter Graph (TPG), where agents, tools, and workflows are modular, optimizable nodes. To guide evolution, we derive "textual gradients," structured natural language feedback from execution traces, to pinpoint failures and suggest granular modifications. The core of our framework is Group Relative Agent Optimization (GRAO), a novel meta-learning strategy that learns from historical optimization experiences. By analyzing past successes and failures, GRAO becomes progressively better at proposing effective updates, allowing the system to learn how to optimize itself. Extensive experiments on complex benchmarks like GAIA and MCP-Universe show that TPGO significantly enhances the performance of state-of-the-art agent frameworks, achieving higher success rates through automated, self-improving optimization.

---


### 189. [GeoRelight: Learning Joint Geometrical Relighting and Reconstruction with Flexible Multi-Modal Diffusion Transformers](https://arxiv.org/abs/2604.20715)

**<font color=#1a73e8>作者：</font>** Yuxuan Xue, Ruofan Liang, Egor Zakharov 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Relighting a person from a single photo is an attractive but ill-posed task, as a 2D image ambiguously entangles 3D geometry, intrinsic appearance, and illumination. Current methods either use sequential pipelines that suffer from error accumulation, or they do not explicitly leverage 3D geometry during relighting, which limits physical consistency. Since relighting and estimation of 3D geometry are mutually beneficial tasks, we propose a unified Multi-Modal Diffusion Transformer (DiT) that jointly solves for both: GeoRelight. We make this possible through two key technical contributions: isotropic NDC-Orthographic Depth (iNOD), a distortion-free 3D representation compatible with latent diffusion models; and a strategic mixed-data training method that combines synthetic and auto-labeled real data. By solving geometry and relighting jointly, GeoRelight achieves better performance than both sequential models and previous systems that ignored geometry.

---


### 190. [Tokenised Flow Matching for Hierarchical Simulation Based Inference](https://arxiv.org/abs/2604.20723)

**<font color=#1a73e8>作者：</font>** Giovanni Charles, Cosmo Santoni, Seth Flaxman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The cost of simulator evaluations is a key practical bottleneck for Simulation Based Inference (SBI). In hierarchical settings with shared global parameters and exchangeable site-level parameters and observations, this structure can be exploited to improve simulation efficiency. Existing hierarchical SBI approaches factorise the posterior yet still simulate across multiple sites per training sample; We instead explore likelihood factorisation (LF) to train from single-site simulations. In LF sampling we learn a per-site neural surrogate of the simulator and then assemble synthetic multi-site observations to amortise inference for the full hierarchical posterior. Building on this, we propose Tokenised Flow Matching for Posterior Estimation (TFMPE), a tokenised flow matching approach that supports function-valued observations through likelihood factorisation. To enable systematic evaluation, we introduce a benchmark for hierarchical SBI. We validate TFMPE on this benchmark and on realistic infectious disease and computational fluid dynamics models, finding well-calibrated posteriors while reducing computational cost.

---


### 191. [Interval POMDP Shielding for Imperfect-Perception Agents](https://arxiv.org/abs/2604.20728)

**<font color=#1a73e8>作者：</font>** William Scarbro, Ravi Mangal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous systems that rely on learned perception can make unsafe decisions when sensor readings are misclassified. We study shielding for this setting: given a proposed action, a shield blocks actions that could violate safety. We consider the common case where system dynamics are known but perception uncertainty must be estimated from finite labeled data. From these data we build confidence intervals for the probabilities of perception outcomes and use them to model the system as a finite Interval Partially Observable Markov Decision Process with discrete states and actions. We then propose an algorithm to compute a conservative set of beliefs over the underlying state that is consistent with the observations seen so far.
This enables us to construct a runtime shield that comes with a finite-horizon guarantee: with high probability over the training data, if the true perception uncertainty rates lie within the learned intervals, then every action admitted by the shield satisfies a stated lower bound on safety. Experiments on four case studies show that our shielding approach (and variants derived from it) improves the safety of the system over state-of-the-art baselines.

---


### 192. [Near-Future Policy Optimization](https://arxiv.org/abs/2604.20733)

**<font color=#1a73e8>作者：</font>** Chuanyu Qin, Chenxu Yang, Qingyi Si 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has become a core post-training recipe. Introducing suitable off-policy trajectories into on-policy exploration accelerates RLVR convergence and raises the performance ceiling, yet finding a source of such trajectories remains the key challenge. Existing mixed-policy methods either import trajectories from external teachers (high-quality but distributionally far) or replay past training trajectories (close but capped in quality), and neither simultaneously satisfies the strong enough (higher $Q$ , more new knowledge to learn) and close enough (lower $V$ , more readily absorbed) conditions required to maximize the effective learning signal $\mathcal{S} = Q/V$. We propose \textbf{N}ear-Future \textbf{P}olicy \textbf{O}ptimization (\textbf{NPO}), a simple mixed-policy scheme that learns from a policy's own near-future self: a later checkpoint from the same training run is a natural source of auxiliary trajectories that is both stronger than the current policy and closer than any external source, directly balancing trajectory quality against variance cost. We validate NPO through two manual interventions, early-stage bootstrapping and late-stage plateau breakthrough, and further propose \textbf{AutoNPO},an adaptive variant that automatically triggers interventions from online training signals and selects the guide checkpoint that maximizes $S$. On Qwen3-VL-8B-Instruct with GRPO, NPO improves average performance from 57.88 to 62.84, and AutoNPO pushes it to 63.15, raising the final performance ceiling while accelerating convergence.

---


### 193. [Fast Bayesian equipment condition monitoring via simulation based inference: applications to heat exchanger health](https://arxiv.org/abs/2604.20735)

**<font color=#1a73e8>作者：</font>** Peter Collett, Alexander Johannes Stasik, Simone Casolo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate condition monitoring of industrial equipment requires inferring latent degradation parameters from indirect sensor measurements under uncertainty. While traditional Bayesian methods like Markov Chain Monte Carlo (MCMC) provide rigorous uncertainty quantification, their heavy computational bottlenecks render them impractical for real-time process control. To overcome this limitation, we propose an AI-driven framework utilizing Simulation-Based Inference (SBI) powered by amortized neural posterior estimation to diagnose complex failure modes in heat exchangers. By training neural density estimators on a simulated dataset, our approach learns a direct, likelihood-free mapping from thermal-fluid observations to the full posterior distribution of degradation parameters. We benchmark this framework against an MCMC baseline across various synthetic fouling and leakage scenarios, including challenging low-probability, sparse-event failures. The results show that SBI achieves comparable diagnostic accuracy and reliable uncertainty quantification, while accelerating inference time by a factor of82$\times$ compared to traditional sampling. The amortized nature of the neural network enables near-instantaneous inference, establishing SBI as a highly scalable, real-time alternative for probabilistic fault diagnosis and digital twin realization in complex engineering systems.

---


### 194. [F\textsuperscript{2}LP-AP: Fast \& Flexible Label Propagation with Adaptive Propagation Kernel](https://arxiv.org/abs/2604.20736)

**<font color=#1a73e8>作者：</font>** Yutong Shen, Ruizhe Xia, Jingyi Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Semi-supervised node classification is a foundational task in graph machine learning, yet state-of-the-art Graph Neural Networks (GNNs) are hindered by significant computational overhead and reliance on strong homophily assumptions. Traditional GNNs require expensive iterative training and multi-layer message passing, while existing training-free methods, such as Label Propagation, lack adaptability to heterophilo\-us graph structures. This paper presents \textbf{F$^2$LP-AP} (Fast and Flexible Label Propagation with Adaptive Propagation Kernel), a training-free, computationally efficient framework that adapts to local graph topology. Our method constructs robust class prototypes via the geometric median and dynamically adjusts propagation parameters based on the Local Clustering Coefficient (LCC), enabling effective modeling of both homophilous and heterophilous graphs without gradient-based training. Extensive experiments across diverse benchmark datasets demonstrate that \textbf{F$^2$LP-AP} achieves competitive or superior accuracy compared to trained GNNs, while significantly outperforming existing baselines in computational efficiency.

---


### 195. [AAC: Admissible-by-Architecture Differentiable Landmark Compression for ALT](https://arxiv.org/abs/2604.20744)

**<font color=#1a73e8>作者：</font>** An T. Le, Vien Ngo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce \textbf{AAC} (Architecturally Admissible Compressor), a differentiable landmark-selection module for ALT (A*, Landmarks, and Triangle inequality) shortest-path heuristics whose outputs are admissible by construction: each forward pass is a row-stochastic mixture of triangle-inequality lower bounds, so the heuristic is admissible for \emph{every} parameter setting without requiring convergence, calibration, or projection. At deployment, the module reduces to classical ALT on a learned subset, composing end-to-end with neural encoders while preserving the classical toolchain. The construction is the first differentiable instance of the compress-while-preserving-admissibility tradition in classical heuristic search.
Under a matched per-vertex memory protocol, we establish that ALT with farthest-point-sampling landmarks (FPS-ALT) has provably near-optimal coverage on metric graphs, leaving at most a few percentage points of headroom for \emph{any} selector. AAC operates near this ceiling: the gap is $0.9$--$3.9$ percentage points on 9 road networks and ${\leq}1.3$ percentage points on synthetic graphs, with zero admissibility violations across $1{,}500+$ queries and all logged runs. At matched memory, AAC is also $1.2$--$1.5{\times}$ faster than FPS-ALT at the median query on DIMACS road networks, amortizing its offline cost within $170$--$1{,}924$ queries. A controlled ablation isolates the binding constraint: training-objective drift under default initialization, not architectural capacity; identity-on-first-$m$ initialization closes the expansion-count gap entirely. We release the module, a reusable matched-memory benchmarking protocol with paired two-one-sided-test (TOST) equivalence and pre-registration, and a reference compressed-differential-heuristics baseline.

---


### 196. [Lifecycle-Aware Federated Continual Learning in Mobile Autonomous Systems](https://arxiv.org/abs/2604.20745)

**<font color=#1a73e8>作者：</font>** Beining Wu, Jun Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated continual learning (FCL) allows distributed autonomous fleets to adapt collaboratively to evolving terrain types across extended mission lifecycles. However, current approaches face several key challenges: 1) they use uniform protection strategies that do not account for the varying sensitivities to forgetting on different network layers; 2) they focus primarily on preventing forgetting during training, without addressing the long-term effects of cumulative drift; and 3) they often depend on idealized simulations that fail to capture the real-world heterogeneity present in distributed fleets. In this paper, we propose a lifecycle-aware dual-timescale FCL framework that incorporates training-time (pre-forgetting) prevention and (post-forgetting) recovery. Under this framework, we design a layer-selective rehearsal strategy that mitigates immediate forgetting during local training, and a rapid knowledge recovery strategy that restores degraded models after long-term cumulative drift. We present a theoretical analysis that characterizes heterogeneous forgetting dynamics and establishes the inevitability of long-term degradation. Our experimental results show that this framework achieves up to 8.3\% mIoU improvement over the strongest federated baseline and up to 31.7\% over conventional fine-tuning. We also deploy the FCL framework on a real-world rover testbed to assess system-level robustness under realistic constraints; the testing results further confirm the effectiveness of our FCL design.

---


### 197. [Amodal SAM: A Unified Amodal Segmentation Framework with Generalization](https://arxiv.org/abs/2604.20748)

**<font color=#1a73e8>作者：</font>** Bo Zhang, Zhuotao Tian, Xin Tao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Amodal segmentation is a challenging task that aims to predict the complete geometric shape of objects, including their occluded regions. Although existing methods primarily focus on amodal segmentation within the training domain, these approaches often lack the generalization capacity to extend effectively to novel object categories and unseen contexts. This paper introduces Amodal SAM, a unified framework that leverages SAM (Segment Anything Model) for both amodal image and amodal video segmentation. Amodal SAM preserves the powerful generalization ability of SAM while extending its inherent capabilities to the amodal segmentation task. The improvements lie in three aspects: (1) a lightweight Spatial Completion Adapter that enables occluded region reconstruction, (2) a Target-Aware Occlusion Synthesis (TAOS) pipeline that addresses the scarcity of amodal annotations by generating diverse synthetic training data, and (3) novel learning objectives that enforce regional consistency and topological regularization. Extensive experiments demonstrate that Amodal SAM achieves state-of-the-art performance on standard benchmarks, while simultaneously exhibiting robust generalization to novel scenarios. We anticipate that this research will advance the field toward practical amodal segmentation systems capable of operating effectively in unconstrained real-world environments.

---


### 198. [Autark: A Serverless Toolkit for Prototyping Urban Visual Analytics Systems](https://arxiv.org/abs/2604.20759)

**<font color=#1a73e8>作者：</font>** Lucas Alexandre, João Rulff, Talisson Souza 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The development of visual analytics (VA) systems has traditionally been a labor-intensive process, balancing design methodologies with complex software engineering practices. In domain-specific fields like urban VA, this challenge is amplified by heterogeneous data streams and a reliance on complex, multi-service architectures that hinder fast development, deployment, and reproducibility. Despite the richness of the urban VA literature, the field lacks a consolidated toolkit that encapsulates the core components of these systems, such as spatial data management, analytical processing, and visualization, into a unified, lightweight framework. In this paper, we introduce Autark, a serverless toolkit designed for the rapid prototyping of urban VA systems. Autark provides domain-aware abstractions through a self-contained architecture, enabling researchers to transition from design intention to deployed, shareable systems within hours. Furthermore, Autark's structured, tightly scoped interfaces make it well-suited for AI-assisted coding workflows, where LLMs produce more reliable code when composing from well-defined abstractions rather than generating complex solutions from scratch. Our contributions are: (1) the Autark toolkit, a serverless architecture for rapid prototyping of urban VA; (2) a comparative study of LLM coding effectiveness with and without Autark; and (3) a series of usage scenarios demonstrating its capability to streamline the creation of robust, shareable urban VA prototypes. Autark is available at this https URL.

---


### 199. [Exploring High-Order Self-Similarity for Video Understanding](https://arxiv.org/abs/2604.20760)

**<font color=#1a73e8>作者：</font>** Manjin Kim, Heeseung Kwon, Karteek Alahari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Space-time self-similarity (STSS), which captures visual correspondences across frames, provides an effective way to represent temporal dynamics for video understanding. In this work, we explore higher-order STSS and demonstrate how STSSs at different orders reveal distinct aspects of these dynamics. We then introduce the Multi-Order Self-Similarity (MOSS) module, a lightweight neural module designed to learn and integrate multi-order STSS features. It can be applied to diverse video tasks to enhance motion modeling capabilities while consuming only marginal computational cost and memory usage. Extensive experiments on video action recognition, motion-centric video VQA, and real-world robotic tasks consistently demonstrate substantial improvements, validating the broad applicability of MOSS as a general temporal modeling module. The source code and checkpoints will be publicly available.

---


### 200. [CVEs With a CVSS Score Greater Than or Equal to 9](https://arxiv.org/abs/2604.20765)

**<font color=#1a73e8>作者：</font>** Lena Sinterhauf, Andreas Aßmuth, Roland Kaltefleiter  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Critical vulnerabilities with Common Vulnerability Scoring System scores of 9.0 or higher pose severe risks to organisations' information systems. Timely detection and remediation are essential to minimise economic and reputational damage from cyberattacks. This paper provides a thorough analysis of the identification and resolution timelines of such critical vulnerabilities. A mixed-methods approach is employed, integrating quantitative data from global vulnerability databases analysing 245,456 Common Vulnerabilities and Exposures records spanning from 2009 to 2024, of which 12.8 % were critical, with qualitative case studies of notable incidents. This methodical combination of quantitative and qualitative data sources enables the identification of patterns and delay factors in vulnerability management. The findings indicate significant delays in public disclosure and patch deployment, influenced by industry-specific factors, resource availability and organisational processes. The paper concludes with a series of actionable recommendations to improve the efficiency of vulnerability responses. Despite faster disclosure, the remediation gap for critical vulnerabilities remains a systemic risk, driven by organisational inertia and system complexity.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-220](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
