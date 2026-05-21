# 📦 其他研究 | 2026年05月22日

> 本类共 **352** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-352](./part-08.md)

---

### 1. [Neural Estimation of Pairwise Mutual Information in Masked Discrete Sequence Models](https://arxiv.org/abs/2605.20187)

**<font color=#1a73e8>作者：</font>** Jai Sharma, Yifan Wang, Bryan Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding dependencies between variables is critical for interpretability and efficient generation in masked diffusion models (MDMs), yet these models primarily expose marginal conditional distributions and do not explicitly represent inter-variable dependence. We propose a neural framework for estimating pairwise conditional mutual information (MI) directly from the hidden states of a pretrained MDM, using ground-truth MI computed from the model's own conditional distributions for supervision. The resulting estimator captures the model's internal belief about dependency structure and predicts the full MI matrix in a single forward pass, enabling MI-guided parallel decoding by identifying conditionally independent subsets of variables. We evaluate our approach on Sudoku and protein sequence generation with ESM-C, where the MI maps recover known structural constraints and enable a 3-5x magnitude reduction in inference-time forward passes compared to sequential decoding, while preserving generative quality and outperforming entropy-based parallelization methods.

---


### 2. [GraphDiffMed: Knowledge-Constrained Differential Attention with Pharmacological Graph Priors for Medication Recommendation](https://arxiv.org/abs/2605.20188)

**<font color=#1a73e8>作者：</font>** Krati Saxena, Tomohiro Shibata  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recommending safe and effective medication combinations from electronic health records (EHRs) is a core clinical AI problem, yet it remains difficult because patient trajectories are long, noisy, and clinically heterogeneous. Existing methods typically excel at either temporal modeling across visits or pharmacological knowledge integration (e.g., drug-drug interactions, DDIs), but rarely achieve both while robustly suppressing noise. We present GraphDiffMed, a knowledge-constrained medication recommendation framework built on dual-scale Differential Attention v2. Differential attention is applied at both intra-visit and inter-visit levels to filter spurious signals within encounters and across longitudinal history, while pharmacological constraints are incorporated during learning. Experiments on MIMIC-III and ablation studies show that this design consistently improves recommendation quality and ranking over strong baselines while achieving a more favorable safety performance balance. We further find that the strongest-performing configuration uses only demographic auxiliary features under our experimental setting. Overall, GraphDiffMed demonstrates that combining noise-aware attention with pharmacological constraints yields more reliable and clinically meaningful medication recommendation. We open-source our code at this https URL.

---


### 3. [Tool-Augmented Agent for Closed-loop Optimization,Simulation,and Modeling Orchestration](https://arxiv.org/abs/2605.20190)

**<font color=#1a73e8>作者：</font>** Liyuan Deng, Shujian Deng, Yongkang Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Iterative industrial design-simulation optimization is bottlenecked by the CAD-CAE semantic gap: translating simulation feedback into valid geometric edits under diverse, coupled constraints. To fill this gap, we propose COSMO-Agent (Closed-loop Optimization, Simulation, and Modeling Orchestration), a tool-augmented reinforcement learning (RL) framework that teaches LLMs to complete the closed-loop CAD-CAE process. Specifically, we cast CAD generation, CAE solving, result parsing, and geometry revision as an interactive RL environment, where an LLM learns to orchestrate external tools and revise parametric geometries until constraints are satisfied. To make this learning stable and industrially usable, we design a multi-constraint reward that jointly encourages feasibility, toolchain robustness, and structured output validity. In addition, we contribute an industry-aligned dataset that covers 25 component categories with executable CAD-CAE tasks to support realistic training and evaluation. Experiments show that COSMO-Agent training substantially improves small open-source LLMs for constraint-driven design, exceeding large open-source and strong closed-source models in feasibility, efficiency, and stability.

---


### 4. [Pseudo-Siamese Network for Planning in Target-Oriented Proactive Dialogues](https://arxiv.org/abs/2605.20195)

**<font color=#1a73e8>作者：</font>** Xinyue Kang, Maodong Li, Yibin Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A target-oriented proactive dialogue system is designed to steer conversations toward predefined targets while actively providing suggestions. The core paradigm of such a system is to plan a reasonable dialogue path and subsequently guide language models (e.g., pre-trained or large language models) to generate responses, where dialogue path planning serves as the central component-a novel yet under-explored problem. In this work, we propose a Forward-Focused Bidirectional Pseudo-Siamese Network (FF-BPSN) for dialogue path planning toward predefined dialogue targets. FF-BPSN employs two identical transformer-based decoders for forward and backward planning, together with a forward-focused module that integrates bidirectional information to construct the final forward path. This path benefits from bidirectional planning while prioritizing forward information. We then employ the planned path to guide language models in response generation. Extensive experiments on DuRecDial and DuRecDial 2.0 demonstrate that FF-BPSN achieves state-of-the-art performance in dialogue path planning and significantly enhances the effectiveness of target-oriented proactive dialogue systems.

---


### 5. [Augmented Analytics and Decision Quality: The Role of Trust among Non-Technical BI Users](https://arxiv.org/abs/2605.20198)

**<font color=#1a73e8>作者：</font>** Thuy Pham Thi Phuong, Ha Nguyen Manh, Ngan Nguyen Thi Thuy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Augmented analytics has transformed how business intelligence (BI) systems support managerial decision-making. This is especially true for users without technical backgrounds, who increasingly rely on automated insights rather than manual analysis. BI research has previously concentrated on system adoption and user intention, with very little research examining the impact of AI-enabled analytics on decision quality and the cognitive mechanisms in between. Using the theory of cognitive delegation, this paper investigates the role of trust in augmented analytics and decision-making quality among non-technical BI users. 250 business professionals completed the survey, and the data were analyzed using partial least squares structural equation modeling (PLS-SEM). The results show that augmented analytics capabilities lead to a significant increase in perceived ease of use, perceived usefulness, and trust in BI systems. In addition, trust and usefulness influence BI adoption and improve decision quality. Furthermore, trust has a direct and positive impact on decision quality, highlighting its importance as an enabler of reliance on AI-generated insights. This study considers augmented analytics as a form of cognitive delegation and expands the scope of BI adoption research to include decision-making outcomes.

---


### 6. [Long-Context Reasoning Through Proxy-Based Chain-of-Thought Tuning](https://arxiv.org/abs/2605.20201)

**<font color=#1a73e8>作者：</font>** Miao Li, Irina Saparina, Alexander Gurung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent large language models support inputs of up to 10 million tokens, yet they perform poorly on long-context tasks that require complex reasoning. Such tasks can be solved using only a subset of the input -- a proxy context -- rather than the full sequence. Despite sharing the same underlying reasoning process, models exhibit a significant performance disparity between proxy and full contexts. To improve long-context reasoning, we propose ProxyCoT, a novel training framework that transfers reasoning capabilities from short proxy contexts to full long contexts. Specifically, we first obtain high-quality chain-of-thought reasoning traces on proxy contexts through reinforcement learning or distillation from a larger teacher model, and then ground the generated traces in full long contexts with supervised fine-tuning. Experiments across different datasets demonstrate that ProxyCoT consistently outperforms strong baselines with reduced computational overhead. Furthermore, models trained with ProxyCoT generalize their long-context reasoning capabilities to out-of-domain tasks.

---


### 7. [GrandGuard: Taxonomy, Benchmark, and Safeguards for Elderly-Chatbot Interaction Safety](https://arxiv.org/abs/2605.20203)

**<font color=#1a73e8>作者：</font>** Changxuan Fan, Xi Yang, Yueyuan Zheng 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As older adults increasingly use LLM-based chatbots for companionship and assistance, a safety gap is emerging. Older adults may face vulnerabilities from social isolation, limited digital literacy, and cognitive decline, yet existing safety benchmarks largely target general harms and overlook elderly-specific risks. For example, a prompt such as "how to repair a ceiling light alone in the dark" may be benign for most users but poses a serious fall risk for older adults with mobility limitations. We introduce GrandGuard, the first comprehensive framework for assessing and mitigating elderly-specific contextual risks in LLM interactions. We develop a three-level taxonomy with 50 fine-grained risk types across mental well-being, financial, medical, toxicity, and privacy domains, grounded in real-world incidents, community discussions, and analysis of stakeholder studies. Using this taxonomy, we construct a benchmark of 10,404 labeled prompts and responses, showing that several leading LLMs mishandle elderly-specific contextual risks in over 50% of cases. We mitigate these failures with two safeguards: a fine-tuned Llama-Guard-3 and a policy-enhanced gpt-oss-safeguard-20b, achieving up to 96.2% and 90.9% unsafe-prompt detection accuracy, respectively. GrandGuard lays the groundwork for AI systems that move beyond general safety to support aging populations.

---


### 8. [RealUserSim: Bridging the Reality Gap in Agent Benchmarking via Grounded User Simulation](https://arxiv.org/abs/2605.20204)

