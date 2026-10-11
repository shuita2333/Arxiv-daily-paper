# 🔐 大模型安全相关研究 | 2026年10月12日

> 本类共 **9** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [When Routing Reveals Membership: Privacy Leakage from MoE Router Telemetry](https://arxiv.org/abs/2610.10616)

**<font color=#1a73e8>作者：</font>** Yixin Tan, Jiayang Liu, Lu Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) language models produce routing information during inference that may be logged or exposed for monitoring, debugging, load analysis, and safety auditing. Unlike ordinary model outputs, this telemetry reveals a view of the model's internal computation, raising a privacy question: can it reveal whether an example was used to fine-tune the deployed model? We introduce a router-augmented membership inference attack that combines conventional output-side signals with aggregated routing features and applies a membership classifier learned from independently fine-tuned shadow models to the target model. Across three MoE architectures and three data domains, router telemetry consistently improves membership inference over a strong output-signal ensemble, increasing TPR at 1\% FPR by 2.7--9.4 percentage points across all nine settings. The leakage persists across full fine-tuning, frozen-router training, LoRA, and instruction tuning, and remains observable with only discrete expert selections, restricted telemetry, or a single shadow model. Mechanistic analysis further shows that the leakage does not require router-specific memorization: fine-tuning introduces membership information into hidden representations, while the router exposes a projection of this signal even when its parameters are frozen. Perturbing the telemetry reduces this additional leakage only as its fidelity degrades. Our results show that router telemetry can turn an operational signal into an additional privacy surface for fine-tuned MoE models.

---


### 2. [Safe at One Loop, Risky at Another: Aligning Safety Across Recurrent Depths in Looped Language Models](https://arxiv.org/abs/2610.10625)

**<font color=#1a73e8>作者：</font>** Yi Wang, Xiuyuan Qi, Dongqi Han 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Looped Language Models (LoopLMs) provide a parameter efficient approach to scaling model capabilities through repeated use of shared parameters across recurrent steps. Since each recurrent depth can be read out independently, a single LoopLM exposes a broader output space across inference depths, raising an important question: whether safety is preserved throughout recurrent computation. Prior evaluations suggest that deeper recurrence can improve safety on harmful queries, but robustness under jailbreak attacks remains unclear. We therefore conduct a comprehensive safety evaluation of LoopLMs under jailbreak attacks targeting different recurrent depths. We find that attack success can increase at deeper inference depths, the same query can elicit different safety behaviors across depths, and attacks constructed against one depth can transfer to others. Moreover, SFT and preference alignment do not eliminate these safety gaps, motivating an alignment method designed for LoopLMs. We introduce SafeBridge, which combines lightweight depth specific control of shared recurrent layers, selective state bridging, and joint safety supervision across recurrent depths. Across model scales, multiple attack methods, and safety benchmarks, SafeBridge substantially reduces attack success for both matched-depth and cross-depth attacks. It also improves general utility over the vanilla models while maintaining comparable over-refusal behavior. Our results show that the safety of a LoopLM cannot be inferred from a single recurrent depth, motivating safety alignment across recurrent computation. Our code and model checkpoints will be released upon acceptance.

---


### 3. [BRANCH: Bypassing Multi-Scanner AI Guardrails](https://arxiv.org/abs/2610.10742)

**<font color=#1a73e8>作者：</font>** William Hackett, Peter Garraghan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI systems increasingly rely on Large Language Models (LLMs) as core reasoning engines, making them targets for prompt injection and jailbreaks. Guardrails monitor and validate model inputs and outputs, yet their isolated, task-focused detection leaves gaps in their classification making them susceptible to bypasses. In response, guardrail systems formed by multiple scanners have emerged that collaboratively detect different types of malicious instructions, whereby shared latent representations across classification boundaries render established bypassing techniques ineffective. We propose BRANCH, a bypassing methodology designed for multi-scanner guardrail systems. Our method leverages a branching tree search approach that dynamically applies adversarial perturbation against individual scanners, with subsequent perturbation optimization and technique selection based on overall improvement across all guardrail system scanners, effectively decoupling bypass evaluation from attack signal optimization. Our findings demonstrate that BRANCH achieves 100% attack success rate across 6 guardrail systems in 120 scenarios with 72% fewer queries and 4.5x reduced wallclock time compared to established techniques, while preserving semantic meaning within the bypass. We also show how bypasses generated by BRANCH transfer to 29 unseen guardrails, including 8 commercial black-box guardrails, improving attack success in some cases up to 100% with no additional optimization.

---


### 4. [False Claims, Credible Images: A Red-Teaming Benchmark for Commercial Image Generators](https://arxiv.org/abs/2610.11112)

**<font color=#1a73e8>作者：</font>** Zeyu Ye, Yanchun Li, Sibei He 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Image-generation models can now produce text-rich, natural-looking visual artifacts that are hard to distinguish from real-world evidence, such as news reports and textbook pages. Yet, the same capability introduces a new risk: these models can just as easily fabricate visual misinformation. Even commercial models (e.g., GPT-Image-2) readily produce it. Curiously, we find that these models can recognize a claim as false when asked, yet still render that very claim as credible visual evidence. This discrepancy points to a blind spot in current alignment: safeguards judge what an image shows, not what it asserts; however, existing red-teaming benchmarks target conventional harmful content, such as violent or explicit imagery, and say little about where the alignment boundaries lie for visual misinformation, especially in commercial models. To fill this gap, we introduce EpiReal-Bench, the first systematic benchmark for evaluating visual misinformation risks in commercial image generators, comprising 10k false-claim prompts and 10k corresponding generated images that span 10 real-world claim categories and 10 credible visual formats. We further introduce EpiReal-Attack, a skill-guided black-box optimization framework that uses Pareto-based selection and multimodal feedback to identify commands that bypass alignment safeguards while preserving visual realism, textual legibility, and semantic fidelity. Experiments on four commercial models reveal that more than 70% of false-claim prompts elicit images that faithfully depict the corresponding misinformation, and EpiReal-Attack pushes this rate to 95%. Most worryingly, these models are only a click away, and their outputs are cheap to spread yet hard to disbelieve, leaving this dimension of alignment largely unguarded.

---


### 5. [Safe, Persistent, and Evolving Agent Harness for Understanding Partially Observable Worlds](https://arxiv.org/abs/2610.11552)

**<font color=#1a73e8>作者：</font>** Yisen Gao, Yue Guo, Qing Zong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents can invoke tools fluently, but enterprise workflows demand more than selecting the right tools: actions must strictly comply with organizational policies, tool feedback often conceals hidden side effects under partial observability, and long-horizon tasks require persistent state tracking across multiple records. To address these challenges, we introduce E-Ledger, a multi-agent harness for safe and persistent execution. E-Ledger employs a code approval layer that checks every proposed action against policy before execution, and maintains a world ledger of verified hidden rules alongside evidence-backed dynamic state. Because hidden rules are typically unknown a priori, we further propose WorldAbduct, an abductive, world-model-driven harness evolution framework. WorldAbduct diagnoses execution trajectories across four complementary views (state consistency, world-observation gap, policy-gate correctness, and goal judgment) to hypothesize latent rules, and verifies them through targeted abductive interactions before integrating them into the ledger. On the enterprise benchmark World of Workflows, E-Ledger with WorldAbduct improves safe task completion across four LLM backbones, outperforming the strongest evolution baseline by 5--15 percentage points. Experiments in ScienceWorld and DiscoveryWorld further show that abductive harness evolution carries over to scientific environments. Our code is available at this https URL.

---


### 6. [LTBD: Learnable Trust-Boundary Delimiters for Prompt Injection Defense](https://arxiv.org/abs/2610.11634)

**<font color=#1a73e8>作者：</font>** Luman Zhao, Minghui Xu, Yue Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) perform remarkably well on complex tasks, yet remain highly vulnerable to prompt injection attacks, where malicious instructions embedded in external data can override user intent. Existing defenses remain limited by model fine-tuning requirements, vulnerability to adaptive attacks, or reliance on brittle handcrafted prompts. We argue that a fundamental source of this vulnerability is the lack of an explicit representation of trust provenance. To address this, we introduce Learnable Trust-Boundary Delimiters (LTBD), a lightweight defense that explicitly encodes trust boundaries in the input while keeping the LLM parameters unchanged. LTBD uses a small number of learnable delimiters to distinguish trusted user instructions from untrusted external data, enabling the model to better respect the intended trust hierarchy. Experimental results show that LTBD substantially outperforms inference-time defenses and performs competitively with training-based approaches, while preserving benign-task utility and introducing negligible inference overhead. In particular, LTBD achieves 0.00% ASR on AlpacaFarm and only 0.11-0.19% ASR on TaskTracker. LTBD also remains effective under adaptive attacks, where adversaries have full knowledge of the defense and explicitly attempt to bypass it.

---


### 7. [Same Outcome, Different Evidence: Intent Recovery in LLM Safety Evaluation](https://arxiv.org/abs/2610.11766)

**<font color=#1a73e8>作者：</font>** Haitong Jiang, Chunlin Liu, Sihan Tang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safety evaluations of large language models commonly summarize harmful-output behavior with attack success rate (ASR). Yet the same non-harmful outcome can arise for very different reasons. A model may recover a harmful task and refuse it, fail to recover the task, or respond to something else entirely. Distinguishing these cases becomes especially important under intent-obscuring prompts, where a low ASR does not reveal whether the evaluated task was actually engaged. To make this distinction explicit, we pair ASR with operative understanding rate (UR), which measures whether a response both identifies the evaluated task and treats it as the task to be answered. Across interfaces, this paired view reveals substantial variation hidden by ASR: similar ASR values can correspond to sharply different recovery rates. Controlled English reconstructions show that recovery consistently improves as compressed prompts become more explicit, whereas ASR does not follow the same pattern. A complementary contrast comes from FormalLogic, where high recovery can still coincide with frequent harmful assistance. Together, these results show that non-harmful outcomes are not equally informative about model safety, motivating the joint reporting of intent recovery and ASR in LLM safety evaluation. Code and experiment inputs are available at this https URL.

---


### 8. [ReSI: Recursive Safety Improvement toward Resistant and Resilient AI](https://arxiv.org/abs/2610.12233)

**<font color=#1a73e8>作者：</font>** Jingnan Zheng, Dongcheng Zhang, Yi Zhang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recursive self-improvement, the participation of AI systems in improving their own capabilities, is beginning to move from theoretical prospect to practice, posing both challenges and opportunities for safety alignment. Models evolve through frequent updates, and their safety alignment requires continual adaptation to each new checkpoint. Meanwhile, with evolving red-teaming methods exposing new vulnerabilities, safety improvement for each checkpoint needs to mitigate exposed vulnerabilities and generalize to risks not yet revealed. Following R$^2$AI, we term these goals resistance to known threats and resilience to unforeseen risks. Recursive self-improvement, in turn, inspires an approach to both goals: safety alignment could likewise advance through successive rounds of evaluation and update. We therefore introduce ReSI, a recursive safety improvement framework that implements this approach through automated research. In each round, ReSI applies diverse red-teaming methods to identify vulnerabilities in the current target model, develops training recipes, and promotes the update with the largest safety gain among those passing a Pareto gate on capability retention as the next target model. Across four dense and mixture-of-experts models, ReSI matches or exceeds evaluated frontier models on in-distribution and out-of-distribution safety benchmarks, and outperforms alignment baselines on nearly all safety evaluations while largely preserving general capabilities. In particular, ReSI reduces the mean X-Teaming attack success rate across the four models from 86.01% to 31.45%, well below GPT-5.6-Luna's leading frontier result of 56.69%, indicating stronger resilience to attacks unseen during training. These findings support recursive safety improvement as a practical path toward resistant and resilient AI.

---


### 9. [From Reactive Containment to Proactive Assurance: Lessons from OpenAI, Anthropic, and Google Agent Security Incidents](https://arxiv.org/abs/2610.12463)

**<font color=#1a73e8>作者：</font>** Abbas Raftari  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In 2026, cybersecurity evaluations involving OpenAI, Anthropic, and Google agents reached real systems outside their authorized test scope. The paths were different. OpenAI agents exploited research infrastructure, coordinated across runs, and compromised parts of Hugging Face's production environment. Anthropic reported cases in which a misconfigured third-party environment exposed real systems to agents pursuing simulated cyber tasks. In a separately reported evaluation, Google's Gemini accessed three real organizations through an unintended internet route; Google stated that the model stopped in all three instances. Taken together, the cases show why an evaluation cannot rely on an assumed boundary. That boundary must be verified while the agent is operating. This comparative instrumental case study develops a Proactive Agent Security Assurance Cycle (PASAC) and a five-layer Boundary Assurance Stack. The framework combines risk-tiered task design, executable scope contracts, pre-run validation, least-capability access, independent egress enforcement, credential restrictions, cross-run monitoring, automatic stop conditions, and evidence-based reauthorization. A leading-indicator model, nine design propositions, and seven falsifiable hypotheses turn these lessons into a testable research program. Because the public Gemini record is limited to attributed statements and journalism, its detailed causal mechanism remains provisional. The central conclusion is straightforward: proactive agent security requires continuous assurance across the full execution system, not confidence in any single sandbox or safeguard.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