**<font color=#1a73e8>作者：</font>** Ming Zhu, Juntao Tan, Rithesh Murthy 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> LLM-based user simulation is the primary mechanism for end-to-end agent evaluation, yet simulated users are poor proxies for real humans: unconstrained LLM defaults produce a Formalism Ceiling (style match rates of 6-8% against real users), while hand-crafted behavioral directives trigger Directive Amplification, where models hyper-interpret instructions into unnatural behavioral extremes that vary dramatically across simulator models. We present RealUserSim, the first user simulation framework grounded in real behavioral data. From 14,000+ authentic human-LLM conversations (WildChat), we extract 7,275 executable behavioral profiles and use them to ground LLM simulators. A fidelity benchmark (PT3) on 600 conversations across 71+ domains with anti-leakage controls shows that grounded simulation raises match rate from 24.2% to 45.3% across five behavioral dimensions. Agent evaluation on TauBench with 6 simulator models and extensive analysis shows that grounded simulation acts as a realistic stress test, surfacing three failure mechanisms invisible to cooperative simulators (mean -3.2% to -3.5% task success degradation), while Directive Amplification in existing benchmarks produces unrealistic behavior that compromises the validity of agent evaluation.

---


### 9. [Challenges in Working Towards Patient Engagement in Developing Technology Prototypes](https://arxiv.org/abs/2605.20205)

**<font color=#1a73e8>作者：</font>** Fateme Rajabiyazdi, Julie Babione, Doreen M. Rabi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Creating supportive technologies for people living with multiple chronic conditions is extremely challenging. These patients are often faced with substantial visible and invisible treatment work as well as their everyday responsibilities, including coordinating across providers, tracking information, and repeating communication in emotionally charged contexts. In the Cumulative Complexity Model (CuCoM), the balance between patient workload and patient capacity shapes what patients can realistically take on, including whether a digital tool can be adopted and sustained. In this paper, we report engagement lessons from implementing MyCareCompass, a patient-facing digital health intervention (DHI) intended to support day-to-day self-management for people living with multiple chronic conditions. We define engagement as patient uptake and sustained use during a two-month pilot study of our platform, drawing on usage analytics and follow-up feedback, and distill three implementation lessons for designing for engagement in complex chronic care.

---


### 10. [HealthTale: A Patient-Centric Health Story Visualization Tool](https://arxiv.org/abs/2605.20207)

**<font color=#1a73e8>作者：</font>** Ryan Smith, Kyle D. Chin, Tamara Munzner  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Patients often struggle to communicate coherent accounts of their health histories during time-constrained clinical encounters. These accounts, which we refer to as health stories, include both clinical events and lived experiences. Existing systems prioritize structured, clinician-centered data and provide limited support for eliciting and communicating patient-generated narratives. We present HealthTale, a patient-centric visualization system designed to elicit health stories from patients and structure them to facilitate communication during initial clinical conversations. Its design arises from a multi-stage qualitative investigation across domain expert discussions, online narratives (n=20), patient (n=11) and clinician (n=6) interviews, and elicited health stories (n=22), identifying recurring patterns in how individuals construct and communicate their health stories. HealthTale transforms freeform narratives into structured timeline representations, grounded in a data abstraction that models health stories as events that are grouped by health concern and time, capturing both clinical and contextual information, with the flexibility to handle temporally imprecise data and non-linear distributions of events across time. Through evaluation with patients (n=34) and clinicians (n=3), we find that HealthTale supports recall, organization, and self-advocacy, while enabling clinicians to rapidly interpret patient-generated narratives and establish a shared understanding.

---


### 11. [Artificial Pancreas Implantables -- How Healthcare Professionals May Deal With DIY Bio Cases](https://arxiv.org/abs/2605.20208)

**<font color=#1a73e8>作者：</font>** Austin James, Xavier-Lewis Palmer, Lucas Potter 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Automated insulin delivery (AID) and artificial pancreas systems increasingly serve as safety-critical cyber-physical technologies in clinical care, integrating sensors, algorithms, software, and insulin-delivery hardware to automate a life-sustaining therapy. While regulated commercial systems are supported by formal approval pathways, manufacturer governance, and post-market surveillance, clinicians are also encountering patients who rely on do-it-yourself (DIY) artificial pancreas systems that operate outside conventional regulatory and institutional control structures. This paper examines how routine clinical handling practices intersect with cyberbiosecurity risk across both regulated and DIY AID systems. When insulin delivery systems are fundamentally reconfigured into a bespoke AID system, with the patient-user becoming the primary threat vector by assuming manufacturer-level roles without mandated governance, the entire ecosystem of stakeholders is placed in legal and clinical uncertainty.

---


### 12. [Why Latent Actions Fail, and How to Prevent It](https://arxiv.org/abs/2605.20223)

**<font color=#1a73e8>作者：</font>** Jung Min Lee, Taehyun Cho, Li Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent action models (LAMs) aim to learn action-like representations from unlabeled videos by compressing frame-to-frame changes. The frames of in-the-wild videos, however, contain not only the agent's own state but exogenous state such as background clutter. Since the exogenous state introduces changes unrelated to actions, it hinders reliable latent action learning. This paper investigates this problem analytically by extending a linear LAM framework to explicitly model exogenous state. Our analysis reveals two insights: (1) minimizing the standard reconstruction objective produces latent actions that encode exogenous information from future observation; and (2) learning in a representation space that focuses on endogenous components is a key to mitigating the interference of noise. We further show that previously proposed auxiliary objectives, such as action-supervision, provably encourage latent actions to be consistent across exogenous states. These findings are validated through experiments on both linear and nonlinear LAMs, providing a unified theoretical analysis of how exogenous state hinders latent action learning and why common remedies work.

---


### 13. [AI-Assisted Competency Assessment from Egocentric Video in Simulation-Based Nursing Education](https://arxiv.org/abs/2605.20233)

**<font color=#1a73e8>作者：</font>** Hanchen David Wang, Yilin Liu, Madison J. Lee 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Assessing learner competency in clinical simulation requires expert observation that is time-intensive, difficult to scale, and subject to inter-rater variability. Vision-language models have emerged as a promising tool for understanding complex visual behavior. In this work, we investigate whether visual observations can provide educationally meaningful signals for competency assessment through a three-stage framework that (1) extracts action timelines from egocentric nursing simulation video using frozen visual encoders and few-shot learning, (2) derives sequence-level features and per-session recognition metrics, and (3) relates these to instructor-rated competency. Across 22 densely annotated sessions (3.8 hours, 493 actions), a frozen DINOv2 backbone with HMM Viterbi decoding achieves 57.4% MOF in leave-one-out 1-shot recognition. Surprisingly, we observe a negative trend between recognition accuracy and competency (rho = -0.524, p = 0.012 for mIoU), robust to six confound controls: more competent students produce diverse, harder-to-classify workflows, while simple sequence features show no such relationship. Per-item analysis identifies patient safety protocols and team communication as the expected behaviors most reflected in this pattern, and process model comparisons reveal that higher-competency students exhibit more protocol-consistent action transitions. These findings suggest that recognition accuracy may complement predicted action timelines as a pedagogically informative signal in automated competency assessment.

---


### 14. [TabPFN-MT: A Natively Multitask In-Context Learner for Tabular Data](https://arxiv.org/abs/2605.20234)

**<font color=#1a73e8>作者：</font>** Cormac Cureton, Narges Armanfard  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prior-Data Fitted networks (PFNs) have been very successful in tabular contexts, handling prediction tasks in context. However, they are designed for single-task inference, meaning that predicting several target values within a context requires repeated forward calls and precludes inter-task information sharing. We propose TabPFN-MT, which is trained on an expanded multi-target synthetic prior to capture inter-task dependencies in context. This model uses an expanded $y$-encoder and a shared decoder head to enable multitask in-context learning and simultaneous inference. The model is uniquely specialized for small-to-medium datasets by relying on in-context learning rather than traditional gradient-based training. Within this regime (averaging fewer than 1,000 samples), extensive evaluations across 344 datasets demonstrate that TabPFN-MT establishes a new state-of-the-art for deep tabular multitask learning. Furthermore, despite the inherent compute asymmetry of joint optimization, our model remains highly competitive with the latest state-of-the-art single-task ensembles. Notably, on multitask datasets it achieves an overall Accuracy rank of 4.89, the highest average rank among all models tested. Crucially, TabPFN-MT delivers this highly competitive performance while reducing the inference cost for $T$ tasks from $O(T)$ to $O(1)$ forward passes, offering a massive computational efficiency improvement for multi-target tabular applications.

---


### 15. [Provably Learning Diffusion Models under the Manifold Hypothesis: Collapse and Refine](https://arxiv.org/abs/2605.20235)

**<font color=#1a73e8>作者：</font>** Wei Huang, Andi Han, Mingyuan Bai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models generate high-dimensional data with remarkable quality, yet how their training efficiently learns the score function, bypassing the curse of dimensionality when data is supported on low-dimensional manifolds, remains theoretically unexplained. We identify a collapse-and-refine mechanism driven by the geometry of the score function itself: at small noise scales, the diverging singularity of the score drives a rapid dimensional collapse of the induced denoising map onto the data manifold projection; at moderate noise scales, training refines the intrinsic density on the learned manifold. We instantiate this principle as Score-induced Latent Diffusion (SiLD), a two-stage framework in which both manifold learning and density estimation emerge from a single denoising score matching objective, replacing the heuristic KL regularization of VAE-based latent diffusion models. We prove that the resulting sample complexity depends on the intrinsic dimension rather than the ambient dimension. Experiments on Stacked MNIST, CelebA variants, and molecular generation benchmarks show that SiLD matches or outperforms VAE-based LDMs in generation quality and consistently improves reconstruction, validating our theoretical predictions.

---


### 16. [AnimeAdapter: Fine-grained and Consistent Zero-shot Anime Character Generation](https://arxiv.org/abs/2605.20237)

**<font color=#1a73e8>作者：</font>** Yixuan Han  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a lightweight appearance adapter for Stable Diffusion that enables controllable and consistent anime character generation under diverse editing conditions. Instead of relying on large-scale vision-language models or per-subject fine-tuning, our method injects fine-grained visual features from a single reference image into the diffusion process. Based on CLIP emergent local spatialization, we develop semantic-selective local attention. To further disentangle character appearance from spatial layout, we incorporate pose-aware conditioning during adapter training. The resulting pretrained adapter remains compact, modular, and fully compatible with Stable Diffusion community workflows, while requiring no additional fine-tuning at deployment time. Furthermore, we present a high-quality anime character dataset based on curated and restructured Danbooru prompts, and evaluate our method across several practical character editing scenarios. Our code, model weights, and dataset will be publicly released upon acceptance.

---


### 17. [MagBridge-Battery: A Synthetic Bridge Dataset for Li-ion Magnetometry and State-of-Health Diagnostics](https://arxiv.org/abs/2605.20240)

**<font color=#1a73e8>作者：</font>** Sakthi Prabhu Gunasekar, Prasanna Kumar Rangarajan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Battery health diagnostics today rely overwhelmingly on electrochemical signals measured at the cell terminals. A parallel literature has shown that magnetic sensing can resolve information that terminal-only measurements miss, but method development is limited by the absence, to the best of our knowledge, of public battery magnetic-measurement datasets paired with degradation labels. We release MagBridge-Battery v1.0, a synthetic dataset of 6,760 magnetic-field signatures that bridges real magnetic morphology from the Mohammadi-Jerschow Open Science Framework (OSF) archive with state-of-health (SOH) labels from the PulseBat dataset. The release contains 5,600 PulseBat-conditioned grounded samples, 600 synthetic sensor-anomaly samples derived from clean parents, and 560 low-voltage Regime-B extrapolation samples. A cell-disjoint, parent-child-leakage-free primary benchmark split is verified to contain zero overlapping cells, zero cross-split parent-child pairs, and zero sample-ID overlap. We define three primary benchmark tasks: SOH regression, second-life classification, and anomaly detection, plus an auxiliary anomaly-subtype classification task. A controlled label-shuffle ablation collapses SOH regression from R^2 approximately 0.77 to approximately 0, confirming that the bridge encodes input SOH non-trivially rather than producing label-aligned artifacts. The dataset is released on Zenodo under CC-BY-4.0, and the bridge code and benchmark suite are released under Apache-2.0. This work provides a public benchmark for magnetic-sensing battery diagnostics while paired magnetic-electrochemical measurements remain scarce.

---


### 18. [Geometry-Lite: Interpretable Safety Probing via Layer-Wise Margin Geometry](https://arxiv.org/abs/2605.20241)

**<font color=#1a73e8>作者：</font>** Woo Seob Sim, Yu Rang Park  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prompt-level safety probes for large language models use hidden-state representations to separate safe from unsafe prompts, but strong average detection performance does not explain the geometry of this separation. In particular, it remains unclear how safety evidence is formed across layers, which aspects of that layer-wise geometry support low-false-positive decisions, and which geometric biases remain stable under benchmark shift. We study this as an empirical decomposition problem and introduce Geometry-Lite, a compact prompt-level probe that maps each layer's final prompt-token representation to signed margins under centroid, local-neighborhood, and supervised linear-boundary readouts, then summarizes the resulting margin profiles by boundary position, layer-to-layer change, and coarse shape. Across nine instruction-tuned backbones ($1.2$B--$70$B) and seven safety benchmarks, Geometry-Lite improves over single-layer probes while remaining close to raw multi-layer score stacking, making it a useful instrument for analyzing the multi-layer safety signal. The decomposition shows that safety evidence is expressed primarily through persistent boundary-position geometry: final or extremal margins and unsafe-side layer occupancy dominate aggregate detection performance. In contrast, finite-difference drift and structural summaries add little to pooled AUROC, although drift can provide small recall-oriented corrections under shifted low-FPR thresholds. Under benchmark shift, optimized linear boundaries are sharp on the training mixture, whereas class-conditional mean geometry retains separation more reliably on a predefined hard held-out subset. Overall, prompt-level safety evidence is not primarily a layer-to-layer motion signal, but a persistent layer-wise margin geometry whose useful components and readout-level biases become visible in decision-critical regimes.

---


### 19. [Automated Kernel Discovery Towards Understanding High-dimensional Bayesian Optimization](https://arxiv.org/abs/2605.20249)

**<font color=#1a73e8>作者：</font>** Taeyoung Yun, Woocheol Shin, Inhyuck Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gaussian Process (GP) kernels are central to Bayesian optimization (BO), yet designing effective kernels for high-dimensional problems still relies on extensive manual engineering. Existing automated approaches struggle in high dimensions for two bottlenecks: their kernel search space is limited to additions and multiplications of base kernels, and LLM-based approaches require conditioning on raw observations, which becomes infeasible due to context-length limits and the difficulty of extracting meaningful patterns. We introduce \textbf{Kernel Discovery}, a LLM-driven evolutionary framework for high-dimensional BO that searches a broader kernel space beyond predefined composition rules and does not require conditioning on observations. Motivated by the observation that directly prompting an LLM to generate kernel code yields syntactically varied but functionally identical kernels, we adopt a two-stage approach: an LLM first proposes novel mathematical forms, then a second LLM call converts each form into validated, executable code. We also propose a leave-one-out continuous ranked probability score (LOO-CRPS) as a selection criterion that penalizes overfitted kernels. On five high-dimensional BO benchmarks, our method achieves an average rank of \textbf{1.2 out of 17}, outperforming competitive baselines.
We further analyze the discovered kernels to identify which kernels lead to improvements in high-dimensional BO.

---


### 20. [Physics-informed convolutional neural networks for fluid flow through porous media](https://arxiv.org/abs/2605.20250)

**<font color=#1a73e8>作者：</font>** Rafał Topolnicki, Paweł Dłotko, Maciej Matyka  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate simulation of fluid flow in porous media is challenging due to complex pore-space geometries and the computational cost of solving the Navier-Stokes equations. This difficulty is particularly important when repeated simulations are required, as standard numerical solvers may converge slowly in intricate porous domains. We present a neural-network-based framework for predicting pore-scale velocity fields directly from sample geometry. The method uses a convolutional encoder-decoder architecture with skip connections to preserve spatial detail while extracting multi-scale features. Physical consistency is encouraged through a custom loss function combining velocity reconstruction with incompressibility, no-flow conditions inside solids, periodicity constraints, and agreement with the global tortuosity index. We analyze the influence of the corresponding loss weights and quantify the contribution of individual loss components to prediction accuracy. Several CNN backbones are evaluated to identify architectures providing accurate and robust predictions. The generalization ability of the trained model is tested on samples outside the training distribution, including changes in obstacle geometry, boundary conditions, porosity, and realistic porous structures. Finally, we demonstrate a practical use of the predicted velocity fields as initial conditions for Lattice-Boltzmann simulations. This warm-start strategy accelerates solver convergence, reducing the number of iterations in over 90% of tested cases.

---


### 21. [Multi-Agent Reinforcement Learning for Safe Autonomous Driving Under Pedestrian Behavioral Uncertainty](https://arxiv.org/abs/2605.20255)

**<font color=#1a73e8>作者：</font>** Prakash Aryan, Kaushik Raghupathruni, Timo Kehrer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Simulation-based testing of self-driving cars (SDCs) typically relies on scripted or simplified pedestrian models that do not capture the heterogeneity and uncertainty of real human crossing behavior. This limits the realism of safety assessments, especially in scenarios involving jaywalking, which is governed by latent personality traits that the vehicle cannot observe. We hypothesize that jointly training pedestrians and the SDC with multi-agent reinforcement learning (MARL) produces more realistic interaction scenarios than training the SDC against fixed pedestrian policies, and that the resulting behavior gap between predictable and unpredictable crossings can be measured directly from trajectories. This paper describes a MARL environment in which an SDC and 12 pedestrians are co-trained using Multi-Agent Proximal Policy Optimization (MAPPO). Pedestrian locomotion follows scripted Dijkstra pathfinding, while an RL policy controls high-level go/wait decisions. Jaywalking probability depends on a per-pedestrian personality trait sampled at episode start and hidden from the SDC. In 500-episode evaluations, the co-trained SDC reached 78% of goals with a 14% collision rate, compared to 35% goals and 33% collisions for the best rule-based baseline. A speed differential metric shows that the SDC traveled 2.65 m/s faster near jaywalkers than near crosswalk users at close range (0-3 m), indicating that jaywalking encounters were not anticipated. Jaywalking accounted for 13% of crossing events but was associated with 62% of collisions. Co-training with MARL pedestrians reduced collisions by 30% relative to single-agent RL, as pedestrians learned to wait when the SDC approached at speed.

---


### 22. [FBOS-RL: Feedback-Driven Bi-Objective Synergistic Reinforcement Learning](https://arxiv.org/abs/2605.20256)

**<font color=#1a73e8>作者：</font>** Xikai Zhang, Yongzhi Li, Likang Xiao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has become a cornerstone for aligning and unlocking the reasoning capabilities of large-scale models. At its core, the training loop of GRPO and its variants alternates between rollout sampling and policy update. Unlike supervised learning, where each gradient step is anchored to an explicit ground-truth target, the optimal gradient direction for updating model parameters in this setting is not known a priori; the high-quality rollouts drawn during the sampling stage therefore act as the implicit "teacher" that guides every parameter update. However, GRPO adopt a simple sampling scheme that conditions all rollouts on the same original prompt. When a task lies beyond the policy model's current capability, this sampling scheme rarely yields a high-quality rollout, leaving the policy model without a meaningful gradient direction when updating its parameters, which causes training to stall. To address this issue, we propose FBOS-RL, a Feedback-Driven Bi-Objective Synergistic reinforcement learning framework. Specifically, we let the model perform Feedback-Guided Exploration Enhancement based on the feedback provided by the environment, and on top of this we design two mutually reinforcing training objectives: Exploitation-oriented Policy Alignment(EPA) and Exploration-oriented Capability Cultivation(ECC). Extensive experiments demonstrate that EPA and ECC can mutually reinforce each other, forming a positive flywheel effect that significantly improves both the training efficiency and the final performance ceiling of reinforcement learning. Specifically, under an identical number of rollouts, FBOS-RL learns substantially faster than GRPO and feedback-based baselines and ultimately attains a higher performance ceiling, while exhibiting higher policy entropy and lower gradient norms throughout training.

---


### 23. [Instance Discrimination for Link Prediction](https://arxiv.org/abs/2605.20257)

**<font color=#1a73e8>作者：</font>** Valentin Cuzin-Rambaud, Mathieu Lefort, Rémy Cazabet  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recently, instance discrimination models have emerged as a major solution for self-supervised learning. Having already demonstrated its effectiveness in the image domain, instance discrimination learning is now proving equally convincing in the graph domain, in particular for node classification. However, fewer contributions have tackled the link prediction task. In this contribution, we propose to adapt existing methods to this context. We first provide a rigorous evaluation of existing self-supervised models in the field of link prediction, showing that the main performance depends on the augmentation process (like in computer vision). We then propose a new structural augmentation based on the community structure that is relevant for link prediction. Our main contribution introduces two new models, L-GRACE and L-BGRL, based on link representations instead of node representations, which improve the performance of the existing methods, especially on unattributed graphs, and we show that they perform on par with the state of the art, both in supervised and self-supervised contexts.

---


### 24. [Residual Paving: Diagnosing the Routing Bottleneck in Selective Refusal Editing](https://arxiv.org/abs/2605.20262)

**<font color=#1a73e8>作者：</font>** Bryce Hinkley, Peyman Najafirad  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study selective refusal editing as a three-way control problem: induce non-refusal on designated edit prompts while preserving benign behavior and harmful refusals outside the edit set. We introduce Residual Paving, a routed residual editing method for frozen instruction-tuned transformers that separates route selectivity, whether to intervene, from residual-edit capacity, what edit to apply. An early-layer router predicts a scalar gate and expert mixture; when active, prompt-conditioned bottleneck residual experts apply later-layer residual updates while leaving the backbone unchanged. This decomposition supports an oracle-routing diagnostic where only the learned scalar gate is replaced with the held-out edit/keep label, leaving the residual editor and frozen backbone fixed. On the primary Gemma-3-4B-IT held-out split, learned Residual Paving reduces edit refusal from 88.6% to 4.0%, with 95.5% benign distribution preservation and 87.3% harmful distribution preservation. Same-protocol one-direction steering controls are much weaker on edit success, leaving edit refusal at 86.8% for Edit-target ActAdd and 78.9% for DIM-style refusal steering. The remaining failure is off-target harmful-keep degradation: harmful refusal remains below the frozen-base rate, 65.3% vs. 81.6%. Across six backbones, oracle routing improves the keep-side diagnostic score on every reported row, with median gain +12.9 pp, supporting the interpretation that learned route selectivity is the main observed bottleneck. Trajectory diagnostics on two backbones further suggest directed movement toward edit-target continuations rather than generic refusal suppression.

---


### 25. [Generation of Heterogeneous PET Images from Uniform Organ Activity Maps Using a Pretrained Domain-Adapted Diffusion Model](https://arxiv.org/abs/2605.20267)

**<font color=#1a73e8>作者：</font>** Suya Li, Kaushik Dutta, Debojyoti Pal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic PET images are valuable for quantitative imaging workflow development, scalable virtual imaging trials, and deep learning model training, but conventional physics-based simulation approaches are computationally intensive, limited in anatomical variability, and often fail to capture heterogeneous PET uptake. This study developed a pretrained domain-adapted diffusion (PAD) model for anatomy-conditioned PET synthesis from uniform organ activity maps. PAD adopts a natural-image pretrained text-to-image decoder with an upstream conditioning encoder and a downstream PET-domain adapter. A two-phase training strategy was used, with the first phase learning coarse uptake distributions and the second refining local image details. Uniform organ activity maps were generated from CT-based segmentations by assigning each organ its mean uptake from the paired PET image. Evaluation included quantitative accuracy, noise assessment, radiomic analysis, tumor segmentation performance, and a human observer study. PAD-generated images achieved high quantitative accuracy, with concordance correlation coefficients above 0.92 between organ mean SUVs and assigned activity values. The synthesized images showed noise levels and texture characteristics similar to target PET images and produced comparable tumor segmentation performance. In a two-alternative forced-choice observer study, four readers achieved approximately 50% accuracy, indicating visual indistinguishability between synthesized and target images. PAD also generated realistic PET images from XCAT-derived activity maps, demonstrating compatibility with phantom-based anatomical priors. Overall, PAD provides a diffusion-based framework for generating clinically relevant heterogeneous PET images from uniform organ activity maps derived from clinical segmentations or digital phantoms, supporting data augmentation and downstream imaging studies.

---


### 26. [Catching a Moving Subspace: Low-Rank Bandits Beyond Stationarity](https://arxiv.org/abs/2605.20269)

**<font color=#1a73e8>作者：</font>** Hamed Khosravi, Xiaoming Huo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many bandit deployments (recommendation, clinical dosing, ad targeting) share two facts prior work handles only in isolation: rewards live on a low-dimensional latent subspace, and that subspace drifts. Stationary low-rank bandits exploit rank but break under subspace change; non-stationary linear bandits adapt to drift but pay ambient rate $\widetilde{O}(d\sqrt{T})$. We study piecewise-stationary low-rank linear contextual bandits with scalar feedback: $\theta_t = B_k^\star w_t$ with rank-$r$ factor $B_k^\star\in\mathbb{R}^{d\times r}$ constant within each of $K$ unknown segments and able to shift at boundaries. Our results are tight along three axes. (i) Identification boundary. With single-play scalar rewards, the moving subspace is recoverable through quadratic functionals of rewards iff three probe-side conditions hold: known noise variance, bounded state-noise coupling, and full-dimensional probe support. Each is necessary in the unrestricted-second-moment problem, and jointly they are sufficient, characterizing the boundary of the solvable region. (ii) Algorithm and dynamic regret. SPSC interleaves isotropic probes with windowed projected ridge-UCB exploitation inside the learned $r$-dimensional subspace; a CUSUM-style variant discovers segment boundaries online. The costed dynamic regret is $\widetilde{O}(r\sqrt{T})+\widetilde{O}(T^{2/3})+O(W\,V_{\mathrm{in}})$, replacing the ambient $d\sqrt{T}$ rate with the intrinsic rank. (iii) Empirics. On eleven benchmarks spanning synthetic, UCI/MovieLens, semi-synthetic clinical, and ZOZOTOWN production-log data, SPSC outperforms non-stationary and low-rank baselines whenever $d-r\gtrsim T^{1/6}$, matching the analytical crossover. To our knowledge, this is the first work to characterize the identification boundary and attain the intrinsic-rank dynamic-regret rate in this setting.

---


### 27. [Smaller Abstract State Spaces Enable Cross-Scale Generalization in Reinforcement Learning](https://arxiv.org/abs/2605.20272)

**<font color=#1a73e8>作者：</font>** Nasehatul Mustakim, Lucas Lehnert  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While humans readily generalize abstract concepts to more complex or larger tasks, building Reinforcement Learning (RL) systems with this ability remains elusive. Here, we present the first theoretical model of how such Out-of-Distribution (OOD) generalization can be achieved in RL agents. Our approach considers Partially Observable Markov Decision Processes (POMDPs) and assumes that an intelligent agent uses an abstraction function to determine which experiences can be treated as equivalent and which must be distinguished. First, we extend the existing state abstraction framework and proof techniques to POMDPs. Then, we define a successor-weighted model reduction, a model reduction variant that enables compression into smaller abstract spaces than prior definitions allow. We derive a bound on the agent's OOD test performance, thereby defining the conditions under which OOD generalization is achievable. This bound decomposes an agent's performance loss into approximation and estimation errors, revealing how reducing an agent's abstract state space size improves test performance and OOD generalization. Our analysis suggests that constraining an agent to operate over a small, finite set of abstract states is necessary for achieving generalization to more complex tasks. Our results motivate further research into learning RL architectures that scale across tasks of varying complexity levels.

---


### 28. [You Don't Need Attention: Gated Convolutional Modeling for Watch-Based Fall Detection](https://arxiv.org/abs/2605.20275)

**<font color=#1a73e8>作者：</font>** Sana Alamgeer, Ronish Kumar, Awatif Yasmin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing deep learning approaches for wearable fall detection systems rely on self-attention mechanisms that impose quadratic computational overhead, distributing weights across all time steps. This global weight distribution impairs the precise localization of the brief impact signatures that characterize falls within short, fixed-length windows. To overcome this challenge, we propose Gated-CNN, a lightweight dual-stream architecture that processes accelerometer and gyroscope streams through independent one-dimensional convolutional feature extractors, followed by (i) a sigmoid gating module that selectively suppresses uninformative background activations while amplifying fall-discriminative features, (ii) a global average pooling layer that compresses each stream into a compact fixed-length descriptor, and (iii) a shared classification head that fuses both descriptors for binary fall prediction. For offline evaluation, we evaluate the model across five wrist-mounted inertial measurement unit (IMU) datasets, achieving average F1-scores of 93%, 93%, 90%, 91%, and 90% on SmartFallMM, WEDA-Fall, FallAllD, UMAFall, and UP-Fall, outperforming Transformer baselines. For real-time evaluation, we deployed the model on a Google Pixel Watch 3 and tested across 12 participants. The model achieves an average F1-score of 97% and an accuracy of 98% with zero missed falls, showing that sigmoid gating offers a more structurally aligned and computationally efficient alternative to attention for commodity smartwatch-based fall detection.

---


### 29. [OmniISR: A Unified Framework for Centralized and Federated Learning via Intermediate Supervision and Regularization](https://arxiv.org/abs/2605.20276)

**<font color=#1a73e8>作者：</font>** Wei-Bin Kou, Guangxu Zhu, Ming Tang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The global deployment of edge intelligence operates across heterogeneous legal frameworks. While some regions permit centralized learning (CL) via cloud data aggregation, others enforce strict data localization, necessitating federated learning (FL). This operational dichotomy introduces two incompatible optimization regimes (i.e., unbiased global gradients yet coupled with internal covariate shift in CL versus biased, drift-prone local updates in FL), resulting in that any naive integration of the two lacks rigorous theoretical guarantees. To fill this gap, we propose OmniISR, a unified framework that fuses pure CL, pure FL, and hybrid CL-FL training modes via equipping intermediate supervision and regularization (ISR) signals at multiple hidden layers. Specifically, we propose (i) to use mutual-information (MI) as intermediate supervision to align shifting internal covariate in CL and client-drifting representations in FL, and (ii) to adopt negative-entropy (NE) as intermediate regularizer to penalize overconfident prediction, preserve representational uncertainty, and avoid device-specific collapse. On the theory side, we derive (i) a unified, ISR-agnostic, and non-asymptotic O(1/sqrt(T)) convergence bound that shows the introduced ISR does not violate standard SGD convergence, (ii) a federated drift-bound that quantifies the ISR-reduced client drift, (iii) a gradient-alignment guarantee that ensures non-conflicting CL and FL updates under mild bias, and (iv) an explicit escape-time bound that indicates that CL-FL hybrid mixing enlarges effective stochasticity and accelerates escape from strict saddles. Extensive experiments demonstrate that OmniISR consistently improves model performance in both centralized and federated paradigms, reduces the CL-FL gap by 22.60%, and yields 37/48 paired metric wins across multiple FL algorithms.

---


### 30. [Regulating Anatomy-Aware Rewards via Trajectory-Integral Feedback for Volumetric Computed Tomography Analysis](https://arxiv.org/abs/2605.20277)

**<font color=#1a73e8>作者：</font>** Tianwei Lin, Zhongwei Qiu, Jie Cao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical vision-language models (VLMs) have rapidly advanced as general-purpose multimodal assistants, yet their deployment in 3D Computed Tomography (CT) analysis remains constrained by a persistent mismatch between optimization objectives and clinical rigor. Current Reinforcement Learning (RL) paradigms still rely on lexical proxy signals that induce ``\textit{Evaluation Hallucinations}'', where models optimize linguistic fluency rather than factual clinical correctness, leading to diagnostically critical errors. To bridge this gap, we introduce the \textbf{Clinical Abnormality Benchmarking Substrate (CABS)}, a structured system that decomposes radiology reports into verifiable clinical semantic units. Using CABS, we identify a ``\textit{Mechanistic Divergence}'' in standard RL, where surface-similarity rewards drive policy gradients to bypass medical facts. We therefore propose \textbf{Trajectory-Integral Feedback GRPO (TIF-GRPO)}, a novel framework integrating control-theoretic principles into policy optimization. By formulating clinical reasoning as a pseudo-temporal trajectory for anomaly discovery, TIF-GRPO regulates anatomy-aware rewards via an integral feedback loop that penalizes persistent omissions as cumulative state errors and suppresses hallucinations as excessive control effort. Experiments on 3D CT benchmarks demonstrate that our approach significantly enhances abnormality detection and clinical faithfulness, establishing a new paradigm for fine-grained regulation in medical VLMs. Our project is available at \href{this https URL}{GitHub}.

---


### 31. [ClaimDiff-RL: Fine-Grained Caption Reinforcement Learning through Visual Claim Comparison](https://arxiv.org/abs/2605.20278)

**<font color=#1a73e8>作者：</font>** Tianle Li, Xuyang Shen, Yan Ma 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-form image captioning exposes a reward granularity problem in RL: captions are judged as whole sequences, while the important errors occur at the level of individual visual claims. A good dense caption should be both faithful and informative, avoiding hallucination without omitting salient details. Yet pairwise preferences, reference-based metrics, and holistic scalar rewards compress these local errors into a single sequence-level signal, obscuring the tradeoff between factuality and coverage. We introduce ClaimDiff-RL, a framework that uses reference-conditioned atomic claim differences as the reward unit for caption RL. Given an image, an actor caption, and a reference caption, a multimodal judge enumerates visually grounded differences, verifies each difference against the image, assigns open-vocabulary error types and severity levels, and produces per-difference statistics for reward composition. This makes hallucinated claims and omitted salient facts separately measurable and tunable. Experiments show that holistic scalar rewards can reduce hallucination by increasing missing facts, while ClaimDiff-RL exposes this faithfulness and coverage tradeoff and enables more balanced operating points. On a 160-image human-labeled diagnostic benchmark, public captioning benchmarks, and VQA benchmarks, ClaimDiff-RL improves the hallucination--missing-fact balance, preserves general capability, and even surpasses Gemini-3-Pro-Preview on several fine-grained Capability dimensions such as object counting, spatial relations, and scene recognition. These results suggest that typed, verifiable claim differences are an effective reward unit for fine-grained and diagnosable caption RL.

---


### 32. [FusionCell: Cross-Attentive Fusion of Layout Geometry and Netlist Topology for Standard-Cell Performance Prediction](https://arxiv.org/abs/2605.20287)

**<font color=#1a73e8>作者：</font>** Haoyi Zhang, Kairong Guo, Bojie Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard cells form the building blocks of digital circuits, so their delay and power critically influence chip-level performance; yet characterization still relies on slow simulation sweeps, and many fast predictors ignore layout geometry, missing coupling and layout-dependent effects. The challenge is to jointly represent layout geometry and netlist topology so models capture fine-grained spatial details together with structural connectivity for accurate performance prediction. We introduce FusionCell, a dual-modality predictor that treats routed layout geometry and netlist topology as inputs and fuses them explicitly in a unified model. A DeiT encoder processes three-layer routed layouts, while a graph transformer models heterogeneous device/net graphs. The modalities are integrated through a topology-guided mechanism, where the netlist acts as a structural "map" to actively query relevant physical regions in the layout for joint geometric and topological reasoning. We build a 7nm dataset based on the ASAP7 PDK with over 19.5k cells spanning 149 types using automatic tools, targeting six metrics: signal rise/fall delay, transition, and power. Experimental results demonstrate that FusionCell reduces regression error, with an average MAPE of 0.92 percent, and improves Spearman/Kendall ranking over baselines, while accelerating the characterization process by orders of magnitude compared to circuit simulation.

---


### 33. [TreeText-CTS: Compact, Source-Traceable Tree-Path Evidence for Irregular Clinical Time-Series Prediction](https://arxiv.org/abs/2605.20292)

**<font color=#1a73e8>作者：</font>** Kwanhyung Lee, Juhwan Choi, Jongheon Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Numerical time-series models can effectively process irregular electronic health record (EHR) trajectories, but they do not naturally expose the measurements and temporal patterns supporting each risk estimate as readable evidence. Existing text-based interfaces improve readability, but typically rely on either raw serialization, which is lengthy and redundant, or patient-level free-form summaries, which are difficult to trace to source measurements and time windows. To bridge this gap, we introduce TreeText-CTS (Clinical Time-Series), which converts irregular EHR trajectories into human-readable, compact, source-traceable tree-path evidence units without patient-level summarization or inference-time autoregressive decoding. TreeText-CTS routes multi-scale window summaries through frozen XGBoost models and verbalizes activated tree paths as deterministic, source-traceable evidence units composed of threshold conditions. An evidence selector assembles an informative subset of these units, which a language-model encoder then integrates for prediction. Across PhysioNet 2012 mortality, MIMIC-III mortality, and PhysioNet 2019 sepsis-onset forecasting, TreeText-CTS achieves the best AUROC and AUPRC among evaluated text-based EHR time-series interfaces, improving AUPRC by 6.0 to 9.7 absolute percentage points over the strongest prior text-based interface while remaining competitive with numerical time-series models. Ablations show that tree-path evidence construction, evidence selection, and language-model composition each contribute to performance. Because every span passed to the language-model encoder is constructed from activated tree-path threshold conditions, TreeText-CTS makes the evidence supplied to the final predictor inspectable and source-traceable.

---


### 34. [Closed-form predictive coding via hierarchical Gaussian filters](https://arxiv.org/abs/2605.20293)

**<font color=#1a73e8>作者：</font>** Aleksandrs Baskakovs, Sylvain Estebe, Kenneth Enevoldsen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive coding (PC) offers a local and biologically grounded alternative to backpropagation in the training of artificial neural networks, yet to date, it remains slower, and performance degrades sharply as network depth increases. We trace both problems to a single simplification: current PC networks fix the precision matrix to the identity, discarding precision-weighted prediction errors that the variational derivation requires to be fast, local, and Bayesian. We close this gap by expressing predictive coding networks as deep hierarchical Gaussian filters (HGFs) and restore precision-weighted message passing, yielding dynamic uncertainty estimates and Hebbian-compatible update rules at every layer. The resulting networks can simultaneously learn activations, weights, and precisions under a single free-energy objective, with no global error signal, and resolve inference without requiring iterations or automatic differentiation. On FashionMNIST, our solution approaches backpropagation in epoch-level wall-clock cost while converging in fewer epochs, and outperforms it on online, data efficiency, and concept-drift tasks. We thus establish that closed-form variational inference with online precision learning provides a tractable foundation for deep predictive coding networks, retaining biological and interpretative advantages, without requiring iterative relaxation or global error signals.

---


### 35. [MedCRP-CL: Continual Medical Image Segmentation via Bayesian Nonparametric Semantic Modality Discovery](https://arxiv.org/abs/2605.20297)

**<font color=#1a73e8>作者：</font>** Ziyuan Gao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image segmentation faces a fundamental challenge in continual learning: data arrives sequentially from heterogeneous sources, yet effective continual learning requires discovering which tasks share sufficient structure to benefit from joint learning. Existing methods either apply uniform constraints across all tasks, causing catastrophic forgetting when tasks conflict, or require predefined task groupings that cannot anticipate future task diversity. We introduce MedCRP-CL, a framework that performs online task structure discovery and structure-aware continual learning. Leveraging the Chinese Restaurant Process (CRP), our method dynamically infers task groupings from clinical text prompts as tasks arrive, without requiring predefined cluster counts or access to future tasks. We term these discovered groupings semantic modalities, as they capture finer-grained structure than physical imaging modalities by integrating anatomical region and pathological context. Guided by this discovered structure, we maintain semantic modality-specific LoRA adapters regularized by intra-modality EWC, ensuring parameter isolation across dissimilar task groups while facilitating knowledge transfer within similar ones. The framework is also replay-free, storing only aggregate statistics rather than raw patient data. Experiments on 16 medical segmentation tasks across four imaging modalities demonstrate that MedCRP-CL achieves 73.3% Dice score with only 4.1% forgetting, outperforming the best baseline by 8.0% while requiring 6$\times$ fewer parameters. Code is available at this https URL.

---


### 36. [Mechanisms of Misgeneralization in Physical Sequence Modeling](https://arxiv.org/abs/2605.20299)

**<font color=#1a73e8>作者：</font>** Kento Nishi, Raphael Tang, Karun Kumar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative sequence models are often trained to plan motion in physical domains, from robotics to mechanical simulations. When constructing a dataset to train such a model, engineers may curate demonstrations to specify how trajectories should be distributed over a physical quantity like travel distance or mechanical energy. For example, a roboticist building a maze navigation agent might choose demonstrations whose travel distances cover a fixed range uniformly, hoping to constrain the agent's expected power usage. We find that standard deep learning can violate this intent: each generated trajectory can seem plausible on its own, but the aggregate distribution over the physical quantity is wrong. We call this failure physical misgeneralization, and develop an account of its mechanism. Using controlled synthetic tasks, we show that physical misgeneralization arises when local errors typical of the model class propagate through the physical measurement to shift the recovered distribution. We estimate these errors with a data deviation kernel, and we use it to predict which physical quantities gain or lose mass in both our synthetic and more applied maze navigation and double-pendulum motion tasks. Finally, our mechanistic interpretation helps identify which mitigation strategies are structurally promising, and we use it to propose a kernel-informed intervention.

---


### 37. [Robust Subspace-Constrained Quadratic Models for Low-Dimensional Structure Learning](https://arxiv.org/abs/2605.20300)

**<font color=#1a73e8>作者：</font>** Zheng Zhai, Xiaohui Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose a robust subspace-constrained quadratic model (SCQM) for learning low-dimensional structure from high-dimensional data. Building upon the subspace-constrained quadratic matrix factorization (SQMF) framework, the proposed model accommodates a broad class of noise distributions, including generalized Gaussian and radial Laplace models. This generalization enables reliable performance under both heavy-tailed and light-tailed noise, thereby substantially enhancing robustness across diverse data regimes. To efficiently address the resulting nonconvex optimization problem, we develop a gradient-based algorithm equipped with a backtracking line-search strategy that ensures stable and efficient convergence. In addition, we present a sensitivity analysis of the $\ell_p^p$ and $\ell_2$ loss functions, elucidating their distinct behaviors under varying noise characteristics. Extensive numerical experiments corroborate the theoretical analysis and demonstrate that the proposed approach consistently outperforms existing methods in terms of robustness and reconstruction accuracy.

---


### 38. [Co-Fusion4D: Spatio-temporal Collaborative Fusion for Robust 3D Object Detection](https://arxiv.org/abs/2605.20301)

**<font color=#1a73e8>作者：</font>** Wenxuan Li, Qin Zou, Shoubing Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In autonomous driving, 3D object detection is essential for accurate perception and reliable decision-making. However, object motion and ego-motion often induce cross-frame spatiotemporal inconsistencies in BEV-based detectors, leading to temporal BEV feature misalignment and degraded spatiotemporal consistency.
To address these challenges, we propose Co-Fusion4D, a unified framework that explicitly preserves cross-frame spatiotemporal consistency and suppresses temporal feature drift. Co-Fusion4D adopts a current-frame-centric strategy, treating the current frame as the primary source of information while selectively incorporating historical frames after spatiotemporal filtering and alignment. This dominant-complementary mechanism effectively mitigates cumulative alignment errors, suppresses noisy feature propagation, and exploits reliable temporal cues for a more consistent BEV representation.
In addition, Co-Fusion4D integrates a Dual Attention Fusion (DAF) module to further enhance spatiotemporal feature interaction. DAF jointly leverages intra-frame spatial attention and inter-frame temporal attention to adaptively align and fuse multi-frame features, emphasizing motion-consistent regions while suppressing spurious correlations. By departing from conventional uniform fusion paradigms, this design substantially improves the temporal stability and discriminative capability of BEV representations.
Extensive experiments on the nuScenes benchmark demonstrate that Co-Fusion4D achieves state-of-the-art performance, with 74.9% mAP and 75.6% NDS, without relying on test-time augmentation or external data.

---


### 39. [Neural Collapse by Design: Learning Class Prototypes on the Hypersphere](https://arxiv.org/abs/2605.20302)

**<font color=#1a73e8>作者：</font>** Panagiotis Koromilas, Theodoros Giannakopoulos, Mihalis A. Nicolaou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Supervised classification has a theoretical optimum, Neural Collapse (NC), yet neither of its two dominant paradigms reaches it in practice. Cross entropy (CE) leaves radial degrees of freedom unconstrained and converges to a degenerate geometry, while supervised contrastive learning (SCL) drives features toward NC during pretraining but discards this structure in a post hoc linear probing phase. We show that both paradigms are different appearances of the same method, prototype contrast on the unit hypersphere, and that closing the gap requires fixing each at its specific point of failure. From the CE side, we propose NTCE and NONL, two normalized losses that import contrastive optimization's missing ingredients into classifier learning: a large effective negative set and decoupled alignment and uniformity terms. From the SCL side, we prove that SCL's objective already optimizes throughout training for a principled classifier whose weights are the class mean embeddings, making linear probing both redundant and harmful. Empirically, on four benchmarks including ImageNet-1K, NTCE and NONL surpass CE accuracy, closely approximate NC ($\geq 95\%$), and match CE's converged NC on 4/5 metrics in under $7.5\%$ of its iterations, while SCL with fixed prototypes matches linear probing without the hours-long classifier training phase. The learned geometry yields $+5.5\%$ mean relative improvement in transfer learning, up to $+8.7\%$ under severe class imbalance, and lower mCE on ImageNet-C, recasting supervised learning as prototype learning on the hypersphere, with NC reached by design on both paths.

---


### 40. [AirfoilGen: A valid-by-construction and performance-aware latent diffusion model for airfoil generation](https://arxiv.org/abs/2605.20303)

**<font color=#1a73e8>作者：</font>** Zhijie Yang, Min Tang, Qiang Zou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Airfoil shape design is a fundamental task in aerospace engineering, with a direct impact on flight stability and fuel consumption. Deep learning has recently emerged as a promising tool for this task, but existing deep generative approaches remain limited in both geometric validity and physical controllability. They offer little control over the generated shapes, yielding invalid geometries, and they typically do not condition effectively on aerodynamic performance. To address these issues, this paper proposes AirfoilGen, a valid-by-construction and performance-aware latent diffusion model for airfoil. It first introduces a novel airfoil representation scheme, the circle sweeping representation, to constrain the generative process so that output shapes respect essential airfoil characteristics. It then enables explicit control over aerodynamic performance (e.g., lift and drag coefficients) by operating in a learned latent space: a transformer model encodes airfoil shapes into vector embeddings, and a conditional diffusion model denoises Gaussian noise into these latent embeddings while incorporating target aerodynamic performance. In addition, this paper presents a new dataset of over 200,000 airfoils, which is substantially larger than the widely used UIUC airfoil dataset (1,650 airfoils) and more suitable for training modern deep generative models. Experiments demonstrate that AirfoilGen enables airfoil generation with far greater geometric validity and aerodynamic performance controllability than previously achievable, with an average performance-conditioning accuracy of 98.41%.

---


### 41. [SDM: A Powerful Tool for Evaluating Model Robustness](https://arxiv.org/abs/2605.20308)

**<font color=#1a73e8>作者：</font>** Xinlei Liu, Tao Hu, Jichao Xie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gradient-based attacks are important methods for evaluating model robustness. However, since the proposal of APGD, it has been difficult for such methods to achieve significant breakthroughs. To achieve such an effect, we first analyze the issue of "high-loss non-adversarial examples" that degrades attack performance in previous methods, and prove that this issue arises from inappropriate objectives for adversarial example generation. Subsequently, we reconstruct the objective as "maximizing the difference between the non-ground-truth label probability upper bound and the ground-truth label probability", and proposes a novel and powerful gradient-based attack method named Sequential Difference Maximization (SDM). SDM establishes a three-layer optimization framework of "cycle-stage-step". It adopts the negative probability loss function and the Directional Probability Difference Ratio (DPDR) loss function in the initial and subsequent optimization stages, respectively, and approaches the ideal objective of adversarial example generation via stage-wise sequential optimization. Experiments demonstrate that compared with previous state-of-the-art methods, SDM not only achieves stronger attack performance but also exhibits superior cost-effectiveness. The code is available at this https URL.

---


### 42. [Tiny-Engram: Trigger-Indexed Concept Tables for Generative Vision](https://arxiv.org/abs/2605.20309)

**<font color=#1a73e8>作者：</font>** Runyuan Cai, Yiming Wang, Yu Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current personalization methods for generative vision models typically encode new concepts through continuous adapters or weight updates, yet provide limited control over whether and when a concept should be retrieved. In this work, we introduce Tiny-Engram, a compact trigger-indexed concept table that gives visual memories an explicit lexical address and activation boundary inside frozen image and video generators. Tiny-Engram parameterizes each concept as a small set of memory entries indexed by registered n-gram matches, which modulate text-encoder hidden states only within the matched trigger region. Outside this lexical support, the conditioning pathway is identical to that of the frozen base model. Across both single-encoder latent diffusion and multi-encoder diffusion-transformer backbones, this formulation binds a rare trigger phrase to a target identity while preserving compositional control from the surrounding prompt. We further evaluate the same table-based memory in a text-conditioned video generation setting, where the trigger path reliably alters the generated subject but fine-grained identity persistence across held-out video prompts remains limited. Taken together, these results suggest that small, explicitly addressed concept tables are a practical route to modular visual personalization, with strongest evidence in image generation. For video diffusion, the remaining gap points to a broader requirement: temporally stable identity likely depends on tighter coupling between text-side memory and the evolving visual state, motivating future work on memory injection beyond the text-conditioning interface.

---


### 43. [WaveGraphNet: Physics-Consistent Guided-Wave Damage Localization through Coupled Inverse-Forward Graph Learning](https://arxiv.org/abs/2605.20311)

**<font color=#1a73e8>作者：</font>** Vinay Sharma, Aditya Bharade, Olga Fink  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Guided-wave structural health monitoring enables damage localization in composite plates using sparse networks of bonded piezoelectric transducers. However, inferring the spatial location of defects from pitch-catch measurements remains weakly constrained when only a limited set of damage locations is available for training. As a result, models trained to predict defect locations may perform well on seen cases but generalize poorly to unseen regions of the structure.
This paper proposes WaveGraphNet, a coupled inverse--forward graph learning framework for guided-wave damage localization in Carbon Fiber Reinforced Polymer (CFRP) plates. The sensing layout is explicitly modeled as a graph, where transducers are represented as nodes and measured propagation paths define the graph connectivity. An inverse branch maps graph-structured spectral descriptors of differential guided-wave responses to a damage location, while a forward branch predicts the path-wise energy-deviation patterns of measured wave responses associated with a candidate location. During training, the forward branch serves as a physics-consistent regularizer, discouraging location estimates that are numerically plausible but inconsistent with the measured redistribution of wave-response energy. This coupling encourages agreement between inferred damage coordinates and the underlying wave propagation behavior.
Within this benchmark, the proposed graph-based formulation provides a strong localization model for sparse guided-wave sensing and demonstrates improved robustness in extrapolation to held-out regions compared to both non-graph and graph baselines. These results highlight the potential of coupled inverse-forward graph learning as an effective strategy for guided-wave localization under limited spatial coverage.

---


### 44. [Pramana: A Protocol-Layer Treatment of Claim Verification in Autonomous Agent Networks](https://arxiv.org/abs/2605.20312)

**<font color=#1a73e8>作者：</font>** Ravi Kiran Kadaboina  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous agents deployed in regulated domains must produce a verification artifact per consequential output: a record an auditor can re-execute offline, capturing what was claimed, against what source, by whom, when, and how. Production verification today splits into two unstandardized halves. Probabilistic verdict patterns (self-consistency voting, reviewer LLM ensembles) produce judgments, not artifacts. Artifact-producing patterns (RAG, tool-augmented traces, generator-verifier loops) produce vendor-specific records no external auditor can reconstruct without bespoke integration.
Pramana defines the missing wire format. Every consequential agent output is wrapped in a typed ClaimAttestation with one of four variants (measurement, inference, analogy, citation), each paired with a verify() operation against the recorded source. verify() is deterministic for MeasurementClaim and CitationClaim. For InferenceClaim and AnalogyClaim, determinism is conditional on the oracle (audit-replayable when LLM-backed). The four-way typology derives from classical Indian epistemology (pramana, valid means of knowledge).
The lifecycle is specified in TLA+ and exhaustively verified under TLC across three symmetry-reduced models: 38,563 distinct reachable states, zero invariant violations. The Python reference implementation passes 84 tests. An A2A and MCP wire-extension manifest layers three deployment-grade invariants: reachability, SLA bound, and offline re-verifiability.
An exploratory pilot (n=100, 2,275 reviewer calls) probes LLM-as-judge in code generation. The strongest observation is a 40-percentage-point raw FPR delta across corpora, consistent with reference-solution quality contributing significantly. The pilot does not validate Pramana on its own; the structural argument and formal verification do that.

---


### 45. [Less Data, Faster Training: repeating smaller datasets speeds up learning via sampling biases](https://arxiv.org/abs/2605.20314)

**<font color=#1a73e8>作者：</font>** Jingwen Liu, Ezra Edelman, Surbhi Goel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work investigates the ``small-vs-large gap'', where repeating on fewer samples can lead to compute saving during training compared to using a larger dataset. This is observed across algorithmic tasks, architectures and optimizers and cannot be explained using prior theory. We argue that the speedup comes from appropriate layer-wise growth enabled by sampling biases, which is more pronounced when the dataset size is smaller. We provide both theoretical analysis and empirical evidence from various interventions. Our results suggest that using a smaller dataset with more repetitions is not just a fallback strategy under data scarcity, but can be proactively leveraged as a favorable inductive biases for optimization, particularly in reasoning tasks.

---


### 46. [FullFlow: Upgrading Text-to-Image Flow Matching Models for Bidirectional Vision--Language Generation](https://arxiv.org/abs/2605.20316)

**<font color=#1a73e8>作者：</font>** Eric Tillmann Bill, Enis Simsar, Alessio Tonioni 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern text-to-image diffusion models encode rich visual priors, but expose them only through one-way text-conditioned generation. Existing unified vision--language models derived from them recover bidirectional capability through large-scale joint pretraining or substantial retraining of the text pathway, discarding the strong image prior the text-to-image backbone already encodes. We introduce \emph{FullFlow}, a parameter-efficient recipe that upgrades a pretrained rectified-flow text-to-image model into a bidirectional vision--language generator by training only LoRA adapters and lightweight text heads. FullFlow keeps images in their native continuous flow and adds a discrete insertion process for text. Separate image and text timesteps turn inference into trajectory selection in a two-dimensional generative space, enabling text$\rightarrow$image, image$\rightarrow$text, joint sampling, and partial-text prediction with a single backbone. On Stable Diffusion 3 (SD3) under an identical trainable-parameter count and matched LoRA rank, FullFlow improves text$\rightarrow$image FID from $62.7$ to $31.6$ and image$\rightarrow$text CIDEr from $2.0$ to $99.4$ over a LoRA equivalent following the previous SOTA formulation (Dual Diffusion) at matched wall-clock training time, while reducing peak VRAM from ${\sim}84$\,GB to ${\sim}38$\,GB and raising throughput by ${\sim}8\times$ on two RTX A5000 GPUs in under 24 hours, training only ${\sim}5\%$ of the backbone parameters. The same recipe transfers to FLUX.1-dev and supports downstream VQA through partial-text generation. These results show that strong bidirectional vision--language capability can be unlocked from pretrained text-to-image flow models without full multimodal pretraining.

---


### 47. [Causal Unlearning in Collaborative Optimization: Exact and Approximate Influence Reversal under Adversarial Contributions](https://arxiv.org/abs/2605.20341)

**<font color=#1a73e8>作者：</font>** Ali Mahdavi, Azadeh Zamanifar, Amirfarhad Farhadi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning systems must support data deletion requests to comply with privacy regulations, yet retraining from scratch after each deletion is computationally prohibitive. We present HF-KCU, a method that removes a client's contribution by approximating the influence function through conjugate gradient iterations in Krylov subspaces, reducing complexity from O(d^3) to O(kd) where k<<d.A causal weighting mechanism ensures that only clients holding the deleted data receive parameter updates, preventing spurious changes to unaffected clients. Our method is designed to handle bounded adversarial perturbations to the Hessian and gradient, providing graceful degradation under realistic threat models. We validate HF-KCU across convolutional (ResNet-18, SimpleCNN) and transformer (ViT-Lite) architectures on CIFAR-10, MNIST, and Fashion-MNIST. On CIFAR-10 under Dirichlet (alpha=0.5) partitioning, HF-KCU achieves 47.75 times speedup over retraining while maintaining test accuracy within 0.60% of the rational baseline(71.16 vs 71.76 %). Membership inference attacks on the forget set yield success rates of 0.499 matching the retrained model and confirming effective privacy restoration. We provide convergence guarantees showing that the Krylov approximation error decreases as O((k ^1/2-1)/(k^1/2+1)) where k is the Hessian condition number. The causal weighting mechanism ensures surgical updates, where only clients holding deleted data are modified, preserving model quality for unaffected participants and avoiding the instability of gradient-based approaches in asynchronous federated settings. This design provides interpretability as each update is directly traceable to the influence of the deleted data. The method's efficiency and precision make it suitable for production federated systems where deletion requests arrive asynchronously and computational budgets are constrained.

---


### 48. [Symmetrization of Loss Functions for Robust Training of Neural Networks in the Presence of Noisy Labels](https://arxiv.org/abs/2605.20347)

**<font color=#1a73e8>作者：</font>** Alexandre Lemire Paquin, Brahim Chaib-Draa, Philippe Giguère  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Labeling a training set is often expensive and susceptible to errors, making the design of robust loss functions for label noise an important problem. The symmetry condition provides theoretical guarantees for robustness to such noise. In this work, we study a symmetrization method arising from the unique decomposition of any multi-class loss function into a symmetric component and a class-insensitive term. In particular, symmetrizing the cross-entropy loss leads to a linear multi-class extension of the unhinged loss. Unlike in the binary case, the multi-class version must have specific coefficients in order to satisfy the symmetry condition. Under suitable assumptions, we show that this multi-class unhinged loss is the unique convex multi-class symmetric loss. We also show that it has a fundamental local role: the linear approximation of any symmetric loss around score vectors with equal components is equivalent to the multi-class unhinged loss. We then introduce SGCE and alpha-MAE, two loss functions that interpolate between the multi-class unhinged loss and the Mean Absolute Error while allowing control of the beta-smoothness of the loss. Experiments on standard noisy-label benchmarks show competitive performance compared with existing robust loss functions.

---


### 49. [Synchronization and Turn-Taking in Full-Duplex Speech Dialogue Models](https://arxiv.org/abs/2605.20356)

**<font color=#1a73e8>作者：</font>** Pablo Riera, Pablo Brusco, Cristina Kuo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Full-duplex spoken dialogue models (SDMs) can listen and speak simultaneously, enabling interaction dynamics closer to human conversation than turn-based systems. Inspired by neural coupling in human communication, we study how such models coordinate their internal representations during interaction. We simulate full-duplex dialogues between two instances of the pretrained \textit{Moshi} model under controlled conditions, manipulating channel noise and decoding bias. Synchronization is measured using Centered Kernel Alignment (CKA) across temporal lags, while anticipatory turn-taking cues are probed from delayed internal activations using causal LSTM models, from both speaker and listener perspectives. We find strong representational synchronization under no noise conditions, peaking near zero lag and degrading with noise, and we show that internal states encode anticipatory information that supports turn-taking prediction ahead of time.

---


### 50. [Consistently Informative Soft-Label Temperature for Knowledge Distillation](https://arxiv.org/abs/2605.20357)

**<font color=#1a73e8>作者：</font>** Hoang-Chau Luong, Nghia Van Vo, Kaiqi Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation (KD) transfers knowledge from a high-capacity teacher to a compact student by matching their predictive distributions, with temperature scaling serving as a central mechanism for smoothing teacher predictions and exposing informative "dark knowledge" beyond the hard label. However, the standard fixed-temperature design is inherently sample-agnostic. Since samples differ in logit scale and learning difficulty, a single global temperature produces teacher soft labels with highly inconsistent entropy: some predictions remain overly sharp and provide limited inter-class information, whereas others become over-smoothed and lose class-discriminative information. Moreover, sharing the same temperature between teacher and student further imposes rigid logit-scale alignment despite their capacity mismatch. To address these limitations, we propose CIST (Consistently Informative Soft-label Temperature), which assigns separate sample-wise adaptive temperatures to the teacher and student. This design produces consistently informative teacher soft labels while relaxing rigid teacher--student logit-scale matching. It also reweights the distillation objective according to teacher confidence and student learning difficulty. Theoretically, we show that teacher-label entropy is largely governed by the ratio between the maximum teacher logit and the temperature, providing a principled basis for adaptive smoothing. Empirically, CIST mitigates the inconsistency induced by fixed temperature, and experiments on both vision and language distillation tasks show consistent improvements over standard KD and strong baselines with negligible computational overhead.

---


> [!TIP]
> 当前位于：**1-50**（第 1/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-352](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
